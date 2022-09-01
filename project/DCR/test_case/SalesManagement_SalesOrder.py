from project.DCR.page_object.SalesManagement_SalesOrder import SalesOrderPage
from project.DCR.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.connect_sql import *
from libs.common.time_ui import sleep
import logging
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_export_fixture(drivers):
    yield
    close = SalesOrderPage(drivers)
    close.click_close_export_record()
    close.click_close_sales_order()

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    for i in range(1):
        get_menu_class = menu.get_open_menu_class()
        class_value = "tags-view-item router-link-exact-active router-link-active active"
        if class_value == str(get_menu_class):
            menu.click_close_open_menu()
            sleep(1)

@allure.feature("销售管理-销售单")
class TestAddSalesOrder:
    @allure.story("新增销售单")
    @allure.title("国包用户创建销售单，产品为无码的，买方为临时客户,并直接出库操作")
    @allure.description("销售单页面，国包用户创建销售单，产品为无码的，买方为临时客户，并直接出库操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "EG40052202", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Sales Order")

        add = SalesOrderPage(drivers)
        num = add.customer_random()
        add.click_add_sales()

        add.click_temporary_customer()
        add.input_temporary_customer_name("testcodeless" + num)
        add.input_customer_contact_no("13988776" + num)
        add.click_business_type()

        add.input_sales_brand("oraimo")
        add.input_sales_product("OEB-E75D  BLACK")
        add.input_sales_quantity("1")
        add.click_submit()
        add.click_submit_OK()

        """对新建的销售单，直接出库操作"""
        sales_id = add.get_text_sales_id()
        add.input_sales_order_ID(sales_id)
        add.click_checkbox_orderID()
        add.click_Delivery_button()

        add.input_Payment_Mode("Wechat")
        add.click_quantity_radio_button()

        add.input_delivery_quantity('1')
        add.click_delivery_quantity()

        product = add.get_order_detail_product()
        ValueAssert.value_assert_IsNoneNot(product)
        quantity = add.get_new_delivery_quantity()
        ValueAssert.value_assert_equal('1', quantity)

        """点击Submit提交按钮"""
        add.click_submit()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        dom = DomAssert(drivers)
        dom.assert_att("Successfully")
        sleep(3)
        """断言状态是否更新为Delivered状态"""
        status = add.get_list_status_text()
        ValueAssert.value_assert_equal("Delivered", status)
        #add.click_close_sales_order()


    @allure.story("新增销售单")
    @allure.title("国包用户，新建销售单，无码产品，买方为系统二代客户，并直接出库操作")
    @allure.description("销售单页面，国包用户，新建销售单，无码产品，买方为系统二代客户，并直接出库操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "EG40052202", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Sales Order")
        add = SalesOrderPage(drivers)
        add.click_add_sales()

        add.input_sales_buyer("NG20613")
        add.input_sales_brand("oraimo")
        add.input_sales_product("OEB-E75D  BLACK")
        add.input_sales_quantity('1')
        add.click_submit()
        add.click_submit_OK()

        """对新建的销售单，直接出库操作"""
        add.click_checkbox_orderID()
        add.click_Delivery_button()
        add.input_Payment_Mode("Wechat")
        add.click_quantity_radio_button()

        add.input_delivery_quantity('1')
        add.click_delivery_quantity()

        product = add.get_order_detail_product()
        ValueAssert.value_assert_IsNoneNot(product)
        quantity = add.get_new_delivery_quantity()
        ValueAssert.value_assert_equal('1', quantity)
        """点击Submit提交按钮"""
        add.click_submit()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        dom = DomAssert(drivers)
        dom.assert_att("Successfully")
        sleep(1)
        add.click_search()
        """获取列表，销售单ID与Status文本内容"""
        get_sales_order = add.get_text_sales_id()
        get_status = add.get_text_sales_status("Delivered")

        # """二代用户，查询数据库最近新建的销售单ID"""
        # user = SQL('DCR', 'test')
        # sql = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        # result = user.query_db(sql)
        # order = result[0].get("order_code")
        # status = result[0].get("status")
        # if status == 1:
        #     sales_status = "Delivered"
        # """销售单页面，按销售单ID筛选销售单信息"""
        add.input_sales_order_ID(get_sales_order)
        add.click_search()

        get_sales_order2 = add.get_text_sales_id()
        get_status2 = add.get_text_sales_status("Delivered")
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        ValueAssert.value_assert_equal(get_sales_order, get_sales_order2)
        ValueAssert.value_assert_equal(get_status, get_status2)
        #add.click_close_sales_order()


    @allure.story("新增销售单")
    @allure.title("销售单页面，二代用户新增有码销售单操作")
    @allure.description("销售单页面，二代用户新增有码销售单操作成功后，校验新增的销售单是否存在")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_003(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Sales Management", "Sales Order")
        """销售订单页面，新建销售单"""
        add_sales = SalesOrderPage(drivers)
        add_sales.click_add_sales()
        add_sales.input_sales_buyer("EG000562")
        add_sales.input_sales_brand('TECNO')
        add_sales.input_sales_product("SPARK 6 Go 64+4 AQUA BLUE")
        add_sales.input_sales_quantity('1')
        add_sales.click_submit()
        add_sales.click_submit_OK()

        """二代用户，查询数据库最近新建的销售单ID"""
        sql = SQL('DCR', 'test')
        sql_val = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        result = sql.query_db(sql_val)
        order_code = result[0].get("order_code")
        status = result[0].get("status")
        if status == 0:
            sales_status = "Pending"
        """销售单页面，按销售单ID筛选销售单信息"""
        add_sales.input_sales_order_ID(order_code)
        add_sales.click_search()

        """获取列表，销售单ID与Status文本内容"""
        get_sales_order = add_sales.get_text_sales_id()
        get_status = add_sales.get_text_sales_status("Pending")
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        ValueAssert.value_assert_equal(get_sales_order, order_code)
        ValueAssert.value_assert_equal(get_status, sales_status)
        #add_sales.click_close_sales_order()


    @allure.story("销售单出库")
    @allure.title("销售单页面，二代用户对新增的有码销售单，进行出库操作")
    @allure.description("销售单页面，二代用户对新增的有码销售单，进行出库操作成功后，校验销售单对应的状态是否更新为：Delivered")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")

        """打开Report Analysis->IMEI Inventory Query菜单"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")

        """调用菜单栏，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        delivery = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        delivery.click_unfold()
        delivery.input_material_id("11001120")
        delivery.click_inventory_search()
        imei = delivery.get_text_imei_inventory()
        delivery.close_imei_inventory_query()

        """ 刷新页面 """
        delivery.click_refresh(drivers)
        user.click_gotomenu("Sales Management", "Sales Order")

        """二代用户，查询数据库最近新建的销售单ID"""
        sql = SQL('DCR', 'test')
        sql_val = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        result = sql.query_db(sql_val)
        order_code = result[0].get("order_code")
        # status = result[0].get("status")
        # if status == 80200000:
        #     sales_status = "Delivered"
        """销售单页面，按销售单ID筛选销售单信息"""
        delivery.input_sales_order_ID(order_code)
        delivery.click_search()

        """勾选新建的销售单，直接出库操作"""
        delivery.click_checkbox_orderID()
        """点击Delivery出库按钮"""
        delivery.click_Delivery_button()

        delivery.input_Payment_Mode('Wechat')
        delivery.input_imei(imei)
        delivery.click_check()
        """点击Check按钮后，断言IMEI是否校验成功"""
        get_imei = delivery.get_scan_record_imei(imei)
        get_success = delivery.get_scan_record_success()
        ValueAssert.value_assert_In("Success", get_success)
        ValueAssert.value_assert_In(imei, get_imei)
        """点击提交按钮"""
        delivery.click_submit_delivery()

        """销售单页面，按销售单ID筛选销售单信息，断言该条销售单对应的状态是否更新为：Delivered状态"""
        text_sales_order = delivery.get_text_sales_id()
        delivery.input_sales_order_ID(text_sales_order)
        delivery.click_search()
        text_status = delivery.get_text_sales_status("Delivered")
        """出库操作成功后，验证该条销售单对应的状态是否更新为：Delivered状态"""
        ValueAssert.value_assert_equal(text_status, "Delivered")
        delivery.click_close_sales_order()

        """对出库的销售单，进行退货操作,闭环流程"""
        Base(drivers).refresh()
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Return Order")
        return_order = ReturnOrderPage(drivers)

        """从数据库表中，获取二代出库单ID，传给出库单筛选方法"""
        deli_sql = SQL('DCR', 'test')
        deli_varsql = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200000 order by created_time desc limit 1"
        deli_result = deli_sql.query_db(deli_varsql)
        delivery_code = deli_result[0].get("delivery_code")
        logging.info("打印数据库查询的二代出库单ID delivery_code{}".format(delivery_code))

        return_order.click_Add()
        return_order.click_Return_Type()
        return_order.radio_Delivery_order()
        return_order.input_Delivery_order(delivery_code)
        return_order.click_Check()
        get_success = return_order.get_text_Record()
        get_imei = return_order.get_Scan_Record_IMEI(imei)
        ValueAssert.value_assert_equal("Success", get_success)
        ValueAssert.value_assert_In(imei, get_imei)

        """点击提交按钮"""
        return_order.click_Submit()
        dom = DomAssert(drivers)
        dom.assert_att("Submit Success!")

        """退货单页面，根据出库单ID查询 是否生成一条Return Order ID 退货单"""
        return_order.input_Delivery_Orderid(delivery_code)
        return_order.click_Search()

        """断言筛选退货列表页，获取退货单ID、退货出库单ID、退货状态与数据库表中查询的出库单ID对比是否一致"""
        get_return_order_id = return_order.get_list_return_order_id()
        get_delivery_order_id = return_order.get_text_deliveryID()
        get_status = return_order.get_return_status()
        ValueAssert.value_assert_IsNoneNot(get_return_order_id)
        ValueAssert.value_assert_equal(get_delivery_order_id, delivery_code)
        ValueAssert.value_assert_equal("Approved", get_status)


@allure.feature("销售管理-销售单")
class TestDeleteSalesOrder:
    @allure.story("删除销售单")
    @allure.title("销售单页面，国包用户，删除新建的Pending状态的销售单操作")
    @allure.description("销售单页面，国包用户，对新建Pending状态的销售单进行删除操作")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "EG40052202", "dcr123456")
        """销售管理菜单-打开销售单菜单"""
        user.click_gotomenu("Sales Management", "Sales Order")
        """调用新增销售单用例"""
        delete = SalesOrderPage(drivers)
        dom = DomAssert(drivers)

        delete.click_add_sales()
        delete.input_sales_buyer("NG20613")
        delete.input_sales_brand('oraimo')
        delete.input_sales_product("OEB-E75D  BLACK")
        delete.input_sales_quantity('1')
        delete.click_submit()
        delete.click_submit_OK()

        """获取列表，销售单ID文本内容"""
        get_sales_order = delete.get_text_sales_id()
        """销售单页面，按销售单ID筛选销售单信息"""
        delete.input_sales_order_ID(get_sales_order)
        delete.click_search()

        get_query_sales_order = delete.get_text_sales_id()
        ValueAssert.value_assert_equal(get_query_sales_order, get_sales_order)

        delete.click_delete_sales()
        delete.click_confirm_delete()
        dom.assert_att("Successfully")
        #delete.click_close_sales_order()


    @allure.story("删除销售单")
    @allure.title("销售单页面，国包用户，删除Delivered状态的销售单，提示不支持删除")
    @allure.description("销售单页面，国包用户，删除Delivered状态的销售单，提示不支持删除")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_002(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "EG40052202", "dcr123456")
        """销售管理菜单-打开销售单菜单"""
        user.click_gotomenu("Sales Management", "Sales Order")
        delete = SalesOrderPage(drivers)
        dom = DomAssert(drivers)

        """Status筛选项输入Delivered条件筛选已发货的销售单"""
        delete.input_status_query("Delivered")
        delete.click_search()

        """获取列表，销售单ID与Status文本内容"""
        get_sales_order = delete.get_text_sales_id()
        get_status = delete.get_text_sales_status("Delivered")

        """筛选已发货的销售单，进行删除操作"""
        delete.input_sales_order_ID(get_sales_order)
        delete.click_search()

        if get_status == "Delivered":
            delete.click_delete_sales()
        """断言已发货状态的销售单不支持删除"""
        dom.assert_att("The scanned IMEI exists in the order, fail to delete")
        #delete.click_close_sales_order()


@allure.feature("销售管理-销售单")
class TestExportSalesOrder:
    @allure.story("导出销售单")
    @allure.title("销售单页面，国包用户，导出筛选条件下销售单，导出文件内容和列表查询结果一致")
    @allure.description("销售单页面，国包用户，导出筛选条件下销售单，导出文件内容和列表查询结果一致")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_003_001(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-打开销售单菜单"""
        user.click_gotomenu("Sales Management", "Sales Order")
        export = SalesOrderPage(drivers)
        # 获取当天日期
        base = Base(drivers)
        today = base.get_datetime_today()

        """按销售单创建日期、Status条件筛选销售单"""
        export.click_sales_order_unfold()
        export.input_status_query("Delivered")
        export.list_input_create_date("2022-07-30", today)
        export.click_search()

        """点击导出按钮"""
        export.click_export()
        export.click_download_more()
        export.input_task_name("Sale Order")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Sale Order")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_sales_order()


    @allure.story("导出销售单")
    @allure.title("销售单页面，国包用户，导出筛选条件下销售单详情，导出文件内容和列表查询结果一致")
    @allure.description("销售单页面，国包用户，导出筛选条件下销售单详情，导出文件内容和列表查询结果一致")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_003_002(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """销售管理菜单-打开销售单菜单"""
        user.click_gotomenu("Sales Management", "Sales Order")

        export = SalesOrderPage(drivers)
        # 获取当天日期
        base = Base(drivers)
        today = base.get_datetime_today()

        """按销售单创建日期、Status条件筛选销售单"""
        export.click_sales_order_unfold()
        export.input_status_query("Delivered")
        export.list_input_create_date("2022-07-30", today)
        export.click_search()

        """点击导出按钮"""
        export.click_more_option()
        export.click_export_detail()

        export.click_download_more()
        export.input_task_name("Sales Detail")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Sales Detail")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_sales_order()

if __name__ == '__main__':
    pytest.main(['SalesManagement_SalesOrder.py'])
