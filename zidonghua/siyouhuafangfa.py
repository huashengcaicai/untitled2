 # 有些重要的方法，不允许外部调用，防止子类意外重写，把普通方法设置成私有化方法，在方法名前面加两个下划线

class method(object):

    def __myname(self): # 私有化方法
         print('私有化方法') # 类内部可以调用私有化方法
    def myname(self):
        self.__myname()
        print('普通方法')




a = method()
a.myname()
a.__myname()
