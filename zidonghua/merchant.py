import requests
import json
import traceback
from urllib.parse import urlparse

url = "https://merchant-api.helijia.com/app-merchant/neighborShop/decorate/index?"
params = {"artisanId": "810098cbe260446984e091007fd7aa2c",
"token":"3M7Nudvkg1bp7NJpyEcv"}

r = requests.get(url, params)
# print(r.text)
print(r.status_code)
# print(r.get[data])
print(r.json())
print(r)

c = print(r.url)

# def getJsonValue(r,key):
#
#     if key in r:
#         # print(r[dict])
#         return r[key]
#     else:
#         for i in r:
#             if type(r[i])==dict or type(r[i])==list:
#                 return getJsonValue(josnObject[i],key)
# response = requests.get('c')






# try:
#     #Post接口调用
# r = requests.get(url,params)
# # print(r.text)
# if r.status_code == 200:
#     results = json.loads(response.text)
#     if results['dictId'] == 191:
#         print("Success")
#     else:
#         print("Fail")
#         print(results['total'])
# else:
#     #         #对于http返回非200的code，输出相应的code
#     raise Exception("http error info:%s" % r.status_code)
# except:
# traceback.print_exc()


# requests 最基础的用法，未涉及传参数啊，响应的处理
# 发送GET类型的请求
# r = requests.get(base_url + '/get')
# print(r.status_code)
#
# # 发送POST类型的请求
# r = requests.post(base_url + '/post')
# print(r.status_code)
#
# # 发送put类型的请求
# r = requests.put(base_url + '/put')
# print(r.status_code)
#
# # 发送delete类型的请求
# r = requests.delete(base_url + '/delete')
# print(r.status_code)

# 参数传递
# import requests
#
# base_url = 'http://httpbin.org'
#
# param_data = { 'user': 'huasheng' , 'passwd': '123456'}

# # url 这种用的是params
# r = requests.get(base_url+'/get',params = param_data)
# print(r.url)
# print(r.status_code)

# # # 传递body参数，请求体里传递参数
# from_data = {'user':'huasheng','passwd':'123456'}
# r = requests.post(base_url + '/post',data = from_data)
# print(r.text)
#
#
# # 请求头定制
#
# from_data = {'user':'huasheng','passwd':'123456'}
# header = {'user-agent':'Mozilla./5.0'}
# r = requests.post(base_url+ '/post',data=from_data,headers=header)
#
# print(r.text)
# # 响应内容json
# print(r.json())
#
# heder= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36.36'}
# r = requests.get('https://www.zhihu.com/explore',headers =  heder)
# print(r.text)
# print(r.headers)
#
# cookie设置

# cookie={'user':'51zxw'}
# r=requests.get(base_url+'/cookies',cookies = cookie)
# print(r.text)
# #获取cookie
# r=requests.get('http://www.baidu.com')
# print(type(r.cookies))
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+':'+value)
