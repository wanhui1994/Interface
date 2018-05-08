# coding=utf-8
import requests

class Request():
    def __init__(self):
        pass

    def get_request(self,url,data):
        self.url=url
        self.data=data
        r = requests.get(url,data)
    def post_request(self,url,data):
        self.url=url
        self.data=data
        r = requests.post(url,data)

