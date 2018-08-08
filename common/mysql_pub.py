# coding=utf-8
import pymysql
from Interface.config import read_config
class Mysql():
    # 初始化
    def __init__(self,host,port,user,password,database,charset="utf8"):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.database=database
        self.charset=charset
        self.db=None
        self.cursor=None
    #链接数据库方法
    def connect(self):
        try:
            self.db = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database,charset=self.charset)
            self.cursor = self.db.cursor()
            return True
        except Exception:
            print("数据库连接失败",Exception)

    def close(self):
        self.cursor.close()
        self.db.close()
        print('关闭数据库！')

    def single (self,sql):
        self.connect()
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return self.cursor
        except Exception:
            print("创建表的错误信息：",Exception)
            self.db.rollback()

    def ff(self,sql):
        self.connect()
        try:
           self.cursor.execute(sql)
        except Exception:
            print("错误:",Exception)

    def batch(self,path):
        self.connect()
        try:
            with open(path) as f:
                sql=f.read()
                self.cursor.execute(sql)
                self.db.commit()
                self.cursor.close()
                self.db.close()
                return self.cursor
        except Exception:
            print("插入数据的错误信息：",Exception)
            self.db.rollback()   #数据回滚

    def all(self):
        value = self.cursor.fetchall()
        return value

    def one(self):
        value=self.cursor.fetchone()
        return value

    def description(self):
        value=self.cursor.description()
        return value









