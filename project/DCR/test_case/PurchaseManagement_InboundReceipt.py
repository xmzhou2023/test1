from project.DCR.page_object.PurchaseManagement_InboundReceipt import InboundReceiptPage
from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.connect_sql import *
from libs.common.logger_ui import log
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@pytest.fixture(scope='function')
def function_inbound_imei_fixture(drivers):
    yield
    close = InboundReceiptPage(drivers)
    close.click_close_inbound_imei_detail()
    close.click_close_inbound_receipt()

# @allure.feature("采购管理-二代零售商收货")
# class TestQueryInboundReceipt:
#     @allure.story("查询二代零售商收货")
#     @allure.title("二代用户进入Inbound Receipt页面，按日期筛选收货列表数据加载是否正常")
#     @allure.description("二代用户进入Inbound Receipt页面，按日期筛选收货列表数据加载是否正常")
#     @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
#     @pytest.mark.usefixtures('function_menu_fixture')
#     def test_001_001(self, drivers):
#         user = LoginPage(drivers)
#         user.initialize_login(drivers, "BD291501", "dcr123456")
#
#         """销售管理菜单-出库单-筛选出库单用例"""
#         user.click_gotomenu("Purchase Management", "Inbound Receipt")
#
#         query = InboundReceiptPage(drivers)
#         query.click_unfold()
#         query.input_delivery_date("2022-07-01")
#         query.click_deliver_Order()
#         query.click_select_brand()
#         query.click_deliver_Order()
#         query.click_search()
#         query.click_fold()
#
#         saleo_order = query.text_salesOrder()
#         delivery_order = query.text_deliveryOrder()
#         delivery_date = query.get_delivery_date_text()
#         status = query.get_status_text()
#         product = query.get_product_text()
#         total = query.get_total_text()
#
#         ValueAssert.value_assert_IsNoneNot(saleo_order)
#         ValueAssert.value_assert_IsNoneNot(delivery_order)
#         ValueAssert.value_assert_IsNoneNot(delivery_date)
#         ValueAssert.value_assert_IsNoneNot(status)
#         ValueAssert.value_assert_IsNoneNot(product)
#         query.assert_total(total)
#         #query.click_close_inbound_receipt()
#
#
# @allure.feature("采购管理-二代零售商收货")
# class TestQueryIMEIDetail:
#     @allure.story("查询IMEI详情信息")
#     @allure.title("二代用户进入Inbound Receipt页面，查看收货列表第一条IMEI详情信息加载是否正常")
#     @allure.description("二代用户进入Inbound Receipt页面，查看收货列表第一条IMEI详情信息加载是否正常")
#     @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
#     @pytest.mark.usefixtures('function_inbound_imei_fixture')
#     def test_002_001(self, drivers):
#         user1 = LoginPage(drivers)
#         user1.initialize_login(drivers, "BD291501", "dcr123456")
#
#         """销售管理菜单-出库单-筛选出库单用例"""
#         user1.click_gotomenu("Purchase Management", "Inbound Receipt")
#
#         query = InboundReceiptPage(drivers)
#         query.click_unfold()
#         query.click_select_brand()
#         query.click_deliver_Order()
#         query.click_search()
#         query.click_fold()
#
#         #获取Inbound Receipt列表字段文本
#         list_brand = query.get_brand_text()
#         #点击IMEI Detai功能按钮
#         query.click_imei_detail()
#         select_record = query.get_please_select_record()
#         ValueAssert.value_assert_equal("Please select a record", select_record)
#         #勾选第一条记录前的复选框
#         query.select_checkbox()
#         query.click_imei_detail()
#
#         detail_material = query.get_imei_detail_material_id()
#         detail_product = query.get_imei_detail_product()
#         detail_itel = query.get_imei_detail_itel()
#         detail_brand = query.get_imei_detail_brand()
#         detail_imei = query.get_imei_detail_imei()
#         detail_export = query.get_imei_detail_export()
#         total = query.get_imei_detail_total()
#         query.assert_total_imei_detail(total)
#
#         ValueAssert.value_assert_IsNoneNot(detail_product)
#         ValueAssert.value_assert_IsNoneNot(detail_itel )
#         ValueAssert.value_assert_equal(list_brand, detail_brand)
#         ValueAssert.value_assert_IsNoneNot(detail_material)
#         ValueAssert.value_assert_IsNoneNot(detail_imei)
#         ValueAssert.value_assert_equal("Export", detail_export)
#         #query.click_close_inbound_imei_detail()
#         #query.click_close_inbound_receipt()


@allure.feature("采购管理-二代零售商收货")
class TestScanIMEIInboundReceipt:
    @allure.story("二代扫码收货")
    @allure.title("二代用户进入Inbound Receipt页面，点击扫码收货操作")
    @allure.description("二代用户进入Inbound Receipt页面，点击Stock-in by Scan扫码收货操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD40344201", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Sales Management", "Delivery Order")

        """国包账号，新建出库单"""
        add = DeliveryOrderPage(drivers)
        sql1 = SQL('DCR', 'test')
        """从数据库表查询国包BD403442仓库的库存IMEI"""
        varsql1 = "SELECT IMEI FROM  t_channel_warehouse_current_stock WHERE WAREHOUSE_ID ='62139' AND STATUS = 1  limit 1"
        result = sql1.query_db(varsql1)
        imei = result[0].get("IMEI")

        """点击Add新增出库单按"""
        add.click_add()
        add.input_sub_buyer("BD2915")
        add.input_deli_pay_mode("Online")
        add.input_imei(imei)
        add.click_check()
        add.click_submit()
        try:
            affirm = add.get_text_submit_affirm()
            if affirm == "Submit":
                add.click_submit_affirm()
                DomAssert(drivers).assert_att("Submit successfully")
        except Exception as e:
            DomAssert(drivers).assert_att("Submit successfully")
        sleep(1)
        add.click_search()
        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        salesorder = add.text_sales_order()
        deliveryorder = add.text_delivery_order()

        """从数据库表中，获取国包出库单ID，传给出库单筛选方法"""
        sql2 = SQL('DCR', 'test')
        varsql2 = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        result = sql2.query_db(varsql2)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        sleep(1)

        add.input_salesorder(order_code)
        add.input_deliveryorder(delivery_code)
        add.click_search()

        """出库单页面，调用断言封装的方法，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        sleep(1)


        """Inbound Receipt页面，扫码收货操作"""
        user.initialize_login(drivers, "BD291501", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Purchase Management", "Inbound Receipt")
        scan_receipt = InboundReceiptPage(drivers)
        scan_receipt.click_scan_imei_receipt()
        scan_receipt.input_scan_imei(imei)
        scan_receipt.click_check()

        """点击Check后，断言扫码的IMEI是否校验通过"""
        get_scanned = scan_receipt.get_scanned()
        get_success = scan_receipt.get_inbound_scan_record_success()
        get_record_imei = scan_receipt.get_inbound_scan_record_imei(imei)
        get_order_detail_scanned = scan_receipt.get_order_detail_scanned()
        ValueAssert.value_assert_equal(get_scanned, get_order_detail_scanned)
        ValueAssert.value_assert_In('Success', get_success)
        ValueAssert.value_assert_equal(get_record_imei, imei)

        """点击Submit提交按钮"""
        scan_receipt.click_submit()
        DomAssert(drivers).assert_att('INBOUND_SUCCESS')
        sleep(1.5)
        """查询最近出库，且待收货状态的出库单"""
        scan_receipt.input_deliveryOrder(delivery_code)
        """点击Search查询按钮"""
        scan_receipt.click_search()
        """"断言根据Delivery Order ID筛选项筛选，收货成功后，Status是否更新为Goods Receipt状态"""
        get_list_salesorder = scan_receipt.text_salesOrder()
        get_list_delivery = scan_receipt.text_deliveryOrder()
        get_list_status = scan_receipt.get_list_status()
        ValueAssert.value_assert_equal(get_list_salesorder, order_code)
        ValueAssert.value_assert_equal(get_list_delivery, delivery_code)
        ValueAssert.value_assert_equal('Goods Receipt', get_list_status)


if __name__ == '__main__':
    pytest.main(['PurchaseManagement_InboundReceipt.py'])
