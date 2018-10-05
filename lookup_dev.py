import itertools
import sqlite3
import fns
from fns import measures, change
from core import G
import humanmodifier

MHScript.loadModel('default')
human = G.app.mhapi.modifiers.human
human.setGender(1)

conn = sqlite3.connect("lookupX.db")
print("Created/Connected \n")
c = conn.cursor() 

arr = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
muscle = arr
weight = arr
prop = arr
height = arr
neck_circ = arr
neck_height = arr
upperarm_circ = arr
upperarm_length = arr
lowerarm_length = arr
wrist_circ = arr
frontchest = arr
bust_circ = arr
underbust = arr
waist = arr
napetowaist = arr
waisttohip = arr
shoulder = arr
hips = arr
upperleg = arr
thigh = arr
lowerleg = arr
calf = arr
knee = arr
ankle = arr
n = measures()
##muscle only...#
c.execute('''CREATE TABLE `table1` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')
n = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table1` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
	
conn.commit()	
##.....musles_ends.....##

##...muscle, weight....##
c.execute('''CREATE TABLE `table2` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w in itertools.product(muscle, weight):
	human.setMuscle(m)
	human.setWeight(w)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table2`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
##ends###

###.....above + prop####
c.execute('''CREATE TABLE `table3` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p in itertools.product(muscle, weight, prop):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table3`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
##ends###

###........above + height
c.execute('''CREATE TABLE `table4` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h in itertools.product(muscle, weight, prop, height):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table4`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + neck_circ####
c.execute('''CREATE TABLE `table5` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc in itertools.product(muscle, weight, prop, height, neck_cir):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table5`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + neck_height####
c.execute('''CREATE TABLE `table6` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt in itertools.product(muscle, weight, prop, height, neck_cir, neck_height):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table6`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + upperarm_circ####
c.execute('''CREATE TABLE `table7` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table7`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + upperarm_length####
c.execute('''CREATE TABLE `table8` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table8`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table9` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table9`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table10` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table10`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table11` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)	
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table11`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table12` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)	
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table12`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table13` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)	
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table13`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table14` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table14`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table15` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table15`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table16` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table16`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table17` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table17`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table18` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table18`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table19` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips, upperleg ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table19`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table20` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg, th in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips, upperleg, thigh  ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(th)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table20`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table21` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg, th, llg in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips,upperleg, thigh, lowerleg ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(th)
	human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(llg)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table21`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table22` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg, th, llg, cf in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips,upperleg, thigh, lowerleg, calf ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(th)
	human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(llg)
	human.getModifier('measure/measure-calf-circ-decr|incr').setValue(cf)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table22`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###



###......above + lowerarm_length####
c.execute('''CREATE TABLE `table23` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg, th, llg, cf, k in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips,upperleg, thigh, lowerleg, calf, knee ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(th)
	human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(llg)
	human.getModifier('measure/measure-calf-circ-decr|incr').setValue(cf)
	human.getModifier('measure/measure-knee-circ-decr|incr').setValue(k)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table23`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###


####All parameters#####
c.execute('''CREATE TABLE `table24` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')
MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg, th, llg, cf, k, a  in itertools.product(muscle, weight, prop, height, neck_circ, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_circ, underbust, waist, napetowaist, waisttohip, shoulder, hips, upperleg, thigh, lowerleg, calf, knee, ankle) :
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)	
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(th)
	human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(llg)
	human.getModifier('measure/measure-calf-circ-decr|incr').setValue(cf)
	human.getModifier('measure/measure-knee-circ-decr|incr').setValue(k)
	human.getModifier('measure/measure-ankle-circ-decr|incr').setValue(a)
	
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table24`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
	
conn.commit()	





































import itertools
import sqlite3
import fns
from fns import measures, change
from core import G
import humanmodifier

MHScript.loadModel('default')
human = G.app.mhapi.modifiers.human
human.setGender(1)

conn = sqlite3.connect("lookupX.db")
print("Created/Connected \n")
c = conn.cursor() 

arr = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
muscle = arr
weight = arr
prop = arr
height = arr
neck_circ = arr
neck_height = arr
upperarm_circ = arr
upperarm_length = arr
lowerarm_length = arr
wrist_circ = arr
frontchest = arr
bust_circ = arr
underbust = arr
waist = arr
napetowaist = arr
waisttohip = arr
shoulder = arr
hips = arr
upperleg = arr
thigh = arr
lowerleg = arr
calf = arr
knee = arr
ankle = arr
n = measures()
##muscle only...#
c.execute('''CREATE TABLE `table1` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	n = change(n)
	nx = n
	nx.insert(0,a)
	c.execute('''INSERT INTO `table1` VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
	
conn.commit()
##.....musles_ends.....##

##...muscle, weight....##
c.execute('''CREATE TABLE `table2` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w in itertools.product(muscle, weight):
	human.setMuscle(m)
	human.setWeight(w)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table2`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
##ends###

###.....above + prop####
c.execute('''CREATE TABLE `table3` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p in itertools.product(muscle, weight, prop):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table3`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
##ends###

###........above + height
c.execute('''CREATE TABLE `table4` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h in itertools.product(muscle, weight, prop, height):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table4`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + neck_circ####
c.execute('''CREATE TABLE `table5` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc in itertools.product(muscle, weight, prop, height, neck_cir):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table5`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + neck_height####
c.execute('''CREATE TABLE `table6` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt in itertools.product(muscle, weight, prop, height, neck_cir, neck_height):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table6`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + upperarm_circ####
c.execute('''CREATE TABLE `table7` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table7`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + upperarm_length####
c.execute('''CREATE TABLE `table8` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table8`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table9` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table9`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table10` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table10`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table11` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)	
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table11`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table12` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)	
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table12`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table13` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)	
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table13`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table14` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table14`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table15` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table15`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table16` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table16`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table17` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table17`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table18` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table18`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table19` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips, upperleg ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table19`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table20` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg, th in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips, upperleg, thigh  ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(th)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table20`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table21` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg, th, llg in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips,upperleg, thigh, lowerleg ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(th)
	human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(llg)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table21`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###

###......above + lowerarm_length####
c.execute('''CREATE TABLE `table22` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg, th, llg, cf in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips,upperleg, thigh, lowerleg, calf ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(th)
	human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(llg)
	human.getModifier('measure/measure-calf-circ-decr|incr').setValue(cf)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table22`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###



###......above + lowerarm_length####
c.execute('''CREATE TABLE `table23` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg, th, llg, cf, k in itertools.product(muscle, weight, prop, height, neck_cir, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_cir, underbust, waist, napetowaist, waisttohip, shoulder, hips,upperleg, thigh, lowerleg, calf, knee ):
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(th)
	human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(llg)
	human.getModifier('measure/measure-calf-circ-decr|incr').setValue(cf)
	human.getModifier('measure/measure-knee-circ-decr|incr').setValue(k)
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table23`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ends###


####All parameters#####
c.execute('''CREATE TABLE `table24` (`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')
MHScript.loadModel('default')
n = measures()

for m, w, p, h, nc, nt, uc, ul, ll, wc, c, bc, ub, wa, nw, wh, s, hp, ulg, th, llg, cf, k, a  in itertools.product(muscle, weight, prop, height, neck_circ, neck_height, upperarm_circ, upperarm_length, lowerarm_length, wrist_circ, frontchest, bust_circ, underbust, waist, napetowaist, waisttohip, shoulder, hips, upperleg, thigh, lowerleg, calf, knee, ankle) :
	human.setMuscle(m)
	human.setWeight(w)
	human.setBodyProportions(p)
	human.setHeight(h)
	human.getModifier('measure/measure-neck-circ-decr|incr').setValue(nc)
	human.getModifier('measure/measure-neck-height-decr|incr').setValue(nt)
	human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(uc)
	human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(ul)
	human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(ll)
	human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(wc)
	human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(c)
	human.getModifier('measure/measure-bust-circ-decr|incr').setValue(bc)
	human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(ub)
	human.getModifier('measure/measure-waist-circ-decr|incr').setValue(wa)
	human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(nw)
	human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(wh)
	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(s)	
	human.getModifier('measure/measure-hips-circ-decr|incr').setValue(hp)
	human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(ulg)
	human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(th)
	human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(llg)
	human.getModifier('measure/measure-calf-circ-decr|incr').setValue(cf)
	human.getModifier('measure/measure-knee-circ-decr|incr').setValue(k)
	human.getModifier('measure/measure-ankle-circ-decr|incr').setValue(a)
	
	n = change(n)
	nx = n
	c.execute('''INSERT INTO `table24`  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
	
conn.commit()	






































