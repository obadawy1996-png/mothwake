#!/usr/bin/env python3
"""Build GOOGLE_TRENDS.csv from raw Trends JSON (no new requests).

Columns
- mean: mean of the term's 0-100 index over the window, inside its 5-term comparison group
  (values are relative to the group's peak, not absolute volume).
- index_vs_anchor: term mean / mean of the anchor term "analog horror" in the same
  group, geo, property and timeframe. Every group contains the anchor, so this ratio is
  comparable ACROSS groups. "n/a" if the anchor mean is 0.
- recent_vs_prior: 12-month = mean of last 4 complete weeks / mean of the 4 weeks before
  (partial week dropped). 7-day = mean of the last 48 complete hourly points / mean of
  the preceding points. "n/a" when the prior mean is 0.
- rising_related / top_related: US only, 12 months, from /widgetdata/relatedsearches
  (filled for the US rows of the matching property; blank elsewhere = not requested).
"""
import csv
import json
import sys

RAW = sys.argv[1]
OUT = sys.argv[2]
ANCHOR = "analog horror"
ml = json.load(open(RAW + "/gtrends_multiline_2026-11-19.json"))
try:
    rel = json.load(open(RAW + "/gtrends_related_2026-11-19.json"))
except FileNotFoundError:
    rel = []
relmap = {(r["term"], r["property"]): r for r in rel}


def mean(xs):
    return sum(xs) / len(xs) if xs else 0.0


rows = []
for rec in ml:
    tl = [p for p in (rec["timeline"] or []) if not p.get("isPartial")]
    if not tl:
        for k in rec["keywords"]:
            rows.append([k, rec["geo"], rec["property"], rec["timeframe"], rec["group"],
                         "unknown", "unknown", "unknown", "", "", rec["fetched_at"][:10],
                         "no data returned"])
        continue
    ai = rec["keywords"].index(ANCHOR)
    amean = mean([p["value"][ai] for p in tl])
    for i, k in enumerate(rec["keywords"]):
        vals = [p["value"][i] for p in tl]
        m = mean(vals)
        if rec["timeframe"] == "today 12-m":
            recent, prior = vals[-4:], vals[-8:-4]
        else:
            recent, prior = vals[-48:], vals[:-48]
        pm = mean(prior)
        rvp = round(mean(recent) / pm, 2) if pm else "n/a"
        r = relmap.get((k, rec["property"])) if rec["geo"] == "US" and rec["timeframe"] == "today 12-m" else None
        rising = "; ".join(f'{x["query"]} ({x["value"]})' for x in ((r or {}).get("rising") or [])[:8]) if r else ""
        top = "; ".join(f'{x["query"]} ({x["value"]})' for x in ((r or {}).get("top") or [])[:5]) if r else ""
        if r and r.get("rising") is None:
            rising = "not obtained"
        rows.append([k, rec["geo"], rec["property"], rec["timeframe"], rec["group"], round(m, 1),
                     round(m / amean, 3) if amean else "n/a", rvp, rising, top,
                     rec["fetched_at"][:10], f"{len(vals)} points; zero points={vals.count(0)}"])

with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["term", "geo", "property", "timeframe", "comparison_group", "mean",
                "index_vs_anchor_analog_horror", "recent_vs_prior", "rising_related_US_12m",
                "top_related_US_12m", "date_checked", "notes"])
    w.writerows(rows)
print(len(rows))
