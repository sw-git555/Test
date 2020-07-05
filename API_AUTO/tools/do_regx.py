import re
from tools.get_global import GetAdmin


class DoRegx:
    def do_regx(self, s, g_class):
        while re.search('\$\{(.*?)\}', s):
            key = re.search('\$\{(.*?)\}', s).group(0)
            value = re.search('\$\{(.*?)\}', s).group(1)
            s = s.replace(key, str(getattr(g_class, value)))
        return s


# if __name__ == '__main__':
#     s1 = '{"action":"addone","data" :{"desc": "一个管理员","password": "111111","realname": "黎明","studentno": "001","username": "${admin}","usertype": 1000}}'
#     s = DoRegx().do_regx(s1,GetAdmin)
#     print(s)

""":头匹配
group() == group(0)
group(1/2/...)根据match里的()分组
"""
# s = 'www.baidu.com'
# res = re.match('(w)(ww)',s)# 全匹配
# print(res.group())

""":findall
查找需要匹配的内容，存在列表里
如果分组，列表里嵌套元组
返回所有能查到的结果
"""
# s = 'hellowordhello'
# res = re.findall('(he)(llo)', s)
# res = re.findall('hello', s)
# print(res)


""":search()
思想：
    1.匹配到$后的变量名，把名字分组
    2.group()匹配到${username},作为被替换的值
    3.group(1)匹配到username,可以设定为全局变量需要反射的值例如：getattr(GetAdmin,group(1))
    4.全局变量的名字必须和${var}的var相等才方便使用
"""
# s = '{"username": "${username}", "password": "1234"}'
# res = re.search('\$\{(.*?)\}',s)
# print(res.group())
# print(res.group(1))
