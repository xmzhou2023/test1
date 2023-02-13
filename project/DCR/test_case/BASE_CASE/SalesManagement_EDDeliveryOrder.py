import logging
from project.DCR.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from project.DCR.page_object.PurchaseManagement_InboundReceipt import InboundReceiptPage
from project.DCR.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
from libs.common.connect_sql import *
from libs.common.time_ui import sleep
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert, DomAssert
from public.base.basics import Base
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

@allure.feature("销售管理-二代出库单")
class TestQuerySubDelivery:
    @allure.story("查询出库单")
    @allure.title("二代用户，按出库单条件筛选，出库单列表数据")
    @allure.description("二代用户，根据销售单与出库单条件，筛选出库单列表数据")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Sales Management", "Delivery Order")
        """出库单页面 实例化销售管理页面组件类"""
        query = DeliveryOrderPage(drivers)
        """出库单页面，筛选出库单用例"""
        sales_order = query.text_sales_order()
        delivery_order = query.text_delivery_order()
        query.input_salesorder(sales_order)
        query.input_deliveryorder(delivery_order)
        query.click_search()

        sales_order2 = query.text_sales_order()
        delivery_order2 = query.text_delivery_order()
        """出库单页面，调用断言封装的方法，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(sales_order, sales_order2)
        ValueAssert.value_assert_equal(delivery_order, delivery_order2)
        #query.click_close_delivery_order()


@allure.feature("销售管理-二代出库单")
class TestAddSubDeliveryReceipt:
    @allure.story("新增出库单")
    @allure.title("二代新增出库单,零售商收货操作,零售商退货出库单,二代审核退货单")
    @allure.description("二代新增出库单,零售商收货操作,零售商退货出库单,二代审核退货单")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        """出库单列表页，二代用户新增出库单用例 """
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "BD291501", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user1.click_gotomenu("Sales Management", "Delivery Order")
        add = DeliveryOrderPage(drivers)
        """查询二代BD2915仓库的库存IMEI"""
        sql1 = SQL('DCR', 'test')
        varsql1 = "SELECT IMEI FROM  t_channel_warehouse_current_stock WHERE WAREHOUSE_ID = 62134   AND STATUS = 1 limit 1"
        result_imei = sql1.query_db(varsql1)
        sub_imei = result_imei[0].get("IMEI")
        """点击Add新增出库单按钮"""
        add.click_add()
        """如果buyer买家为二代账号，则调用input_sub_buyer方法；buyer买家为零售商账号，input_retail_buyer方法"""
        add.input_retail_buyer("EG000562")
        add.input_deli_pay_mode("Online")
        add.input_imei(sub_imei)
        add.click_check()
        add.click_submit()
        dom = DomAssert(drivers)
        try:
            affirm = add.get_text_submit_affirm()
            if affirm == "Submit":
                add.click_submit_affirm()
                dom.assert_att("Submit successfully")
        except Exception as e:
            logging.info("打印日志{}".format(e))
        add.click_search()

        sql2 = SQL('DCR', 'test')
        varsql2 = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200000 order by created_time desc limit 1"
        result = sql2.query_db(varsql2)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        logging.info("查询数据库order_code字段{}".format(order_code))
        logging.info("查询数据库delivery_code字段{}".format(delivery_code))
        sleep(1)

        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        salesorder = add.text_sales_order()
        deliveryorder = add.text_delivery_order()
        """出库单页面，筛选出库单ID"""
        add.input_salesorder(order_code)
        add.input_deliveryorder(delivery_code)
        add.click_search()
        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        sleep(1)
        """断言后端，数据库是否存在新建的出库单，获取列表出库单页面，销售ID、出库单ID、状态文本内容与数据库对比是否一致"""
        del_sales_order = add.text_sales_order()
        del_delivery_order = add.text_delivery_order()
        del_status = add.text_delivery_Status()
        sleep(1)

        """判断如果买家ID=EG000562，查询数据库表中二代最近新建的出库单信息"""
        user = SQL('DCR', 'test')
        varsql4 = "select order_code,delivery_code,status from  t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200000 order by created_time desc limit 1"
        result = user.query_db(varsql4)
        order_id = result[0].get("order_code")
        delivery_id = result[0].get("delivery_code")
        status = result[0].get("status")
        sleep(1)
        ValueAssert.value_assert_equal(del_sales_order, order_id)
        ValueAssert.value_assert_equal(del_delivery_order, delivery_id)
        if status == 80200000:
            delivery_status = "On Transit"
            ValueAssert.value_assert_equal(delivery_status, del_status)
        add.click_close_delivery_order()

        """ 零售商EG00056201账号登录， 进行快速收货 """
        user1.initialize_login(drivers, "EG00056201", "dcr123456")
        """打开采购单Purchase Management菜单"""
        user1.click_gotomenu("Purchase Management", "Inbound Receipt")
        receipt = InboundReceiptPage(drivers)
        """从数据库表，查询最近新建的销售单ID与出库单ID"""
        sql3 = SQL('DCR', 'test')
        varsql3 = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200000 order by created_time desc limit 1"
        result = sql3.query_db(varsql3)
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
        """关闭收货页面"""
        receipt.click_close_inbound_receipt()

        """零售商EG00056201账号, 进行退货操作"""
        Base(drivers).refresh()
        """打开Purchase Management菜单"""
        user1.click_gotomenu("Sales Management", "Return Order")
        """实例化 二代退货单类"""
        return_order = ReturnOrderPage(drivers)
        """从数据库表，查询二代账号，最近新建的销售单ID与出库单ID"""
        sql3 = SQL('DCR', 'test')
        varsql4 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200001 order by created_time desc limit 1"
        result = sql3.query_db(varsql4)
        delivery_code = result[0].get("delivery_code")
        """点击添加退货单按钮"""
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
        Delivery_OrderID = return_order.get_text_deliveryID()
        status = return_order.get_return_status()
        ValueAssert.value_assert_equal(Delivery_OrderID, delivery_code)
        ValueAssert.value_assert_equal("Pending Approval", status)
        """关闭退货页面"""
        return_order.click_close_return_order()


        """退货单列表页面，二代账号, 进行审核退货单操作"""
        user1.initialize_login(drivers, "BD291501", "dcr123456")
        """打开Purchase Management菜单"""
        user1.click_gotomenu("Sales Management", "Return Order")
        """实例化 Return order退货单类"""
        return_approve = ReturnOrderPage(drivers)
        sql4 = SQL('DCR', 'test')
        """从数据库表，查询二代账号，最近新建的销售单ID与出库单ID"""
        varsql5 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200001 order by created_time desc limit 1"
        result = sql4.query_db(varsql5)
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
    pytest.main(['SalesManagement_EDDeliveryOrder.py'])
