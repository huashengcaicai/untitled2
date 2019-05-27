import requests  # 导入requests包

r = requests.get(url='https://search-api.helijia.com/search-api/search/queryDefaultWord?city=440300')
print(r.status_code)  # 查看请求返回的状态
print(r.content)
print(r.headers)
print(r.history)

# 结果
200

import requests  # 调用requests库

test_url = 'http://www.baidu.com'  # 访问接口的url地址
response = requests.get(test_url)  # 发起一个请求，使用get方法
result = response.text  # 读取请求返回的结果
print(result)  # 打印返回的结果



