import os
from tools.get_date import str_time_ymd

'''专门读取路径的值'''
# 根目录
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试用例路径
test_case_path = os.path.join(base_path, 'test_data', 'test.xlsx')
# 测试报告路径
test_report_path = os.path.join(base_path, 'test_result', 'http_report', 'test.html')
# 测试图片路径
test_image_path = os.path.join(base_path, 'test_result', 'image', 'test.jpg')
# 用例配置文件路径
case_config_path = os.path.join(base_path, 'config', 'case.config')
# mysql配置文件路径
mysqldb_config_path = os.path.join(base_path, 'config', 'database.config')
# 邮件配置文件路径
mail_config_path = os.path.join(base_path, 'config', 'mail.config')
# 日志文件路径
log_path = os.path.join(base_path, 'test_result', 'log', str_time_ymd + '.txt')
# sqlite数据库文件路径
sqlite_database_path = os.path.join(base_path, 'CIMP', 'cimp', 'backend', 'db.sqlite3')
# mysql配置文件路径
mysql_config_path = os.path.join(base_path, 'config', 'database.config')
# print(database_path)
