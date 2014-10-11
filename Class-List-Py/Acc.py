#-*- coding=utf-8 -*-

#==========================
#The MIT License
#Emal:ghostwwl@gmail.com
#  edit by Ghostwwl
#==========================

import win32com.client
class accessdb:
    def __init__(self,dbpath,dbname,dbpw='admin'):
        self.dbpath=dbpath
        self.dbname=dbname
        self.dbqw=dbpw
        self.db='Provider=Microsoft.Jet.OLEDB.4.0;Persist Security Info=False;Data Source=%s' % (dbpath+dbname+'.mdb')
    def open(self,sql):
        self.conn=win32com.client.Dispatch('ADODB.Connection')
        self.conn.Open(self.db)
        self.rs=win32com.client.Dispatch('ADODB.Recordset')
        self.sql=sql
        self.rs.Open('['+self.sql+']',self.conn,1,3)
        self.rs.MoveFirst()
    def printrcd(self):
        count=1
        record={}
        while not self.rs.EOF:
            fields=''
            recd=''     
            for i in range(self.rs.Fields.count):
                record[self.rs.Fields(i).Name]=self.rs.Fields.Item(i).Value
            #for m in flds.keys():fields=fields+m+'|'   
            fields = '|'.join(record.keys())           #感谢limodou提供的方法
            for n in record.values():recd=recd+unicode(n)+'|' #这个要unicode转换所以没用上面方法
            print "===================================="
            print fields         
            print recd
            print "第%s条记录:" % (count)   
            count+=1
            self.rs.MoveNext()
        self.conn.Close()
def main():
    print """
此程序需要win32com模块
输入dbpath示例:c:/ or c:\\t
输入dbname示例:mark
输入dbtable示例:a      
在输入dbname时不需要加.mdb直接输入数据库名           
"""
    pth=raw_input("Enter the dbpath:")
    nam=raw_input("Enter the dbname:")
    #cfield=raw_input("模糊查询的条件字段:")
    #cval=raw_input("条件字段值:")   模糊查询 一直有问题 还是以后再改
    mysql="select * from %s " %(raw_input("Enter the table name:"))
    db=accessdb(pth,nam)
    db.open(mysql)
    db.printrcd()
    
if __name__=="__main__":
    main()