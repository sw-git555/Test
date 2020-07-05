import datetime
# 获取当前时间
now_time = datetime.datetime.now()
# 格式化时间字符串
str_time_ymd = now_time.strftime("%Y%m%d")
str_time_mdhms = now_time.strftime("%m%d%H%M%S")
# print(type(str_time_mdhms))