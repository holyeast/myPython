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
    global result
    result = True

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls, url="https://www.baidu.com") # 读取浏览器类型
        cls.homepage = BaiduPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        # if result is False:
        #     self.skipTest("跳过")
        pass

    def tearDown(self):
        self.homepage.home_page()

    # 百度搜索
    def test_search(self):
        """百度搜索"""
        self.homepage.search(u"腾讯视频")

    def test_a_search1(self):
        """百度搜索"""
        self.homepage.search(u"腾讯视频")
        global result
        result = False

    def test_b_search2(self):
        """百度搜索"""
        logger.info(result)
        self.homepage.search(u"腾讯视频")

    def test_c_search3(self):
        """百度搜索"""
        self.homepage.search(u"腾讯视频")


if __name__ == '__main__':
    unittest.main()



