'''
# -*- coding: utf-8 -*-
# @Time : 2022/6/20 14:00
# @Author : 李小素
# @File :
# @Software: PyCharm
# @project: 数据库
'''
from libs.common.connect_sql import *
from libs.common.logger_ui import log
from project.IPM.page_base.yamlbase import *

class IpmMysql(SQL):
    def __init__(self,parameter,expect=None,ininame='database',name='IPM', env='test'):
        """
        数据库查询并返回值到list
        :param expect: yaml文件名
        :param ininame: ini模块名
        :param parameter: ini参数名
        :param name: 路径_项目
        :param env: 路径_ini配置文件
        """
        super().__init__(name, env,ininame,parameter)
        self.filelist = YamlRead(expect)

    def query_sql(self,sql):
        res=self.query_db(sql=self.filelist.yaml_read(sql))
        return res

    def db_delete(self,sql):
        self.delete_db(sql=self.filelist.yaml_read(sql))

    def db_updata(self,sql):
        self.change_db(sql=self.filelist.yaml_read(sql))

def pluck(lst, key):
  return [x.get(key) for x in lst]

def sql_query_db(databases,sql,listname):

    """
      数据库查询并返回值到list
      :param databases: 数据库表名（在ini配置文件中database已配置）
      :param sql: 传入sql
      :param listname: 查询字段名
      """
    mysql=SQL('IPM','test','database',databases)
    lis = mysql.query_db(sql=sql)
    return pluck(lis, listname)

def listsma(lists):
    """
      遍历list内的每一个元素，如果该元素不是列表或元组就加到生成器里，如果是可迭代对象就继续递归调用，直到把所有子列表都打散，最终返回一个大列表
      :param lists: list
      """
    for k in lists:
        if not isinstance(k,(list,tuple)):
            yield k
        else:
            yield from listsma(k)





def generatelist(databases_one,sql_one,listname_one,databases_two,sql_two,listname_two):
    """
      多个数据库之间的关联查询
      :param databases_one: 数据库表名
      :param sql_one: sql
      :param listname_one: 查询字段名
      :param databases_two: 第二个数据库名
      :param sql_two: sql
      :param listname_two: 查询字段名
      """
    res=sql_query_db(databases_one,sql_one,listname_one)
    lists = []
    for i, k in enumerate(res):
        try:
            result = sql_query_db(databases=databases_two,
                             sql=f"{sql_two}='{k}'",        #f"SELECT field_name FROM flow_field WHERE field_code='{k}'",
                             listname=listname_two)
            lists.append(result)
        except:
            log.info('SQL执行报错')
            raise
    return list(listsma(lists))


if __name__ == '__main__':
    # sql=IpmMysql(expect='center_Personal.yaml',parameter='db_ipm_config_uat')
    # print(sql.query_sql('查询2'))
    # print(sql_query_db('db_ipm_config_uat','SELECT node_bid FROM flow_mat_node WHERE flow_type="MOBILE"AND state_code="enable"','node_bid'))
    # generatelist('db_ipm_config_uat','SELECT * FROM flow_mat_member WHERE flow_type="MOBILE" and obj_type_name="CKD_110" and is_delete=0 ','')
    res=sql_query_db('db_ipm_config_uat',
        "SELECT `constraint` -> '$.isHeader' FROM view_config_attr where display_name='工厂' and view_bid = '958708729249927168' LIMIT 1",
                  "'constraint` -> '$.isHeader'")
    print(res)