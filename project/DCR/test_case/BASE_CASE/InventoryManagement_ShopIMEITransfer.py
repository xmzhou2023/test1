from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.InventoryManagement_ShopIMEITransfer import ShopIMEITransferPage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
from libs.common.time_ui import sleep
import datetime
import pytest
import allure

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("库存管理-门店IMEI调店")
class TestQueryIMEITransfer:
    @allure.story("查询门店IMEI调店")
    @allure.title("库存管理页面，按状态查询门店IMEI调店")
    @allure.description("库存管理页面，按状态查询门店IMEI调店")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user2 = LoginPage(drivers)
        user2.initialize_login(drivers, "xiongbo92", "dcr123456")
        user2.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
        query = ShopIMEITransferPage(drivers)
        """按创建日期与状态筛选门店IMEI调店记录"""
        query.click_unfold()
        query.shop_imei_transfer_create_date_query('2022-12-08', '2022-12-08')
        query.click_create_end_date()
        query.input_status_query('Approved')
        query.click_search()
        get_transfer_id = query.get_list_field_text('Get Shop IMEI Transfer To Shop ID')
        get_status = query.get_list_field_text('Get Shop IMEI Transfer Status')
        get_create_date = query.get_list_field_text('Get Shop IMEI Transfer CreateDate')
        """断言列表字段内容是否与筛选的字段值匹配正确"""
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_In('2022-12-08', get_create_date)
        ValueAssert.value_assert_equal('Approved', get_status)
        get_total = query.get_list_total_text()
        query.assert_total(get_total)


    @allure.story("查询门店IMEI调店")
    @allure.title("库存管理页面，按单个条件查询门店IMEI调店")
    @allure.description("库存管理页面，按单个条件查询门店IMEI调店")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user2 = LoginPage(drivers)
        user2.initialize_login(drivers, "xiongbo92", "dcr123456")
        user2.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
        query = ShopIMEITransferPage(drivers)
        """获取列表Transfer ID字段内容"""
        query.click_unfold()
        """按Transfer ID条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_query('Shop IMEI Transfer ID query', 'Shop IMEI Transfer Input ID query', 'IT202212080353230011')
        query.click_search()
        query.assert_shop_imei_transfer_field('Transfer ID', 'IT202212080353230011')
        get_total = query.get_list_total_text()
        ValueAssert.value_assert_equal('1', get_total)
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()

        """按Country条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_select_query('Shop IMEI Transfer Country query', 'Shop IMEI Transfer Country click query', 'Shop IMEI Transfer Country select query', 'Egypt', 'Egypt')
        query.click_search()
        query.assert_shop_imei_transfer_field('From Country', 'Egypt')
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()

        """按Sales Region 条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_select_query('Shop IMEI Transfer SalesRegion query', 'Shop IMEI Transfer SalesRegion query', 'Shop IMEI Transfer SalesRegion select query', 'Cairo', 'Cairo')
        query.click_search()
        query.assert_shop_imei_transfer_field('Transfer From Sales Region3', 'Cairo')
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()

        """按From Shop条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_select_query('Shop IMEI Transfer FromShop query',  'Shop IMEI Transfer FromShop click query', 'Shop IMEI Transfer FromShop select query', 'EG000706', 'EG000706')
        query.click_search()
        query.assert_shop_imei_transfer_field('From Shop ID', 'EG000706')
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()

        """按To Shop 条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_select_query('Shop IMEI Transfer ToShop query',  'Shop IMEI Transfer ToShop click query', 'Shop IMEI Transfer ToShop select query', 'lhmShop018', 'lhmShop018')
        query.click_search()
        query.assert_shop_imei_transfer_field('To Shop', 'lhmShop018')
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()

        """按 Brand 条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_select_query('Shop IMEI Transfer Brand query',  'Shop IMEI Transfer Brand click query', 'Shop IMEI Transfer Brand select query', 'TECNO', 'TECNO')
        query.click_search()
        query.assert_shop_imei_transfer_field('Brand', 'TECNO')
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()

        """按Creator条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_select_query('Shop IMEI Transfer Creator query', 'Shop IMEI Transfer Creator click query', 'Shop IMEI Transfer Creator select query', 'lhmadmin', 'lhmadmin lhmadmin')
        query.click_search()
        query.assert_shop_imei_transfer_field('Creator ID', 'lhmadmin')
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()

        """按 Market Name条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_select_query('Shop IMEI Transfer MarketName query', 'Shop IMEI Transfer MarketName click query', 'Shop IMEI Transfer MarketName select query', 'SPARK 6 Go', 'SPARK 6 Go')
        query.click_search()
        query.assert_shop_imei_transfer_field('Market Name', 'SPARK 6 Go')
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()

        """按IMEI条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_query('Shop IMEI Transfer IMEI query', 'Shop IMEI Transfer Input IMEI query', '356560541846104')
        query.click_search()
        query.assert_shop_imei_transfer_field('IMEI', '356560541846104')
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()

        """按Status 条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_select_query('Shop IMEI Transfer Status query', 'Shop IMEI Transfer Status click query', 'Shop IMEI Transfer Status select query', 'Approved', 'Approved')
        query.click_search()
        get_list_status = query.get_list_field_text('Get Shop IMEI Transfer Status')
        ValueAssert.value_assert_equal('Approved', get_list_status)
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()

        """按 Model 条件，筛选门店IMEI调店记录"""
        query.shop_imei_transfer_input_select_query('Shop IMEI Transfer Model query', 'Shop IMEI Transfer Model click query', 'Shop IMEI Transfer Model select query', 'KE5k', 'KE5k')
        query.click_search()
        query.assert_shop_imei_transfer_field('Model', 'KE5k')
        """重置筛选条件"""
        query.click_shop_imei_transfer_reset()


@allure.feature("库存管理-门店IMEI调店")
class TestNewRejectIMEITransfer:
    @allure.story("新建门店IMEI调拨单")
    @allure.title("库存管理页面，新建门店IMEI调拨单，然后审核拒绝门店IMEI调店操作")
    @allure.description("库存管理页面，新建门店IMEI调店、拒绝门店IMEI调店操作,Shop:EG000397,EG000388")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "xiongbo92", "dcr123456")
        user1.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
        shop_transfer = ShopIMEITransferPage(drivers)
        """新建门店调度单操作"""
        shop_transfer.add_shop_transfer_order('EG000388', '352427572805181')
        """断言输入的IMEI是否验证通过"""
        get_scanned = shop_transfer.get_scanned_value()
        get_order_detail_scanned = shop_transfer.get_order_detail_scanned()
        get_imei = shop_transfer.get_scan_record_imei('352427572805181')
        get_success = shop_transfer.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('352427572805181', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        shop_transfer.click_add_submit_ok()
        """ 筛选新建的调店单记录"""
        shop_transfer.query_add_shop_imei_transfer('EG000388', 'Pending')
        """断言 筛选新建的调店单状态是否正确"""
        get_transfer_id = shop_transfer.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        shop_transfer.assert_shop_imei_transfer_field('Status', 'Pending')
        shop_transfer.assert_shop_imei_transfer_field('Creator ID', 'xiongbo92')
        shop_transfer.assert_shop_imei_transfer_field('To Shop ID', 'EG000388')

        """拒绝调店操作"""
        shop_transfer.click_all_check_box()
        shop_transfer.click_operation_approve_reject('Reject')
        shop_transfer.input_reject_reason('同意拒绝', 'Yes')
        DomAssert(drivers).assert_att('Approval successfully')
        sleep(1)
        """根据当前门店与Rejected状态筛选，对比列表状态是否更新为Rejected"""
        shop_transfer.click_unfold()
        shop_transfer.input_status_query('Rejected')
        shop_transfer.click_search()
        get_status = shop_transfer.get_list_transfer_status_text()
        ValueAssert.value_assert_equal('Rejected', get_status)


        @allure.story("新建门店IMEI调拨单单")
        @allure.title("库存管理页面，新建门店IMEI调拨单，一次拒绝多条调拨单")
        @allure.description("库存管理页面，新建门店IMEI调拨单、一次拒绝多条调拨单,Shop:EG000397,EG000388")
        @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
        @pytest.mark.UI  # 用例标记
        @pytest.mark.usefixtures('function_menu_fixture')
        def test_002_002(self, drivers):
            user1 = LoginPage(drivers)
            user1.initialize_login(drivers, "xiongbo92", "dcr123456")
            user1.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
            add_shop_transfer = ShopIMEITransferPage(drivers)
            """新建第一条门店调度单操作"""
            add_shop_transfer.add_shop_transfer_order('EG000388', '352427572805603')
            """断言输入的IMEI是否验证通过"""
            get_scanned = add_shop_transfer.get_scanned_value()
            get_order_detail_scanned = add_shop_transfer.get_order_detail_scanned()
            get_imei = add_shop_transfer.get_scan_record_imei('352427572805603')
            get_success = add_shop_transfer.get_scan_record_success()
            ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
            ValueAssert.value_assert_equal('352427572805603', get_imei)
            ValueAssert.value_assert_In('Success', get_success)
            """点击提交按钮"""
            add_shop_transfer.click_add_submit_ok()
            """筛选新建的调店单记录"""
            add_shop_transfer.query_add_shop_imei_transfer('EG000388', 'Pending')
            get_transfer_id = add_shop_transfer.get_list_transfer_id()
            ValueAssert.value_assert_IsNoneNot(get_transfer_id)
            """断言新建的调店单状态、to shop和 创建人字段内容是否正确"""
            add_shop_transfer.assert_shop_imei_transfer_field('Status', 'Pending')
            add_shop_transfer.assert_shop_imei_transfer_field('Creator ID', 'xiongbo92')
            add_shop_transfer.assert_shop_imei_transfer_field('To Shop ID', 'EG000388')
            """点击重置按钮"""
            add_shop_transfer.click_shop_imei_transfer_reset()

            """新建第二条门店调度单操作"""
            add_shop_transfer.add_shop_transfer_order('EG000388', '352427572805421')
            """断言输入的IMEI是否验证通过"""
            get_scanned = add_shop_transfer.get_scanned_value()
            get_order_detail_scanned = add_shop_transfer.get_order_detail_scanned()
            get_imei = add_shop_transfer.get_scan_record_imei('352427572805421')
            get_success = add_shop_transfer.get_scan_record_success()
            ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
            ValueAssert.value_assert_equal('352427572805421', get_imei)
            ValueAssert.value_assert_In('Success', get_success)
            """点击提交按钮"""
            add_shop_transfer.click_add_submit_ok()
            """筛选新建的调店单记录"""
            add_shop_transfer.query_add_shop_imei_transfer('EG000388', 'Pending')
            """断言 筛选新建的调店单状态是否正确"""
            add_shop_transfer.assert_shop_imei_transfer_field('Status', 'Pending')
            add_shop_transfer.assert_shop_imei_transfer_field('Creator ID', 'xiongbo92')
            add_shop_transfer.assert_shop_imei_transfer_field('To Shop ID', 'EG000388')
            """点击重置按钮"""
            add_shop_transfer.click_shop_imei_transfer_reset()

            """筛选Pending状态的调拨单，然后勾选第一二条记录，一次拒绝多条调拨单操作"""
            """筛选新建的调店单记录"""
            add_shop_transfer.query_add_shop_imei_transfer('EG000388', 'Pending')
            """点击勾选两条待拒绝的复选框"""
            add_shop_transfer.click_all_check_box()
            add_shop_transfer.click_approve_reject('Reject')
            add_shop_transfer.input_reject_reason('同意拒绝', 'Yes')
            DomAssert(drivers).assert_att('Approval successfully')
            sleep(1)
            """根据当前门店与Rejected状态筛选，对比列表状态是否更新为Rejected"""
            add_shop_transfer.query_shop_imei_transfer_status('Rejected')
            add_shop_transfer.assert_shop_imei_transfer_field('Status', 'Rejected')


    @allure.story("新建门店IMEI调拨单")
    @allure.title("库存管理页面，新建门店IMEI调拨单(出库IMEI)，并审核门店调拨单")
    @allure.description("库存管理页面，新建门店IMEI调拨单(出库IMEI)，并审核门店调拨单")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_003(self, drivers):
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "xiongbo92", "dcr123456")
        user1.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
        approve = ShopIMEITransferPage(drivers)
        """新建店铺调拨单，把imei: 352427572880721，从门店：EG000397 调入门店EG000388"""
        approve.add_shop_transfer_order('EG000388', '352427572880721')
        """断言输入的IMEI是否验证通过"""
        get_scanned = approve.get_scanned_value()
        get_order_detail_scanned = approve.get_order_detail_scanned()
        get_imei = approve.get_scan_record_imei('352427572880721')
        get_success = approve.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('352427572880721', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        approve.click_add_submit_ok()
        """筛选新建的调店单记录"""
        approve.query_add_shop_imei_transfer('EG000388', 'Pending')
        """断言 筛选新建的调店单状态是否正确"""
        get_transfer_id = approve.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        approve.assert_shop_imei_transfer_field('Status', 'Pending')

        """审核调店操作"""
        approve.click_first_checkbox()
        approve.click_operation_approve_yes_ok('Approve', 'Yes')
        DomAssert(drivers).assert_att('Approval successfully')
        sleep(1)
        """根据当前筛选的门店及 Approved状态，筛选查询的记录是否更新状态为Approved"""
        approve.query_shop_imei_transfer_status('Approved')
        approve.assert_shop_imei_transfer_field('Status', 'Approved')

        """新建店铺调拨单，把imei: 352427572880721，从门店EG000388 调回门店EG000397"""
        approve.add_shop_transfer_order('EG000397', '352427572880721')
        """断言输入的IMEI是否验证通过"""
        get_scanned = approve.get_scanned_value()
        get_order_detail_scanned = approve.get_order_detail_scanned()
        get_imei = approve.get_scan_record_imei('352427572880721')
        get_success = approve.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('352427572880721', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        approve.click_add_submit_ok()
        """筛选新建的调店单记录"""
        approve.query_add_shop_imei_transfer('EG000397', 'Pending')
        """断言 筛选新建的调店单状态是否正确"""
        get_transfer_id = approve.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        approve.assert_shop_imei_transfer_field('Status', 'Pending')

        """审核调店操作"""
        approve.click_all_check_box()
        approve.click_operation_approve_yes_ok('Approve', 'Yes')
        DomAssert(drivers).assert_att('Approval successfully')
        sleep(1)
        """根据当前筛选的门店及 Approved状态，筛选查询的记录是否更新状态为Approved"""
        approve.query_add_shop_imei_transfer('EG000397', 'Approved')
        get_transfer_id = approve.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        approve.assert_shop_imei_transfer_field('Status', 'Approved')
        approve.assert_shop_imei_transfer_field('To Shop ID', 'EG000397')


    @allure.story("新建门店IMEI调拨单")
    @allure.title("库存管理页面，创建门店调拨单(出库IMEI)，一次审核同意多条门店调拨单")
    @allure.description("库存管理页面，创建门店调拨单(出库IMEI)，一次审核同意多条门店调拨单")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor 352427572805108
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_004(self, drivers):
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "xiongbo92", "dcr123456")
        user1.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
        approve = ShopIMEITransferPage(drivers)
        """新建第一条门店调拨单，把imei: 352427572805348，从门店：EG000397 调入门店 EG000388"""
        approve.add_shop_transfer_order('EG000388', '352427572805348')
        """断言输入的IMEI是否验证通过"""
        get_scanned = approve.get_scanned_value()
        get_order_detail_scanned = approve.get_order_detail_scanned()
        get_imei = approve.get_scan_record_imei('352427572805348')
        get_success = approve.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('352427572805348', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        approve.click_add_submit_ok()
        """筛选新建的调店单记录"""
        approve.query_add_shop_imei_transfer('EG000388', 'Pending')
        """断言 筛选新建的调店单状态是否正确"""
        get_transfer_id = approve.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        """断言新建的调店单状态、to shop和 创建人字段内容是否正确"""
        approve.assert_shop_imei_transfer_field('Status', 'Pending')
        approve.assert_shop_imei_transfer_field('Creator ID', 'xiongbo92')
        approve.assert_shop_imei_transfer_field('To Shop ID', 'EG000388')
        """点击重置按钮"""
        approve.click_shop_imei_transfer_reset()

        """新建第二条门店调拨单操作"""
        approve.add_shop_transfer_order('EG000388', '352427572805108')
        """断言输入的IMEI是否验证通过"""
        get_scanned = approve.get_scanned_value()
        get_order_detail_scanned = approve.get_order_detail_scanned()
        get_imei = approve.get_scan_record_imei('352427572805108')
        get_success = approve.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('352427572805108', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        approve.click_add_submit_ok()
        """筛选新建的调店单记录"""
        approve.query_add_shop_imei_transfer('EG000388', 'Pending')
        """断言 筛选新建的调店单状态是否正确"""
        approve.assert_shop_imei_transfer_field('Status', 'Pending')
        approve.assert_shop_imei_transfer_field('Creator ID', 'xiongbo92')
        approve.assert_shop_imei_transfer_field('To Shop ID', 'EG000388')
        get_total = approve.get_list_total()
        ValueAssert.value_assert_equal('2', get_total)

        """筛选Pending状态的调拨单，然后勾选第一二条记录，一次审核多条调拨单操作"""
        approve.click_all_check_box()
        approve.click_approve_yes_ok_button('Approve', 'Yes')
        DomAssert(drivers).assert_att('Approval successfully')
        sleep(1)
        """根据当前门店与Rejected状态筛选，对比列表状态是否更新为Rejected"""
        approve.query_add_shop_imei_transfer('EG000388', 'Approved')
        approve.assert_shop_imei_transfer_field('Status', 'Approved')
        approve.assert_shop_imei_transfer_field('To Shop ID', 'EG000388')

        """新建店铺调拨单，把imei: 352427572805108、352427572805348，从门店EG000388 调回门店EG000397"""
        approve.add_shop_transfer_order('EG000397', '352427572805108')
        """断言输入的IMEI是否验证通过"""
        get_success = approve.get_scan_record_success()
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        approve.click_add_submit_ok()
        approve.add_shop_transfer_order('EG000397', '352427572805348')
        """断言输入的IMEI是否验证通过"""
        get_success = approve.get_scan_record_success()
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        approve.click_add_submit_ok()
        """筛选新建的调店单记录"""
        approve.query_add_shop_imei_transfer('EG000397', 'Pending')
        """断言 筛选新建的调店单状态是否正确"""
        get_transfer_id = approve.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        approve.assert_shop_imei_transfer_field('Status', 'Pending')
        approve.assert_shop_imei_transfer_field('To Shop ID', 'EG000397')
        get_total = approve.get_list_total()
        ValueAssert.value_assert_equal('2', get_total)

        """审核调店操作"""
        approve.click_all_check_box()
        approve.click_approve_yes_ok_button('Approve', 'Yes')
        DomAssert(drivers).assert_att('Approval successfully')
        sleep(1)
        """根据当前筛选的门店及 Approved状态，筛选查询的记录是否更新状态为Approved"""
        approve.query_add_shop_imei_transfer('EG000397', 'Approved')
        get_transfer_id = approve.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        approve.assert_shop_imei_transfer_field('Status', 'Approved')
        approve.assert_shop_imei_transfer_field('To Shop ID', 'EG000397')



    @allure.story("新建门店IMEI调拨单")
    @allure.title("库存管理页面，新建门店IMEI调店，配置无需审核，新建成功后自动审核通过")
    @allure.description("库存管理页面，新建门店IMEI调店，配置无需审核，新建成功后自动审核通过")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_005(self, drivers):
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "lhmadmin", "dcr123456")
        user1.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
        add_shop_transfer = ShopIMEITransferPage(drivers)
        """新建门店调拨单"""
        add_shop_transfer.add_shop_transfer_order('EG000706', '356560541846104')
        """断言输入的IMEI是否验证通过"""
        get_scanned = add_shop_transfer.get_scanned_value()
        get_order_detail_scanned = add_shop_transfer.get_order_detail_scanned()
        get_imei = add_shop_transfer.get_scan_record_imei('356560541846104')
        get_success = add_shop_transfer.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('356560541846104', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        add_shop_transfer.click_add_submit_ok()
        """筛选新建的调店单记录"""
        add_shop_transfer.query_add_shop_imei_transfer('EG000706', 'Approved')
        """获取门店调店列表，creatorid、Status与to shop字段是否正确"""
        get_transfer_id1 = add_shop_transfer.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id1)
        add_shop_transfer.assert_shop_imei_transfer_field('Status', 'Approved')
        add_shop_transfer.assert_shop_imei_transfer_field('Creator ID', 'lhmadmin')
        add_shop_transfer.assert_shop_imei_transfer_field('To Shop ID', 'EG000706')

        """新建店铺调拨单，把imei从门店EG000706 调回门店SN001872"""
        add_shop_transfer.add_shop_transfer_order('SN001872', '356560541846104')
        """断言输入的IMEI是否验证通过"""
        get_scanned = add_shop_transfer.get_scanned_value()
        get_order_detail_scanned = add_shop_transfer.get_order_detail_scanned()
        get_imei = add_shop_transfer.get_scan_record_imei('356560541846104')
        get_success = add_shop_transfer.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('356560541846104', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        add_shop_transfer.click_add_submit_ok()
        """断言 筛选新建的调店单状态是否正确"""
        add_shop_transfer.query_add_shop_imei_transfer('SN001872', 'Approved')
        get_transfer_id2 = add_shop_transfer.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id2)
        add_shop_transfer.assert_shop_imei_transfer_field('Status', 'Approved')
        add_shop_transfer.assert_shop_imei_transfer_field('To Shop ID', 'SN001872')


    @allure.story("新建门店IMEI调拨单")
    @allure.title("库存管理页面，新建门店IMEI调店(出库SN)，并审核门店IMEI调店")
    @allure.description("库存管理页面，新建门店IMEI调店(出库SN)，审核门店IMEI调店")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_006(self, drivers):
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "xiongbo92", "dcr123456")
        user1.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
        shop_transfer_sn = ShopIMEITransferPage(drivers)
        """新建店铺调拨单，把imei: IHA50U911700181，从门店：EG000809 调至门店 EG000811 """
        shop_transfer_sn.add_shop_transfer_order('EG000811', 'IHA50U911700181')
        """断言输入的IMEI是否验证通过"""
        get_scanned = shop_transfer_sn.get_scanned_value()
        get_order_detail_scanned = shop_transfer_sn.get_order_detail_scanned()
        get_imei = shop_transfer_sn.get_scan_record_imei('IHA50U911700181')
        get_success = shop_transfer_sn.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('IHA50U911700181', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        shop_transfer_sn.click_add_submit_ok()
        """筛选新建的调店单记录"""
        shop_transfer_sn.query_add_shop_imei_transfer('EG000811', 'Approved')
        """断言门店调店列表，creatorid、Status与to shop字段是否正确"""
        get_transfer_id1 = shop_transfer_sn.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id1)
        shop_transfer_sn.assert_shop_imei_transfer_field('Status', 'Approved')
        shop_transfer_sn.assert_shop_imei_transfer_field('Creator ID', 'xiongbo92')
        shop_transfer_sn.assert_shop_imei_transfer_field('To Shop ID', 'EG000811')

        """新建店铺调拨单，把imei从门店EG000811 调回门店EG000809"""
        shop_transfer_sn.add_shop_transfer_order('EG000809', 'IHA50U911700181')
        """断言输入的IMEI是否验证通过"""
        get_scanned = shop_transfer_sn.get_scanned_value()
        get_order_detail_scanned = shop_transfer_sn.get_order_detail_scanned()
        get_imei = shop_transfer_sn.get_scan_record_imei('IHA50U911700181')
        get_success = shop_transfer_sn.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('IHA50U911700181', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        shop_transfer_sn.click_add_submit_ok()
        """ 筛选新建的调拨单记录"""
        shop_transfer_sn.query_add_shop_imei_transfer('EG000809', 'Approved')
        """断言门店调店列表，Status与to shop字段是否正确"""
        get_transfer_id2 = shop_transfer_sn.get_list_transfer_id()
        ValueAssert.value_assert_IsNoneNot(get_transfer_id2)
        shop_transfer_sn.assert_shop_imei_transfer_field('Status', 'Approved')
        shop_transfer_sn.assert_shop_imei_transfer_field('To Shop ID', 'EG000809')


@allure.feature("库存管理-门店IMEI调店")
class TestApproveRejectTransfer:
    @allure.story("拒绝门店IMEI调拨单")
    @allure.title("门店IMEI调店页面，将Approved状态的数据，进行Reject拒绝操作")
    @allure.description("库存管理页面，门店IMEI调店页面，将Approved状态的数据，进行Reject拒绝操作")
    @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.RT  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_001(self, drivers):
        user2 = LoginPage(drivers)
        user2.initialize_login(drivers, "xiongbo92", "dcr123456")
        user2.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
        approve = ShopIMEITransferPage(drivers)
        """按状态筛选门店IMEI调店记录"""
        approve.click_unfold()
        approve.input_status_query('Approved')
        approve.click_search()
        """勾选复选框"""
        approve.click_all_check_box()
        approve.click_approve_reject('Approve')
        DomAssert(drivers).assert_att('The data you selected include completed, please reselect')
        sleep(1)
        approve.click_approve_reject('Reject')
        DomAssert(drivers).assert_att('The data you selected include completed, please reselect')


    @allure.story("拒绝门店IMEI调拨单")
    @allure.title("门店IMEI调店页面，将Reject状态的数据，进行Approved拒绝操作")
    @allure.description("库存管理页面，门店IMEI调店页面，将Reject状态的数据，进行Reject拒绝操作")
    @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.RT  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_002(self, drivers):
        user2 = LoginPage(drivers)
        user2.initialize_login(drivers, "xiongbo92", "dcr123456")
        user2.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
        approve = ShopIMEITransferPage(drivers)
        approve.click_unfold()
        approve.input_status_query('Rejected')
        approve.click_search()
        """勾选复选框"""
        approve.click_all_check_box()
        approve.click_approve_reject('Approve')
        DomAssert(drivers).assert_att('The data you selected include completed, please reselect')
        sleep(1)
        approve.click_approve_reject('Reject')
        DomAssert(drivers).assert_att('The data you selected include completed, please reselect')


if __name__ == '__main__':
    pytest.main(['InventoryManagement_ShopIMEITransfer.py'])

