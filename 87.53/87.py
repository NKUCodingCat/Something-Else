#-*-coding=utf-8-*-
import os
import re
import requests
from threading import Thread
from Queue import Queue
from time import sleep
C = re.compile("百度为您找到相关结果约(\d+(,\d+)*)个")
D = re.compile("\,")
headers= {
	'Accept':' application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
	'Accept-Language':' zh-CN',
	'Content-Type':' application/x-www-form-urlencoded',
	'User-Agent':' Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)',
	'Pragma':' no-cache'	
	}
List = [x/100.0 for x in range(3443,10001)]
ERR = []
Data = open("Da.txt","a")
for arguments in List:
	#s = requests.Session()
	try:
		r = requests.get("http://www.baidu.com/s?wd=%E7%8E%87"+str(arguments)+"site%3Agov.cn",headers = headers)
		"""
	proxies = {
		'http': 'http://127.0.0.1:8087',
		'https': 'http://127.0.0.1:8087',
	}
	"""
	except:
		ERR.append(arguments)
	#r = s.get("""https://www.google.ca/search?q=%E7%8E%87+"""+str(arguments)+"""+site:gov.cn""", proxies=proxies, verify=False,headers = headers)
	try:
		a = C.findall(r.content)[0]
	except:
		print r.content
		#raw_input()
	print a
	Data.writelines(str(arguments)+"\t"+D.sub("",a[0])+"\n")
	print arguments
	
	sleep(2)
print ERR