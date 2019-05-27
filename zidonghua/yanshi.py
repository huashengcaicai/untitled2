# Python 推导式列表推导式，字典推导式，集合推到式

# 列表推导式：一.30以内被3整除的数 ,二：30以内所有能被3整除的数的平方，三.找到嵌套列表中名字含有两个‘e’的所有名字
m = [i for i in range(30) if i % 3 is 0]
print(m)

def squared(x):
    return x*x
multiples = [squared(i) for i in range(30) if i % 3 is 0]
print(multiples)

names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

print([name for lst in names for name in lst if name.count('e') >= 2])  # 注意遍历顺序，这是实现的关键

# 字典推导式 一.将字典的key和value对调 二.合并大小写对应的value值，将k统一成小写

case = {'a': 10, 'b': 34}
case_frequency = {case[k]: k for k in case}
print(case_frequency)

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}
print(mcase_frequency)


# 集合推导式,计算列表中每个值的平方，自带去重功能
squared = {x**2 for x in [1, -1, 2]}
print(squared)


# [{'city': '北京北京', 'max_temp': '35', 'min_temp': '23'},
# {'city': '北京海淀', 'max_temp': '36', 'min_temp': '23'}]

# [('北京北京', '35'), ('北京海淀', '36')]

old_list = [{'city': '北京北京', 'max_temp': '35', 'min_temp': '23'}, {'city': '北京海淀', 'max_temp': '36', 'min_temp': '23'}]
new_list = []
for item in old_list:
    new_list.append((item['city'], item['max_temp']))

new_list = [(item['city'], item['max_temp']) for item in old_list]
