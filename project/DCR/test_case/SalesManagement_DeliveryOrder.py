from project.DCR.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
import logging
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
from libs.common.connect_sql import *
from project.DCR.page_object.PurchaseManagement_InboundReceipt import InboundReceiptPage
from project.DCR.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
import datetime
import pytest
import allure

@allure.feature("销售管理-出库单")
class TestQueryDeliveryOrder:
    @allure.story("查询出库单列表")
    @allure.title("出库单页面，查询出库单列表加载数据")
    @allure.description("出库单页面，查询出库单列表加载数据正常，断言查询的出库单数据是否加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD40344201", "dcr123456")

        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Delivery Order")

        list = DeliveryOrderPage(drivers)
        sale_order = list.text_sales_order()
        deli_order = list.text_delivery_order()
        deli_date = list.get_delivery_date_text()
        status = list.text_delivery_Status()
        total = list.get_total_text()

        ValueAssert.value_assert_IsNoneNot(sale_order)
        ValueAssert.value_assert_IsNoneNot(deli_order)
        ValueAssert.value_assert_IsNoneNot(deli_date)
        ValueAssert.value_assert_IsNoneNot(status)
        list.assert_total(total)
        list.click_close_delivery_order()


@allure.feature("销售管理-出库单")
class TestViewDeliveryIMEIDetails:
    @allure.story("查看出库单IMEI详情")
    @allure.title("国包用户，查看出库单IMEI详情")
    @allure.description("国包用户，查看出库单IMEI详情")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_002_001(self, drivers):
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "BD40344201", "dcr123456")

        """打开销售管理-打开出库单页面"""
        user1.click_gotomenu("Sales Management", "Delivery Order")

        imei_detail = DeliveryOrderPage(drivers)
        sales_order = imei_detail.get_sales_order_text()
        imei_detail.input_salesorder(sales_order)
        imei_detail.click_search()

        list_sales_order = imei_detail.get_sales_order_text()
        list_product = imei_detail.get_list_product_text()
        list_item = imei_detail.get_list_item_text()

        """点击IMEI Detail查看按钮"""
        imei_detail.click_imei_detail()
        detail_title_sale = imei_detail.get_detail_title_sale_text()
        detail_product = imei_detail.get_detail_product_text()
        detail_item = imei_detail.get_detail_item_text()
        detail_imei = imei_detail.get_detail_imei_text()
        detail_total = imei_detail.get_detail_total_text()

        ValueAssert.value_assert_equal(sales_order, list_sales_order)
        ValueAssert.value_assert_In(list_sales_order, detail_title_sale)
        ValueAssert.value_assert_equal(list_product, detail_product)
        ValueAssert.value_assert_equal(list_item, detail_item)
        ValueAssert.value_assert_IsNoneNot(detail_imei)
        ValueAssert.value_assert_In("1", detail_total)
        imei_detail.click_close_imei_detail()
        imei_detail.click_close_delivery_order()


@allure.feature("销售管理-出库单")
class TestExportDeliveryOrder:
    @allure.story("导出筛选的出库单")
    @allure.title("出库单页面，导出筛选的出库单记录")
    @allure.description("出库单页面，筛选出库单记录后，导出筛选的出库单记录")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    def test_003_001(self, drivers):
        user2 = LoginPage(drivers)
        user2.initialize_login(drivers, "BD40344201", "dcr123456")

        """打开销售管理-打开出库单页面"""
        user2.click_gotomenu("Sales Management", "Delivery Order")

        export = DeliveryOrderPage(drivers)
        # 获取日期
        base = Base(drivers)
        today = base.get_datetime_today()

        export.click_unfold()
        export.input_delivery_date(today, today)
        export.click_status_input_box()
        export.click_fold()
        export.click_search()

        #筛选出库单后，点击导出功能
        export.click_export()
        export.click_download_more()
        export.input_task_name("Delivery Order")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Delivery Order")
        ValueAssert.value_assert_equal(task_id, "BD40344201")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        export.click_close_export_record()
        export.click_close_delivery_order()


@allure.feature("销售管理-出库单")
class TestAddDeliveryOrder:
    @allure.story("新建出库单，产品为无码的，买方为临时客户")
    @allure.title("国包用户，新建出库单，产品为无码的，买方为临时客户")
    @allure.description("国包用户，新建出库单，产品为无码时，买方为临时客户")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_001(self, drivers):
        user3 = LoginPage(drivers)
        user3.initialize_login(drivers, "BD40344201", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user3.click_gotomenu("Sales Management", "Delivery Order")

        add = DeliveryOrderPage(drivers)
        num = add.customer_random()
        add.click_add()
        add.click_temporary_customer()
        add.input_deli_pay_mode("Wechat")
        add.input_temporary_customer_name("lhmcustomer" + num)
        add.input_customer_contact_no("13873094" + num)
        add.click_business_type()

        add.click_quantity_radio_button()
        add.click_quantity_add()
        add.click_quantity_product("TECNO B1 BLACK")
        add.input_delivery_quantity("1")
        add.get_delivery_quantity_text("1")
        """点击Submit提交按钮"""
        add.click_submit()

        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        dom = DomAssert(drivers)
        dom.assert_att("Submit successfully")
        sleep(4)

        """断言查询新建的无码出库单"""
        user = SQL('DCR', 'test')
        varsql1 = "select * from  t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667'  and status=80200001 order by created_time desc limit 1"
        result = user.query_db(varsql1)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        logging.info("查询数据库销售单号order_code{}".format(order_code))
        logging.info("查询数据库出库单号delivery_code{}".format(delivery_code))
        sleep(1)

        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        salesorder = add.text_sales_order()
        deliveryorder = add.text_delivery_order()

        """出库单页面，筛选新建的无码出库单ID"""
        add.input_salesorder(order_code)
        add.input_deliveryorder(delivery_code)
        add.click_search()

        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        add.click_close_delivery_order()


    @allure.story("新建出库单，产品为有码的，买方为临时客户")
    @allure.title("国包用户，新建出库单，产品为有码的，买方为临时客户")
    @allure.description("国包用户，新建出库单，产品为有码的，买方为临时客户")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_002(self, drivers):
        user4 = LoginPage(drivers)
        user4.initialize_login(drivers, "BD40344201", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user4.click_gotomenu("Sales Management", "Delivery Order")

        add = DeliveryOrderPage(drivers)
        num = add.customer_random()
        add.click_add()
        add.click_temporary_customer()
        add.input_deli_pay_mode("Wechat")
        add.input_temporary_customer_name("lhmcustomer" + num)
        add.input_customer_contact_no("13873094" + num)
        add.click_business_type()

        """从数据库表查询国包BD403442仓库的库存IMEI"""
        varsql = "SELECT IMEI FROM  t_channel_warehouse_current_stock WHERE WAREHOUSE_ID ='62139' AND STATUS = 1  limit 1"
        user = SQL('DCR', 'test')
        result = user.query_db(varsql)
        imei = result[0].get("IMEI")
        sleep(1)
        add.input_imei(imei)
        add.click_check()
        add.click_submit()
        dom = DomAssert(drivers)
        try:
            affirm = add.get_text_submit_affirm()
            if affirm == "Submit":
                add.click_submit_affirm()
                dom.assert_att("Submit successfully")
        except Exception as e:
            dom.assert_att("Submit successfully")
        sleep(4)

        """断言查询新建的无码出库单"""
        user = SQL('DCR', 'test')
        varsql1 = "select * from  t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667'  and status=80200001 order by created_time desc limit 1"
        result = user.query_db(varsql1)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        sleep(2)

        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        salesorder = add.text_sales_order()
        deliveryorder = add.text_delivery_order()

        """出库单页面，筛选新建的无码出库单ID"""
        add.input_salesorder(order_code)
        add.input_deliveryorder(delivery_code)
        add.click_search()

        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        add.click_close_delivery_order()


if __name__ == '__main__':
    pytest.main(['SalesManagement_DeliveryOrder.py'])

