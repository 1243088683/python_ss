# coding:utf-8
import unittest

class Test(unittest.TestCase):
    u'''这是一个类的描述'''

    def setUp(self):
        print("---start---")

    def tearDown(self):
        print("---end---")

    def login(self):
        print("这是登录方法")

    def test_01(self):          # 定义一个测试用例名称
        self.login()
        u'''这是描述这个用例：账号---密码----'''
        a = 1
        b = 2   # 描述一行
        self.assertEqual(3,a+b)      # 断言a+b是不是等于3

    def test_02(self):
        u'''这是描述这个用例：账号---密码----'''
        a = '百度搜索'
        b = '百度'
        # self.assertEqual(1,b-a)    # 判断相等
        # self.assertFalse(b)
        # self.assertTrue(a)
        self.assertIn(b,a, msg="%s 不在 %s 里面"%(b,a))  # 包含的意思  第3位为输入中文

    def test_03(self):
        print("3333")
        self.assertEqual(1,1)

class Test8(unittest.TestCase):

    def setUp(self):
        print("3")

    def tearDown(self):
        print("444")

if __name__ == '__main__':
    unittest.main()

