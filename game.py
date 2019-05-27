'''
为了更好的理解面向对象编程，下面以'pk小游戏为例'
这打架呢，有两个人物，白鲸和花生
属性
name玩家的名字
blood玩家的血量
方法呢
tong（）捅对方一刀，对方掉10滴血
kanren（）砍对方一刀，对方掉15滴血
chiyao（）吃一颗药，补10滴血
_str_打印玩家状态
定义类，创建_init_方法

'''

class Hero(object):
    def __init__(self, name):
        self.name = name
        self.blood = 100
    def tong(self, enemy):
        enemy.blood -= 10
        print('%s 捅了%s一刀' % (self.name, enemy.name))
    def kanren(self, enemy):
        enemy.blood -= 15
        print('%s 砍了%s一刀' % (self.name, enemy.name))
    def kaiqiang(self, enemy):
        enemy.blood -=20
        print('%s 击中%s了一枪' % (self.name, enemy.name))
    def chiyao(self):
        self.blood += 10
        print('%s 吃了一颗药，加了10滴血' % (self.name))
    def __str__(self):
        return '%s 还剩余血量 %s' % (self.name,self.blood)

huasheng = Hero('花生')
baijing = Hero('白鲸')
print(huasheng)
print(baijing)
huasheng.tong(baijing)
# huasheng.tong(baijing)
# huasheng.tong(baijing)
baijing.kanren(huasheng)
huasheng.chiyao()
huasheng.tong(baijing)
huasheng.tong(baijing)
huasheng.tong(baijing)
huasheng.tong(baijing)
huasheng.tong(baijing)
huasheng.tong(baijing)
huasheng.tong(baijing)
huasheng.tong(baijing)
huasheng.tong(baijing)
huasheng.tong(baijing)
print(huasheng)
print(baijing)

