# !/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import os
import time
from selenium import webdriver
from testsuits.test_baidu import TestBaidu
from  testsuits.test_tencent import TestTencent
from unit.HTMLTestRunner import HTMLTestRunner


# unittest suite 批量添加测试用例，逐个进行执行
suite = unittest.TestSuite()
suite.addTest(TestBaidu('test_search'))
suite.addTest(TestBaidu('test_search1'))
suite.addTest(TestBaidu('test_search2'))
suite.addTest(TestBaidu('test_search3'))
suite.addTest(TestBaidu('test_error'))
suite.addTest(TestTencent('test_about_com_message'))
suite.addTest(TestTencent('test_about_com_message1'))
suite.addTest(TestTencent('test_mess_message'))
suite.addTest(TestTencent('test_mess_message2'))
suite.addTest(TestTencent('test_tencent_fail'))

# 测试报告 title
xxx_title = u"EMC项目Web自动化测试报告"
# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
print(HtmlFile)
isExists = os.path.exists(report_path)
if not isExists:
    try:
        os.makedirs(report_path)
    except Exception as e:
        print("创建文件夹失败",e)

if __name__ == '__main__':
    # open(HemlFile) 创建 html 测试报告
    with open(HtmlFile,"wb") as report:
        runner = HTMLTestRunner(stream=report,title=xxx_title,description=u"测试结果")
        runner.run(suite)

    # driver = webdriver.PhantomJS()
    # driver.maximize_window()
    # driver.get("https://blog.csdn.net/huilan_same/article/details/52160186")
    # time.sleep(10)
    # driver.save_screenshot("report.png")
    # time.sleep(10)
    # driver.close()
    # print(suite)
    # for i in suite:
    #     print(i)
    #     runner.run(i)
