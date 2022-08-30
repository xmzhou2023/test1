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
            sleep(1)


@allure.feature("库存管理-门店IMEI调拨")
class TestNewIMEITransferStore:
    @allure.story("新建门店IMEI调店")
    @allure.title("库存管理页面，新建门店IMEI调店")
    @allure.description("库存管理页面，新建门店IMEI调店")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user1 = LoginPage(drivers)

        user1.initialize_login(drivers, "xiongbo92", "dcr123456")
        user1.click_gotomenu("Inventory Management", "Shop IMEI Transfer")

        shop_transfer = ShopIMEITransferPage(drivers)

        shop_transfer.click_add_imei_transfer()
        shop_transfer.input_shop_transfer('NG003965')
        shop_transfer.input_scan_imei('352802482806943')
        """点击Check检查按钮"""
        shop_transfer.click_check()
        """断言输入的IMEI是否验证通过"""
        get_scanned = shop_transfer.get_scanned_value()
        get_order_detail_scanned = shop_transfer.get_order_detail_scanned()
        get_imei = shop_transfer.get_scan_record_imei('352802482806943')
        get_success = shop_transfer.get_scan_record_success()
        ValueAssert.value_assert_equal(get_order_detail_scanned, get_scanned)
        ValueAssert.value_assert_equal('352802482806943', get_imei)
        ValueAssert.value_assert_In('Success', get_success)

        """点击提交按钮"""
        shop_transfer.click_add_submit_ok()
        #shop_transfer.search_shop_pending('NG003965', 'Pending')
        shop_transfer.click_unfold()
        shop_transfer.input_to_shop_query('NG003965')
        shop_transfer.input_status_query('Pending')
        shop_transfer.click_search()

        get_transfer_id = shop_transfer.get_list_transfer_id_text()
        get_status = shop_transfer.get_list_status_text('Pending')
        get_creator_id = shop_transfer.get_list_creator_id_text()
        get_to_shop = shop_transfer.get_list_to_shop_text('NG003965')

        ValueAssert.value_assert_IsNoneNot(get_transfer_id)
        ValueAssert.value_assert_equal('Pending', get_status)
        ValueAssert.value_assert_equal('NG003965', get_to_shop)
        ValueAssert.value_assert_equal('xiongbo92', get_creator_id)

        """拒绝调店操作"""
        shop_transfer.click_check_box()
        shop_transfer.click_approve_reject('Reject')
        shop_transfer.input_reject_reason('同意拒绝')
        DomAssert(drivers).assert_att('Approval successfully')
        sleep(2)
        shop_transfer.click_reset()
        get_status = shop_transfer.get_list_status_text('Rejected')
        ValueAssert.value_assert_equal('Rejected', get_status)



    # @allure.story("审核门店IMEI调店")
    # @allure.title("库存管理页面，审核门店IMEI调店")
    # @allure.description("库存管理页面，对新建的门店IMEI调店，进行审核操作")
    # @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    # @pytest.mark.usefixtures('function_menu_fixture')
    # def test_001_002(self, drivers):
    #     user2 = LoginPage(drivers)
    #
    #     user2.initialize_login(drivers, "xiongbo92", "dcr123456")
    #     user2.click_gotomenu("Inventory Management", "Shop IMEI Transfer")
    #
    #     approve = ShopIMEITransferPage(drivers)
    #
    #     approve.click_unfold()
    #     approve.input_to_shop_query('NG003965')
    #     approve.input_status_query('Pending')
    #     approve.click_search()



    # def test_001_002(self,drivers):
    #     user1 = LoginPage(drivers)
    #     user1.dcr_login(drivers, "xiongbo92", "dcr123456")
    #     user1.click_gotomenu("IMEIManagement", "ShopIMEITransfer")
    #
    #     user = ShopIMEITransferPage(drivers)
    #     user.search_pending()
    #     user.click_xvanze()
    #     user.click_approve_reject('Approve')
    #     user.click_YesORCancel('Cancel')
    #
    # def test_001_003(self,drivers):
    #     user1 = LoginPage(drivers)
    #     user1.dcr_login(drivers, "xiongbo92", "dcr123456")
    #     user1.click_gotomenu("IMEIManagement", "ShopIMEITransfer")
    #
    #     user = ShopIMEITransferPage(drivers)
    #     user.search_pending()   #筛选出未同意及未拒绝的调拨单
    #     user.click_xvanze()
    #     user.click_approve_reject('Reject')
    #     user.click_YesORCancel('Cancel')
    #     # user.click_YesORCancel('Yes')
    #     # user.click_RejectOK()
    #
    # def test_004_001(self, drivers):
    #     #登录dcr
    #     user1 = LoginPage(drivers)
    #     user1.dcr_login(drivers, "xiongbo92", "dcr123456")
    #     user1.click_gotomenu("IMEIManagement", "ShopIMEITransfer")
    #
    #     #新建店铺调拨单，把351517496367986从lwz_shop调入liufei_shop
    #     user = ShopIMEITransferPage(drivers)
    #     user.click_addIMEITransfer()
    #     user.input_ShopTransfer('EG000805 ','liufei_shop')
    #     user.input_ScanIMEI('351517496367986')
    #     user.click_check()
    #     user.click_addSubmit()
    #     user.click_addok()
    #     sleep(1)
    #     #同意lwz_shop到liufei_shop调拨单
    #     user.refresh()
    #     user.search_pending()
    #     user.click_xvanze()
    #     user.click_approve_reject('Approve')
    #     user.click_YesORCancel('Yes')
    #     user.click_ApproveOK()
    #
    #     #新建店铺调拨单，把351517496367986从liufei_shop调入lwz_shop
    #     user.refresh()
    #     sleep(1)
    #     user.click_addIMEITransfer()
    #     user.input_ShopTransfer('NG003965 ', 'lwz_shop')
    #     sleep(1)
    #     user.input_ScanIMEI('351517496367986')
    #     user.click_check()
    #     user.click_addSubmit()
    #     sleep(1)
    #     user.click_addok()
    #     sleep(2)
    #     #同意lwz_shop到liufei_shop调拨单
    #     user.refresh()
    #     sleep(2)
    #     user.search_pending()
    #     user.click_xvanze()
    #     user.click_approve_reject('Approve')
    #     user.click_YesORCancel('Yes')
    #     user.click_ApproveOK()
    #
    # def test_005_001(self, drivers):
    #     #登录dcr并进入ShopIMEI
    #     user1 = LoginPage(drivers)
    #     user1.dcr_login(drivers, "xiongbo92", "dcr123456")
    #     user1.click_gotomenu("IMEIManagement", "ShopIMEITransfer")
    #
    #     user = ShopIMEITransferPage(drivers)
    #     #新建到liufei_shop的调拨单
    #     user.click_addIMEITransfer()
    #     user.input_ShopTransfer('EG000805 ','liufei_shop')
    #     user.input_ScanIMEI('351517496668490')
    #     user.click_check()
    #     user.click_addSubmit()
    #     user.click_addok()
    #
    #     #拒绝调拨单
    #     user.search_pending()  # 筛选出未同意及未拒绝的调拨单
    #     user.click_xvanze()
    #     user.click_approve_reject('Reject')
    #     #user.click_YesORCancel('Cancel')
    #     user.click_YesORCancel('Yes')
    #     user.click_RejectOK()


if __name__ == '__main__':
    pytest.main(['InventoryManagement_ShopIMEITransfer.py'])

