#=*=coding=utf-8-*-

#L[1] 课程名称 L[6]周次 L[7]时间 L[8]起止 L[9]位置

import xlrd,xlwt,os
import re,json
path = os.path.split(os.path.realpath(__file__))[0]
L = [112,137,239,409,443,436,527,522,535,513,533,502,524,603,601]
for i in L:
	D = {}
	for k in range(1,8):
		D[str(k)] = {}
		for jh in range(1,13):
			D[str(k)][str(jh)] = []
	FIL = open(path+"\\bin\\ZL"+str(i)+".json","w")
	FIL.write(json.dumps(D))
	FIL.close()