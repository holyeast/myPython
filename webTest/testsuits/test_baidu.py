# !/usr/bin/python
# -*- coding:utf-8 -*-

import time
import json
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.page_baidu import BaiduPage
from unit.base_page import BasePage
from logs.logger import Logger
# 实现类
logger = Logger(logger="Login").getlog()



class TestBaidu(unittest.TestCase):
    """百度网站WEB测试"""

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self, url="https://www.baidu.com") # 读取浏览器类型


    def tearDown(self):
        self.driver.quit()

    # 百度搜索
    def test_search(self):
        """百度搜索"""
        homepage = BaiduPage(self.driver)
        homepage.search(u"腾讯视频")

    def test_error(self):
        """百度错误用例"""
        homepage = BaiduPage(self.driver)
        homepage.error_test(u"腾讯视频")






if __name__ == '__main__':
    unittest.main()



