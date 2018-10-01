import xlwt
from xlwt import Workbook
import fns
from fns import measures, change
from core import G
import humanmodifier

wb  = Workbook()
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)

def metric_write(mat,r,c,sheet,wb):
	for row, value in enumerate(mat, start=r):
		sheet.write(row, c, value) 	
	
m1 = measures() 	
human = G.app.mhapi.modifiers.human
for  i in range(11):
	a = 0.1*(i)
	human.setMuscle(a)
	n1 = change(m1)
	chf	= str(a)
	label = 'muscle-'+chf
	sheet1.write(0,(3+i),label)
	metric_write(n1,1,(3+i),sheet1,wb)
	
	for i2 in range (11):
		a2 = 0.1*(i2)
		human.setWeight(a2)
		n2 = change(n1)
		chf2 = str(a2)
		label2 = 'weight-'+chf2
		sheet1.write((22+(22*i2)),(3+i),label2)
		metric_write(n2,(23+(22*i2)),(3+i),sheet1,wb)

wb.save('xlwt lookup.xls')

