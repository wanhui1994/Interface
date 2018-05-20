# coding=utf-8
import pymysql
import json
import logging
from Interface.common import mysql_pub
from Interface.config import read_config
from Interface.common import requests_pub
from Interface.common import excel
class Tastcase():
    def setUp(self):
        pass
    def jiek(self):
        ip=read_config.config.get("localhost","ip")
        port=read_config.config.get("localhost","port")
        name=read_config.config.get("localhost","name")
        psw=read_config.config.get("localhost","password")
        self.mysql=mysql_pub.Mysql(ip,int(port),name,psw,"testlibrary",charset="utf8")
        self.mysql.connect()
        self.mysql.single("SELECT * FROM base_mobile_redis_2 WHERE user_account='5304280130021';")
        # mysql.batch("C:/Users/admin/Desktop/sql/2.sql")
        self.a=self.mysql.all()

    def requests(self):
        self.jiek()
        col=0
        for i in range(0,len(self.a)):
            url="http://xf.faxuan.net//useris/service/getdetail?"
            param={'userAccount':self.a[i][1]}
            requests = requests_pub.Request()
            requests.url(url)
            requests.params(param)
            requests.get_request()
            data = requests.json()
            phone=data.index('userPhone')
            user=data.index('userAccount')
            if data[phone+1] ==self.a[i][0] and data[user+1]==self.a[i][1] and data[data.index('userBindingType')+1]==str(1)or data[data.index('userBindingType')+1]== str(3):
                sql1="SELECT * FROM base_mobile_redis_2 WHERE user_account="
                sql2=str(self.a[i][1])
                sql=sql1+sql2
                self.mysql.single(sql)
                self.b=self.mysql.one()
                if data[phone+1] == self.b[0] and data[user+1] == self.b[2] and data[data.index('userBindingType')+1]== self.b[2]:
                    pass
            else:
                print(self.a[i][1],self.a[i][0])
                Excel=excel.Excelwrite()
                Excel.new_excel('test','test')
                Excel.write(0,col,'test')
                col+=1











b=Tastcase()
b.requests()