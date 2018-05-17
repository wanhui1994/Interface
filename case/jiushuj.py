# coding=utf-8
import pymysql
from task.common import mysql_pub
from task.config import read_config
from task.common import requests_pub
class Tastcase():
    def setUp(self):
        pass
    def jiek(self):
        ip=read_config.ip
        port=read_config.port
        name=read_config.name
        psw=read_config.password
        mysql=mysql_pub.Mysql(ip,int(port),name,psw,"testlibrary",charset="utf8")
        mysql.connect()
        mysql.single("SELECT * FROM `course` WHERE FIRST_NAME='WH123456';")
        mysql.batch("C:/Users/admin/Desktop/sql/2.sql")
        a=mysql.all()
        print(a)

    def

b=Tastcase()
b.jiek()