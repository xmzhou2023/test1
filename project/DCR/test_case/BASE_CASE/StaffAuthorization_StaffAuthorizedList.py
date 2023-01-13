from project.DCR.page_object.StaffAuthorization_StaffAuthorizedList import StaffAuthorizedList
from public.base.basics import Base, random_list
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import pytest
import allure
import random
import logging

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@pytest.fixture(scope='function')
def function_staff_authorized_list_fixture(drivers):
    yield
    close = StaffAuthorizedList(drivers)
    close.click_close_menu('Staff Authorized List')

@allure.feature("员工授权-人员授权列表")
class TestQueryStaffAuthorizedList:
    @allure.story("查询员工授权列表")
    @allure.title("员工授权列表页面，查询员工授权每个筛选项,进行随机组合")
    @allure.description("员工授权列表页面，查询员工授权列表每个筛选项，进行随机组合，断言查询结果数据符合查询条件")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_staff_authorized_list_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)

        """打开报表分析-打开IMEI库存查询页面"""
        user.click_gotomenu("Staff & Authorization", "Staff Authorized List")

        """查看IMEI库存查询 列表数据加载是否正常"""
        page = StaffAuthorizedList(drivers)
        page.click_button('Unfold')

        """查询Activation Time，对结果进行判断,注意字典的键要和表格的表头一致"""
        query_dic = {'User ID': 'zhao11',
                     'Brand': 'TECNO',
                     'Position': 'Regional Sales Manager',
                     'Country': 'Bangladesh',
                     'Role': 'RSM',
                     'Customer': 'Yes',
                     'Warehouse': 'Yes',
                     'Staff Type': 'Transsion Staff',
                     'Shop': 'Yes',
                     'Authorized Sales Region': 'Yes',
                     'Inactive Day(No Login)': '0',
                     'Last Login Date': '2023-01-11'}
        list_query = []
        for i in query_dic:
            list_query.append(i)
        num = random.randint(10, 11)
        list_random = random_list(list_query, num)
        logging.info('the query condition is %s' % list_random)
        # 开始 对随机查询条件进行输入
        for i in list_random:
            page.select_content(i, query_dic[i])
            logging.info('the query condition is {},values is {}'.format(i, query_dic[i]))
        page.click_button('Search')
        sleep(5)
        # 进行结果断言

        total = int(page.get_total_content())
        logging.info('the total in test case is %s' % total)
        if total > 0:
            # 进行结果断言
            for i in list_random:
                logging.info('Now the i  is %s' % i)
                if i == 'Customer' or i == 'Warehouse' or i == 'Shop':
                    colum = page.get_table_column(i)
                    logging.info('then the colum is {}'.format(colum))
                    #带有数值的定位和其他不带数据的定位不一样
                    attribute = int(page.get_table_column_number(colum))
                    ValueAssert.value_assert_Notequal(attribute, 0)
                    page.click_table_column_number(colum)
                    pagetitle=page.get_page_title()
                    logging.info('the title is %s'%pagetitle)
                    ValueAssert.value_assert_equal(pagetitle, 'User Authorization')
                    page.click_close_menu(pagetitle)
                elif i == 'Role':
                    colum = page.get_table_column(i)
                    logging.info('then the colum is {}'.format(colum))
                    #Role字段定位和其他不一样，单独列举
                    attribute = page.get_text_content(colum)
                    ValueAssert.value_assert_equal(attribute, query_dic[i])
                    page.click_table_text(colum)
                    pagetitle=page.get_pop_windows_content()
                    ValueAssert.value_assert_equal(pagetitle, query_dic[i])
                    page.click_close_role()
                elif i == 'Authorized Sales Region':
                    colum = page.get_table_column(i)
                    logging.info('then the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    ValueAssert.value_assert_equal(attribute, query_dic[i])
                    page.click_table_text(colum)
                    pagetitle=page.get_page_title()
                    ValueAssert.value_assert_equal(pagetitle, 'User Authorization')
                    page.click_close_menu(pagetitle)
                elif i == 'Last Login Date':
                    colum = page.get_table_column(i)
                    logging.info('that the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    ValueAssert.value_assert_date_in(attribute, query_dic[i], query_dic[i])
                elif i == 'Inactive Day(No Login)':
                    colum = page.get_table_column(i)
                    logging.info('that the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    ValueAssert.value_assert_date_in(attribute, query_dic[i], query_dic[i])
                else:
                    colum = page.get_table_column(i)
                    logging.info('finally the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    logging.info('the attribute is %s'%attribute)
        else:
            logging.info('the total is empty')

    @allure.story("导出员工授权列表")
    @allure.title("员工授权列表页面，导出页面数据")
    @allure.description("员工授权列表页面，查询员工授权列表的筛选项，导出数据")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_staff_authorized_list_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)

        """打开报表分析-打开IMEI库存查询页面"""
        user.click_gotomenu("Staff & Authorization", "Staff Authorized List")

        """查看IMEI库存查询 列表数据加载是否正常"""
        page = StaffAuthorizedList(drivers)
        page.click_button('Unfold')

        page.select_content('Role', 'RSM')
        page.click_button('Search')
        total = int(page.get_total_content())
        logging.info('the total in test case is %s' % total)
        if total > 0:
            page.click_button('Export')
            sleep(5)
            complete_value =page.get_download_value()
            ValueAssert.value_assert_equal(complete_value, 100)
        else:
            logging.info('the total is empty')

    @allure.story("员工授权列表点击跳转")
    @allure.title("员工授权列表页面，点击customer等进行跳转查看")
    @allure.description("员工授权列表页面，点击customer等进行跳转查看")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_staff_authorized_list_fixture')
    def test_001_003(self, drivers):
        user = LoginPage(drivers)

        """打开报表分析-打开IMEI库存查询页面"""
        user.click_gotomenu("Staff & Authorization", "Staff Authorized List")

        """查看IMEI库存查询 列表数据加载是否正常"""
        page = StaffAuthorizedList(drivers)
        page.click_button('Unfold')

        page.select_content('User ID', 'TK555555')
        page.select_content('Inactive Day(No Login)', '0')
        page.click_button('Search')
        total = int(page.get_total_content())
        logging.info('the total in test case is %s' % total)
        if total > 0:
            jump_list=['Customer','Warehouse','Shop','Authorized Sales Region','Role']
            for i in jump_list:
                logging.info('Now the i  is %s' % i)
                if i == 'Customer' or i == 'Warehouse' or i == 'Shop':
                    colum = page.get_table_column(i)
                    logging.info('then the colum is {}'.format(colum))
                    #带有数值的定位和其他不带数据的定位不一样
                    attribute = int(page.get_table_column_number(colum))
                    ValueAssert.value_assert_Notequal(attribute, 0)
                    page.click_table_column_number(colum)
                    page_title=page.get_page_title()
                    logging.info('the title is %s'%page_title)
                    ValueAssert.value_assert_equal(page_title, 'User Authorization')
                    total_value=int(page.get_total_jump())
                    ValueAssert.value_assert_equal(total_value, attribute)
                    page.click_close_menu(page_title)
                elif i == 'Role':
                    colum = page.get_table_column(i)
                    logging.info('then the colum is {}'.format(colum))
                    #Role字段定位和其他不一样，单独列举
                    attribute = page.get_text_content(colum)
                    ValueAssert.value_assert_equal(attribute, 'Transsion Administrator')
                    page.click_table_text(colum)
                    page_title=page.get_pop_windows_content()
                    ValueAssert.value_assert_equal(page_title, 'Transsion Administrator')
                    page.click_close_role()
                elif i == 'Authorized Sales Region':
                    colum = page.get_table_column(i)
                    logging.info('then the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    ValueAssert.value_assert_equal(attribute, 'Yes')
                    page.click_table_text(colum)
                    page_title=page.get_page_title()
                    ValueAssert.value_assert_equal(page_title, 'User Authorization')
                    page.click_close_menu(page_title)
        else:
            logging.info('the total is empty')

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
