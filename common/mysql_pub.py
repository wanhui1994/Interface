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
        self.connect=None
        self.cursor=None
    #链接数据库方法
    def connect(self):
        try:
            self.connect = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database,charset=self.charset)
            self.cursor = self.connect.cursor()
            return True
        except Exception:
            print("错误信息：",Exception)

    def close(self):
        self.cursor.close()
        self.connect.close()

    def single (self,sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception:
            print("创建表的错误信息：",Exception)
            self.connect.rollback()

    def batch(self,path):
        try:
            self.path=path
            with open(path) as f:
                sql=f.read()
                self.cursor.execute(sql)
                self.connect.commit()
                self.cursor.close()
                self.connect.close()
        except Exception:
            print("插入数据的错误信息：",Exception)
            # self.connect.rollback()   #数据回滚

if __name__ == '__main__':
    mysql=Mysql("192.168.10.215",3306,"root","123456","testlibrary",charset="utf8")
    mysql.connect()
    mysql.batch("C:/Users/admin/Desktop/sql/1.sql")


