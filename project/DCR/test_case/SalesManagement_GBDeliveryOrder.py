from project.DCR.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from project.DCR.page_object.PurchaseManagement_InboundReceipt import InboundReceiptPage
from project.DCR.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
from public.base.assert_ui import ValueAssert
from libs.common.connect_sql import *
from public.base.basics import Base
from project.DCR.page_object.Center_Component import LoginPage
from libs.common.time_ui import sleep
import pytest
import allure

@allure.feature("销售管理-出库单")
class TestDistDelivery():
    @allure.story("国包查询出库单")
    @allure.title("国包用户按出库单条件筛选，出库单列表数据")
    @allure.description("根据销售单与出库单条件，筛选出库单列表数据")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_query_delivery(self, drivers):
        """DCR 国包账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "BD40344201", "dcr123456")
        sleep(5)
        """销售管理菜单-出库单列表-筛选出库单数据用例"""
        user.click_gotomenu("Sales Management", "Delivery Order")
        sleep(5)

        """出库单页面 实例化销售管理页面组件类"""
        delivery = DeliveryOrderPage(drivers)
        """出库单页面，筛选出库单用例"""
        salesorder = delivery.text_sales_order()
        deliveryorder = delivery.text_delivery_order()

        delivery.input_salesorder(salesorder)
        delivery.input_deliveryorder(deliveryorder)
        delivery.click_search()
        sleep(3)

        salesorder2 = delivery.text_sales_order()
        deliveryorder2 = delivery.text_delivery_order()
        """出库单页面，调用断言封装的方法，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(salesorder, salesorder2)
        ValueAssert.value_assert_equal(deliveryorder, deliveryorder2)
        """重置筛选条件"""
        delivery.click_reset()
        sleep(1)


@allure.feature("销售管理-出库单")
class TestAddDistDelivery():
    @allure.story("国包新增出库单")
    @allure.title("国包新增出库单")
    @allure.description("国包用户新增出库单，然后根据新建的出库断言是否加载正常")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_add_delivery_Order(self, drivers):
        """出库单列表页，国包账号 新增出库单用例 """
        add = DeliveryOrderPage(drivers)
        """从数据库表查询国包BD403442仓库的库存IMEI"""
        varsql = "SELECT IMEI FROM  t_channel_warehouse_current_stock WHERE WAREHOUSE_ID ='62139' AND STATUS = 1  limit 1"
        user = SQL('DCR', 'test')
        result = user.query_db(varsql)
        imei = result[0].get("IMEI")

        """点击Add新增出库单按"""
        add.click_add()
        add.input_sub_buyer("BD2915")
        add.input_deli_pay_mode("Online")
        add.input_imei(imei)
        add.click_check()
        sleep(1)
        add.click_submit()
        affirm = add.get_text_submit_affirm()
        sleep(1)
        if affirm == "Submit":
            add.click_submit_affirm()
        sleep(1)

        """从数据库表中，获取二代出库单ID，传给出库单筛选方法"""
        user = SQL('DCR', 'test')
        varsql = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        result = user.query_db(varsql)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        sleep(1)
        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        salesorder = add.text_sales_order()
        deliveryorder = add.text_delivery_order()
        add.input_salesorder(order_code)
        add.input_deliveryorder(delivery_code)
        add.click_search()
        sleep(3)
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
        user = SQL('DCR', 'test')
        varsql2 = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        result = user.query_db(varsql2)
        ordercode = result[0].get("order_code")
        deliverycode = result[0].get("delivery_code")
        status = result[0].get("status")
        ValueAssert.value_assert_equal(del_sales_order, ordercode)
        ValueAssert.value_assert_equal(del_delivery_order, deliverycode)
        if status == 80200000:
            delivery_status = "On Transit"
            ValueAssert.value_assert_equal(delivery_status, del_status)
        sleep(1)


    @allure.story("二代快速收货")
    @allure.title("二代快速收货")
    @allure.description("新增出库单成功后，然后快速收货")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_quick_receiv(self, drivers):
        """二代账号登录 进行 快速收货"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "BD291501", "dcr123456")
        sleep(5)
        """打开Purchase Management菜单"""
        user.click_gotomenu("Purchase Management", "Inbound Receipt")
        sleep(4)

        """二代账号筛选 最近新建的出库单ID，快速收货操作"""
        receiv = InboundReceiptPage(drivers)

        """从数据库表，查询最近新建的销售单ID与出库单ID"""
        user = SQL('DCR', 'test')
        varsql = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        result = user.query_db(varsql)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")

        receiv.input_salesOrder(order_code)
        receiv.input_deliveryOrder(delivery_code)
        receiv.click_search()
        sleep(3)
        receiv.checkbox()
        receiv.click_quick_received()
        sleep(1)
        receiv.click_save()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        success = receiv.get_successfully_text()
        sleep(0.5)
        ValueAssert.value_assert_In("Successfully", success)
        sleep(1.5)
        status = receiv.text_status()
        """二代收货页面，验证收货后Status：显示GoodsReceipt状态，匹配一致"""
        ValueAssert.value_assert_equal("Goods Receipt", status)
        """获取列表文本 销售单ID与 出库单ID"""
        salesorder = receiv.text_salesOrder()
        deliveryorder = receiv.text_deliveryOrder()
        """筛选二代收货列表数据，断言数据正确性"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        sleep(1)


    @allure.story("二代申请退货")
    @allure.title("二代申请退货")
    @allure.description("收货成功后，然后申请退货操作")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_return_order(self, drivers):
        """二代账号, 进行退货操作"""
        """刷新页面"""
        refresh = Base(drivers)
        refresh.refresh()

        """打开Purchase Management菜单"""
        menu = LoginPage(drivers)
        menu.click_gotomenu("Sales Management", "Return Order")
        sleep(3)

        """实例化 二代退货单类"""
        return_order = ReturnOrderPage(drivers)

        """退货单列表页面，二代或者零售商用户退货操作"""
        """从数据库表，查询国包账号，最近新建的销售单ID与出库单ID"""
        user = SQL('DCR', 'test')
        varsql = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200001 order by created_time desc limit 1"
        result = user.query_db(varsql)
        delivery_code = result[0].get("delivery_code")

        return_order.click_Add()
        return_order.click_Return_Type()
        return_order.radio_Delivery_order()
        return_order.input_Delivery_order(delivery_code)
        return_order.click_Check()
        record = return_order.get_text_Record()
        ValueAssert.value_assert_equal("Success", record)

        return_order.click_Submit()
        success = return_order.get_submit_success_text()
        sleep(0.5)
        ValueAssert.value_assert_In(success, "Submit Success!")
        sleep(3.5)
        """方法参数赋值给变量"""
        return_order.input_Delivery_Orderid(delivery_code)

        return_order.click_Search()
        sleep(2)

        """筛选退货列表页，获取退货出库单ID文本 与数据库表中查询的出库单ID对比是否一致"""
        Delivery_OrderID = return_order.get_text_deliveryID()
        status = return_order.get_return_status()
        ValueAssert.value_assert_equal(Delivery_OrderID, delivery_code)
        ValueAssert.value_assert_equal("Pending Approval", status)
        sleep(1)


    @allure.story("国包退货审核通过")
    @allure.title("国包退货审核通过")
    @allure.description("国包根据退货单，进行审核退货操作")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_return_order_Approve(self, drivers):
        """退货单列表页面，国包账号, 进行退货审核操作"""
        user1 = LoginPage(drivers)
        user1.dcr_login(drivers, "BD40344201", "dcr123456")
        sleep(5)
        """打开Purchase Management菜单"""
        user1.click_gotomenu("Sales Management", "Return Order")
        sleep(3)

        """实例化 Return order退货单类"""
        return_approve = ReturnOrderPage(drivers)
        """从数据库表，查询国包账号，最近新建的销售单ID与出库单ID"""
        user = SQL('DCR', 'test')
        varsql = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200001 order by created_time desc limit 1"
        result = user.query_db(varsql)
        delivery_code = result[0].get("delivery_code")

        return_approve.input_Delivery_Orderid(delivery_code)
        return_approve.click_Search()
        sleep(2)
        return_approve.click_checkbox()
        return_approve.click_Approve_button()
        return_approve.input_remark("同意退货")
        return_approve.click_agree()
        sleep(0.5)
        success = return_approve.get_Approval_Success()
        ValueAssert.value_assert_In(success, "Approval successfully")
        sleep(2)
        """退货成功后，获取列表第一个状态，断言判断是否审核成功"""
        status = return_approve.get_text_Status()
        ValueAssert.value_assert_equal("Approved", status)
        sleep(1)


if __name__ == '__main__':
    pytest.main(['SalesManagement_GBDeliveryOrder.py'])
