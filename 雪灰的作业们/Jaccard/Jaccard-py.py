import re
str1 = "I do not like green eggs and ham"
str2 = "I do not like them, So does Sam"
str1 = re.sub("[^a-zA-Z ]","",str1)
str2 = re.sub("[^a-zA-Z ]","",str2)
Lis1 = str1[:]
Lis2 = str2[:]
print Lis2
Q1 = []
Q2 = []
for i in range(len(Lis1)-1):
	Q1.append([Lis1[i],Lis1[i+1]])
for i in range(len(Lis2)-1):
	Q2.append([Lis2[i],Lis2[i+1]])
QSUM = Q1+Q2
QSN = []
QSP = []
[QSN.append(i) for i in QSUM if not i in QSN]
[QSP.append(i) for i in Q1 if i in Q2]
print float(len(QSP))/float(len(QSN))