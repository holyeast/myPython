# !/usr/bin/python
# -*- coding:utf-8 -*-

from logs.logger import Logger
from selenium import webdriver
import os
import configparser

logger = Logger(logger="BrowserEngine").getlog()
# 浏览器引擎类
class BrowserEngine(object):

    def __init__(self,driver):
        self.driver = driver

    # 打开浏览器，访问 url 地址
    def open_browser(self, driver, url):
        # 读取 config 配置文件
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        # 读取 config 配置文件内容
        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser." % browser)
        logger.info("The test server url is %s" % url)

        if browser == "FireFox":
             driver = webdriver.Firefox()
             logger.info("Starting firefox browser")
        elif browser == "Chrome":
            driver = webdriver.Chrome()
            logger.info("Starting Chorme browser")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("Starting IE browser")

        try:
            driver.get(url) # 访问 url 地址
            logger.info("Open url %s" % url)
            driver.implicitly_wait(10)
            logger.info("Set implicitly wait 10 seconds")
            driver.maximize_window()
            return driver
        except Exception as e:
            logger.info()

    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        print(self.driver)
        self.driver.quit()