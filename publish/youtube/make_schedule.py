"""YouTube schedule (owner request 2026-11-21): main slot 18:00 daily from 22 Nov (13 Shorts, strategy order);
SAVE FILE second slot 13:00 22-26 Nov while GTA 6 interest is high [M: ~60% of peak on 20 Nov]. Times are channel-local [E]."""
import json, shutil
from pathlib import Path
R = Path(__file__).resolve().parents[2]
TAIL = "\n\nA MOTHWAKE original fiction story. Some things should stay asleep.\nFind the hidden moth in every episode."
S = [
 ("2026-11-22","13:00","episodes/SAVE_FILE/masters/G1_MidnightLaunch_master_v2.mp4","He bought the new game at midnight. It knew his window.","Would you keep playing?","#horror #animatedhorror #gaming",True),
 ("2026-11-22","18:00","episodes/PILOT_01/masters/SH012_RainSounds_master_v7.mp4","I paused the rain sounds. The tapping didn't.","Did you spot the moth?","#horror #animatedhorror #rainsounds",False),
 ("2026-11-23","13:00","episodes/SAVE_FILE/masters/G2_GhostCar_master_v2.mp4","Everyone's hunting the ghost car. It's in our car park.","Would you get in?","#horror #animatedhorror #gaming",True),
 ("2026-11-23","18:00","episodes/PILOT_01/masters/SH025_WhichDoorP1_master_v2.mp4","Which door is my front door? Choose before 6 a.m.","Left or right? Most votes decides Part 2.","#horror #animatedhorror #whichdoor",False),
 ("2026-11-24","13:00","episodes/SAVE_FILE/masters/G3_RulesAfterMidnight_master_v2.mp4","Rules for playing after midnight. Rule 4 isn't a game.","What's your late-night gaming rule?","#horror #animatedhorror #gaming",True),
 ("2026-11-24","18:00","episodes/PILOT_01/masters/SH019_NightlightRules_master_v9.mp4","My little brother's nightlight has three rules","Which rule would you break first?","#horror #animatedhorror #horrorrules",False),
 ("2026-11-25","13:00","episodes/SAVE_FILE/masters/G4_ChooseWisely_master_v2.mp4","The game gave him a choice. Then someone knocked.","Let him in or keep playing?","#horror #animatedhorror #gaming",True),
 ("2026-11-25","18:00","episodes/WEEK_01/masters/SH003_HoldStill_master_v2.mp4","Night mode blurs anything that moves. Except him.","Pause on the last photo. How many are sharp?","#horror #animatedhorror #nightmode",False),
 ("2026-11-26","13:00","episodes/SAVE_FILE/masters/G5_SecretEnding_master_v2.mp4","He found the secret ending. It's our building.","Did you spot the moth in every part?","#horror #animatedhorror #gaming",True),
 ("2026-11-26","18:00","episodes/WEEK_01/masters/SH015_Streetlamp_master_v2.mp4","They fixed the streetlamp. Who is standing under it?","Would you walk past it?","#horror #animatedhorror #winterhorror",False),
 ("2026-11-27","18:00","episodes/WEEK_01/masters/SH022_SleepParalysis_master_v2.mp4","How to survive sleep paralysis (rule 3 matters)","Has this ever happened to you?","#horror #animatedhorror #sleepparalysis",False),
 ("2026-11-28","18:00","episodes/WEEK_01/masters/SH028_PauseAtSeven_master_v2.mp4","Pause at 7 seconds. How many people do you count?","Comment your count before you rewatch.","#horror #animatedhorror #pauseit",False),
 ("2026-11-29","18:00","episodes/WEEK_02/masters/SH005_LastPrescription_master_v2.mp4","Same customer every night. Her husband died in 2017.","Would you deliver to flat eight?","#horror #animatedhorror #nightshift",False),
 ("2026-11-30","18:00","episodes/WEEK_02/masters/SH010_WrittenFromInHere_master_v2.mp4","I wrote \"hi\" on the bus window. Who wrote back?","Where was it sitting?","#horror #animatedhorror #nightbus",False),
 ("2026-12-01","18:00","episodes/WEEK_02/masters/SH026_KettleInTheGlass_master_v2.mp4","One thing in this kitchen is wrong. Can you find it?","Comment your time.","#horror #animatedhorror #findit",False),
 ("2026-12-02","18:00","episodes/WEEK_02/masters/SH016_SixtySecondLight_master_v4.mp4","Our hallway light has rules. Don't argue with it.","What's your number?","#horror #animatedhorror #horrorrules",False),
 ("2026-12-03","18:00","episodes/WEEK_02/masters/SH001_DryerSix_master_v4.mp4","Dryer six gave back everything I lost. Then me.","Which one of us is typing this?","#horror #animatedhorror #laundromat",False),
 ("2026-12-04","18:00","episodes/WEEK_02/masters/SH009_StillCounting_master_v2.mp4","Theo always wins hide-and-seek. Now I know why.","How high has it counted now?","#horror #animatedhorror #hideandseek",False),
]
out = []
for k, (d, t, src, title, q, tags, gta) in enumerate(S, 1):
    f = f"{k:02d}_{Path(src).stem.split('_master')[0]}.mp4"
    shutil.copyfile(R / src, Path(__file__).parent / f) if not (Path(__file__).parent / f).exists() else None
    desc = q + TAIL + ("\nMade for everyone up all night with the new open-world games." if gta else "") + "\n\n" + tags
    assert len(title) <= 100 and len(desc) <= 5000
    out.append({"n": k, "file": f, "date": d, "time": t, "title": title, "description": desc, "status": "pending"})
(Path(__file__).parent / "schedule.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
print(len(out), "videos ready")
