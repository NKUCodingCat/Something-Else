def Tran(STR,d):
	S = ""
	for i in STR:
		i = i.lower()
		if ord(i)>=97 and ord(i)<=122:
			S += chr((ord(i)-97+d)%26+97)
		else:
			S+=i
	return S
def Loop(STR):
	for i in range(25):
		print "+",i+1,"--->",Tran(STR,i+1)
Loop("abcdefg")