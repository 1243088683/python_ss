# coding:utf-8
import unittest
# 一次执行文件中所有的用例


# from common import HTMLTestRunner  新建文件夹common下放置

# 直接放在lib文件里
import HTMLTestRunner

# 下面三行代码python2报告出现乱码时候可以加上
'''import sys
reload(sys)
sys.setdefaul tencoding('utf8')'''



# 测试用例所在的路径
case_dir = "D:\\test\\test_unit\\test_case"
# 想单独执行某个文件夹下的子文件 直接在后面加路径比如baidu
# case_dir = "D:\\test\\test_unit\\test_case\\baidu"

'''想单独执行test_00 开头的脚本
defaultTestLoader 加载所有的测试用例（pattern='test_00*.py',）'''
# discover 方法加载全部用例
discover = unittest.defaultTestLoader.discover(start_dir=case_dir,  # 测试用例所在的路径
                                               pattern='test*.py',
                                               top_level_dir=None)

print(discover)

# 批量运行所有的用例    TestRunner 指的是运行器

'''runner = unittest.TextTestRunner()
# TextTestRunner 进行测试用例执行的实例，其中text的意思是以文本形式显示测试结果
runner.run(discover)'''

if __name__ == '__main__':
    # 指定存放报告的路径
    report_path = "D:\\test\\test_unit\\test_report\\result.html"

    fp = open(report_path,"wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="测试报告的主题",
                                           description="这是什么项目的测试报告")
    runner.run(discover)



