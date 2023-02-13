from project.DCR.page_object.PurchaseManagement_CustomerInvoice import CustomerInvoiceQuery,CustomerInvoiceSql
from public.base.basics import Base, random_list
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import pytest
import allure
import random
import logging

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_customer_invoice_fixture(drivers):
    yield
    close = CustomerInvoiceQuery(drivers)
    close.click_close_customer_invoice('Customer Invoice')

@allure.feature("采购管理-客户发票")
class TestCustomerInvoice:
    @allure.story("查询客户发票")
    @allure.title("用户进入CustomerInvoice页面，进行“随机查询”操作")
    @allure.description("用户进入CustomerInvoice页面，进行“随机查询”操作，断言查询结果数据符合查询条件")
    @allure.severity("critical")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_customer_invoice_fixture')
    def test_001_001(self, drivers):
        """DCR 管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开采购管理-打开客户发票页面"""
        user.click_gotomenu("Purchase Management", "Customer Invoice")
        """展开筛选输入框"""
        page = CustomerInvoiceQuery(drivers)
        page.click_button('Unfold')

        """随机查询，对结果进行判断,注意字典的键要和表格的表头一致"""
        query_dic = {'Customer': 'IN401537T',
                     'DN': 'GBR2225082',
                     'Status': 'Finished',
                     'Material ID': '10029521',
                     'SAP Delivery Date': '2022-11-03',
                     'Brand': 'TECNO',
                     'Model': 'CH6h',
                     'Category': 'Mobile',
                     'Market Name': 'CAMON 18',
                     'Customer Region3': 'DEL-UP',
                     'SAP Customer ID': '401537',
                     'IMEI': '351151321771608',
                     'Box': '43012202123266',
                     }
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
        # 进行结果断言

        total = int(page.get_total_content())
        logging.info('the total in test case is %s' % total)
        if total > 0:
            # 进行结果断言
            for i in list_random:
                logging.info('Now the i  is %s' % i)
                if i == 'Customer' or i == 'Box':
                    logging.info('Now this condition %s could not been checked' %i )
                elif i == 'Model' or i == 'Brand' or i == 'Market Name' or i == 'Category' or i == 'Material ID':
                    colum = page.get_table_column(i)
                    logging.info('then the colum is {}'.format(colum))
                    attribute = page.get_table_content(colum)
                    ValueAssert.value_assert_In(query_dic[i], attribute)
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

    @allure.story("导出客户发票")
    @allure.title("用户进入CustomerInvoice页面，进行“查询”操作后，导出页面数据")
    @allure.description("用户进入CustomerInvoice页面，进行“查询”操作后，导出页面数据，断言导出成功")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    @pytest.mark.usefixtures('function_customer_invoice_fixture')
    def test_001_002(self, drivers):
        """DCR 账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开采购管理-打开客户发票页面"""
        user.click_gotomenu("Purchase Management", "Customer Invoice")

        """筛选数据"""
        page = CustomerInvoiceQuery(drivers)
        page.click_button('Unfold')
        page.select_content('DN', 'GBR2225031')
        page.click_button('Search')

        # 进行结果断言
        total = int(page.get_total_content())
        logging.info('the total in test case is %s' % total)
        if total > 0:
            page.click_button('Export')
            complete_value = page.get_download_value()
            ValueAssert.value_assert_equal(complete_value, 100)
        else:
            logging.info('the total is empty')


    @allure.story("导出客户发票IMEIDETAIL详情页面")
    @allure.title("用户进入CustomerInvoice页面，进行“查询”操作后，点击IMEIDETAIL，导出页面数据")
    @allure.description("用户进入CustomerInvoice页面，进行“查询”操作后，点击IMEIDETAIL进入详情页面，导出页面数据，断言导出成功")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    @pytest.mark.usefixtures('function_customer_invoice_fixture')
    def test_001_003(self, drivers):
        """DCR 账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开采购管理-打开客户发票页面"""
        user.click_gotomenu("Purchase Management", "Customer Invoice")

        """筛选数据"""
        page = CustomerInvoiceQuery(drivers)
        page.click_button('Unfold')
        page.select_content('DN', 'GBR2225031')
        page.click_button('Search')

        # 进入详情页
        page.click_detail()
        imei_total = page.get_total_detail()
        if imei_total > 0:
            page.click_detail_export()
            complete_value = page.get_download_detail()
            ValueAssert.value_assert_equal(complete_value, 100)
        else:
            logging.info('the imei detail total is empty')
        page.clos_detail()


    @allure.story("导出客户具体发票")
    @allure.title("用户进入CustomerInvoice页面，进行“查询”操作后，导出页面数据")
    @allure.description("用户进入CustomerInvoice页面，进行“查询”操作后，选中一条数据，导出，断言导出成功")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    @pytest.mark.usefixtures('function_customer_invoice_fixture')
    def test_001_004(self, drivers):
        """DCR 账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开采购管理-打开客户发票页面"""
        user.click_gotomenu("Purchase Management", "Customer Invoice")

        """筛选数据"""
        page = CustomerInvoiceQuery(drivers)
        page.click_button('Unfold')
        page.select_content('DN', 'GBR2225031')
        page.click_button('Search')
        total = int(page.get_total_content())
        ValueAssert.value_assert_equal(total, 1)

        # 选中数据，导出发票，因服务器无法判断下载路径下是否有文件，所以先不断言
        page.click_check_box()
        page.click_button('Export Invoice')


    @allure.story("DN同步，查看发票同步结果")
    @allure.title("用户进入CustomerInvoice页面，进行DN同步页面数据")
    @allure.description("用户进入CustomerInvoice页面，进行DN同步页面数据，检查同步结果")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    @pytest.mark.usefixtures('function_customer_invoice_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开采购管理-打开客户发票页面"""
        user.click_gotomenu("Purchase Management", "Customer Invoice")

        """筛选数据"""
        page = CustomerInvoiceQuery(drivers)
        page.click_button('Unfold')
        page.select_content('DN', 'SDL2380271')
        page.select_content('Status', 'On Transit')
        page.click_button('Search')
        total = int(page.get_total_content())
        ValueAssert.value_assert_equal(total,1)


        """ 执行删除语言，断言total为0 """
        CustomerInvoiceSql(drivers).delete_dn('SDL2380271')
        logging.info('delete DN successfully!')
        page.click_button('Search')
        total = int(page.get_total_content())
        ValueAssert.value_assert_equal(total,0)

        """ 执行DN同步，确认同步数据正确 """
        page.click_button('Sync DN')
        page.input_dn('SDL2380271')
        total = int(page.get_total_content())
        ValueAssert.value_assert_equal(total,1)

        # 进入详情页
        page.click_detail()
        imei_total = page.get_total_detail()
        ValueAssert.value_assert_equal(imei_total, 20)





if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
