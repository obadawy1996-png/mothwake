"""Generates the week-2 edit JSONs (times = narration word timings + 1.2 s hook card)."""
import json, os
W="episodes/WEEK_02/"; F=W+"flow/"; S=W+"audio/sfx/"; V=W+"audio/vo/"
def cut(c,i,o,bed=-26,**k): return dict(src=F+c+".mp4",**{"in":i,"out":o},bed_db=bed,**k)
def sfx(f,i,o,at,db): return dict(file=S+f,**{"in":i,"out":o},at=at,db=db)
def cap(s,e,t,st="Cap"): return dict(start=s,end=e,text=t,style=st)
def card(s,e,t): return dict(start=s,end=e,text=t)
def ed(name,cuts,vo,sfxs,caps,cards,labels=()):
    return dict(name=name,out_dir=W+"masters",watermark="brand/kit/watermark_gold.png",
        caption_style=dict(size=80,marginv=780),cuts=cuts,vo=vo,sfx=sfxs,captions=caps,cards=cards,labels=list(labels))
E={}
E["SH005"]=ed("SH005_LastPrescription_master",
 [cut("SH005_C4",5.5,6.7),cut("SH005_C1a",0.5,6.5),cut("SH005_C2a",0.0,5.0),cut("SH005_C2b",4.0,8.0),cut("SH005_C3",0.5,7.5),cut("SH005_C4",0.0,8.0)],
 [dict(file=V+"IVY_SH005.mp3",**{"in":0,"out":27.2},at=1.2)],
 [sfx("nightlight_hum.wav",0,22,1.2,-22),sfx("low_drone.wav",0,8,9.6,-18),sfx("bell.wav",0,2.5,23.3,-6),
  sfx("low_drone.wav",0,8,23.2,-12),sfx("presence_swell.wav",0,3.5,24.0,-6)],
 [cap(1.2,3.6,"Same customer. *Every night*."),cap(3.6,5.0,"Same prescription."),cap(5.3,8.3,"Mrs Ferris. *Sleeping tablets*\nfor her husband."),
  cap(9.8,12.0,"Her husband\n*died nine years ago*."),cap(13.1,15.7,"'When he wakes, dear,\nhe *wanders*.'","Whisper"),cap(17.0,18.8,"Every night *for a year*."),
  cap(20.1,21.3,"Tonight she *didn't come*."),cap(22.1,23.4,"Then *the bell*."),cap(24.6,26.7,"'My wife is *sleeping* now.'","Whisper"),
  cap(26.8,28.7,"'You'll bring them\nto *flat eight*.'","Whisper")],
 [card(0,1.2,"SHE CAME EVERY NIGHT.\nTONIGHT, HE DID."),card(29.0,31.2,"WOULD YOU DELIVER\nTO FLAT EIGHT?")],
 [dict(start=9.8,end=12.2,text="FERRIS, ARTHUR  ·  DECEASED 2017",x=540,y=330,size=40)])
E["SH010"]=ed("SH010_WrittenFromInHere_master",
 [cut("SH010_C3",5.0,6.2),cut("SH010_C1",0.5,7.5),cut("SH010_C2",0.0,6.0),cut("SH010_C3",3.0,6.0),cut("SH010_C4",0.5,7.5)],
 [dict(file=V+"IVY_SH010.mp3",**{"in":0,"out":19.2},at=1.2)],
 [sfx("bus_rumble.wav",0,23,1.2,-14),sfx("low_drone.wav",0,8,14.2,-14),sfx("slow_breath.wav",0,3,17.4,-6),sfx("presence_swell.wav",0,3.5,18.6,-6)],
 [cap(1.2,2.9,"I wrote *hi*\non the bus window."),cap(3.6,4.8,"Something *wrote back*."),cap(6.2,7.6,"It knew *my name*."),
  cap(8.6,9.9,"From outside, I thought."),cap(10.5,13.7,"Then I realised...\nI could *read it*."),cap(14.9,16.9,"From outside,\nit'd be *backwards*."),
  cap(17.7,19.8,"It was written\n*from in here*.","Whisper")],
 [card(0,1.2,"SOMETHING WROTE BACK\nON MY BUS WINDOW."),card(21.4,24.2,"WHERE WAS IT SITTING?\nCOMMENT YOUR GUESS.")],
 [dict(start=8.2,end=14.2,text="HELLO IVY",x=800,y=760,size=58)])
E["SH026"]=ed("SH026_KettleInTheGlass_master",
 [cut("SH026_C1",0.0,1.2),cut("SH026_C1",1.2,3.4),cut("SH026_C2",0.0,8.0),cut("SH026_C3",1.0,7.0),cut("SH026_C4",0.5,8.0)],
 [dict(file=V+"IVY_SH026.mp3",**{"in":0,"out":18.72},at=1.2)],
 [sfx("low_drone.wav",0,8,1.2,-20),sfx("low_drone.wav",0,8,11.4,-14),sfx("switch_click.wav",0,0.5,17.6,-2),
  sfx("kettle_rumble.wav",0,7,17.7,-10),sfx("presence_swell.wav",0,3.5,18.6,-6)],
 [cap(1.2,2.9,"One thing in this kitchen\nis *wrong*."),cap(3.7,4.6,"*Find it*."),cap(6.0,7.4,"I came down for *water*."),
  cap(8.4,10.2,"Didn't notice. *Did you?*"),cap(11.6,13.1,"The kettle *in the glass*\nis boiling."),cap(13.9,14.9,"The real one's *cold*."),
  cap(15.9,17.6,"Someone in there\nis *making tea*.","Whisper"),cap(18.8,19.9,"For *two*.","Whisper")],
 [card(0,1.2,"ONE THING IN THIS\nKITCHEN IS WRONG."),card(21.6,24.9,"HOW FAST DID YOU FIND IT?\nCOMMENT YOUR TIME.")])
E["SH016"]=ed("SH016_SixtySecondLight_master",
 [cut("SH016_C4",6.0,7.2),cut("SH016_C1",0.0,7.5),cut("SH016_C2",0.0,8.0),cut("SH016_C3",0.0,8.0),cut("SH016_C4",0.5,8.0)],
 [dict(file=V+"IVY_SH016.mp3",**{"in":0,"out":27.84},at=1.2)],
 [sfx("switch_click.wav",0,0.5,1.6,-2),sfx("nightlight_hum.wav",0,12,1.6,-22),sfx("timer_ticks.wav",0,11,1.6,-20),
  sfx("flicker_buzz.wav",0,0.5,12.9,-6),sfx("low_drone.wav",0,8,13.2,-14),sfx("key_rattle.wav",0,1.08,16.9,-8),
  sfx("low_drone.wav",0,8,21.0,-12),sfx("presence_swell.wav",0,3.5,25.0,-6)],
 [cap(1.2,3.3,"Our hallway light lasts\n*sixty seconds*."),cap(4.3,5.0,"There are *rules*."),cap(6.0,7.3,"*One*: press once."),
  cap(8.4,9.4,"*Two*: walk."),cap(10.4,11.2,"It hears *running*."),cap(12.0,13.8,"*Three*: if it goes out early..."),
  cap(14.5,16.5,"stand still...\nand *say your number*."),cap(17.6,18.6,"*Nine*.","Whisper"),cap(19.8,21.3,"*Four*: don't argue."),
  cap(22.5,25.3,"I didn't argue.\nSo *it kept it*."),cap(25.5,28.5,"Everyone who didn't argue\n*lives here*.")],
 [card(0,1.2,"OUR HALLWAY LIGHT\nHAS RULES."),card(29.4,32.2,"WHAT'S YOUR NUMBER?\nDON'T ARGUE.")])
E["SH001"]=ed("SH001_DryerSix_master",
 [cut("SH001_C4",3.0,4.2),cut("SH001_C1",0.0,8.0),cut("SH001_C2",2.0,8.0),cut("SH001_C3",0.0,8.0),cut("SH001_C4",0.0,7.0)],
 [dict(file=V+"IVY_SH001.mp3",**{"in":0,"out":25.12},at=1.2)],
 [sfx("dryer_hum.wav",0,29,1.2,-15),sfx("tap_one.wav",0,0.3,8.4,-4),sfx("switch_click.wav",0,0.5,13.9,-4),
  sfx("low_drone.wav",0,8,15.2,-14),sfx("presence_swell.wav",0,3.5,23.4,-6)],
 [cap(1.2,2.4,"*Dryer six* was running."),cap(3.3,4.3,"I hadn't put *anything* in."),cap(5.4,7.2,"3 a.m. *Just me*."),
  cap(8.8,9.8,"It gave me a *sock*."),cap(10.8,12.6,"Mine. From when\nI was *seven*."),cap(13.9,15.9,"Then *everything I ever lost*."),
  cap(17.4,19.8,"Then my *scarf*.\nThe one I was wearing."),cap(21.1,22.8,"I looked up.\n*Through the glass*."),
  cap(24.2,26.0,"She folds better\n*than I do*.","Whisper")],
 [card(0,1.2,"DRYER SIX WAS RUNNING.\nI PUT NOTHING IN."),card(27.4,30.2,"WHICH ONE OF US\nIS TYPING THIS?")])
E["SH009"]=ed("SH009_StillCounting_master",
 [cut("SH009_C3",6.0,7.2),cut("SH009_C1",0.0,4.5),cut("SH009_C2",1.0,5.0),cut("SH009_C3",4.0,7.5),cut("SH009_C4",0.0,8.0),cut("SH009_C5",0.0,8.0)],
 [dict(file=V+"IVY_SH009.mp3",**{"in":0,"out":11.45},at=1.2),dict(file=V+"IVY_SH009_counter.wav",**{"in":0,"out":5.0},at=12.65,db=2),
  dict(file=V+"IVY_SH009.mp3",**{"in":16.4,"out":22.64},at=17.6)],
 [sfx("low_drone.wav",0,8,1.2,-22),sfx("low_drone.wav",0,8,9.7,-14),sfx("low_drone.wav",0,8,17.7,-12),
  sfx("switch_click.wav",0,0.5,25.6,-2),sfx("presence_swell.wav",0,3.5,25.9,-6)],
 [cap(1.2,3.0,"Theo always wins\n*hide-and-seek*."),cap(4.0,4.9,"I learned *why*."),cap(5.8,8.0,"Nineteen, twenty. *Coming*."),
  cap(8.9,10.4,"He said: *shh*.","Whisper"),cap(11.1,12.3,"It's *still counting*.","Whisper"),
  cap(12.7,17.4,"*Three thousand, four hundred\nand eleven...*","Whisper"),cap(17.7,18.7,"He wasn't *winning*."),
  cap(19.3,21.5,"He's been hiding.\n*Since last winter*."),cap(22.5,23.6,"*Ready or not*.","Whisper")],
 [card(0,1.2,"THEO ALWAYS WINS\nHIDE-AND-SEEK."),card(26.0,29.2,"HOW HIGH HAS IT\nCOUNTED NOW?")])
for k,v in E.items():
    p=f"{W}edits/{k}_edit.json"
    if not os.path.exists(p): json.dump(v,open(p,"w",encoding="utf-8"),indent=1,ensure_ascii=False)
    print(k, round(sum(c["out"]-c["in"] for c in v["cuts"]),2))
