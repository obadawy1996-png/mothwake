#!/usr/bin/env python3
"""YT_SEED_SHORTS.csv: first 10 Shorts in YouTube's Shorts shelf for each seed search
(sp=EgIYAQ%3D%3D, under 4 min, relevance order). views_rounded comes from the shelf
accessibility text (rounded by YouTube). Exact views / publish date / length / likes /
channel come from the public /shorts/<id> page when YouTube served it (else 'unknown').
Also writes per-seed summary to stdout."""
import csv, json, re, statistics, collections, datetime as dt
def av(t):
    m = re.search(r", ([\d\.,]+) (thousand|million|billion)? ?views", t or "")
    return float(m.group(1).replace(',', '')) * {'thousand': 1e3, 'million': 1e6, 'billion': 1e9}.get(m.group(2), 1) if m else None
def title_of(t):
    return re.sub(r", [\d\.,]+ (thousand |million |billion )?views - play Short$", "", t or "")
search = json.load(open("raw/yt_seed_search_2026-11-19.json"))
det = {d["id"]: d for d in json.load(open("raw/yt_seed_shorts_detail_2026-11-19.json")) if d.get("title")}
for d in json.load(open("raw/yt_shorts_search_resolved_2026-11-19.json")):
    if d.get("title"): det.setdefault(d["id"], d)
byq = collections.defaultdict(list)
for x in search:
    if x.get("shelf") and x.get("id"): byq[x["query"]].append(x)
TODAY = dt.date(2026, 11, 19)
rows, summ = [], []
for q, xs in byq.items():
    vals, recent = [], []
    for rank, x in enumerate(xs[:10], 1):
        d = det.get(x["id"], {})
        v = av(x["accessibility"]); vals.append(v or 0)
        pub = (d.get("publish") or "")[:10]
        age = (TODAY - dt.date.fromisoformat(pub)).days if pub else None
        if age is not None and age <= 90: recent.append(int(d["views"]))
        rows.append([q, rank, x["id"], d.get("title") or title_of(x["accessibility"]), re.sub(r"\s+", " ", (d.get("author") or "unknown")).split(" ▷")[0].strip(),
                     int(v) if v else "unknown", d.get("views") or "unknown", pub or "unknown",
                     age if age is not None else "unknown", d.get("length_s") or "unknown",
                     d.get("likes") or "unknown", d.get("comments") or "unknown", x["fetched_at"][:10],
                     "youtube.com/results sp=EgIYAQ (shelf) + /shorts/<id> page"])
    summ.append((q, statistics.median(vals), max(vals), len(recent), statistics.median(recent) if recent else None))
with open("YT_SEED_SHORTS.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["seed", "shelf_rank", "video_id", "title", "channel", "views_rounded_shelf", "views_exact",
                "publish_date", "age_days", "length_s", "likes", "comments", "date_checked", "source"])
    w.writerows(rows)
for s in summ: print(s)
json.dump(summ, open("raw/seed_summary_2026-11-19.json", "w"), indent=1)
