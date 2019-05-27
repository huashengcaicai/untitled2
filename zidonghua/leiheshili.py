

# class Animal(object):
#     colour = 'red '  # 类是属性
#     def __init__(self):
#         self.name = '小花' # 方法里的属性,实例属性
#
#
# a = Animal.colour  # 类对象类属性可以
# # b = Animal.name    # 类对象访问实例属性 ，no不可以
# print(a)
# # print(b)
#
# # c = Animal()
# # d = Animal()
# # print(a)


class Person(object):
    country = 'china' #类属性
    def __init__(self,name):
        self.name = name

agou = Person('阿狗')
Person.country = '日本' # 类属性修改后，实例对象在访问类属性就是更新后的了
print(agou.country)
agou.country = '美国' # 实例对象也可以访问，类属性，此时通过实例对象修改类属性
print(agou.country)   # 这里指的被实例对象修改的类属性后，看看实例对象属性打印出来，看是否修改
print(Person.country) # 这里是指实例对象修改了类属性，那么类对象访问类属性，看看是否被修改，发现这里并没有修改




