from project.DCR.page_object.PurchaseManagement_DistributorReceipt import DitributorReceiptPage, DistributorReceiptQuery
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base, random_list
from project.DCR.page_object.PurchaseManagement_DistributorReceipt import DitributorReceiptPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert,DomAssert
from libs.common.time_ui import sleep
import pytest
import allure
import random
import logging

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_dist_receipt_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("采购管理-国包收货")
class TestDistributorReceipt:
    @allure.story("国包收货")
    @allure.title("国包收货页面，进行一键收货操作 ")
    @allure.description("国包收货页面，进行一键收货操作 ")
    @allure.severity("critical")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_dist_receipt_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "xiongbo92", "dcr123456")
        user.click_gotomenu("Purchase Management", "Distributor Receipt")
        """调用国包快速收货用例，并断言收货是否成功"""
        receipt = DitributorReceiptPage(drivers)
        query = DistributorReceiptQuery(drivers)
        """根据dn与sap customer id 条件筛选待收货的dn数据"""
        receipt.click_unfold()
        receipt.input_sap_customer_id_query('100055')
        receipt.input_dn_query('8100053878')
        """点击查询按钮"""
        receipt.click_search_reset('Search')
        """断言 筛选的数据与查询条件是否一致"""
        receipt.assert_query_result('DN', '8100053878')
        receipt.assert_query_result('SAP Customer ID', '100055')
        list_total = query.get_total_content()
        ValueAssert.value_assert_equal('1', list_total)
        """获取列表Total Quantity字段文本内容"""
        list_total_quantity = receipt.get_list_quantity_text()
        """先勾选复选框，然后点击快速收货功能"""
        receipt.click_first_checkbox()
        receipt.click_quick_receive_button()
        dn = receipt.get_quick_receive_dn()
        quantity = receipt.get_quick_receive_quantity()
        receipt.click_quick_receive_submit()
        ValueAssert.value_assert_equal('8100053878', dn)
        ValueAssert.value_assert_equal(list_total_quantity, quantity)
        """断言国包收货提示成功，状态已更新 """
        DomAssert(drivers).assert_att('Set Up Successfully')
        receipt.click_search_reset('Search')
        list_total = query.get_total_content()
        ValueAssert.value_assert_equal('0', list_total)
        """删除数据库已收货的DN数据，恢复DN数据状态"""
        receipt.delete_dist_receipt_dn_data('8100053878')
        """查询国包收货列表, 该DN数据是否复原能查询到"""
        receipt.click_search_reset('Search')
        receipt.assert_query_result('DN', '8100053878')
        receipt.assert_query_result('SAP Customer ID', '100055')


    @allure.story("国包收货")
    @allure.title("国包收货页面，创建收货单扫码IMEI进行收货入库操作")
    @allure.description("国包收货页面，创建收货单扫码IMEI进行收货入库操作")
    @allure.severity("critical")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_dist_receipt_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "NG100055", "dcr123456")
        user.click_gotomenu("Purchase Management", "Distributor Receipt")
        """调用国包快速收货用例，并断言收货是否成功"""
        scan_imei_receipt = DitributorReceiptPage(drivers)
        query = DistributorReceiptQuery(drivers)
        """根据IMEI与sap customer id 条件筛选待收货的dn数据"""
        scan_imei_receipt.click_unfold()
        scan_imei_receipt.input_sap_customer_id_query('100055')
        scan_imei_receipt.input_dn_query('8100150180')
        scan_imei_receipt.input_imei_query('352153455475088')
        """点击查询按钮"""
        scan_imei_receipt.click_search_reset('Search')
        """获取列表是否查询到数据"""
        list_total = query.get_total_content()
        if int(list_total) == 1:
            """如果列表有筛选的DN与IMEI数据，则点击扫码IMEI收货功能"""
            scan_imei_receipt.click_stock_in_by_scan_button()
            """打开创建Inbound Order，输入IMEI进行扫码收货操作"""
            scan_imei_receipt.create_inbound_order_imei2('352153455475088')
            DomAssert(drivers).assert_att('INBOUND_SUCCESS')

            """删除数据库已收货的IMEI数据，恢复DN下已收货的IMEI状态"""
            scan_imei_receipt.delete_dist_receipt_imei_data('352153455475088')
            """点击查询按钮"""
            scan_imei_receipt.click_search_reset('Search')
            """断言判断DN下的IMEI状态恢复正常，能查询到满足DN,IMEI条件的数据"""
            list_total = query.get_total_content()
            ValueAssert.value_assert_equal('1', list_total)
        else:
            logging.info("该IMEI数据已扫码入库")


    @allure.story("国包收货")
    @allure.title("国包收货页面，创建收货单扫码Box ID进行收货操作 ")
    @allure.description("国包收货页面，创建收货单扫码Box ID进行收货操作 ")
    @allure.severity("critical")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_dist_receipt_fixture')
    def test_001_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "NG100055", "dcr123456")
        user.click_gotomenu("Purchase Management", "Distributor Receipt")
        """调用国包快速收货用例，并断言收货是否成功"""
        scan_imei_receipt = DitributorReceiptPage(drivers)
        query = DistributorReceiptQuery(drivers)
        """根据Box ID与sap customer id 条件筛选待收货的dn数据"""
        scan_imei_receipt.click_unfold()
        scan_imei_receipt.input_sap_customer_id_query('100055')
        scan_imei_receipt.input_dn_query('8100146459')
        scan_imei_receipt.input_box_id_query('81012108100173')
        """点击查询按钮"""
        scan_imei_receipt.click_search_reset('Search')
        """获取列表是否查询到数据"""
        list_total = query.get_total_content()
        if int(list_total) == 1:
            """如果列表有筛选的DN与IMEI数据，则点击扫码IMEI收货功能 NG100055"""
            scan_imei_receipt.click_stock_in_by_scan_button()
            """打开创建Inbound Order，输入Box ID进行扫码收货操作"""
            scan_imei_receipt.create_inbound_order_box_id('81012108100173')
            DomAssert(drivers).assert_att('INBOUND_SUCCESS')

            """删除数据库已收货的IMEI数据，恢复DN下已收货的IMEI状态"""
            scan_imei_receipt.delete_dist_receipt_box_id_data('81012108100173')
            """点击查询按钮"""
            scan_imei_receipt.click_search_reset('Search')
            """断言判断DN下的IMEI状态恢复正常，能查询到满足DN,IMEI条件的数据"""
            list_total = query.get_total_content()
            ValueAssert.value_assert_equal('1', list_total)
        else:
            logging.info("该Box ID数据已扫码入库")


    @allure.story("国包收货")
    @allure.title("国包收货页面，通过DN同步")
    @allure.description("国包收货页面，通过DN同步DN数据")
    @allure.severity("critical")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_dist_receipt_fixture')
    def test_001_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "xiongbo92", "dcr123456")
        user.click_gotomenu("Purchase Management", "Distributor Receipt")
        sync_dn = DitributorReceiptPage(drivers)
        query = DistributorReceiptQuery(drivers)
        """根据dn与sap customer id 条件筛选待收货的dn数据"""
        sync_dn.click_unfold()
        sync_dn.input_sap_customer_id_query('100055')
        sync_dn.input_dn_query('8100150827')
        """点击查询按钮"""
        sync_dn.click_search_reset('Search')
        """获取列表是否查询到数据"""
        list_total = query.get_total_content()
        if int(list_total) == 0:
            """如果列表无DN数据，则点击同步DN功能,输入同步的DN信息"""
            sync_dn.click_more_option_sync_dn()
            """输入不存在的DN信息，弹出提示获取的数据为空"""
            sync_dn.input_sync_dn('111')
            """点击同步DN的提交"""
            sync_dn.click_sync_dn_submit()
            DomAssert(drivers).assert_att('DN:[111]获取的数据为空')
            """输入存在的DN信息，弹出提示：Set Up Successfully"""
            sync_dn.input_sync_dn('8100150827')
            """输入DN后，获取并判断Customer ID、Date、Country输入框是否为disabled禁用状态"""
            sync_dn.click_sync_dn_submit()
            DomAssert(drivers).assert_att('Set Up Successfully')
            """点击查询按钮, 列表是否加载同步的DN数据"""
            sync_dn.click_search_reset('Search')
            sync_dn.assert_query_result('DN', '8100150827')
            sync_dn.assert_query_result('SAP Customer ID', '100055')
            list_total = query.get_total_content()
            ValueAssert.value_assert_equal('1', list_total)

            """筛选出DN信息后，删除数据库已同步的DN数据"""
            sync_dn.delete_dist_sync_dn_date('8100150827')
            """然后点击查询，是否查询不到被删除的DN数据"""
            sync_dn.click_search_reset('Search')
            list_total = query.get_total_content()
            ValueAssert.value_assert_equal('0', list_total)
        elif int(list_total) == 1:
            """若列表筛选有该DN数据，断言筛选的数据与查询条件是否一致"""
            sync_dn.assert_query_result('DN', '8100150827')
            sync_dn.assert_query_result('SAP Customer ID', '100055')
            """筛选出DN信息后，删除数据库已同步的DN数据"""
            sync_dn.delete_dist_sync_dn_date('8100150827')
            """然后点击查询，是否查询不到被删除的DN数据"""
            sync_dn.click_search_reset('Search')
            list_total = query.get_total_content()
            ValueAssert.value_assert_equal('0', list_total)

            """如果列表无DN数据，则点击同步DN功能,输入同步的DN信息"""
            sync_dn.click_more_option_sync_dn()
            """输入存在的DN信息，弹出提示：Set Up Successfully"""
            sync_dn.input_sync_dn('8100150827')
            """输入DN后，获取并判断Customer ID、Date、Country输入框是否为disabled禁用状态"""
            sync_dn.click_sync_dn_submit()
            DomAssert(drivers).assert_att('Set Up Successfully')
            """点击查询按钮, 列表是否加载同步的DN数据"""
            sync_dn.click_search_reset('Search')
            sync_dn.assert_query_result('DN', '8100150827')
            sync_dn.assert_query_result('SAP Customer ID', '100055')
            list_total = query.get_total_content()
            ValueAssert.value_assert_equal('1', list_total)


    @allure.story("国包收货")
    @allure.title("国包收货页面，按每个条件筛选国包收货数据")
    @allure.description("国包收货页面，按每个条件筛选国包收货数据")
    @allure.severity("critical")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_dist_receipt_fixture')
    def test_001_005(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        user.click_gotomenu("Purchase Management", "Distributor Receipt")
        query_dist = DitributorReceiptPage(drivers)
        query = DistributorReceiptQuery(drivers)
        """展开筛选项"""
        query_dist.click_unfold()
        """按 model字段进行筛选"""
        query_dist.input_receipt_model_query('it5026')
        query_dist.click_search_reset('Search')
        query_dist.assert_query_result('Model', 'it5026')
        query_dist.click_search_reset('Reset')
        """按 material id字段进行筛选"""
        query_dist.input_material_id_query('10036421')
        query_dist.click_search_reset('Search')
        query_dist.click_imei_detail()
        query_dist.assert_query_result('Material ID', '10036421')
        query_dist.click_imei_detail_close()
        query_dist.click_search_reset('Reset')
        """按 DN 字段进行筛选"""
        query_dist.input_dn_query('SSE2300409')
        query_dist.click_search_reset('Search')
        query_dist.assert_query_result('DN', 'SSE2300409')
        query_dist.click_search_reset('Reset')
        """按 SAP Delivery Date字段进行筛选"""
        query_dist.input_sap_delivery_date_query('2023-02-06')
        query_dist.click_search_reset('Search')
        query_dist.assert_query_result('SAP Delivery Date', '2023-02-06')
        query_dist.click_search_reset('Reset')
        """按 SAP Customer ID字段进行筛选"""
        query_dist.input_sap_customer_id_query('406012')
        query_dist.click_search_reset('Search')
        query_dist.assert_query_result('SAP Customer ID', '406012')
        query_dist.click_search_reset('Reset')
        """按 Brand字段进行筛选"""
        query_dist.input_brand_query('itel')
        query_dist.click_search_reset('Search')
        query_dist.assert_query_result('Brand', 'itel')
        query_dist.click_search_reset('Reset')
        """按 IMEI 字段进行筛选"""
        query_dist.input_imei_query('359696712858606')
        query_dist.click_search_reset('Search')
        list_total = query.get_total_content()
        ValueAssert.value_assert_equal('1', list_total)
        query_dist.click_search_reset('Reset')
        """按 market_name字段进行筛选"""
        query_dist.input_market_name_query('AX8')
        query_dist.click_search_reset('Search')
        query_dist.assert_query_result('Market Name', 'AX8')
        query_dist.click_search_reset('Reset')
        """按 country字段进行筛选"""
        query_dist.input_country_query('India', 'Country')
        query_dist.click_search_reset('Search')
        query_dist.assert_query_result('Country', 'India')
        query_dist.click_search_reset('Reset')
        """按 status字段进行筛选"""
        query_dist.assert_query_result('Status', 'On Transit')
        query_dist.input_status_query('Receiving', 'On Transit', 'Finished', 'Country')
        query_dist.click_search_reset('Search')
        query_dist.assert_query_result('Status', 'Finished')
        query_dist.click_search_reset('Reset')


    @allure.story("国包收货")
    @allure.title("国包收货页面，筛选DN记录，查看IMEI详情信息，并导出详情信息")
    @allure.description("国包收货页面，查看IMEI详情信息是否与筛选的DN一致，并导出详情信息")
    @allure.severity("critical")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_dist_receipt_fixture')
    def test_001_006(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        user.click_gotomenu("Purchase Management", "Distributor Receipt")
        view_imei = DitributorReceiptPage(drivers)

        list_dn = view_imei.get_list_dn_text()
        list_total_quantity = view_imei.get_list_quantity_text()
        logging.info("打印Distributor Receipt列表Total Quantity字段的总数量：{}".format(list_total_quantity))
        """根据DN条件进行筛选"""
        view_imei.click_unfold()
        view_imei.input_dn_query(list_dn)
        view_imei.click_search_reset('Search')
        """点击详情按钮"""
        view_imei.click_imei_detail()
        imei_detail_dn = view_imei.get_imei_detail_dn_text()
        get_detail_total = view_imei.text_imei_detail_total()
        logging.info("打印Distributor Receipt详情页的Total总分页数：{}".format(get_detail_total))
        """ 断言列表获取的DN，与打开IMEI Detail详情页的DN比较一致 """
        ValueAssert.value_assert_In(list_dn, imei_detail_dn)
        """ 断言列表获取的quantity总条数，与打开IMEI Detail详情页的Total总条数比较一致，此处断言取消，如果为TV或配件时，个数必定不一致 """
        # ValueAssert.value_assert_equal(list_total_quantity, get_detail_total)

        """点击IMEI Detail详情页的导出按按， 断言导出进度条是否100%"""
        logging.info('the total in test case is %s' % get_detail_total)
        if int(get_detail_total) > 0:
            view_imei.click_distri_imei_detail_export()
            sleep(4)
            complete_value = view_imei.get_imei_detail_download_value()
            ValueAssert.value_assert_equal(complete_value, 100)
        else:
            logging.info('the total is empty')
        """关闭IMEI Detail详情页面"""
        view_imei.click_imei_detail_close()


    @allure.story("国包收货")
    @allure.title("国包收货页面，筛选DN记录，查询国包收货每个筛选项,进行随机组合筛选")
    @allure.description("国包收货页面，查询国包每个筛选项，进行随机组合，断言查询结果数据符合查询条件")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_dist_receipt_fixture')
    def test_001_007(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开采购管理-打开国包收货页面"""
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
                # elif i == 'Material ID':
                #     page.click_detail()
                #     colum = page.get_table_column(i)
                #     logging.info('this the colum is {}'.format(colum))
                #     attribute = page.get_table_content(colum)
                #     ValueAssert.value_assert_equal(attribute, query_dic[i])
                #     page.clos_detail()
                elif i == 'IMEI' or i == 'Material ID':
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


    @allure.story("国包收货")
    @allure.title("国包收货页面，筛选DN记录后，导出国包收货筛选后的记录")
    @allure.description("国包收货页面，筛选DN记录后，导出国包收货筛选后的记录，断言是否导出成功")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_dist_receipt_fixture')
    def test_001_008(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        user.click_gotomenu("Purchase Management", "Distributor Receipt")
        export = DitributorReceiptPage(drivers)
        query = DistributorReceiptQuery(drivers)
        """根据DN条件进行筛选"""
        export.click_unfold()
        list_dn = export.get_list_dn_text()
        export.input_dn_query(list_dn)
        """点击查询按钮"""
        export.click_search_reset('Search')
        """获取列表分页总条数"""
        get_list_total = query.get_total_content()
        """点击IMEI Detail详情页的导出按按， 断言导出进度条是否100%"""
        logging.info('the total in test case is %s' % get_list_total)
        if int(get_list_total) > 0:
            export.click_import_export('Export')
            sleep(2)
            complete_value = export.get_list_download_value()
            ValueAssert.value_assert_equal(complete_value, 100)
        else:
            logging.info('the total is empty')


if __name__ == '__main__':
    pytest.main(['PurchaseManagement_DistributorReceipt.py'])
