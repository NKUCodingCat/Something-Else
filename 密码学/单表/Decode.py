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

Key = {
"C":"e"
,"I":"h"
,"S":"t"
,"N":"a"
,"B":"n"
,"J":"i"
,"M":"o"
,"P":"r"
,"A":"l"
,"G":"c"
,"Y":"y"
,"T":"v"
,"D":"d"
,"V":"w"
,"E":"g"
,"F":"f"
,"Z":"u"
,"Q":"m"
,"O":"z"
,"R":"s"
,"X":"p"
,"H":"b"
}
Code = ""


for i in STR:
	if i.isalpha():
		try: 
			Code += Key[i]
		except:
			Code += i
	else:
		Code+=i
print "Your Message is :",Code