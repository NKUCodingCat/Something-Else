#=*=coding=utf-8-*-

#L[1] 课程名称 L[6]周次 L[7]时间 L[9]位置

import xlrd,xlwt,os
import re

Dict = {}


ZL2 = re.compile(r"二主楼")
ZL= re.compile(r"主楼")
XQ = re.compile(r"校区")
TEDA = re.compile(r"泰达")
QJ = re.compile(r"七教")


path = os.path.split(os.path.realpath(__file__))[0]
data = xlrd.open_workbook(path+'\\class.xls')
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows ):
	L = table.row_values(i)
	M = L[9].encode("utf-8")

	pos = L[9]
	val = (L[1],L[6],L[7])
	
	if  not pos:
		continue
	
	if pos not in Dict:
		K = []
		K.append(val)
		Dict[pos] = K

	else:

		new = Dict[pos]
		new.append(val)
		Dict[pos] = new

ERRLIST = []	
trans = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12}
#print Dict
wbk = xlwt.Workbook()
print(len(Dict.keys()))
for  i  in Dict.keys():

	sheet = wbk.add_sheet(i)
	for j in Dict[i]:
		L = re.split("[\\/]",j[2])
		for k in range(len(L)):
			a = re.sub("[^\d\w]+","",L[k])
			if not a:
				continue
			try:
				L[k] = int(a)
			except:
				#print L[k]
				L[k] = trans[a.lower()]
		L.sort()	
		try:
			sheet.write_merge(  L[0]  , L[-1] ,int(j[1]) , int(j[1]), j[0] )
		except:
			
			ERRLIST.append(i)

wbk.save(path+"\\class\\res.xls")
ERR = list(set(ERRLIST))
print(len(ERR))
f = open(path+"\\ERR.txt","w")
for i in ERR:
	f.writelines(i.encode("utf-8")+'\n')