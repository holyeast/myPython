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
suite_class = unittest.TestLoader().loadTestsFromTestCase(TestBaidu)
print(suite_class)
suite_discover = unittest.TestLoader().discover(start_dir='testsuits', pattern='test_*.py')
print(suite_discover)
suite.addTests(suite_baidu)


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
        runner = HTMLTestRunner(stream=report,title=xxx_title,description=u"测试结果", verbosity=2)
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

