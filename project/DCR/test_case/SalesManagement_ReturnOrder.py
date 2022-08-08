from project.DCR.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
from project.DCR.page_object.SalesManagement_SalesOrder import SalesOrderPage
from project.DCR.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
from libs.common.connect_sql import *
import pytest
import allure


@allure.feature("销售管理-退货单")
class TestReturnOrder:
    @allure.story("卖家创建退货单")
    @allure.title("卖家创建无码销售单；然后卖家创建退货单，退货类型为Return To Seller，退无码产品")
    @allure.description("销售单页面，国包用户创建销售单，产品为无码的；卖家创建退货单，退货类型为Return To Seller，退无码产品")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    def test_001_001(self, drivers):
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

        """从数据库表，查询国包账号，最近新建的销售单ID"""
        sql1 = SQL('DCR', 'test')
        varsql1 = "select order_code from t_channel_sale_ticket where warehouse_id='61735' and seller_id='1596874516539127' and buyer_id='1596874516539550' and status=0 order by created_time desc limit 1"
        result1 = sql1.query_db(varsql1)
        order_code = result1[0].get("order_code")
        """按销售单ID条件筛选新建的销售单"""
        add.input_sales_order_ID(order_code)
        add.click_search()

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
        sleep(3)

        """获取列表，销售单ID与Status文本内容"""
        add.click_search()
        get_sales_order = add.get_text_sales_id()
        get_status = add.get_text_sales_status("Delivered")

        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        ValueAssert.value_assert_equal(get_sales_order, order_code)
        ValueAssert.value_assert_equal(get_status, "Delivered")
        add.click_close_sales_order()


        """卖家创建退货单，退货类型为Return To Seller，退无码产品"""
        base = Base(drivers)
        base.refresh()
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Return Order")

        returnorder = ReturnOrderPage(drivers)
        """从数据库表，查询国包账号，最近新建的出库单ID"""
        sql2 = SQL('DCR', 'test')
        varsql2 = "select delivery_code from t_channel_delivery_ticket where warehouse_id='61735' and seller_id='1596874516539127' and buyer_id='1596874516539550' and status=80200000 order by created_time desc limit 1"
        result2 = sql2.query_db(varsql2)
        delivery_code = result2[0].get("delivery_code")

        returnorder.click_Add()
        returnorder.click_Return_Type()

        returnorder.click_radio_quantity()
        returnorder.input_quantity_customer("NG20613")
        returnorder.input_quantity_delivery_order(delivery_code)
        returnorder.click_quantity_product("OEB-E75D  BLACK")
        returnorder.input_return_quantity('1')

        """点击Check按钮后，断言Order Detail列表记录是否正确"""
        returnorder.click_Check()
        get_quantity_deli = returnorder.get_quantity_deli_order_text(delivery_code)
        ValueAssert.value_assert_equal(get_quantity_deli, delivery_code)

        get_seller_id = returnorder.get_quantity_seller_id_text("EG400522")
        ValueAssert.value_assert_equal("EG400522", get_seller_id)
        get_buyer_id = returnorder.get_quantity_buyer_id_text("NG20613")
        ValueAssert.value_assert_equal("NG20613", get_buyer_id)

        returnorder.click_Submit()
        dom = DomAssert(drivers)
        dom.assert_att("Submit Success!")
        """方法参数赋值给变量"""
        returnorder.input_Delivery_Orderid(delivery_code)
        returnorder.click_Search()

        """筛选退货列表页，获取退货出库单ID文本 与数据库表中查询的出库单ID对比是否一致"""
        Delivery_OrderID = returnorder.get_text_deliveryID()
        status = returnorder.get_return_status()
        ValueAssert.value_assert_equal(Delivery_OrderID, delivery_code)
        ValueAssert.value_assert_equal("Approved", status)
        returnorder.click_close_return_order()


    @allure.story("卖家创建退货单")
    @allure.title("卖家创建有码出库单；然后卖家创建退货单，退货类型为Return To Seller、输入出库单号退货")
    @allure.description("销售单页面，国包用户创建有码出库单；卖家创建退货单，退货类型为Return To Seller、输入出库单号退货")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD40344201", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Delivery Order")

        add_delivery = DeliveryOrderPage(drivers)

        """从数据库表查询国包BD403442仓库的库存IMEI"""
        imei_varsql = "SELECT IMEI FROM  t_channel_warehouse_current_stock WHERE WAREHOUSE_ID ='62139' AND STATUS = 1  limit 1"
        imei_sql = SQL('DCR', 'test')
        imei_result = imei_sql.query_db(imei_varsql)
        imei = imei_result[0].get("IMEI")

        add_delivery.click_add()
        add_delivery.input_sub_buyer("BD2915")
        add_delivery.input_deli_pay_mode("Online")
        add_delivery.input_imei(imei)
        add_delivery.click_check()

        get_deli_quantity = add_delivery.get_delivery_quantity()
        get_order_deli_quantity = add_delivery.get_order_detail_deli_quantity()
        ValueAssert.value_assert_equal(get_deli_quantity, get_order_deli_quantity)

        add_delivery.click_submit()
        dom = DomAssert(drivers)
        try:
            affirm = add_delivery.get_text_submit_affirm()
            if affirm == "Submit":
                add_delivery.click_submit_affirm()
                dom.assert_att("Submit successfully")
        except Exception as e:
            dom.assert_att("Submit successfully")
        sleep(4.5)

        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        salesorder = add_delivery.text_sales_order()
        deliveryorder = add_delivery.text_delivery_order()
        del_status = add_delivery.text_delivery_Status()

        """从数据库表中，获取国包出库单ID，传给出库单筛选方法"""
        deli_sql = SQL('DCR', 'test')
        deli_varsql = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        deli_result = deli_sql.query_db(deli_varsql)
        order_code = deli_result[0].get("order_code")
        delivery_code = deli_result[0].get("delivery_code")
        sleep(1)
        add_delivery.input_salesorder(order_code)
        add_delivery.input_deliveryorder(delivery_code)
        add_delivery.click_search()

        """出库单页面，调用断言封装的方法，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        ValueAssert.value_assert_equal("On Transit", del_status)
        sleep(1)
        add_delivery.click_close_delivery_order()


        """卖家创建退货单，退货类型为Return To Seller，退有码产品，输入出库单号退货"""
        base = Base(drivers)
        base.refresh()
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Return Order")

        return_order = ReturnOrderPage(drivers)
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
        ValueAssert.value_assert_equal("Approved", status)
        return_order.click_close_return_order()


    # @allure.story("卖家创建退货单")
    # @allure.title("卖家创建有码出库单；然后卖家创建退货单，退货类型为Return To Seller、扫IMEI退货")
    # @allure.description("销售单页面，国包用户卖家创建有码出库单；卖家创建退货单，退货类型为Return To Seller、扫IMEI退货")
    # @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    # def test_001_003(self, drivers):





if __name__ == '__main__':
    pytest.main(['SalesManagement_ReturnOrder.py'])
