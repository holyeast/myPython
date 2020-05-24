# !/usr/bin/python
# -*- coding:utf-8 -*-

import time
import json
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.page_tencent import TentcentPage
from logs.logger import Logger

# 实现类
logger = Logger(logger="Staff").getlog()
class TestTencent(unittest.TestCase):
    """腾讯网站WEB测试"""
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls, url="https://www.tencent.com") # 读取浏览器类型

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 查看公司简介
    def test_about_com_message(self):
        """查看公司简介"""
        tencentpage = TentcentPage(self.driver)
        tencentpage.get_about_con_text(text=u"腾讯以技术丰富互联网用户的生活。")

    def test_about_com_message1(self):
        """查看公司简介"""
        tencentpage = TentcentPage(self.driver)
        tencentpage.get_about_con_text(text=u"腾讯以技术丰富互联网用户的生活。")

    def test_mess_message(self):
        """查看公司简介"""
        tencentpage = TentcentPage(self.driver)
        tencentpage.get_mess_text(text=u"用户为本，科技向善")

    def test_mess_message2(self):
        """查看公司简介"""
        tencentpage = TentcentPage(self.driver)
        tencentpage.get_mess_text(text=u"用户为本，科技向善")

    def test_tencent_fail(self):
        """查看公司简介"""
        tencentpage = TentcentPage(self.driver)
        tencentpage.get_mess_text(text=u"腾讯啊手动阀")




if __name__ == '__main__':
    unittest.main()



