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







conn.close()
