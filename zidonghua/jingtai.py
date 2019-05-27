class Person(object):
    colour = '黄色'

    def __int__(self,name):
        self.name = name

    @classmethod #利用装饰器去装饰方法
    def get_colour(cls):
        print(Person.colour)
    @staticmethod # 静态方法
    def set_colour():
        Person.colour = '白色'
        print(Person.colour)


Person.set_colour() # 类对象调用
huasheng = Person()
huasheng.set_colour() # 实例对象也可以调用类方法

