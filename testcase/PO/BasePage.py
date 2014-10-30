#-*- coding: utf-8 -*-
__author__ = 'tsbc'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class BasePage(object):
	"""
	BasePage封装所有页面都公用的方法，例如driver, url
	"""
	#初始化driver、url、等
	def __init__(self, selenium_driver, base_url, pagetitle):
		self.base_url = base_url
		self.pagetitle = pagetitle
		self.driver = selenium_driver
		self.verificationErrors = []

	#打开页面，校验页面链接是否加载正确
	def _open(self, url, pagetitle):
		#使用get打开访问链接地址
		self.driver.get(url)
		self.driver.maximize_window()
		#使用assert进行校验，打开的链接地址是否与配置的地址一致。调用on_page()方法
		assert self.on_page(pagetitle), u"打开开页面失败 %s" % url

	#重写元素定位方法
	def find_element(self, *loc):
		return self.driver.find_element(*loc)

	#定义open方法，调用_open()进行打开链接
	def open(self):
		self._open(self.base_url, self.pagetitle)

	#使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
	def on_page(self, pagetitle):
		return pagetitle in self.driver.title

	#定义script方法，用于执行js脚本，范围执行结果
	def script(self, src):
		return self.driver.execute_script(src)

	#重写定义send_keys方法
	def send_keys(self, loc, vaule, clear_first=True, click_first=True):
		try:
			loc = getattr(self, "_%s" % loc)
			if click_first:
				self.find_element(*loc).click()
			if clear_first:
				self.find_element(*loc).clear()
			self.find_element(*loc).send_keys(vaule)
		except AttributeError:
			print u"%s 页面中未能找到 %s 元素" % (self, loc)