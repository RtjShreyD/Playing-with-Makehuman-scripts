import sqlite3
import fns
from fns import measures, change
from core import G
import humanmodifier

conn = sqlite3.connect("lookup.db")
print("Created/Connected \n")
c = conn.cursor() 

MHScript.loadModel('default')
human = G.app.mhapi.modifiers.human
n1 = measures()

def iters(human):	
	
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										for i11 in range(11):
											a11 = 0.1*(i11)
											human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(a11)
											for i12 in range (11):
												a12 = 0.1*(i12)
												human.getModifier('measure/measure-bust-circ-decr|incr').setValue(a12)
												for i13 in range(11):
													a13 = 0.1*(i13)
													human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(a13)
													for i14 in range(11):
														a14 = 0.1*(i14)
														human.getModifier('measure/measure-waist-circ-decr|incr').setValue(a14)
														for i15 in range(11):
															a15 = 0.1*(i15)
															human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(a15)
															for i16 in range(11):
																a16 = 0.1*(i16)
																human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(a16)
																for i17 in range(11):
																	a17 = 0.1*(i17)
																	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(a17)
																	for i18 in range(11):
																		a18 = 0.1*(i18)
																		human.getModifier('measure/measure-hips-circ-decr|incr').setValue(a18)
																		


##create table for change in muscles only....
c.execute('''CREATE TABLE `muscle` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	n1 = change(n1)
	nx = n1
	nx.insert(0,a)
	c.execute('''INSERT INTO `muscle` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
	
conn.commit()
##.....musles_ends.....##

##create table for change in muscle, weight...
c.execute('''CREATE TABLE `mus+wt` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n2 = measures()

for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		n2 = change(n2)
		nx = n2
		nx.insert(0,a2)
		c.execute('''INSERT INTO `mus+wt` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
##.....muscles, weight_ends....##
	
##create table for change in muscle, weight, height...
c.execute('''CREATE TABLE `mus+wt+ht` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n3 = measures()

for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			n3 = change(n3)
			nx = n3
			nx.insert(0,a3)
			c.execute('''INSERT INTO `mus+wt+ht` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
##......muscle, weight, height_ends.....##

##create table for change in mus, wt, height, body proportions
c.execute('''CREATE TABLE `mus+wt+ht+prop` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n4 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				n4 = change(n4)
				nx = n4
				nx.insert(0,a4)
				c.execute('''INSERT INTO `mus+wt+ht+prop` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
##......muscle, weight, height, proportions_ends.....##
####....IN TABLES MUS,WT,HT,PROP ARE COMBINED AND FURTHER USED AS ALL_MACRO + ... FOR EASY DECODING AND SHORT NAMING.

##Create table.....ALL_MACRO + neck circ.....
c.execute('''CREATE TABLE `all_macro+neck_cir` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n5 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					n5 = change(n5)
					nx = n5
					nx.insert(0,a5)
					c.execute('''INSERT INTO `all_macro+neck_cir` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###.....ALL_MACRO + neck circ_ends.......###

###Create table.....AL_MACRO +NECK CIRC+NECK HEIGHT.......
c.execute('''CREATE TABLE `all_macro+neck_cir+neck_ht` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n6 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						n6 = change(n6)
						nx = n6
						nx.insert(0,a6)
						c.execute('''INSERT INTO `all_macro+neck_cir+neck_ht` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
##.....AL_MACRO +NECK CIRC+NECK HEIGHT_ends....##
###The above all is coded as allm_nck##
###Create table for allm_neck + upperarm circ .....
c.execute('''CREATE TABLE `allm_nck+ua_cir` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n7 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							n7 = change(n7)
							nx = n7
							nx.insert(0,a7)
							c.execute('''INSERT INTO `allm_nck+ua_cir` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###Create table for allm_neck + upperarm circ + upperarm length.....
c.execute('''CREATE TABLE `allm_nck+ua_c+ua_len` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n8 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								n8 = change(n8)
								nx = n8
								nx.insert(0,a8)
								c.execute('''INSERT INTO `allm_nck+ua_c+ua_len` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)	

conn.commit()
###allm_neck + upperarm circ + upperarm length_ends.........####
###Create table all above + lowerarm length.......
c.execute('''CREATE TABLE `amnk_ua + la_len` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n9 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									n9 = change(n9)
									nx = n9
									nx.insert(0,a9)
									c.execute('''INSERT INTO `amnk_ua + la_len` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###all above + lowerarm length_ends.......##
###Create table for all+wrist......
c.execute('''CREATE TABLE `all+wrist` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')
									
MHScript.loadModel('default')
n10 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										n10 = change(n10)
										nx = n10
										nx.insert(0,a10)
										c.execute('''INSERT INTO `all+wrist` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###all+wrist......ends##
####Frontchest distance....
c.execute('''CREATE TABLE `chest_dist` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n11 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										for i11 in range(11):
											a11 = 0.1*(i11)
											human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(a11)
											n11 = change(n11)
											nx = n11
											nx.insert(0,a11)
											c.execute('''INSERT INTO `chest_dist` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###Chest distance...ends###
####bust(aka chest) circumference......
c.execute('''CREATE TABLE `bust_cir` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n12 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										for i11 in range(11):
											a11 = 0.1*(i11)
											human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(a11)
											for i12 in range (11):
												a12 = 0.1*(i12)
												human.getModifier('measure/measure-bust-circ-decr|incr').setValue(a12)
												n12 = change(n12)
												nx = n12
												nx.insert(0,a12)
												c.execute('''INSERT INTO `bust_cir` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###bust_cir ends..##
###under bust_circ .......
c.execute('''CREATE TABLE `ubust_cir` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n13 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										for i11 in range(11):
											a11 = 0.1*(i11)
											human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(a11)
											for i12 in range (11):
												a12 = 0.1*(i12)
												human.getModifier('measure/measure-bust-circ-decr|incr').setValue(a12)
												for i13 in range(11):
													a13 = 0.1*(i13)
													human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(a13)
													n13 = change(n13)
													nx = n13
													nx.insert(0,a13)
													c.execute('''INSERT INTO `ubust_cir` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###ubust circ ends....##
###Waist circumference.......

c.execute('''CREATE TABLE `waist_cir` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n14 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										for i11 in range(11):
											a11 = 0.1*(i11)
											human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(a11)
											for i12 in range (11):
												a12 = 0.1*(i12)
												human.getModifier('measure/measure-bust-circ-decr|incr').setValue(a12)
												for i13 in range(11):
													a13 = 0.1*(i13)
													human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(a13)
													for i14 in range(11):
														a14 = 0.1*(i14)
														human.getModifier('measure/measure-waist-circ-decr|incr').setValue(a14)
														n14 = change(n14)
														nx = n14
														nx.insert(0,a14)
														c.execute('''INSERT INTO `waist_cir` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###Waist_cir ends....
####Nape to waist distance.......
c.execute('''CREATE TABLE `np2waist` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n15 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										for i11 in range(11):
											a11 = 0.1*(i11)
											human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(a11)
											for i12 in range (11):
												a12 = 0.1*(i12)
												human.getModifier('measure/measure-bust-circ-decr|incr').setValue(a12)
												for i13 in range(11):
													a13 = 0.1*(i13)
													human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(a13)
													for i14 in range(11):
														a14 = 0.1*(i14)
														human.getModifier('measure/measure-waist-circ-decr|incr').setValue(a14)
														for i15 in range(11):
															a15 = 0.1*(i15)
															human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(a15)
															n15 = change(n15)
															nx = n15
															nx.insert(0,a15)
															c.execute('''INSERT INTO `np2waist` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###np2waist ends......###
###waist to hip distance.....
c.execute('''CREATE TABLE `waist2hip` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n16 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										for i11 in range(11):
											a11 = 0.1*(i11)
											human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(a11)
											for i12 in range (11):
												a12 = 0.1*(i12)
												human.getModifier('measure/measure-bust-circ-decr|incr').setValue(a12)
												for i13 in range(11):
													a13 = 0.1*(i13)
													human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(a13)
													for i14 in range(11):
														a14 = 0.1*(i14)
														human.getModifier('measure/measure-waist-circ-decr|incr').setValue(a14)
														for i15 in range(11):
															a15 = 0.1*(i15)
															human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(a15)
															for i16 in range(11):
																a16 = 0.1*(i16)
																human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(a16)
																n16 = change(n16)
																nx = n16
																nx.insert(0,a16)
																c.execute('''INSERT INTO `waist2hip` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###waist2hip...ends....###
###shoulder distance.....
c.execute('''CREATE TABLE `shoulder` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n17 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										for i11 in range(11):
											a11 = 0.1*(i11)
											human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(a11)
											for i12 in range (11):
												a12 = 0.1*(i12)
												human.getModifier('measure/measure-bust-circ-decr|incr').setValue(a12)
												for i13 in range(11):
													a13 = 0.1*(i13)
													human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(a13)
													for i14 in range(11):
														a14 = 0.1*(i14)
														human.getModifier('measure/measure-waist-circ-decr|incr').setValue(a14)
														for i15 in range(11):
															a15 = 0.1*(i15)
															human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(a15)
															for i16 in range(11):
																a16 = 0.1*(i16)
																human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(a16)
																for i17 in range(11):
																	a17 = 0.1*(i17)
																	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(a17)
																	n17 = change(n17)
																	nx = n17
																	nx.insert(0,a17)
																	c.execute('''INSERT INTO `shoulder` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)

conn.commit()
###shoulder ends....###
### Hips circumference.....
c.execute('''CREATE TABLE `hips` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n18 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										for i11 in range(11):
											a11 = 0.1*(i11)
											human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(a11)
											for i12 in range (11):
												a12 = 0.1*(i12)
												human.getModifier('measure/measure-bust-circ-decr|incr').setValue(a12)
												for i13 in range(11):
													a13 = 0.1*(i13)
													human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(a13)
													for i14 in range(11):
														a14 = 0.1*(i14)
														human.getModifier('measure/measure-waist-circ-decr|incr').setValue(a14)
														for i15 in range(11):
															a15 = 0.1*(i15)
															human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(a15)
															for i16 in range(11):
																a16 = 0.1*(i16)
																human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(a16)
																for i17 in range(11):
																	a17 = 0.1*(i17)
																	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(a17)
																	for i18 in range(11):
																		a18 = 0.1*(i18)
																		human.getModifier('measure/measure-hips-circ-decr|incr').setValue(a18)
																		n18 = change(n18)
																		nx = n18
																		nx.insert(0,a18)
																		c.execute('''INSERT INTO `hips` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
conn.commit()
###Hips ends....###
###Upper leg height.....
c.execute('''CREATE TABLE `ul_ht` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n19 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		for i3 in range(11):
			a3 = 0.1*(i3)
			human.setHeight(a3)
			for i4 in range(11):
				a4 = 0.1*(i4)
				human.setBodyProportions(a4)
				for i5 in range(11):
					a5 = 0.1*(i5)
					human.getModifier('measure/measure-neck-circ-decr|incr').setValue(a5)
					for i6 in range(11):
						a6 = 0.1*(i6)
						human.getModifier('measure/measure-neck-height-decr|incr').setValue(a6)
						for i7 in range(11):
							a7 = 0.1*(i7)
							human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(a7)
							for i8 in range(11):
								a8 = 0.1*(i8)
								human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(a8)
								for i9 in range(11):
									a9 = 0.1*(i9)
									human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(a9)
									for i10 in range(11):
										a10 = 0.1*(i10)
										human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(a10)
										for i11 in range(11):
											a11 = 0.1*(i11)
											human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(a11)
											for i12 in range (11):
												a12 = 0.1*(i12)
												human.getModifier('measure/measure-bust-circ-decr|incr').setValue(a12)
												for i13 in range(11):
													a13 = 0.1*(i13)
													human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(a13)
													for i14 in range(11):
														a14 = 0.1*(i14)
														human.getModifier('measure/measure-waist-circ-decr|incr').setValue(a14)
														for i15 in range(11):
															a15 = 0.1*(i15)
															human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(a15)
															for i16 in range(11):
																a16 = 0.1*(i16)
																human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(a16)
																for i17 in range(11):
																	a17 = 0.1*(i17)
																	human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(a17)
																	for i18 in range(11):
																		a18 = 0.1*(i18)
																		human.getModifier('measure/measure-hips-circ-decr|incr').setValue(a18)
																		for i19 in range(11):
																			a19 = 0.1*(i19)
																			human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(a19)
																			n19 = change(n19)
																			nx = n19
																			nx.insert(0,a19)
																			c.execute('''INSERT INTO `ul_ht` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
conn.commit()
###upper leg height ends....##
#### thigh cicumference.....
c.execute('''CREATE TABLE `thigh` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')																	
																 											
MHScript.loadModel('default')
n20 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	iters(human)
	for i19 in range(11):
		a19 = 0.1*(i19)
		human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(a19)															
		for i20 in range (11):
			a20 = 0.1*(i20)
			human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(a20)
			n20 = change(20)
			nx = n20
			nx.insert(0,a20)
			c.execute('''INSERT INTO `thigh` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
conn.commit()
##thigh ends.....###
###lower leg height.....
c.execute('''CREATE TABLE `ll_ht` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')
MHScript.loadModel('default')
n21 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	iters(human)
	for i19 in range(11):
		a19 = 0.1*(i19)
		human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(a19)															
		for i20 in range (11):
			a20 = 0.1*(i20)
			human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(a20)
			for i21 in range(11):
				a21 = 0.1*(i21)
				human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(a21)
				n21 = change(n21)
				nx = n21
				nx.insert(0,a21)
				c.execute('''INSERT INTO `ll_ht` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
conn.commit()
###lowerleg height...ends...###																					
####Calf circumference........
c.execute('''CREATE TABLE `calf_cir` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

MHScript.loadModel('default')
n22 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	iters(human)
	for i19 in range(11):
		a19 = 0.1*(i19)
		human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(a19)															
		for i20 in range (11):
			a20 = 0.1*(i20)
			human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(a20)
			for i21 in range(11):
				a21 = 0.1*(i21)
				human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(a21)
				for i22 in range(11):
					a22  = 0.1*(i22)
					human.getModifier('measure/measure-calf-circ-decr|incr').setValue(a22)
					n22 = change(n22)
					nx = n22
					nx.insert(0,a22)
					c.execute('''INSERT INTO `calf_cir` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
conn.commit()
####calf circ ends.....###

###Knee .......
c.execute('''CREATE TABLE `Knee` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')																						
																					
MHScript.loadModel('default')
n23 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	iters(human)
	for i19 in range(11):
		a19 = 0.1*(i19)
		human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(a19)															
		for i20 in range (11):
			a20 = 0.1*(i20)
			human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(a20)
			for i21 in range(11):
				a21 = 0.1*(i21)
				human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(a21)
				for i22 in range(11):
					a22  = 0.1*(i22)
					human.getModifier('measure/measure-calf-circ-decr|incr').setValue(a22)
					for i23 in range(11):
						a23 = 0.1*(i23)
						human.getModifier('measure/measure-knee-circ-decr|incr').setValue(a23)
						n23 = change(n23)
						nx = n23
						nx.insert(0,a23)
						c.execute('''INSERT INTO `Knee` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
conn.commit()
###knee_ends.....	####

###Ankle .......
c.execute('''CREATE TABLE `Ankle` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')																						
																					
MHScript.loadModel('default')
n24 = measures()
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	iters(human)
	for i19 in range(11):
		a19 = 0.1*(i19)
		human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(a19)															
		for i20 in range (11):
			a20 = 0.1*(i20)
			human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(a20)
			for i21 in range(11):
				a21 = 0.1*(i21)
				human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(a21)
				for i22 in range(11):
					a22  = 0.1*(i22)
					human.getModifier('measure/measure-calf-circ-decr|incr').setValue(a22)
					for i23 in range(11):
						a23 = 0.1*(i23)
						human.getModifier('measure/measure-knee-circ-decr|incr').setValue(a23)
						for i24 in range(24):
							a24 = 0.1*(i24)
							human.getModifier('measure/measure-ankle-circ-decr|incr').setValue(a24)
							n24 = change(n24)
							nx = n24
							nx.insert(0,a24)
							c.execute('''INSERT INTO `Ankle` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',nx)
conn.commit()
###Ankle...ends...###

print("Successfully ended \n")																							
conn.close()
