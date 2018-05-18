# coding=utf-8
import pymysql
from task.common import mysql_pub
from task.config import read_config
from task.common import requests_pub
class Tastcase():
    def setUp(self):
        pass
    def jiek(self):
        ip=read_config.config.get("stagweb","ip")
        port=read_config.config.get("stagweb","port")
        name=read_config.config.get("stagweb","name")
        psw=read_config.config.get("stagweb","password")
        mysql=mysql_pub.Mysql(ip,int(port),name,psw,"base",charset="utf8")
        mysql.connect()
        mysql.single("SELECT * FROM `base_mobile_redis_3` WHERE user_account='5305211050016';")
        # mysql.batch("C:/Users/admin/Desktop/sql/2.sql")
        self.a=mysql.all()

    def requests(self):
        self.jiek()
        for i in range(0,len(self.a)):
            print(self.a[i][1])
            url="http://xf.faxuan.net//useris/service/getdetail?"
            param={'userAccount':self.a[i][1]}
            requests = requests_pub.Request()
            requests.url(url)
            requests.params(param)
            requests.get_request()
            data = requests.json()
    def

            print(requests.content)



b=Tastcase()
b.jiek()
b.requests()