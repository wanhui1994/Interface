# coding=utf-8
from Interface.common.excel import Excelread
from Interface.common.mysql_pub import Mysql

# 获取excel中的数据
class Gj():
    def Ex(self,num):
        e = Excelread()
        path="C:\\Users\\admin\\Desktop\\"
        e.open(path+"AreaCode-eb.xls","Sheet1")
        a=e.columns(6)
        codea=[idx for idx,b in enumerate(a) if b==1] #根据code获取数据
        codeb=[idx for idx,b in enumerate(a) if b==2] #根据code获取数据
        b=e.columns(num)
        self.m=[] #存储查询后的数据
        self.k=[]
        for i in codea:
            self.m.append(b[i])
        for i in codeb:
            self.m.append(b[i])
        for i in range(len(self.m)):
              self.k.append(int(self.m[i]))
        print(self.k)

    def Ex1(self,num):
        e = Excelread()
        path="C:\\Users\\admin\\Desktop\\"
        e.open(path+"AreaCode-eb.xls","Sheet1")
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
    def Mq1(self,database):
        myq = Mysql("27.221.53.20",59903,"dev","dev123456","gbase")
        myq.connect()
        sql = "SELECT COUNT(*) FROM "
        sql1= " WHERE CODE in("
        sql3=sql+database+sql1+(",".join('%s' %id for id in self.m))+")"
        myq.ff(sql3)
        a =myq.all()
        return list(a[0])

        # for i in range(len(self.m)):
        #     sql3=sql+database+sql1+str(self.m[i])
    def jiu(self):
        self.Ex1(0)
        m = self.Mq("c_striveareas")
        self.Ex1(2)
        c = self.quc() #去重获取的父级地区
        self.oldarea =self.Mq("c_striveareas")
        print("旧地区添加的area，子地区\父地区：%s"%m,self.oldarea)

    def jiubanner(self):
        self.Ex1(0)
        m = self.Mq("b_banner_area")
        self.Ex1(2)
        c = self.quc() #去重获取的父级地区
        self.oldbanner =self.Mq("b_banner_area")
        print("旧地区添加的banner，子地区\父地区：%s"%m,self.oldbanner)

    def jiunew(self):
        self.Ex1(0)
        m = self.Mq("c_news_area")
        self.Ex1(2)
        c = self.quc() #去重获取的父级地区
        self.oldnew =self.Mq("c_news_area")
        print("旧地区添加的资讯，子地区\父地区：%s"%m,self.oldnew)

    def jiutheme(self):
        self.Ex1(0)
        m = self.Mq1("c_theme")
        self.Ex1(2)
        c = self.quc() #去重获取的父级地区
        self.oldtheme =self.Mq1("c_theme")
        print("旧地区添加的主题，子地区\父地区：%s"%m,self.oldtheme)

    def jiuadmin(self):
        self.Ex1(0)
        m = self.Mq("b_admin_area")
        self.Ex1(2)
        c = self.quc() #去重获取的父级地区
        self.oldadmin =self.Mq("b_admin_area")
        print("旧地区添加的admin，子地区\父地区：%s"%m,self.oldadmin)

    def sou(self):
        self.jiu()
        self.jiubanner()
        self.jiunew()
        self.jiuadmin()
        self.jiutheme()



g=Gj()
g.sou()

