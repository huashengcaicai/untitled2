# from function import fun
# print(fun(16))

# print(fun("dd"))

# 钩子函数(空函数)
# def donothing():
#     pass

def huasheng(*args):
    if  isinstance(args,tuple):
        _sum = 0
        print(args)
        print(type(args))
        for arg in args:
            if isinstance(arg ,int):
                _sum += arg
            else:
                print('arg:{} is not int type'.format(arg))
        return _sum
    else:
        print('error:',type(args))

print(huasheng(*(2,10,3,6,'hu')))
