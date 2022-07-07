import pymysql

class sql_object():
    def mysql_verify(self, varsql):
        """连接数据库"""
        conn = pymysql.connect(
            host='rm-wz9i71jx0x9u04kgd.mysql.rds.aliyuncs.com',
            user='trnuser',
            passwd='admin@123',
            port=3306,
            db='tcm_manager_test',
            charset='utf8')

        """生成游标对象"""
        cur = conn.cursor()

        """查询SQL语句"""
        datao_bject = varsql

        """执行SQL语句"""
        cur.execute(datao_bject)

        """fetchone()方法获得单个的元组，也就是一条记录(row)，如果没有结果，则返回 None"""
        """通过fetchall()方法获得多个数据  返回多个元组，即返回多个记录(rows),则返回 None"""
        data = cur.fetchone()
        listdata = []

        """打印输出所有数据"""
        for i in data[:]:
            listdata.append(i)
        return listdata

        """关闭游标"""
        cur.close()
        """关闭连接"""
        conn.close()


if __name__ == '__main__':
    pass

