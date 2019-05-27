import itchat

# 登录
itchat.login()
# 发送消息
itchat.send(u'你好', 'filehelper')
http://open-customer-api.helijia.com/hlj-open-service/order/tmallSubmitOrder?
extOrderNo=12344346&productNum=1&productPrice=10&mobile=15000000100&
address=%E6%B5%8B%E8%AF%95%E5%9C%B0%E5%9D%80&cityName=%E5%8C%97%E4%BA%AC%E5%B8%82&
sellerNick=%E5%95%86%E5%AE%B6%E6%B5%8B%E8%AF%95%E5%B8%90%E5%8F%B742&skuCode=0
&serviceCode=beauty_spa&storeName=%E6%B5%8B%E8%AF%95%E5%BA%97%E9%93%BA




import requests
import unittest
import json
import traceback
from urllib.parse import urlparse


class testadd(unittest.TestCase):
    def fasong(self):
        url =  "http://open-customer-api.helijia.com/hlj-open-service/order/tmallSubmitOrder?"
        params =  {"extOrderNo": "19890023", "productNum": "1", "productPrice": "100", "mobile": "15313333526",
                  "address": "落葵地址11","skuCode":"0",
                  "cityName": "北京市", "sellerNick": "商家测试帐号42", "serviceCode": "beauty_spa","storeName":"花生店"}
        r = requests.get(url, params)
        # m = r.json()
        print(r.url)
        print(r.json())
        # print(m['success'])
        # return m['success']
        # self.assertEqual(m['success'], true, "msg: 失败")



    def quxiao(self):
        url = "http://open-customer-api.helijia.com/hlj-open-service/order/cancelOrder?"
        params = {"extOrderNo": "19890011"}
        r = requests.get(url, params)
        print(r.url)
        print(r.json())


qingqiu = testadd()
qingqiu.fasong()
# qingqiu.quxiao()



import requests
import unittest
import json
import traceback
from urllib.parse import urlparse


class testadd(unittest.TestCase):
    def fasong(self):
        url =  "http://stg-open-customer-api.helijia.com/hlj-open-service/order/tmallSubmitOrder?"
        params =  {"extOrderNo": "19890026", "productNum": "1", "productPrice": "100", "mobile": "15313333526",
                  "address": "落葵地址11","skuCode":"tmall_mei_jia",
                  "cityName": "北京市", "sellerNick": "100001", "serviceCode": "spa","storeName":"花生店"}
        r = requests.get(url, params)
        # m = r.json()
        print(r.url)
        print(r.json())
        # print(m['success'])
        # return m['success']
        # self.assertEqual(m['success'], true, "msg: 失败")



    def quxiao(self):
        url = "http://open-customer-api.helijia.com/hlj-open-service/order/cancelOrder?"
        params = {"extOrderNo": "19890011"}
        r = requests.get(url, params)
        print(r.url)
        print(r.json())


qingqiu = testadd()
qingqiu.fasong()
# qingqiu.quxiao()
