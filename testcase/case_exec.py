#-*- coding: utf-8 -*-
__author__ = 'tsbc'

import unittest
import sys, time
import caseLogin126mail_PO
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("public")
from public import HTMLTestRunner

#定义单元测试容器
testunit = unittest.TestSuite()


#将测试用例加入测试容器中
testunit.addTest(unittest.makeSuite(caseLogin126mail_PO.Caselogin126mail))

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

#定义个报告存放路径，支持相对路径
filename = "..\\result\\"+now+"_result.html"
fp = file(filename, 'wb')

#定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')

#运行测试用例
runner.run(testunit)
fp.close() #关闭报告文件