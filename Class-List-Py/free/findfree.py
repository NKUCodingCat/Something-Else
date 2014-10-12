#=*=coding=utf-8-*-

#L[1] 课程名称 L[6]周次 L[7]时间 L[9]位置

import xlrd,xlwt,os
import re




path = os.path.split(os.path.realpath(__file__))[0]
data = xlrd.open_workbook(path+'\\res.xls')

names = data.sheet_names() 
Lis = [[[]for row in range(12)] for row in range(7)]
All = []
print Lis

for tab in names:
	L = data.sheet_by_name(tab)
	All.append (tab)
	for x in range(1,13):
		
		for y in range(1,8):
			try:
				val = L.cell(x,y).value
			except:
				val = ""
			if  val:
				Lis[y-1][x-1].append(tab)
				
