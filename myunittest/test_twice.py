# coding=utf-8
import unittest
from selenium import webdriver

'''运行以下代码，测试固件只会执行一次，即留浏览器只会打开关闭一次，并且两个测试函数的执行按照suite中添加的顺序执行。'''


class BaiduTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://www.baidu.com')
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_news(self):
        """验证：测试百度首页点击新闻后的跳转"""
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.get('https://www.baidu.com')

    def test_baidu_map(self):
        """验证：测试百度首页点击地图后的跳转"""
        self.driver.find_element_by_link_text('地图').click()
        self.driver.get('https://www.baidu.com')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BaiduTest('test_baidu_news'))
    suite.addTest(BaiduTest('test_baidu_map'))
    unittest.TextTestRunner().run(suite)
