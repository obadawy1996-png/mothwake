#!/usr/bin/env python3
"""MOTHWAKE analytics: ingest real platform exports, cohort analysis, HTML dashboard.

  analytics.py ingest <platform> <export.csv>   platform: youtube|tiktok|instagram|facebook
  analytics.py dashboard [--db PATH] [--out PATH]
  analytics.py cohorts

Only REAL exports go in analytics/data.db (YouTube Studio "Advanced mode → Export",
TikTok/Instagram/Facebook insights exports, or connector pulls). Nothing is estimated.
Column names are mapped flexibly; unmapped KPIs stay empty and show as "no data".
"""
from __future__ import annotations

import argparse
import csv
import html
import sqlite3
import statistics
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "analytics" / "data.db"

KPIS = ["views", "engaged_views", "shown_in_feed", "viewed_vs_swiped_pct", "impressions", "ctr_pct",
        "avg_view_duration_s", "avg_pct_viewed", "watch_hours", "likes", "comments", "shares",
        "subscribers_gained", "returning_viewers", "reach", "followers_gained", "revenue"]
ALIASES = {  # lowercase source header → KPI
    "views": "views", "engaged views": "engaged_views", "shown in feed": "shown_in_feed",
    "stayed to watch (%)": "viewed_vs_swiped_pct", "viewed vs. swiped away (%)": "viewed_vs_swiped_pct",
    "impressions": "impressions", "impressions click-through rate (%)": "ctr_pct",
    "average view duration": "avg_view_duration_s", "average percentage viewed (%)": "avg_pct_viewed",
    "watch time (hours)": "watch_hours", "likes": "likes", "comments added": "comments", "comments": "comments",
    "shares": "shares", "subscribers gained": "subscribers_gained", "subscribers": "subscribers_gained",
    "returning viewers": "returning_viewers", "reach": "reach", "accounts reached": "reach",
    "followers gained": "followers_gained", "new followers": "followers_gained",
    "estimated revenue (usd)": "revenue", "your estimated revenue (usd)": "revenue",
    "video title": "title", "content": "title", "title": "title", "video": "video_id", "content id": "video_id",
    "video publish time": "published", "publish time": "published", "duration": "duration_s",
}


def conn(db=DB):
    db.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(db)
    c.execute(f"""CREATE TABLE IF NOT EXISTS metrics(platform TEXT, video_id TEXT, title TEXT, published TEXT,
        duration_s REAL, format TEXT, source_file TEXT, ingested TEXT, {', '.join(k + ' REAL' for k in KPIS)},
        PRIMARY KEY(platform, video_id, source_file))""")
    return c


def num(v):
    if v is None or str(v).strip() in ("", "-", "—"):
        return None
    s = str(v).replace(",", "").replace("%", "").replace("$", "").strip()
    if ":" in s:  # h:mm:ss or m:ss
        parts = [float(p) for p in s.split(":")]
        return sum(p * 60 ** i for i, p in enumerate(reversed(parts)))
    try:
        return float(s)
    except ValueError:
        return None


def ingest(platform, path, db=DB):
    c = conn(db)
    n = 0
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            rec = {}
            for k, v in row.items():
                key = ALIASES.get((k or "").strip().lower())
                if key:
                    rec[key] = v
            vid = rec.get("video_id") or rec.get("title")
            if not vid or str(vid).lower() == "total":
                continue
            dur = num(rec.get("duration_s"))
            fmt = "short" if (dur is not None and dur <= 180 and platform == "youtube") or platform != "youtube" else "long"
            vals = [num(rec.get(k)) for k in KPIS]
            c.execute(f"INSERT OR REPLACE INTO metrics VALUES({','.join('?' * (8 + len(KPIS)))})",
                      (platform, str(vid), rec.get("title"), rec.get("published"), dur, fmt, Path(path).name,
                       datetime.now(timezone.utc).isoformat(timespec="seconds"), *vals))
            n += 1
    c.commit()
    print(f"ingested {n} rows from {path} ({platform})")


def cohorts(db=DB):
    """Return per (platform, format, duration band) medians — compare like with like."""
    c = conn(db)
    rows = c.execute("SELECT platform, format, duration_s, views, avg_pct_viewed, subscribers_gained FROM metrics").fetchall()
    out = {}
    for p, f, d, v, apv, sg in rows:
        band = "unknown" if d is None else ("<30s" if d < 30 else "30-60s" if d <= 60 else "1-3m" if d <= 180
                                            else "3-8m" if d <= 480 else "8-14m" if d <= 840 else "14m+")
        out.setdefault((p, f, band), []).append((v, apv, sg))
    res = {}
    for k, vals in out.items():
        def med(i):
            xs = [x[i] for x in vals if x[i] is not None]
            return statistics.median(xs) if xs else None
        res[k] = {"n": len(vals), "median_views": med(0), "median_avg_pct_viewed": med(1), "median_subs": med(2)}
    return res


def fmt(v, pct=False):
    if v is None:
        return '<span class="nd">no data</span>'
    return f"{v:,.1f}%" if pct else f"{v:,.0f}"


def dashboard(db=DB, out=ROOT / "analytics" / "dashboard.html"):
    c = conn(db)
    total = c.execute("SELECT COUNT(*) FROM metrics").fetchone()[0]
    plat = c.execute("SELECT platform, COUNT(*), SUM(views), SUM(shares), SUM(comments), SUM(subscribers_gained), "
                     "SUM(followers_gained), AVG(avg_pct_viewed), SUM(revenue) FROM metrics GROUP BY platform").fetchall()
    vids = c.execute("SELECT platform, format, title, duration_s, views, avg_pct_viewed, viewed_vs_swiped_pct, ctr_pct, "
                     "subscribers_gained, shares FROM metrics ORDER BY views DESC LIMIT 50").fetchall()
    coh = cohorts(db)
    e = html.escape
    rows_p = "".join(f"<tr><td>{e(p)}</td><td>{n}</td><td>{fmt(v)}</td><td>{fmt(s)}</td><td>{fmt(cm)}</td>"
                     f"<td>{fmt((sg or 0) + (fg or 0) if (sg is not None or fg is not None) else None)}</td>"
                     f"<td>{fmt(apv, True)}</td><td>{fmt(rv)}</td></tr>"
                     for p, n, v, s, cm, sg, fg, apv, rv in plat)
    rows_c = "".join(f"<tr><td>{e(p)}</td><td>{e(f)}</td><td>{e(b)}</td><td>{d['n']}</td><td>{fmt(d['median_views'])}</td>"
                     f"<td>{fmt(d['median_avg_pct_viewed'], True)}</td><td>{fmt(d['median_subs'])}</td></tr>"
                     for (p, f, b), d in sorted(coh.items()))
    rows_v = "".join(f"<tr><td>{e(p)}</td><td>{e(f)}</td><td>{e(t or '')}</td><td>{fmt(d)}</td><td>{fmt(v)}</td>"
                     f"<td>{fmt(a, True)}</td><td>{fmt(sw, True)}</td><td>{fmt(ct, True)}</td><td>{fmt(sg)}</td>"
                     f"<td>{fmt(sh)}</td></tr>" for p, f, t, d, v, a, sw, ct, sg, sh in vids)
    empty = "" if total else ('<p class="banner">No platform data has been ingested yet. Channels are not live. '
                              'Every panel shows "no data" until real exports are added.</p>')
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MOTHWAKE Analytics</title><style>
:root{{--bg:#090A0D;--panel:#16151B;--text:#E7E2D8;--muted:#77717D;--gold:#B89A68;--line:#25232B}}
body{{margin:0;background:var(--bg);color:var(--text);font:15px/1.5 Inter,system-ui,sans-serif;padding:24px 16px}}
h1{{font:600 26px Georgia,serif;letter-spacing:.2em;color:var(--gold);margin:0 0 4px}}h2{{font-size:15px;color:var(--gold);margin:28px 0 8px;letter-spacing:.08em;text-transform:uppercase}}
.sub{{color:var(--muted);margin:0 0 16px}}.wrap{{max-width:1200px;margin:auto}}.tbl{{overflow-x:auto;background:var(--panel);border-radius:8px}}
table{{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}}th,td{{padding:8px 10px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap}}
th:first-child,td:first-child,td:nth-child(3){{text-align:left}}th{{color:var(--muted);font-weight:600;font-size:12px;text-transform:uppercase}}
.nd{{color:var(--muted);font-style:italic}}.banner{{border:1px solid var(--gold);padding:12px;border-radius:8px;color:var(--gold)}}
</style></head><body><div class="wrap"><h1>MOTHWAKE</h1><p class="sub">Cross-platform performance · {total} video-rows · generated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC · real exports only</p>{empty}
<h2>By platform</h2><div class="tbl"><table><tr><th>Platform</th><th>Videos</th><th>Views</th><th>Shares</th><th>Comments</th><th>Subs/followers gained</th><th>Avg % viewed</th><th>Revenue</th></tr>{rows_p}</table></div>
<h2>Cohorts (compare like with like)</h2><div class="tbl"><table><tr><th>Platform</th><th>Format</th><th>Duration band</th><th>n</th><th>Median views</th><th>Median % viewed</th><th>Median subs</th></tr>{rows_c}</table></div>
<h2>Videos (top 50 by views)</h2><div class="tbl"><table><tr><th>Platform</th><th>Format</th><th>Title</th><th>Duration s</th><th>Views</th><th>Avg % viewed</th><th>Viewed vs swiped</th><th>CTR</th><th>Subs</th><th>Shares</th></tr>{rows_v}</table></div>
<p class="sub">Views are not equal across platforms: monetization value differs by platform, format and region. See research/PLATFORM_MONETIZATION.md.</p></div></body></html>"""
    out.write_text(page)
    print("dashboard:", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["ingest", "dashboard", "cohorts"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--db", type=Path, default=DB)
    ap.add_argument("--out", type=Path, default=ROOT / "analytics" / "dashboard.html")
    a = ap.parse_args()
    if a.cmd == "ingest":
        ingest(a.args[0], a.args[1], a.db)
    elif a.cmd == "dashboard":
        dashboard(a.db, a.out)
    else:
        for k, v in sorted(cohorts(a.db).items()):
            print(k, v)
