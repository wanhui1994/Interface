# coding=utf-8

import pymysql

db = pymysql.connect(host='27.221.53.50',port=13306,user='dev',password='aInfIfsfEAF',database='sale',charset="utf8")
cursor = db.cursor()
cursor.execute("SELECT id,invoice_num FROM `invoice`;")
a = cursor.fetchall()
db1 = pymysql.connect(host='27.221.53.50',port=13306,user='dev',password='aInfIfsfEAF',database='sales',charset="utf8")
cursore = db1.cursor()
cursore.execute("SELECT ID,INVOICE_CODE FROM f_invoice ORDER BY id ASC;")
a1 = cursore.fetchall()
for i in range(0,len(a1)):
    if a[i][0]==a1[i][0] and a[i][1]== a1[i][1]:
        print('pass',i)
    else:
        print('no:',i)


