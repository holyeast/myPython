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

# from pageobjects.emc_homepage import  EmcHomePage
import  time
from logs.logger import Logger
logger = Logger(logger="Tencent").getlog()

class TentcentPage(BasePage):
    # 简介
    about_btn_xpath = "xpath=>//a[@href='https://www.tencent.com/zh-cn/about.html']"
    # 公司简介
    about_con_btn_xpath = "xpath=>//a[@href='https://www.tencent.com/zh-cn/about.html#about-con-1']"
    # 简介内容
    text_about_con_xpath = "xpath=>//div[@class='brief-text-box']/h4"
    # 愿景和使命
    text_mess_xpath = "xpath=>//div[@class='r-mess mess']/p"


    def get_about_con_text(self, text):
        """腾讯-公司简介"""
        self.hover_mouse(self.about_btn_xpath)
        time.sleep(1)
        self.click(self.about_con_btn_xpath)
        result = self.find_element(self.text_about_con_xpath).text
        assert result == text

    def get_mess_text(self, text):
        """腾讯-愿景和使命"""
        result = self.find_element(self.text_mess_xpath).text
        assert result == text

