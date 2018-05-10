# coding=utf-8
import pymysql
class test():
    # 通过sql将此地区的所有更新的用户都获取到（获取账号、手机号、QQ号、type值）
    def mysql(self,ho,pr,us,pas,base):
        db=pymysql.connect(host=ho,port=pr,user=us,password=pas,database=base)
        cu=db.cursor()
        sql="SELECT * FROM test WHERE name='万惠'"
        cu.execute(sql)
        dis=cu.description
        all=cu.fetchall()
        print(all)
a=test()
a.mysql('localhost',3306,'root','123456','testlibrary')

