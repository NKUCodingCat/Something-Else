K = raw_input("input the Key:")
Key = []
[Key.append(i.upper()) for i in K if ((ord(i.upper())>64 and ord(i.upper())<91)and (i.upper() not in Key))]
[Key.append(chr(i+65)) for i in range(26) if chr(i+65) not in Key]
print "Your Key is :","".join(Key)
SRC = raw_input("Input the Message:")
Code = ""
for i in SRC:
	i = i.upper()
	if i.isalpha():
		Code += Key[ord(i)-65]
	else:
		Code+=i
print "Your Code is :",Code