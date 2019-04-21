# coding:utf-8
import unittest
import HTMLTestRunner

#     生成HTML 测试报告


# 用例路径
case_dir = "D:\\test\\test_unit\\test_case"

def all_case():
    discover = unittest.defaultTestLoader.discover(start_dir=case_dir,  # 测试用例所在的路径
                                                   pattern='test*.py',
                                                   top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    import time
    # now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    # 报告存放路径
    report_path = "D:\\test\\test_unit\\test_report\\result.html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case())

    fp.close()