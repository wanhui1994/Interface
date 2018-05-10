# coding=utf-8
import pymysql
import requests
import json
class Test():
    # 通过sql将此地区的所有更新的用户都获取到（获取账号、手机号、QQ号、type值）
    def mysql(self,ho,pr,us,pas,base,charset="utf8"):
        db=pymysql.connect(host=ho,port=pr,user=us,password=pas,database=base,charset="utf8")
        cu=db.cursor()
        sql="""SELECT * FROM test WHERE name='万惠'"""
        cu.execute(sql)
        dis=cu.description
        all=cu.fetchall()
        # print(len(all))
        # print(all[1][0:3])
        userAccount=[]
        userAccount1=[]
        userPhone=[]
        userPhone1=[]
        userQQ=[]
        userQQ1=[]
        type=[]
        type1=[]
        for i in range(0,len(all)):
            userAccount.append(all[i][0])
            userPhone.append(all[i][1])
            userQQ.append(all[i][2])
            type.append(all[i][3])

        for j in range(len(userAccount)):
            url1="http://xf.faxuan.net/useris/service/getdetail?userAccount="
            url2="&key=Wed+May+02+2018+17%3A40%3A55+GMT%2B0800"
            url=url1+userAccount[j]+url2
            r = requests.get(url)
            a=r.json()
            p1=a.index('userAccount')
            p2=a.index('userPhone')
            p3=a.index('userQQ')
            p4=a.index('userBindingType')
            userAccount1.append(a[p1+1])
            userPhone1.append(a[p2+1])
            userQQ1.append(a[p3+1])
            type1.append(a[p4+1])
        for a1 in range(len(userAccount)):
            if userAccount[a1]==userAccount1[a1]:
                pass

            else:
                print('账号不一致：','id',a1,userAccount[a1],userAccount1[a1])

        for a2 in range(len(userPhone)):
            if userPhone[a2]==userPhone1[a2]:
                pass
            else:
                print('手机号不一致：','id',a2,userPhone[a2],userPhone1[a2])
        for a3 in range(len(userQQ)):
            if userQQ[a3]==userQQ1[a3]:
                pass
            else:
                print('QQ号不一致：','id',a3,userQQ[a3],userQQ1[a3])

        for a4 in range(len(type)):
            if type[a4]==type1[a4]:
                pass
            else:
                print('QQ号不一致：','id',a4,type[a4],type1[a4])


a=Test()
a.mysql('localhost',3306,'root','123456','testlibrary')

