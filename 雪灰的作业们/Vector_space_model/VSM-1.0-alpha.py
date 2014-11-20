import sys,os,math,re
def Sim(One,Two):
	if not len(One) == len(Two):
		raise TypeError 
	S = 0
	E1 = 0
	E2 = 0
	for i in range(len(One)):
		S += float(One[i])*float(Two[i])
		E1 += One[i]*One[i]
		E2 += Two[i]*Two[i]
	Value = S/((E1**0.5)*(E2**0.5))
	return Value
	
ToFind = ["woman","computer","wailing","atmosphere","right","distance","structure","awfully","quickly","small"]
path = os.path.split(os.path.realpath(__file__))[0]
File = os.listdir(path+"\\Test")
FlieTar = "Tar.txt"
Dict = {}
for i in File:

	v = []
	Text = open(path+ "\\Test\\"+i).read()
	for word in ToFind:
		num = re.findall(word,Text)
		v.append(len(num))
		
	Dict[i] = v[:]
tf_idf_wei = {}
for i in Dict.keys():
	v = []
	for j in range(len(Dict[i])):
		num = 0
		for  k in Dict.keys():
			if  Dict[k][j] > 0:
				num+=1
		BN = (float(len(Dict.keys())))/num
		if Dict[i][j]!=0:
			wei = float(1+math.log(Dict[i][j]))*math.log(BN)
		else:
			wei = 0
		v.append(wei)
	tf_idf_wei[i] = v[:]
Tar = []
Text = open(path+ "\\Tar.txt").read()

for word in ToFind:
	num = re.findall(word,Text)
	Tar.append(len(num))

res = []
	
for i in tf_idf_wei.keys():
	res.append([i,Sim(tf_idf_wei[i],Tar)])

res.sort(key = lambda k:k[1])

for i in res:
	print "The similarity between",i[0],"and Tar.txt is",i[1]