#!/usr/bin/env python3
"""Merge raw channel data -> raw/shorts_channel_metrics_2026-11-19.json (no network)."""
import json, re, statistics, datetime as dt
TODAY = dt.datetime(2026, 11, 19, tzinfo=dt.timezone.utc)
def rv(t):
    if not t: return None
    m = re.match(r"([\d\.]+)([KMB]?) views", t.replace(',', ''))
    return float(m.group(1)) * {'K': 1e3, 'M': 1e6, 'B': 1e9, '': 1}[m.group(2)] if m else None
tabs = {}
desc = {}
for f in ['raw/yt_shorts_channels_2026-11-19.json', 'raw/yt_shorts_channels_2026-11-19_b.json']:
    for c in json.load(open(f)):
        tabs[c['handle']] = c.get('shorts_tab', [])
        desc[c['handle']] = c.get('description', '')
details = {}
def add(d):
    if d.get('title') and d.get('channel_id'):
        details.setdefault(d['channel_id'], {})[d['id']] = d
for c in json.load(open('raw/yt_shorts_channels_2026-11-19.json')):
    for d in c.get('detail', []): add(d)
for f in ['raw/yt_shorts_search_resolved_2026-11-19.json', 'raw/yt_seed_shorts_detail_2026-11-19.json']:
    for d in json.load(open(f)): add(d)
out = []
seen = set()
for c in json.load(open('raw/yt_channels_rss_2026-11-19.json')):
    cid = c.get('channel_id')
    if cid in seen: continue
    seen.add(cid)
    rs = [e for e in c.get('rss', []) if e['is_short'] and e.get('views')]
    v = [int(e['views']) for e in rs]
    lk = [int(e['likes']) / int(e['views']) for e in rs if e.get('likes') and int(e['views']) > 0]
    dates = [dt.datetime.fromisoformat(e['published']) for e in rs]
    last30 = sum(1 for d in dates if (TODAY - d).days <= 30)
    tab = tabs.get(c['handle'], [])
    tabv = [(rv(s['views']), s['title']) for s in tab if rv(s['views']) is not None]
    top = max(tabv) if tabv else (None, None)
    det = details.get(cid, {})
    lens = [int(d['length_s']) for d in det.values() if d.get('length_s')]
    coms = [(d['comments'], d['views'], d['title']) for d in det.values() if d.get('comments')]
    out.append({
        'title': (c.get('title') or '').strip(), 'url': 'https://www.youtube.com/channel/' + cid if cid else c['url'],
        'handle_in': c['handle'], 'subs': c.get('subscribers'), 'joined': c.get('joined'), 'video_count': c.get('video_count'),
        'shorts_tab_visible': len(tab), 'rss_shorts_n': len(rs),
        'rss_median_views': statistics.median(v) if v else None,
        'rss_min_date': min(dates).date().isoformat() if dates else None, 'rss_max_date': max(dates).date().isoformat() if dates else None,
        'shorts_last30d_in_rss': last30,
        'tab_median20': statistics.median([x for x, _ in tabv[:20]]) if tabv else None,
        'top_tab': top, 'like_rate_median': round(statistics.median(lk), 4) if lk else None,
        'len_median': statistics.median(lens) if lens else None, 'len_n': len(lens), 'lens': lens,
        'comments_samples': coms[:3], 'rss_titles': [e['title'] for e in rs[:6]],
        'desc': (desc.get(c['handle']) or '')[:200],
        'detail_desc': [d.get('desc', '')[:150] for d in list(det.values())[:2]],
    })
json.dump(out, open('raw/shorts_channel_metrics_2026-11-19.json', 'w'), indent=1, ensure_ascii=False)
for o in out:
    print(f"## {o['title']} | {o['subs']} | joined {o['joined']} | vids {o['video_count']} | tab {o['shorts_tab_visible']} | rssN {o['rss_shorts_n']} med {o['rss_median_views']} ({o['rss_min_date']}..{o['rss_max_date']}) last30={o['shorts_last30d_in_rss']} | like {o['like_rate_median']} | len {o['len_median']} n{o['len_n']} | top {o['top_tab']}")
    print('   T:', ' || '.join(t[:60] for t in o['rss_titles'][:5]))
    print('   D:', o['desc'][:150].replace('\n',' '), '|', ' / '.join(x.replace('\n',' ')[:100] for x in o['detail_desc']))
