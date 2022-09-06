from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.InventoryManagement_ShopIMEITransfer import ShopIMEITransferPage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
import pytest
import allure

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    for i in range(1):
        get_menu_class = menu.get_open_menu_class()
        class_value = "tags-view-item router-link-exact-active router-link-active active"
        if class_value == str(get_menu_class):
            menu.click_close_open_menu()

# @allure.feature("库存管理-门店IMEI调店")
# class TestNewRejectIMEITransfer:
#     @allure.story("新建、拒绝门店IMEI调店")
#     @allure.title("库存管理页面，新建、拒绝门店IMEI调店操作")
#     @allure.description("库存管理页面，新建、拒绝门店IMEI调店操作")
#     @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
#     @pytest.mark.usefixtures('function_menu_fixture')
#     def test_001_001(self, drivers):
#         user1 = LoginPage(drivers)
#         user1.initialize_login(drivers, "xiongbo92", "dcr123456")
#         user1.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
#
#         shop_transfer = ShopIMEITransferPage(drivers)
#         """新建门店调度单"""
#         shop_transfer.click_add_imei_transfer()
#         shop_transfer.input_shop_transfer('NG003965')
#         shop_transfer.input_scan_imei('350644371718900')
#         """点击Check检查按钮"""
#         shop_transfer.click_check()
#         """断言输入的IMEI是否验证通过"""
#         get_scanned = shop_transfer.get_scanned_value()
#         get_order_detail_scanned = shop_transfer.get_order_detail_scanned()
#         get_imei = shop_transfer.get_scan_record_imei('350644371718900')
#         get_success = shop_transfer.get_scan_record_success()
#         ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
#         ValueAssert.value_assert_equal('350644371718900', get_imei)
#         ValueAssert.value_assert_In('Success', get_success)
#         """点击提交按钮"""
#         shop_transfer.click_add_submit_ok()
#         """断言 筛选新建的调店单状态是否正确"""
#         shop_transfer.click_unfold()
#         shop_transfer.input_to_shop_query('NG003965')
#         shop_transfer.input_status_query('Pending')
#         shop_transfer.click_search()
#
#         get_transfer_id = shop_transfer.get_list_transfer_id_text()
#         get_status = shop_transfer.get_list_status_text('Pending')
#         get_creator_id = shop_transfer.get_list_creator_id_text()
#         get_to_shop = shop_transfer.get_list_to_shop_text('NG003965')
#
#         ValueAssert.value_assert_IsNoneNot(get_transfer_id)
#         ValueAssert.value_assert_equal('Pending', get_status)
#         ValueAssert.value_assert_equal('NG003965', get_to_shop)
#         ValueAssert.value_assert_equal('xiongbo92', get_creator_id)
#
#         """拒绝调店操作"""
#         shop_transfer.click_check_box()
#         shop_transfer.click_approve_reject('Reject')
#         shop_transfer.input_reject_reason('同意拒绝')
#         DomAssert(drivers).assert_att('Approval successfully')
#         sleep(2)
#         shop_transfer.click_reset()
#         get_status = shop_transfer.get_list_status_text('Rejected')
#         ValueAssert.value_assert_equal('Rejected', get_status)


@allure.feature("库存管理-门店IMEI调店")
class TestApproveIMEITransfer:
    @allure.story("审核门店IMEI调店")
    @allure.title("库存管理页面，审核门店IMEI调店")
    @allure.description("库存管理页面，审核门店IMEI调店")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "xiongbo92", "dcr123456")
        user1.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
        approve = ShopIMEITransferPage(drivers)

        """新建店铺调拨单，把imei: 352802482806943，从门店EG000394：CJP-TECNO1 调入门店NG003965：lwz_shop"""
        approve.click_add_imei_transfer()
        approve.input_shop_transfer('NG003965')
        approve.input_scan_imei('352802482806943')
        """点击Check检查按钮"""
        approve.click_check()
        """断言输入的IMEI是否验证通过"""
        get_scanned = approve.get_scanned_value()
        get_order_detail_scanned = approve.get_order_detail_scanned()
        get_imei = approve.get_scan_record_imei('352802482806943')
        get_success = approve.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('352802482806943', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        approve.click_add_submit_ok()

        """断言 筛选新建的调店单状态是否正确"""
        approve.click_unfold()
        approve.input_to_shop_query('NG003965')
        approve.input_status_query('Pending')
        approve.click_search()
        get_transfer_id = approve.get_list_transfer_id_text()
        get_status = approve.get_list_status_text('Pending')
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Pending', get_status)

        """审核调店操作"""
        approve.click_check_box()
        approve.click_approve_yes_ok('Approve', 'Yes')
        DomAssert(drivers).assert_att('Approval successfully')
        sleep(1)
        approve.click_reset()
        get_status = approve.get_list_status_text('Approved')
        ValueAssert.value_assert_equal('Approved', get_status)

        """新建店铺调拨单，把imei: 352802482806943，从门店NG003965：lwz_shop调回门店EG000394：CJP-TECNO1"""
        approve.click_add_imei_transfer()
        approve.input_shop_transfer('EG000394')
        approve.input_scan_imei('352802482806943')
        """点击Check检查按钮"""
        approve.click_check()
        """断言输入的IMEI是否验证通过"""
        get_scanned = approve.get_scanned_value()
        get_order_detail_scanned = approve.get_order_detail_scanned()
        get_imei = approve.get_scan_record_imei('352802482806943')
        get_success = approve.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('352802482806943', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        approve.click_add_submit_ok()

        """断言 筛选新建的调店单状态是否正确"""
        approve.input_to_shop_query('EG000394')
        approve.input_status_query('Pending')
        approve.click_search()
        get_transfer_id = approve.get_list_transfer_id_text()
        get_status = approve.get_list_status_text('Pending')
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Pending', get_status)

        """审核调店操作"""
        approve.click_check_box()
        approve.click_approve_yes_ok('Approve', 'Yes')
        DomAssert(drivers).assert_att('Approval successfully')
        sleep(1)
        approve.click_reset()
        get_transfer_id = approve.get_list_transfer_id_text()
        get_status = approve.get_list_status_text('Approved')
        get_to_shop = approve.get_list_to_shop_text('EG000394')
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Approved', get_status)
        ValueAssert.value_assert_equal('NG003965', get_to_shop)

        """新建店铺调拨单，把imei: 352802482806943，从门店EG000394：CJP-TECNO1 调入门店NG003965：lwz_shop"""
        approve.click_add_imei_transfer()
        approve.input_shop_transfer('NG003965')
        approve.input_scan_imei('352802482806943')
        """点击Check检查按钮"""
        approve.click_check()
        """断言输入的IMEI是否验证通过"""
        get_scanned = approve.get_scanned_value()
        get_order_detail_scanned = approve.get_order_detail_scanned()
        get_imei = approve.get_scan_record_imei('352802482806943')
        get_success = approve.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('352802482806943', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        approve.click_add_submit_ok()

        """断言 筛选新建的调店单状态是否正确"""
        approve.click_unfold()
        approve.input_to_shop_query('NG003965')
        approve.input_status_query('Pending')
        approve.click_search()
        get_transfer_id = approve.get_list_transfer_id_text()
        get_status = approve.get_list_status_text('Pending')
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Pending', get_status)

        """审核调店操作"""
        approve.click_check_box()
        approve.click_approve_yes_ok('Approve', 'Yes')
        DomAssert(drivers).assert_att('Approval successfully')
        sleep(1)
        approve.click_reset()
        get_status = approve.get_list_status_text('Approved')
        ValueAssert.value_assert_equal('Approved', get_status)

        """新建店铺调拨单，把imei: 352802482806943，从门店NG003965：lwz_shop调回门店EG000394：CJP-TECNO1"""
        approve.click_add_imei_transfer()
        approve.input_shop_transfer('EG000394')
        approve.input_scan_imei('352802482806943')
        """点击Check检查按钮"""
        approve.click_check()
        """断言输入的IMEI是否验证通过"""
        get_scanned = approve.get_scanned_value()
        get_order_detail_scanned = approve.get_order_detail_scanned()
        get_imei = approve.get_scan_record_imei('352802482806943')
        get_success = approve.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('352802482806943', get_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        approve.click_add_submit_ok()

        """断言 筛选新建的调店单状态是否正确"""
        approve.input_to_shop_query('EG000394')
        approve.input_status_query('Pending')
        approve.click_search()
        get_transfer_id = approve.get_list_transfer_id_text()
        get_status = approve.get_list_status_text('Pending')
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Pending', get_status)

        """审核调店操作"""
        approve.click_check_box()
        approve.click_approve_yes_ok('Approve', 'Yes')
        DomAssert(drivers).assert_att('Approval successfully')
        sleep(1)
        approve.click_reset()
        get_transfer_id = approve.get_list_transfer_id_text()
        get_status = approve.get_list_status_text('Approved')
        get_to_shop = approve.get_list_to_shop_text('EG000394')
        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Approved', get_status)
        ValueAssert.value_assert_equal('EG000394', get_to_shop)


# @allure.feature("库存管理-门店IMEI调店")
# class TestQueryIMEITransfer:
#     @allure.story("查询门店IMEI调店数据")
#     @allure.title("库存管理页面，按状态查询门店IMEI调店")
#     @allure.description("库存管理页面，按状态查询门店IMEI调店")
#     @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
#     @pytest.mark.usefixtures('function_menu_fixture')
#     def test_003_001(self, drivers):
#         user2 = LoginPage(drivers)
#         user2.initialize_login(drivers, "xiongbo92", "dcr123456")
#         user2.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
#
#         query = ShopIMEITransferPage(drivers)
#         get_transfer_id = query.get_list_transfer_id_text()
#         get_creator = query.get_list_creator_id_text()
#
#         ValueAssert.value_assert_IsNoneNot(get_transfer_id)
#         ValueAssert.value_assert_IsNoneNot(get_creator)
#         get_total = query.get_total_text()
#         query.assert_total(get_total)
#
#         """按状态筛选门店IMEI调店记录"""
#         query.click_unfold()
#         query.input_create_date_query('2022-08-01')
#         query.click_create_end_date()
#         query.input_status_query('Approved')
#         query.click_search()
#
#         get_transfer_id = query.get_list_transfer_id_text()
#         get_status = query.get_list_status_text('Approved')
#         get_creator = query.get_list_creator_id_text()
#         get_shop = query.get_list_to_shop_text('EG000394')
#
#         ValueAssert.value_assert_IsNoneNot(get_transfer_id)
#         ValueAssert.value_assert_IsNoneNot(get_status)
#         ValueAssert.value_assert_IsNoneNot(get_creator)
#         ValueAssert.value_assert_equal('EG000394', get_shop)
#         get_total = query.get_total_text()
#         query.assert_total(get_total)


# @allure.feature("库存管理-门店IMEI调店")
# class TestApproveRejectTransfer:
#     @allure.story("将完成状态的记录，进行Approved门店IMEI调店操作")
#     @allure.title("门店IMEI调店页面，将Approved状态的数据，进行Reject拒绝操作")
#     @allure.description("库存管理页面，门店IMEI调店页面，将Approved状态的数据，进行Reject拒绝操作")
#     @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
#     @pytest.mark.usefixtures('function_menu_fixture')
#     def test_004_001(self, drivers):
#         user2 = LoginPage(drivers)
#         user2.initialize_login(drivers, "xiongbo92", "dcr123456")
#         user2.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
#
#         approve = ShopIMEITransferPage(drivers)
#         """按状态筛选门店IMEI调店记录"""
#         approve.click_unfold()
#         approve.input_status_query('Approved')
#         approve.click_search()
#
#         approve.click_first_checkbox()
#         approve.click_approve_reject('Approve')
#         DomAssert(drivers).assert_att('The data you selected include completed, please reselect')
#         sleep(1)
#         approve.click_approve_reject('Reject')
#         DomAssert(drivers).assert_att('The data you selected include completed, please reselect')
#         sleep(1)
#
#
#     @allure.story("将完成状态的记录，进行Reject门店IMEI调店操作")
#     @allure.title("门店IMEI调店页面，将Reject状态的数据，进行Approved拒绝操作")
#     @allure.description("库存管理页面，门店IMEI调店页面，将Reject状态的数据，进行Reject拒绝操作")
#     @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
#     @pytest.mark.usefixtures('function_menu_fixture')
#     def test_004_002(self, drivers):
#         user2 = LoginPage(drivers)
#         user2.initialize_login(drivers, "xiongbo92", "dcr123456")
#         user2.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
#
#         approve = ShopIMEITransferPage(drivers)
#         approve.click_unfold()
#         approve.input_status_query('Rejected')
#         approve.click_search()
#
#         approve.click_first_checkbox()
#         approve.click_approve_reject('Approve')
#         DomAssert(drivers).assert_att('The data you selected include completed, please reselect')
#         sleep(1)
#         approve.click_approve_reject('Reject')
#         DomAssert(drivers).assert_att('The data you selected include completed, please reselect')

if __name__ == '__main__':
    pytest.main(['InventoryManagement_ShopIMEITransfer.py'])

