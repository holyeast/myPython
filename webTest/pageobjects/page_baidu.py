# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
 页面类，主要存放页面的元素定位和简单的操作函数.
 页面类主要是元素定位和页面操作写成函数，以供测试类使用
 集成 BasePage 二次封装通用类
 通常 1个页面为一个类
"""
# EMC首页类
from unit.base_page import BasePage
import  time


class BaiduPage(BasePage):

    input_box_xpath = "xpath=>//input[@name='wd']"
    btn_sure_xpath = "xpath=>//input[@value='百度一下']"
    # 首页
    home_page_xpath = "xpath=>//a[text()='百度首页']"

    def home_page(self):
        self.click(self.home_page_xpath)
        time.sleep(1)
        print("返回百度首页")

    def search(self, keyword):
        self.send_keys(self.input_box_xpath, keyword)
        self.click(self.btn_sure_xpath)






