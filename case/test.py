# coding=utf-8
from Interface.common.excel import Excelread
from Interface.common.mysql_pub import Mysql

# 获取excel中的数据
class Gj():
    def Ex(self,num):
        e = Excelread()
        path="C:\\Users\\admin\\Desktop\\"
        e.open(path+"20180724AreaCode.xls","Sheet1")
        a=e.columns(num)
        self.m=[]
        #转换类型
        for i in range(len(a)):
            if i>=1:
              self.m.append(int(a[i]))
        # print((",".join('%s' %id for id in self.m)))

    def quc(self):
        '''列表去重'''
        q = list(set(self.m))
        return q
    def sqq(self):
        '''sql查询前半段'''
        self.count = "SELECT COUNT(*) FROM"
        self.one="SELECT * FROM"

    def sqh(self):
         '''sql查询后半段'''
         self.codeall="WHERE AREA_CODE in"
         self.codeone="WHERE AREA_CODE = "

    #获取查询地区总数的数据
    def Mq(self,database):
        myq = Mysql("27.221.53.20",59903,"dev","dev123456","gbase")
        myq.connect()
        sql = "SELECT COUNT(*) FROM "
        sql1= " WHERE AREA_CODE in("
        sql3=sql+database+sql1+(",".join('%s' %id for id in self.m))+")"
        myq.ff(sql3)
        a =myq.all()
        return list(a[0])

        # for i in range(len(self.m)):
        #     sql3=sql+database+sql1+str(self.m[i])
    def jiu(self):
        self.Ex(0)
        m = self.Mq("c_striveareas")
        self.Ex(2)
        c = self.quc() #去重获取的父级地区
        m1 =self.Mq("c_striveareas")
        if len(c) in m1:
            print(m,m1)







g=Gj()
g.jiu()

