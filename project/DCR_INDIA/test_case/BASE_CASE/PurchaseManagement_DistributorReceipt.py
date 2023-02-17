from project.DCR_INDIA.page_object.PurchaseManagement_DistributorReceipt import  DistributorReceiptQuery
from public.base.basics import Base, random_list
from project.DCR_INDIA.page_object.Center_Component import LoginPage
from public.base.basics import Base
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

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_dist_receipt_fixture(drivers):
    yield
    close = DistributorReceiptQuery(drivers)
    close.click_close_distributor_receipt_query()

@allure.feature("采购管理-国包收货")
class TestDistributorReceipt:
    @allure.story("查询国包收货")
    @allure.title("国包收货页面，查询国包收货每个筛选项,进行随机组合")
    @allure.description("国包收货页面，查询国包收货每个筛选项，进行随机组合，断言查询结果数据符合查询条件")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_dist_receipt_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        #user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开报表分析-打开IMEI库存查询页面"""
        user.click_menu("Purchase Management", "Distributor Receipt")
        """查看IMEI库存查询 列表数据加载是否正常"""
        page = DistributorReceiptQuery(drivers)
        page.click_button('Unfold')
        """查询Activation Time，对结果进行判断,注意字典的键要和表格的表头一致"""
        query_dic = {'Customer': 'IN400134I',
                     'Model': 'A661L',
                     'Material ID': '10029424',
                     'DN': 'SGJ2297556',
                     'SAP Delivery Date': '2022-12-29',
                     'SAP Customer ID': '400134',
                     'Brand': 'itel',
                     'Category': 'Mobile',
                     'IMEI': '350803286783066',
                     'Market Name': 'A49',
                     'Customer Region3': 'UP-UK-RAJ',
                     'Delivery Country': 'India',
                     'Status': 'Finished'}
        list_query = []
        for i in query_dic:
            list_query.append(i)
        num = random.randint(3, 8)
        list_random = random_list(list_query, num)
        logging.info('the query condition is %s' % list_random)
        # 开始 对随机查询条件进行输入
        for i in list_random:
            page.select_content(i, query_dic[i])
            logging.info('the query condition is {},values is {}'.format(i, query_dic[i]))
        page.click_button('Search')
        sleep(5)
        total=int(page.get_total_content())
        logging.info('the total in test case is %s'%total)
        if total >0:
            # 进行结果断言
            for i in list_random:
                logging.info('Now the i  is %s' % i)
                if i == 'Customer':
                    logging.info('Now the Customer is %s' % query_dic[i])
                elif i == 'Model' or i == 'Brand' or i == 'Market Name' or i == 'Category':
                    colum = page.get_table_column(i)
                    logging.info('then the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    ValueAssert.value_assert_In(query_dic[i], attribute)
                elif i == 'Material ID':
                    page.click_detail()
                    colum = page.get_table_column(i)
                    logging.info('this the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    ValueAssert.value_assert_equal(attribute, query_dic[i])
                    page.clos_detail()
                elif i == 'IMEI':
                    page.click_detail()
                    imei_total = page.get_total_detail()
                    colum = page.get_table_column(i)
                    logging.info('this imei colum is {}'.format(colum))
                    attribute_list = []
                    if imei_total > 0:
                        for j in range(imei_total):
                            m = j + 1
                            attribute_list.append(page.get_table_detail(m, colum))
                    ValueAssert.value_assert_In(query_dic[i], attribute_list)
                    page.clos_detail()
                elif i == 'SAP Delivery Date':
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


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
