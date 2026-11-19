#!/usr/bin/env python3
"""MOTHWAKE Google Trends collector (public trends.google.com JSON endpoints, no key).

Endpoints: /trends/api/explore, /trends/api/widgetdata/multiline,
/trends/api/widgetdata/relatedsearches. The ")]}'" prefix is stripped.
hl=en-US, tz=0. Every response is saved raw. On HTTP 429 it backs off
(30s, 60s, 120s) and records the failure instead of inventing data.

Usage: python gtrends_collector.py out_dir
"""
import datetime as dt
import json
import os
import subprocess
import sys
import time
import urllib.parse

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
OUT = sys.argv[1]
JAR = os.path.join(OUT, ".gt_cookies")
ANCHOR = "analog horror"
GROUPS = [
    [ANCHOR, "horror rules", "scary story animation", "horror shorts", "would you rather horror"],
    [ANCHOR, "creepypasta animation", "liminal space", "backrooms", "sleep paralysis"],
    [ANCHOR, "mimic horror", "skinwalker", "christmas horror", "winter horror"],
    [ANCHOR, "horror animation", "two sentence horror", "survival scenario", "pick a door"],
]
GEOS = ["US", "GB", "CA", "AU"]
PROPS = ["youtube", ""]          # "" = web search
TIMES = ["today 12-m", "now 7-d"]
LOG = []


def now():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def get(path, params):
    url = "https://trends.google.com" + path + "?" + urllib.parse.urlencode(params)
    for wait in (0, 30, 60, 120):
        if wait:
            time.sleep(wait)
        r = subprocess.run(["curl", "-sS", "-m", "40", "-A", UA, "-b", JAR, "-c", JAR,
                            "-w", "\n%{http_code}", url], capture_output=True, timeout=60)
        body, _, code = r.stdout.decode("utf-8", "replace").rpartition("\n")
        if code == "200":
            body = body[body.find("{"):] if body.startswith(")]}'") else body
            try:
                return json.loads(body)
            except ValueError:
                LOG.append({"t": now(), "path": path, "code": code, "note": "unparseable"})
                return None
        LOG.append({"t": now(), "path": path, "code": code, "backoff_next": wait})
        if code != "429":
            return None
    return None


def explore(kws, geo, prop, tf):
    req = {"comparisonItem": [{"keyword": k, "geo": geo, "time": tf} for k in kws],
           "category": 0, "property": prop}
    return get("/trends/api/explore", {"hl": "en-US", "tz": "0", "req": json.dumps(req)})


def widget(w, kind):
    return get("/trends/api/widgetdata/" + kind,
               {"hl": "en-US", "tz": "0", "req": json.dumps(w["request"]), "token": w["token"]})


def main():
    os.makedirs(OUT, exist_ok=True)
    subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-c", JAR, "-o", "/dev/null",
                    "https://trends.google.com/trends/?geo=US"])
    series, related = [], []
    for gi, g in enumerate(GROUPS):
        for geo in GEOS:
            for prop in PROPS:
                for tf in TIMES:
                    ex = explore(g, geo, prop, tf)
                    rec = {"group": gi, "keywords": g, "geo": geo, "property": prop or "web",
                           "timeframe": tf, "fetched_at": now(), "timeline": None}
                    if ex:
                        ws = {w["id"]: w for w in ex.get("widgets", [])}
                        if "TIMESERIES" in ws:
                            ml = widget(ws["TIMESERIES"], "multiline")
                            if ml:
                                rec["timeline"] = [{"time": p.get("time"), "formattedTime": p.get("formattedTime"),
                                                    "value": p.get("value"), "isPartial": p.get("isPartial")}
                                                   for p in ml.get("default", {}).get("timelineData", [])]
                    series.append(rec)
                    time.sleep(2.5)
                    json.dump(series, open(os.path.join(OUT, "gtrends_multiline_2026-11-19.json"), "w"), indent=0)
    # related queries: single-term explore, US, both properties, 12 months
    terms = sorted({k for g in GROUPS for k in g})
    for prop in PROPS:
        for k in terms:
            ex = explore([k], "US", prop, "today 12-m")
            rec = {"term": k, "geo": "US", "property": prop or "web", "timeframe": "today 12-m",
                   "fetched_at": now(), "rising": None, "top": None}
            if ex:
                for w in ex.get("widgets", []):
                    if w.get("id") == "RELATED_QUERIES":
                        rq = widget(w, "relatedsearches")
                        if rq:
                            lists = rq.get("default", {}).get("rankedList", [])
                            def items(i):
                                return [{"query": x.get("query"), "value": x.get("formattedValue")}
                                        for x in (lists[i].get("rankedKeyword", []) if len(lists) > i else [])]
                            rec["top"], rec["rising"] = items(0), items(1)
            related.append(rec)
            time.sleep(2.5)
            json.dump(related, open(os.path.join(OUT, "gtrends_related_2026-11-19.json"), "w"), indent=0)
    json.dump(LOG, open(os.path.join(OUT, "gtrends_errors_2026-11-19.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
