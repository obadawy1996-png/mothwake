#!/usr/bin/env python3
"""YT_AUTOCOMPLETE.csv from raw suggestqueries JSON (client=firefox&ds=yt). Rank = position in the list (1 = first)."""
import csv, json, re
PILLAR = {"rules": "Rules & Survival", "survive": "Rules & Survival", "survival": "Rules & Survival",
          "if you": "Rules & Survival", "if your": "Rules & Survival", "night shift": "Rules & Survival",
          "dont open": "Rules & Survival", "door": "Interactive", "would you": "Interactive",
          "what would": "Interactive", "choice": "Interactive", "choose": "Interactive"}
def pillar(seed):
    for k, v in PILLAR.items():
        if k in seed: return v
    return "Micro Horror / topic"
HORROR = re.compile(r"horror|scary|creep|rule|survive|run|door|mimic|demon|backroom|liminal|analog|skinwalker|ghost|night|3am|knock|nightmare|paranormal|fear|haunt|curse|monster|zombie", re.I)
rows = []
for f in ["raw/yt_autocomplete_2026-11-19.json", "raw/yt_autocomplete_2026-11-19_b.json"]:
    for r in json.load(open(f)):
        for i, s in enumerate(r["suggestions"] or []):
            rows.append([r["q"], pillar(r["q"]), i + 1, s, "yes" if HORROR.search(s) else "no",
                         r["fetched_at"][:10], "suggestqueries.google.com client=firefox ds=yt (unpersonalised, no geo param)"])
with open("YT_AUTOCOMPLETE.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["seed", "pillar", "rank", "suggestion", "horror_relevant_heuristic", "date_checked", "source"])
    w.writerows(rows)
print(len(rows))
