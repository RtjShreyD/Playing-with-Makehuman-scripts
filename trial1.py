from core import G
import getpath
import humanmodifier

Measurerer = (__import__("0_modeling_a_measurement"))

human = G.app.mhapi.modifiers.human

ruler = Measurerer.Ruler()

#print 'waist [cm]: ',ruler.getMeasure(human,'measure/measure-waist-circ-decr|incr','metric')

human.getModifier('measure/measure-waist-circ-decr|incr').setValue(1.0)
human.applyAllTargets()   
#print 'waist [cm], 1.0: ',ruler.getMeasure(human,'measure/measure-waist-circ-decr|incr','metric')