import unittest

class TestStringMethods(unittest.TestCase):
    def var(self):
        # 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
        a = 100
        # def func():
        #     global a    # 加了个global表示不再局部中创建这个变量了. 而是直接使用全局的a
        #     a = 28
        #     b = 30
        #     print(b)
        print(a)
        # func()
        print(a)
        # print(b)  #会报NameError的错误，因为b是局部变量

    def test_qiantao(self):
        # 嵌套函数
        def outer():
            def inner():
                a = 1
                b = 3
                c = a+b
                print('this is in inner c=',c)
            d = 9
            e = 8
            f = d*e
            inner()
            print('this is in outer f =', f)
            # inner()
        outer()
        # outer.inner()
        # print(outer().d)

    def digui(self):
        # 函数的递归
        # 定义：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
        # 递归的特性：必须有一个明确的结束条件（return），要不就变成死循环了，每次进入更深一层递归时，
        # 问题规模相比上一次递归都应有所减少，递归的执行效率不高，递归层次过多会导致栈的溢出(相当于存放数据的盒子)。列子：
        def fact(n):
            if n==1:
                return 1
            else:
                return n * fact(n - 1)
        res = fact(5)
        print(res)
        #计算过程：
        # ===> fact(5)
        # ===> 5 * fact(4)
        # ===> 5 * (4 * fact(3))
        # ===> 5 * (4 * (3 * fact(2)))
        # ===> 5 * (4 * (3 * (2 * fact(1))))
        # ===> 5 * (4 * (3 * (2 * 1)))
        # ===> 5 * (4 * (3 * 2))
        # ===> 5 * (4 * 6)
        # ===> 5 * 24
        # ===> 120

if __name__ == '__main__':
    unittest.main()



https://user.helijia.com/app-user-center/user/accountLogin?deviceType=wap&platform=wap&system=unkown&mobile=15313333526&password=123456wo&imageCode=&black_box=eyJ2IjoiamhTcVhTa0lERndrUytzMVpuSnUrZkxFdEhNdjYyUjJZczdFTzBsdmx5WkFJZExiZkhVL3pvN25tbjB0V2VZYyIsIm9zIjoid2ViIiwiaXQiOjc2NDgsInQiOiI5WnpxenJCN3RCUlJQSnhUMnAyUmwrUnZTU0ZBT2Z0M2ZoemRHeDlLQmxJaW45TXZBTmtoR2czVmJnbjhnN0hNNVB5WGowL2N6azFnZUh0d1drSkE2UT09In0%3D&device_type=wap