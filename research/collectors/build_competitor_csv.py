#!/usr/bin/env python3
"""Build research/COMPETITOR_DATABASE.csv from the public YouTube snapshots in research/raw/.

Measured fields are computed from the snapshot JSON (fetched via yt_public_collector.py).
Qualitative fields come from the ANNOT table below and are written by the researcher from
channel descriptions and video titles seen in the snapshot (not from thumbnails, which could
not be fetched: i.ytimg.com was blocked). Re-run after a new snapshot; update ANNOT by hand.
"""
import csv, json, re, statistics, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AS_OF = "2026-11-19"
SNAPS = ["raw/yt_channels_2026-11-19.json", "raw/yt_channels_2026-11-19_b.json", "raw/yt_channels_2026-11-19_c.json"]

def num(t):
    if not t:
        return None
    t = t.replace(",", "").replace(" views", "").replace(" subscribers", "").replace(" subscriber", "").strip()
    m = re.match(r"([\d.]+)\s*([KMB]?)", t)
    if not m:
        return None
    return int(float(m.group(1)) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)])

def days(p):
    m = re.match(r"(\d+)\s*([a-z]+)", p or "")
    if not m:
        return None
    n, u = int(m.group(1)), m.group(2)
    if u.startswith(("mi", "h", "s")):
        return 0
    return {"d": n, "w": 7 * n, "mo": 30 * n, "y": 365 * n}.get(
        "mo" if u.startswith("mo") else u[0], None)

def dur(s):
    if not s or ":" not in s:
        return None
    t = 0
    for x in s.split(":"):
        if not x.isdigit():
            return None
        t = t * 60 + int(x)
    return t

def fmt_s(s):
    if s is None:
        return "unknown"
    s = int(s)
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"

# handle: (name, category, story_format, visual_style, title_pattern, growth_signals, tier, confidence, notes)
ANNOT = {
 # ---------- small / new ----------
 "@ParaHauntYT": ("ParaHaunt", "2D animated horror (creatures/urban legends/analog-horror creatures)", "Listicle creature compilations ('6 Trevor Henderson Giants', 'Top 6 SCPs') + Shorts", "Animated creature showcases (per channel description); style not visually verified", "Number + named creature set + [Animation]", "Joined May 2025; 461K subs; Shorts median ~689K views; draws on other creators' creature IP (Trevor Henderson, SCP)", "riser", "high", "Fastest riser found. Heavy reliance on third-party creature IP (SCP is CC BY-SA; Trevor Henderson creatures are his own IP) - not a model for an original brand."),
 "@Theglendalearchives": ("The Glendale Archives", "found footage / analog horror (liminal, last-person-on-Earth)", "Serialized first-person 'the world is empty' found-footage logs", "Found-footage / analog presentation (per titles+description); not visually verified", "Plain-sentence first-person hook + '(Found Footage / Analog)'", "Joined Mar 2025; 186K subs; recent median ~742K views on ~1 long-form per month", "riser", "high", "Strong evidence that slow, lonely, atmospheric serialized premises work in 2026. Low gore."),
 "@krisarchives_analog": ("Kris Archives", "analog horror (fan parodies of children's IP)", "Analog-horror reinterpretations of known IP (Cat in the Hat, FNAF, Pokemon)", "Drawn analog-horror art (creator says 'I'm an artist'); not visually verified", "Known IP + '(Analog Horror)'", "Joined May 2025; 76.5K subs; median recent ~175K; top 2.5M in ~3 months", "riser", "high", "Growth driven by famous third-party IP - legal/brand risk; not a path for MOTHWAKE."),
 "@liminalstatic0": ("Liminal Static", "liminal spaces / backrooms-style Shorts", "Atmospheric liminal-space Shorts", "Atmospheric environments (per description); not visually verified", "unknown (Shorts titles only)", "Joined Jan 25 2026; 12 videos (all Shorts); 16.6K subs; Shorts median ~253K views", "small/new", "medium", "Shorts-only; long-form performance unknown. Shows Shorts appetite for pure atmosphere."),
 "@InsomniaRulesStories": ("Insomnia Rules", "rules-based horror narration", "'I work the night shift at X. There are rules' first-person narration", "Narration over static/illustrated art (assumed from format; not verified)", "'I Work/Took a Job at [remote place]. [Rule hook]'", "Joined May 5 2025; 45.6K subs; spun off from Insomnia Stories because rules stories 'didn't perform well on my main channel' (channel description)", "small/new", "high", "Recent median 18K; uploads slowed (2 long-form in ~90d)."),
 "@UltisTheGoober": ("Ultis", "horror reaction / exploration (adjacent)", "Reacting to TikTok horror, skinwalker sightings, analog horror, liminal spaces", "Commentary / reaction", "'Exploring Horrifying X' / 'Watching Tik Tok's Most Horrifying...'", "Joined Dec 2024; 190K subs; median recent ~175K", "riser", "high", "Adjacent (not fiction) - useful as topic-demand signal: skinwalker, uncanny valley, liminal."),
 "@StoryBoredz": ("StoryBoredz", "animated storytime (incl. cryptid encounters)", "First-person 'life story' animated storytime", "Animated storytime (per description); not visually verified", "Short cliffhanger 'I Saw an ACTUAL Cryptid...'", "Joined Jan 2024; 224K subs; median recent ~158K", "riser", "medium", "Cryptid-encounter episodes are among its top videos (2.3M)."),
 "@intothedarkanimate": ("Into The Dark Animations", "2D animated horror (skinwalker/wendigo/fire-lookout)", "Curated 'true' story compilations, animated", "Self-described amateur animation ('not an expert animator')", "'This Skinwalker Story Still Haunts Me (Animated)'", "13.7K subs; 32 videos; recent median ~17.5K (ratio >1)", "small/new", "high", "Small channel punching above its weight on skinwalker/wendigo topics. Joined 2018 but content recent."),
 "@MHSMidnightHorrorStories": ("MHS Midnight Horror Stories", "2D animated true-style horror", "Numbered compilations '4 TRUE Hiking Horror Stories'", "Animated (per description); not verified", "Number + TRUE + setting + Animated", "Joined Mar 2024; 16.9K subs; 41 videos", "small/new", "high", "Generic compilation format; median recent ~6K."),
 "@GRDAnimations": ("GRD Animations", "2D animated true-style horror", "Numbered 'TRUE horror stories animated' compilations", "2D (per description)", "Number + TRUE + Animated", "Weekly; 70.9K subs; median recent ~7K (low ratio)", "small/new", "high", "Shows saturation of the 'N true horror stories animated' template."),
 "@sssstories": ("SSS Scary Shorts Stories", "2D animated true-style horror", "Numbered themed compilations (coworker, stranger, Halloween)", "Animated (per description)", "Number + True + theme + Animated", "52.1K subs; frequent uploads; median ~8.6K", "small/new", "high", "Template channel; low views/subs."),
 "@DarkAceAnimations": ("DarkAce Animations", "2D animated true-style horror", "Numbered compilations", "Animated (per description)", "ALL-CAPS number + theme", "96.3K subs; last long-form ~1y ago; median ~9K", "small/new", "high", "Stalled; best videos 6-7 years old."),
 "@creepyanimatedstory": ("Creepy Animated Stories", "2D animated horror (English version of a Russian channel)", "Serialized animated stories ('Don't Go Outside' parts)", "2D animated (per titles)", "Title + 'Horror animated story'", "Dormant ~3 years", "small/new", "high", "Dormant benchmark of an early-wave channel."),
 "@BecauseItsInteresting": ("Because It's Interesting", "animated thriller/suspense stories", "Daily melodrama-thriller animated stories", "Animated (per titles)", "Sensational clause + '!!' + Animated Stories", "1,262 videos; median ~3K; daily", "small/new", "high", "Volume over quality; ratio 0.05."),
 "@JordanGrupe": ("Jordan Grupe Horror", "horror narration (original fiction)", "Original serialized first-person horror by a published author", "Narration", "'I Work for a Secret Facility...' / 'My Hometown Has a Secret...'", "3 uploads/week; 68K subs; median ~12K", "small/new", "high", "Original-fiction narrator; shows ceiling of audio-only original stories without animation."),
 "@horrorontherocks": ("Horror on the Rocks", "horror narration", "NoSleep/creepypasta/'I work at' narration", "Narration", "'I Work At A [place]. I Have So...'", "32.7K subs; frequent uploads; median ~9K", "small/new", "high", ""),
 "@sodagirl": ("soda girl", "internet-horror analysis (analog horror/ARG/lost media)", "Long-form analysis of analog horror, ARGs, haunted games", "Commentary", "'The Dark Secret Hiding In An Abandoned Kids MMO'", "48.3K subs; median recent ~116K (ratio 2.4)", "small/new", "high", "Adjacent: analysis channels amplify original series - a discovery route."),
 "@ChillingAbyss": ("Chilling Abyss", "analog horror (original series 'Arcadia')", "Original analog-horror series + standalone tapes", "Analog/VHS (per titles); not verified", "ALL-CAPS title + '- Analog Horror'", "31.4K subs; 27 videos; median ~23K", "small/new", "high", "Original series; small but ratio 0.73."),
 "@whitestageducation": ("White Stag Education", "analog horror (original series)", "Fake educational broadcasts", "Analog/VHS educational pastiche (per titles)", "ALL-CAPS fake-program titles", "Only 5 videos; 38.2K subs; dormant ~3y", "small/new", "high", "Proves tiny catalogues can build audiences when concept is strong; dormant."),
 "@TheBaroqueHour": ("The Baroque Hour", "analog horror (original series ORPHEUS)", "Numbered episode series with teasers", "Analog (per titles)", "'NN. Title | ORPHEUS [Analog Horror]'", "3.13K subs; 16 videos; last ~9 months", "small/new", "high", "Small original series; typical long-tail outcome."),
 "@NirixiAnimation": ("Nirixi Animation", "2D animated psychological horror (indie studio)", "Pilot episode + concept trailers ('UNBECOMING')", "Independent dark psychological animation (per description)", "ALL-CAPS series title | Official Pilot/Trailer", "Joined Sep 2025; 1.45K subs; Shorts median ~2.4K", "small/new", "high", "Closest tonal analogue to MOTHWAKE found; shows how slow premium-animation channels grow without a release cadence."),
 "@Animighthorrorstories": ("Animight Horror Stories", "2D animated original horror shorts", "Original short horror animations (Ouija, spirit revenge)", "Original 2D with custom characters (per description)", "'The Unseen Friend - Spirit Revenge Horror Story'", "1.37K subs; median recent views <10", "small/new", "high", "Illustrates that 'original 2D horror' alone does not get discovered."),
 "@Rulesoffear": ("Rules of Fear", "rules-based horror Shorts", "Rules-format short horror", "unknown", "unknown", "Joined May 2025; 1.11K subs; Shorts median ~5K", "small/new", "medium", "Part of a long tail of near-zero-sub 'rules' channels in search (saturation signal)."),
 "@HistoryMysteryHorror": ("History, Mystery, and Horror", "dark history / mystery (adjacent)", "Dark-history explainers", "unknown", "'What Happened to...' / 'Why Victorians...'", "Joined Oct 17 2025 with 895 videos (~2+/day) ; median ~1.4K", "small/new", "high", "Mass-production pattern - the kind targeted by YouTube's inauthentic-content policy. Cautionary."),
 "@LeleHillanimated": ("Lele Hill Animated", "2D animated urban legends", "Long compilations '15 Urban Legends Horror Stories Animated - 11-2026'", "Animated (per titles)", "Number + Urban Legends + month-year", "47.7K subs; median recent ~470 views", "small/new", "high", "Compilation-dump pattern, near-zero reach now."),
 # ---------- risers / mid ----------
 "@Lullorin": ("Lullorin", "analog horror / rules-based domestic horror", "'If [ordinary family thing happens twice]... [instruction]' rules-style episodes set at home at night", "Analog-horror presentation (per description: 'analog horror for the hours after the lights go out'); not visually verified", "'If Your [Mom/Sibling/Bed] Ever [uncanny repeat]... [ALL-CAPS COMMAND]'", "Joined Oct 18 2026 (about 1 month before snapshot); 22 videos; 33.8K subs; top video 3.3M in ~3 weeks; median recent ~80K", "riser", "high", "Fastest new launch found. ~22 uploads in ~1 month - production method unknown (AI use not verified either way). Domestic-uncanny + rule-command title is the hottest measured title pattern this month."),
 "@JustaRockinSpace": ("Just a Rock in Space", "animated folklore creatures / dark history (adjacent)", "Animated listicles of obscure mythical creatures and dark history", "Self-described '100% HUMAN MADE ANIMATIONS'; '[NO AI]' tag in titles", "'Disturbing Mythical Creatures You've Never Heard Of' + [NO AI]", "Joined Dec 2024; 368K subs from 16 videos; median recent ~797K (ratio 2.2); top 8.9M", "riser", "high", "Key case study: 'human-made / NO AI' positioning used as a selling point in 2026 titles."),
 "@TheRuleFiles": ("The Rule Files", "rules-based horror", "'If Moths Cover Your Porch Light... DON'T OPEN THE DOOR' (seen in topic scan, 52K views, ~3 weeks)", "unknown", "'If X... DON'T Y'", "Joined Mar 22 2026 (About page); subscriber count not shown/parsed", "small/new", "low", "Handle @TheRuleFiles is a guess - not verified to be the same channel as the topic-scan uploader. That uploader uses a moth premise - MOTHWAKE must avoid any similar 'moths at the porch light' plot to stay clearly original."),
 "@AnimatedHorrorFlicks": ("Animated Horror Flicks", "2D animated original horror", "Original standalone stories; seasonal specials (Easter/Halloween)", "2D animation (per description: 'original... all written, narrated...')", "'The Night Shift | Easter Special | Scary Stories Animated'", "172K subs; ~1 upload/90d; median ~68K (ratio 0.4)", "riser", "high", "Closest benchmark for original, written-for-animation stories; holiday-special titling."),
 "@MerrilyHorrorAnimations": ("Merrily Horror Animations", "2D animated folklore / urban legends", "Single-legend episodes (Teke Teke, Hanako-san, Gryla)", "2D animated (per titles)", "Legend name + Animated Horror Story | origin", "113K subs; median ~38.5K; 'GRYLA | Icelandic Christmas' episode in recent uploads", "riser", "high", "Folklore + Christmas folklore angle."),
 "@thrillerteller": ("Thriller Teller", "animated psychological horror short films", "Standalone psychological-horror shorts", "Animated short films (per description)", "ALL-CAPS premise | A Psychological Horror Short Film", "408K subs; top 10M; last upload ~4 months; median ~178K", "riser", "high", "Best evidence that 'psychological horror short film' framing travels; low upload rate still works."),
 "@MortHorror": ("Mort", "2D animated true-style horror", "Themed compilations (neighbor, delivery guy)", "Hand-made 2D; description states 'No automated content generation was used'", "Number + CREEPY + theme + ANIMATED", "552K subs; frequent; median ~138K", "benchmark", "high", "Explicit no-AI disclosure in description - positioning signal post-crackdown."),
 "@Seontbh": ("Seon", "animated horror storytime", "First-person short stories", "Animated (per titles)", "'I Saw a Face Inside My Apartment's Trash Chute'", "202K subs; median ~22.5K", "riser", "high", "Older channel, steady."),
 "@Surkee": ("Surkee", "3D (SFM) horror animation", "Standalone uncanny shorts ('They Look Like Trees')", "Source Filmmaker 3D (per description)", "Short uncanny phrase", "172K subs; median ~189K (ratio 1.1); Shorts median ~134K", "riser", "high", "High ratio with minimal, uncanny concepts."),
 "@greylockhorror": ("GREYLOCK", "analog horror (original tape series)", "Numbered tapes", "Analog/VHS (per titles)", "'TAPE 0NN - phrase   GREYLOCK [Analog...]'", "121K subs from 12 videos; dormant ~2y; ratio 3.5", "riser", "high", "Small catalogue, strong series identity."),
 "@StretchBackroomsAnimated": ("Stretch - Backrooms Animated & Explained", "backrooms animation", "Entity explainers + animated episodes", "Animated (per description)", "'\"Name\" - Backrooms Entity NN (Backrooms Animation)'", "139K subs; long-form dormant ~3y; Shorts median ~333K", "riser", "high", "Backrooms lore IP is community-owned; Shorts still strong."),
 "@xbackroom": ("XBackroom", "backrooms / liminal found footage", "Backrooms found-footage shorts and episodes", "3D found footage (per titles)", "'Backrooms - X (Found Footage)'", "1.61M subs; Shorts median ~141K; recent long-form median ~66K", "benchmark", "high", "Backrooms film (May 2026) era benchmark."),
 "@StrawberryNightmare": ("Strawberry Nightmare", "2D animated urban legends", "Urban legends + original stories", "2D (per titles)", "Title | Horror animation |", "Dormant ~3 years", "riser", "high", "Former riser now dormant; tier kept for comparison."),
 "@UrbanLegendsAnimated": ("Urban Legends Animated", "2D animated urban legends", "Very long compilations (median ~2h)", "Animated (per titles)", "Number + Urban Legends + month-year", "179K subs; median ~10K", "riser", "high", "Long compilation format with low ratio."),
 "@NightmareTales": ("Nightmare Tales", "2D animated scary stories", "Numbered episodes incl. Japanese legends", "2D (per titles)", "'NN | Title - Animated Scary Story'", "306K subs; last long-form ~1y", "riser", "high", "Australian; numbered-episode branding."),
 "@DrNoSleepAnimations": ("Dr. NoSleep Animations", "2D animated horror", "Situation compilations ('3 School Lockdown Horror Stories')", "Animated", "Number + situation + Horror Stories Animated", "657K subs; median ~68K; ~1h videos", "benchmark", "high", "Lockdown/situational premises historically top."),
 "@InsomniaStories": ("Insomnia Stories", "horror narration ('I work at' / remote jobs)", "First-person remote-job stories", "Narration", "'I Work on a Ship in the Bering Sea. Our Captain...'", "114K subs; median ~16.5K; ~1.4h videos", "riser", "high", "Remote/cold settings (Bering Sea, Lake Superior, Mount Rainier) recur in recent titles."),
 "@LighthouseHorror": ("Lighthouse Horror", "horror narration ('I work at' format)", "First-person job/rules stories", "Narration", "'I Work In A PRISON For Monsters...'", "913K subs; median ~189K; ~48m videos", "benchmark", "high", "Biggest 'I work at' narration benchmark found."),
 "@tales_of_the_grotesque": ("Tales of the Grotesque", "2D animated short horror series", "Episodic grotesque shorts with teasers", "Animated series (per description)", "'Title - Episode NN | Tales of the grotesque'", "Joined Apr 2023; 157K subs; median ~19K", "riser", "medium", "Indonesia-based, English titles; episodic branding."),
 "@vintageeight": ("Vintage Eight", "analog horror (original series)", "Original series (Tangi Virus) + tapes", "Analog/VHS", "'Unknown Tape 00N (analog horror)'", "114K subs; recent median ~1.3K vs top 1.8M (4y ago)", "riser", "high", "Decay after early analog-horror wave."),
 "@crowmudgeon": ("Crowmudgeon", "internet-horror analysis", "Long analyses of analog horror series", "Commentary", "'The Loneliest World in Analog Horror'", "231K subs; median ~360K (ratio 1.56)", "riser", "high", "'Loneliest world' analysis 2.2M in 6 months - loneliness/emptiness theme demand."),
 # ---------- benchmarks ----------
 "@LlamaArts": ("Llama Arts", "2D animated horror (true-style stories)", "Submitted 'true' stories animated; anthology", "2D cartoon", "'True X Horror Stories Animated'", "2.57M subs; last long-form ~1y; recent median ~564K", "benchmark", "high", "Recent upload titled 'An A.I Written Halloween Horror Story Animated'."),
 "@Snarled": ("SNARLED (Something Scary)", "2D animated horror storytelling", "Weekly 'Something Scary' episodes incl. fan-submitted stories", "2D animated", "'FAN SUBMITTED STORY // Something Scary | Snarled'", "2.27M subs; recent median ~4.3K views (measured)", "benchmark", "high", "Severe views-to-subs decline vs 8-12M classics - legacy subs do not guarantee reach."),
 "@mrnightmare": ("Mr. Nightmare", "horror narration (true-style)", "Themed 'N Scary TRUE X Horror Stories'", "Narration over imagery", "Number + Scary TRUE + theme", "7.16M subs; median ~864K; frequent", "benchmark", "high", ""),
 "@MrBallen": ("MrBallen", "dark/mysterious true stories (adjacent)", "Host-led true stories", "Host on camera", "Plain-sentence mystery hook", "11.4M subs; median ~1.2M", "benchmark", "high", "Adjacent non-fiction; title style worth noting (plain-sentence hook)."),
 "@LOCAL58TV": ("LOCAL58TV", "analog horror (original)", "Short broadcast-intrusion shorts", "Analog TV broadcast pastiche", "'LOCAL58TV - Title'", "686K subs; 16 videos; recent median ~753K", "benchmark", "high", "Genre founder (Kris Straub)."),
 "@AlexxKister": ("Alex Kister (The Mandela Catalogue)", "analog horror (original)", "Original series + standalone pieces", "Analog/VHS", "Series title + volume", "1.08M subs; 32 videos; feature adaptation set for June 9 2028 (press)", "benchmark", "high", "IP-to-film pathway."),
 "@kanepixels": ("Kane Pixels (Backrooms)", "found footage / liminal (original)", "Serialized found-footage", "3D found footage", "'Backrooms - Title'", "3.7M subs; median ~2.7M; A24 feature May 29 2026", "benchmark", "high", "Category-defining; film success raised liminal interest (press)."),
 "@GeminiHomeEntertainment": ("Gemini Home Entertainment", "analog horror (original)", "Fake educational VHS anthology", "Analog VHS educational pastiche", "Short ALL-CAPS titles", "416K subs; 19 videos; new upload 1.3M in ~1 month", "benchmark", "high", ""),
 "@Nexpo": ("Nexpo", "internet-horror analysis", "Lost media / ARG / analog horror explainers", "Commentary", "'The Darkest X'", "4.01M subs; median ~2.25M", "benchmark", "high", "Adjacent amplifier."),
 "@Wendigoon": ("Wendigoon", "horror/mystery explainers (adjacent)", "Iceberg explainers (recent: Cryptid Iceberg series)", "Commentary", "'The X of the Cryptid Iceberg'", "4.75M subs; median ~2.15M; 2-4h videos", "benchmark", "high", "Recent 4-part Cryptid Iceberg - cryptid demand signal."),
 "@HorrorShortsParty": ("Horror Shorts Party", "2D animated true-style horror", "Topical themed compilations ('3 GTA 6 True Horror Stories')", "2D animated", "Number + trending topic + True Horror Stories ANIMATED", "1.71M subs; median ~375K; frequent", "benchmark", "high", "Topical hooks (GTA 6, Charlie Charlie)."),
 "@WanseeEntertainment": ("Wansee Entertainment", "2D animated horror (mature)", "'N TRUE Scary Stories Animated'", "2D animated (mature audiences per description)", "Number + TRUE + Animated", "1.84M subs; median ~232K", "benchmark", "high", "Multi-language spin-offs (FR/DE/Hindi seen in search)."),
 "@IMRScaryTales": ("IMR Scary Tales", "2D animated true-style horror", "Brand/job-themed compilations ('3 True DoorDash Horror Stories')", "2D animated", "Number + True + brand/place", "1.25M subs; median ~93K", "benchmark", "high", "Template format with brand names."),
 "@Darksomnium": ("The Dark Somnium", "horror narration", "Creepypasta / 'I'm a guard at...' narration", "Narration + original music", "Quoted first-person premise", "884K subs; recent views not parsed", "benchmark", "medium", "Recent-video parse failed in snapshot; views unknown."),
 "@SCP": ("SCP Explained - Story & Animation", "SCP animated explainers", "SCP entries animated/explained", "Animated", "'SCP-NNNN Title'", "2.49M subs; median ~43.5K long-form; Shorts median ~178K", "benchmark", "high", "Shorts outperform long-form by ~4x (median)."),
 "@CreepsMcPasta": ("CreepsMcPasta", "creepypasta narration", "Narrated creepypasta", "Narration", "Quoted story title + Creepypasta", "2.08M subs; median ~54.5K", "benchmark", "high", "Legacy narrator; low ratio."),
 "@MrCreeps": ("Mr. Creeps", "creepypasta narration", "Narrated creepypasta & rules stories", "Narration", "Quoted title + Creepypasta", "1.03M subs; median ~48K", "benchmark", "high", ""),
}

def main():
    snaps = {}
    for s in SNAPS:
        p = os.path.join(ROOT, s)
        for c in json.load(open(p)):
            prev = snaps.get(c["handle"])
            # keep the snapshot with more data (b-run re-fetched some handles)
            if prev is None or (len(c.get("popular_videos", [])) + len(c.get("recent_videos", []))
                                >= len(prev.get("popular_videos", [])) + len(prev.get("recent_videos", []))):
                c["_src"] = s
                snaps[c["handle"]] = c
    cols = ["channel_name", "url", "category", "subscribers", "subscribers_source", "subscribers_as_of",
            "created_date", "upload_frequency", "recent_performance", "top_videos", "views_to_subs_signal",
            "shorts_vs_longform", "typical_duration", "story_format", "visual_style", "thumbnail_pattern",
            "engagement_notes", "growth_signals", "tier", "confidence", "notes"]
    rows = []
    for h, a in ANNOT.items():
        c = snaps.get(h)
        if not c:
            continue
        name, cat, fmt, vis, tpat, growth, tier, conf, notes = a
        subs = num(c.get("subscribers"))
        rv = c.get("recent_videos", [])
        v10 = [x for x in (num(v["views"]) for v in rv[:10]) if x is not None]
        dd = [days(v["published"]) for v in rv]
        n90 = sum(1 for x in dd if x is not None and x <= 90)
        durs = [x for x in (dur(v["duration"]) for v in rv[:10]) if x]
        sh = c.get("recent_shorts", [])
        shv = [x for x in (num(s["views"]) for s in sh) if x is not None]
        med = statistics.median(v10) if v10 else None
        ratio = (med / subs) if med and subs else None
        if ratio is None:
            sig = "unknown"
        else:
            lab = ("very high" if ratio >= 1 else "high" if ratio >= 0.3 else "normal" if ratio >= 0.1 else "low")
            sig = f"{lab}: median of last 10 long-form views / subs = {ratio:.2f} (measured)"
        if rv and (dd[0] is None or sum(x is None for x in dd) > len(dd) // 2):
            uf = "unknown (recent upload dates not parseable in snapshot)"
        elif rv:
            uf = (f"{n90}{'+' if n90 >= len(rv) else ''} long-form uploads in last ~90d "
                  f"(from {len(rv)} most recent; YouTube relative dates); last long-form ~{dd[0] if dd[0] is not None else 'unknown '}d ago")
        else:
            uf = "unknown (no long-form videos tab data)"
        perf = (f"median views last 10 long-form = {int(med):,} (YouTube-rounded, measured {AS_OF})" if med else "unknown")
        pv = c.get("popular_videos", [])
        if pv and all(v.get("views") and "view" not in (v.get("published") or "") for v in pv[:3]):
            top = "; ".join(f"{v['title'][:60]} ({v['views']}, {v['published']})" for v in pv[:3]) + " [Popular sort]"
        elif rv:
            best = sorted([v for v in rv if num(v["views"]) is not None], key=lambda v: num(v["views"]), reverse=True)[:2]
            top = ("Popular sort not returned; best of 15 most recent: " +
                   "; ".join(f"{v['title'][:60]} ({v['views']} views, {v['published']})" for v in best))
        else:
            top = "unknown"
        svl = (f"videos tab: {len(rv)} recent long-form parsed; shorts tab: {len(sh)} recent Shorts visible"
               + (f", median Shorts views {int(statistics.median(shv)):,}" if shv else "")
               + f"; total public videos {c.get('video_count') or 'unknown'}")
        rows.append({
            "channel_name": name, "url": "https://www.youtube.com/" + h, "category": cat,
            "subscribers": c.get("subscribers") or "unknown",
            "subscribers_source": "youtube.com channel /about page (public ytInitialData, rounded by YouTube)" if c.get("subscribers") else "unknown",
            "subscribers_as_of": AS_OF if c.get("subscribers") else "unknown",
            "created_date": (c.get("joined") or "unknown") + (" (YouTube 'Joined' date; may predate current content)" if c.get("joined") else ""),
            "upload_frequency": uf, "recent_performance": perf, "top_videos": top,
            "views_to_subs_signal": sig, "shorts_vs_longform": svl,
            "typical_duration": (fmt_s(statistics.median(durs)) + " median of last 10 long-form") if durs else "unknown",
            "story_format": fmt, "visual_style": vis,
            "thumbnail_pattern": "thumbnails unknown (i.ytimg.com blocked); title pattern: " + tpat,
            "engagement_notes": "unknown - likes/comments not collected (watch pages redirect to a blocked host); total views " + (c.get("total_views") or "unknown"),
            "growth_signals": growth, "tier": tier, "confidence": conf,
            "notes": (notes + f" | snapshot: research/{c['_src']} fetched {c.get('fetched_at')}").strip(" |"),
        })
    out = os.path.join(ROOT, "COMPETITOR_DATABASE.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "rows ->", out)

if __name__ == "__main__":
    main()
