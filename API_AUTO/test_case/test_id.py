from tools.get_global import GetAdmin, GetTeacher, GetStudent
from tools.handle_sqlite import db
from tools.get_global import GetCookie,GetAdminId


# new_admin = getattr(GetAdmin, 'Admin')
# sql = "select ID from cimp_user where username = 'admin'"
# print(sql)
# for i in db.select_sql(sql):
#     print(i[0])

# newid = getattr(GetAdminId,'Adminid')
# a = {'caseid': 2, 'url': 'http://127.0.0.1/api/account', 'data': {'action': 'modifyone', 'id': 0, 'newdata': {'studentno': '0001'}}, 'title': '修改管理员', 'method': 'put', 'data_type': 'json', 'expect': 0, 'test_result': '{\'ret\': 1, \'msg\': \'Traceback (most recent call last):\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\datastore\\\\common\\\\models.py", line 107, in modify\\n    user = User.objects.get(id=uid)\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\manager.py", line 82, in manager_method\\n    return getattr(self.get_queryset(), name)(*args, **kwargs)\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\query.py", line 399, in get\\n    clone = self.filter(*args, **kwargs)\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\query.py", line 892, in filter\\n    return self._filter_or_exclude(False, *args, **kwargs)\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\query.py", line 910, in _filter_or_exclude\\n    clone.query.add_q(Q(*args, **kwargs))\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\sql\\\\query.py", line 1290, in add_q\\n    clause, _ = self._add_q(q_object, self.used_aliases)\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\sql\\\\query.py", line 1318, in _add_q\\n    split_subq=split_subq, simple_col=simple_col,\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\sql\\\\query.py", line 1251, in build_filter\\n    condition = self.build_lookup(lookups, col, value)\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\sql\\\\query.py", line 1116, in build_lookup\\n    lookup = lookup_class(lhs, rhs)\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\lookups.py", line 20, in __init__\\n    self.rhs = self.get_prep_lookup()\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\lookups.py", line 70, in get_prep_lookup\\n    return self.lhs.output_field.get_prep_value(self.rhs)\\n  File "C:\\\\Users\\\\27932\\\\Desktop\\\\API_AUTO\\\\CIMP\\\\cimp\\\\backend\\\\lib\\\\site-packages\\\\django\\\\db\\\\models\\\\fields\\\\__init__.py", line 966, in get_prep_value\\n    return int(value)\\nTypeError: int() argument must be a string, a bytes-like object or a number, not \\\'list\\\'\\n\'}', 'sheet_name': 'put_customer'}
# newid = getattr(GetAdminId,'Adminid')
# a['data']['id'] = newid
# print(a)

item = {'caseid': 2, 'url': 'http://127.0.0.1/api/account', 'data': {'action': 'addone', 'data': {'desc': '一个管理员', 'password': '111111', 'realname': '黎明', 'studentno': '001', 'username': 'admin0705003314', 'usertype': 1000}}, 'title': '添加管理员', 'method': 'post', 'data_type': 'json', 'expect': 0, 'test_result': 'fail', 'test_sql': '{"sql":"SELECT id\n  FROM cimp_user\n  where username = "${admin}"}', 'sheet_name': 'add_customer'}
str = '{"sql":"SELECT id FROM cimp_user where username = "${admin}"}'
if item['test_sql'] and item['test_sql'].find('${admin}') != -1:
    print(item['test_sql'])
    item['test_sql'] = item['test_sql'].replace("${admin}", getattr(GetAdmin, 'Admin'))
    print(item['test_sql'])