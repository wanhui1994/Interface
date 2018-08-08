# coding=utf-8
import requests

class Request():
    def __init__(self):
        pass

    def url(self,url):
        self.url1= url

    def params(self,param):
        self.params1=param

    def get_request(self):
        try:
            self.repson = requests.get(self.url1,self.params1,timeout=10)
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
    def json_dictionary(self):
        # self.dict = self.json
        for i in range(self.json):
            self.dict={i[0]:i[1]}
        return self.dict

