# names = ['Michael', 'Bob', 'Tracy']
# scores = [95, 75, 85]
'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 ,
分割，整个字典包括在花括号 {} 中 ,格式如下所示：键值是唯一的
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
元组使用小括号，列表使用方括号，字典使用大括号
访问键值
'''''
d = {'huasheng': 95, 'bailian': 75, 'qiaosong': '乔松'}
print(d['bailian'])
print(d.get('bailian')) #获取指定键值的值
print(len(d)) # 字典内置函数和方法
print(str(d))
print(type(str(d)))
# 字典内置的方法


# 修改键值


d = {'Name': 'huasheng', 'Age': 30, 'Class': 'First'}
d['Age'] = 25  # 更新
d['School'] = "beida"  # 添加
print ( d['Age'])
print (d['School'])

d = {'Name': 'huasheng', 'Age': 30, 'Class': 'First'}
del dict['Name']  # 删除键是'Name'的条目
dict.clear()  # 清空词典所有条目
del d  # 删除词典
print( dict['Name'])
print(d)
#  print( dict['class'])

# dict = {'Name': 'huasheng', 'Age': 30, 'Name': 'bailian'}
# print( dict['Name'])

# 键必须是不可以变的，所以可以用数字，字符串或元组充当，所以列表就不行
# dict = {['Name']: 'Zara', 'Age': 7}
# print (dict['Name'])


# set和dict类似，也是一组key的集合，但不存储value

s = set([1, 2,'huasheng'])
print(s)
#重复的key会被自动过滤
s = set([1,2,2,2,3,3])
print(s)
#
s.add(4)
print(s)
s.add(4)
print(s)
s.remove(2)
print(s)


