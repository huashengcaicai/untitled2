class Person(object):

    def __init__(self):
        self.__age = 18
    @property  #通过property这个属性对age提供getattr方法
    def age(self):
        return self.__age #通过实例化的方法调用私有属性，进行访问
    @age.setter #使用装饰器，提供一个settr方法
    def age(self,age):

        if age < 0:
            print('年龄是不可以小于0的')
        else:
            self.__age = age
    # age = property(get_age,set_age)

# huasheng = Person()
# res = huasheng.get_age()
# print(res)
# huasheng.set_age(100)
# res = huasheng.get_age()
# print(res)

huasheng = Person()
huasheng.age = 89
print(huasheng.age)

