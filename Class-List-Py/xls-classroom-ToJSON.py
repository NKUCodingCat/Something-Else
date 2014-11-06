#=*=coding=utf-8-*-

#L[1] 课程名称 L[6]周次 L[7]时间 L[8]起止 L[9]位置

import xlrd,xlwt,os
import re,json

Dict = {}

style = xlwt.easyxf(u"align: wrap on, vert centre, horiz centre;")
style.font.Size = 100

ZL2 = re.compile(r"二主楼")
ZL= re.compile(r"主楼")
XQ = re.compile(r"校区")
TEDA = re.compile(r"泰达")
QJ = re.compile(r"七教")
FindNUM = re.compile("\d+")


path = os.path.split(os.path.realpath(__file__))[0]
data = xlrd.open_workbook(path+'\\class.xlsx')
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows ):
	L = table.row_values(i)
	M = L[9].encode("utf-8")

	if ZL2.findall(M):
		pos = "2ZL"+(M[-4:])
		
	elif ZL.findall(M):
		K = FindNUM.findall(M)
		if  K:
			pos = "ZL"+(K[0])
		else:
			pos = ""
		
	else:
		pos = ""
	'''	
	elif XQ.findall(M):
		pos = "XQ"+(M[-3:])
		
	elif TEDA.findall(M):
		pos = "TEDA"+(M[-4:])
	'''	
	

	#pos = L[9]
	val = [L[1],L[6],L[7],L[8]]
	
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

	#sheet = wbk.add_sheet(i.decode("utf-8","ignore"))
	
	#for T in range(1,8):
		#sheet.col(T).width = 6250
	
	Lis = []
	
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
		j [2] = L
		j [1] = int(j[1])
		
		for cla in j[2]:
			Lis.append([j[0],j[1],cla,j[3]])
	
	count = len(Lis)
	for a in range( len(Lis)):
		for b in range( len(Lis)-1 , a , -1):
			src = Lis[a]
			res = Lis[b]
			if  src[1] == res[1] and src[2]==res[2]:
			
				if src[0][-1] ==  "]":
					src[0] = src[0]+res[0]+"["+res[3]+"]"
				else:
					src[0] = src[0]+"["+src[3]+"]"+res[0]+"["+res[3]+"]"
				Lis[a] = src
				del(Lis[b])
		
			
			
	Dict[i] = Lis[:]
	D = {}
	#print Dict[i]
	for k in range(1,8):
		D[str(k)] = {}
		for jh in range(1,13):
			D[str(k)][str(jh)] = []
	for jc in Dict[i]:
		D[str(jc[1])][str(jc[2])].append(jc[0])
	FIL = open(path+"\\bin\\"+str(i)+".json","w")
	FIL.write(json.dumps(D))
	FIL.close()
	#raw_input()
	
	#for m in Dict[i]:
		
		#sheet.write(  m[2] , m[1],m[0])

		#ERRLIST.append(i)
	
	
	
	#print Lis
	#raw_input("PAUSE")


		
		
		
		
		
		
		
		
		
'''
		for m in L:
			try:
				sheet.write(  m,j[1] , j[0] )
			except:
				ERRLIST.append(i)
		print j
		raw_input("PAUSE")
'''
	
#wbk.save(path+"\\free\\res.xls")
#ERR = list(set(ERRLIST))
#print(len(ERR))
#f = open(path+"\\free\\ERR2.txt","w")
#for i in ERR:
	#f.writelines(i+'\n')