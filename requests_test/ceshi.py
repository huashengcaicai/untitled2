#coding=utf-8
import unittest

from appium import webdriver


class Login( unittest.TestCase ):

    def test_login(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '79KR8PU8SOLV79B6'
        desired_caps['appPackage'] = 'cn.zhimawu'
        desired_caps['appActivity'] = 'cn.zhimawu.SplashActivity'
        self.driver = webdriver.Remote( 'http://localhost:4723/wd/hub', desired_caps )

        self.driver.implicitly_wait( 10000 )

        self.driver.find_element_by_id("cn.zhimawu:id/login").click()
        self.driver.find_element_by_id("cn.zhimawu:id/editPhone").send_keys("18600105776")
        self.driver.find_element_by_id("cn.zhimawu:id/edit_pwd").send_keys("111111qq")
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()

        self.driver.implicitly_wait( 10000 )

if __name__ == '__main__':
    login=Login()
    login.test_login()