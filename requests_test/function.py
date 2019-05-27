'''python中使用def定义函数,函数的定义格式为
                    def 函数名(参数列表)
                        代码块
                        return 返回值
如果没有return语句,函数也会有函数值,返回None

把逻辑封装到一个函数中
'''
def fun():
        a = 10
        _sum = 0
        for i in range(a+1):
            _sum += i
        return _sum,_sum*2,_sum-3   # 可以返回多个结果
print(fun())


def fun(num):
    if isinstance(num,(int)):
        a = num
        _sum = 0
        for i in range(a+1):
            _sum += i
        return _sum,_sum*2,_sum*3
    else:
        return "args is bad"

print("please input a number")
num =int(input())
print(fun(num))