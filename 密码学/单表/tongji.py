#coding=utf-8
import os,sys,re
PA = os.path.split(os.path.realpath(__file__))[0]+"\\ToSolve.txt"
try:
	F = open(PA)
except:
	print "Open Files ERR......"
	os.system("PAUSE")
	sys.exit(0)
STR = F.read()
F.close()
ARR = re.split(" ",STR)
for i in ARR:
	if len(i)<=3:
		print i
Di = {}
#print STR
for i in STR:
	if i.isalpha():
		#print i
		try:
			Di[i] += 1
		except:
			Di[i] = 1
for i in range(26):
	try:
		Di[chr(65+i)]
	except:
		Di[chr(65+i)] = 0
A = [(j,Di[j]) for j in Di.keys()]
A.sort(key = lambda x:x[1])
print A