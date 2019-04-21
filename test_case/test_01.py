# coding:utf-8

#  unittest测试用例

from selenium import webdriver
import unittest
import time

# test1 继承unittest.TestCase
class Test1(unittest.TestCase):

    # 定义一个测试类，是多个测试用例的集合，可以把一些相同的操作写成一个类

    def setUp(self):   # 前置条件操作
        self.driver = webdriver.Chrome()
        self.driver.get("http:www.baidu.com")

    def test_01(self):     # 定义一个测试用例名称
        self.driver .find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()

        time.sleep(2)
        test_result = self.driver.title
        print(test_result)  # 只是打印出测试结果test_result
        # 断言：判断测试结果与我们的预期结果是不是相同的
        qiwang = u'selenium_百度搜索'
        self.assertEqual(test_result,qiwang)   # 判断结果是否相等

    def test_02(self):
        self.driver.find_element_by_id("kw").send_keys("python")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        test_result2 = self.driver.title
        print(test_result2)  # 只是打印出测试结果test_result
        # 断言：判断测试结果与我们的预期结果是不是相同的

        qiwang_2 = u'python_百度搜索'
        self.assertEqual(test_result2, qiwang_2)  # 判断结果是否相等

    def tearDown(self):      # 后置操作tearDown
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
