# coding=utf-8
import configparser

#读取配置文件

config=configparser.ConfigParser()
config.read("IpConfig.ini")

try:
    config.add_section("yunpingtai-xs")
    config.set("yunpingtai-xs","IP","150.138.148.222")
    config.set("yunpingtai-xs","port","63307")
    config.set("yunpingtai-xs","name","dev")
    config.set("yunpingtai-xs","password","dev123456")
except configparser.DuplicateSectionError:
     print("Section 'yunpingtai-xs' already exists")

config.write(open("IpConfig.ini", "w"))
ip=config.get("yunpingtai-xs","IP")
port=config.get("yunpingtai-xs","port")
name=config.get("yunpingtai-xs","name")
password=config.get("yunpingtai-xs","password")

