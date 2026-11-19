#!/usr/bin/env python3
"""MOTHWAKE public YouTube collector (no API key, no paid services).

Reads only PUBLIC youtube.com pages (channel /about, /videos, /shorts, the
"Popular" sort via the public web client continuation, and search results)
and extracts the embedded ytInitialData JSON. Nothing is logged in, nothing
is posted, no credits are used.

Usage:
  python research/collectors/yt_public_collector.py channels handles.txt out.json
  python research/collectors/yt_public_collector.py search "query one" "query two" > out.json

Every value carries the fetch timestamp (UTC). Relative dates ("3 days ago")
are kept verbatim; YouTube rounds subscriber counts (3 significant figures).
Limitations: this depends on YouTube's undocumented page structure and may
break when YouTube changes its markup. The YouTube Data API v3 (needs a key)
is the robust replacement.
"""
import datetime as dt
import json
import re
import subprocess
import sys
import time

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")


def now():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def curl(url, data=None):
    cmd = ["curl", "-sL", "-m", "40", "-A", UA,
           "-H", "Accept-Language: en-US,en;q=0.9",
           "-b", "CONSENT=YES+1; SOCS=CAI"]
    if data is not None:
        cmd += ["-H", "Content-Type: application/json", "--data-binary", "@-"]
    cmd.append(url)
    r = subprocess.run(cmd, input=(json.dumps(data).encode() if data else None),
                       capture_output=True, timeout=60)
    return r.stdout.decode("utf-8", "replace")


def initial_data(html):
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    return json.loads(m.group(1)) if m else None


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


def parse_lockups(d):
    vids = []
    for lv in walk(d, "lockupViewModel"):
        try:
            md = lv["metadata"]["lockupMetadataViewModel"]
            title = md["title"]["content"]
            parts = []
            for row in md.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", []):
                for p in row.get("metadataParts", []):
                    parts.append(p.get("text", {}).get("content"))
            badges = [b["text"] for b in walk(lv.get("contentImage", {}), "thumbnailBadgeViewModel")
                      if isinstance(b, dict) and "text" in b]
            vids.append({"id": lv.get("contentId"), "title": title,
                         "views": parts[0] if parts else None,
                         "published": parts[1] if len(parts) > 1 else None,
                         "duration": badges[0] if badges else None})
        except (KeyError, TypeError):
            continue
    return vids


def parse_shorts(d):
    out = []
    for s in walk(d, "shortsLockupViewModel"):
        om = s.get("overlayMetadata", {})
        out.append({"title": om.get("primaryText", {}).get("content"),
                    "views": om.get("secondaryText", {}).get("content")})
    return out


def popular(html, d):
    """Follow the public 'Popular' chip continuation on the /videos tab."""
    key = re.search(r'"INNERTUBE_API_KEY":"([^"]+)"', html)
    ver = re.search(r'"INNERTUBE_CLIENT_VERSION":"([^"]+)"', html)
    token = None
    for chip in walk(d, "chipViewModel"):
        if chip.get("text") == "Popular":
            t = walk(chip, "continuationCommand")
            if t:
                token = t[0].get("token")
    if not (key and ver and token):
        return []
    body = {"context": {"client": {"clientName": "WEB", "clientVersion": ver.group(1),
                                   "hl": "en", "gl": "US"}}, "continuation": token}
    raw = curl("https://www.youtube.com/youtubei/v1/browse?key=" + key.group(1), body)
    try:
        return parse_lockups(json.loads(raw))
    except ValueError:
        return []


def channel(handle):
    base = "https://www.youtube.com/" + handle.lstrip("/")
    rec = {"handle": handle, "url": base, "fetched_at": now()}
    a = initial_data(curl(base + "/about"))
    if a:
        av = walk(a, "aboutChannelViewModel")
        if av:
            av = av[0]
            rec.update({
                "subscribers": av.get("subscriberCountText"),
                "total_views": av.get("viewCountText"),
                "video_count": av.get("videoCountText"),
                "joined": (av.get("joinedDateText") or {}).get("content"),
                "country": av.get("country"),
                "channel_id": av.get("channelId"),
                "description": (av.get("description") or "")[:400],
            })
        md = walk(a, "channelMetadataRenderer")
        if md:
            rec["title"] = md[0].get("title")
    vh = curl(base + "/videos")
    vd = initial_data(vh)
    rec["recent_videos"] = parse_lockups(vd)[:15] if vd else []
    rec["popular_videos"] = popular(vh, vd)[:10] if vd else []
    sd = initial_data(curl(base + "/shorts"))
    rec["recent_shorts"] = parse_shorts(sd)[:15] if sd else []
    return rec


def search_channels(q):
    url = ("https://www.youtube.com/results?search_query=" +
           q.replace(" ", "+") + "&sp=EgIQAg%253D%253D")
    d = initial_data(curl(url))
    res = []
    for c in walk(d, "channelRenderer") if d else []:
        txt = lambda k: (c.get(k, {}) or {}).get("simpleText")
        res.append({"query": q, "title": txt("title"),
                    "handle_text": txt("subscriberCountText"),   # YouTube puts @handle here
                    "subs_text": txt("videoCountText"),          # ...and subscribers here
                    "channel_id": c.get("channelId"),
                    "fetched_at": now()})
    return res


def search_videos(q, sp="CAMSBAgEEAE%253D"):
    """Top videos for a query. Default sp = sort by view count, uploaded this month, videos only."""
    url = "https://www.youtube.com/results?search_query=" + q.replace(" ", "+") + "&sp=" + sp
    d = initial_data(curl(url))
    out = []
    for v in walk(d, "videoRenderer") if d else []:
        g = lambda k: (v.get(k) or {}).get("simpleText")
        try:
            out.append({"title": v["title"]["runs"][0]["text"],
                        "channel": v["ownerText"]["runs"][0]["text"],
                        "views": g("viewCountText"), "published": g("publishedTimeText"),
                        "duration": g("lengthText"), "id": v.get("videoId")})
        except (KeyError, IndexError, TypeError):
            continue
    return out


def views_int(t):
    m = re.match(r"([\d,]+) views", t or "")
    return int(m.group(1).replace(",", "")) if m else None


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "channels":
        handles = [l.strip() for l in open(sys.argv[2]) if l.strip() and not l.startswith("#")]
        out = []
        for h in handles:
            try:
                out.append(channel(h))
            except Exception as e:  # keep going; record the failure
                out.append({"handle": h, "error": repr(e), "fetched_at": now()})
            time.sleep(1.0)
        json.dump(out, open(sys.argv[3], "w"), indent=1, ensure_ascii=False)
    elif mode == "search":
        allr = []
        for q in sys.argv[2:]:
            allr += search_channels(q)
            time.sleep(1.0)
        json.dump(allr, sys.stdout, indent=1, ensure_ascii=False)
    elif mode == "topics":
        # topics <queries.txt> <out.json>: top-by-views videos uploaded this month per query
        qs = [l.strip() for l in open(sys.argv[2]) if l.strip() and not l.startswith("#")]
        res = []
        for q in qs:
            vids = search_videos(q)
            vs = sorted([x for x in (views_int(v["views"]) for v in vids) if x is not None], reverse=True)
            res.append({"query": q, "fetched_at": now(), "filter": "this month, sorted by views, videos",
                        "n_results": len(vids),
                        "top1_views": vs[0] if vs else None,
                        "median_views_top20": vs[len(vs) // 2] if vs else None,
                        "n_over_100k": sum(1 for x in vs if x >= 100000),
                        "n_over_1m": sum(1 for x in vs if x >= 1000000),
                        "videos": vids[:20]})
            time.sleep(1.0)
        json.dump(res, open(sys.argv[3], "w"), indent=1, ensure_ascii=False)
