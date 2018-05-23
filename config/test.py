# coding=utf-8

import requests
import requests.exceptions


# url="https://www.baidu.com/@@"
url="http://xf.faxuan.net//useris/service/getdetail?userAccount=2342312312312"
data=requests.get(url)
# try:
#     print('pass')
# except requests.exceptions.HTTPError:
#     print('ConnectionError -- please wait 3 seconds')

