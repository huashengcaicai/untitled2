
class Car(object):
    def __str__(self):
        return '我是魔法方法'

    def getself(self):
        print(self)
        print('self=%s'%id(self))
bwm = Car()
# print(bwm)
bwm.getself()

# 魔法方法

