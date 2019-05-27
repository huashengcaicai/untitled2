import requests
import unittest
import json
import traceback
from urllib.parse import urlparse


class testadd(unittest.TestCase):
    def fasong(self):
        url =  "https://app-ym.helijia.com/api/ym/1.0/helper/editHelperArtisan？"
        params =  {'helperArtisanId': 4536, 'remark': "测试手艺人，请勿使用", 'helperCode': "mozhu",}
        r = requests.post(url, params)
        # m = r.json()
        print(r.url)
        print(r.json())
        # print(m['success'])
        # return m['success']
        # self.assertEqual(m['success'], true, "msg: 失败")


fasong = testadd()
fasong.fasong()