# coding=utf-8
from task.common import mysql_pub
from task.common import requests_pub
from task.config import read_config
import unittest
class Tastcase(unittest.TestCase):
    def setUp(self):
        pass
    def jiek(self):
        print("1")
        ip=read_config.ip
        port=read_config.port
        name=read_config.name
        psw=read_config.password
        mysql_pub.Mysql.__init__(ip,port,name,psw,"testlibrary",charset="utf8")

        # # self.a.batch("C:/Users/admin/Desktop/sql/1.sql")
        # # self.a.close()

b=Tastcase()
b.jiek()