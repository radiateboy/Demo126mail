# -*- coding: utf-8 -*-
import csv


class ld():

	#读取本地CSV文件
	my_file = "data\\mail_login.csv"

	data = csv.reader(file(my_file, 'rb'))


	def logindata(self):
		for keys in data:
			if "login_name" != keys[0]:
				username = keys[0]
				print username
			if "login_password" != keys[1]:
				password = keys[1]
				print password
			if "remark" != keys[2]:
				remark = keys[2]
				print remark
smallld = ld()
