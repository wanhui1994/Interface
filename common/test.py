# coding=utf-8
'''方案一：将数据库中的2个表 以excel的形式保存  然后对比这2个excel中的数据
   方案二：直接对比2个数据库中的表'''
import redis
import pymysql
import xlwt,xlrd
import requests

class Mysql():
    def mysql(self,ho,pr,us,pas,base):
       # bk=xlrd.open_workbook("C:/Users/admin/Desktop/shuju.xls")
       # sh1= bk.add_sheet("shee2")
       db=pymysql.connect(host=ho,port=pr,user=us,password=pas,database=base)
       cu=db.cursor()
       #查询需要处理的数据信息
       #sql="""SELECT d.user_account, d.user_phone FROM base_mobile_redis_2 d, base_user u WHERE u.user_account = d.user_account AND u.user_phone=d.user_phone  AND u.user_binding_type = 2"""
       sql = """select * from base_mobile_redis_2 d,base_user u  where d.user_account=u.user_account and d.user_phone!=u.user_phone"""
       cu.execute(sql)
       dis=cu.description
       all=cu.fetchall()
       for i in range(1,len(all)):
           # print(all[i][0])
           url1="http://xf.faxuan.net/useris/service/getdetail?userAccount="
           url2="&key=Wed+May+02+2018+17%3A40%3A55+GMT%2B0800"
           url3=all[i][0]
           url=url1+url3+url2
           r= requests.get(url)
           print(r.status_code)







# mysql("192.168.10.215",3306,"root","123456","testlibrary")
aa=Mysql()
aa.mysql("27.221.53.20",7153,"dev_user","faxuan.net@2015^","base")