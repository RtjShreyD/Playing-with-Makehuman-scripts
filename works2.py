import sqlite3
import fns
from fns import measures, change
from core import G
import humanmodifier

conn = sqlite3.connect("lookup.db")
print("Created/Connected \n")
c = conn.cursor()
m1 = measures() 
##create table for change in muscles only
c.execute('''CREATE TABLE `muscle` (`delta_fc`	INTEGER,`height`	REAL,`neck_cir`	REAL,`neck_ht`	REAL,`ua_cir`	REAL,`ua_len`	REAL,`la_len`	REAL,`wrist`	REAL,`fc_dist`	REAL,`bust`	REAL,`ubust`	REAL,`waist`	REAL,`np2waist`	REAL,`w2hip`	REAL,`sh_dist`	REAL,`hip_cir`	REAL,`ul_ht`	REAL,`th_cir`	REAL,`ll_ht`	REAL,`calf_cir`	REAL,`knee`	REAL,`ankle`	REAL)''')

human = G.app.mhapi.modifiers.human
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	n1 = change(m1)
	n1.insert(0,a)
	c.execute('''INSERT INTO `muscle` VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',n1)
	
conn.commit()
conn.close()

































