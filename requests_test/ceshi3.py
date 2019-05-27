# -*- coding:gbk -*-
# 将json串转换为python格式
# 对比一下原始字符串和输出的，发现前后顺序变了，因为在转化为python的字典数据的过程中，顺序会变化。

import json_1
sJOSN = '{"userAccount":"54321","date":"2016-12-06 10:26:17","ClickTime": 1480991177,"jsonInfo":{"lon":121.5612,"lat":31.1832,"isGps":1,"netType":"WIFI","addr":"浦东新区长江南路1099弄56号"}}'
sValue = json_1.loads(sJOSN)
print(sValue)
print(type(sJOSN))

#
# # # -*- coding:gbk -*-
# # 将python格式转换为json格式
import json_1
sDict={'jsonInfo': {'netType': 'WIFI', 'lat': 31.1832, 'addr': '浦东新区长江南路1099弄56号', 'isGps': 1, 'lon': 121.5612}, 'userAccount': '54321', 'ClickTime': 1480991177, 'date': '2016-12-06 10:26:17'}
sValue = json_1.dumps(sDict)
print(sValue)
print(type(sValue))
#
# # # -*- coding:gbk -*-
# # # 解析json数据
# #
import json_1
sJOSN = '{"userAccount":"54321","date":"2016-12-06 10:26:17","ClickTime": 1480991177,"jsonInfo":{"lon":121.5612,"lat":31.1832,"isGps":1,"netType":"WIFI","addr":"浦东新区长江南路1099弄56号"}}'
sValue = json_1.loads(sJOSN)
for k in sValue.keys():
  if str(type(sValue[k]))!="<class 'dict'>":
    print(k+':'+ str(sValue[k]))
  else:
    print(str(k)+':')
    for k1 in sValue[k].keys():
      print(' '*3 + k1 +':'+str(sValue[k][k1]))