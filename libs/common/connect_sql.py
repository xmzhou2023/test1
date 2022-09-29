import pymysql
import cx_Oracle
from libs.common.read_config import *


class SQL(object):
    def __init__(self, name, env, ini_name=None, values=None):  # 此处可以加入这个类中需要定义的参数
        self.name = name
        self.env = env
        self.ini_name = ini_name
        self.values = values
        self.ini = ReadConfig(self.name, self.env)
        self.sql = ast.literal_eval(self.ini.db)

    # 获取连接方法
    def get_db_conn(self):
        if self.ini_name == None:
            if self.sql['drive'].lower() == 'mysql':
                conn = pymysql.connect(
                    host=self.sql['host'],                            # 数据库地址
                    port=self.sql['port'],                            # 端口（配置文件传入的是字符串格式，所以这里取值的时候，用getint的方法 ）
                    user=self.sql['user_name'],                       # 账号
                    passwd=str(self.sql['password']),                 # 密码
                    db=self.sql['db_name'],                           # 要操作的数据库名
                    charset='utf8')                              # 指定编码格式
                return conn
            elif self.sql['drive'].lower() == 'oracle':                             # 指定编码格式
                conn = cx_Oracle.connect("{}/{}@{}:{}/{}".format(
                    self.sql['user_name'],
                    self.sql['password'],
                    self.sql['host'],
                    self.sql['port'],
                    self.sql['db_name']))
                return conn
        else:
            sql = ast.literal_eval(self.ini.IPM_db)
            conn = pymysql.connect(
                host=sql['host'],  # 数据库地址
                port=sql['port'],  # 端口（配置文件传入的是字符串格式，所以这里取值的时候，用getint的方法 ）
                user=sql['user_name'],  # 账号
                passwd=str(sql['password']),  # 密码
                db=sql['db_name'],  # 要操作的数据库名
                charset='utf8')  # 指定编码格式
            return conn

    # 查询
    def query_db(self, sql):
        conn = self.get_db_conn()                                  # 获取连接
        if self.sql['drive'].lower() == 'mysql':
            cur = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 建立游标
            cur.execute(sql)                                      # 执行sql
            conn.commit()
            result = cur.fetchall()                               # 获取所有查询结果

        elif self.sql['drive'].lower() == 'oracle':
            cur = conn.cursor()  # 建立游标
            cur.execute(sql)
            columnNames = [d[0].lower() for d in cur.description]# 执行sql
            conn.commit()
            result = cur.fetchall()                               # 获取所有查询结果
            result = [dict(zip(columnNames, row)) for row in result]
        cur.close()                                           # 关闭游标
        conn.close()                                          # 关闭连接
        return result

    # 更改
    def change_db(self, sql):
        conn = self.get_db_conn()                            # 获取连接
        cur = conn.cursor()                             # 建立游标
        try:
            cur.execute(sql)                            # 执行sql
            conn.commit()                               # 提交更改
        except Exception as e:
            conn.rollback()                             # 回滚
        finally:
            cur.close()                                 # 关闭游标
            conn.close()                                # 关闭连接0

    # 删除
    def delete_db(self, sql):
        conn = self.get_db_conn()                            # 获取连接
        cur = conn.cursor()                             # 建立游标
        try:
            cur.execute(sql)                            # 执行sql
            conn.commit()                               # 提交更改
        except Exception as e:
            conn.rollback()                             # 回滚
        finally:
            cur.close()                                 # 关闭游标
            conn.close()                                # 关闭连接0

    """ -----------------常用SQL----------------------- """

    def check_sql(self, column=None, table=None, condition=None, condition_value=None):
        """查询"""
        try:
            sql = "SELECT {} FROM {} WHERE {}='{}'".format(column, table, condition, condition_value)
            # sql = "SELECT * FROM test_cloud_user.member_controller.yml WHERE mobile = '18668242746';"
            result = self.query_db(sql)
            return result
        except Exception as e:
            return e

    def insert_sql(self, table=None, condition=None, condition_value=None):
        """新增"""
        try:
            sql = "INSERT INTO {}({}) VALUES ({})".format(table, condition, condition_value)
            self.change_db(sql)
            result = self.query_db("SELECT * from {}".format(table))
            return result
        except Exception as e:
            return e

    def delete_sql(self, table=None,condition=None, condition_value=None):
        """删除"""
        try:
            sql = "DELETE FROM {} WHERE {}='{}'".format(table, condition, condition_value)
            result = self.delete_db(sql)
            return result
        except Exception as e:
            return e

    def update_sql(self, table=None,column=None, column_value=None,condition=None, condition_value=None):
        """修改"""
        try:
            sql = "UPDATE {} SET {}='{}' WHERE {}='{}'".format(table, column, column_value, condition, condition_value)
            self.change_db(sql)
            result = self.query_db("SELECT * FROM {} WHERE {}='{}'".format(table, column_value, condition))
            return result
        except Exception as e:
            return e

if __name__ == '__main__':
    a = SQL('DRP','test')
    # print(a.query_db("select * from uc_user where name_zh='刘勇' and card_no='18650617'"))
    print(a.check_sql(column='*',table='uc_user',condition='name_zh',condition_value="黄琴"))
    # print(a.delete_sql(table='uc_user',condition='id',condition_value='1'))
    # print(a.insert_sql(table='uc_user',condition='id,name_zh,email,card_no',condition_value="'1','测试人员','yong.liu6@transsion.com','18888888'"))
    # print(a.update_sql(table='uc_user',column='name_zh',column_value='evan',condition='card_no',condition_value='18888888'))
    IPM = SQL('TBM','test')
    print(IPM.query_db("SELECT count(bid) FROM kd_device_info WHERE model = '50A712U'"))
    # print(IPM.query_db("SELECT DISTINCT obj_type_name FROM flow_mat_member WHERE obj_type_name='2.4G wifi saw' and is_delete=0;"))
    a = SQL("OA", "test")
    ie = a.query_db(
        "select count(gdzt) from ECOLOGY.uf_gdcs where lcid in (select requestid from ECOLOGY.workflow_requestbase where currentnodetype ='3'  and requestid in(select lcid from ECOLOGY.uf_gdcs )) and gdzt !='0'")
    print(ie)
