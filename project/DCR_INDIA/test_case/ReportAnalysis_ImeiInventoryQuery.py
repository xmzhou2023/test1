from project.DCR_INDIA.page_object.ReportAnalysis_ImeiInventoryQuery import ImeiInventoryQuery
import logging
from project.DCR_INDIA.page_object.Center_Component import LoginPage
from public.base.basics import Base,random_list
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
import datetime
import pytest
import allure
import random
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_imei_inventory_query_fixture(drivers):
    yield
    close = ImeiInventoryQuery(drivers)
    close.click_close_imei_inventory_query()

@allure.feature("报表分析-IMEI库存查询")
class TestImeiInventoryQuery:
    @allure.story("查询IMEI库存")
    @allure.title("IMEI库存查询页面，查询IMEI库存每个筛选项,进行随机组合")
    @allure.description("IMEI库存页面，查询IMEI库存每个筛选项，进行随机组合，断言查询结果数据符合查询条件")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_imei_inventory_query_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        """打开报表分析-打开IMEI库存查询页面"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        """查看IMEI库存查询 列表数据加载是否正常"""
        page = ImeiInventoryQuery(drivers)
        page.click_button('Unfold')
        """查询Activation Time，对结果进行判断,注意字典的键要和表格的表头一致"""
        query_dic={'Receive Date':'2022-11-08',
                   'Box ID':'43012210040316',
                   'Customer ID':'IN400747I',
                   'Customer Type':'Distributor',
                   'Material ID':'10034565',
                   'Warehouse ID':'WIN400747I',
                   'Warehouse Type':'Main Warehouse',
                   'SAP Customer ID':'400747',
                   'IMEI/SN':'357179273059668',
                   'Sales Region 3':'GUJ-MH',
                   'Activated Or Not':'Yes',
                   'Brand':'itel',
                   'Model':'P110N',
                   'Market Name':'P110N',
                   'Series':'Power',
                   'Category':'Mobile',
                   'Dealer Category':'10',
                   'Activation Date':'2022-12-01'}
        list_query = []
        for i in query_dic:
            list_query.append(i)
        num=random.randint(3,8)
        list_random=random_list(list_query,num)
        logging.info('the query condition is %s'%list_random)
        #开始 对随机查询条件进行输入
        for i in list_random:
            page.select_content(i,query_dic[i])
            logging.info('the query condition is {},values is {}'.format(i,query_dic[i]))
        page.click_button('Search')
        sleep(5)
        #进行结果断言
        for i in list_random:
            colum = page.get_table_column(i)
            logging.info('the colum is {}'.format(colum))
            attribute = page.get_table_content(colum)
            if i == 'Receive Date':
                ValueAssert.value_assert_date_in(attribute,query_dic[i],query_dic[i])
            else:
                ValueAssert.value_assert_equal(attribute, query_dic[i])

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
