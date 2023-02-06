from project.DCR.page_object.PurchaseManagement_DistributorReceipt import DitributorReceiptPage, DistributorReceiptQuery
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base, random_list
from project.DCR.page_object.PurchaseManagement_DistributorReceipt import DitributorReceiptPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import pytest
import allure
import random
import logging

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_distributor_receipt_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()


#国包快速收货待修改用例
@allure.feature("采购管理-国包收货")
class TestDistributorReceipt:
    @allure.story("国包快速收货")
    @allure.title("国包收货页面，进行快速收货操作 ")
    @allure.description("国包收货页面，进行快速收货操作 EC402067")
    @allure.severity("critical")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_distributor_receipt_fixture')
    def test_001_001(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "EC402067", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Purchase Management", "Distributor Receipt")
        """调用国包快速收货用例，并断言收货是否成功"""
        receipt = DitributorReceiptPage(drivers)
        list_dn = receipt.get_list_dn_text()
        list_quantity = receipt.get_list_quantity_text()
        receipt.click_unfold()
        receipt.input_dn(list_dn)
        receipt.click_search()
        receipt.click_first_chekbox()
        receipt.click_quick_receive()
        dialog_dn = receipt.get_dialog_text_dn()
        dialog_quantity = receipt.get_dialog_text_quantity()
        """ 增加断言，验证列表获取的DN与快速收货对话框的DN是否一致 """
        ValueAssert.value_assert_equal(list_dn, dialog_dn)
        """断言列表获取的quantity与快速收货对话框的quantity是否一致"""
        ValueAssert.value_assert_equal(list_quantity, dialog_quantity)
        receipt.click_quick_receive_submit()
        """断言国包收货成功，状态已更新，列表显示:No Data """
        success = receipt.get_success_text()
        ValueAssert.value_assert_equal(success, "Set Up Successfully")
        receipt.click_reset()


@allure.feature("采购管理-国包收货")
class TestQueryIMEIDetail:
    @allure.story("查询IMEI详情")
    @allure.title("国包收货页面，筛选DN记录，查看IMEI详情信息，并导出详情信息")
    @allure.description("国包收货页面，查看IMEI详情信息是否与筛选的DN一致，并导出详情信息")
    @allure.severity("critical")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_distributor_receipt_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Purchase Management", "Distributor Receipt")
        view_imei = DitributorReceiptPage(drivers)
        """获取当天日期"""
        today = Base(drivers).get_datetime_today()

        list_dn = view_imei.get_list_dn_text()
        list_total_quantity = view_imei.get_list_quantity_text()
        logging.info("打印Distributor Receipt列表Total Quantity字段的总数量：{}".format(list_total_quantity))
        """根据DN条件进行筛选"""
        view_imei.click_unfold()
        view_imei.input_dn(list_dn)
        view_imei.click_search()
        """点击详情按钮"""
        view_imei.click_imei_detail()
        imei_detail_dn = view_imei.get_text_imei_detail_DN()
        get_detail_total = view_imei.text_imei_detail_total()
        logging.info("打印Distributor Receipt详情页的Total总分页数：{}".format(get_detail_total))
        """ 断言列表获取的DN，与打开IMEI Detail详情页的DN比较一致 """
        ValueAssert.value_assert_In(list_dn, imei_detail_dn)
        """ 断言列表获取的quantity总条数，与打开IMEI Detail详情页的Total总条数比较一致 """

        ValueAssert.value_assert_equal(list_total_quantity, get_detail_total)
        """点击IMEI Detail详情页的导出按按， 断言导出进度条是否100%"""
        logging.info('the total in test case is %s' % get_detail_total)
        if int(get_detail_total) > 0:
            view_imei.click_distri_imei_detail_export()
            sleep(4)
            complete_value = view_imei.get_download_value()
            ValueAssert.value_assert_equal(complete_value, 100)
        else:
            logging.info('the total is empty')
        """关闭IMEI Detail详情页面"""
        view_imei.click_imei_detail_close()


    @allure.story("查询国包收货")
    @allure.title("国包收货页面，筛选DN记录，查询国包收货每个筛选项,进行随机组合筛选")
    @allure.description("国包收货页面，查询国包每个筛选项，进行随机组合，断言查询结果数据符合查询条件")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_distributor_receipt_fixture')
    def test_002_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开报表分析-打开IMEI库存查询页面"""
        user.click_gotomenu("Purchase Management", "Distributor Receipt")
        """查看IMEI库存查询 列表数据加载是否正常"""
        page = DistributorReceiptQuery(drivers)
        page.click_button('Unfold')
        """查询Activation Time，对结果进行判断,注意字典的键要和表格的表头一致"""
        query_dic = {'Customer': 'IN401157',
                     'Model': 'KG5h',
                     'Material ID': '10030598',
                     'DN': 'GRJ2287789',
                     'SAP Delivery Date': '2022-11-26',
                     'SAP Customer ID': '401157',
                     'Brand': 'TECNO',
                     'Category': 'Mobile',
                     'IMEI': '351364951010680',
                     'Market Name': 'SPARK Go 2022',
                     'Customer Region3': 'BIH-JH',
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
        # 进行结果断言

        total = int(page.get_total_content())
        logging.info('the total in test case is %s' % total)
        if total > 0:
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
    pytest.main(['PurchaseManagement_DistributorReceipt.py'])
