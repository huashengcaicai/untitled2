import random
#random模块中包含随机选择元素的函数
values = [0,1,2,3,4]
print(type(values),values)
'''#从序列中随机抽取一个元素
r = random.choice(values)
print(type(r),r)
#从已知的序列中抽取N个不同元素的样本
m = random.sample(values,4)
print(type(m),m)
#打乱序列中元素的顺序
m = random.shuffle(values)
print(type(values),values,m)
'''
#随机生成整数
p = random.randint(0,20)
print(type(p),p)

#continue跳出本次循环，进入下一个循环
'''for i in range(0,10):
    if i < 6:
        print(i)
    else:
        continue
    print("hehe....")
'''#break跳出整个循环
for j in range(10):
    if j < 6:
        print(j)
    else:
        break
    print("hahaha...")

import xlrd
