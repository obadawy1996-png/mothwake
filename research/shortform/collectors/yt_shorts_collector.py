#!/usr/bin/env python3
"""MOTHWAKE public YouTube Shorts collector (no API key, no paid services).

Reads only PUBLIC youtube.com HTML pages and their embedded ytInitialData /
ytInitialPlayerResponse JSON:
  - /results?search_query=...&sp=EgIYAQ%253D%253D   (videos under 4 min)
  - /@handle/about, /@handle/shorts
  - /shorts/<videoId>   (exact view count, length, publish date, likes, comments)
Nothing is logged in, posted or paid for.

Usage:
  python yt_shorts_collector.py discover queries.txt out.json
  python yt_shorts_collector.py channels handles.txt out.json [n_detail]
  python yt_shorts_collector.py suggest queries.txt out.json   (YouTube autocomplete)
"""
import datetime as dt
import json
import re
import subprocess
import sys
import time
import urllib.parse

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")


def now():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def curl(url):
    cmd = ["curl", "-sL", "-m", "40", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
           "-b", "CONSENT=YES+1; SOCS=CAI", url]
    r = subprocess.run(cmd, capture_output=True, timeout=60)
    return r.stdout.decode("utf-8", "replace")


def jvar(html, name):
    """Decode the JSON object assigned to `var <name> = {...}` with a real JSON parser."""
    i = html.find("var " + name + " = ")
    if i < 0:
        return None
    try:
        obj, _ = json.JSONDecoder().raw_decode(html, i + len("var " + name + " = "))
        return obj
    except ValueError:
        return None


def walk(o, key, out=None):
    out = [] if out is None else out
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key:
                out.append(v)
            walk(v, key, out)
    elif isinstance(o, list):
        for v in o:
            walk(v, key, out)
    return out


def search(q, sp="EgIYAQ%253D%253D"):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(q) + "&sp=" + sp
    d = jvar(curl(url), "ytInitialData")
    out = []
    for v in walk(d, "videoRenderer") if d else []:
        g = lambda k: (v.get(k) or {}).get("simpleText")
        try:
            own = v["ownerText"]["runs"][0]
            out.append({"query": q, "id": v.get("videoId"), "title": v["title"]["runs"][0]["text"],
                        "channel": own["text"],
                        "handle": own["navigationEndpoint"]["browseEndpoint"].get("canonicalBaseUrl"),
                        "views": g("viewCountText"), "published": g("publishedTimeText"),
                        "duration": g("lengthText"), "fetched_at": now()})
        except (KeyError, IndexError, TypeError):
            continue
    # Shorts shelves inside search results
    for s in walk(d, "shortsLockupViewModel") if d else []:
        vid = (walk(s, "reelWatchEndpoint") or [{}])[0].get("videoId")
        out.append({"query": q, "id": vid, "shelf": "shorts",
                    "accessibility": s.get("accessibilityText"), "fetched_at": now()})
    return out


def short_detail(vid, tries=3):
    # YouTube sometimes serves a page whose player response has no videoDetails;
    # retry with a pause before recording the gap.
    for attempt in range(tries):
        h = curl("https://www.youtube.com/shorts/" + vid)
        pr = jvar(h, "ytInitialPlayerResponse") or {}
        vd = pr.get("videoDetails", {})
        if vd.get("title"):
            break
        time.sleep(3 + 4 * attempt)
    mf = pr.get("microformat", {}).get("playerMicroformatRenderer", {})
    like = re.search(r'"likeCount":"(\d+)"', h)
    com = re.search(r'"accessibilityText":"View ([\d,\.KM]+) comments"', h)
    return {"id": vid, "title": vd.get("title"), "length_s": vd.get("lengthSeconds"),
            "views": vd.get("viewCount") or mf.get("viewCount"), "publish": mf.get("publishDate"),
            "likes": like.group(1) if like else None,
            "comments": com.group(1) if com else None,
            "author": vd.get("author"), "channel_id": vd.get("channelId"),
            "desc": (vd.get("shortDescription") or "")[:300], "fetched_at": now()}


def channel(handle, n_detail=8):
    base = "https://www.youtube.com/" + handle.lstrip("/")
    rec = {"handle": handle, "url": base, "fetched_at": now()}
    a = jvar(curl(base + "/about"), "ytInitialData")
    if a:
        av = walk(a, "aboutChannelViewModel")
        if av:
            av = av[0]
            rec.update({"subscribers": av.get("subscriberCountText"),
                        "total_views": av.get("viewCountText"),
                        "video_count": av.get("videoCountText"),
                        "joined": (av.get("joinedDateText") or {}).get("content"),
                        "country": av.get("country"),
                        "description": (av.get("description") or "")[:400]})
        md = walk(a, "channelMetadataRenderer")
        if md:
            rec["title"] = md[0].get("title")
    sd = jvar(curl(base + "/shorts"), "ytInitialData")
    shorts = []
    for s in walk(sd, "shortsLockupViewModel") if sd else []:
        om = s.get("overlayMetadata", {})
        vid = (walk(s, "reelWatchEndpoint") or [{}])[0].get("videoId")
        shorts.append({"id": vid, "title": om.get("primaryText", {}).get("content"),
                       "views": om.get("secondaryText", {}).get("content"),
                       "a11y": s.get("accessibilityText")})
    rec["shorts_tab"] = shorts
    rec["detail"] = []
    for s in shorts[:n_detail]:
        if s["id"]:
            try:
                rec["detail"].append(short_detail(s["id"]))
            except Exception as e:
                rec["detail"].append({"id": s["id"], "error": repr(e)})
            time.sleep(0.5)
    return rec


def about_and_rss(handle):
    """Channel /about + the public RSS feed (last 15 uploads: publish date, exact views, likes).
    Used when per-Short pages are throttled. RSS has no duration."""
    base = "https://www.youtube.com/" + handle.lstrip("/")
    rec = {"handle": handle, "url": base, "fetched_at": now()}
    a = jvar(curl(base + "/about"), "ytInitialData")
    av = walk(a, "aboutChannelViewModel") if a else []
    if av:
        av = av[0]
        rec.update({"channel_id": av.get("channelId"), "subscribers": av.get("subscriberCountText"),
                    "video_count": av.get("videoCountText"),
                    "joined": (av.get("joinedDateText") or {}).get("content"),
                    "total_views": av.get("viewCountText")})
    md = walk(a, "channelMetadataRenderer") if a else []
    if md:
        rec["title"] = md[0].get("title")
        rec["channel_id"] = rec.get("channel_id") or md[0].get("externalId")
    rec["rss"] = []
    if rec.get("channel_id"):
        x = curl("https://www.youtube.com/feeds/videos.xml?channel_id=" + rec["channel_id"])
        for e in re.findall(r"<entry>(.*?)</entry>", x, re.S):
            g = lambda p: (re.search(p, e, re.S) or [None, None])[1]
            rec["rss"].append({"id": g(r"<yt:videoId>(.*?)</yt:videoId>"),
                               "title": g(r"<title>(.*?)</title>"),
                               "is_short": "/shorts/" in (g(r'<link rel="alternate" href="(.*?)"') or ""),
                               "published": g(r"<published>(.*?)</published>"),
                               "views": g(r'<media:statistics views="(\d+)"'),
                               "likes": g(r'<media:starRating count="(\d+)"')})
    return rec


def suggest(q):
    url = ("https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=" +
           urllib.parse.quote_plus(q))
    try:
        return json.loads(curl(url))[1]
    except (ValueError, IndexError):
        return None


if __name__ == "__main__":
    mode = sys.argv[1]
    lines = [l.strip() for l in open(sys.argv[2]) if l.strip() and not l.startswith("#")]
    out = []
    if mode == "discover":
        for q in lines:
            out += search(q)
            time.sleep(1.0)
    elif mode == "channels":
        n = int(sys.argv[4]) if len(sys.argv) > 4 else 8
        for h in lines:
            try:
                out.append(channel(h, n))
            except Exception as e:
                out.append({"handle": h, "error": repr(e), "fetched_at": now()})
            print(h, file=sys.stderr)
            time.sleep(1.0)
    elif mode == "rss":
        for h in lines:
            try:
                out.append(about_and_rss(h))
            except Exception as e:
                out.append({"handle": h, "error": repr(e), "fetched_at": now()})
            time.sleep(1.5)
    elif mode == "suggest":
        for q in lines:
            out.append({"q": q, "suggestions": suggest(q), "fetched_at": now()})
            time.sleep(0.5)
    json.dump(out, open(sys.argv[3], "w"), indent=1, ensure_ascii=False)
