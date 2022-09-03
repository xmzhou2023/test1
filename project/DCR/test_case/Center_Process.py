import logging

from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.Center_Process import SalesOrderPage
from project.DCR.page_object.Center_Process import InboundReceiptPage
from project.DCR.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
from project.DCR.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from public.base.basics import Base
from libs.common.connect_sql import *
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    for i in range(1):
        get_menu_class = menu.get_open_menu_class()
        class_value = "tags-view-item router-link-exact-active router-link-active active"
        if class_value == str(get_menu_class):
            menu.click_close_open_menu()

@allure.feature("渠道销售业务流程")
class TestSalesBusinessProcess:
    @allure.story("渠道销售有码产品业务流程")
    @allure.title("销售单页面，二代新增销售单操作")
    @allure.description("销售单页面，二代新增销售单操作成功后，校验新增的销售单是否存在")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Sales Management", "Sales Order")

        """销售订单页面，新建销售单、直接出库、筛选、然后快速收货场景功能"""
        add_sales = SalesOrderPage(drivers)
        add_sales.click_add_sales()
        add_sales.input_sales_buyer("EG000562")
        add_sales.input_sales_brand('TECNO')
        add_sales.input_sales_product("SPARK 6 Go 64+4 AQUA BLUE")
        add_sales.input_sales_quantity('1')
        add_sales.click_submit()
        add_sales.click_submit_OK()

        """二代用户，查询数据库最近新建的销售单ID"""
        sql1 = SQL('DCR', 'test')
        sql_val1 = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        result = sql1.query_db(sql_val1)
        order = result[0].get("order_code")
        status = result[0].get("status")
        if status == 0:
            sales_status = "Pending"
        """销售单页面，按销售单ID筛选销售单信息"""
        add_sales.input_sales_order_ID(order)
        add_sales.click_search()

        """获取列表，销售单ID与Status文本内容"""
        get_sales_order = add_sales.get_text_sales_id()
        get_status = add_sales.get_sales_status_text("Pending")
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        ValueAssert.value_assert_equal(get_sales_order, order)
        ValueAssert.value_assert_equal(get_status, sales_status)


    @allure.story("渠道销售有码产品业务流程")
    @allure.title("销售单页面，对新增的销售单进行出库操作")
    @allure.description("销售单页面，对新增的销售单进行出库操作成功后，校验销售单状态是否更新")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")

        """打开Report Analysis->IMEI Inventory Query菜单"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")

        """调用菜单栏，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        delivery = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        delivery.click_unfold()
        delivery.input_material_id('11001120')
        delivery.click_inventory_search()
        imei = delivery.get_text_imei_inventory()
        logging.info("打印获取IMEI Inventory Query页面的IMEI:{}".format(imei))
        delivery.click_close_imei_inventory()

        """ 刷新页面 """
        delivery.click_refresh(drivers)
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Sales Management", "Sales Order")

        """二代用户，查询数据库最近新建的销售单ID"""
        sql2 = SQL('DCR', 'test')
        sql_val2 = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        result = sql2.query_db(sql_val2)
        order = result[0].get("order_code")
        """销售单页面，按销售单ID筛选销售单信息"""
        delivery.input_sales_order_ID(order)
        delivery.click_search()

        """勾选新建的销售单，直接出库操作"""
        delivery.click_checkbox_orderID()
        delivery.click_Delivery_button()
        delivery.input_Payment_Mode('Wechat')
        delivery.input_imei(imei)
        """点击检查IMEI按钮"""
        delivery.click_check()

        """断言检查出库单数量是否一致,扫码IMEI是否加载正确，是否有Success提示"""
        get_success = delivery.get_Deli_Scan_Record_Success()
        ValueAssert.value_assert_In("Success", get_success)
        get_imei = delivery.get_Deli_Scan_Record_IMEI(imei)
        ValueAssert.value_assert_equal(get_imei, imei)
        get_deli_quantity = delivery.get_delivery_quantity()
        get_order_deli_quantity = delivery.get_order_detail_deli_quantity()
        ValueAssert.value_assert_equal(get_deli_quantity, get_order_deli_quantity)

        delivery.click_submit_delivery()
        """销售单页面，按销售单ID筛选销售单信息，断言该条销售单对应的状态是否更新为：Delivered状态"""
        text_sales_order = delivery.get_text_sales_id()
        delivery.input_sales_order_ID(text_sales_order)
        delivery.click_search()
        text_status = delivery.get_sales_status_text("Delivered")
        """出库操作成功后，验证该条销售单对应的状态是否更新为：Delivered状态"""
        ValueAssert.value_assert_equal(text_status, "Delivered")


    @allure.story("渠道销售有码产品业务流程")
    @allure.title("采购管理页面，零售商用户快速收货操作")
    @allure.description("采购管理页面，零售商用户快速收货操作成功后，校验收货状态是否更新")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_003(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "EG00056201", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Purchase Management", "Inbound Receipt")

        """定义账号标识是否是二代sub_Account还是零售商retail_Account 账号收货"""
        usercount = "retail_Account"

        """调用零售商收货筛选与 快速收货用例"""
        receipt = InboundReceiptPage(drivers)
        """查询BD40344201国包账号下出库单数据库表，返回销售单ID与出库单ID，作为筛选条件，验证新增的出库单是否成功"""
        if usercount == "sub_Account":
            """从数据库表，查询最近新建的销售单ID与出库单ID"""
            user = SQL('DCR', 'test')
            varsql = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
            result = user.query_db(varsql)
            salesid = result[0].get("order_code")
            deliveryid = result[0].get("delivery_code")
        elif usercount == "retail_Account":
            """从数据库表，查询最近新建的销售单ID与出库单ID"""
            sql3 = SQL('DCR', 'test')
            var_sql3 = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200000 order by created_time desc limit 1"
            result = sql3.query_db(var_sql3)
            salesid = result[0].get("order_code")
            deliveryid = result[0].get("delivery_code")

            receipt.input_salesOrder(salesid)
            receipt.input_deliveryOrder(deliveryid)
            receipt.click_search()
            receipt.click_checkbox()
            receipt.click_quick_received()
            receipt.click_save()
            """获取收货提交成功提示语，断言是否包含Successfully提示语"""
            DomAssert(drivers).assert_att("Successfully")
            sleep(2)
            status = receipt.get_text_status()
            """ 二代收货页面，断言收货后Status更新为：Goods Receipt状态 """
            ValueAssert.value_assert_equal(status, "Goods Receipt")
            """获取列表文本 销售单ID与 出库单ID"""
            salesorder = receipt.get_text_salesOrder()
            deliveryorder = receipt.get_text_deliveryOrder()
            """筛选二代收货列表数据，断言数据正确性"""
            ValueAssert.value_assert_equal(salesorder, salesid)
            ValueAssert.value_assert_equal(deliveryorder, deliveryid)


    @allure.story("渠道销售有码产品业务流程")
    @allure.title("退货页面，零售商用户，对已收货的销售单，进行退货操作")
    @allure.description("退货页面，零售商用户收货成功后，对已收货的销售的，进行退货操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_004(self, drivers):
            """零售商EG00056201账号, 进行退货操作"""
            user1 = LoginPage(drivers)
            user1.initialize_login(drivers, "EG00056201", "dcr123456")

            """打开Purchase Management菜单"""
            user1.click_gotomenu("Sales Management", "Return Order")

            """实例化 二代退货单类"""
            return_order = ReturnOrderPage(drivers)
            """从数据库表，查询二代账号，最近新建的销售单ID与出库单ID"""
            sql4 = SQL('DCR', 'test')
            var_sql4 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200001 order by created_time desc limit 1"
            result = sql4.query_db(var_sql4)
            delivery_code = result[0].get("delivery_code")

            return_order.click_Add()
            return_order.click_Return_Type()
            return_order.radio_Delivery_order()
            return_order.input_Delivery_order(delivery_code)
            return_order.click_Check()
            record = return_order.get_text_Record()
            ValueAssert.value_assert_equal("Success", record)
            return_order.click_Submit()

            """断言页面是否存在提交成功 Submit Success!文本"""
            dom = DomAssert(drivers)
            dom.assert_att("Submit Success!")
            """方法参数赋值给变量"""
            return_order.input_Delivery_Orderid(delivery_code)
            return_order.click_Search()

            """筛选退货列表页，获取退货出库单ID文本 与数据库表中查询的出库单ID对比是否一致"""
            delivery_order_id = return_order.get_text_deliveryID()
            status = return_order.get_return_status()
            ValueAssert.value_assert_equal(delivery_order_id, delivery_code)
            ValueAssert.value_assert_equal("Pending Approval", status)


    @allure.story("渠道销售有码产品业务流程")
    @allure.title("退货页面，二代账号, 进行审核退货单操作")
    @allure.description("二代账号, 进行退货审核操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_005(self, drivers):
        """退货单列表页面，二代账号, 进行审核退货单操作"""
        user2 = LoginPage(drivers)
        user2.initialize_login(drivers, "BD291501", "dcr123456")

        """打开Purchase Management菜单"""
        user2.click_gotomenu("Sales Management", "Return Order")

        """实例化 Return order退货单类"""
        return_approve = ReturnOrderPage(drivers)
        """从数据库表，查询二代账号，最近新建的销售单ID与出库单ID"""
        varsql5 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200001 order by created_time desc limit 1"
        sql5 = SQL('DCR', 'test')
        result = sql5.query_db(varsql5)
        delivery_code = result[0].get("delivery_code")

        return_approve.input_Delivery_Orderid(delivery_code)
        return_approve.click_Search()

        return_approve.click_checkbox()
        return_approve.click_Approve_button()
        return_approve.input_remark("同意退货")
        return_approve.click_agree()

        """ 断言页面是否存在审核成功Approval successfully文本 """
        dom = DomAssert(drivers)
        dom.assert_att("Approval successfully")

        """退货成功后，获取列表第一个状态，断言判断是否审核成功"""
        status = return_approve.get_text_Status()
        ValueAssert.value_assert_equal("Approved", status)


@allure.feature("渠道销售业务流程")
class TestDeliveryBusinessProcess:
    @allure.story("聚道出库无码产品业务流程")
    @allure.title("出库单页面，国包用户，新增无码出库单操作")
    @allure.description("出库单页面，国包用户，新增无码出库单操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        user3 = LoginPage(drivers)
        user3.initialize_login(drivers, "BD40344201", "dcr123456")

        """打开销售管理-打开出库单页面"""
        user3.click_gotomenu("Sales Management", "Delivery Order")

        add = DeliveryOrderPage(drivers)
        add.click_add()
        add.input_sub_buyer("BD2915")
        add.input_deli_pay_mode("Online")
        add.click_quantity_radio_button()
        add.click_quantity_add()
        add.click_quantity_product("TECNO B1 BLACK")
        add.input_delivery_quantity("1")
        add.click_delivery_quantity_text()

        """增加断言 检查Delivery Quantity数量是否与输入的数量一致"""
        get_deli_quantity = add.get_delivery_quantity_text()
        ValueAssert.value_assert_equal("1", get_deli_quantity)

        """点击Submit提交按钮"""
        add.click_submit()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        dom = DomAssert(drivers)
        dom.assert_att("Submit successfully")
        sleep(2)
        """断言查询新建的无码出库单"""
        sql1 = SQL('DCR', 'test')
        varsql1 = "select order_code,delivery_code, status from t_channel_delivery_ticket where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        result = sql1.query_db(varsql1)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        delivery_status = result[0].get("status")
        status = add.delivery_convert_status(delivery_status)

        """出库单页面，筛选新建的无码出库单ID"""
        add.input_salesorder(order_code)
        add.input_deliveryorder(delivery_code)
        add.click_search()
        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        get_sales_order = add.text_sales_order()
        get_delivery_order = add.text_delivery_order()
        get_status = add.text_delivery_Status()
        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(get_sales_order, order_code)
        ValueAssert.value_assert_equal(get_delivery_order, delivery_code)
        ValueAssert.value_assert_equal(get_status, status)


    @allure.story("聚道出库无码产品业务流程")
    @allure.title("国包新建无码出库单后，二代用户，快速收货无码出库单")
    @allure.description("国包新建无码出库单成功后，然后二代快速收货无码出库单")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_002(self, drivers):
        """二代账号登录 进行 快速收货"""
        user4 = LoginPage(drivers)
        user4.initialize_login(drivers, "BD291501", "dcr123456")

        """打开Purchase Management菜单"""
        user4.click_gotomenu("Purchase Management", "Inbound Receipt")

        """二代账号筛选 最近新建的出库单ID，快速收货操作"""
        receiv = InboundReceiptPage(drivers)

        """从数据库表，查询最近新建的销售单ID与出库单ID"""
        sql2 = SQL('DCR', 'test')
        varsql2 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        result = sql2.query_db(varsql2)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")

        receiv.input_salesOrder(order_code)
        receiv.input_deliveryOrder(delivery_code)
        """点击筛选查询按钮"""
        receiv.click_search()

        receiv.click_checkbox()
        receiv.click_quick_received()
        receiv.click_save()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        dom = DomAssert(drivers)
        dom.assert_att("Successfully")
        sleep(2)

        """获取列表文本 销售单ID、出库单ID、Status状态"""
        salesorder = receiv.get_text_salesOrder()
        deliveryorder = receiv.get_text_deliveryOrder()
        status = receiv.get_text_status()
        """断言二代收货页面 销售单ID、出库单ID是否与数据库查询的数据一致"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        """断言收货后Status：显示GoodsReceipt状态，匹配一致"""
        ValueAssert.value_assert_equal("Goods Receipt", status)


    @allure.story("聚道出库无码产品业务流程")
    @allure.title("二代用户，申请退货无码出库单")
    @allure.description("二代收货成功后，然后申请退货无码出库单操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_003(self, drivers):
        """二代账号, 对无码出库单进行退货操作"""
        user5 = LoginPage(drivers)
        user5.initialize_login(drivers, "BD291501", "dcr123456")

        """打开Purchase Management菜单"""
        user5.click_gotomenu("Sales Management", "Return Order")

        """实例化 二代退货单类"""
        return_order = ReturnOrderPage(drivers)

        """退货单列表页面，二代或者零售商用户退货操作"""
        """从数据库表，查询国包账号，最近新建的销售单ID与出库单ID"""
        sql3 = SQL('DCR', 'test')
        varsql3 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200001 order by created_time desc limit 1"
        result = sql3.query_db(varsql3)
        delivery_code = result[0].get("delivery_code")
        sleep(1)
        return_order.click_Add()
        return_order.click_Return_Type()
        return_order.click_radio_quantity()
        return_order.input_quantity_customer("BD2915")
        return_order.input_quantity_delivery_order(delivery_code)
        return_order.click_quantity_product("TECNO B1  BLACK")
        return_order.input_return_quantity("1")
        """点击Check按钮后，断言Order Detail列表记录是否正确"""
        return_order.click_Check()
        get_quantity_deli = return_order.get_quantity_deli_order_text(delivery_code)
        ValueAssert.value_assert_equal(get_quantity_deli, delivery_code)

        get_seller_id = return_order.get_quantity_seller_id_text("BD403442")
        ValueAssert.value_assert_equal("BD403442", get_seller_id)
        get_buyer_id = return_order.get_quantity_buyer_id_text("BD2915")
        ValueAssert.value_assert_equal("BD2915", get_buyer_id)
        """点击提交"""
        return_order.click_Submit()
        DomAssert(drivers).assert_att("Submit Success!")

        """方法参数赋值给变量"""
        return_order.input_Delivery_Orderid(delivery_code)
        return_order.click_Search()

        """筛选退货列表页，获取退货出库单ID文本 与数据库表中查询的出库单ID对比是否一致"""
        delivery_order_id = return_order.get_text_deliveryID()
        status = return_order.get_return_status()
        ValueAssert.value_assert_equal(delivery_order_id, delivery_code)
        ValueAssert.value_assert_equal("Pending Approval", status)


    @allure.story("聚道出库无码产品业务流程")
    @allure.title("退货单页面，国包用户，审核无码退货单操作")
    @allure.description("退货单页面，国包用户，进行审核无码退货单操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_004(self, drivers):
        """退货单列表页面，国包账号, 进行退货审核操作"""
        user6 = LoginPage(drivers)
        user6.initialize_login(drivers, "BD40344201", "dcr123456")

        """打开Purchase Management菜单"""
        user6.click_gotomenu("Sales Management", "Return Order")

        """实例化 Return order退货单类"""
        return_approve = ReturnOrderPage(drivers)
        """从数据库表，查询国包账号，最近新建的销售单ID与出库单ID"""
        sql4 = SQL('DCR', 'test')
        varsql4 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200001 order by created_time desc limit 1"
        result = sql4.query_db(varsql4)
        delivery_code = result[0].get("delivery_code")

        return_approve.input_Delivery_Orderid(delivery_code)
        return_approve.click_Search()

        return_approve.click_checkbox()
        return_approve.click_Approve_button()
        return_approve.input_remark("同意退货")
        return_approve.click_agree()
        """ 断言页面是否存在审核成功Approval successfully文本 """
        dom = DomAssert(drivers)
        dom.assert_att("Approval successfully")
        """退货成功后，获取列表第一个状态，断言判断是否审核成功"""
        status = return_approve.get_text_Status()
        ValueAssert.value_assert_equal("Approved", status)

if __name__ == '__main__':
    pytest.main(['Center_Process.py'])
