# coding=utf-8

from Interface.common import mysql_pub
from Interface.config import read_config
from Interface.common import requests_pub
from Interface.common import excel
from Interface.logs import loging
class Tastcase():
    def setUp(self):
        pass
    def jiek(self):
        ip=read_config.config.get("localhost","ip")
        port=read_config.config.get("localhost","port")
        name=read_config.config.get("localhost","name")
        psw=read_config.config.get("localhost","password")
        self.mysql=mysql_pub.Mysql(ip,int(port),name,psw,"testlibrary",charset="utf8")
        self.mysql.connect()
        self.mysql.single("SELECT * FROM base_mobile_redis_2;")
        # mysql.batch("C:/Users/admin/Desktop/sql/2.sql")
        self.a=self.mysql.all()

    def requests(self):
        self.jiek()
        col=0
        col1=0
        for i in range(0,len(self.a)):
            url="http://xf.faxuan.net//useris/service/getdetail?"
            param={'userAccount':self.a[i][1]}
            requests = requests_pub.Request()
            requests.url(url)
            requests.params(param)
            req = requests.get_request()
            if req.status_code == 200:
                data = requests.json()
                phone=data.index('userPhone')
                user=data.index('userAccount')
                if data[phone+1] ==self.a[i][0] and data[user+1]==self.a[i][1] and data[data.index('userBindingType')+1]==str(1)or data[data.index('userBindingType')+1]== str(3):
                    self.log('临时表中的数据和缓存中的数据一致哦！')
                    sql1="SELECT * FROM base_mobile_redis_2 WHERE user_account="
                    sql2=str(self.a[i][1])
                    sql=sql1+sql2
                    self.mysql.single(sql)
                    self.b=self.mysql.one()
                    if data[phone+1] == self.b[0]  and data[user+1] == self.b[1] and data[data.index('userBindingType')+1] == self.b[2]:
                        self.log('base表中的数据和缓存中的数据一致哦！')
                    else:
                         self.log('%name此账号数据库和缓存中的文件不一致！'.format(self.b[1]))

                else:
                    self.log('临时表中和缓存中不一致的数据:账号：%name 手机号：%phone'.format(self.a[i][1],self.a[i][0]))
                    Excel=excel.Excelwrite()
                    Excel.new_excel('test','test')
                    Excel.write(0,col,'test')
                    self.log('将不一致的数据已经插入到新建的excel文件中了')
                    col+=1
            else:
                self.log('%name此账号缓存中没有哦！'.format(self.a[i][1]))
                print('此账号缓存中没有哦！')
                Excel=excel.Excelwrite()
                Excel.new_excel('notdata','notdata')
                Excel.write(0,col1,'test')
                col1+=1
				
    def log(self,mamessage):
        lg=loging.Log()
        lg.go()
        self.value = lg.debug(mamessage)
        return self.value











b=Tastcase()
b.requests()