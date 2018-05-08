# coding=utf-8
import pymysql

class Mysql():
    # 初始化
    def __init__(self,host,port,user,password,database,charset="utf8"):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.database=database
        self.charset=charset
        self.db.connect=""
        self.db.cursor=""
    #链接数据库方法
    def connect(self):
        try:
            self.db.connect = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database,charset=self.charset)
            self.db.cursor = self.db.connect.cursor()
            return True
        except Exception:
            print("错误信息：",Exception)

    def close(self):
        self.db.cursor.close()
        self.db.connect.close()

    def single (self,sql):
        try:
            self.db.cursor.execute(sql)
        except Exception:
            print("创建表的错误信息：",Exception)
            self.db.connect.rollback()

    def batch(self,path):
        try:
            with open(path) as f:
                sql=f.read()
                self.db.cursor.execute(sql)
                self.db.connect.commit()
        except Exception:
            print("插入数据的错误信息：",Exception)
            self.db.connect.rollback()   #数据回滚

if __name__ == "__main__":





