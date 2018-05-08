# coding=utf-8
import pymysql
import requests
import os
import subprocess

class Mysql():
    def __init__(self):
        pass

    def mysql_(self,ho,pr,us,pas,base):
        db=pymysql.connect(host=ho,port=pr,user=us,password=pas,database=base,charset="utf8")
        cu=db.cursor()
        path="C:/Users/admin/Desktop/sql/1.sql"
        with open(path) as f:
            mysql_data=f.read()
            cu.execute(mysql_data)
        db.commit()
        cu.close()
        db.close()
    def url(self,name,user):
        domain = name
        ur="http://"+name+"/useris/service/getdetail?userAccount="+user+"&key=Wed+May+02+2018+17%3A40%3A55+GMT%2B0800"



a=Mysql()
a.mysql("192.168.10.215",3306,"root","123456","testlibrary")


