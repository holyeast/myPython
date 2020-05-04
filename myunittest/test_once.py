# coding=utf-8
import unittest
from selenium import webdriver


'''运行以下代码，测试固件会执行两次，即留浏览器会打开关闭两次，并且两个测试函数的执行并没有确定的先后顺序。'''


class BaiduTest1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        '''验证：测试百度首页点击新闻后的跳转'''
        self.driver.find_element_by_link_text('新闻').click()

    def test_baidu_map(self):
        '''验证：测试百度首页点击地图后的跳转'''
        self.driver.find_element_by_link_text('地图').click()

        
if __name__ == '__main__':
    unittest.main(verbosity=2)
