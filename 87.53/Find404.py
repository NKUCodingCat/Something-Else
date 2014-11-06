#-*- coding:utf8 -*-
import os
import re
import requests
from threading import Thread
from Queue import Queue
from time import sleep
re.compile("找到约 (\d+,\d+,\d+|\d+,\d+|\d+) 条结果")
headers= {
	'Accept':' application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
	'Accept-Language':' zh-CN',
	'Content-Type':' application/x-www-form-urlencoded',
	'User-Agent':' Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)',
	'Pragma':' no-cache'	
	}
List = [x/100.0 for x in range(0,10001)]

#q是任务队列
#NUM是并发线程总数
#JOBS是有多少任务
q = Queue()
NUM = 30

#具体的处理函数，负责处理单个任务
def do_somthing_using(arguments):
	s = requests.Session()
	proxies = {
        'http': 'http://127.0.0.1:8087',
        'https': 'http://127.0.0.1:8087',
	}
	r = s.get("""https://www.google.com/search?q=%E7%8E%87+"""+str(arguments)+"""+site:gov.cn""", proxies=proxies, verify=False)
	
	print r.content

#这个是工作进程，负责不断从队列取数据并处理
def working():
	while True:
		arguments = q.get()
		do_somthing_using(arguments)
		q.task_done()
#fork NUM个线程等待队列
for i in range(NUM):
	t = Thread(target=working)
	t.setDaemon(True)
	t.start()
#把JOBS排入队列
for i in List:
	q.put(i)
#等待所有JOBS完成
