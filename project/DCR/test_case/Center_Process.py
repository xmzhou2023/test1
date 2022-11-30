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
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("渠道销售业务流程")
class TestSalesBusinessProcess:
    @allure.story("渠道销售有码多个品牌产品业务流程")
    @allure.title("销售单页面，二代新增有码多个品牌销售单操作")
    @allure.description("销售单页面，二代新增有码多个品牌销售单操作成功后，校验新增的销售单是否存在")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        """1 二代账号登录，获取IMEI Inverter Query列表的IMEI"""
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
        tecno_imei = delivery.get_text_imei_inventory()
        logging.info("打印获取IMEI Inventory Query页面的IMEI:{}".format(tecno_imei))
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        delivery.input_material_id('10705705')
        delivery.click_inventory_search()
        itel_imei = delivery.get_text_imei_inventory()
        logging.info("打印获取IMEI Inventory Query页面的IMEI:{}".format(itel_imei))
        delivery.click_close_imei_inventory()


        """2 销售订单页面，新建有码销售单操作"""
        add_sales = SalesOrderPage(drivers)
        add_sales.click_refresh(drivers)
        user.click_gotomenu("Sales Management", "Sales Order")
        add_sales.click_add_sales()
        add_sales.input_sales_buyer("EG000562")
        add_sales.input_sales_brand('TECNO')
        add_sales.input_sales_product("SPARK 6 Go 64+4 AQUA BLUE")
        """点击Add Product添加多个品牌"""
        add_sales.click_sales_order_add_product_button()
        add_sales.click_sales_order_add_brand2('itel')
        add_sales.input_sales_order_add_product2('POWER 100 4+4 LIGHT BLUE')
        add_sales.click_submit()
        add_sales.click_submit_OK()
        """二代用户，查询数据库最近新建的销售单ID,返回sales order id """
        sales_order = add_sales.query_sql_sales_order_id('62134', '1596874516539662', '1596874516539668', '0')
        """销售单页面，按销售单ID筛选销售单信息"""
        add_sales.input_sales_order_ID(sales_order)
        add_sales.click_search()
        """获取列表，销售单ID与Status文本内容"""
        get_sales_order = add_sales.get_text_sales_id()
        get_status = add_sales.get_sales_status_text()
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        ValueAssert.value_assert_equal(get_sales_order, sales_order)
        ValueAssert.value_assert_equal(get_status, "Pending")

        """3 对新增的销售单进行出库操作,校验销售单状态是否更新 """
        """勾选新建的销售单，直接出库操作"""
        delivery.click_checkbox_orderID()
        delivery.click_Delivery_button()
        delivery.input_Payment_Mode('Wechat')
        """出库品牌TECNO"""
        delivery.input_imei(tecno_imei)
        """点击检查IMEI按钮"""
        delivery.click_check()
        """出库品牌itel"""
        delivery.input_imei(itel_imei)
        delivery.click_check()
        """断言检查出库单数量是否一致,扫码IMEI是否加载正确，是否有Success提示"""
        get_success = delivery.get_Deli_Scan_Record_Success()
        ValueAssert.value_assert_In("Success", get_success)
        get_deli_quantity = delivery.get_delivery_quantity()
        ValueAssert.value_assert_equal('2', get_deli_quantity)
        """点击Submit出库单提交按钮"""
        delivery.click_submit_delivery()
        DomAssert(drivers).assert_att('Successfully')
        """销售单页面，按销售单ID筛选销售单信息，断言该条销售单对应的状态是否更新为：Delivered状态"""
        delivery.input_sales_order_ID(sales_order)
        delivery.click_search()
        text_status = delivery.get_sales_status_text()
        """出库操作成功后，验证该条销售单对应的状态是否更新为：Delivered状态"""
        ValueAssert.value_assert_equal(text_status, "Delivered")
        add_sales.click_close_sales_order()


        """4 断言进入Delivery Order菜单，是否生成条件对应的出库单记录，状态是否为Delivered"""
        delivery.click_refresh(drivers)
        user.click_gotomenu("Sales Management", "Delivery Order")
        salesid, deliveryid = add_sales.query_sql_delivery_order_id2('62134', '1596874516539662', '1596874516539668', '80200000')
        logging.info("打印最近新建的销售单ID与出库单ID:{}".format(salesid, deliveryid))
        deli_assert = DeliveryOrderPage(drivers)
        deli_assert.input_salesorder(salesid)
        deli_assert.click_search()
        deli_status = deli_assert.get_status_text()
        get_delivery_text = deli_assert.text_delivery_order()
        ValueAssert.value_assert_equal('On Transit', deli_status)
        ValueAssert.value_assert_equal(deliveryid, get_delivery_text)
        """断言 查看该条出库单记录的IEMI Detail详情信息是否正确"""
        """打开IMEI Detail弹窗"""
        deli_assert.click_imei_detail()
        deli_detail_title = deli_assert.get_detail_title_delivery_id_text()
        detail_total = deli_assert.get_detail_total_text()
        ValueAssert.value_assert_In(deliveryid, deli_detail_title)
        ValueAssert.value_assert_In('2', detail_total)
        """关闭出库单IMEI Detail详情页"""
        deli_assert.click_close_imei_detail()


        """5 采购管理页面，零售商用户快速收货操作"""
        user.initialize_login(drivers, "EG00056201", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Purchase Management", "Inbound Receipt")
        """调用零售商收货筛选与 快速收货用例"""
        receipt = InboundReceiptPage(drivers)
        """从数据库查询BD40344201国包账号下最近新建的出库单，返回销售单ID与出库单ID，作为筛选条件，验证新增的出库单是否成功"""
        receipt.input_salesOrder(salesid)
        receipt.input_deliveryOrder(deliveryid)
        receipt.click_inbound_receipt_search()
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
        """关闭收货页面"""
        receipt.click_close_inbound_receipt()


        """刷新页面"""
        add_sales.click_refresh(drivers)
        """6 退货页面，零售商用户，对已收货的销售单，进行退货操作"""
        user.initialize_login(drivers, "EG00056201", "dcr123456")
        """打开Purchase Management菜单"""
        user.click_gotomenu("Sales Management", "Return Order")
        """实例化 二代退货单类"""
        return_order = ReturnOrderPage(drivers)
        """从数据库表，查询二代账号，最近新建的销售单ID与出库单ID"""
        delivery_code = add_sales.query_sql_delivery_order_id1('62134', '1596874516539662', '1596874516539668', '80200001')
        return_order.click_Add()
        return_order.click_Return_Type()
        return_order.radio_Delivery_order()
        return_order.input_Delivery_order(delivery_code)
        return_order.click_Check()
        record = return_order.get_text_Record()
        ValueAssert.value_assert_equal("Success", record)
        return_order.click_Submit()
        """断言页面是否存在提交成功 Submit Success!文本"""
        DomAssert(drivers).assert_att("Submit Success!")
        """方法参数赋值给变量"""
        return_order.input_Delivery_Orderid(delivery_code)
        return_order.click_Search()
        """筛选退货列表页，获取退货出库单ID文本 与数据库表中查询的出库单ID对比是否一致"""
        delivery_order_id = return_order.get_text_deliveryID()
        status = return_order.get_return_status()
        ValueAssert.value_assert_equal(delivery_order_id, delivery_code)
        ValueAssert.value_assert_equal("Pending Approval", status)
        return_order.click_close_return_order()


        """7 退货单列表页面，二代账号, 进行审核退货单操作"""
        user.initialize_login(drivers, "BD291501", "dcr123456")
        """打开Purchase Management菜单"""
        user.click_gotomenu("Sales Management", "Return Order")
        """实例化 Return order退货单类"""
        return_approve = ReturnOrderPage(drivers)
        """从数据库表，查询二代账号，最近新建的销售单ID与出库单ID"""
        return_approve.input_Delivery_Orderid(delivery_code)
        return_approve.click_Search()
        return_approve.click_checkbox()
        return_approve.click_Approve_button()
        return_approve.input_remark("同意退货")
        return_approve.click_agree()
        """ 断言页面是否存在审核成功Approval successfully文本 """
        DomAssert(drivers).assert_att("Approval successfully")
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
        user2 = LoginPage(drivers)
        user2.initialize_login(drivers, "BD40344201", "dcr123456")
        """1 国包用户，新增无码出库单操作"""
        user2.click_gotomenu("Sales Management", "Delivery Order")
        add = DeliveryOrderPage(drivers)
        add.click_add()
        add.input_sub_buyer("BD2915")
        add.input_deli_pay_mode("Online")
        add.click_quantity_radio_button()
        add.click_quantity_add()
        add.click_quantity_product("A2 se BLACK")
        add.input_delivery_quantity("1")
        add.click_delivery_quantity_text()
        """增加断言 检查Delivery Quantity数量是否与输入的数量一致"""
        get_deli_quantity = add.get_delivery_quantity_text()
        ValueAssert.value_assert_equal("1", get_deli_quantity)
        """点击Submit提交按钮"""
        add.click_submit()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        DomAssert(drivers).assert_att("Submit successfully")
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


        """2 二代用户，快速收货无码出库单"""
        user2.initialize_login(drivers, "BD291501", "dcr123456")
        """打开Purchase Management菜单"""
        user2.click_gotomenu("Purchase Management", "Inbound Receipt")
        """二代账号筛选 最近新建的出库单ID，快速收货操作"""
        receipt = InboundReceiptPage(drivers)
        """从数据库表，查询最近新建的销售单ID与出库单ID"""
        sql2 = SQL('DCR', 'test')
        varsql2 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        result = sql2.query_db(varsql2)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        receipt.input_salesOrder(order_code)
        receipt.input_deliveryOrder(delivery_code)
        """点击筛选查询按钮"""
        receipt.click_inbound_receipt_search
        receipt.click_checkbox()
        receipt.click_quick_received()
        receipt.click_save()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        DomAssert(drivers).assert_att("Successfully")
        sleep(2)
        """获取列表文本 销售单ID、出库单ID、Status状态"""
        salesorder = receipt.get_text_salesOrder()
        deliveryorder = receipt.get_text_deliveryOrder()
        status = receipt.get_text_status()
        """断言二代收货页面 销售单ID、出库单ID是否与数据库查询的数据一致"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        """断言收货后Status：显示GoodsReceipt状态，匹配一致"""
        ValueAssert.value_assert_equal("Goods Receipt", status)
        receipt.click_close_inbound_receipt()


        """刷新页面"""
        receipt = SalesOrderPage(drivers)
        receipt.click_refresh(drivers)
        """二代用户，申请退货无码出库单"""
        user2.click_gotomenu("Sales Management", "Return Order")
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
        return_order.click_quantity_product("A2 se  BLACK")
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


        """4 退货单页面，国包用户，审核无码退货单操作"""
        user2.initialize_login(drivers, "BD40344201", "dcr123456")
        """打开Purchase Management菜单"""
        user2.click_gotomenu("Sales Management", "Return Order")
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
        DomAssert(drivers).assert_att("Approval successfully")
        """退货成功后，获取列表第一个状态，断言判断是否审核成功"""
        status = return_approve.get_text_Status()
        ValueAssert.value_assert_equal("Approved", status)


if __name__ == '__main__':
    pytest.main(['Center_Process.py'])
