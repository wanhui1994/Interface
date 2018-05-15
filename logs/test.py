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
        self.db=None
        self.cursor=None
    #链接数据库方法
    def connect(self):
        try:
            self.db = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database,charset=self.charset)
            self.cursor = self.db.cursor()
            return True
        except Exception:
            print("错误信息：",Exception)
    def batch(self,path):
        self.connect()
        try:
            with open(path) as f:
                sql=f.read()
                print(sql)
                self.cursor.execute(sql)
                self.db.commit()
                self.cursor.close()
                self.db.close()
                return self.cursor
        except Exception:
            print("插入数据的错误信息：",Exception)
            self.db.rollback()   #数据回滚

if __name__ == '__main__':
    mysql1=Mysql("192.168.10.215",3306,"root","123456","testlibrary",charset="utf8")
    mysql1.connect()
    mysql1.batch("C:/Users/admin/Desktop/sql/1.sql")


