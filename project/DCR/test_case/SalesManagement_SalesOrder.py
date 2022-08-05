from project.DCR.page_object.SalesManagement_SalesOrder import SalesOrderPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.connect_sql import *
from libs.common.time_ui import sleep
import pytest
import allure


@allure.feature("销售管理-销售单")
class TestAddSalesOrder:
    @allure.story("新增销售单")
    @allure.title("国包用户创建销售单，产品为无码的，买方为临时客户,并直接出库")
    @allure.description("销售单页面，国包用户创建销售单，产品为无码的，买方为临时客户，并直接出库")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
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
        add.click_close_sales_order()


    @allure.story("新增销售单")
    @allure.title("国包用户，新建销售单，无码产品，买方为系统二代客户，并直接出库")
    @allure.description("销售单页面，国包用户，新建销售单，无码产品，买方为系统二代客户，并直接出库")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
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
        sleep(3)

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
        add.click_close_sales_order()


    @allure.story("新增销售单")
    @allure.title("销售单页面，二代用户新增销售单操作")
    @allure.description("销售单页面，二代用户新增销售单操作成功后，校验新增的销售单是否存在")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    def test_001_003(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Sales Management", "Sales Order")

        """销售订单页面，新建销售单、直接出库、筛选、然后快速收货场景功能"""
        """调用新增销售单用例"""
        add_sales = SalesOrderPage(drivers)
        add_sales.click_add_sales()
        add_sales.input_sales_buyer("EG000562")
        add_sales.input_sales_brand('TECNO')
        add_sales.input_sales_product("SPARK 6 Go 64+4 AQUA BLUE")
        add_sales.input_sales_quantity('1')
        add_sales.click_submit()
        add_sales.click_submit_OK()

        """二代用户，查询数据库最近新建的销售单ID"""
        user = SQL('DCR', 'test')
        sql = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        result = user.query_db(sql)
        order = result[0].get("order_code")
        status = result[0].get("status")
        if status == 0:
            sales_status = "Pending"
        """销售单页面，按销售单ID筛选销售单信息"""
        add_sales.input_sales_order_ID(order)
        add_sales.click_search()

        """获取列表，销售单ID与Status文本内容"""
        get_sales_order = add_sales.get_text_sales_id()
        get_status = add_sales.get_text_sales_status("Pending")
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        ValueAssert.value_assert_equal(get_sales_order, order)
        ValueAssert.value_assert_equal(get_status, sales_status)
        add_sales.click_close_sales_order()


    @allure.story("销售单出库")
    @allure.title("销售单页面，二代用户对新增的销售单进行出库操作")
    @allure.description("销售单页面，二代用户对新增的销售单进行出库操作成功后，校验销售单对应的状态是否更新为：Delivered")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
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
        user = SQL('DCR', 'test')
        sql = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        result = user.query_db(sql)
        order = result[0].get("order_code")
        # status = result[0].get("status")
        # if status == 80200000:
        #     sales_status = "Delivered"
        """销售单页面，按销售单ID筛选销售单信息"""
        delivery.input_sales_order_ID(order)
        delivery.click_search()

        """勾选新建的销售单，直接出库操作"""
        delivery.click_checkbox_orderID()
        delivery.click_Delivery_button()

        delivery.input_Payment_Mode('Wechat')
        delivery.input_imei(imei)
        delivery.click_check()
        delivery.click_submit_delivery()

        """销售单页面，按销售单ID筛选销售单信息，断言该条销售单对应的状态是否更新为：Delivered状态"""
        text_sales_order = delivery.get_text_sales_id()
        delivery.input_sales_order_ID(text_sales_order)
        delivery.click_search()
        text_status = delivery.get_text_sales_status("Delivered")
        """出库操作成功后，验证该条销售单对应的状态是否更新为：Delivered状态"""
        ValueAssert.value_assert_equal(text_status, "Delivered")
        delivery.click_close_sales_order()


@allure.feature("销售管理-销售单")
class TestDeleteSalesOrder:
    @allure.story("删除销售单")
    @allure.title("销售单页面，国包用户，删除新建的销售单操作")
    @allure.description("销售单页面，国包用户，对新建Pending状态的销售单进行删除操作")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    def test_002_001(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD40344201", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Sales Management", "Sales Order")

        """销售订单页面，新建销售单、直接出库、筛选、然后快速收货场景功能"""
        """调用新增销售单用例"""
        delete = SalesOrderPage(drivers)
        dom = DomAssert(drivers)

        delete.click_add_sales()
        delete.input_sales_buyer("BD2915")
        delete.input_sales_brand('TECNO')
        delete.input_sales_product("CAMON 15 Pro 128+6 ICE JADEITE")
        delete.input_sales_quantity('1')
        delete.click_submit()
        delete.click_submit_OK()

        """获取列表，销售单ID与Status文本内容"""
        get_sales_order = delete.get_text_sales_id()
        """销售单页面，按销售单ID筛选销售单信息"""
        delete.input_sales_order_ID(get_sales_order)
        delete.click_search()

        get_query_sales_order = delete.get_text_sales_id()
        ValueAssert.value_assert_equal(get_query_sales_order, get_sales_order)

        delete.click_delete_sales()
        delete.click_confirm_delete()
        dom.assert_att("Successfully")
        delete.click_close_sales_order()

if __name__ == '__main__':
    pytest.main(['SalesManagement_SalesOrder.py'])
