
from core import G
import humanmodifier

Measurerer = (__import__("0_modeling_a_measurement"))

human = G.app.mhapi.modifiers.human

ruler = Measurerer.Ruler()

print 'waist [cm]: ',ruler.getMeasure(human,'measure/measure-waist-circ-decr|incr','metric')

###macro_modifiers###
human.setAgeYears(25)
human.setWeight(1.0)
human.setHeight(0.5)
human.setMuscle(1.0)
human.setGender(1.0)
human.setBodyProportions(1.0)
###macro_end###

##measure modifiers##
human.getModifier('measure/measure-neck-circ-decr|incr').setValue(0.5)
human.getModifier('measure/measure-neck-height-decr|incr').setValue(1.0)
human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(0.7)
human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(0.5)
human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(0.5)
human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(0.5)
human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(0.6)
human.getModifier('measure/measure-bust-circ-decr|incr').setValue(0.5)
human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(0.5)
human.getModifier('measure/measure-waist-circ-decr|incr').setValue(1.0)
human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(0.5)
human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(0.5)
human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(0.5)
human.getModifier('measure/measure-hips-circ-decr|incr').setValue(0.5)
human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(0.5)
human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(0.5)
human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(0.5)
human.getModifier('measure/measure-calf-circ-decr|incr').setValue(0.5)
human.getModifier('measure/measure-knee-circ-decr|incr').setValue(0.5)
human.getModifier('measure/measure-ankle-circ-decr|incr').setValue(0.5)
##measure modifiers_ends##

human.applyAllTargets()   
#print 'waist [cm], 1.0: ',ruler.getMeasure(human,'measure/measure-waist-circ-decr|incr','metric')

##print( "waist [cm], -1.0: ",ruler.getMeasure(human,'measure/measure-waist-circ-decr|incr','metric'))   print syntax when using Python3 Makehuman package.

MHScript.screenShot('front.png')

MHScript.modifyRotationZ(-90.0)

MHScript.screenShot('side.png')

MHScript.modifyRotationZ(90.0)