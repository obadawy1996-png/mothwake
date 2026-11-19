#!/usr/bin/env python3
"""Re-fetch Shorts whose detail record has no title (intermittent empty player response).
Usage: python repair_details.py file.json [file2.json ...]  (edits in place, keeps originals' ids)"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yt_shorts_collector as Y  # noqa: E402


def fix(rec):
    if rec.get("id") and not rec.get("title"):
        d = Y.short_detail(rec["id"])
        if d.get("title"):
            for k, v in d.items():
                rec[k] = v
            rec["repaired"] = True
        time.sleep(0.5)


for f in sys.argv[1:]:
    data = json.load(open(f))
    for item in data:
        if "detail" in item:            # channel records
            for d in item["detail"]:
                fix(d)
        else:
            fix(item)
    json.dump(data, open(f, "w"), indent=1, ensure_ascii=False)
    n = sum(1 for i in data for d in (i.get("detail") or [i]) if not d.get("title"))
    print(f, "still missing:", n)
