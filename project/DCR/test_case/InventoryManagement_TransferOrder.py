from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.InventoryManagement_TransferOrder import TransferOrderPage
from project.DCR.page_object.Center_Process import SalesOrderPage
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
from public.base.basics import Base
import logging
import allure
import pytest

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("库存管理-调拨单")
class TestQueryTransferOrder:
    @allure.story("查询调拨单数据")  # 场景名称
    @allure.title("库存管理页面，按单个条件查询 调拨单记录")  # 用例名称
    @allure.description("库存管理页面，按单个条件查询 调拨单记录")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "xiongbo92", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")
        query_transfer = TransferOrderPage(drivers)
        query_transfer.click_unfold('Unfold')
        """按Transfer ID条件，筛选调拨单记录"""
        query_transfer.transfer_order_input_query('Transfer Transfer ID input query', 'Transfer Transfer ID input query', 'TFHK202212060004')
        query_transfer.click_search_reset('Search')
        query_transfer.assert_search_transfer_order_field('Transfer ID', 'TFHK202212060004')
        get_total = query_transfer.get_transfer_order_total_text()
        ValueAssert.value_assert_equal('1', get_total)
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Transfer From Customer 条件，筛选调拨单记录"""
        query_transfer.transfer_order_input_select_query('From Customer click query', 'From Customer input query', 'From Customer select query', 'NG20613', 'NG20613')
        query_transfer.click_search_reset('Search')
        query_transfer.assert_search_transfer_order_field('Transfer From Customer', 'xylSub dealer(NG20613)')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Transfer To Customer条件，筛选调拨单记录"""
        query_transfer.transfer_order_input_select_query('Transfer To Customer click query', 'Transfer To Customer input query', 'Transfer To Customer select query', 'BD2915', 'BD2915')
        query_transfer.click_search_reset('Search')
        query_transfer.assert_search_transfer_order_field('Transfer To Customer', 'lhmSubdealer001(BD2915)')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Transfer From Warehouse条件，筛选调拨单记录"""
        query_transfer.transfer_order_input_select_query('Transfer From Warehouse click query', 'Transfer From Warehouse input query', 'Transfer From Warehouse select query', 'WNG2061301', 'WNG2061301')
        query_transfer.click_search_reset('Search')
        query_transfer.assert_search_transfer_order_field('Transfer From Warehouse', 'W.H LhmSub dealer(WNG2061301)')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Transfer To Warehouse条件，筛选调拨单记录"""
        query_transfer.transfer_order_input_select_query('Transfer To Warehouse click query', 'Transfer To Warehouse input query', 'Transfer To Warehouse select query', 'WBD291502', 'WBD291502')
        query_transfer.click_search_reset('Search')
        query_transfer.assert_search_transfer_order_field('Transfer To Warehouse', 'W.H lhmSubdealer001(WBD291502)')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Create Date 条件，筛选调拨单记录"""
        query_transfer.input_transfer_create_start_date('2022-12-06')
        query_transfer.input_transfer_create_end_date('2022-12-06')
        """点击空白区域"""
        query_transfer.click_create_date_label()
        query_transfer.click_search_reset('Search')
        query_transfer.assert_contains_transfer_order_field('Create Date', '2022-12-06')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Transfer To Warehouse条件，筛选调拨单记录"""
        query_transfer.transfer_order_input_select_query('Transfer To Warehouse click query', 'Transfer To Warehouse input query', 'Transfer To Warehouse select query', 'WBD291502', 'WBD291502')
        query_transfer.click_search_reset('Search')
        query_transfer.assert_search_transfer_order_field('Transfer To Warehouse', 'W.H lhmSubdealer001(WBD291502)')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Receipt Status条件，筛选调拨单记录"""
        query_transfer.transfer_order_click_query('Transfer Receipt Status click query', 'Transfer Receipt Status select query', 'Rejected')
        query_transfer.click_search_reset('Search')
        query_transfer.assert_search_transfer_order_field('Receipt Status', 'Rejected')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Transfer Type条件，筛选调拨单记录"""
        query_transfer.transfer_order_click_query('Transfer Transfer Type click query', 'Transfer Transfer Type select query', 'To Customer')
        query_transfer.click_search_reset('Search')
        query_transfer.assert_search_transfer_order_field('Transfer Type', 'To Customer')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Brand条件，筛选调拨单记录"""
        query_transfer.transfer_order_input_select_query('Transfer Brand click query', 'Transfer Brand input query', 'Transfer Brand select query', 'itel', 'itel')
        query_transfer.click_search_reset('Search')
        query_transfer.click_create_date_label
        query_transfer.assert_search_transfer_order_field('Brand', 'itel')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Model条件，筛选调拨单记录"""
        query_transfer.transfer_order_input_select_query('Transfer Model click query', 'Transfer Model input query', 'Transfer Model select query', 'it5607', 'it5607')
        query_transfer.click_search_reset('Search')
        query_transfer.assert_search_transfer_order_field('Model', 'it5607')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按Market Name条件，筛选调拨单记录"""
        query_transfer.transfer_order_input_select_query('Transfer Market Name click query', 'Transfer Market Name input query', 'Transfer Market Name select query', 'POWER 100', 'POWER 100')
        query_transfer.click_search_reset('Search')
        query_transfer.assert_search_transfer_order_field('Market Name', 'POWER 100')
        """重置筛选条件"""
        query_transfer.click_search_reset('Reset')

        """按IMEI条件，筛选调拨单记录"""
        query_transfer.transfer_order_input_query('Transfer IMEI click query', 'Transfer IMEI input query', '354196616529945')
        query_transfer.click_search_reset('Search')
        get_total = query_transfer.get_transfer_order_total_text()
        if int(get_total) > 1:
            logging.info("查询Transfer Order列表，能查询到符合条件的数据，分页总条数大于1：{}".format(get_total))
        """重置筛选条件"""
        query_transfer.transfer_click_imei_detail()
        query_transfer.assert_search_transfer_order_field('IMEI', '354196616529945')
        query_transfer.close_transfer_imei_detail()
        query_transfer.click_search_reset('Reset')



    @allure.story("查看调拨单IMEI详情")  # 场景名称
    @allure.title("查看调拨单IMEI详情")  # 用例名称
    @allure.description("调拨单页面，点击IMEI Detail功能，查看调拨单IMEI详情")
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")
        detail = TransferOrderPage(drivers)
        """根据Transfer ID条件筛选挑拨单数据"""
        transfer_id = detail.get_list_transfer_order_id()
        detail.input_transfer_order_id_query(transfer_id)
        detail.click_search_reset('Search')
        sleep(1)
        """获取调拨单列表字段内容"""
        transfer_id2 = detail.get_list_transfer_order_id()
        ValueAssert.value_assert_equal(transfer_id, transfer_id2)
        get_list_brand = detail.get_list_field('Get list Brand')
        get_list_item = detail.get_list_field('Get list item')
        get_list_model = detail.get_list_field('Get list Model')
        get_list_from_cust = detail.get_list_field('Get list Transfer From Cust')
        """点击查看IMEI Detail详情页，获取列表字段内容，进行断言"""
        detail.click_transfer_imei_detail()
        get_detail_transfer = detail.get_list_field('Get Detail Transfer ID')
        get_detail_brand = detail.get_list_field('Get Detail Brand')
        get_detail_item = detail.get_list_field('Get Detail Item')
        get_detail_model = detail.get_list_field('Get Detail Model')
        get_detail_imei = detail.get_list_field('Get Detail IMEI')
        get_detail_customer = detail.get_list_field('Get Detail Customer Name')
        """IMEI Detail详情页，断言详情页列表字段内容是否正确"""
        ValueAssert.value_assert_equal(transfer_id2, get_detail_transfer)
        ValueAssert.value_assert_equal(get_list_brand, get_detail_brand)
        ValueAssert.value_assert_equal(get_list_item, get_detail_item)
        ValueAssert.value_assert_equal(get_list_model, get_detail_model)
        ValueAssert.value_assert_IsNoneNot(get_detail_imei)
        ValueAssert.value_assert_In(get_detail_customer, get_list_from_cust)
        detail.close_transfer_imei_detail()



@allure.feature("库存管理-调拨单")
class TestNewRecallTransferOrder:
    @allure.story("创建调拨单，No Receive未收货状态的调拨单,可撤回调拨单")  # 场景名称
    @allure.title("创建调拨单，No Receive未收货状态的调拨单,可撤回调拨单")  # 用例名称
    @allure.description("创建调拨单页面，两个不同客户之间的调拨，未收货状态，然后撤回调拨单")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")
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
        get_transfer_id = transfer.get_list_transfer_order_id()
        logging.info("打印获取Transfer Order列表的Transfer ID字段内容{}".format(get_transfer_id))
        get_audited = transfer.get_list_transfer_order_status()
        get_receive = transfer.get_list_transfer_receipt_status()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Audited', get_audited)
        ValueAssert.value_assert_equal('No Receive', get_receive)

        """ 撤回新增的TransferOrder"""
        """筛选Transfer Order页面，Received已经收货状态数据"""
        transfer.click_unfold('Unfold')
        """根据transfer ID条件筛选调拨单"""
        transfer.input_transfer_order_id_query(get_transfer_id)
        transfer.click_transfer_receipt_status_query('No Receive')
        """点击查询按钮"""
        transfer.click_search_reset('Search')
        sleep(1)
        """勾选复选框"""
        transfer.click_transfer_order_checkbox()
        """点击recall撤回功能"""
        transfer.click_more_option_recall_confirm()
        """弹出成功提示语断言"""
        DomAssert(drivers).assert_att('Successfully')
        get_order_status = transfer.get_list_transfer_order_status()
        get_receipt_status = transfer.get_list_transfer_receipt_status()
        ValueAssert.value_assert_equal('Recall', get_order_status)
        ValueAssert.value_assert_equal('No Receive', get_receipt_status)



    @allure.story("创建调拨单(同个客户：不同仓库之间调拨)，然后被调拨方收货")
    @allure.title("创建调拨单(同个客户：不同仓库之间调拨)，然后被调拨方收货")
    @allure.description("NG2061301客户创建调拨单，NG2061303客户收货")
    @allure.severity("critical")
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "NG2061301", "dcr123456")
        """调用菜单栏方法，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        get_imei = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        get_imei.click_unfold()
        get_imei.input_warehouse_query('WNG2061301')
        get_imei.select_brand_query('itel')
        get_imei.click_inventory_search()
        imei = get_imei.get_text_imei_inventory()
        logging.info("打印从IMEI Inventory Query页面，获取的imei:{}".format(imei))
        get_imei.click_close_imei_inventory()

        """刷新页面"""
        get_imei.click_refresh(drivers)
        """进入Transfer Order创建同级调拨单，不同客户之间调拨"""
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
        get_transfer_id = receipt.get_list_transfer_order_id()
        logging.info("打印获取Transfer Order列表,新建的Transfer ID：{}".format(get_transfer_id))
        get_audited = receipt.get_list_transfer_order_status()
        get_receive = receipt.get_list_transfer_receipt_status()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Audited', get_audited)
        ValueAssert.value_assert_equal('No Receive', get_receive)

        """ NG2061303 被调拨的客户登录，确认收货操作 """
        user.initialize_login(drivers, "NG2061303", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")
        """筛选待收货状态的调拨单"""
        receipt.click_unfold('Unfold')
        receipt.input_transfer_order_id_query(get_transfer_id)
        receipt.click_transfer_receipt_status_query('No Receive')
        receipt.click_search_reset('Search')
        sleep(1)
        """未勾选复选框时，点击Confirm Receipt操作，提示 请选择记录"""
        receipt.click_confirm_receipt1()
        DomAssert(drivers).assert_att('Please select a record')
        sleep(1)
        """勾选第一个复选框后，点击Confirm Receipt 确认收货操作"""
        receipt.click_transfer_order_checkbox()
        receipt.click_transfer_confirm_receipt('已收货', 'Confirm Receipt')
        DomAssert(drivers).assert_att('Successfully')
        """筛选Received 已收货状态的记录，进行断言,调拨单号是否正确，状态是否更新为Received状态 """
        receipt.click_transfer_receipt_status_query('Received')
        receipt.click_search_reset('Search')
        sleep(1)
        transfer_id1 = receipt.get_list_transfer_order_id()
        get_audited = receipt.get_list_transfer_order_status()
        get_received = receipt.get_list_transfer_receipt_status()
        ValueAssert.value_assert_equal(get_transfer_id, transfer_id1)
        ValueAssert.value_assert_equal('Audited', get_audited)
        ValueAssert.value_assert_equal('Received', get_received)


    @allure.story("创建调拨单(同级调拨：不同客户间调拨)，from调拨方收货无权限, 然后被调拨方可以收货")
    @allure.title("创建调拨单(同级调拨：不同客户间调拨)，from调拨方收货无权限, 然后被调拨方可以收货")
    @allure.description("BD291501客户创建调拨单，NG2061301客户收货")
    @allure.severity("critical")
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")
        """调用菜单栏方法，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        get_imei = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        get_imei.click_unfold()
        get_imei.input_warehouse_query('WBD291502')
        get_imei.select_brand_query('itel')
        get_imei.click_inventory_search()
        imei_itel = get_imei.get_text_imei_inventory()
        logging.info("打印从IMEI Inventory Query页面，获取的imei:{}".format(imei_itel))
        get_imei.click_close_imei_inventory()

        """刷新页面"""
        get_imei.click_refresh(drivers)
        """进入Transfer Order创建同个客户，不同仓库之间的调拨单"""
        user.click_gotomenu("Inventory Management", "Transfer Order")
        transfer = TransferOrderPage(drivers)
        transfer.click_create()
        transfer.click_transfer_from_customer('BD2915 lhmSubdealer001 ')
        transfer.click_transfer_to_customer('NG20613 xylSub dealer')
        transfer.click_transfer_to_warehouse('WNG2061301')
        transfer.input_scan_imei(imei_itel)
        """点击Check 按钮，校验IMEI是否存在此仓库"""
        transfer.click_check()
        """断言输入的IMEI是否验证通过"""
        get_scanned = transfer.get_scanned()
        get_deli_quantity = transfer.get_delivery_quantity()
        get_scan_record_imei = transfer.get_scan_record_imei(imei_itel)
        get_scan_record_success = transfer.get_scan_record_success()
        ValueAssert.value_assert_equal(get_scanned, get_deli_quantity)
        ValueAssert.value_assert_equal(imei_itel, get_scan_record_imei)
        ValueAssert.value_assert_In('Success', get_scan_record_success)
        """点击提交按钮"""
        transfer.click_submit()
        DomAssert(drivers).assert_att('Successfully')
        transfer.click_submit_ok()
        """断言列表展示新增的调拨单，状态是否正确"""
        get_transfer_id = transfer.get_list_transfer_order_id()
        logging.info("打印获取Transfer Order列表的Transfer ID字段内容{}".format(get_transfer_id))
        get_audited = transfer.get_list_transfer_order_status()
        get_receive = transfer.get_list_transfer_receipt_status()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Audited', get_audited)
        ValueAssert.value_assert_equal('No Receive', get_receive)

        """from调拨方收货操作，提示：无权限收货"""
        """筛选待收货状态的调拨单"""
        transfer.input_transfer_order_id_query(get_transfer_id)
        transfer.click_search_reset('Search')
        sleep(1)
        """勾选第一个复选框后，点击Confirm Receipt 确认收货操作"""
        transfer.click_transfer_order_checkbox()
        transfer.click_transfer_confirm_receipt('已收货', 'Confirm Receipt')
        get_confirm_receipt_button = transfer.get_list_field('Transfer Confirm Receipt Button')
        ValueAssert.value_assert_equal("Confirm Receipt", get_confirm_receipt_button)
        """关闭Transfer Order确认收货窗口"""
        transfer.close_transfer_receipt_remark()

        """ NG2061303 被调拨的客户登录，确认收货操作 """
        user.initialize_login(drivers, "NG2061301", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")
        """筛选待收货状态的调拨单"""
        transfer.click_unfold('Unfold')
        transfer.input_transfer_order_id_query(get_transfer_id)
        transfer.click_transfer_receipt_status_query('No Receive')
        transfer.click_search_reset('Search')
        sleep(1)
        """获取Transfer Order列表字段内容"""
        transfer_id2 = transfer.get_list_transfer_order_id()
        get_list_brand = transfer.get_list_field('Get list Brand')
        get_list_item = transfer.get_list_field('Get list item')
        get_list_model = transfer.get_list_field('Get list Model')
        get_list_cust = transfer.get_list_field('Get list Transfer From Cust')
        """点击查看IMEI Detail详情页，获取列表字段内容，进行断言是否匹配"""
        transfer.click_transfer_imei_detail()
        get_detail_transfer = transfer.get_list_field('Get Detail Transfer ID')
        get_detail_brand = transfer.get_list_field('Get Detail Brand')
        get_detail_item = transfer.get_list_field('Get Detail Item')
        get_detail_model = transfer.get_list_field('Get Detail Model')
        get_detail_imei = transfer.get_list_field('Get Detail IMEI')
        get_detail_customer = transfer.get_list_field('Get Detail Customer Name')
        """IMEI Detail详情页，断言详情页列表字段内容是否正确"""
        ValueAssert.value_assert_equal(transfer_id2, get_detail_transfer)
        ValueAssert.value_assert_equal(get_list_brand, get_detail_brand)
        ValueAssert.value_assert_equal(get_list_item, get_detail_item)
        ValueAssert.value_assert_equal(get_list_model, get_detail_model)
        ValueAssert.value_assert_IsNoneNot(get_detail_imei)
        ValueAssert.value_assert_In(get_detail_customer, get_list_cust)
        transfer.close_transfer_imei_detail()

        """勾选第一个复选框后，点击Confirm Receipt 确认收货操作"""
        transfer.click_transfer_order_checkbox()
        transfer.click_transfer_confirm_receipt('已收货', 'Confirm Receipt')
        DomAssert(drivers).assert_att('Successfully')
        """筛选Received 已收货状态的记录，进行断言,调拨单号是否正确，状态是否更新为Received状态 """
        transfer.click_transfer_receipt_status_query('Received')
        transfer.click_search_reset('Search')
        sleep(1)
        transfer_id1 = transfer.get_list_transfer_order_id()
        get_audited = transfer.get_list_transfer_order_status()
        get_received = transfer.get_list_transfer_receipt_status()
        ValueAssert.value_assert_equal(get_transfer_id, transfer_id1)
        ValueAssert.value_assert_equal('Audited', get_audited)
        ValueAssert.value_assert_equal('Received', get_received)


    @allure.story("导入调拨单，导入成功断言，然后to 方退货操作，退货from方，单据更新为拒绝状态")
    @allure.title("导入调拨单(同级客户调拨：不同客户间调拨)，导入成功断言，然后to 方退货操作，退货from方，单据更新为拒绝状态")
    @allure.description("NG2061301客户导入调拨单，BD291501客户退货操作")
    @allure.severity("normal")
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "NG2061301", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")
        import_transfer = TransferOrderPage(drivers)
        """Transfer Order页面，未点击Upload按钮，直接点击Save，提示请上传文件"""
        import_transfer.click_transfer_order_import()
        DomAssert(drivers).assert_att('Please upload first.')
        sleep(0.5)
        """Transfer Order页面，上传文件导入一条正常的IMEI记录，能导入成功"""
        import_transfer.upload_true_file('TransferOrderTemplate.xlsx')
        """筛选当天导入的记录"""
        today = Base(drivers).get_datetime_today()
        import_transfer.input_import_date(today)
        import_transfer.click_search_reset('Search')
        """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
        get_file_name = import_transfer.get_list_field('Get Import Record File Name')
        get_status = import_transfer.get_list_field('Get Import Record Status')
        get_total = import_transfer.get_list_field('Get Import Record Total')
        get_success = import_transfer.get_list_field('Get Import Record Success')
        get_failed = import_transfer.get_list_field('Get Import Record Failed')
        get_import_date = import_transfer.get_list_field('Get Import Import Date')
        ValueAssert.value_assert_equal('TransferOrderTemplate.xlsx', get_file_name)
        ValueAssert.value_assert_equal('Upload Successfully', get_status)
        ValueAssert.value_assert_equal('1', get_total)
        ValueAssert.value_assert_equal('1', get_success)
        ValueAssert.value_assert_equal('0', get_failed)
        ValueAssert.value_assert_In(today, get_import_date)
        """关闭当前打开的菜单"""
        user.click_close_open_menu()

        """to方登录，打开transfer Order菜单，进行退货操作"""
        user.initialize_login(drivers, "BD291501", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")
        """根据Transfer ID条件筛选挑拨单数据"""
        transfer_id = import_transfer.get_list_transfer_order_id()
        import_transfer.input_transfer_order_id_query(transfer_id)
        import_transfer.click_search_reset('Search')
        sleep(1)
        """勾选第一个复选框后，点击Confirm Receipt 确认收货操作"""
        import_transfer.click_transfer_order_checkbox()
        import_transfer.click_transfer_return_goods('退货', 'Return Goods')
        DomAssert(drivers).assert_att('Successfully')
        """获取Transfer Order列表，Receipt Status状态是否更新为Rejected"""
        get_audited = import_transfer.get_list_transfer_order_status()
        get_receive = import_transfer.get_list_transfer_receipt_status()
        ValueAssert.value_assert_equal('Audited', get_audited)
        ValueAssert.value_assert_equal('Rejected', get_receive)

        """断言NG2061301账号IMEI Inventory Query是否能查询到退回的IMEI"""
        user.initialize_login(drivers, "NG2061301", "dcr123456")
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        assert_imei = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        assert_imei.imei_inventory_query_imei('354196616530083')
        get_imei = assert_imei.get_text_imei_inventory1()
        ValueAssert.value_assert_equal("354196616530083", get_imei)


    @allure.story("导入调拨单，导入文件一条IMEI成功，其他3条IMEI导入失败，然后to方退货导入成功的一条IMEI，退货from方，单据更新为拒绝状态")
    @allure.title("导入调拨单(同级客户调拨：不同客户间调拨)，然后to 方退货操作，退货from方，单据更新为拒绝状态")
    @allure.description("NG2061301客户导入调拨单，导入一条IMEI成功，其他3条IMEI导入失败，BD291501客户退货操作")
    @allure.severity("normal")
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_005(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "NG2061301", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")
        import_transfer = TransferOrderPage(drivers)
        """Transfer Order页面，未点击Upload按钮，直接点击Save，提示请上传文件"""
        import_transfer.click_transfer_order_import()
        DomAssert(drivers).assert_att('Please upload first.')
        sleep(0.5)
        """Transfer Order页面，上传文件导入多条IMEI，其中一条IMEI成功，其他IMEI失败"""
        import_transfer.upload_true_file('TransferOrderTemplate导入多条其中一条成功.xlsx')
        """筛选当天导入的记录"""
        today = Base(drivers).get_datetime_today()
        import_transfer.input_import_date(today)
        import_transfer.click_search_reset('Search')
        """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
        get_file_name = import_transfer.get_list_field('Get Import Record File Name')
        get_status = import_transfer.get_list_field('Get Import Record Status')
        get_total = import_transfer.get_list_field('Get Import Record Total')
        get_success = import_transfer.get_list_field('Get Import Record Success')
        get_failed = import_transfer.get_list_field('Get Import Record Failed')
        get_import_date = import_transfer.get_list_field('Get Import Import Date')
        ValueAssert.value_assert_equal('TransferOrderTemplate导入多条其中一条成功.xlsx', get_file_name)
        ValueAssert.value_assert_equal('Upload Successfully', get_status)
        ValueAssert.value_assert_equal('4', get_total)
        ValueAssert.value_assert_equal('1', get_success)
        ValueAssert.value_assert_equal('3', get_failed)
        ValueAssert.value_assert_In(today, get_import_date)
        """关闭当前打开的菜单"""
        user.click_close_open_menu()

        """to方登录，打开transfer Order菜单，进行退货操作"""
        user.initialize_login(drivers, "BD291501", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")
        """根据Transfer ID条件筛选挑拨单数据"""
        get_list_transfer_id1 = import_transfer.get_list_transfer_order_id()
        import_transfer.input_transfer_order_id_query(get_list_transfer_id1)
        import_transfer.click_search_reset('Search')
        sleep(1)
        """断言IMEI Detail详情页，加载的Transfer ID、Brand、Transfer From、IMEI字段内容是否与实际数据一致"""
        """获取调拨单列表字段内容"""
        get_list_transfer_id2 = import_transfer.get_list_transfer_order_id()
        ValueAssert.value_assert_equal(get_list_transfer_id1, get_list_transfer_id2)
        get_list_brand = import_transfer.get_list_field('Get list Brand')
        get_list_from_cust = import_transfer.get_list_field('Get list Transfer From Cust')
        get_list_total = import_transfer.get_transfer_order_list_total()
        ValueAssert.value_assert_equal('1', get_list_total)
        """打开IMEI Detail详情页"""
        import_transfer.click_transfer_imei_detail()
        get_detail_total = import_transfer.get_transfer_detail_total()
        ValueAssert.value_assert_equal('1', get_detail_total)
        get_detail_transfer = import_transfer.get_list_field('Get Detail Transfer ID')
        get_detail_brand = import_transfer.get_list_field('Get Detail Brand')
        get_detail_imei = import_transfer.get_list_field('Get Detail IMEI')
        get_detail_from_customer = import_transfer.get_list_field('Get Detail Customer Name')
        """IMEI Detail详情页，断言详情页列表字段内容是否正确"""
        ValueAssert.value_assert_equal(get_list_transfer_id2, get_detail_transfer)
        ValueAssert.value_assert_equal(get_list_brand, get_detail_brand)
        ValueAssert.value_assert_IsNoneNot(get_detail_imei)
        ValueAssert.value_assert_In(get_detail_from_customer, get_list_from_cust)
        """关闭IMEI Detail详情页"""
        import_transfer.close_transfer_imei_detail()

        """勾选第一个复选框后，点击Confirm Receipt 确认收货操作"""
        import_transfer.click_transfer_order_checkbox()
        import_transfer.click_transfer_return_goods('退货', 'Return Goods')
        DomAssert(drivers).assert_att('Successfully')
        """获取Transfer Order列表，Receipt Status状态是否更新为Rejected"""
        import_transfer.click_search_reset('Search')
        sleep(1)
        get_audited = import_transfer.get_list_transfer_order_status()
        get_receive = import_transfer.get_list_transfer_receipt_status()
        ValueAssert.value_assert_equal('Audited', get_audited)
        ValueAssert.value_assert_equal('Rejected', get_receive)

        """断言NG2061301账号IMEI Inventory Query是否能查询到退回的IMEI"""
        user.initialize_login(drivers, "NG2061301", "dcr123456")
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        assert_imei = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        assert_imei.imei_inventory_query_imei('354196616529945')
        get_imei = assert_imei.get_text_imei_inventory1()
        ValueAssert.value_assert_equal("354196616529945", get_imei)


@allure.feature("库存管理-调拨单")
class TestRecallTransferOrder:
    @allure.story("撤回调拨单")  # 场景名称
    @allure.title("已审核Received状态的调拨单不可撤回")  # 用例名称
    @allure.description("调拨单页面，已收货Received状态的调拨单，点击Recall撤回操作，不可撤回")
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD291501", "dcr123456")
        user.click_gotomenu("Inventory Management", "Transfer Order")
        recall = TransferOrderPage(drivers)
        """筛选Transfer Order页面，Received已经收货状态数据"""
        recall.click_unfold('Unfold')
        recall.input_transfer_create_start_date("2022-09-01")
        recall.click_transfer_receipt_status_query('Received')
        recall.click_search_reset('Search')
        sleep(1)
        recall.click_transfer_order_checkbox()
        """对已收货Received状态的数据，进行Recall撤回操作"""
        recall.click_more_option_recall()
        DomAssert(drivers).assert_att('Only No Receive or Audited can confirm receipt')


if __name__ == '__main__':
    pytest.main(['InventoryManagement_TransferOrder.py'])
