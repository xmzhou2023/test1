
'''
#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/5/18 16:00
# @Author : 李小素
# @File : test_area_cfg.py
# @Software: PyCharm
# @title:个人中心
'''

from project.IPM.page_object.Center_Component import *
from libs.common.logger_ui import log
from public.base.assert_ui import *
from project.IPM.page_base.pubic_element import *






#断言
class AssertMode(PubicMethod):

    def assert_elements_Small(self, expected_results, actual_results, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与yamlw文件断言<=
        '''
        global form_list, form
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = self.filelist.yaml_read(expected_results)
            log.info(f'{form}')
            assert set(form) <= set(form_list)
            log.info(f'查询结果字段{form_list}与包含字段{form}一致')
        except:
            log.error(f'{form_list}<={form}断言失败')
            raise

    def db_assert_elements_Small(self, expected_results, listname, actual_results,databases, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言<=
        '''
        global form_list, form
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = sql_query_db(databases=databases,sql=self.filelist.yaml_read(expected_results),
                                listname=listname)
            log.info(f'{form}')
            assert set(form) <= set(form_list)
            log.info(f'查询结果字段{form_list}与包含字段{form}一致')
        except:
            log.error(f'{form_list}<={form}断言失败')
            raise

    def many_db_assert_elements_Small(self, databases_one, sql_one,listname_one,databases_two,sql_two,listname_two, actual_results, get_attributs='innerText'):
        '''

        databases_one:数据库表名
        sql_one：sql
        listname_one:查询字段名
        databases_two：第二个数据库名
        sql_two：sql
        listname_two：查询字段名   (获取预期结果)
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言<=
        '''
        global form_list, form
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = generatelist(databases_one,
                     self.filelist.yaml_read(sql_one),
                     listname_one,databases_two,
                     self.filelist.yaml_read(sql_two),
                     listname_two)
            log.info(f'{form}')
            assert set(form) <= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise
    def assert_elements_large(self, expected_results, actual_results, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与yamlw文件断言>=
        '''
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = self.filelist.yaml_read(expected_results)
            log.info(f'{form}')
            assert set(form) >= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def db_assert_elements_large(self, expected_results, listname, actual_results, databases,get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言>=
        '''
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = sql_query_db(databases=databases,sql=self.filelist.yaml_read(expected_results),
                                listname=listname)
            log.info(f'{form}')
            assert set(form) >= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def many_db_assert_elements_large(self, databases_one, sql_one,listname_one,databases_two,sql_two,listname_two, actual_results,get_attributs='innerText'):
        '''
        databases_one:数据库表名
        sql_one：sql
        listname_one:查询字段名
        databases_two：第二个数据库名
        sql_two：sql
        listname_two：查询字段名   (获取预期结果)
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言>=
        '''
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = generatelist(databases_one,
                     self.filelist.yaml_read(sql_one),
                     listname_one,databases_two,
                     self.filelist.yaml_read(sql_two),
                     listname_two)

            log.info(f'{form}')
            assert set(form) >= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def assert_elements_equal(self, expected_results, actual_results, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与yamlw文件断言==
        '''
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = self.filelist.yaml_read(expected_results)
            log.info(f'{form}')
            assert set(form) == set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def db_assert_elements_equal(self, expected_results, listname, actual_results,databases, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言==
        '''
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = sql_query_db(databases=databases,sql=self.filelist.yaml_read(expected_results),
                                listname=listname)
            log.info(f'{form}')
            assert set(form) == set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise


    def many_db_assert_elements_equal(self, databases_one, sql_one,listname_one,databases_two,sql_two,listname_two, actual_results, get_attributs='innerText'):
        '''
        databases_one:数据库表名
        sql_one：sql
        listname_one:查询字段名
        databases_two：第二个数据库名
        sql_two：sql
        listname_two：查询字段名   (获取预期结果)
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言==
        '''
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = generatelist(databases_one,
                     self.filelist.yaml_read(sql_one),
                     listname_one,databases_two,
                     self.filelist.yaml_read(sql_two),
                     listname_two)

            log.info(f'{form}')
            assert set(form) == set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise
    def assert_elements_notequal(self, expected_results, actual_results, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与yamlw文件断言!=
        '''
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = self.filelist.yaml_read(expected_results)
            log.info(f'{form}')
            assert set(form) != set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise
    def db_assert_elements_notequal(self, expected_results, listname, actual_results,databases, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言!=
        '''
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = sql_query_db(databases=databases,sql=self.filelist.yaml_read(expected_results),
                                listname=listname)
            log.info(f'{form}')
            assert set(form) != set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def many_db_assert_elements_notequal(self, databases_one, sql_one,listname_one,databases_two,sql_two,listname_two, actual_results, get_attributs='innerText'):
        '''
        databases_one:数据库表名
        sql_one：sql
        listname_one:查询字段名
        databases_two：第二个数据库名
        sql_two：sql
        listname_two：查询字段名   (获取预期结果)
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言!=
        '''
        try:

            form_list = self.form_elements(formheader=actual_results, get_attributs=get_attributs)
            form = generatelist(databases_one,
                     self.filelist.yaml_read(sql_one),
                     listname_one,databases_two,
                     self.filelist.yaml_read(sql_two),
                     listname_two)
            log.info(f'{form}')
            assert set(form) != set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise
    def assert_elements_Smalls(self, expected_results, actual_results, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与yamlw文件断言<=,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = self.filelist.yaml_read(expected_results)
            log.info(f'{form}')
            assert set(form) <= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise
    def db_assert_elements_Smalls(self, expected_results, listname, actual_results,databases, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言<=,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = sql_query_db(databases=databases,sql=self.filelist.yaml_read(expected_results),
                                listname=listname)
            log.info(f'{form}')
            assert set(form) <= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def many_db_assert_elements_Smalls(self, databases_one, sql_one,listname_one,databases_two,sql_two,listname_two, actual_results, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言<=,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = generatelist(databases_one,
                     self.filelist.yaml_read(sql_one),
                     listname_one,databases_two,
                     self.filelist.yaml_read(sql_two),
                     listname_two)
            log.info(f'{form}')
            assert set(form) <= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise
    def assert_elements_larges(self, expected_results, actual_results, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与yamlw文件断言>=,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = self.filelist.yaml_read(expected_results)
            log.info(f'{form}')
            assert set(form) >= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def db_assert_elements_larges(self, expected_results, listname, actual_results,databases, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言>=,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = sql_query_db(databases=databases,sql=self.filelist.yaml_read(expected_results),
                                listname=listname)
            log.info(f'{form}')
            assert set(form) >= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def many_db_assert_elements_larges(self, databases_one, sql_one,listname_one,databases_two,sql_two,listname_two, actual_results, get_attributs='innerText'):
        '''
        databases_one:数据库表名
        sql_one：sql
        listname_one:查询字段名
        databases_two：第二个数据库名
        sql_two：sql
        listname_two：查询字段名   (获取预期结果)
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言>=,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = generatelist(databases_one,
                     self.filelist.yaml_read(sql_one),
                     listname_one,databases_two,
                     self.filelist.yaml_read(sql_two),
                     listname_two)
            log.info(f'{form}')
            assert set(form) >= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def assert_elements_equals(self, expected_results, actual_results, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与yamlw文件断言==,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = self.filelist.yaml_read(expected_results)
            log.info(f'{form}')
            assert set(form) >= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def db_assert_elements_equals(self, expected_results, listname, actual_results, databases,get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言==,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = sql_query_db(databases=databases,sql=self.filelist.yaml_read(expected_results),
                                listname=listname)
            log.info(f'{form}')
            assert set(form) >= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def many_db_assert_elements_equals(self, databases_one, sql_one,listname_one,databases_two,sql_two,listname_two, actual_results,get_attributs='innerText'):
        '''
        databases_one:数据库表名
        sql_one：sql
        listname_one:查询字段名
        databases_two：第二个数据库名
        sql_two：sql
        listname_two：查询字段名   (获取预期结果)
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言==,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = generatelist(databases_one,
                     self.filelist.yaml_read(sql_one),
                     listname_one,databases_two,
                     self.filelist.yaml_read(sql_two),
                     listname_two)
            log.info(f'{form}')
            assert set(form) >= set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def assert_elements_notequals(self, expected_results, actual_results, get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与yamlw文件断言!=,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = self.filelist.yaml_read(expected_results)
            log.info(f'{form}')
            assert set(form) != set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def db_assert_elements_notequals(self, expected_results, listname, actual_results, databases,get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言!=,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = sql_query_db(databases=databases,sql=self.filelist.yaml_read(expected_results),
                                listname=listname)
            log.info(f'{form}')
            assert set(form) != set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def many_db_assert_elements_notequals(self, databases_one, sql_one,listname_one,databases_two,sql_two,listname_two, actual_results,get_attributs='innerText'):
        '''
        databases_one:数据库表名
        sql_one：sql
        listname_one:查询字段名
        databases_two：第二个数据库名
        sql_two：sql
        listname_two：查询字段名   (获取预期结果)
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言!=,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = generatelist(databases_one,
                     self.filelist.yaml_read(sql_one),
                     listname_one,databases_two,
                     self.filelist.yaml_read(sql_two),
                     listname_two)
            log.info(f'{form}')
            assert set(form) != set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def assert_element_equal(self,actual_results,expected_results,choice=None,get_attribute='innerText'):
        '''
        actual_results：实际结果（传入实际结果元素）
        expected_results：预期结果
        页面元素与yaml中配置的预期结果相等
        '''
        global actuals, Expected
        try:
            actual = self.find_element(self.chome[actual_results],choice=choice)
            actuals=actual.get_attribute(get_attribute)
            Expected = self.filelist.yaml_read(expected_results)
            assert actuals ==  Expected
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise
    def assert_element_equal_number(self,actual_results,expected_results,choice=None,get_attribute='innerText'):
        '''
        actual_results：实际结果（传入实际结果元素）
        expected_results：预期结果
        页面元素与yaml中配置的预期结果相等
        '''
        global actuals, Expected
        try:
            actual = self.find_element(self.chome[actual_results],choice=choice)
            actuals=actual.get_attribute(get_attribute)
            Expected = self.filelist.yaml_read(expected_results)
            print(f'1111111111实际{actuals}，预期{Expected}')
            assert actuals ==  Expected
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise


    def db_assert_element_equal(self,actual_results,expected_results,databases,choice=None,listname=None,get_attribute='innerText'):
        '''
        actual_results：实际结果（传入实际结果元素）
        expected_results：预期结果
        页面元素与数据库中查询结果相等
        '''
        try:
            actual = self.find_element(self.chome[actual_results],choice=choice)
            actuals=actual.get_attribute(get_attribute)
            Expected = sql_query_db(databases=databases,
                                    sql=self.filelist.yaml_read(expected_results),
                                    listname=listname)
            assert set(actuals) ==  set(Expected)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise
    def many_db_assert_element_equal(self,actual_results,
                                     databases_one,
                                     sql_one,
                                     listname_one,
                                     databases_two,
                                     sql_two,
                                     listname_two,
                                     choice=None,
                                     default=None,
                                     get_attribute='innerText',):
        '''
        databases_one:数据库表名
        sql_one：sql
        listname_one:查询字段名
        databases_two：第二个数据库名
        sql_two：sql
        listname_two：查询字段名   (获取预期结果)
        expected_results：预期结果
        default:默认值
        页面元素与数据库中查询结果相等
        '''
        try:
            if default != None:
                actual = self.get_element_handling(element=actual_results,choice=choice,get_attribute=get_attribute)
                Expected = generatelist(databases_one,
                         self.filelist.yaml_read(sql_one),
                         listname_one,databases_two,
                         self.filelist.yaml_read(sql_two),
                         listname_two)
                defaults=self.filelist.yaml_read(default)
                result= defaults+Expected
                assert set(actual) ==  set(result)
                log.info(f'实际结果({actual})与预期结果({result})相等，断言成功！')
            else:
                actual = self.get_element_handling(element=actual_results, choice=choice, get_attribute=get_attribute)
                Expected = generatelist(databases_one,
                                        self.filelist.yaml_read(sql_one),
                                        listname_one, databases_two,
                                        self.filelist.yaml_read(sql_two),
                                        listname_two)
                assert set(actual) == set(Expected)
                log.info(f'实际结果({actual})与预期结果({Expected})相等，断言成功！')
        except:
            log.infoo(f'实际结果与预期结果不相等，断言失败！')
            raise False


    def assert_elements_notequals_not_in(self, expected_results, actual_results,get_attributs='innerText'):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:读取多个元素与数据库查询的结果断言!=,特殊处理
        '''
        try:

            form_list = self.elements_detail_special(formheader=actual_results, get_attributs=get_attributs)
            form = self.filelist.yaml_read(expected_results)
            log.info(f'{form}')
            for t in form_list:
                print(t)
                assert t != form
            log.info(f'查询结果字段{form_list}与包含字段{form}一致')
        except:
            log.error('预期结果在实际结果中')
            raise



    def db_assert_s(self,parameter,word,sql):
        ass=SQLAssert(name='IPM', env='test',ini_name='database',values=parameter)
        ass.assert_sql(self.filelist.yaml_read(word),self.filelist.yaml_read(sql))







    def db_text_assert_elements_equal(self,actual_results,expected_results, listname, databases):
        '''
        expected_results:表头预期结果
        actual_results：表头字段获取
        test:文本和sql相对应
        '''
        try:

            form_list = self.filelist.yaml_read(actual_results)
            form = sql_query_db(databases=databases,sql=self.filelist.yaml_read(expected_results),
                                listname=listname)
            log.info(f'{form}')
            assert set(form) == set(form_list)
            log.info(f'实际结果与预期结果匹配成功')
        except:
            log.error(f'实际结果与预期结果匹配失败')
            raise

    def element_not_found(self,locator,choice=None):
        '''
        locator：元素
        test:断言元素不存在
        '''
        assert not len(self.find_element(self.chome[locator],choice=choice))


if __name__ == '__main__':
    pass