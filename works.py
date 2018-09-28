import xlwt
from xlwt import Workbook
import fns
from fns import measures, change
from core import G
import humanmodifier

wb  = Workbook()
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=False)

def metric_write(mat,c,sheet,wb):
	for row, value in enumerate(mat, start=1):
		sheet.write(row, c, value)
	 	
	
m1 = measures() 
metric_write(m1,2,sheet1,wb)
	
human = G.app.mhapi.modifiers.human
for  i in range(10):
	a = 0.1*(i+1)
	human.setMuscle(a)
	n1 = change(m1)
	metric_write(n1,(3+i),sheet1,wb)
	
wb.save('xlwt lookup.xls')

