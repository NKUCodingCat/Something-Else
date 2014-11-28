K = raw_input("input the Key:")
Key = []
[Key.append(i.upper()) for i in K if ((ord(i.upper())>64 and ord(i.upper())<91)and (i.upper() not in Key))]
[Key.append(chr(i+65)) for i in range(26) if chr(i+65) not in Key]
print "Your Key is :","".join(Key)
SRC = raw_input("Input the Code:")
Code = ""
for i in SRC:
	i = i.upper()
	if i.isalpha():
		for j in range(26):
			if Key[j] == i:
				Code += chr(65+j)
	else:
		Code+=i
print "Your Message is :",Code