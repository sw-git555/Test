import unittest
from tools.http_request import HttpRequests
from tools.get_global import GetCookie, GetAdminId, GetAdmin
from ddt import ddt, data
from tools.read_config import ReadConfig
from tools.do_excel import DoExcel
from tools.print_log import initLogging
from tools.project_path import log_path, case_config_path
from tools.handle_sqlite import HandleSqlite

test_data = DoExcel().get_data()


# print(test_data)


# print(test_data)

@ddt
class TestHttp(unittest.TestCase):
    result_list = []
    test_result_list = []

    def setUp(self):
        print('start')

    def tearDown(self):
        print('end')

    @classmethod
    def tearDownClass(cls, result_list=result_list, test_result_list=test_result_list):
        DoExcel().write_all_back(result_data=result_list, test_result_data=test_result_list)

    @data(*test_data)
    def test_api(self, item, result_list=result_list, test_result_list=test_result_list):
        print("正在执行的用例是{0}".format(item['title']))
        excel_row = eval(ReadConfig().get_config(case_config_path, 'Excel_row', 'excel_row'))
        if item['title'] == '修改管理员':
            newid = getattr(GetAdminId, 'Adminid')
            item['data']['id'] = newid
        res = HttpRequests(item['url'], item['method'], data=item['data'],
                           cookies=getattr(GetCookie, 'Cookie')).send_request('json')
        if res.cookies:
            setattr(GetCookie, 'Cookie', res.cookies)
        if str(res.json()).find('id') != -1 and item['title'] == '添加管理员':
            setattr(GetAdminId, 'Adminid', res.json()['id'])
        if item['test_sql'] and item['test_sql'].find('${admin}') != -1:
            item['test_sql'] = item['test_sql'].replace('${admin}', getattr(GetAdmin, 'admin'))
        try:
            if item['test_sql'] is not None:
                sql_result = HandleSqlite().select_sql(eval(item['test_sql'])['sql'])
                if sql_result:
                    self.assertEqual(sql_result[0][0], res.json()['id'])
            self.assertEqual(int(res.json()['ret']), item['expect'])
            test_result = 'pass'
        except AssertionError as e:
            test_result = 'fail'
            initLogging(log_path, e)
        except Exception as e:
            print('执行了Exception')
            test_result = 'fail'
            initLogging(log_path, e)
        finally:
            # DoExcel().write_back(item['caseid'] + 1, excel_row['result'], str(res.json()),
            #                      sheet_name=item['sheet_name'])
            # DoExcel().write_back(item['caseid'] + 1, excel_row['test_result'], test_result,
            #                      sheet_name=item['sheet_name'])
            str_json = str(res.json())
            result_list.append(str_json)
            test_result_list.append(test_result)


if __name__ == '__main__':
    unittest.main()
