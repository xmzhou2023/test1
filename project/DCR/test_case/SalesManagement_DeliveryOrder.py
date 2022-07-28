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
        user.dcr_login(drivers, "lhmadmin", "dcr123456")

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
class TestExportDeliveryOrder:
    @allure.story("导出筛选的出库单")
    @allure.title("出库单页面，导出筛选的出库单记录")
    @allure.description("出库单页面，筛选出库单记录后，导出筛选的出库单记录")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    def test_002_001(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """打开销售管理-打开出库单页面"""
        user = LoginPage(drivers)
        user.click_gotomenu("Sales Management", "Delivery Order")

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
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        create_date1 = create_date[0:10]
        complete_date = export.get_complete_date_text()
        complete_date1 = complete_date[0:10]
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Delivery Order")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date1, today)
        ValueAssert.value_assert_equal(complete_date1, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_delivery_order()


@allure.feature("销售管理-出库单")
class TestDistAddQuantityDeliveryOrder:
    @allure.story("新增无码出库单")
    @allure.title("出库单页面，国包新增无码出库单操作")
    @allure.description("出库单页面，国包新增无码出库单操作")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    def test_003_001(self, drivers):
        user = LoginPage(drivers)
        user.dcr_login(drivers, "BD40344201", "dcr123456")

        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Delivery Order")
        add = DeliveryOrderPage(drivers)

        add.click_add()
        add.input_sub_buyer("BD2915")
        add.input_deli_pay_mode("Online")
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

        """断言查询新建的无码出库单"""
        user = SQL('DCR', 'test')
        varsql1 = "select order_code,delivery_code, status from  t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        result = user.query_db(varsql1)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        sleep(1)

        """出库单页面，筛选新建的无码出库单ID"""
        add.input_salesorder(order_code)
        add.input_deliveryorder(delivery_code)
        add.click_search()
        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        salesorder = add.text_sales_order()
        deliveryorder = add.text_delivery_order()
        """出库单页面，断言，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        sleep(1)


@allure.feature("销售管理-出库单")
class TestSubReceivQuantity:
    @allure.story("快速收货无码出库单")
    @allure.title("国包新建无码出库单后，二代快速收货，无码出库单")
    @allure.description("国包新建无码出库单成功后，然后二代快速收货无码出库单")
    @allure.severity("critical")  # 分别为5种类型等级：critical\normal\minor
    def test_004_001(self, drivers):
        """二代账号登录 进行 快速收货"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "BD291501", "dcr123456")

        """打开Purchase Management菜单"""
        user.click_gotomenu("Purchase Management", "Inbound Receipt")

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

        receiv.select_checkbox()
        receiv.click_quick_received()

        receiv.click_save()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        dom = DomAssert(drivers)
        dom.assert_att("Successfully")

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


@allure.feature("销售管理-出库单")
class TestSubQuantityReturn:
    @allure.story("二代退货无码出库单")
    @allure.title("二代申请退货无码出库单")
    @allure.description("二代收货成功后，然后申请退货无码出库单操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_005_001(self, drivers):
        """二代账号, 对无码出库单进行退货操作"""
        """刷新页面"""
        refresh = Base(drivers)
        refresh.refresh()

        """打开Purchase Management菜单"""
        menu = LoginPage(drivers)
        menu.click_gotomenu("Sales Management", "Return Order")

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

        dom = DomAssert(drivers)
        dom.assert_att("Submit Success!")
        """方法参数赋值给变量"""
        return_order.input_Delivery_Orderid(delivery_code)
        return_order.click_Search()

        """筛选退货列表页，获取退货出库单ID文本 与数据库表中查询的出库单ID对比是否一致"""
        Delivery_OrderID = return_order.get_text_deliveryID()
        status = return_order.get_return_status()
        ValueAssert.value_assert_equal(Delivery_OrderID, delivery_code)
        ValueAssert.value_assert_equal("Pending Approval", status)
        sleep(1)


@allure.feature("销售管理-出库单")
class TestDistQuantityReturnApprove:
    @allure.story("国包审核无码退货单")
    @allure.title("退货单页面，国包用户，审核无码退货单操作")
    @allure.description("退货单页面，国包用户，进行审核无码退货单操作")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_006_001(self, drivers):
        """退货单列表页面，国包账号, 进行退货审核操作"""
        user1 = LoginPage(drivers)
        user1.dcr_login(drivers, "BD40344201", "dcr123456")

        """打开Purchase Management菜单"""
        user1.click_gotomenu("Sales Management", "Return Order")

        """实例化 Return order退货单类"""
        return_approve = ReturnOrderPage(drivers)
        """从数据库表，查询国包账号，最近新建的销售单ID与出库单ID"""
        user = SQL('DCR', 'test')
        varsql = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200001 order by created_time desc limit 1"
        result = user.query_db(varsql)
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
        sleep(1)


if __name__ == '__main__':
    pytest.main(['SalesManagement_DeliveryOrder.py'])

