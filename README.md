# SeleniumAutomatedTestCases

当临时项目126邮箱登录功能以及联系人管理功能脚本开发

登录账号：auto_tester
密码：123qwe

可以调用public目录下的plogin126mail.py中的login方法进行登录。
再不适用PO的情况下，可以使用public\location.py 中重新构造的find_element方法
项目目录介绍：

data目录用来存储  数据文件
result 目录用来存储测试报告
result\image 目录用来存储截图快照
testcase 目录用来存放要执行的测试脚本，只要是case,全部以“case”为文件开头
testcase\public 目录用来存放公共方法，和重定义过的通用方法
testcase\PO 以PO设计模型编写脚本，以页面为单位进行划分（BasePage+各个页面脚本）
test_doc 目录存储测试用例设计等相关文档（由简到繁，慢慢补充）
