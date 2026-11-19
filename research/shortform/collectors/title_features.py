#!/usr/bin/env python3
"""Title-feature lift over RSS Shorts (exact views, last <=15 uploads per channel).
lift = Short views / median views of that channel's RSS Shorts. Core animated-horror channels only."""
import json, re, statistics, html, sys
EXCLUDE = {"Serial Clips", "Mr.spinechill", "ParaBlack", "Velvet Horror", "Studio Wrong", "Transfuse",
           "amandaprescottfx", "HIGuacamole", "Lumpy Touch", "Doctor Nowhere", "Disturbia Files", "The Face of Horror"}
FEAT = {
  "conditional_if (If you/your...)": r"^\W*(if|in this town, if|in this town, when|when)\b",
  "rule_word (rule/rules)": r"\brules?\b",
  "imperative_never/dont": r"\b(never|don.?t|do not)\b",
  "time_3am_midnight_night": r"\b(3 ?am|midnight|at night|night shift)\b",
  "family_member (mom/dad/sister...)": r"\b(mom|mum|dad|mother|father|sister|brother|grandma|girlfriend)\b",
  "door": r"\bdoors?\b",
  "explicit_choice (or / which / would you / pick / choose)": r"(\bor\b.*\?|\bwhich\b|would you|\bpick\b|\bchoose\b|\byou decide\b)",
  "question_mark": r"\?",
  "series_part (Part N)": r"\bpart\s*\d+|\bpt\.?\s*\d+|\b\d+\s*$",
  "mimic/imposter": r"\b(mimic|imposter|not my|not your|isn.?t)\b",
  "survival_word (survive/apocalypse/zombie/bunker)": r"\b(surviv\w*|apocalypse|zombie\w*|bunker)\b",
  "analog_horror_tag": r"analog horror",
  "backrooms/liminal": r"backrooms|liminal",
  "emoji_present": r"[\U0001F300-\U0001FAFF☀-➿]",
  "ellipsis_cliffhanger (…/...)": r"(\.\.\.|…)",
}
data = json.load(open("raw/yt_channels_rss_2026-11-19.json"))
rows, seen = [], set()
for c in data:
    t = (c.get("title") or "").strip()
    if t in EXCLUDE or c.get("channel_id") in seen: continue
    seen.add(c.get("channel_id"))
    rs = [e for e in c.get("rss", []) if e["is_short"] and e.get("views")]
    if len(rs) < 5: continue
    med = statistics.median(int(e["views"]) for e in rs)
    if med <= 0: continue
    for e in rs:
        rows.append((t, html.unescape(e["title"]), int(e["views"]) / med, int(e["views"]), e["published"][:10]))
print("shorts:", len(rows), "channels:", len({r[0] for r in rows}))
res = []
for name, pat in FEAT.items():
    yes = [r[2] for r in rows if re.search(pat, r[1], re.I)]
    no = [r[2] for r in rows if not re.search(pat, r[1], re.I)]
    chans = len({r[0] for r in rows if re.search(pat, r[1], re.I)})
    if len(yes) >= 8:
        res.append((name, len(yes), chans, round(statistics.median(yes), 2), round(statistics.median(no), 2),
                    round(statistics.mean(yes), 2)))
for r in sorted(res, key=lambda x: -x[3]): print(r)
json.dump({"n_shorts": len(rows), "features": res}, open("raw/title_feature_lift_2026-11-19.json", "w"), indent=1)

# Outlier rate: share of Shorts with lift >= 3 (3x the channel's own median)
base = sum(1 for r in rows if r[2] >= 3) / len(rows)
print("baseline outlier rate (>=3x):", round(base, 3), "n=", len(rows))
orates = []
for name, pat in FEAT.items():
    ys = [r for r in rows if re.search(pat, r[1], re.I)]
    if len(ys) >= 8:
        k = sum(1 for r in ys if r[2] >= 3)
        orates.append((name, len(ys), k, round(k / len(ys), 3)))
for o in sorted(orates, key=lambda x: -x[3]): print(o)
print("TOP OUTLIERS:")
for r in sorted(rows, key=lambda r: -r[2])[:20]: print(round(r[2], 1), r[3], r[4], r[0], "|", r[1][:80])
json.dump({"n_shorts": len(rows), "features_median_lift": res, "baseline_outlier_rate": base,
           "features_outlier_rate": orates,
           "top_outliers": sorted(rows, key=lambda r: -r[2])[:25]},
          open("raw/title_feature_lift_2026-11-19.json", "w"), indent=1, ensure_ascii=False)
