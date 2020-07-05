import pymysql
from tools.read_config import ReadConfig
from tools.project_path import mysql_config_path


class HandleMysql:
    def __init__(self):
        db_config = eval(ReadConfig.get_config(mysql_config_path, 'Config', 'db_config'))
        db = pymysql.connect(db_config["host"], db_config["user"], db_config["password"],
                             db_config["database"], port=db_config["port"])
        self.cursor = db.cursor()

    def select_sql(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute_sql(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            print('执行成功')
            # 提交修改
            self.conn.commit()
            print('修改成功')
        except Exception as e:
            # 发生错误时回滚
            self.conn.rollback()


if __name__ == '__main__':
    sql = 'select * from jobs'
    data = HandleMysql().select_sql(sql)
    print(data)
    print(type(data))
    for i in data:
        print(i)
