# coding=utf-8

import requests
from Interface.common.requests_pub import Request

class xf(Request):


   def clearPoint(self,userAccount,password,domainCode):
        self.userAccount1=userAccount
        self.password1=password
        self.domainCode1=domainCode
        # 获取sid接口
        self.url("http://xf.faxuan.net/useris/service/getusersidByUserAccount?")
        parmas1={'userAccount':self.userAccount1,'password':self.password1}
        self.params(parmas1)
        self.sid = self.get_request()
        print(self.sid.text)
        # 清除当日积分接口
        self.url("http://xf.faxuan.net/pss/service/pointService!clearPoint.do?")
        parmas2={'domainCode':self.domainCode1,'userAccount':self.userAccount1,'ssid':self.sid.text.strip(),'timestamp':'null'}
        self.params(parmas2)
        point = self.get_request()
        print(point.url)
        print(point.text)
   def commitStudy(self):
       # 退出学习接口
       self.url("http://xf.faxuan.net/sss/service/coursewareService!commitStudy.do?")
       parmas={'domainCode':self.domainCode1,
               'userAccount':self.userAccount1,
               'stime':1140,
               'ssid':self.sid.text.strip(),
               'timestamp':'null',
               'validate':'null',
               'type':'1'}
       self.params(parmas)
       c=self.get_request()
       print(c.url)
       print(c.text)
       print(c.status_code)

   def commitExercises(self):
       self.url("http://xf.faxuan.net/sss/service/coursewareService!commitExercises.do?")
       parmas={'domainCode':self.domainCode1,
               'userAccount':self.userAccount1,
               'paperId':'2569',
               'series':'15',
               # 'myExamAnswer':'"[{"questionId":"129335","score":"10.0","answerNo":"B"},{"questionId":"129336","score":"20.0","answerNo":"AB"},{"questionId":"129337","score":"30.0","answerNo":"1"}]"',
               # 'myExamAnswer':'[{"questionId":"129361","answerNo":"A"}]',
               'myExamAnswer':'[{"questionId":"334834","answerNo":"B"},{"questionId":"334978","answerNo":"BD"},{"questionId":"335019","answerNo":"1"}]',
               'ssid':self.sid.text.strip(),
               'timestamp':'null',
               'validate':'null',
               'type':'1'}
       self.params(parmas)
       d=self.get_request()
       print(d.url)
       print(d.text)
       print(d.status_code)

   def getcodes(self,domainCode1):
       self.url("http://xf.faxuan.net/useris/service/getcodes?")
       parmas={'domainCode':domainCode1}
       self.params(parmas)
       codes = self.get_request()
       print(codes.text)

a=xf()
a.clearPoint('2016033120005','123abc','100011001000000')
a.commitStudy()
a.commitExercises()
a.getcodes('100011001000000')
