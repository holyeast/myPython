from test_twice import BaiduTest
import unittest

suite = unittest.TestSuite()
suite.addTest(BaiduTest('test_baidu_news'))
suite.addTest(BaiduTest('test_baidu_map'))
unittest.TextTestRunner().run(suite)

