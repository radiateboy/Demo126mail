# -*- coding: utf-8 -*-
from selenium import webdriver
import sys
sys.path.append("public")
from public import location
from public import plogin126mail
from test import test_support
import unittest
import xlrd
import ConfigParser

class Login126Mail(unittest.TestCase):
	def setUp(self):
		print "start"
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		#声明find_element方法
		self.fd = location
		self.verificationErrors = []
		#载入ini配置文件
		cf = ConfigParser.ConfigParser()
		cf.read("..\\data\\login_126mail_data.ini")
		#读取配置数据
		self.base_url = cf.get("urlconf", "url")
		#定义用户名密码变量
		# self.username = "auto_tester"
		# self.password = "123qwe"
		#定位关键字变量
		self.userinput = cf.get("keywords", "userinput")
		self.passinput = cf.get("keywords", "passinput")
		self.btnsubmit = cf.get("keywords", "btnsubmit")
		self.errorwords = cf.get("keywords", "errorwords")
		self.useridwords = cf.get("keywords", "useridwords")
		self.lg = plogin126mail.PubLogin("login")

	def action(self, case_id, case_summary, username, password):
		self.driver.get(self.base_url)
		self.driver.maximize_window()
		print u"========【" + case_id + u"】" + case_summary + u"============="
		print username
		print password
		self.lg.login(username, password, self.driver, self.userinput, self.passinput, self.btnsubmit)
		spanTF = True
		try:
			errortxt = self.fd.findCss(self.driver, self.errorwords).text
			spanTF = True
		except:
			spanTF = False
		if spanTF:
			print errortxt
		else:
			print self.driver.title
			self.assertTrue(self.fd.findId(self.driver, self.useridwords).text, u"登录跳转失败!")

	@staticmethod
	def getTestFunc(case_id, case_summary, username, password):
		def func(self):
			self.action(case_id, case_summary, username, password)
		return func


	def tearDown(self):
		print "finished"
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

def __generateTestCases():
	data = xlrd.open_workbook(u"..\\data\\login_126mail_data.xls")
	#通过索引顺序获取Excel表
	table = data.sheets()[0]
	for args in range(1, table.nrows):
		txt = table.row_values(args)
		setattr(Login126Mail, 'test_login126mail_%s' % txt[1], Login126Mail.getTestFunc(*txt))
__generateTestCases()


def test_main():
	test_support.run_unittest(Login126Mail)
