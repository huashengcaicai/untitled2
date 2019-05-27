#


#通过下标来获取数组中的某一个元素
# print(name[0])
#采用左闭右开的原则获取连续的几个元素
# print(name[0:4])
#根据下标从左向右取元素，如果输反了只会打印出来[]
# print(name[-3:-1])
print(name[-5:-3])
#如果开始的下标或者结束的下标不输入的话，默认从头开始取或者取到最后一个元素
# print(name[:2])
# print(name[-2:])


#把列表转换为字符串
# a = ['ni','hao','hehe']
# b = ['1','2','3']
# print ( " ".join(a))
# print (type('+'.join(b)))
# print ('+'.join(b))

#把字符串转化为列表
# list = [1,2,3,'a']
# print(list)
# str = '1+2+3+4'
# sr = 'hello world'
# print(str.split('+'))#以'+'为分隔符，把字符串分为列表
# print(sr.split())
# print(type(sr.split()))

#字符串简单的用法
# name = 'my name is bailian'
# #统计字符串中包含几个m
# print(name.count("m"))
# #以name为中心打印50个字符，不够的用'-'补齐
# print(name.center(50," "))

#函数
# def func1():
#     "文档说明"
#     print("这是第一个方法")#函数的逻辑
#     return 1
#
# def func2():
#     "testing2"
#     print("这是第二个方法")
# # 调用方法
# x = func1()
# print(type(x),x)
# y = func2()
# print(type(y),y)
#
# print('from func1 return is %s' %x)
# print('from func1 return is %s' %y)