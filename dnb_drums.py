patt = "(x )( x)  "
d1 >> play(P[patt],sample=7,drive=.02)
d2 >> play("  o ",amp=.3,sample=2,lpf=0)
d3 >> play("~",sample=4,amp=.1,chop=0,spin=4,dur=PDur(3,5),echo=.5,mix=.2).stop()
d4 >> play("a",amp=PStep(6,.2,),pan=.3)
d5 >> play("S",amp=[.3,.2,.2,.2])
d6 >> play("[ { i}]{i }",sample=6,amp=[.1,.2],pshift=PRange(-1,1,10).shuffle(10))
d7 >> play("[--]",amp=sinvar([.1,.6],8),sample=P[:20],room=.1,spin=8)

d_all.every(16,"amen",2)

d_all.room=.2
d_all.mix=.2
d_all.drive=0
