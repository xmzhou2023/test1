import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta
from project.DCR.page_object.SalesManagement_ReturnOrder import ReturnOrderPage,ReturnOrderQuery
from project.DCR.page_object.SalesManagement_SalesOrder import SalesOrderPage
from project.DCR.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from project.DCR.page_object.PurchaseManagement_InboundReceipt import InboundReceiptPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert, DomAssert
from public.base.assert_ui import SQLAssert
from libs.common.time_ui import sleep
from libs.common.connect_sql import *
from libs.config.conf import DOWNLOAD_PATH
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


@allure.feature("销售管理-退货单")
class TestReturnOrder:
    @allure.story("创建退货单")
    @allure.title("卖家创建无码销售单；然后卖家创建退货单，退货类型为Return To Seller，退无码产品")
    @allure.description("销售单页面，国包用户创建销售单，产品为无码的；卖家创建退货单，退货类型为Return To Seller，退无码产品")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
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
        logging.info("打印查询数据库的销售单 order_code{}".format(order_code))
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
        add.click_search()
        """获取列表，销售单ID与Status文本内容"""
        get_sales_order = add.get_text_sales_id()
        get_status = add.get_text_sales_status("Delivered")
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        ValueAssert.value_assert_equal(get_sales_order, order_code)
        ValueAssert.value_assert_equal(get_status, "Delivered")
        add.click_close_sales_order()
        """卖家创建退货单，退货类型为Return To Seller，退无码产品"""
        Base(drivers).refresh()
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Return Order")

        returnorder = ReturnOrderPage(drivers)
        """从数据库表，查询国包账号，最近新建的出库单ID"""
        sql2 = SQL('DCR', 'test')
        varsql2 = "select delivery_code from t_channel_delivery_ticket where warehouse_id='61735' and seller_id='1596874516539127' and buyer_id='1596874516539550' and status=80200000 order by created_time desc limit 1"
        result2 = sql2.query_db(varsql2)
        delivery_code = result2[0].get("delivery_code")
        logging.info("打印查询数据库的出库单 delivery_code{}".format(delivery_code))
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
        """点击提交按钮"""
        returnorder.click_Submit()
        DomAssert(drivers).assert_att("Submit Success!")
        """方法参数赋值给变量"""
        returnorder.input_Delivery_Orderid(delivery_code)
        returnorder.click_Search()
        """断言筛选退货列表页，获取退货单ID、退货出库单ID、退货状态与数据库表中查询的出库单ID对比是否一致"""
        get_return_order_id = returnorder.get_list_return_order_id()
        ValueAssert.value_assert_IsNoneNot(get_return_order_id)
        get_delivery_order_id = returnorder.get_text_deliveryID()
        get_status = returnorder.get_return_status()
        ValueAssert.value_assert_equal(get_delivery_order_id, delivery_code)
        ValueAssert.value_assert_equal("Approved", get_status)
        #returnorder.click_close_return_order()


    @allure.story("创建退货单")
    @allure.title("卖家创建有码出库单；然后卖家创建退货单，退货类型为Return To Seller、输入出库单号退货")
    @allure.description("销售单页面，国包用户创建有码出库单；卖家创建退货单，退货类型为Return To Seller、输入出库单号退货")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD40344201", "dcr123456")
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        """调用菜单栏，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        delivery = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        #sleep(2)
        imei = delivery.get_text_imei_inventory()
        logging.info("打印获取IMEI Inventory Query页面的IMEI:{}".format(imei))
        delivery.close_imei_inventory_query()
        """ 刷新页面 """
        delivery.click_refresh(drivers)
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Delivery Order")
        add_delivery = DeliveryOrderPage(drivers)
        """点击Add新增出库单按"""
        add_delivery.click_add()
        add_delivery.input_sub_buyer("BD2915")
        add_delivery.input_deli_pay_mode("Online")
        add_delivery.input_imei(imei)
        add_delivery.click_check()

        """断言检查出库单数量是否一致,扫码IMEI是否加载正确，是否有Success提示"""
        get_success = add_delivery.get_Deli_Scan_Record_Success()
        ValueAssert.value_assert_equal(get_success, "Success")
        get_imei = add_delivery.get_Deli_Scan_Record_IMEI(imei)
        ValueAssert.value_assert_equal(get_imei, imei)
        get_deli_quantity = add_delivery.get_delivery_quantity()
        get_order_deli_quantity = add_delivery.get_order_detail_deli_quantity()
        ValueAssert.value_assert_equal(get_deli_quantity, get_order_deli_quantity)

        """点击提交按钮"""
        add_delivery.click_submit()
        dom = DomAssert(drivers)
        try:
            affirm = add_delivery.get_text_submit_affirm()
            if affirm == "Submit":
                add_delivery.click_submit_affirm()
                dom.assert_att("Submit successfully")
        except Exception as e:
            #logging.info("打印日志{}".format(e))
            pass
        add_delivery.click_search()
        """从数据库表中，获取国包出库单ID，传给出库单筛选方法"""
        deli_sql = SQL('DCR', 'test')
        deli_varsql = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        deli_result = deli_sql.query_db(deli_varsql)
        order_code = deli_result[0].get("order_code")
        delivery_code = deli_result[0].get("delivery_code")
        logging.info("打印查询数据库的销售单 order_code{}".format(order_code))
        logging.info("打印查询数据库的出库单 delivery_code{}".format(delivery_code))

        add_delivery.input_salesorder(order_code)
        add_delivery.input_deliveryorder(delivery_code)
        add_delivery.click_search()

        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        salesorder = add_delivery.text_sales_order()
        deliveryorder = add_delivery.text_delivery_order()
        del_status = add_delivery.text_delivery_Status()

        """出库单页面，调用断言封装的方法，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        ValueAssert.value_assert_equal("On Transit", del_status)
        add_delivery.click_close_delivery_order()
        """卖家创建退货单，退货类型为Return To Seller，退有码产品，输入出库单号退货"""
        Base(drivers).refresh()
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


    @allure.story("创建退货单")
    @allure.title("卖家创建有码出库单；然后卖家创建退货单，退货类型为Return To Seller、扫IMEI退货")
    @allure.description("销售单页面，国包用户卖家创建有码出库单；卖家创建退货单，退货类型为Return To Seller、扫IMEI退货")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD40344201", "dcr123456")
        """打开Report Analysis->IMEI Inventory Query菜单"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        """调用菜单栏，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        delivery = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        imei = delivery.get_text_imei_inventory()
        logging.info("打印获取IMEI Inventory Query页面的IMEI:{}".format(imei))
        delivery.close_imei_inventory_query()
        """ 刷新页面 """
        delivery.click_refresh(drivers)
        """打开销售管理-打开出库单页面，创建有码出库单"""
        user.click_gotomenu("Sales Management", "Delivery Order")
        deli_return = DeliveryOrderPage(drivers)
        # """从数据库表查询国包BD403442仓库的库存IMEI 查询的IMEI已禁用 """
        # imei_varsql = "SELECT IMEI FROM  t_channel_warehouse_current_stock WHERE WAREHOUSE_ID ='62139' AND STATUS = 1  limit 1"
        # imei_sql = SQL('DCR', 'test')
        # imei_result = imei_sql.query_db(imei_varsql)
        # imei = imei_result[0].get("IMEI")
        # logging.info("打印数据库查询的 imei{}".format(imei))
        """点击Add新增出库单按"""
        deli_return.click_add()
        deli_return.input_sub_buyer("BD2915")
        deli_return.input_deli_pay_mode("Wallet")
        deli_return.input_imei(imei)
        deli_return.click_check()

        """断言检查出库单数量是否一致,扫码IMEI是否加载正确，是否有Success提示"""
        get_success = deli_return.get_Deli_Scan_Record_Success()
        ValueAssert.value_assert_equal(get_success, "Success")
        get_imei = deli_return.get_Deli_Scan_Record_IMEI(imei)
        ValueAssert.value_assert_equal(get_imei, imei)
        get_deli_quantity = deli_return.get_delivery_quantity()
        get_order_deli_quantity = deli_return.get_order_detail_deli_quantity()
        ValueAssert.value_assert_equal(get_deli_quantity, get_order_deli_quantity)

        """点击提交按钮"""
        deli_return.click_submit()
        dom = DomAssert(drivers)
        try:
            affirm = deli_return.get_text_submit_affirm()
            if affirm == "Submit":
                deli_return.click_submit_affirm()
                dom.assert_att("Submit successfully")
        except Exception as e:
            #logging.info("打印日志{}".format(e))
            pass
        sleep(3)

        """从数据库表中，获取国包出库单ID，传给出库单筛选方法"""
        deli_sql = SQL('DCR', 'test')
        deli_varsql = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
        deli_result = deli_sql.query_db(deli_varsql)
        order_code = deli_result[0].get("order_code")
        delivery_code = deli_result[0].get("delivery_code")
        logging.info("打印数据库查询的销售单ID order_code{}".format(order_code))
        logging.info("打印数据库查询的出库单ID delivery_code{}".format(delivery_code))

        deli_return.input_salesorder(order_code)
        deli_return.input_deliveryorder(delivery_code)
        deli_return.click_search()

        """出库单列表页面，获取页面，销售单与出库单的文本内容进行筛选"""
        salesorder = deli_return.text_sales_order()
        deliveryorder = deli_return.text_delivery_order()
        del_status = deli_return.text_delivery_Status()

        """出库单页面，调用断言封装的方法，比较页面获取的文本是否与查询的结果相等"""
        ValueAssert.value_assert_equal(salesorder, order_code)
        ValueAssert.value_assert_equal(deliveryorder, delivery_code)
        ValueAssert.value_assert_equal("On Transit", del_status)
        deli_return.click_close_delivery_order()

        """卖家创建退货单，退货类型为Return To Seller、退有码产品，扫IMEI退货"""
        Base(drivers).refresh()
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Return Order")
        return_order = ReturnOrderPage(drivers)

        """点击add退货按钮"""
        return_order.click_Add()
        return_order.click_Return_Type()
        return_order.radio_Boxid_IMEI()
        return_order.input_BoxID_IMEI(imei)
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
        ValueAssert.value_assert_equal(buyer_id, "BD2915")
        ValueAssert.value_assert_equal(return_quantity, "1")
        """点击提交按钮"""
        return_order.click_Submit()
        dom.assert_att("Submit Success!")
        sleep(2.5)
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


    @allure.story("创建退货单")
    @allure.title("退货单页面，撤回退货单，Pending Approval状态的订单可撤回")
    @allure.description("销售单页面，国包用户卖家创建无码出库单；二代用户快速收货；最后新建退货单，然后进行撤回退货单")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "EG40052202", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Delivery Order")
        """新建无码出库单操作"""
        delivery = DeliveryOrderPage(drivers)

        delivery.click_add()
        delivery.input_sub_buyer("NG20613")
        delivery.input_deli_pay_mode("Wechat")
        delivery.click_quantity_radio_button()
        delivery.click_quantity_add()
        delivery.click_quantity_product("OCD-M201")
        delivery.input_delivery_quantity('1')
        delivery.click_submit()
        DomAssert(drivers).assert_att("Submit successfully")
        sleep(2.5)
        delivery.click_search()
        get_delivery_order = delivery.get_delivery_order_text()
        """数据库断言,列表新建的出库单 与数据库的出库单是否一致"""
        deli_sql = SQLAssert('DCR', 'test')
        varsql2 = "select delivery_code from t_channel_delivery_ticket where warehouse_id='61735' and seller_id='1596874516539127' and buyer_id='1596874516539550' and status=80200000 order by created_time desc limit 1"
        deli_sql.assert_sql(get_delivery_order, varsql2)
        delivery.click_close_delivery_order()

        """二代用户快速收货操作"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "NG2061301", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Purchase Management", "Inbound Receipt")
        """新建无码出库单操作"""
        receipt = InboundReceiptPage(drivers)
        """从数据库表，查询最近新建的销售单ID与出库单ID"""
        sql3 = SQL('DCR', 'test')
        var_sql3 = "select delivery_code from t_channel_delivery_ticket where warehouse_id='61735' and seller_id='1596874516539127' and buyer_id='1596874516539550' and status=80200000 order by created_time desc limit 1"
        result = sql3.query_db(var_sql3)
        delivery_id = result[0].get("delivery_code")
        logging.info("打印查询数据库表新建的出库单ID:{}".format(delivery_id))

        receipt.input_deliveryOrder(delivery_id)
        receipt.click_search()
        receipt.select_checkbox()
        receipt.click_quick_received()
        """选择收货的仓库"""
        receipt.input_select_warehouse("WNG2061301")
        receipt.click_save()
        """获取收货提交成功提示语，断言是否包含Successfully提示语"""
        DomAssert(drivers).assert_att("Successfully")
        sleep(2)
        status = receipt.get_status_text()
        """ 二代收货页面，断言收货后Status更新为：Goods Receipt状态 """
        ValueAssert.value_assert_equal(status, "Goods Receipt")
        receipt.click_close_inbound_receipt()

        """二代用户打开退货页面，点击退货按钮，进行退货操作"""
        user.initialize_login(drivers, "NG2061301", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Return Order")
        recall_return = ReturnOrderPage(drivers)
        recall_return.click_Add()
        recall_return.click_Return_Type()
        recall_return.click_radio_quantity()
        recall_return.input_quantity_customer("NG20613")
        recall_return.input_quantity_delivery_order(delivery_id)

        recall_return.click_quantity_product("OCD-M201")
        recall_return.input_return_quantity('1')
        recall_return.click_Check()
        recall_return.click_Submit()
        DomAssert(drivers).assert_att("Submit Success!")

        """筛选新建的退货单数据，然后进行撤销操作"""
        recall_return.input_Delivery_Orderid(delivery_id)
        recall_return.click_Search()

        get_status = recall_return.get_return_status()
        ValueAssert.value_assert_equal(get_status, "Pending Approval")

        recall_return.click_checkbox()
        """点击更多操作，Recall 撤销功能"""
        recall_return.click_more_option_recall()
        """断言是否提示撤销成功，获取状态是否更新为Cancel状态"""
        DomAssert(drivers).assert_att("Approval successfully")
        get_status_cancel = recall_return.get_return_status()
        ValueAssert.value_assert_equal(get_status_cancel, "Cancel")
        #recall_return.click_close_return_order()

    @allure.story("创建退货单")
    @allure.title("The imei is already been activated")
    @allure.description("配置Return Need Check Activation Or Not，输入已激活imei提示：The imei is already been activated")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_005(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SN400001", "xLily6x")
        menu.click_gotomenu("Sales Management", "Return Order")
        delivery = ReturnOrderPage(drivers)
        delivery.click_Add()
        delivery.input_BoxID_IMEI('356209114219980')
        delivery.click_Check()
        delivery.assert_Scan_Record('356209114219980', '1', 'The imei is already been activated')
        delivery.input_BoxID_IMEI('356514118470111')
        delivery.click_Check()
        delivery.assert_Scan_Record('356514118470111')

    @allure.story("创建退货单")
    @allure.title("上月Return Date不可选择")
    @allure.description("上月Return Date不可选择")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_006(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SN400001", "xLily6x")
        menu.click_gotomenu("Sales Management", "Return Order")
        delivery = ReturnOrderPage(drivers)
        delivery.click_Add()
        month_date = datetime.now().date() - relativedelta(months=1)
        last_date = month_date.strftime("%Y-%m-%d")
        delivery.input_BasicInfo('Return Date', last_date)
        sleep(2)
        delivery.click_blank()
        data = delivery.get_BasicInfo('Return Date')
        ValueAssert.value_assert_Notequal(data, last_date)


@allure.feature("销售管理-退货单")
class TestReturnQuery:
    @allure.story("查询退货单")
    @allure.title("在退货单界面，按条件对退货单进行查询，判断结果和查询条件一致")
    @allure.description("在退货单界面，按条件对退货单进行查询，判断结果和查询条件一致")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "xiongbo92", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Return Order")

        page = ReturnOrderQuery(drivers)
        page.click_unfold()

        #查询上传日期并断言日期和查询结果一致
        page.input_return_date('2022-09-06','2022-09-06')
        page.click_search()
        result_date=page.get_table_txt(3)    #第3列
        ValueAssert.value_assert_In('2022-09-06',result_date)
        page.click_reset()

        #查询退单ID并断言退单ID和查询结果一致
        page.input_return_order('RDHK202211280031')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        result_date=page.get_table_txt(2)    #第3列
        ValueAssert.value_assert_In('RDHK202211280031',result_date)
        page.click_reset()

        #查询出库ID并断言出库单ID和查询结果一致
        page.input_delivery_order('02HK2211280000023')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        result_date=page.get_table_txt(4)    #第3列
        ValueAssert.value_assert_In('02HK2211280000023',result_date)
        page.click_reset()

        #查询退单品牌并断言退单品牌和查询结果一致
        page.input_brand('itel')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        result_date=page.get_table_txt(10)    #第3列
        ValueAssert.value_assert_In('itel',result_date)
        page.click_reset()

        #查询退单类型并断言退单类型和查询结果一致
        page.input_return_type('Return To Seller')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        result_date=page.get_table_txt(7)    #第7列
        ValueAssert.value_assert_In('Return To Seller',result_date)
        page.click_reset()

        #查询退单状态并断言退单状态和查询结果一致
        page.input_return_status('Approved')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        result_date=page.get_table_txt(6)    #第6列
        ValueAssert.value_assert_In('Approved',result_date)
        page.click_reset()

        #查询卖家并断言卖家和查询结果一致
        page.input_seller('BD403442')
        page.input_return_date('2022-10-20','2022-10-30')
        page.click_search()
        result_date=page.get_table_txt(15)    #第7列
        ValueAssert.value_assert_In('BD403442',result_date)
        page.click_reset()

        #查询买家并断言买家和查询结果一致
        page.input_buyer('BD2915')
        page.input_return_date('2022-10-20','2022-10-30')
        page.click_search()
        result_date=page.get_table_txt(20)    #第6列
        ValueAssert.value_assert_In('BD2915',result_date)
        page.click_reset()

        #查询买家仓库地址并断言买家仓库地址和查询结果一致
        page.input_buyer_area('Kaolack Dept')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        result_date=page.get_table_txt(37)    #第6列
        ValueAssert.value_assert_In('Kaolack Dept',result_date)
        page.click_reset()

        #查询卖家仓库地址并断言卖家仓库地址和查询结果一致
        page.input_seller_area('Kaolack Dept')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        result_date=page.get_table_txt(34)    #第7列
        ValueAssert.value_assert_In('Kaolack Dept',result_date)
        page.click_reset()

        #查询型号并断言型号和查询结果一致
        page.input_model('it6350')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        result_date=page.get_table_txt(11)    #第6列
        ValueAssert.value_assert_In('it6350',result_date)
        page.click_reset()

        #查询市场名字并断言市场名字和查询结果一致
        page.input_market_name('A48')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        result_date=page.get_table_txt(13)    #第6列
        ValueAssert.value_assert_In('A48',result_date)
        page.click_reset()

        #查询IMEI并断言IMEI和查询结果一致
        page.input_phone('352287800106087')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        page.click_detail()
        result_date=page.get_phone_detail()    #第6列
        ValueAssert.value_assert_In('352287800106087',result_date)
        page.close_phone_detail()
        page.click_reset()

        #查询卖方国家并断言卖方国家和查询结果一致
        page.input_seller_country('Nigeria')
        page.input_return_date('2022-11-20','2022-11-30')
        page.click_search()
        result_date=page.get_table_txt(17)    #第6列
        ValueAssert.value_assert_In('Nigeria',result_date)
        page.click_reset()

    @allure.story("导出退货单")
    @allure.title("在退货单界面，按条件对退货单进行查询，导出查询结果和查询条件一致")
    @allure.description("在退货单界面，按条件对退货单进行查询，导出查询结果和查询条件一致")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "xiongbo92", "dcr123456")
        """打开销售管理-打开出库单页面"""
        user.click_gotomenu("Sales Management", "Return Order")

        page = ReturnOrderQuery(drivers)
        page.click_unfold()

        # 查询卖方国家并断言卖方国家和查询结果一致
        page.input_return_date('2022-10-10', '2022-11-30')
        page.click_search()
        file_begin = int(len([lists for lists in os.listdir(DOWNLOAD_PATH) if os.path.isfile(os.path.join(DOWNLOAD_PATH, lists))]))
        page.click_export()
        #export_txt = page.export_status()
        #ValueAssert.value_assert_In('Download...', export_txt)

        file_then = int(len([lists for lists in os.listdir(DOWNLOAD_PATH) if os.path.isfile(os.path.join(DOWNLOAD_PATH, lists))]))
        ValueAssert.value_assert_Notequal(file_begin,file_then)
        page.click_export_detail()
        file_three = int(len([lists for lists in os.listdir(DOWNLOAD_PATH) if os.path.isfile(os.path.join(DOWNLOAD_PATH, lists))]))
        ValueAssert.value_assert_Notequal(file_three, file_then)
        page.click_reset()


    @allure.story("查询退货单")
    @allure.title("随机条件组合查询退货单")
    @allure.description("退货单页面，查询退货单的随机条件组合查询")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_003(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """变量"""
        query_dict = {
            'Return Order ID': 'RDHK202212020050',
            'Delivery/DN Order ID': '02HK2212020000015',
            'Brand': 'TECNO',
            'Return Date': '2022-12-02',
            'Status': 'Approved',
            'Return Type': 'Return To Seller',
            'Seller': 'CN100742',
            'Buyer': 'CN20058',
            'Seller Warehouse Region': 'Bangladesh District',
            'Buyer Warehouse Region': 'Transsion',
            'Model': 'T529',
            'Market Name': 'T529',
            'Seller Country': 'China',
            'IMEI': '351594528651620'
        }
        query = ReturnOrderQuery(drivers)
        user.click_gotomenu("Sales Management", "Return Order")
        query.click_unfold()
        query.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['SalesManagement_ReturnOrder.py'])
