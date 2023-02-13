from project.DCR.page_object.PurchaseManagement_DistributorPurchase import DistributorPurchaseQuery
from public.base.basics import Base, random_list
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert
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

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_distributor_purchase_fixture(drivers):
    yield
    close = DistributorPurchaseQuery(drivers)
    close.click_close_distributor_purchase('Distributor Purchase')


@allure.feature("采购管理-国包采购") # 模块名称
class TestDistributorPurchase:
    @allure.story("查询国包采购") # 场景名称
    @allure.title("用户进入国包采购页面，进行“随机查询”操作")  # 用例名称
    @allure.description("用户进入国包采购页面，进行“随机查询”操作，断言查询结果数据符合查询条件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    @pytest.mark.usefixtures('function_distributor_purchase_fixture')
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开采购管理-打开客户发票页面"""
        user.click_gotomenu("Purchase Management", "Distributor Purchase")

        """展开筛选输入框"""
        page = DistributorPurchaseQuery(drivers)
        page.click_button('Unfold')

        """随机查询，对结果进行判断,注意字典的键要和表格的表头一致"""
        query_dic = {'Customer ID': 'BD404060',
                     'Status': 'Confirmed',
                     'Order ID': 'DP2212140001',
                     'Order Date': '2022-12-14',
                     'Brand': 'Infinix',
                     'Model': 'X652A'
                     }
        list_query = []
        for i in query_dic:
            list_query.append(i)
        num = random.randint(2, 6)
        list_random = random_list(list_query, num)
        logging.info('the query condition is %s' % list_random)
        # 开始 对随机查询条件进行输入
        for i in list_random:
            page.select_content(i, query_dic[i])
            logging.info('the query condition is {},values is {}'.format(i, query_dic[i]))
        page.click_button('Search')
        # 进行结果断言

        total = int(page.get_total_content())
        logging.info('the total in test case is %s' % total)
        if total > 0:
            # 进行结果断言
            for i in list_random:
                logging.info('Now the i  is %s' % i)
                if i == 'Model' or i == 'Brand':
                    colum = page.get_table_column(i)
                    logging.info('then the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    ValueAssert.value_assert_In(query_dic[i], attribute)
                elif i == 'Order Date':
                    colum = page.get_table_column(i)
                    logging.info('that the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    ValueAssert.value_assert_date_in(attribute, query_dic[i], query_dic[i])
                else:
                    colum = page.get_table_column(i)
                    logging.info('finally the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    ValueAssert.value_assert_equal(query_dic[i], attribute)
        else:
            logging.info('the total is empty')

    @allure.story("查询国包采购")  # 场景名称
    @allure.title("用户进入国包采购页面，进行“导出”操作")  # 用例名称
    @allure.description("用户进入国包采购页面，进行“查询”操作后，断言查询结果能正常导出")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_distributor_purchase_fixture')
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开采购管理-打开客户发票页面"""
        user.click_gotomenu("Purchase Management", "Distributor Purchase")

        """展开筛选输入框"""
        page = DistributorPurchaseQuery(drivers)
        page.click_button('Unfold')

        page.select_content('Order Date', '2022-07-25')
        page.click_button('Search')
        # 进行结果断言
        total = int(page.get_total_content())
        if total>0:
            page.click_button('Export')

        """进入导出记录界面进行断言"""
        #Center_Component的LoginPage类，集成了Export Record界面的操作方法
        user.click_gotomenu("Basic Data Management", "Export Record")
        user.input_task_name('Distributor Purchase')
        today=Base(drivers).get_datetime_today()
        user.export_record_create_start_date(today)
        user.click_search()
        attribute = user.assert_exist_download()
        ValueAssert.value_assert_equal(attribute, True)


    @allure.story("查询国包采购")  # 场景名称
    @allure.title("用户进入国包采购页面，进行“新增采购”操作")  # 用例名称
    @allure.description("用户进入国包采购页面，进行“新增采购”操作后，断言新增成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_distributor_purchase_fixture')
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开采购管理-打开客户发票页面"""
        user.click_gotomenu("Purchase Management", "Distributor Purchase")

        """点击新增按钮"""
        page = DistributorPurchaseQuery(drivers)
        page.click_button('Add')

        #新增页面
        today = Base(drivers).get_datetime_today()
        delivery_date = Base(drivers).get_last_day(-10)
        page.add_distributor_purchase('Customer', 'BD404060')
        page.add_distributor_purchase('date', delivery_date)
        page.add_distributor_purchase('Brand','TECNO')
        page.add_distributor_purchase('product', 'F3 16+1 BORDEAUX RED')
        page.add_distributor_purchase('quantity', 1)
        page.add_submit()

        """对新增结果进行断言"""
        page.click_button('Unfold')
        page.select_content('Customer ID','BD404060')
        page.select_content('Brand','TECNO')
        page.select_content('Order Date',today)
        page.click_button('Search')
        total = int(page.get_total_content())
        ValueAssert.value_assert_over(total,1)
        colum = page.get_table_column('Status')
        logging.info('that the colum is {}'.format(colum))
        attribute = page.get_table_content(colum)
        ValueAssert.value_assert_equal(attribute, 'Pending')

        """进行确认或者取消操作，结果断言"""
        #Center_Component的LoginPage类，集成了Export Record界面的操作方法
        page.click_check_box()
        status_list=['Confirm','Cancel']
        select_num =random.randint(0,1)
        button=status_list[select_num]
        page.click_action_button(button)       #随机选择确定或取消按钮
        page.click_button('Search')
        colum_action = page.get_table_column('Status')
        attribute = page.get_table_content(colum_action)
        if button == 'Confirm':
            ValueAssert.value_assert_In(attribute, 'Confirmed')
        else:
            ValueAssert.value_assert_In(attribute, 'Canceled')

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
