# coding=utf-8
from Interface.common.excel import Excelread
from Interface.common.mysql_pub import Mysql

class Old():
    def Ex(self,num):
        '''获得整列的数据'''
        e = Excelread()
        path="C:\\Users\\admin\\Desktop\\"
        e.open(path+"AreaCode-eb.xls","Sheet1")
        a=e.columns(num)
        self.m=[]
        #转换类型
        for i in range(len(a)):
            if i>=1:
              self.m.append(int(a[i]))

    def Exa(self,num):
        '''根据code获得相对类型的数据'''
        e = Excelread()
        path="C:\\Users\\admin\\Desktop\\"
        e.open(path+"AreaCode-eb.xls","Sheet1")
        a=e.columns(6)
        codea=[idx for idx,b in enumerate(a) if b==1] #根据code1获取数据
        codeb=[idx for idx,b in enumerate(a) if b==2] #根据code2获取数据
        b=e.columns(num)
        self.m=[] #存储查询后的数据
        self.k=[]
        for i in codea:
            self.m.append(b[i])
        for i in codeb:
            self.m.append(b[i])
        for i in range(len(self.m)):
              self.k.append(int(self.m[i]))


    def quc(self):
        '''列表去重'''
        q = list(set(self.m))
        return q

    def select(self,database,name1,name,term):
        '''数据库查询语句'''
        sql="SELECT"+" "+name1+" "+"FROM+"+" "+database+" "+"WHERE"+" "+name+" "+term
        return sql

    #多条数据查询sql拼接--旧
    def sqlall(self,database,name1,name,term,fun):
        path=(",".join('%s' %id for id in fun))
        sql = self.select(database,name1,name,term)+"("+path+")"
        return sql

     #一条数据查询sql拼接--旧
    def sqlone(self,database,name1,name,term,fun):
        path=(",".join('%s' %id for id in fun))
        sql = self.select(database,name1,name,term)+path
        return sql

    #连接数据库
    def Mqall(self,database,name1,name,term,fun):
        myq = Mysql("27.221.53.20",59903,"dev","dev123456","gbase")
        myq.connect()
        sql=self.sqlall(database,name1,name,term,fun)
        myq.query(sql)
        a=myq.all()
        return a

    def Mqaone(self,database,name1,name,term,fun):
        myq = Mysql("27.221.53.20",59903,"dev","dev123456","gbase")
        myq.connect()
        sql=self.sqlone(database,name1,name,term,fun)
        myq.query(sql)
        a=myq.all()
        return list(a[0])


    def old_area(self):
        # self.Ex(0)
        self.oldarea = self.Mqall("c_striveareas","AREA_CODE","in",self.m)
        # self.Ex(2)
        # quchogn=self.quc()
        # self.oldparent = self.Mqall("c_striveareas","AREA_CODE","in",self.m)
        print(self.oldarea)

    def old_banner(self):
        # self.Ex(0)
        self.oldbanner = self.Mqall("b_banner_area","2","AREA_CODE","in","3")
        print(type(self.oldbanner))
        # self.Ex(2)
        # quchogn=self.quc()
        # self.oldparentbanner = self.Mqall("b_banner_area","AREA_CODE","in",self.m)
        # '''查询地区下有多少数据'''
        print(self.oldbanner)

#
# class Newold(Old):
#    def new_area(self):
#        self.Exa(3)
#        newarea = self.Mqall("c_striveareas","","AREA_CODE","in",self.k)
#        self.Exa(4)
#        newparent = self.Mqall("c_striveareas","AREA_CODE","in",self.k)
#        if self.oldarea[0] == newarea[0]:
#            newbanner=self.Mqall("b_banner_area","AREA_CODE","in",self.k)
#            if self.oldbanner[0] == newbanner[0]:






g=Old()
g.old_banner()
