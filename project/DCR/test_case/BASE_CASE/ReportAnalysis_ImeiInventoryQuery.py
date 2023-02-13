from project.DCR.page_object.ReportAnalysis_ImeiInventoryQuery import ImeiInventoryQuery
import logging
from project.DCR.page_object.Center_Component import LoginPage
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
    @allure.title("IMEI库存查询页面，查询IMEI库存每个筛选项")
    @allure.description("IMEI库存页面，查询IMEI库存每个筛选项，断言查询结果数据符合查询条件")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_imei_inventory_query_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开报表分析-打开IMEI库存查询页面"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")

        """查看IMEI库存查询 列表数据加载是否正常"""
        page = ImeiInventoryQuery(drivers)
        page.click_button('Unfold')

        """1查询收货日期，对结果进行判断"""
        page.select_content('Receive Date','2022-12-10')
        page.click_button('Search')
        colum = page.get_table_column('Receive Date')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_date_in(attribute,'2022-12-10','2022-12-10')
        page.click_button('Reset')

        """2查询box id，对结果进行判断"""
        page.select_content('Box ID', '43012211060271')
        page.click_button('Search')
        colum = page.get_table_column('Box ID')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, '43012211060271')
        page.click_button('Reset')

        """3查询Customer，对结果进行判断"""
        page.select_content('Customer ID', 'CN20058')
        page.click_button('Search')
        colum = page.get_table_column('Customer ID')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'CN20058')
        page.click_button('Reset')

        """4查询Customer Type，对结果进行判断"""
        page.select_content('Customer Type', 'Retailer')
        page.click_button('Search')
        colum = page.get_table_column('Customer Type')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'Retailer')
        page.click_button('Reset')

        """5查询Material ID，对结果进行判断"""
        page.select_content('Material ID', '10026678')
        page.click_button('Search')
        colum = page.get_table_column('Material ID')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, '10026678')
        page.click_button('Reset')

        """6查询Warehouse，对结果进行判断"""
        page.select_content('Warehouse ID', 'WNG100055')
        page.click_button('Search')
        colum = page.get_table_column('Warehouse ID')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'WNG100055')
        page.click_button('Reset')

        """7查询Warehouse Type，对结果进行判断"""
        page.select_content('Warehouse Type', 'Branch Warehouse')
        page.click_button('Search')
        colum = page.get_table_column('Warehouse Type')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'Branch Warehouse')
        page.click_button('Reset')

        """8查询SAP Customer ID，对结果进行判断"""
        page.select_content('SAP Customer ID', '100742')
        page.click_button('Search')
        colum = page.get_table_column('SAP Customer ID')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, '100742')
        page.click_button('Reset')

        """9查询IMEI，对结果进行判断"""
        page.select_content('IMEI/SN', '351594528651521')
        page.click_button('Search')
        colum = page.get_table_column('IMEI/SN')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, '351594528651521')
        page.click_button('Reset')

        """10查询Sales Region，对结果进行判断"""
        page.select_content('Sales Region 3', 'Central2-PK')
        page.click_button('Search')
        colum = page.get_table_column('Sales Region 3')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'Central2-PK')
        page.click_button('Reset')

        """11查询Activated Or Not，对结果进行判断"""
        page.select_content('Activated Or Not', 'Yes')
        page.click_button('Search')
        colum = page.get_table_column('Activated Or Not')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'Yes')
        page.click_button('Reset')

        """12查询Brand，对结果进行判断"""
        page.select_content('Brand', 'itel')
        page.click_box()
        page.click_button('Search')
        colum = page.get_table_column('Brand')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'itel')
        page.click_button('Reset')

        """13查询Model，对结果进行判断"""
        page.select_content('Model', 'it2163S')
        page.click_button('Search')
        colum = page.get_table_column('Model')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'it2163S')
        page.click_button('Reset')

        """14查询Market Name，对结果进行判断"""
        page.select_content('Market Name', 'Vision 3')
        page.click_button('Search')
        colum = page.get_table_column('Market Name')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'Vision 3')
        page.click_button('Reset')

        """15查询Series，对结果进行判断"""
        page.select_content('Series', 'HOT')
        page.click_box()
        page.click_button('Search')
        colum = page.get_table_column('Series')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'HOT')
        page.click_button('Reset')

        """16查询Category，对结果进行判断"""
        page.select_content('Category', 'TV')
        page.click_button('Search')
        sleep(3)
        colum = page.get_table_column('Category')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'TV')
        page.click_button('Reset')

        """17查询Dealer Category，对结果进行判断"""
        page.select_content('Dealer Category', 'wka')
        page.click_button('Search')
        sleep(4)
        colum = page.get_table_column('Dealer Category')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'wka')
        page.click_button('Reset')

        """18查询Activation Time，对结果进行判断"""
        page.select_content('Activation Date','2022-12-10')
        page.click_box()
        page.click_button('Search')
        colum = page.get_table_column('Activation Date')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute,'2022-12-10')
        page.click_button('Reset')


    @allure.story("查询IMEI库存")
    @allure.title("IMEI库存查询页面，查询IMEI库存每个筛选项,进行随机组合")
    @allure.description("IMEI库存页面，查询IMEI库存每个筛选项，进行随机组合，断言查询结果数据符合查询条件")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_imei_inventory_query_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开报表分析-打开IMEI库存查询页面"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        """查看IMEI库存查询 列表数据加载是否正常"""
        page = ImeiInventoryQuery(drivers)
        page.click_button('Unfold')

        """查询Activation Time，对结果进行判断,注意字典的键要和表格的表头一致"""
        query_dic={'Receive Date':'2022-07-28',
                   'Box ID':'43012206172264',
                   'Customer ID':'PH400515',
                   'Customer Type':'Distributor',
                   'Material ID':'10030597',
                   'Warehouse ID':'WPH40051501',
                   'Warehouse Type':'Main Warehouse',
                   'SAP Customer ID':'400515',
                   'IMEI/SN':'357498771856148',
                   'Sales Region 3':'Central2-PK',
                   'Activated Or Not':'Yes',
                   'Brand':'TECNO',
                   'Model':'KG5h',
                   'Market Name':'SPARK Go 2022',
                   'Series':'SPARK',
                   'Category':'Mobile',
                   'Dealer Category':'retail KA',
                   'Activation Date':'2022-07-30'}
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


    @allure.story("查询IMEI库存")
    @allure.title("IMEI库存查询页面，查询IMEI库存每个筛选项,进行随机组合")
    @allure.description("IMEI库存页面，查询IMEI库存每个筛选项，进行随机组合，断言查询结果数据符合查询条件")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_imei_inventory_query_fixture')
    def test_001_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开报表分析-打开IMEI库存查询页面"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")

        """查看IMEI库存查询 列表数据加载是否正常"""
        page = ImeiInventoryQuery(drivers)
        page.click_button('Unfold')

        """12查询Brand，对结果进行判断"""
        page.select_content('Brand', 'itel')
        page.click_box()
        page.click_button('Search')
        colum = page.get_table_column('Brand')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'itel')
        page.click_button('Reset')

        """13查询Model，对结果进行判断"""
        page.select_content('Model', 'it2163S')
        page.click_button('Search')
        sleep(3)
        colum = page.get_table_column('Model')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'it2163S')
        page.click_button('Reset')

        """14查询Market Name，对结果进行判断"""
        page.select_content('Market Name', 'Vision 3')
        page.click_button('Search')
        sleep(2)
        colum = page.get_table_column('Market Name')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'Vision 3')
        page.click_button('Reset')

        """15查询Series，对结果进行判断"""
        page.select_content('Series', 'HOT')
        page.click_box()
        page.click_button('Search')
        sleep(2)
        colum = page.get_table_column('Series')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'HOT')
        page.click_button('Reset')

        """16查询Category，对结果进行判断"""
        page.select_content('Category', 'TV')
        page.click_button('Search')
        sleep(3)
        colum = page.get_table_column('Category')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'TV')
        page.click_button('Reset')

        """17查询Dealer Category，对结果进行判断"""
        page.select_content('Dealer Category', 'wka')
        page.click_button('Search')
        sleep(4)
        colum = page.get_table_column('Dealer Category')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'wka')
        page.click_button('Reset')

        """18查询Activation Time，对结果进行判断"""
        page.select_content('Activation Date','2022-12-10')
        page.click_box()
        page.click_button('Search')
        colum = page.get_table_column('Activation Date')
        logging.info('the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute,'2022-12-10')
        page.click_button('Reset')



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
