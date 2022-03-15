# coding:utf-8

import pymysql
# from common.readCofig import *
from common.read_yaml import get_yaml_filepath
from common.read_env import environ

# data = ReadYamlConfigs("data.yaml").get_yaml_data()#读取数据
data = get_yaml_filepath(Environ=environ)
db = data['db']
# 获取连接方法
def get_db_conn():
    conn = pymysql.connect(
            host=db['host'],            # 数据库地址
            port=db['port'],         # 端口（配置文件传入的是字符串格式，所以这里取值的时候，用getint的方法 ）
            user=db['user_name'],            # 账号
            passwd=str(db['password']),    # 密码
            db=db['db_name'],    # 要操作的数据库名
            charset='utf8' )# 指定编码格式

    return conn


#查询
def query_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 建立游标
    # cur = conn.cursor()  # 建立游标
    cur.execute(sql)  # 执行sql
    conn.commit()
    result = cur.fetchall()  # 获取所有查询结果
    # result = str(result).replace(",","")  # 去掉逗号
    # result = str(result).replace("(","")  # 去掉逗号
    # result = str(result).replace(")","")  # 去掉逗号
    print(result)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result  # 返回结果


# 更改
def change_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    try:
        cur.execute(sql)  # 执行sql
        conn.commit()  # 提交更改
    except Exception as e:
        conn.rollback()  # 回滚
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接0

# 删除
def delete_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    try:
        cur.execute(sql)  # 执行sql
        conn.commit()  # 提交更改
    except Exception as e:
        conn.rollback()  # 回滚
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接0

# 封装常用数据库操作

#查询
def check_sql(lie=None,biao=None,tiaojian=None,tiaojianzhi=None):
    # 注意sql中''号嵌套的问题
    sql = "SELECT {} FROM {} WHERE {}='{}'".format(lie,biao,tiaojian,tiaojianzhi)
    # sql = "SELECT * FROM test_cloud_user.member_controller.yml WHERE mobile = '18668242746';"
    result = query_db(sql)
    return result
#删除
def delete_sql(biao=None,tiaojian=None,tiaojianzhi=None):
    # 注意sql中''号嵌套的问题
    sql = "DELETE FROM {} WHERE {}='{}'".format(biao,tiaojian,tiaojianzhi)
    result = delete_db(sql)
    return result

# def add_user(name, password):
#     sql = "insert into member_controller.yml (name, passwd) values ('{}','{}')".format(name, password)
#     change_db(sql)
#
#
# def sql(sql=None):
#     # sql = "delete from member_controller.yml where name='{}'".format(name)
#     change_db(sql)

if __name__ == '__main__':
    query_db("select * from uc_user where name_zh='刘勇'")
