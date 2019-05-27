import unittest
import HTMLTestRunner
class testadd(unittest.TestCase):
    def setUp(self):
        pass
    def test_add1(self):
        self.assertEqual(2+3+5,10)
    def test_add2(self):
        self.assertEqual(0+8+7,15)
    def test_add3(self):
        self.assertEqual(0+10+7,17)
    def test_qs1(self):
        print("test_qs1(self)")
        self.assertEqual(1,1,"msg: 1!=2")
    def test_upper(self):
        print("test_upper(self)")
        self.assertEqual('foo'.upper(), 'FOO')

    def tearDown(self):
        pass
def suite():
    suiteTest=unittest.TestSuite()
    suiteTest.addTest(testadd("test_add1"))
    suiteTest.addTest(testadd("test_add2"))
    suiteTest.addTest(testadd("test_add3"))
    suiteTest.addTest(testadd("test_qs1"))
    suiteTest.addTest(testadd("test_upper"))
    return suiteTest
if __name__=="__main__":
    file='E:\\anzhuang\\result1.html'
    fp=open(file,'wb')
    #定义测试报告的标题与描述
    ##runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'我是测试报告的标题哈哈哈',description=u'我是测试报告的描述')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        description=u'详细测试用例结果'    #不传默认为空

    )
    runner.run(suite())
    fp.close()