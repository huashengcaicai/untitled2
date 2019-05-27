def hsone(a1,a2,a3,):
    pass
'''其中a1,a2,a3是函数的参数，函数的参数类型可分为：
普通参数（位置参数）、默认参数、可变参数（不定长参数）、关键字参数
、组合参数，总共5种。'''

# 必须参数,这里str是形参，这个形参类型取决于调用时的实参类型，实际参数多余形式参数时，会报错
def hello(age):
    print('必须参数是',age)
hello(18)

# 默认参数 ，默认参数就是定义函数时，形参给定一个值,在调用时，不赋值话，会使用默认参数，省略默认参数
def hstwo(name,age=23):
    print('我叫：',name)
    print('我今年',age)
hstwo('王二',28)
# 传参数时也可以使用，key=value的这种格式的写法，如果一个参数带了参数名，另一个没带，那么默认参数必须带参数名
# 当有默认参数时，key=value这中，不可以调换顺序
hstwo(name='huasheng',age=18)

# 可变参数（不定长参数）收集参数
def change(age, *som):
    print(age)
    for i in som:
        print(i)
    return
change('name','year','mon','address')

# 这里具体介绍一下关键字参数
def func_name(name='TOM', age=20, addr='No addr'):
    print('I am a student.')
    print("My name is {0}, and I am {1} years old, I come from {2}.".format(name, age, addr))
# 调用
# 关键字参数调用时，参数的位置是不重要的
func_name(name='WangMeili', addr='China', age=23)

dir={'name':'miss','age':'18'}
def Deaf(school,banji,**other):
     print('学校:',school,'班级:',banji,'学生信息:',other)

Deaf('清华','大二',**dir)


dir={'name':'miss','age':'18'}
def Deaf(school,banji,*other):
     print('Xuexiao:',school,'\n','Banji:',banji,'\n','Student_info:',other)
Deaf('Tsinghua','Class 2',*dir)

# 收集参数

def InstroStu(*args):
    print("Hello everyone,allow me to introduce myself:")
    print(type(args))
    for params in args:
        print(params)
# 调用
# 相当于把提供的实参，装入到args中
InstroStu('WangMeili', 18, 'Nanjing', 'single')
InstroStu('TOM')


# 关键字收集参数

def Stu(**kwargs):
    print('Hello everyone,allow me to introduce myself： ')
    print(type(kwargs))
    # 对于字典的访问
    for key, value in kwargs.items():
        print(key, '--->', value)
# 调用
Stu(name='wangmeili', age=19, add='Nanjing', lover='Gavin', work='Teacher')
Stu(name='TOM')
Stu()


# 组合参数
'''组合参数就是将之前讲过的4中参数同时引入函数作为形参，
值得注意的是，定义参数时的顺序必须为：
必须参数、关键字参数、默认参数、不定长参数。'''

'''
位置参数，默认参数，收集参数（tuple），关键字参数，收集关键字参数（dict)
位置参数必须放在最前面，收集关键字参数放在最后面
说明：默认参数、关键字参数和收集参数(tuple)的位置可以进行互换。
如果收集参数在前，则其后的所有参数除了收集关键字参数外，都会变成关键字参数，
若要修改参数的默认值，方法同关键字参数；如果收集参数在后，
那么前面所有的参数除了位置参数外，都会变成默认参数，若要修改默认值，方法同默认参数。'''