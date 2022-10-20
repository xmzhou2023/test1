from project.DCR.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from project.DCR.page_object.PurchaseManagement_InboundReceipt import InboundReceiptPage
from project.DCR.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
from project.DCR.page_object.Center_Process import SalesOrderPage
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.connect_sql import *
from public.base.basics import Base
from project.DCR.page_object.Center_Component import LoginPage
from libs.common.time_ui import sleep
import logging
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

@allure.feature("销售管理-国包出库单")
class TestQueryDistDelivery:
    @allure.story("国包查询出库单")
    @allure.title("国包用户按出库单条件筛选，出库单列表数据")
    @allure.description("根据销售单与出库单条件，筛选出库单列表数据")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD40344201", "dcr123456")

        """销售管理菜单-出库单列表-筛选出库单数据用例"""
        user.click_gotomenu("Sales Management", "Delivery Order")

        """出库单页面 实例化销售管理页面组件类"""
        query = DeliveryOrderPage(drivers)
        """出库单页面，筛选出库单用例"""
        salesorder = query.text_sales_order()
        deliveryorder = query.text_delivery_order()
        query.input_salesorder(salesorder)
        query.input_deliveryorder(deliveryorder)
        query.click_search()

        salesorder2 = query.text_sales_order()
        deliveryorder2 = query.text_delivery_order()
        """出库单页面，调用断言封装的方法，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(salesorder, salesorder2)
        ValueAssert.value_assert_equal(deliveryorder, deliveryorder2)
        #query.click_close_delivery_order()


@allure.feature("销售管理-国包出库单")
class TestAddDistDeliveryOrder:
    @allure.story("国包新增出库单，二代快速收货，二代退货出库单，国包审核退货单")
    @allure.title("国包新增出库单，二代快速收货，二代退货出库单，国包审核退货单")
    @allure.description("国包用户新增出库单，二代快速收货，二代退货出库单，国包审核退货单")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        """出库单列表页，国包账号 新增出库单用例 """
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "BD40344201", "dcr123456")

        """打开Report Analysis->IMEI Inventory Query菜单"""
        user1.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        """调用菜单栏，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        delivery = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        imei = delivery.get_text_imei_inventory()
        logging.info("打印获取IMEI Inventory Query页面的IMEI:{}".format(imei))
        delivery.click_close_imei_inventory()

        """ 刷新页面 """
        delivery.click_refresh(drivers)

        """销售管理菜单-出库单列表-筛选出库单数据用例"""
        user1.click_gotomenu("Sales Management", "Delivery Order")
        add = DeliveryOrderPage(drivers)
        # sql1 = SQL('DCR', 'test')
        # """从数据库表查询国包BD403442仓库的库存IMEI"""
        # varsql1 = "SELECT IMEI FROM  t_channel_warehouse_current_stock WHERE WAREHOUSE_ID ='62139' AND STATUS = 1  limit 1"
        # result = sql1.query_db(varsql1)
        # imei = result[0].get("IMEI")

        """点击Add新增出库单按"""
        add.click_add()
        add.input_sub_buyer("BD2915")
        add.input_deli_pay_mode("Online")
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
            #dom.assert_att("Submit successfully")
            logging.info("打印日志{}".format(e))
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
        """ 后端断言，数据库是否存在新建的出库单，获取列表出库单页面，销售ID、出库单ID、状态文本内容与数据库对比是否一致"""
        del_sales_order = add.text_sales_order()
        del_delivery_order = add.text_delivery_order()
        del_status = add.text_delivery_Status()
        sleep(1)
        """判断如果买家ID=BD2915，查询数据库表中国包最近新建的出库单信息"""
        """校验出库单列表，是否存在新增的销售单与出库单号"""
        sql3 = SQL('DCR', 'test')
        varsql3 = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        result = sql3.query_db(varsql3)
        ordercode = result[0].get("order_code")
        deliverycode = result[0].get("delivery_code")
        status = result[0].get("status")

        """筛选后断言，后端查询数据库sales_order、delivery_order、status字段是否与列表字段一致"""
        ValueAssert.value_assert_equal(del_sales_order, ordercode)
        ValueAssert.value_assert_equal(del_delivery_order, deliverycode)
        if status == 80200000:
            delivery_status = "On Transit"
            ValueAssert.value_assert_equal(delivery_status, del_status)
        add.click_close_delivery_order()


        """二代账号登录 进行 快速收货操作"""
        user1.initialize_login(drivers, "BD291501", "dcr123456")
        """打开Purchase Management菜单"""
        user1.click_gotomenu("Purchase Management", "Inbound Receipt")
        """二代账号筛选 最近新建的出库单ID，快速收货操作"""
        receipt = InboundReceiptPage(drivers)

        """从数据库表，查询最近新建的销售单ID与出库单ID"""
        sql4 = SQL('DCR', 'test')
        varsql4 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        result = sql4.query_db(varsql4)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")

        receipt.input_salesOrder(order_code)
        receipt.input_deliveryOrder(delivery_code)
        receipt.click_search()
        receipt.select_checkbox()
        receipt.click_quick_received()
        receipt.click_save()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        dom = DomAssert(drivers)
        dom.assert_att("Successfully")

        status = receipt.text_status()
        """二代收货页面，验证收货后Status：显示GoodsReceipt状态，匹配一致"""
        ValueAssert.value_assert_equal("Goods Receipt", status)
        """获取列表文本 销售单ID与 出库单ID"""
        salesorder = receipt.text_salesOrder()
        deliveryorder = receipt.text_deliveryOrder()
        """筛选二代收货列表数据，断言数据正确性"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        """ 关闭收货页面"""
        receipt.click_close_inbound_receipt()


        """二代账号, 进行退货操作"""
        Base(drivers).refresh()
        """打开Purchase Management菜单"""
        user1.click_gotomenu("Sales Management", "Return Order")
        """实例化 二代退货单类"""
        return_order = ReturnOrderPage(drivers)

        """退货单列表页面，二代或者零售商用户退货操作"""
        """从数据库表，查询国包账号，最近新建的销售单ID与出库单ID"""
        sql5 = SQL('DCR', 'test')
        varsql5 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200001 order by created_time desc limit 1"
        result = sql5.query_db(varsql5)
        delivery_code = result[0].get("delivery_code")

        return_order.click_Add()
        return_order.click_Return_Type()
        return_order.radio_Delivery_order()
        return_order.input_Delivery_order(delivery_code)
        return_order.click_Check()
        record = return_order.get_text_Record()
        ValueAssert.value_assert_equal("Success", record)

        return_order.click_Submit()
        dom = DomAssert(drivers)
        dom.assert_att("Submit Success!")

        """退货单页面，根据出库单ID查询 是否生成一条Return Order ID 退货单"""
        return_order.input_Delivery_Orderid(delivery_code)
        return_order.click_Search()

        """筛选退货列表页，获取退货出库单ID文本 与数据库表中查询的出库单ID对比是否一致"""
        Delivery_OrderID = return_order.get_text_deliveryID()
        status = return_order.get_return_status()
        ValueAssert.value_assert_equal(Delivery_OrderID, delivery_code)
        ValueAssert.value_assert_equal("Pending Approval", status)
        """关闭退货单页面"""
        return_order.click_close_return_order()


        """退货单列表页面，国包账号, 进行退货审核操作"""
        user1.initialize_login(drivers, "BD40344201", "dcr123456")

        """打开Purchase Management菜单"""
        user1.click_gotomenu("Sales Management", "Return Order")

        """实例化 Return order退货单类"""
        return_approve = ReturnOrderPage(drivers)
        """从数据库表，查询国包账号，最近新建的销售单ID与出库单ID"""
        sql6 = SQL('DCR', 'test')
        varsql6 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200001 order by created_time desc limit 1"
        result = sql6.query_db(varsql6)
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
        #return_approve.click_close_return_order()


if __name__ == '__main__':
    pytest.main(['SalesManagement_GBDeliveryOrder.py'])
