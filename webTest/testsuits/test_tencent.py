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

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self, url="https://www.tencent.com") # 读取浏览器类型

    def tearDown(self):
        self.driver.quit()

    # 查看公司简介
    def test_about_com_message(self):
        """查看公司简介"""
        tencentpage = TentcentPage(self.driver)
        tencentpage.get_about_con_text(text=u"腾讯啊手动阀")



if __name__ == '__main__':
    unittest.main()



