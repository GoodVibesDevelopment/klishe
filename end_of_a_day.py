# 1) SETTINGS
Clock.set_time(0)
Clock.midi_nudge=0.04
Clock.bpm=120
Scale.default=Scale.minor

var.mp = P[(3,5,7),(4,6,8),(0,2,4)]
p1 >> MidiOut(var.mp+(7,0,0), dur=[4,4,8], amp=1, channel=0, chop=2,oct=4)
p2 >> karp([0,2,4],dur=PStep(6,.4),oct=[5,6,],amp=.6,cut=.3,room=.3,mix=0)

p2.dur=PStep(6,.25)
d2 >> play("|x1| ",amp=1.2,rate=1.4).sometimes("amen")
d3 >> play(" s (s[ss])",dur=1/2)

s1.stop()
p4.stop()
p2.dur=PStep(6,.25)
p2.stop()
p1.amp=0
# BASS
b1 >> jbass(p1.pitch[0], amp=.4, dur=P[1,1]|PDur(3,8), sus=0.3, oct=4)
# DRUMS
d1 >> play("x ")
d2 >> play("|x1| ").sometimes("amen")
d3 >> play(" s (s[ss])",dur=1/2)
d4 >> play("[--]S", amp=.5)
d5 >> play("c", dur=PDur(3,5), spin=8, amp=.4, pshift=sinvar([0,7],8))
d7 >> play("<  H ><  * ><  ( =) >", room=.8,dur=1/2)
d8 >> play("=", dur=32)
# OTHER STUFF
p3 >> charm(P[0,2,4,3,1,4,3,2]*var([1,2],[32,32]), dur=var([1/2,1/4],[12,4]), sus=P[0.2,.2,.3,.1,.5,1].shuffle(8), hpf=linvar([300,1200],4), amp=1.3,spin=8)
# p3.stop()

s1 >> space(p1.pitch[[1,2]] & P[13,14], dur=4, oct=5, hpf=1500,chop=16,amp=.2)
s1.chop=PRand(P[:16])
s1.stop()

p1.solo()
p4 >> lazer(dur=4,chop=12,lpf=0,amp=.7).follow(p1)
p4 >> MidiOut(P*(0,2,4),channel=1,amp=.4,dur=1.5,oct=6) + var([-4,-3,0],[4,4,8])

d9 >> play("{x v p}",dur=P[.5,.25,1,2].shuffle(8),amp=1,sample=5).sometimes("amen")
