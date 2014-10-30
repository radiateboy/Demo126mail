#-*- coding: utf-8 -*-
__author__ = 'tsbc'

import sys
import time
import unittest
reload(sys)
sys.setdefaultencoding('utf-8')
import location
import saveScreenshot

class PubLogin(unittest.TestCase):
	"""
	对用例登录模块进行封装
	"""
	def login(self, username, password, driver, userinput, passinput, btnsubmit):
		"""
		构造登录使用的公用方法
		"""
		self.driver = driver
		self.fd = location

		self.driver.implicitly_wait(30)
		self.fd.findId(self.driver, userinput).clear()
		self.fd.findId(self.driver, userinput).send_keys(username)
		self.fd.findId(self.driver, passinput).clear()
		self.fd.findId(self.driver, passinput).send_keys(password)
		time.sleep(1)
		saveScreenshot.saveScreenshot(driver, "login126mail")
		self.fd.findId(self.driver, btnsubmit).click()