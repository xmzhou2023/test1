from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.InventoryManagement_TransferOrder import TransferOrderPage
from project.DCR.page_object.Center_Process import SalesOrderPage
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
import logging
import allure
import pytest

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    for i in range(1):
        get_menu_class = menu.get_open_menu_class()
        class_value = "tags-view-item router-link-exact-active router-link-active active"
        if class_value == str(get_menu_class):
            menu.click_close_open_menu()

@allure.feature("库存管理-调拨单")
class TestNewRecallTransferOrder:
    @allure.story("创建调拨单，测回调拨单")  # 场景名称
    @allure.title("创建调拨单，撤回调拨单")  # 用例名称
    @allure.description("创建调拨单页面，两个不同客户之间的调拨，然后撤回调拨单，形成闭环")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")

        """打开Report Analysis->IMEI Inventory Query菜单"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        """调用菜单栏，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        get_imei = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        get_imei.click_unfold()
        get_imei.input_warehouse_query('WBD291502')
        get_imei.click_inventory_search()
        imei = get_imei.get_text_imei_inventory()
        logging.info("打印从IMEI Inventory Query页面，获取的imei:{}".format(imei))
        get_imei.click_close_imei_inventory()
        """刷新页面"""
        get_imei.click_refresh(drivers)

        user.click_gotomenu("Inventory Management", "Transfer Order")
        transfer = TransferOrderPage(drivers)
        transfer.click_create()
        transfer.click_transfer_from_customer('BD2915 lhmSubdealer001 ')
        transfer.click_transfer_to_customer('NG20613 xylSub dealer')
        transfer.input_scan_imei(imei)
        """点击Check 按钮，校验IMEI是否存在此仓库"""
        transfer.click_check()
        """断言输入的IMEI是否验证通过"""
        get_scanned = transfer.get_scanned()
        get_deli_quantity = transfer.get_delivery_quantity()
        get_scan_record_imei = transfer.get_scan_record_imei(imei)
        get_scan_record_success = transfer.get_scan_record_success()
        ValueAssert.value_assert_equal(get_scanned, get_deli_quantity)
        ValueAssert.value_assert_equal(imei, get_scan_record_imei)
        ValueAssert.value_assert_In('Success', get_scan_record_success)
        """点击提交按钮"""
        transfer.click_submit()
        DomAssert(drivers).assert_att('Successfully')
        transfer.click_submit_ok()

        """断言列表展示新增的调拨单，状态是否正确"""
        get_transfer_id = transfer.get_list_transfer_id()
        logging.info("打印获取Transfer Order列表的Transfer ID字段内容{}".format(get_transfer_id))
        get_audited = transfer.get_list_order_status()
        get_receive = transfer.get_list_receipt_status()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Audited', get_audited)
        ValueAssert.value_assert_equal('No Receive', get_receive)

        """ 撤回新增的TransferOrder"""
        """筛选Transfer Order页面，Received已经收货状态数据"""
        transfer.click_unfold()
        transfer.input_transfer_id_query(get_transfer_id)
        transfer.click_receipt_status_query('No Receive')
        transfer.click_search()

        transfer.click_first_checkbox()
        transfer.click_more_option_recall_confirm()
        DomAssert(drivers).assert_att('Successfully')

        get_order_status = transfer.get_list_order_status()
        get_receipt_status = transfer.get_list_receipt_status()
        ValueAssert.value_assert_equal('Recall', get_order_status)
        ValueAssert.value_assert_equal('No Receive', get_receipt_status)


@allure.feature("库存管理-调拨单")
class TestConfirmReceiptTransferOrder:
    @allure.story("创建调拨单，然后被调拨方收货")
    @allure.title("创建调拨单，然后被调拨方收货")
    @allure.description("NG2061301客户创建调拨单，NG2061303客户收货")
    @allure.severity("critical")
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "NG2061301", "dcr123456")

        """打开Report Analysis->IMEI Inventory Query菜单"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        """调用菜单栏，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        get_imei = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        get_imei.click_unfold()
        get_imei.input_warehouse_query('WNG2061301')
        get_imei.click_inventory_search()
        imei = get_imei.get_text_imei_inventory()
        logging.info("打印从IMEI Inventory Query页面，获取的imei:{}".format(imei))
        get_imei.click_close_imei_inventory()

        """刷新页面"""
        get_imei.click_refresh(drivers)
        user.click_gotomenu("Inventory Management", "Transfer Order")

        receipt = TransferOrderPage(drivers)
        receipt.click_create()
        receipt.click_transfer_from_customer('NG20613 xylSub dealer ')
        receipt.click_transfer_from_warehouse('WNG2061301')
        receipt.click_transfer_to_customer('NG20613 xylSub dealer')
        receipt.click_transfer_to_warehouse('WNG2061304')
        receipt.input_scan_imei(imei)
        """点击Check 按钮，校验IMEI是否存在此仓库"""
        receipt.click_check()
        """断言输入的IMEI是否验证通过"""
        get_scanned = receipt.get_scanned()
        get_deli_quantity = receipt.get_delivery_quantity()
        get_scan_record_success = receipt.get_scan_record_success()
        ValueAssert.value_assert_equal(get_scanned, get_deli_quantity)
        ValueAssert.value_assert_In('Success', get_scan_record_success)
        """点击提交按钮"""
        receipt.click_submit()
        DomAssert(drivers).assert_att('Successfully')
        receipt.click_submit_ok()

        """断言列表展示新增的调拨单，状态是否正确"""
        get_transfer_id = receipt.get_list_transfer_id()
        logging.info("打印获取Transfer Order列表,新建的Transfer ID：{}".format(get_transfer_id))
        get_audited = receipt.get_list_order_status()
        get_receive = receipt.get_list_receipt_status()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Audited', get_audited)
        ValueAssert.value_assert_equal('No Receive', get_receive)

        """ NG2061303 被调拨的客户登录，确认收货操作 """
        user.initialize_login(drivers, "NG2061303", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")
        """筛选待收货状态的调拨单"""
        receipt.click_unfold()
        receipt.input_transfer_id_query(get_transfer_id)
        receipt.click_receipt_status_query('No Receive')
        receipt.click_search()

        """未勾选复选框时，点击Confirm Receipt操作，提示 请选择记录"""
        receipt.click_confirm_receipt1()
        DomAssert(drivers).assert_att('Please select a record')
        sleep(1)
        """勾选第一个复选框后，点击Confirm Receipt 确认收货操作"""
        receipt.click_first_checkbox()
        receipt.click_confirm_receipt('已收货')
        DomAssert(drivers).assert_att('Successfully')

        """筛选Received 已收货状态的记录，进行断言,调拨单号是否正确，状态是否更新为Received状态 """
        receipt.click_receipt_status_query('Received')
        receipt.click_search()
        transfer_id1 = receipt.get_list_transfer_id()
        get_audited = receipt.get_list_order_status()
        get_received = receipt.get_list_receipt_status()
        ValueAssert.value_assert_equal(get_transfer_id, transfer_id1)
        ValueAssert.value_assert_equal('Audited', get_audited)
        ValueAssert.value_assert_equal('Received', get_received)


@allure.feature("库存管理-调拨单")
class TestViewIMEIDetailTransfer:
    @allure.story("查看调拨单IMEI详情")  # 场景名称
    @allure.title("查看调拨单IMEI详情")  # 用例名称
    @allure.description("调拨单页面，点击IMEI Detail功能，查看调拨单IMEI详情")
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")

        detail = TransferOrderPage(drivers)
        """根据Transfer ID条件筛选"""
        transfer_id = detail.get_list_transfer_id()
        detail.input_transfer_id_query(transfer_id)
        detail.click_search()

        transfer_id2 = detail.get_list_transfer_id()
        ValueAssert.value_assert_equal(transfer_id, transfer_id2)
        get_list_brand = detail.get_list_field('Get list Brand')
        get_list_item = detail.get_list_field('Get list item')
        get_list_model = detail.get_list_field('Get list Model')
        get_list_cust = detail.get_list_field('Get list Transfer From Cust')

        """点击查看IMEI Detail详情功能"""
        detail.click_imei_detail()
        get_detail_transfer = detail.get_list_field('Get Detail Transfer ID')
        get_detail_brand = detail.get_list_field('Get Detail Brand')
        get_detail_item = detail.get_list_field('Get Detail Item')
        get_detail_model = detail.get_list_field('Get Detail Model')
        get_detail_imei = detail.get_list_field('Get Detail IMEI')
        get_detail_customer = detail.get_list_field('Get Detail Customer Name')

        ValueAssert.value_assert_equal(transfer_id2, get_detail_transfer)
        ValueAssert.value_assert_equal(get_list_brand, get_detail_brand)
        ValueAssert.value_assert_equal(get_list_item, get_detail_item)
        ValueAssert.value_assert_equal(get_list_model, get_detail_model)
        ValueAssert.value_assert_IsNoneNot(get_detail_imei)
        ValueAssert.value_assert_In(get_detail_customer, get_list_cust)
        detail.click_close_imei_detail()


@allure.feature("库存管理-调拨单")
class TestRecallTransferOrder:
    @allure.story("撤回调拨单")  # 场景名称
    @allure.title("撤回Received状态的调拨单")  # 用例名称
    @allure.description("调拨单页面，已收货Received状态的调拨单，Recall撤回操作，不支持撤回")
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")

        recall = TransferOrderPage(drivers)
        """筛选Transfer Order页面，Received已经收货状态数据"""
        recall.click_unfold()
        recall.click_receipt_status_query('Received')
        recall.click_search()
        recall.click_first_checkbox()
        """对已收货Received状态的数据，进行Recall撤回操作"""
        recall.click_more_option_recall()
        DomAssert(drivers).assert_att('Only No Receive or Audited can confirm receipt')

if __name__ == '__main__':
    pytest.main(['InventoryManagement_TransferOrder.py'])
