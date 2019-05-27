import requests
import unittest
import json
import traceback
from urllib.parse import urlparse


class testadd(unittest.TestCase):
    def fasong(self):
        url = "http://open-customer-api.helijia.com/hlj-open-service/order/tmallSubmitOrder?"
        params = {"extOrderNo": "198900559", "productNum": "1", "productPrice": "100", "mobile": "15313333526",
                  "address": "核销码", "skuCode": "0",
                  "cityName": "北京市", "sellerNick": "商家测试帐号42", "serviceCode": "beauty_spa", "storeName": "花生店"}
        r = requests.get(url, params)
        # m = r.json()
        print(r.url)
        print(r.json())
        # print(m['success'])
        # return m['success']
        # self.assertEqual(m['success'], true, "msg: 失败")



    def quxiao(self):
        url = "http://open-customer-api.helijia.com/hlj-open-service/order/cancelOrder?"
        params = {"extOrderNo": "19890053"}
        r = requests.get(url, params)
        print(r.url)
        print(r.json())


qingqiu = testadd()
qingqiu.fasong()
# qingqiu.quxiao()
