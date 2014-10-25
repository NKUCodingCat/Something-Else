import sys,os,math,re
fi = re.compile("[A-Za-z]+")
path = os.path.split(os.path.realpath(__file__))[0]
File = os.listdir(path+"\\Test")
List = []
for name in File:
	text = open(path+"\\Test\\"+name).read()
	Word = fi.findall(text)
	Word = {}.fromkeys(Word).keys()
	List.append(Word)
Wo = fi.findall(open(path+"\\Tar.txt").read())
Tar = {}.fromkeys(Wo).keys()
G = []
for i in List:
	[G.append(j) for j in Tar if j in i]
	print G
	G = []
