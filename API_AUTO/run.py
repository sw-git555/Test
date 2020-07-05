import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
from test_case.test_http import TestHttp
from tools.project_path import test_report_path

# 测试套件
suite = unittest.TestSuite()
# suite.addTest(TestHttpRequest('test_api'))  # 测试类的实例
# 多模块运行
# 方法1：分多个文件
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttp))
#suite.addTest(loader.loadTestsFromTestCase(XXXX))

# 方法2：

# 普通执行
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 生成报告
with open(test_report_path, 'wb') as f:
    runner = HTMLTestRunner(stream=f,
                            title="test report",
                            description="测试报告:",
                            verbosity=2)

    runner.run(suite)