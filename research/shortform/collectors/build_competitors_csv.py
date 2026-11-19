#!/usr/bin/env python3
"""SHORTS_COMPETITORS.csv from raw/shorts_channel_metrics_2026-11-19.json + raw RSS + hand annotations.

Measured columns (no human judgement):
  subs (YouTube-rounded, /about), shorts_count_seen (Shorts tab items visible on first load, max 48),
  median_views_recent_shorts (exact views from the public RSS feed, Shorts among the channel's
  last 15 uploads; n and date range given), top_short (highest of the visible Shorts-tab items,
  YouTube-rounded views), typical_duration_s (median lengthSeconds of Shorts whose /shorts page
  was served; n given; 'unknown' if none), like rate (RSS likes / views, median).
Annotated columns (pillar, hook_style, visual_complexity, narration, sound, ending): from TITLES,
  DESCRIPTIONS and channel About text only. No video was watched (thumbnails and playback not
  available to this session), so visual/narration/sound are 'unknown (not viewed)' unless the
  channel states it.
"""
import csv, json, html, statistics

M = {m["title"]: m for m in json.load(open("raw/shorts_channel_metrics_2026-11-19.json"))}
RSS = {(c.get("title") or "").strip(): c for c in json.load(open("raw/yt_channels_rss_2026-11-19.json"))}
NV = "unknown (not viewed)"
# title: (pillar, hook_style, visual, narration, sound, ending, extra_note, confidence)
A = {
 "ParaHaunt": ("Micro Horror (creature/analog-horror IP)", "Creature name + credited source in brackets ('Watch Tower [Doctor Nowhere]')", "med (stated 'animated'; not viewed)", NV, NV, "lore reveal / creature fact", "Animates other creators' IP with credit (Doctor Nowhere, Trevor Henderson): rights model MOTHWAKE should not copy", "high"),
 "Liminal Static": ("Interactive (pick-a-path liminal)", "'Pick a Path / Pick a Pod / Birth Month' choice prompt", NV, NV, NV, "open choice -> comments", "12 Shorts in 6 weeks, then no uploads since 2026-03-08 (RSS)", "high"),
 "RULES OF FEAR": ("Rules & Survival (job rules)", "'Congratulations... You've Been Hired as...' + rule number", NV, NV, NV, "rule broken / serial 'Rule Number Five'", "Shorts mostly ~2 min (over the 45 s target)", "high"),
 "Stretch - Backrooms Animated & Explained": ("Micro Horror (Backrooms entities)", "Entity number + name ('Backrooms Entity 67 - Partygoers')", "med (stated 'animation')", NV, NV, "lore", "Backrooms wiki IP; last Shorts in RSS are from 2022", "medium"),
 "Dusk Broadcast": ("Rules & Survival (liminal survival guides)", "'3 Methods to Catch a Mimic' how-to framing", NV, NV, NV, "instructional", "Mostly long-form; only 4 Shorts visible", "medium"),
 "TwistAnimations": ("Micro Horror (found-footage serial)", "Series title + episode ('The Pink Hallway - Discovery #3')", "high (3D VFX/Blender per descriptions)", NV, NV, "serial cliffhanger", "3D, not 2D", "high"),
 "Horror Bytes": ("Rules & Survival (job rules, mass-volume)", "Long descriptive titles ('Rural Airport Nightmare: Rules Turned Deadly!')", NV, NV, NV, "unknown", "431 videos, RSS median 35 views: volume-without-reach contrast (inauthentic-content risk pattern)", "high"),
 "INSTITUTE 19": ("Rules & Survival (analog-horror rules, own world)", "'If [X]... [COMMAND] | Soviet Analog Horror'", NV, NV, NV, "rule as final line", "Original fictional institute; object numbering (Object 19-004) = series world", "high"),
 "Spooky Terror": ("Rules & Survival (horror-comedy serial)", "'[Place] Rules (Part N)' / 'My Reflection Is One Second Late'", "stated animation; not viewed", NV, NV, "'Part N is next' cliffhanger", "Joined 2026-11-01; 23 Shorts in 18 days", "high"),
 "Liminal Lands": ("Rules & Survival (dreamcore rules)", "'RULES to follow if you...' / 'There exists a world you can only reach at...'", NV, NV, NV, "rules list", "Top short 2.4M (rounded)", "high"),
 "VoidCast": ("Interactive / scenario (Roblox-animated 'what if')", "Second-person premise + emoji ('Your Arrow Always Points To Mom')", "low-med (Roblox animation, stated)", NV, NV, "twist", "Family-friendly scenario, horror-adjacent; daily cadence", "medium"),
 "VONNshorts": ("Rules & Survival ('In This Town, if...')", "'In This Town, If [X], You [Y]'", "AI video (channel states 'I make AI short videos')", NV, NV, "emotional twist + 'Would you...?' in description", "Template title on every upload; self-described AI", "high"),
 "Dr Scario": ("Rules & Survival (3AM rules)", "Quoted warning ('If you hear knocking at 3AM... don't open it.')", NV, NV, NV, "unknown", "One 30K outlier on a 22-sub channel; no uploads since 2026-05", "high"),
 "Last Instructions": ("Rules & Survival / Interactive (job offer)", "'Will you accept the offer?' / 'Would You survive this Job??'", NV, NV, NV, "question to viewer", "~2 min Shorts", "high"),
 "Horror Darkvibe": ("Rules & Survival (backrooms/dog rules)", "'Never TRUST...' / 'YOUR Dog Does This, Then...'", NV, NV, NV, "unknown", "Description says 'Hire2Die' (renamed); likes hidden", "medium"),
 "Night Shift Tales": ("Rules & Survival (night-shift jobs)", "'[Job] Night Shift Horror | Terrifying Rules'", NV, NV, NV, "unknown", "13 uploads in 5 days (Oct 2025), then stopped", "high"),
 "OBLIVARA": ("Rules & Survival (escape-room scenario serial)", "'You Wake Up in a STRANGE Room... PART N'", NV, NV, NV, "serial cliffhanger", "Joined 2026-11-08", "high"),
 "Grim Tales": ("Interactive (pick a door, serial)", "'Pick A Door N - Would You Survive Your Door?'", NV, NV, NV, "door reveal + next part", "Part 4 = 289,585 views (RSS, 2026-01-19) on a 2.17K-sub channel", "high"),
 "Everdust": ("Interactive (dilemma choice, serial)", "Ticking dilemma + 'or' ('The roof is lifting... hide in the bathtub or drive away?')", NV, NV, NV, "binary choice -> comments decide", "Joined 2026-10-05. Uses a real disaster (Joplin tornado 2011) labelled 'FICTION': sensitivity risk", "high"),
 "What If Animator": ("Interactive / scenario ('What if...')", "'What if [catastrophe] in 100 days and you had $X'", "low-med (Roblox-style per description link)", NV, NV, "choice consequence", "398 videos in ~15 months", "medium"),
 "SimplyPyro": ("Rules & Survival / Interactive (bunker survival)", "First-person conflict + emoji ('They Laughed at My Bunker... Now They Want In')", "stated #animation; not viewed", NV, NV, "serial (Bunker Part 3)", "Joined 2026-11-11; 1,586,444 views on a Short published 2026-11-13 (RSS)", "high"),
 "You Decide Stories": ("Interactive (comment decides next part)", "Mundane message + contradiction ('Mom Called Me For Dinner... Then Texted \"I'm Still At Work\"')", "stated 'Animated'; not viewed", NV, NV, "majority comment vote picks next part", "12 s Short reached 27,627 on a 195-sub channel", "high"),
 "unfixed": ("Interactive (two doors, liminal)", "'Two Doors, One Choice (Which Door Would You Choose)'", NV, NV, NV, "open choice", "Top 1.8M (rounded); only 3 Shorts in RSS window", "high"),
 "Dark_Liminal": ("Interactive (pick a door)", "'Which door did you pick?'", NV, NV, NV, "open choice", "Identical titles repeated across uploads", "high"),
 "TRZ_FTB": ("Interactive (serial 'what would you do')", "Situation + 'Run or freeze?' ('Lockdown Part 5...')", NV, NV, NV, "binary choice + Part N", "Joined 2026-09-30; RSS median 104,786", "high"),
 "WhatWouldYouDo": ("Interactive (mimic POV choices)", "Short imperative + choice ('Open the door... or trust the vents?')", NV, NV, NV, "binary choice", "Joined 2026-11-13; 143,026 views (seed search detail)", "high"),
 "Stick Rift": ("Interactive / survival (stick-figure serial)", "'Don't Open the Door | Lockdown Pt 1'", "low (stick figures, stated)", NV, NV, "serial", "Copies the 'Lockdown' premise seen on TRZ_FTB", "high"),
 "UnwholesomePenguin": ("Micro Horror (two-sentence horror, hand-drawn)", "Two-sentence story title ('Not my dad')", "med (Procreate hand-drawn, stated)", NV, NV, "twist sentence", "Solo artist, 'all made by me'; top 9.5M (rounded); recent RSS Shorts from 2024", "high"),
 "Dark Robot": ("Micro Horror (two-sentence horror)", "'[Title] - Two Sentence Horror Stories'", "stated animated; not viewed", NV, NV, "twist sentence", "Top 7.1M (rounded) but RSS median 7,830", "high"),
 "Darkbox Silent Horror": ("Micro Horror (silent webcomic)", "Short noun titles ('Red Plastic Bag')", "low-med (motion comic; webcomic per About)", "no (silent format)", NV, "visual punchline", "Malaysian webcomic anthology, 1,361 videos", "medium"),
 "Twisted Reveries": ("Micro Horror (urban legends)", "Legend name + hook ('La Llorona: Why You Should Fear the River')", NV, NV, NV, "lore", "Real-folklore retellings, 24 subs", "high"),
 "Nightline Horror": ("Micro Horror (sound/trend bait)", "'Don't Check The Sound' / 'Have you seen these before?!'", NV, NV, NV, "unknown", "Mixed formats; several 9-17x outliers in Nov 2025", "medium"),
 "LIGHTS ARE OFF": ("Micro Horror (cursed 3D)", "Calm caption over wrong image ('I think it's safe to swim here')", "high (3D, states 'No AI was used')", NV, NV, "visual reveal", "Benchmark: 55,906,277 views (RSS) on a 15 s Short", "high"),
 "The Hidden Transmission": ("Micro Horror (analog horror)", "'[Wrong domestic image] - Analog Horror' ('Father Eats in the Basement')", NV, NV, NV, "unknown", "Top 6.5M (rounded) on an 18.8K-sub channel", "high"),
 "Mr. Analog Horror": ("Micro Horror (analog horror PSAs)", "'Analog horror - DO NOT OPEN YOUR APARTMENT DOOR'", NV, NV, NV, "unknown", "Likes hidden", "medium"),
 "Secret Zone": ("Rules & Survival (analog survival protocols)", "'If [everyday event]...' ('If your dog ever starts barking at your mom...')", NV, NV, NV, "protocol", "Closest public analogue to the MOTHWAKE Rules pillar; RSS median 74,455, daily cadence", "high"),
 "Internet Nightmares": ("Interactive (pick a door)", "'Pick a Door... [setting]' ('Pick the RIGHT Door and Survive 72 Hours Alone')", NV, NV, NV, "door reveal", "57.4K subs but RSS median 1,767 (Oct 2026)", "high"),
 "Couple of horrorz": ("Micro Horror (two-sentence horror)", "'Based on a two sentence horror story by u/[Reddit user]'", NV, NV, NV, "twist", "Adapts Reddit users' stories (credited): rights model to avoid", "high"),
 "Seeking Horror": ("Interactive / Rules", "'Would You Survive Your Door?' / 'If You See Freddy Do THIS'", NV, NV, NV, "door reveal", "Uses FNAF IP in titles; likes hidden", "medium"),
 "3 AM Rules": ("Rules & Survival (3AM rules, own series)", "'If [X] at 3AM, DON'T [Y]'", NV, NV, NV, "rule number + 'save this / send it'", "Joined 2026-11-03; 13 Shorts; RSS median 1,539", "high"),
 "Make your Choice": ("Interactive (choice-ending episodes)", "'You're the Last Person on Earth... So Who's Knocking?'", "stated 'short animated episodes'", NV, NV, "choice -> viewers decide", "Joined 2026-11-18; 1 Short", "high"),
 "We are hiring": ("Rules & Survival (job/backrooms)", "'99% of the people failed to survive this challenge'", NV, NV, NV, "unknown", "Collapsed to 331 median (RSS, Oct-Nov 2026) from 419K top", "medium"),
 "Lost Tapes": ("Rules & Survival ('NEVER...' rules)", "'NEVER IGNORE YOUR CAT AT 3AM'", NV, NV, NV, "unknown", "No uploads since 2025-10-18", "high"),
 # contrast / adjacent rows (kept to show patterns, flagged)
 "Disturbia Files": ("CONTRAST: reposted clips", "'This Kid Fell For The Skinwalker's Trap... 😱'", "n/a", "n/a", "n/a", "n/a", "Descriptions credit TikTok creators ('Credit: ... via tiktok') and claim fair use: reused-content risk example", "high"),
 "The Face of Horror": ("CONTRAST: reposted clips", "'She Thought It Was Fun Until This Happened...'", "n/a", "n/a", "n/a", "n/a", "'All credit goes to the original creator' (description): reused-content risk example", "high"),
 "Doctor Nowhere": ("ADJACENT: analog-horror creator", "n/a", "n/a", "n/a", "n/a", "n/a", "1.63M subs, only 2 Shorts (speed-draws); IP source for ParaHaunt/TwistAnimations", "high"),
 "HIGuacamole": ("ADJACENT: fandom-IP animation memes", "IP + meme ('Barney Fights a Mimic')", "med", NV, NV, "n/a", "Poppy Playtime / Dandy's World IP; 18M-view mimic Short", "medium"),
}
cols = ["name", "url", "pillar", "subs", "subs_as_of", "shorts_count_seen", "median_views_recent_shorts",
        "median_basis", "top_short_title", "top_short_views", "typical_duration_s", "hook_style",
        "visual_complexity", "narration", "sound_design_notes", "ending_style", "engagement_notes",
        "joined", "shorts_in_last_30d", "source", "confidence"]
rows = []
for name, a in A.items():
    m = M.get(name)
    if not m:
        continue
    pillar, hook, vis, narr, snd, end, note, conf = a
    tt, tv = m["top_tab"] if m["top_tab"] else (None, None)
    tv, tt = (m["top_tab"][0], m["top_tab"][1]) if m["top_tab"] and m["top_tab"][0] else (None, None)
    like = m["like_rate_median"]
    coms = "; ".join(f"{c[0]} comments on {int(c[1]):,} views" for c in m["comments_samples"][:2] if c[1])
    eng = (f"median like/view {like:.2%} (RSS)" if like else "likes hidden or 0 (RSS)") + (f"; {coms}" if coms else "") + f"; {note}"
    dur = f"{statistics.median(m['lens']):.0f} (n={m['len_n']}, range {min(m['lens'])}-{max(m['lens'])})" if m["lens"] else "unknown"
    rows.append([name, m["url"], pillar, (m["subs"] or "unknown").replace(" subscribers", "").replace(" subscriber", ""),
                 "2026-11-19", f"{m['shorts_tab_visible']}{'+' if m['shorts_tab_visible'] == 48 else ''}",
                 f"{m['rss_median_views']:,.0f}" if m["rss_median_views"] is not None else "unknown",
                 f"exact, RSS, n={m['rss_shorts_n']} Shorts published {m['rss_min_date']}..{m['rss_max_date']}" if m["rss_shorts_n"] else "n/a",
                 html.unescape(tt) if tt else "unknown", f"{tv:,.0f} (YouTube-rounded, top of {m['shorts_tab_visible']} visible)" if tv else "unknown",
                 dur, hook, vis, narr, snd, end, eng, (m["joined"] or "").replace("Joined ", ""),
                 m["shorts_last30d_in_rss"],
                 "youtube.com /about + /shorts tab + feeds/videos.xml + /shorts/<id> pages; raw/yt_channels_rss_2026-11-19.json, raw/yt_shorts_channels_2026-11-19*.json",
                 conf])
with open("SHORTS_COMPETITORS.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(cols); w.writerows(rows)
print(len(rows), "rows;", sum(1 for r in rows if not r[2].startswith(("CONTRAST", "ADJACENT"))), "core")
