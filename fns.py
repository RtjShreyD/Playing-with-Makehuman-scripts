from core import G
import humanmodifier


def measures():
	
	Measurerer = (__import__("0_modeling_a_measurement"))
	human = G.app.mhapi.modifiers.human
	ruler = Measurerer.Ruler()
	H = ruler.getMeasure
	#print 'waist [cm]: ',ruler.getMeasure(human,'measure/measure-waist-circ-decr|incr','metric')
	#data = ruler.getMeasure(human,'measure/measure-waist-circ-decr|incr','metric')
	neck_cir = H(human,'measure/measure-neck-circ-decr|incr','metric')
	neck_ht = H(human,'measure/measure-neck-height-decr|incr','metric')
	ua_cir = H(human,'measure/measure-upperarm-circ-decr|incr','metric')
	ua_len = H(human,'measure/measure-upperarm-length-decr|incr','metric')
	la_len = H(human,'measure/measure-lowerarm-length-decr|incr','metric')
	wrist = H(human,'measure/measure-wrist-circ-decr|incr','metric')
	fc_dist = H(human,'measure/measure-frontchest-dist-decr|incr','metric')
	bust = H(human,'measure/measure-bust-circ-decr|incr','metric')
	ubust = H(human,'measure/measure-underbust-circ-decr|incr','metric')
	waist = H(human,'measure/measure-waist-circ-decr|incr','metric')
	np2waist = H(human,'measure/measure-napetowaist-dist-decr|incr','metric')
	w2hip = H(human,'measure/measure-waisttohip-dist-decr|incr','metric')
	sh_dist = H(human,'measure/measure-shoulder-dist-decr|incr','metric')
	hip_cir = H(human,'measure/measure-hips-circ-decr|incr','metric')
	ul_ht = H(human,'measure/measure-upperleg-height-decr|incr','metric')
	th_cir = H(human,'measure/measure-thigh-circ-decr|incr','metric')
	ll_ht = H(human,'measure/measure-lowerleg-height-decr|incr','metric')
	calf_cir = H(human,'measure/measure-calf-circ-decr|incr','metric')
	knee = H(human,'measure/measure-knee-circ-decr|incr','metric')
	ankle = H(human,'measure/measure-ankle-circ-decr|incr','metric')
		
	data = [neck_cir, neck_ht, ua_cir, ua_len, la_len, wrist, fc_dist, bust, ubust, waist, np2waist, w2hip, sh_dist, hip_cir, ul_ht, th_cir, ll_ht, calf_cir, knee, ankle]
	return data
		
def change(old_m):
	old = old_m
	new = measures()
	mat = []
	
	for  i in range(20):
		delta = new[i] - old[i]
		if  delta == 0:
			mat.append(old[i])
		else: 
			mat.append(new[i])s
			
	return 	mat