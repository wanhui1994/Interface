# coding=utf-8
import configparser

#读取配置文件
config=configparser.ConfigParser()
config.read("IpConfig.ini")

ip=config.get("test","IP")
port=config.get("test","port")
name=config.get("test",'name')
password=config.get("test","password")
