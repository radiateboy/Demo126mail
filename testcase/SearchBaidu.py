# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time


class Baidu(unittest.TestCase):
	"""百度首页搜索测试用例"""
	#脚本初始化
	def setUp(self):
		self.driver = webdriver.Ie()
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.baidu.com"
		self.verificationErrors = []
		self.accept_next_alert = True
	#测试用例
	def test_baidu_search(self):
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("kw").clear()
		driver.find_element_by_id("kw").send_keys("selenium")
		driver.find_element_by_id("su").click()
		time.sleep(10)
	
	#脚本退出
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()

