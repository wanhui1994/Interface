# coding=utf-8
a=1
b=1
c=0
d=1
while d<10:
    c=a+b
    a=b
    b=c
    d+=1
    print(c)