from tools.do_excel import DoExcel
from tools.http_request import HttpRequests
from tools.get_global import GetCookie,GetAdminId


def run(test_data):
    for item in test_data:
        # print(item['data_type'])
        # print(item['data'])
        # print(type(item['data']))
        print("正在执行的用例是{0}".format(item['title']))
        if item['title'] == '修改管理员':
            newid = getattr(GetAdminId,'Adminid')
            item['data']['id'] = newid
        res = HttpRequests(item['url'], item['method'], data=item['data'],
                           cookies=getattr(GetCookie, 'Cookie')).send_request(type=item['data_type'])
        if res.cookies:
            setattr(GetCookie, 'Cookie', res.cookies)
        elif str(res.json()).find('id') != -1 and item['title'] == '添加管理员':
            setattr(GetAdminId, 'Adminid', res.json()['id'])
        print("请求的结果是{0}".format(res.json()))
        DoExcel().write_back(item['caseid'] + 1, 8, str(res.json()), sheet_name=item['sheet_name'])

        if int(res.json()['ret']) == item['expect']:
            test_result = 'pass'
        else:
            test_result = 'fail'
        DoExcel().write_back(item['caseid'] + 1, 9, test_result, sheet_name=item['sheet_name'])


test_data = DoExcel().get_data()
print(test_data)
run(test_data)
