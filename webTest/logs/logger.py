# !/usr/bin/python
# -*- coding:utf-8 -*-

import logging
import os.path
import time

class Logger(object):

    def getlog(self):
        return self.logger

    # 初始化加载
    def __init__(self,logger):
        # 创建一个 logger 对象
        self.logger = logging.getLogger(logger) # loggger 对象为被执行的对象类
        self.logger.setLevel(logging.DEBUG) # 设置日志模式为调试模式

        # 创建一个 handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time())) # 设置日期格式

        # 创建一个 handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义 handler 输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s ')
        ch.setFormatter(formatter)

        # 给logger 添加 handler
        self.logger.addHandler(ch)





