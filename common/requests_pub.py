# coding=utf-8
import requests

class Request():
    def __init__(self):
        pass

    def url(self,url):
        self.url= url

    def params(self,param):
        self.params=param

    def get_request(self):
        try:
            self.repson = requests.get(self.url,self.params,)
            return self.repson
        except TimeoutError:
            print('地址访问异常')


    def post_request(self,url,data):
        self.url=url
        self.data=data
        r = requests.post(url,data)

    def json(self):
        self.json = self.repson.json()
        return self.json


