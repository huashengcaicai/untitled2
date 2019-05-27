import requests  # 导入requests包
r=requests.get('http://www.baidu.com')
print(type(r.cookies))
print(r.cookies)
for key,value in r.cookies.items():
    print (key+':'+value)

cookie={'user','51zxw'}
r=requests.get(base_url+'/cookies',cookies = cookie)
print(r.text)