from project.DCR.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from project.DCR.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.Center_Process import SalesOrderPage
from project.DCR.page_object.PurchaseManagement_InboundReceipt import InboundReceiptPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
from libs.common.connect_sql import *
import datetime
import logging
import pytest
import allure


"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_view_fixture(drivers):
    yield
    close = DeliveryOrderPage(drivers)
    close.click_close_imei_detail()
    close.click_close_delivery_order()

@pytest.fixture(scope='function')
def function_export_fixture(drivers):
    yield
    close = DeliveryOrderPage(drivers)
    close.click_close_export_record()
    close.click_close_delivery_order()

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("销售管理-出库单")
class TestQueryDeliveryOrder:
    @allure.story("查询出库单列表")
    @allure.title("出库单页面，查询出库单列表加载数据")
    @allure.description("出库单页面，查询出库单列表加载数据正常，断言查询的出库单数据是否加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD40344201", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Delivery Order")

        list1 = DeliveryOrderPage(drivers)
        sale_order = list1.text_sales_order()
        deli_order = list1.text_delivery_order()
        deli_date = list1.get_delivery_date_text()
        status = list1.text_delivery_Status()
        total = list1.get_total_text()

        ValueAssert.value_assert_IsNoneNot(sale_order)
        ValueAssert.value_assert_IsNoneNot(deli_order)
        ValueAssert.value_assert_IsNoneNot(deli_date)
        ValueAssert.value_assert_IsNoneNot(status)
        list1.assert_total(total)
        #list1.click_close_delivery_order()


@allure.feature("销售管理-出库单")
class TestViewDeliveryIMEIDetails:
    @allure.story("查看出库单IMEI详情")
    @allure.title("国包用户，查看出库单IMEI详情")
    @allure.description("国包用户，查看出库单IMEI详情")
    @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_view_fixture')
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
        detail_title_sale = imei_detail.get_detail_title_delivery_id_text()
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
        #imei_detail.click_close_imei_detail()
        #imei_detail.click_close_delivery_order()


@allure.feature("销售管理-出库单")
class TestExportDeliveryOrder:
    @allure.story("导出筛选的出库单")
    @allure.title("出库单页面，导出筛选的出库单记录")
    @allure.description("出库单页面，筛选出库单记录后，导出筛选的出库单记录")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
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
        #export.click_close_export_record()
        #export.click_close_delivery_order()


@allure.feature("销售管理-出库单")
class TestAddDeliveryOrder:
    @allure.story("新建出库单")
    @allure.title("国包用户，新建出库单，产品为无码的，买方为临时客户")
    @allure.description("国包用户，新建出库单，产品为无码时，买方为临时客户")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_001(self, drivers):
        user3 = LoginPage(drivers)
        user3.initialize_login(drivers, "EG40052202", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user3.click_gotomenu("Sales Management", "Delivery Order")

        add = DeliveryOrderPage(drivers)
        num = add.customer_random()
        add.click_add()
        add.click_temporary_customer()
        add.input_deli_pay_mode("Wechat")
        add.input_temporary_customer_name("lhmcustomer" + num)
        add.input_customer_contact_no("13873094" + num)
        add.click_business_type('Retail&Wholesale')

        add.click_quantity_radio_button()
        add.click_quantity_add()
        add.click_quantity_product("OEP-E22")
        add.input_delivery_quantity("1")
        get_deli_quantity = add.get_delivery_quantity_text()
        ValueAssert.value_assert_equal(get_deli_quantity, "1")
        add.click_delivery_quantity_text()

        """点击Submit提交按钮"""
        add.click_submit()

        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        dom = DomAssert(drivers)
        dom.assert_att("Submit successfully")
        sleep(1)
        add.click_search()
        """断言查询新建的无码出库单"""
        user = SQL('DCR', 'test')
        varsql1 = "select order_code,delivery_code from t_channel_delivery_ticket where warehouse_id='61735' and seller_id='1596874516539127' and status=80200001 order by created_time desc limit 1"
        result = user.query_db(varsql1)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        logging.info("打印查询数据库销售单号order_code{}".format(order_code))
        logging.info("打印查询数据库出库单号delivery_code{}".format(delivery_code))

        """出库单页面，筛选新建的无码出库单ID"""
        add.input_salesorder(order_code)
        add.input_deliveryorder(delivery_code)
        add.click_search()

        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        get_salesorder = add.text_sales_order()
        get_deliveryorder = add.text_delivery_order()
        get_status = add.text_delivery_Status()

        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(get_salesorder, order_code)
        ValueAssert.value_assert_equal(get_deliveryorder, delivery_code)
        ValueAssert.value_assert_equal("Goods Receipt", get_status)
        #add.click_close_delivery_order()


    @allure.story("新建出库单")
    @allure.title("国包用户，新建出库单，产品为有码的，买方为临时客户,卖家退货单")
    @allure.description("国包用户，新建出库单，产品为有码的，买方为临时客户,卖家创建退货单")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_002(self, drivers):
        user4 = LoginPage(drivers)
        user4.initialize_login(drivers, "BD40344201", "dcr123456")

        """打开Report Analysis->IMEI Inventory Query菜单"""
        user4.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        """调用菜单栏，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        delivery = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        imei = delivery.get_text_imei_inventory()
        logging.info("打印获取IMEI Inventory Query页面的IMEI:{}".format(imei))
        delivery.click_close_imei_inventory()

        """ 刷新页面 """
        delivery.click_refresh(drivers)
        """打开销售管理-打开出库单页面"""
        user4.click_gotomenu("Sales Management", "Delivery Order")

        add = DeliveryOrderPage(drivers)
        num = add.customer_random()
        add.click_add()
        add.click_temporary_customer()
        add.input_deli_pay_mode("Wechat")
        add.input_temporary_customer_name("lhmcustomer" + num)
        add.input_customer_contact_no("13873094" + num)
        add.click_business_type('Retail&Wholesale')
        add.input_imei(imei)
        add.click_check()
        """断言检查出库单数量是否一致,扫码IMEI是否加载正确，是否有Success提示"""
        get_success = add.get_Deli_Scan_Record_Success()
        ValueAssert.value_assert_equal(get_success, "Success")
        get_imei = add.get_Deli_Scan_Record_IMEI(imei)
        ValueAssert.value_assert_equal(get_imei, imei)
        get_deli_quantity = add.get_delivery_quantity()
        get_order_deli_quantity = add.get_order_detail_deli_quantity()
        ValueAssert.value_assert_equal(get_deli_quantity, get_order_deli_quantity)

        """点击提交按钮"""
        add.click_submit()
        """点击提交后，盘点是否有弹出确认价格提示框，如果没有就执行except下面的语句，直接提交成功，断言是否有成功提示语"""
        try:
            affirm = add.get_text_submit_affirm()
            if affirm == "Submit":
                add.click_submit_affirm()
                DomAssert(drivers).assert_att("Submit successfully")
        except Exception as e:
            logging.info("打印日志{}".format(e))
        sleep(1)
        add.click_search()
        """断言查询新建的无码出库单"""
        sql2 = SQL('DCR', 'test')
        varsql2 = "select * from  t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667'  and status=80200001 order by created_time desc limit 1"
        result = sql2.query_db(varsql2)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        logging.info("打印数据库查询的销售单ID order_code{}".format(order_code))
        logging.info("打印数据库查询的出库单ID delivery_code{}".format(delivery_code))

        """出库单页面，筛选新建的无码出库单ID"""
        add.input_salesorder(order_code)
        add.input_deliveryorder(delivery_code)
        add.click_search()

        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        get_salesorder = add.text_sales_order()
        get_deliveryorder = add.text_delivery_order()
        get_status = add.text_delivery_Status()

        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(get_salesorder, order_code)
        ValueAssert.value_assert_equal(get_deliveryorder, delivery_code)
        ValueAssert.value_assert_equal("Goods Receipt", get_status)
        add.click_close_delivery_order()


        """卖家创建退货单，退货类型为Return To Seller、退有码产品，输入Delivery Order出库单ID整单退货"""
        base = Base(drivers)
        base.refresh()
        """打开销售管理-打开出库单页面"""
        user4.click_gotomenu("Sales Management", "Return Order")
        return_order = ReturnOrderPage(drivers)

        return_order.click_Add()
        return_order.click_Return_Type()
        return_order.radio_Delivery_order()
        return_order.input_Delivery_order(delivery_code)
        return_order.click_Check()

        """点击check按钮后，断言加载出库单信息，获取检查Scan Record结果与 Order Detail列表下出库单记录是否加载正常"""
        record = return_order.get_text_Record()
        ValueAssert.value_assert_equal("Success", record)
        delivery_order_id = return_order.get_Order_Detail_Deli_Order_ID()
        seller_id = return_order.get_Order_Detail_Seller_ID()
        buyer_id = return_order.get_Order_Detail_Buyer_ID()
        return_quantity = return_order.get_Order_Detail_Return_Quantity()

        ValueAssert.value_assert_equal(delivery_order_id, delivery_code)
        ValueAssert.value_assert_equal(seller_id, "BD403442")
        ValueAssert.value_assert_IsNoneNot(buyer_id)
        ValueAssert.value_assert_equal(return_quantity, "1")

        """点击提交按钮"""
        return_order.click_Submit()
        dom = DomAssert(drivers)
        dom.assert_att("Submit Success!")

        """退货单页面，根据出库单ID查询 是否生成一条Return Order ID 退货单"""
        return_order.input_Delivery_Orderid(delivery_code)
        return_order.click_Search()

        """断言筛选退货列表页，获取退货单ID、退货出库单ID、退货状态与数据库表中查询的出库单ID对比是否一致"""
        get_return_order_id = return_order.get_list_return_order_id()
        ValueAssert.value_assert_IsNoneNot(get_return_order_id)
        get_delivery_order_id = return_order.get_text_deliveryID()
        get_status = return_order.get_return_status()
        ValueAssert.value_assert_equal(get_delivery_order_id, delivery_code)
        ValueAssert.value_assert_equal("Approved", get_status)
        #return_order.click_close_return_order()



    @allure.story("新建出库单")
    @allure.title("二代用户，新建出库单，出库类型为BoxID，买方为零售商有多个门店，转零售商库存")
    @allure.description("二代用户，新建出库单，出库类型为BoxID，买方为零售商有多个门店，转零售商库存，卖家退货")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor  43012202214859
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_003(self, drivers):
        user5 = LoginPage(drivers)
        user5.initialize_login(drivers, "BD291501", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user5.click_gotomenu("Sales Management", "Delivery Order")
        add_delivery = DeliveryOrderPage(drivers)
        add_delivery.create_delivery_order('EG000562', 'Wechat', '43012211021179')
        """断言Check后，列表展示的出库单校验成功的记录"""
        get_deli_scan_record = add_delivery.get_Deli_Scan_Record_Success()
        ValueAssert.value_assert_equal('Success', get_deli_scan_record)
        """断言 获取出库数量是否正确"""
        get_deli_quantity = add_delivery.get_delivery_quantity_text()
        logging.info("打印获取检查后的出库数量：{}".format(get_deli_quantity))
        ValueAssert.value_assert_equal('10', get_deli_quantity)
        """获取创建出库单，点击check后，Order Detail列表获取Product字段"""
        get_deli_order_detail_product = add_delivery.get_delivery_order_detail_product()

        """"点击提交按钮"""
        add_delivery.click_submit()
        """点击提交后，盘点是否有弹出确认价格提示框，如果没有就执行except下面的语句，直接提交成功，断言是否有成功提示语"""
        try:
            affirm = add_delivery.get_text_submit_affirm()
            if affirm == "Submit":
                add_delivery.click_submit_affirm()
                DomAssert(drivers).assert_att("Submit successfully")
        except Exception as e:
            logging.info("打印日志{}".format(e))
        sleep(1)
        add_delivery.click_search()
        """"后端断言，创建出库单成功后，查询数据库表是否新增出库单记录"""
        order_code, delivery_code = add_delivery.select_sql_delivery_order('62134', '1596874516539662', '1596874516539668')
        """出库单页面，筛选新建的无码出库单ID"""
        add_delivery.query_delivery_order(order_code, delivery_code)
        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        get_sales_order = add_delivery.text_sales_order()
        get_delivery_order = add_delivery.text_delivery_order()
        get_status = add_delivery.text_delivery_Status()
        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(get_sales_order, order_code)
        ValueAssert.value_assert_equal(get_delivery_order, delivery_code)
        ValueAssert.value_assert_equal("On Transit", get_status)
        user5.click_close_open_menu()


        """ 断言 新建出库单成功后，检查Sales Order页面，能生成一条对应的销售单，打开IMEI Detail详情页断言"""
        Base(drivers).refresh()
        """打开Purchase Management菜单"""
        user5.click_gotomenu("Sales Management", "Sales Order")
        query_sales = SalesOrderPage(drivers)
        query_sales.input_sales_order_ID(order_code)
        query_sales.click_search()
        get_sales_order = query_sales.get_text_sales_id()
        """断言列表Status 是否是Delivered状态 """
        get_status = query_sales.get_sales_status_text("Delivered")
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        ValueAssert.value_assert_equal(order_code, get_sales_order)
        ValueAssert.value_assert_equal('Delivered', get_status)
        """在Sales Order页面，打开IMEI Detail详情页，断言详情信息是否与出库单IMEI一致"""
        query_sales.click_sales_order_imei_detail()
        get_imei_detail_product = query_sales.get_list_field_text('Get Sales IMEI Detail Product')
        get_imei_detail_brand = query_sales.get_list_field_text('Get Sales IMEI Detail Brand')
        get_imei_detail_total = query_sales.get_sales_imei_detail_total()
        ValueAssert.value_assert_equal(get_deli_order_detail_product, get_imei_detail_product)
        ValueAssert.value_assert_equal('TECNO', get_imei_detail_brand)
        ValueAssert.value_assert_equal(get_deli_quantity, get_imei_detail_total)
        """关闭IMEI Detail详情页"""
        query_sales.close_sales_order_imei_detail()
        """关闭销售单页面"""
        user5.click_close_open_menu()


        """ 零售商EG00056201账号登录， 进行快速收货 """
        user5.initialize_login(drivers, "EG00056201", "dcr123456")
        """打开采购单Purchase Management菜单"""
        user5.click_gotomenu("Purchase Management", "Inbound Receipt")
        receipt = InboundReceiptPage(drivers)
        """查询最近新建的销售单ID与出库单ID,进行快速收货操作"""
        receipt.inbound_quick_received(order_code, delivery_code)
        """断言 获取快速收货弹出页面，Order ID与 Quantity字段内容是否匹配一致"""
        get_order_id = receipt.get_list_field_text('Get Quick Received Order ID')
        get_received_quantity = receipt.get_list_field_text('Get Quick Received Quantity')
        ValueAssert.value_assert_equal(order_code, get_order_id)
        ValueAssert.value_assert_equal(get_deli_quantity, get_received_quantity)
        """"点击保存按钮"""
        receipt.click_save()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        DomAssert(drivers).assert_att("Successfully")
        sleep(1)
        """获取列表Status字段内容"""
        status = receipt.text_status()
        """二代收货页面，验证收货后Status：显示GoodsReceipt状态，匹配一致"""
        ValueAssert.value_assert_equal('Goods Receipt', status)
        """点击IMEI Detail查看详情信息"""
        receipt.select_checkbox()
        receipt.click_imei_detail()
        """断言 订单号与 IMEI数量是否匹配"""
        get_dn_title = receipt.get_list_field_text('Get DN Delivery Order ID')
        #get_total = receipt.get_imei_detail_total('Get IMEI Detail Total')
        logging.info("打印详情页DN标题的出库单ID:{}".format(get_dn_title))
        #ValueAssert.value_assert_equal(get_deli_quantity, get_total)
        ValueAssert.value_assert_In(delivery_code, get_dn_title)
        """关闭详情页面"""
        receipt.click_close_inbound_imei_detail()
        """关闭收货页面"""
        user5.click_close_open_menu()


        """断言收货成功后，IMEI Inventory Query列表，根据Box ID条件查询，Box ID是否入库"""
        Base(drivers).refresh()
        user5.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        box_id = SalesOrderPage(drivers)
        """IMEI Inventory Query页面,根据box id筛选是否存在箱号记录"""
        box_id.query_inventory_box_id('43012211021179')
        """断言 IMEI Inventory Query列表，box_id是否正确，Total 总IMEI条数是否与出库数量一致"""
        get_box_id = box_id.get_list_box_id_text()
        ValueAssert.value_assert_equal('43012211021179', get_box_id)
        logging.info("打印获取IMEI Inventory Query页面的Box ID:{}".format(get_box_id))
        get_list_total = box_id.get_inventory_list_total()
        ValueAssert.value_assert_equal(get_deli_quantity, get_list_total)
        """"关闭IMEI inventory Query页面"""
        user5.click_close_open_menu()


        """零售商EG00056201账号, 进行退货操作"""
        Base(drivers).refresh()
        """打开Purchase Management菜单"""
        user5.click_gotomenu("Sales Management", "Return Order")
        """实例化 二代退货单类"""
        return_order = ReturnOrderPage(drivers)
        return_order.add_return_order_box_sn_imei('43012211021179')
        record = return_order.get_text_Record()
        get_scanned = return_order.get_scanned_number()
        ValueAssert.value_assert_equal("Success", record)
        ValueAssert.value_assert_equal(get_deli_quantity, get_scanned)
        return_order.click_Submit()
        """断言页面是否存在提交成功 Submit Success!文本"""
        DomAssert(drivers).assert_att("Submit Success!")
        """根据出库单号，查询退货单记录，进行断言"""
        return_order.query_return_order(delivery_code)
        """筛选退货列表页，获取退货出库单ID文本 与数据库表中查询的出库单ID对比是否一致"""
        delivery_orderid = return_order.get_text_deliveryID()
        status = return_order.get_return_status()
        ValueAssert.value_assert_equal(delivery_orderid, delivery_code)
        ValueAssert.value_assert_equal("Pending Approval", status)
        """关闭退货页面"""
        user5.click_close_open_menu()


        """退货单列表页面，二代账号, 进行审核退货单操作"""
        user5.initialize_login(drivers, "BD291501", "dcr123456")
        """打开Purchase Management菜单"""
        user5.click_gotomenu("Sales Management", "Return Order")
        """实例化 Return order退货单类"""
        return_approve = ReturnOrderPage(drivers)
        """查询二代账号，最近新建的出库单ID"""
        return_approve.approve_return_order(delivery_code)
        """ 断言页面是否存在审核成功Approval successfully文本 """
        DomAssert(drivers).assert_att("Approval successfully")
        """退货成功后，获取列表第一个状态，断言判断是否审核成功"""
        status = return_approve.get_text_Status()
        get_return_type =return_approve.get_list_return_type()
        ValueAssert.value_assert_equal("Approved", status)
        ValueAssert.value_assert_equal('Return To Seller', get_return_type)
        """关闭退货页面"""
        user5.click_close_open_menu()


        """断言 Delivery Order页面，筛选退货成功的出库单，获取产品与Return Quantity字段内容变红色，退货数量显示正确"""
        Base(drivers).refresh()
        user5.click_gotomenu("Sales Management", "Delivery Order")
        """出库单页面，筛选新建的无码出库单ID"""
        add_delivery.query_delivery_order(order_code, delivery_code)
        """断言获取出库单列表，出库数量与退货数量是否匹配一致"""
        get_delivery_quantity = add_delivery.get_list_field_text('Get list Delivery Quantity')
        get_return_quantity = add_delivery.get_list_field_text('Get list Return Quantity')
        ValueAssert.value_assert_equal(get_deli_quantity, get_delivery_quantity)
        ValueAssert.value_assert_equal(get_deli_quantity, get_return_quantity)
        """断言获取出库单列表，产品、出库数量与退货数量字段 是否为红色"""
        product_color = add_delivery.get_field_style_color('Get list Product text')
        return_quantity_color = add_delivery.get_field_style_color('Get list Product text')
        logging.info("打印获取出库单列表，产品字段内容颜色:{}".format(product_color))
        ValueAssert.value_assert_In('color: red', product_color)
        ValueAssert.value_assert_In('color: red', return_quantity_color)
        """关闭出库单页面"""
        user5.click_close_open_menu()


        """断言打开卖家 IMEI Inventory Query页面，根据Box ID条件查询，Box ID是否回到IMEI Inventory Query列表"""
        Base(drivers).refresh()
        user5.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        """IMEI Inventory Query页面 根据box id筛选是否存在箱号记录"""
        box_id.query_inventory_box_id('43012211021179')
        """断言 IMEI Inventory Query列表，box_id是否正确，Total 总IMEI条数是否与出库数量一致"""
        get_box_id = box_id.get_list_box_id_text()
        ValueAssert.value_assert_equal('43012211021179', get_box_id)
        logging.info("打印获取IMEI Inventory Query页面的Box ID:{}".format(get_box_id))
        get_list_total = box_id.get_inventory_list_total()
        ValueAssert.value_assert_equal(get_deli_quantity, get_list_total)


    @allure.story("新建出库单")
    @allure.title("二代用户，新建出库单，出库类型为IMEI，买方为零售商有只有一个门店，自动转门店销量")
    @allure.description("二代用户，新建出库单，出库类型为IMEI，买方为零售商只有一个门店，自动转门店销量，卖家退货")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor  43012202214859
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_004(self, drivers):
        user5 = LoginPage(drivers)
        user5.initialize_login(drivers, "NG2061301", "dcr123456")
        """打开IMEI Inventory Query菜单"""
        user5.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        process = SalesOrderPage(drivers)
        """根据指定仓库、Brand、Activated 条件筛选库存IMEI"""
        process.imei_inventory_query_imei2('WNG2061304 NG2061303', 'TECNO', 'Yes')
        get_imei1 = process.get_text_imei_inventory()
        get_imei2 = process.get_text_imei_inventory2()
        logging.info("打印获取IMEI Inventory Query页面的IMEI:{}".format(get_imei1, get_imei2))
        user5.click_close_open_menu()


        """打开销售管理-打开出库单页面"""
        Base(drivers).refresh()
        add_delivery = DeliveryOrderPage(drivers)
        """打开销售管理-打开出库单页面"""
        user5.click_gotomenu("Sales Management", "Delivery Order")
        add_delivery.create_delivery_order_many_imei('NG2061303 WNG2061304', 'EG400000', 'Online', get_imei1, get_imei2)
        """断言Check后，列表展示的出库单校验成功的记录"""
        get_deli_scan_record = add_delivery.get_Deli_Scan_Record_Success()
        ValueAssert.value_assert_equal('Success', get_deli_scan_record)
        """断言 获取出库数量是否正确"""
        get_deli_quantity = add_delivery.get_delivery_quantity_text()
        logging.info("打印获取检查后的出库数量：{}".format(get_deli_quantity))
        ValueAssert.value_assert_equal('2', get_deli_quantity)
        """"点击提交按钮"""
        add_delivery.click_submit()
        """点击提交后，盘点是否有弹出确认价格提示框，如果没有就执行except下面的语句，直接提交成功，断言是否有成功提示语"""
        try:
            affirm = add_delivery.get_text_submit_affirm()
            if affirm == "Submit":
                add_delivery.click_submit_affirm()
                DomAssert(drivers).assert_att("Submit successfully")
        except Exception as e:
            logging.info("打印日志{}".format(e))
        sleep(1)
        add_delivery.click_search()
        """"后端断言，创建出库单成功后，查询数据库表是否新增出库单记录"""
        order_code, delivery_code = add_delivery.select_sql_delivery_order('78787', '1596874516539550', '1796874516566507')
        """出库单页面，筛选新建的无码出库单ID"""
        add_delivery.query_delivery_order(order_code, delivery_code)
        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        get_sales_order = add_delivery.text_sales_order()
        get_delivery_order = add_delivery.text_delivery_order()
        get_status = add_delivery.text_delivery_Status()
        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(get_sales_order, order_code)
        ValueAssert.value_assert_equal(get_delivery_order, delivery_code)
        ValueAssert.value_assert_equal("On Transit", get_status)
        user5.click_close_open_menu()


        """ 零售商lhmtest2022账号登录， 进行快速收货 """
        user5.initialize_login(drivers, "lhmtest2022", "dcr123456")
        """打开采购单Purchase Management菜单"""
        user5.click_gotomenu("Purchase Management", "Inbound Receipt")
        receipt = InboundReceiptPage(drivers)
        """查询最近新建的销售单ID与出库单ID,进行快速收货操作"""
        receipt.inbound_quick_received(order_code, delivery_code)
        """断言 获取快速收货弹出页面，Order ID与 Quantity字段内容是否匹配一致"""
        get_order_id = receipt.get_list_field_text('Get Quick Received Order ID')
        ValueAssert.value_assert_equal(order_code, get_order_id)
        """"点击保存按钮"""
        receipt.click_save()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        DomAssert(drivers).assert_att("Successfully")
        sleep(1.5)
        """获取列表Status字段内容"""
        status = receipt.text_status()
        """二代收货页面，验证收货后Status：显示GoodsReceipt状态，匹配一致"""
        ValueAssert.value_assert_equal('Goods Receipt', status)
        """关闭收货页面"""
        user5.click_close_open_menu()


        """断言收货成功后，Shop Purchase Query列表，根据IMEI条件查询，IMEI是否入Shop Purchase Query页面"""
        Base(drivers).refresh()
        user5.click_gotomenu("Purchase Management", "Shop Purchase Query")
        """根据IMEI筛选是否存记录,断言Shop Sales Query列表，字段内容是否正确，Total条数是否与筛选的IMEI一致"""
        process.shop_purchase_query_imei(get_imei1)
        get_total = process.shop_sales_assert_total()
        get_shop_id = process.get_list_field_text('Get Shop Purchase list Shop ID')
        ValueAssert.value_assert_equal('1', get_total)
        logging.info("打印Shop Purchase Query列表total：{}".format(get_total))
        ValueAssert.value_assert_equal('SN001872', get_shop_id)
        """"关闭Shop Purchase Query页面"""
        user5.click_close_open_menu()


        """断言收货成功后，Shop Sales Query列表，根据IMEI条件查询，IMEI是否入Shop Sales Query页面"""
        Base(drivers).refresh()
        user5.click_gotomenu("Sales Management", "Shop Sales Query")
        """根据IMEI筛选是否存记录,断言Shop Sales Query列表，字段内容是否正确，Total条数是否与筛选的IMEI一致"""
        process.shop_sales_query_imei(get_imei1)
        get_total = process.shop_sales_assert_total()
        ValueAssert.value_assert_equal('1', get_total)
        #get_shop_id = process.get_list_field_text('Get Shop Sales list Shop ID')
        #ValueAssert.value_assert_equal('SN001872', get_shop_id)
        """然后删除需要退货的IMEI，首先删除Shop Sales Query页面IMEI"""
        process.shop_sales_query_delete()
        DomAssert(drivers).assert_att('Deleted Successfully')
        """"关闭Shop Sales Query页面"""
        user5.click_close_open_menu()


        """Shop Purchase Query列表，筛选IMEI，然后Cancel取消 IMEI"""
        Base(drivers).refresh()
        user5.click_gotomenu("Purchase Management", "Shop Purchase Query")
        process.shop_purchase_query_imei(get_imei1)
        process.shop_purchase_query_cancel()
        DomAssert(drivers).assert_att('Cancel success')
        get_status = process.get_list_field_text('Get Shop Purchase list Status')
        ValueAssert.value_assert_equal('Canceled', get_status)
        """"关闭Shop Purchase Query页面"""
        user5.click_close_open_menu()


        """打开MEI Inventory Query菜单, 查看门店采购查询页面，删除的IMEI，是否转入渠道IMEI库存页面"""
        Base(drivers).refresh()
        user5.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        process.imei_inventory_query_imei(get_imei1)
        get_list_imei = process.get_list_field_text('获取IMEI文本内容1')
        ValueAssert.value_assert_equal(get_list_imei, get_imei1)
        """"关闭Shop Purchase Query页面"""
        user5.click_close_open_menu()


        """零售商进行退货操作"""
        Base(drivers).refresh()
        """打开Purchase Management菜单"""
        user5.click_gotomenu("Sales Management", "Return Order")
        """实例化 二代退货单类"""
        return_order = ReturnOrderPage(drivers)
        return_order.add_return_order_box_sn_imei(get_imei1)
        record = return_order.get_text_Record()
        ValueAssert.value_assert_equal("Success", record)
        """点击提交按钮"""
        return_order.click_Submit()
        """断言页面是否存在提交成功 Submit Success!文本"""
        DomAssert(drivers).assert_att("Submit Success!")
        """关闭退货页面"""
        user5.click_close_open_menu()


        """退货单列表页面，二代账号, 进行审核退货单操作"""
        user5.initialize_login(drivers, "NG2061301", "dcr123456")
        """打开Purchase Management菜单"""
        user5.click_gotomenu("Sales Management", "Return Order")
        """查询二代账号，最近新建的出库单ID"""
        return_order.approve_return_order(delivery_code)
        """ 断言页面是否存在审核成功Approval successfully文本 """
        DomAssert(drivers).assert_att("Approval successfully")
        """退货成功后，获取列表第一个状态，断言判断是否审核成功"""
        status = return_order.get_text_Status()
        get_return_type = return_order.get_list_return_type()
        ValueAssert.value_assert_equal("Approved", status)
        ValueAssert.value_assert_equal('Return To Seller', get_return_type)


    @allure.story("新建出库单")
    @allure.title("二代用户，新建出库单，出库类型为IMEI，买方为零售商只有一个门店，自动转门店库存")
    @allure.description("二代用户，新建出库单，出库类型为IMEI，买方为零售商只有一个门店，自动转门店库存，卖家退货")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_005(self, drivers):
        user5 = LoginPage(drivers)
        user5.initialize_login(drivers, "NG2061301", "dcr123456")
        """打开IMEI Inventory Query菜单"""
        user5.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        process = SalesOrderPage(drivers)
        """根据指定仓库、Brand、Activated 条件筛选库存IMEI"""
        process.imei_inventory_query_imei2('WNG2061304 NG2061303', 'TECNO', 'Yes')
        get_imei1 = process.get_text_imei_inventory()
        logging.info("打印获取IMEI Inventory Query页面的IMEI:{}".format(get_imei1))
        user5.click_close_open_menu()


        """打开销售管理-打开出库单页面"""
        Base(drivers).refresh()
        add_delivery = DeliveryOrderPage(drivers)
        """打开销售管理-打开出库单页面"""
        user5.click_gotomenu("Sales Management", "Delivery Order")
        add_delivery.create_delivery_order_imei('NG2061303 WNG2061304', 'SN001868', 'Online', get_imei1)
        """断言Check后，列表展示的出库单校验成功的记录"""
        get_deli_scan_record = add_delivery.get_Deli_Scan_Record_Success()
        ValueAssert.value_assert_equal('Success', get_deli_scan_record)
        """断言 获取出库数量是否正确"""
        get_deli_quantity = add_delivery.get_delivery_quantity_text()
        logging.info("打印获取检查后的出库数量：{}".format(get_deli_quantity))
        ValueAssert.value_assert_equal('1', get_deli_quantity)
        """"点击提交按钮"""
        add_delivery.click_submit()
        """点击提交后，盘点是否有弹出确认价格提示框，如果没有就执行except下面的语句，直接提交成功，断言是否有成功提示语"""
        try:
            affirm = add_delivery.get_text_submit_affirm()
            if affirm == "Submit":
                add_delivery.click_submit_affirm()
                DomAssert(drivers).assert_att("Submit successfully")
        except Exception as e:
            logging.info("打印日志{}".format(e))
        sleep(1)
        add_delivery.click_search()
        """"后端断言，创建出库单成功后，查询数据库表是否新增出库单记录"""
        sales_order, delivery_code = add_delivery.select_sql_delivery_order('78787', '1596874516539550', '1596874516539764')
        """出库单页面，筛选新建的无码出库单ID"""
        add_delivery.query_delivery_order(sales_order, delivery_code)
        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        get_sales_order = add_delivery.text_sales_order()
        get_delivery_order = add_delivery.text_delivery_order()
        get_deli_status = add_delivery.text_delivery_Status()
        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(get_sales_order, sales_order)
        ValueAssert.value_assert_equal(get_delivery_order, delivery_code)
        ValueAssert.value_assert_equal("On Transit", get_deli_status)
        user5.click_close_open_menu()


        """ 零售商SN00186801账号登录，进行快速收货 """
        user5.initialize_login(drivers, "SN00186801", "dcr123456")
        """打开采购单Purchase Management菜单"""
        user5.click_gotomenu("Purchase Management", "Inbound Receipt")
        receipt = InboundReceiptPage(drivers)
        """查询最近新建的销售单ID与出库单ID,进行快速收货操作"""
        receipt.inbound_quick_received(sales_order, delivery_code)
        """断言 获取快速收货弹出页面，Order ID与 Quantity字段内容是否匹配一致"""
        get_order_id = receipt.get_list_field_text('Get Quick Received Order ID')
        ValueAssert.value_assert_equal(delivery_code, get_order_id)
        """"点击保存按钮"""
        receipt.click_save()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        DomAssert(drivers).assert_att("Successfully")
        sleep(1.5)
        """获取列表Status字段内容"""
        status = receipt.text_status()
        """二代收货页面，验证收货后Status：显示GoodsReceipt状态，匹配一致"""
        ValueAssert.value_assert_equal('Goods Receipt', status)
        """关闭收货页面"""
        user5.click_close_open_menu()


        """打开 Shop Inventory IMEI Query菜单, 查看门店采购查询页面，删除的IMEI，是否转入渠道IMEI库存页面"""
        Base(drivers).refresh()
        user5.click_gotomenu("Report Analysis", "Shop Inventory IMEI Query")
        process.shop_inventory_imei_query_imei(get_imei1)
        get_list_imei = process.get_list_field_text('Get Shop Inventory IMEI list IMEI')
        get_shop_inventory_total = process.get_shop_inventory_imei_total()
        ValueAssert.value_assert_equal(get_list_imei, get_imei1)
        ValueAssert.value_assert_equal('1', get_shop_inventory_total)
        """"关闭Shop Purchase Query页面"""
        user5.click_close_open_menu()


        """Shop Purchase Query列表，筛选IMEI，然后Cancel取消 IMEI"""
        Base(drivers).refresh()
        user5.click_gotomenu("Purchase Management", "Shop Purchase Query")
        process.shop_purchase_query_imei(get_imei1)
        process.shop_purchase_query_cancel()
        DomAssert(drivers).assert_att('Cancel success')
        sleep(2)
        process.click_search()
        get_cancel_status = process.get_list_field_text('Get Shop Purchase list Status')
        ValueAssert.value_assert_equal('Canceled', get_cancel_status)
        """"关闭Shop Purchase Query页面"""
        user5.click_close_open_menu()


        """零售商进行退货操作"""
        Base(drivers).refresh()
        """打开Purchase Management菜单"""
        user5.click_gotomenu("Sales Management", "Return Order")
        """实例化 二代退货单类"""
        return_order = ReturnOrderPage(drivers)
        return_order.add_return_order_box_sn_imei(get_imei1)
        record = return_order.get_text_Record()
        ValueAssert.value_assert_equal("Success", record)
        """点击提交按钮"""
        return_order.click_Submit()
        """断言页面是否存在提交成功 Submit Success!文本"""
        DomAssert(drivers).assert_att("Submit Success!")
        """关闭退货页面"""
        user5.click_close_open_menu()


        """退货单列表页面，指定传音人员审核, 退货单操作"""
        user5.initialize_login(drivers, "186489011", "dcr123456")
        """打开Purchase Management菜单"""
        user5.click_gotomenu("Sales Management", "Return Order")
        """查询二代账号，最近新建的出库单ID"""
        return_order.approve_return_order(delivery_code)
        """ 断言页面是否存在审核成功Approval successfully文本 """
        DomAssert(drivers).assert_att("Approval successfully")
        """退货成功后，获取列表第一个状态，断言判断是否审核成功"""
        status = return_order.get_text_Status()
        get_return_type = return_order.get_list_return_type()
        ValueAssert.value_assert_equal("Approved", status)
        ValueAssert.value_assert_equal('Return To Seller', get_return_type)

    @allure.story("导入出库单")
    @allure.title("代理员工批量导入出库单")
    @allure.description("代理员工批量导入出库单")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    def test_004_006(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SN405554", "xLily6x")
        """打开Sales Management/Delivery Ordery菜单"""
        user = DeliveryOrderPage(drivers)
        user.click_menu("Sales Management", "Delivery Order")
        """导入出库单"""
        user.click_import()
        user.import_DeliveryOrdery_file('出库单导入成功.xlsx')
        user.assert_import_success()
        user.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        user.click_confirm()
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        """断言ImportRecord页面结果"""
        user.assert_Record_result('Import Record', '出库单导入成功.xlsx', 'Status', 'Upload Successfully')
        user.assert_Record_result('Import Record', '出库单导入成功.xlsx', 'Total', '2')
        user.assert_Record_result('Import Record', '出库单导入成功.xlsx', 'Success', '2')
        user.assert_Record_result('Import Record', '出库单导入成功.xlsx', 'Import Date', today)
        """断言ImportRecord页面结果"""
        user.click_menu("Sales Management", "Delivery Order")
        user.refresh()
        user.assert_first_info('Delivery Date', today)
        user.assert_first_info('Status', 'On Transit')
        user.assert_first_info('Product', 'SPARK Go 2021 32+2 MALDIVES BLUE')
        user.assert_first_info('Product', 'Vision 3 32+2 DEEOCE BLACK')
        OrderID = user.get_FirstRow_info('Delivery Order ID')
        """创建退货单退货"""
        user.click_menu("Sales Management", "Return Order")
        re = ReturnOrderPage(drivers)
        re.click_Add()
        re.radio_Delivery_order()
        re.input_Delivery_order(OrderID)
        re.click_Check()
        re.click_Submit()
        DomAssert(drivers).assert_att('Submit Success!')

    @allure.story("导入出库单")
    @allure.title("传音员工批量导入出库单")
    @allure.description("传音员工批量导入出库单")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    def test_004_007(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "18650493", "xLily6x")
        """打开Sales Management/Delivery Ordery菜单"""
        user = DeliveryOrderPage(drivers)
        user.click_menu("Sales Management", "Delivery Order")
        """导入出库单"""
        user.click_import()
        user.import_DeliveryOrdery_file('出库单导入成功.xlsx')
        user.assert_import_success()
        user.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        user.click_confirm()
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        """断言ImportRecord页面结果"""
        user.assert_Record_result('Import Record', '出库单导入成功.xlsx', 'Status', 'Upload Successfully')
        user.assert_Record_result('Import Record', '出库单导入成功.xlsx', 'Total', '2')
        user.assert_Record_result('Import Record', '出库单导入成功.xlsx', 'Success', '2')
        user.assert_Record_result('Import Record', '出库单导入成功.xlsx', 'Import Date', today)
        """断言ImportRecord页面结果"""
        user.click_menu("Sales Management", "Delivery Order")
        user.refresh()
        user.assert_first_info('Delivery Date', today)
        user.assert_first_info('Status', 'On Transit')
        user.assert_first_info('Product', 'SPARK Go 2021 32+2 MALDIVES BLUE')
        user.assert_first_info('Product', 'Vision 3 32+2 DEEOCE BLACK')
        OrderID = user.get_FirstRow_info('Delivery Order ID')
        """创建退货单退货"""
        user.click_menu("Sales Management", "Return Order")
        re = ReturnOrderPage(drivers)
        re.click_Add()
        re.radio_Delivery_order()
        re.input_Delivery_order(OrderID)
        re.click_Check()
        re.click_Submit()
        DomAssert(drivers).assert_att('Submit Success!')

    @allure.story("打印出库单")
    @allure.title("打印出库单，断言是否弹出打印页面")
    @allure.description("打印出库单，断言是否弹出打印页面")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    def test_004_008(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SN405554", "xLily6x")
        """打开Sales Management/Delivery Ordery菜单"""
        user = DeliveryOrderPage(drivers)
        user.click_menu("Sales Management", "Delivery Order")
        OrderID = user.get_FirstRow_info('Delivery Order ID')
        Date = user.get_FirstRow_info('Delivery Date')
        Product = user.get_FirstRow_info('Product')
        """断言print页面数据"""
        user.click_First_print()
        user.assert_print_content(OrderID)
        user.assert_print_content(Date)
        user.assert_print_content(Product)

    @allure.story("查询出库单")
    @allure.title("组合条件筛选出库单，筛选出正确数据")
    @allure.description("组合条件筛选出库单")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    def test_004_009(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SN405554", "xLily6x")
        """打开Sales Management/Delivery Ordery菜单"""
        user = DeliveryOrderPage(drivers)
        user.click_menu("Sales Management", "Delivery Order")
        user.click_unfold()
        user.input_search('Brand', 'itel')
        user.input_search('Sales Order ID', '02HK2211220003')
        user.input_search('Seller', 'SN405554')
        user.click_search()
        user.assert_Query_result('Sales Order ID', '02HK2211220003')
        user.assert_Query_result('Brand', 'itel')

    @allure.story("查询出库单")
    @allure.title("组合条件筛选出库单，无筛选结果")
    @allure.description("组合条件筛选出库单")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    def test_004_010(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SN405554", "xLily6x")
        """打开Sales Management/Delivery Ordery菜单"""
        user = DeliveryOrderPage(drivers)
        user.click_menu("Sales Management", "Delivery Order")
        user.click_unfold()
        user.input_search('Activated Loss Or Not', 'Yes')
        user.click_search()
        user.assert_NoData()

    @allure.story("新建出库单")
    @allure.title("国包用户，新建出库单，产品为有码的，出库类型为:SN，买方为二代用户")
    @allure.description("国包用户，新建出库单，产品为有码的，出库类型为:SN，买方为二代用户，买收货后，SN退货")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_006(self, drivers):
        user6 = LoginPage(drivers)
        user6.initialize_login(drivers, "IN40080501", "dcr123456")
        """打开IMEI Inventory Query菜单, 获取列表SN"""
        user6.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        process = SalesOrderPage(drivers)
        """根据Brand：itel appliances条件筛选库存SN"""
        process.imei_inventory_query_imei2('WIN400805 400805', 'itel appliances', 'No')
        get_sn1 = process.get_text_imei_inventory1()
        logging.info("打印获取IMEI Inventory Query页面的IMEI:{}".format(get_sn1))
        user6.click_close_open_menu()

        """打开出库单页面，新建出库单出库SN"""
        Base(drivers).refresh()
        add_delivery = DeliveryOrderPage(drivers)
        user6.click_gotomenu("Sales Management", "Delivery Order")
        add_delivery.create_delivery_order('NG20613', 'Wechat', get_sn1)
        """断言Check后，列表展示的出库单校验成功的记录"""
        get_deli_scan_record = add_delivery.get_Deli_Scan_Record_Success()
        ValueAssert.value_assert_equal('Success', get_deli_scan_record)
        """断言 获取出库数量是否正确"""
        get_deli_quantity = add_delivery.get_delivery_quantity_text()
        logging.info("打印获取检查后的出库数量：{}".format(get_deli_quantity))
        ValueAssert.value_assert_equal('1', get_deli_quantity)
        """获取创建出库单页面，点击Check后，Order Detail列表下的Product字段内容"""
        get_product = add_delivery.get_delivery_order_detail_product()
        """"点击提交按钮"""
        add_delivery.click_submit()
        """断言确认销售价格弹窗 Brand 与 Product字段文本内容是否正确"""
        get_confirm_price_product = add_delivery.get_list_field_text('Get Confirm the sale price Product')
        ValueAssert.value_assert_equal(get_product, get_confirm_price_product)
        get_confirm_price_brand = add_delivery.get_list_field_text('Get Confirm the sale price Brand')
        ValueAssert.value_assert_equal('itel appliances', get_confirm_price_brand)
        """点击提交后，盘点是否有弹出确认价格提示框，如果没有就执行except下面的语句，直接提交成功，断言是否有成功提示语"""
        try:
            affirm = add_delivery.get_text_submit_affirm()
            if affirm == "Submit":
                add_delivery.click_submit_affirm()
                DomAssert(drivers).assert_att("Submit successfully")
        except Exception as e:
            logging.info("打印日志{}".format(e))
        add_delivery.click_search()
        """"后端断言，创建出库单成功后，查询数据库表是否新增出库单记录"""
        sales_order, delivery_code = add_delivery.select_sql_delivery_order('86947', '1796874516566407', '1596874516539550')
        """出库单页面，筛选新建的无码出库单ID"""
        add_delivery.query_delivery_order(sales_order, delivery_code)
        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        get_sales_order = add_delivery.text_sales_order()
        get_delivery_order = add_delivery.text_delivery_order()
        get_deli_status = add_delivery.text_delivery_Status()
        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(get_sales_order, sales_order)
        ValueAssert.value_assert_equal(get_delivery_order, delivery_code)
        ValueAssert.value_assert_equal("On Transit", get_deli_status)


        """ 零售商NG2061301账号登录，进行快速收货 """
        user6.initialize_login(drivers, "NG2061301", "dcr123456")
        """打开采购单Purchase Management菜单"""
        user6.click_gotomenu("Purchase Management", "Inbound Receipt")
        receipt = InboundReceiptPage(drivers)
        """查询最近新建的销售单ID与出库单ID,进行快速收货操作"""
        receipt.inbound_quick_received(sales_order, delivery_code)
        """断言 获取快速收货弹出页面，Order ID与 Quantity字段内容是否匹配一致"""
        get_quick_received_order_id = receipt.get_list_field_text('Get Quick Received Order ID')
        get_quick_received_quantity = receipt.get_list_field_text('Get Quick Received Quantity')
        ValueAssert.value_assert_equal(delivery_code, get_quick_received_order_id)
        ValueAssert.value_assert_equal('1', get_quick_received_quantity)
        """NG20613客户存在多个仓库，需选择仓库"""
        receipt.input_select_warehouse('NG2061303  WNG2061304')
        """"点击保存按钮"""
        receipt.click_save()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        DomAssert(drivers).assert_att("Successfully")
        sleep(1.8)
        """获取列表Status字段内容"""
        status = receipt.text_status()
        """二代收货页面，验证收货后Status：显示GoodsReceipt状态，匹配一致"""
        ValueAssert.value_assert_equal('Goods Receipt', status)
        """关闭收货页面"""
        user6.click_close_open_menu()


        """零售商进行退货操作"""
        Base(drivers).refresh()
        """打开Purchase Management菜单"""
        user6.click_gotomenu("Sales Management", "Return Order")
        """实例化 二代退货单类"""
        return_order = ReturnOrderPage(drivers)
        return_order.add_return_order_box_sn_imei(get_sn1)
        record = return_order.get_text_Record()
        ValueAssert.value_assert_equal("Success", record)
        """点击提交按钮"""
        return_order.click_Submit()
        """断言页面是否存在提交成功 Submit Success!文本"""
        DomAssert(drivers).assert_att("Submit Success!")
        """退货单列表页面，指定传音人员审核, 退货单操作"""
        user6.initialize_login(drivers, "IN40080501", "dcr123456")
        """打开Purchase Management菜单"""
        user6.click_gotomenu("Sales Management", "Return Order")
        """查询二代账号，最近新建的出库单ID"""
        return_order.approve_return_order(delivery_code)
        """ 断言页面是否存在审核成功Approval successfully文本 """
        DomAssert(drivers).assert_att("Approval successfully")
        """退货成功后，获取列表第一个状态，断言判断是否审核成功"""
        status = return_order.get_text_Status()
        get_return_type = return_order.get_list_return_type()
        ValueAssert.value_assert_equal("Approved", status)
        ValueAssert.value_assert_equal('Return To Seller', get_return_type)


if __name__ == '__main__':
    pytest.main(['SalesManagement_DeliveryOrder.py'])