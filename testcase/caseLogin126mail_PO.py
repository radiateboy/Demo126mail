#-*- coding: utf-8 -*-
__author__ = 'tsbc'
import sys
import unittest
import xlrd
reload(sys)
sys.setdefaultencoding('utf-8')
from PO import LoginPage
from selenium import webdriver
from test import test_support
import ConfigParser
class Caselogin126mail(unittest.TestCase):
	"""
	登录126邮箱的case
	"""
	def setUp(self):
		self.driver = webdriver.Ie()
		self.driver.implicitly_wait(30)
		self.verificationErrors = []
		#载入ini配置文件
		cf = ConfigParser.ConfigParser()
		cf.read("..\\data\\login_126mail_data.ini")
		#读取配置数据 url地址
		self.url = cf.get("urlconf", "url")
	#用例执行体
	def action(self, case_id, case_summary, username, password):
		login_page = LoginPage.LoginPage(self.driver, self.url, u"网易")
		login_page.open()
		print u"========【" + case_id + u"】" + case_summary + u"============="
		print username
		print password
		#调用用户名输入组件
		login_page.input_username(username)
		login_page.input_password(password)
		login_page.click_submit()
		spanTF = True
		try:
			login_page.show_span()
			spanTF = True
		except:
			spanTF = False
		if spanTF:
			print login_page.show_span()
		else:
			print self.driver.title
			self.assertTrue(login_page.show_userid(), u"登录失败!")

	@staticmethod
	def getTestFunc(case_id, case_summary, username, password):
		def func(self):
			self.action(case_id, case_summary, username, password)
		return func


	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

def __generateTestCases():
	data = xlrd.open_workbook(u"..\\data\\login_126mail_data.xls")
	#通过索引顺序获取Excel表
	table = data.sheets()[0]
	for args in range(1, table.nrows):
		txt = table.row_values(args)
		setattr(Caselogin126mail, 'test_login126mail_%s' % txt[1], Caselogin126mail.getTestFunc(*txt))
__generateTestCases()


def test_main():
	test_support.run_unittest(Caselogin126mail)