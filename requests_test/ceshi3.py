# -*- coding:gbk -*-
# ��json��ת��Ϊpython��ʽ
# �Ա�һ��ԭʼ�ַ���������ģ�����ǰ��˳����ˣ���Ϊ��ת��Ϊpython���ֵ����ݵĹ����У�˳���仯��

import json_1
sJOSN = '{"userAccount":"54321","date":"2016-12-06 10:26:17","ClickTime": 1480991177,"jsonInfo":{"lon":121.5612,"lat":31.1832,"isGps":1,"netType":"WIFI","addr":"�ֶ�����������·1099Ū56��"}}'
sValue = json_1.loads(sJOSN)
print(sValue)
print(type(sJOSN))

#
# # # -*- coding:gbk -*-
# # ��python��ʽת��Ϊjson��ʽ
import json_1
sDict={'jsonInfo': {'netType': 'WIFI', 'lat': 31.1832, 'addr': '�ֶ�����������·1099Ū56��', 'isGps': 1, 'lon': 121.5612}, 'userAccount': '54321', 'ClickTime': 1480991177, 'date': '2016-12-06 10:26:17'}
sValue = json_1.dumps(sDict)
print(sValue)
print(type(sValue))
#
# # # -*- coding:gbk -*-
# # # ����json����
# #
import json_1
sJOSN = '{"userAccount":"54321","date":"2016-12-06 10:26:17","ClickTime": 1480991177,"jsonInfo":{"lon":121.5612,"lat":31.1832,"isGps":1,"netType":"WIFI","addr":"�ֶ�����������·1099Ū56��"}}'
sValue = json_1.loads(sJOSN)
for k in sValue.keys():
  if str(type(sValue[k]))!="<class 'dict'>":
    print(k+':'+ str(sValue[k]))
  else:
    print(str(k)+':')
    for k1 in sValue[k].keys():
      print(' '*3 + k1 +':'+str(sValue[k][k1]))