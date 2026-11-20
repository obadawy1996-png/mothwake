"""SAVE FILE edit JSONs (times = narration word timings + 1.2 s hook card)."""
import json, os
W="episodes/SAVE_FILE/"; F=W+"flow/"; S=W+"audio/sfx/"; V=W+"audio/vo/"
def cut(c,i,o,bed=-26): return {"src":F+c+".mp4","in":i,"out":o,"bed_db":bed}
def sfx(f,i,o,at,db): return {"file":S+f,"in":i,"out":o,"at":at,"db":db}
def cap(s,e,t,st="Cap"): return {"start":s,"end":e,"text":t,"style":st}
def card(s,e,t): return {"start":s,"end":e,"text":t}
def tag(n): return {"start":0,"end":1.2,"text":f"SAVE FILE  ·  {n}/5","x":540,"y":330,"size":40}
def ed(name,g,vo_len,cuts,sfxs,caps,cards,labels=()):
    return {"name":name,"out_dir":W+"masters","watermark":"brand/kit/watermark_gold.png","caption_style":{"size":80,"marginv":780},
            "cuts":cuts,"vo":[{"file":V+f"IVY_{g}.mp3","in":0,"out":vo_len,"at":1.2}],"sfx":sfxs,"captions":caps,"cards":cards,"labels":list(labels)}
E={}
E["G1"]=ed("G1_MidnightLaunch_master","G1",23.6,
 [cut("G1_C5",4.0,5.2),cut("G1_C1",0,3.5),cut("G1_C2",0,8),cut("G1_C3",0,4.0),cut("G1_C4",2.0,8.0),cut("G1_C5",0,6.0)],
 [sfx("nightlight_hum.wav",0,22,1.2,-22),sfx("low_drone.wav",0,8,12.7,-16),sfx("flicker_buzz.wav",0,0.5,22.4,-10),sfx("presence_swell.wav",0,3.5,22.6,-6)],
 [cap(1.2,3.4,"Jun queued till midnight\nfor the *new game*."),cap(4.2,7.0,"The first screen is\na *postcard* of the city."),cap(8.7,11.4,"Sunshine. *Palm trees*."),
  cap(12.0,14.8,"And in the corner...\na *grey building*."),cap(15.7,16.9,"*Our* building."),cap(18.1,21.4,"Third floor. *His window*.\nThe light on."),
  cap(22.3,24.4,"And someone\n*standing in it*.","Whisper")],
 [card(0,1.2,"HE BOUGHT THE NEW GAME\nAT MIDNIGHT. IT KNEW\nHIS WINDOW."),card(25.4,28.7,"WOULD YOU\nKEEP PLAYING?")],[tag(1)])
E["G2"]=ed("G2_GhostCar_master","G2",22.8,
 [cut("G2_C5",5.0,6.2),cut("G2_C1",0,4.0),cut("G2_C2",0,5.0),cut("G2_C3",1.0,5.0),cut("G2_C4",0,4.0),cut("G2_C5",0,8.0)],
 [sfx("nightlight_hum.wav",0,13,1.2,-22),sfx("low_drone.wav",0,8,10.2,-16),sfx("bus_rumble.wav",0,8,18.2,-16),
  sfx("lullaby.wav",0,5.58,20.9,-14),sfx("presence_swell.wav",0,3.5,21.4,-8)],
 [cap(1.2,3.6,"Everyone online is hunting\nthe *ghost car*."),cap(5.0,8.0,"White. *No driver*.\nOnly at night."),cap(9.7,11.2,"Jun found it *on day one*."),
  cap(12.8,13.8,"*Not* in the game."),cap(15.0,18.0,"In *our car park*.\nUnder the dead streetlamp."),cap(19.3,20.4,"*Engine running*."),
  cap(21.1,23.6,"Playing the music\nfrom *his save screen*.","Whisper")],
 [card(0,1.2,"EVERYONE'S HUNTING\nTHE GHOST CAR."),card(24.0,26.2,"WOULD YOU\nGET IN?")],[tag(2)])
E["G3"]=ed("G3_RulesAfterMidnight_master","G3",26.32,
 [cut("G3_C5",6.0,7.2),cut("G3_C1",0,7.0),cut("G3_C2",0,7.0),cut("G3_C4",0,7.5),cut("G3_C3",4.0,6.5),cut("G3_C5",1.0,8.0)],
 [sfx("nightlight_hum.wav",0,22,1.2,-22),sfx("lullaby.wav",0,5.58,8.9,-16),sfx("low_drone.wav",0,8,15.2,-16),
  sfx("slow_breath.wav",0,3,24.0,-8),sfx("presence_swell.wav",0,3.5,25.4,-6)],
 [cap(1.2,2.9,"Jun wrote *rules*\nfor the new game."),cap(3.8,6.5,"*One*: never let your\ncharacter sleep."),cap(7.5,11.7,"*Two*: if the radio plays\na lullaby, save and quit."),
  cap(12.5,15.5,"*Three*: never pause\non a dark street."),cap(17.0,17.8,"*Four*...","Whisper"),
  cap(18.6,22.0,"if your character lies down,\nclose *your own eyes* too.","Whisper"),cap(23.3,24.4,"I asked him *why*."),
  cap(25.4,27.4,"So it doesn't\n*close them for you*.","Whisper")],
 [card(0,1.2,"RULES FOR PLAYING\nAFTER MIDNIGHT."),card(29.0,32.2,"WHAT'S YOUR RULE\nFOR LATE-NIGHT GAMING?")],[tag(3)])
E["G4"]=ed("G4_ChooseWisely_master","G4",22.32,
 [cut("G4_C5",5.0,6.2),cut("G4_C1",0,8.0),cut("G4_C3",0,5.0),cut("G4_C4",0,2.8),cut("G4_C2",0,4.0),cut("G4_C5",0,7.0)],
 [sfx("nightlight_hum.wav",0,9,1.2,-22),sfx("knock3.wav",0,3.32,9.4,-2),sfx("low_drone.wav",0,8,9.2,-14),sfx("knock3.wav",0,3.32,14.4,-4),
  sfx("presence_swell.wav",0,3.5,20.4,-8)],
 [cap(1.2,1.9,"*Night three*."),cap(2.7,4.3,"The game gave Jun\na *choice*."),cap(5.5,8.0,"*Let him in*.\nOr keep playing."),cap(9.4,10.6,"Then *a knock*."),
  cap(11.8,12.6,"*Not* in the game."),cap(13.6,15.9,"On his front door.\n*Same rhythm*."),cap(17.0,19.1,"His thumb is still\nover the *button*."),
  cap(20.1,23.1,"What would *you* pick?\nTell him before he does.","Whisper")],
 [card(0,1.2,"THE GAME GAVE HIM\nA CHOICE. THEN\nSOMEONE KNOCKED."),card(24.0,28.0,"LET HIM IN or KEEP PLAYING?\nCOMMENT BEFORE JUN DOES.")],
 [tag(4),{"start":1.2,"end":4.6,"text":"LET HIM IN","x":340,"y":900,"size":38},{"start":1.2,"end":4.6,"text":"KEEP PLAYING","x":800,"y":900,"size":38}])
E["G5"]=ed("G5_SecretEnding_master","G5",23.92,
 [cut("G5_C5",5.5,6.7),cut("G5_C1",0,6.8),cut("G5_C2",3.5,7.5),cut("G5_C3",2.5,5.0),cut("G5_C4",0,3.0),cut("G5_C5",1.0,8.0),cut("G5_C3",5.0,8.0)],
 [sfx("nightlight_hum.wav",0,26,1.2,-22),sfx("low_drone.wav",0,8,8.0,-16),sfx("save_chime.wav",0,1.05,15.0,-6),
  sfx("presence_swell.wav",0,3.5,18.0,-6),sfx("low_drone.wav",0,8,20.0,-12)],
 [cap(1.2,2.6,"Jun found the *secret ending*."),cap(3.5,6.5,"Past the beach,\npast the *edge of the map*..."),cap(7.5,10.1,"a grey building. *Ours*."),
  cap(11.2,13.6,"Third floor.\nA *moth* on the window."),cap(14.7,15.6,"He pressed *save*."),cap(16.9,19.0,"And the *real moth*\nlanded on his screen."),
  cap(20.1,21.2,"It's not an ending.","Whisper"),cap(22.2,25.0,"It's a *save point*.\nFor the building.","Whisper")],
 [card(0,1.2,"HE FOUND THE\nSECRET ENDING."),card(25.4,27.5,"SAVE FILE  ·  5/5\nSOME THINGS SHOULD STAY ASLEEP.")],[tag(5)])
for k,v in E.items():
    p=f"{W}edits/{k}_edit.json"
    if not os.path.exists(p): json.dump(v,open(p,"w",encoding="utf-8"),indent=1,ensure_ascii=False)
    print(k, round(sum(c["out"]-c["in"] for c in v["cuts"]),2))
