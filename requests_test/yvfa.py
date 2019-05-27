# 1、遍历key值，value值（下面写法完全等价）：
a = {'a': '1', 'b': '2', 'c': '3'}
# 方式一：
for key in a:
    print(key + ':' + a[key])
# 方式二：
# for key in a.keys():
#     print(key + ':' + a[key])
# # 方式三：
# for key, value in a.items():
#     print(key + ':' + value)
# # 方式四：
# for (key, value) in a.items():
#     print(key + ':' + value)
#
#
# # 2、遍历value值：
# for value in a.values():
#     print(value)
#
#
# # 3、遍历字典项
# for kv in a.items():
#     print(kv)
