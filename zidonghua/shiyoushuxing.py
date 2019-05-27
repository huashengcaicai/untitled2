class Person(object):
    name = '花生'
    def __init__(self):
        self.age = 16

Person.name = '白莲'
xiaoming = Person()
xiaoming.age = 19
print(Person.name)
print(xiaoming.age)




class Person(object):
    __name = '小明'
    # name ='huasheng'
    def __init__(self):
        self.__age = 16


    @classmethod
    def get_name(cls):  # 私有属性如果要访问，可以通过定义一个方法
        return cls.__name
    def get_age(self):
        return self.__age


 # 这个是用来演示私有属性是不能被访问的
xiaoming = Person()
print(xiaoming.name)

xiaoming = Person()
res = xiaoming.get_name()
res1 = xiaoming.get_age()
print(res)
print(res1)

class school(Person):
    __student = '5'

    def get_school_name(self):
        print(super)  # 继承子类无法继承私有属性，这里可以去父类创建一个非私有属性，演示
        print(school.__student)  # 私有属性是不能被子类继承，实例属性也是不能继承。类外部无法直接访问私有化属性

huasheng = school()
huasheng.get_school_name()


