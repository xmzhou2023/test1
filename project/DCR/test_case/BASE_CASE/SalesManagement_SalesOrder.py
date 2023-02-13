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
    menu = LoginPage(drivers)
    for i in range(2):
        get_menu_class = menu.get_open_menu_class()
        class_value = "tags-view-item router-link-exact-active router-link-active active"
        if class_value == str(get_menu_class):
            menu.click_close_open_menu()

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("销售管理-销售单")
class TestAddSalesOrder:
    @allure.story("新增销售单")
    @allure.title("国包用户,创建销售单，产品为无码的，买方为临时客户,并直接出库操作")
    @allure.description("销售单页面，国包用户创建销售单，产品为无码的，买方为临时客户，并直接出库操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
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
        add.click_business_type('Retail&Wholesale')
        add.input_sales_brand("oraimo")
        add.input_sales_product("OEB-E75D  BLACK")
        add.input_sales_quantity("1")
        """点击提交按钮"""
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
        DomAssert(drivers).assert_att("Successfully")
        add.click_search()
        """断言状态是否更新为Delivered状态"""
        add.assert_sales_order_field('Status', 'Delivered')
        #add.click_close_sales_order()


    @allure.story("新增销售单")
    @allure.title("国包用户,创建销售单，产品为有码的，买方为临时客户，不出库")
    @allure.description("国包用户,创建销售单，产品为有码的，买方为临时客户，不出库")
    @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD40344201", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Sales Order")
        temporary_cust = SalesOrderPage(drivers)
        num = temporary_cust.customer_random()
        """点击add新建销售单按钮"""
        temporary_cust.click_add_sales()
        """添加临时客户"""
        temporary_cust.click_temporary_customer()
        temporary_cust.input_temporary_customer_name("testTemporaryCust" + num)
        temporary_cust.input_customer_contact_no("13873776" + num)
        temporary_cust.click_business_type('Retail&Wholesale')
        """填写产品信息"""
        temporary_cust.input_sales_brand('TECNO')
        temporary_cust.input_sales_product('SPARK Go 2022 32+2 ATLANBLUE')
        temporary_cust.input_sales_quantity('1')
        temporary_cust.click_submit()
        temporary_cust.click_submit_OK()
        """查询后端数据库，最新新建的销售单ID，然后筛选新建的销售单，买家为临时客户可为空"""
        order_code = temporary_cust.select_sql_sales_order('62139', '1596874516539667', '')
        temporary_cust.input_sales_order_ID(order_code)
        temporary_cust.click_search()
        """断言获取列表销售单ID、状态，与查询数据库表里的销售单ID与状态是否一致"""
        temporary_cust.assert_sales_order_field('Sales Order ID', order_code)
        temporary_cust.assert_sales_order_field('Status', 'Pending')
        """查看Pending 状态的 IMEI Detail 详情,未出库IMEI，IMEI Detail详情显示No Data"""
        temporary_cust.click_sales_order_imei_detail()
        get_imei_detail_header = temporary_cust.get_sales_order_imei_detail_header()
        ValueAssert.value_assert_equal("IMEI Detail", get_imei_detail_header)
        get_imei_detail_total = temporary_cust.get_sales_order_imei_detail_total()
        ValueAssert.value_assert_equal('0', get_imei_detail_total)
        temporary_cust.close_sales_order_imei_detail()


    @allure.story("新增销售单")
    @allure.title("国包用户，新建销售单，无码产品，买方为系统二代客户，并直接出库操作")
    @allure.description("销售单页面，国包用户，新建销售单，无码产品，买方为系统二代客户，并直接出库操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_003(self, drivers):
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
        """点击提交按钮"""
        add.click_submit()
        add.click_submit_OK()
        """对新建的销售单，直接出库操作"""
        add.click_checkbox_orderID()
        add.click_Delivery_button()
        add.input_Payment_Mode("Wechat")
        add.click_quantity_radio_button()
        add.input_delivery_quantity('1')
        add.click_delivery_quantity()
        quantity = add.get_new_delivery_quantity()
        ValueAssert.value_assert_equal('1', quantity)
        """点击Submit提交按钮"""
        add.click_submit()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        DomAssert(drivers).assert_att("Successfully")
        add.click_search()
        """二代用户，查询数据库最近新建的销售单ID,status =2 为Delivered状态 """
        user = SQL('DCR', 'test')
        sql = "select order_code,status from t_channel_sale_ticket where warehouse_id = '61735' and seller_id = '1596874516539127' and buyer_id = '1596874516539550' and status = 2 order by created_time desc limit 1"
        result = user.query_db(sql)
        sales_order_id = result[0].get("order_code")
        status = result[0].get("status")
        if status == 2:
            sales_status = "Delivered"
        # """销售单页面，按销售单ID筛选销售单信息"""
        add.input_sales_order_ID(sales_order_id)
        """点击查询按钮"""
        add.click_search()
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        add.assert_sales_order_field('Sales Order ID', sales_order_id)
        add.assert_sales_order_field('Status', sales_status)
        #add.click_close_sales_order()


    @allure.story("新增销售单")
    @allure.title("销售单页面，二代用户新增有码销售单操作,然后进行直接出库操作,最后进行退货操作")
    @allure.description("销售单页面，二代用户新增有码销售单操作成功后，然后进行出库操作,最后进行退货操作，闭环流程")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_004(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Sales Management", "Sales Order")
        """销售订单页面，新建销售单"""
        add_sales = SalesOrderPage(drivers)
        add_sales.click_add_sales()
        add_sales.input_sales_buyer('EG000562')
        add_sales.input_sales_brand('TECNO')
        add_sales.input_sales_product('SPARK 6 Go 64+4 AQUA BLUE')
        add_sales.input_sales_quantity('1')
        add_sales.click_submit()
        add_sales.click_submit_OK()
        """二代用户，查询数据库最近新建的销售单ID"""
        sql = SQL('DCR', 'test')
        sql_val = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        result = sql.query_db(sql_val)
        sales_order_code = result[0].get("order_code")
        status = result[0].get("status")
        if status == 0:
            sales_status = "Pending"
        """销售单页面，按销售单ID筛选销售单信息"""
        add_sales.input_sales_order_ID(sales_order_code)
        add_sales.click_search()
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        add_sales.assert_sales_order_field('Sales Order ID', sales_order_code)
        add_sales.assert_sales_order_field('Status', sales_status)
        add_sales.click_close_sales_order()

        """ 刷新页面 获取库存IMEI，对新增的销售单，直接出库操作"""
        Base(drivers).refresh()
        """打开Report Analysis->IMEI Inventory Query菜单，获取库存IMEI"""
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
        Base(drivers).refresh()
        user.click_gotomenu("Sales Management", "Sales Order")
        """销售单页面，按销售单ID筛选销售单信息"""
        delivery.input_sales_order_ID(sales_order_code)
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
        """出库操作，点击提交按钮"""
        delivery.click_submit_delivery()

        """销售单页面，按销售单ID筛选销售单信息，断言该条销售单对应的状态是否更新为：Delivered状态"""
        delivery.input_sales_order_ID(sales_order_code)
        delivery.click_search()
        """出库操作成功后，验证该条销售单对应的状态是否更新为：Delivered状态"""
        delivery.assert_sales_order_field('Status', 'Delivered')
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
        DomAssert(drivers).assert_att("Submit Success!")
        """退货单页面，根据出库单ID查询 是否生成一条Return Order ID 退货单"""
        return_order.input_Delivery_Orderid(delivery_code)
        return_order.click_Search()
        """断言筛选退货列表页，获取退货单ID、退货出库单ID、退货状态与数据库表中查询的出库单ID对比是否一致"""
        get_return_order_id = return_order.get_list_return_order_id()
        return_order.assert_return_order_field('Return Order ID', get_return_order_id)
        return_order.assert_return_order_field('Delivery/DN Order ID', delivery_code)
        return_order.assert_return_order_field('Status', 'Approved')


@allure.feature("销售管理-销售单")
class TestDeleteSalesOrder:
    @allure.story("删除销售单")
    @allure.title("销售单页面，国包用户，删除新建的Pending状态的销售单操作")
    @allure.description("销售单页面，国包用户，对新建Pending状态的销售单进行删除操作")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "EG40052202", "dcr123456")
        """销售管理菜单-打开销售单菜单"""
        user.click_gotomenu("Sales Management", "Sales Order")
        """调用新增销售单用例"""
        delete = SalesOrderPage(drivers)
        delete.click_add_sales()
        delete.input_sales_buyer("NG20613")
        delete.input_sales_brand('oraimo')
        delete.input_sales_product("OEB-E75D  BLACK")
        delete.input_sales_quantity('1')
        delete.click_submit()
        delete.click_submit_OK()
        """点击查询，重新加载数据"""
        delete.click_search()
        """获取列表，销售单ID文本内容"""
        get_sales_order = delete.get_text_sales_id()
        """销售单页面，按销售单ID筛选销售单信息"""
        delete.input_sales_order_ID(get_sales_order)
        delete.click_search()
        delete.assert_sales_order_field('Sales Order ID', get_sales_order)
        """点击删除销售单功能，能删除成功"""
        delete.click_delete_sales()
        delete.click_confirm_delete()
        DomAssert(drivers).assert_att("Successfully")
        #delete.click_close_sales_order()


    @allure.story("删除销售单")
    @allure.title("销售单页面，国包用户，删除Delivered状态的销售单，提示不支持删除")
    @allure.description("销售单页面，国包用户，删除Delivered状态的销售单，提示不支持删除")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_002(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "EG40052202", "dcr123456")
        """销售管理菜单-打开销售单菜单"""
        user.click_gotomenu("Sales Management", "Sales Order")
        delete = SalesOrderPage(drivers)
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
        DomAssert(drivers).assert_att("The scanned IMEI exists in the order, fail to delete")
        #delete.click_close_sales_order()


@allure.feature("销售管理-销售单")
class TestExportSalesOrder:
    @allure.story("导出销售单")
    @allure.title("销售单页面，国包用户，导出筛选条件下销售单，导出文件内容和列表查询结果一致")
    @allure.description("销售单页面，国包用户，导出筛选条件下销售单，导出文件内容和列表查询结果一致")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_export_fixture')
    def test_003_001(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, 'lhmadmin', 'dcr123456')
        """销售管理菜单-打开销售单菜单"""
        user.click_gotomenu('Sales Management', 'Sales Order')
        export = SalesOrderPage(drivers)
        # 获取当天日期
        today = Base(drivers).get_datetime_today()
        last_date = export.get_last_day(7)
        """按销售单创建日期、Status条件筛选销售单"""
        export.click_sales_order_unfold()
        export.input_status_query('Delivered')
        export.list_input_create_date(last_date, today)
        export.click_search()

        """点击导出按钮"""
        export.click_export()
        export.click_download_more()
        """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
        export.input_task_name('Sales Order')
        export.export_record_create_date_query(today)
        down_status = export.click_export_search()
        file_size = export.get_file_size_text()
        export_time = export.get_export_time_text()
        export.assert_file_time_size(file_size, export_time)
        export.assert_sales_order_field('Download Status', down_status)
        export.assert_sales_order_field('Task Name', 'Sales Order')
        export.assert_sales_order_field('User ID', 'lhmadmin')
        export.assert_sales_order_field('Create Date', today)
        export.assert_sales_order_field('Completed Date', today)
        export.assert_sales_order_field('Operation', 'Download')
        #export.click_close_export_record()
        #export.click_close_sales_order()


    @allure.story("导出销售单")
    @allure.title("销售单页面，国包用户，导出筛选条件下销售单详情，导出文件内容和列表查询结果一致")
    @allure.description("销售单页面，国包用户，导出筛选条件下销售单详情，导出文件内容和列表查询结果一致")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_export_fixture')
    def test_003_002(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, 'lhmadmin', 'dcr123456')
        """销售管理菜单-打开销售单菜单"""
        user.click_gotomenu('Sales Management', 'Sales Order')
        export = SalesOrderPage(drivers)
        # 获取当天日期
        today = Base(drivers).get_datetime_today()
        last_date = export.get_last_day(7)
        """按销售单创建日期、Status条件筛选销售单"""
        export.click_sales_order_unfold()
        export.input_status_query('Delivered')
        export.list_input_create_date(last_date, today)
        export.click_search()

        """点击导出按钮"""
        export.click_more_option()
        export.click_export_detail()
        export.click_download_more()
        """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
        export.input_task_name('Sales Order Detail')
        export.export_record_create_date_query(today)
        down_status = export.click_export_search()
        file_size = export.get_file_size_text()
        export_time = export.get_export_time_text()
        export.assert_file_time_size(file_size, export_time)
        export.assert_sales_order_field('Download Status', down_status)
        export.assert_sales_order_field('Task Name', 'Sales Order Detail')
        export.assert_sales_order_field('User ID', 'lhmadmin')
        export.assert_sales_order_field('Create Date', today)
        export.assert_sales_order_field('Completed Date', today)
        export.assert_sales_order_field('Operation', 'Download')
        #export.click_close_export_record()
        #export.click_close_sales_order()


@allure.feature("销售管理-销售单")
class TestQuerySalesOrder:
    @allure.story("查询销售单")
    @allure.title("销售单页面，各个条件进行筛选销售单")
    @allure.description("销售单页面，在各个条件下筛选销售单，筛选条件和列表查询结果一致")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_001(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-打开销售单菜单"""
        user.click_gotomenu("Sales Management", "Sales Order")
        page = SalesOrderPage(drivers)
        page.click_unfold()
        """按销售单创建日期、Status条件筛选销售单"""
        page.search_sales_status('Delivered')
        page.click_search()
        result_data = page.get_table_txt(4)
        ValueAssert.value_assert_In('Delivered', result_data)
        page.click_reset()

        """按销售单创建日期、Buyer条件筛选销售单"""
        page.search_sales_buyer('zhaoerdai2')
        page.list_input_create_date('2022-08-15','2022-08-18')
        page.click_search()
        result_data = page.get_table_txt(21)
        ValueAssert.value_assert_In('zhaoerdai2', result_data)
        sleep(4)
        page.click_reset()

        """按销售单创建日期、seller条件筛选销售单"""
        page.search_sales_seller('zhaoguobao1')
        page.list_input_create_date('2022-08-15','2022-08-18')
        page.click_search()
        result_data = page.get_table_txt(18)
        ValueAssert.value_assert_In('zhaoguobao1', result_data)
        page.click_reset()

        """按销售单创建日期、brand条件筛选销售单"""
        page.list_input_create_date('2022-11-25', '2022-11-25')
        page.search_brand('TECNO')
        page.click_search()
        result_data = page.get_table_txt(10)
        ValueAssert.value_assert_In('TECNO', result_data)
        page.click_reset()

        """按销售单创建日期、model条件筛选销售单"""
        page.list_input_create_date('2022-11-25', '2022-11-25')
        page.click_material()              #点击取消日期弹出框
        page.search_model('KF8')
        page.click_search()
        result_data = page.get_table_txt(7)
        ValueAssert.value_assert_In('KF8', result_data)
        page.click_reset()

        """按销售单创建日期、MarketName条件筛选销售单"""
        page.list_input_create_date('2022-11-25', '2022-11-25')
        page.click_material()              #点击取消日期弹出框
        page.search_market('ACE 2N')
        page.click_search()
        result_data = page.get_table_txt(9)
        ValueAssert.value_assert_In('ACE 2N', result_data)
        page.click_reset()

        """按销售单创建日期、创建人筛选销售单"""
        page.list_input_create_date('2022-08-17', '2022-08-17')
        page.click_material()              #点击取消日期弹出框
        page.search_creator('xiongbo92')
        page.click_search()
        result_data = page.get_table_txt(24)
        ValueAssert.value_assert_In('xiongbo92', result_data)
        page.click_reset()

        """按销售单创建日期、订单类型筛选销售单"""
        page.list_input_create_date('2022-11-25', '2022-11-25')
        page.click_material()              #点击取消日期弹出框
        page.search_type('Purchase Order')
        page.click_search()
        result_data = page.get_table_txt(26)
        ValueAssert.value_assert_In('Purchase Order', result_data)
        page.click_reset()


    @allure.story("查询销售单")
    @allure.title("销售单页面，物料和丢失激活条件进行筛选销售单")
    @allure.description("销售单页面，在物料和丢失激活条件下筛选销售单，筛选条件和列表查询结果一致")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_002(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-打开销售单菜单"""
        user.click_gotomenu("Sales Management", "Sales Order")
        page = SalesOrderPage(drivers)
        page.click_unfold()

        """按销售单创建日期、物料ID条件筛选销售单"""
        page.search_material('11001953')
        page.list_input_create_date('2022-11-25', '2022-11-25')
        page.click_search()
        page.click_imei_detail()
        result_data = page.get_detail_txt(2)
        ValueAssert.value_assert_In('11001953', result_data)
        page.click_reset()

        """按销售单创建日期、是否丢失激活筛选销售单"""
        page.list_input_create_date('2022-06-08', '2022-06-09')
        page.click_material()              #点击取消日期弹出框
        page.search_active('Yes')
        page.click_search()
        result_data = page.get_table_txt(20)
        ValueAssert.value_assert_In('System virtual customer', result_data)
        page.click_reset()

        """按销售单创建日期、买家类型筛选销售单"""
        page.list_input_create_date('2022-11-25', '2022-11-25')
        page.click_material()              #点击取消日期弹出框
        page.search_buyer_type('Retailer')
        page.click_search()
        result_data = page.get_table_txt(22)
        ValueAssert.value_assert_In('Retailer', result_data)
        page.click_reset()

        """按销售单创建日期、卖家类型筛选销售单"""
        page.list_input_create_date('2022-11-25', '2022-11-25')
        page.click_material()              #点击取消日期弹出框
        page.search_seller_type('Sub-dealer')
        page.click_search()
        result_data = page.get_table_txt(19)
        ValueAssert.value_assert_In('Sub-dealer', result_data)
        page.click_reset()


if __name__ == '__main__':
    pytest.main(['SalesManagement_SalesOrder.py'])
