#coding=utf-8
import requests
from lxml import etree
import xlwt
import json,os,re,time
path = os.path.split(os.path.realpath(__file__))[0]+"/"
def Page_Deal(content):
	code = content.decode('gbk', 'ignore')
	page = etree.HTML(code)
	target = page.xpath(u'/html/body/table/tr')[2].xpath(u'td/center/table/tr')
	return [ [  re.sub("\s","",j.text) for j in i.xpath(u'td')]  for i in target[1:]]
def Xlwt_Wt(Array):
	wb=xlwt.Workbook()
	ws=wb.add_sheet('Sheet1')
	col, lin = 0,0
	for i in Array:
		for j in i:
			ws.write(lin,col,j)
			col += 1
		lin += 1
		col = 0
	wb.save(path+'class.xls')

Page="""http://jwc.nankai.edu.cn/apps/xksc/index.asp?Page=%s"""
length = re.findall("""(?<=index\.asp\?Page\=)\d+(?=>最后一页)""".decode("utf-8").encode("GBK"),requests.get(Page%1).content)[0]
db = []
for i in range(1,int(length)+1):
	while True:
		try:
			con = requests.get(Page%i).content
			time.sleep(0.1)
			break
		except:
			pass
	db.extend(Page_Deal(con))
	
	print i
Xlwt_Wt(db)