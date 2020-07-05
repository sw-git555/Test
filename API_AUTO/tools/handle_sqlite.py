import sqlite3
from tools.project_path import sqlite_database_path


class HandleSqlite:
    def __init__(self):
        self.conn = sqlite3.connect(sqlite_database_path)
        # 使用cursor()方法获取操作游标
        self.cursor = self.conn.cursor()

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
        except:
            # 发生错误时回滚
            self.conn.rollback()

    def close_sql(self):
        # 关闭连接
        self.conn.close()


db = HandleSqlite()
if __name__ == '__main__':
    sql = "SELECT id FROM cimp_user where username ='admin0704180705'"
    print(db.select_sql(sql)[0][0])
# sql = "delete from common_customer where id = 46 "

# db.close()
