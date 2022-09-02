from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.InventoryManagement_TransferOrder import TransferOrderPage
from libs.common.connect_sql import SQL
from public.base.assert_ui import ValueAssert, DomAssert
import logging
import allure
import pytest

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""
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
        user.click_gotomenu("Inventory Management", "Transfer Order")

        transfer = TransferOrderPage(drivers)
        transfer.click_create()
        transfer.click_transfer_from_customer()
        transfer.click_transfer_to_customer()
        transfer.input_scan_imei('356560549278086')
        """点击Check 按钮，校验IMEI是否存在此仓库"""
        transfer.click_check()
        """断言输入的IMEI是否验证通过"""
        get_scanned = transfer.get_scanned()
        get_deli_quantity = transfer.get_delivery_quantity()
        get_scan_record_imei = transfer.get_scan_record_imei('356560549278086')
        get_scan_record_success = transfer.get_scan_record_success()
        ValueAssert.value_assert_equal(get_scanned, get_deli_quantity)
        ValueAssert.value_assert_equal('356560549278086', get_scan_record_imei)
        ValueAssert.value_assert_In('Success', get_scan_record_success)
        """点击提交按钮"""
        transfer.click_submit()
        DomAssert(drivers).assert_att('Successfully')
        transfer.click_submit_ok()

        get_transfer_id = transfer.get_transfer_id()
        logging.info("打印获取Transfer Order列表的Transfer ID字段内容{}".format(get_transfer_id))
        get_audited = transfer.get_order_status_text()
        get_receive = transfer.get_receipt_status_text()
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

        get_order_status = transfer.get_list_order_status('Recall')
        get_receipt_status = transfer.get_list_receipt_status('No Receive')
        ValueAssert.value_assert_equal('Recall', get_order_status)
        ValueAssert.value_assert_equal('No Receive', get_receipt_status)


@allure.feature("库存管理-调拨单")
class TestRecallTransferOrder:
    @allure.story("撤回调拨单")  # 场景名称
    @allure.title("撤回Received状态的调拨单")  # 用例名称
    @allure.description("调拨单页面，已收货Received状态的调拨单，Recall撤回操作，不支持撤回")
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
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



# @allure.feature("脚本名称")  # 模块名称
# class TestUtil:
#     @allure.story("创建调拨单")  # 场景名称
#     @allure.title("创建调拨单，撤回调拨单")  # 用例名称
#     @allure.description("创建调拨单页面，同个客户不同仓库间调拨，然后撤回调拨单，形成闭环")
#     @allure.severity("normal")  # 用例等级
#     @pytest.mark.smoke  # 用例标记
#     def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
#         user = LoginPage(drivers)
#         user.dcr_login(drivers, "BD291501", "dcr123456")
#         all_visit = TransferOrderPage(drivers)
#         all_visit.click_menu("Inventory Management", "Transfer Order")
#         #  新增TransferOrder
#         all_visit.click_create()
#         all_visit.input_to_warehouse('lhmSubdealer001 WBD291503')
#         all_visit.input_imei('350644371718348')
#         all_visit.click_check()
#         all_visit.click_submit()
#         all_visit.click_ok()
#         #  撤回新增的TransferOrder
#         all_visit.choose_box()
#         all_visit.click_more_option()
#         all_visit.click_recall()
#         all_visit.click_recall_confirm()
#         #  增加数据库断言 前端断言  后端断言  相对路径


#     @allure.story("二级标题")  # 场景名称
#     @allure.title("三级标题")  # 用例名称
#     @allure.description("创建调拨单页面，同级调拨：不同客户间调拨")
#     @allure.severity("normal")  # 用例等级
#     @pytest.mark.smoke  # 用例标记
#     def test_001_002(self, drivers):
#         user = LoginPage(drivers)
#         user.dcr_login(drivers, "BD291501", "dcr123456")
#         all_visit = TransferOrderPage(drivers)
#         all_visit.click_menu("Inventory Management", "Transfer Order")
#         all_visit.click_create()
#         all_visit.input_to_customer('NG20613 xylSub dealer')
#         all_visit.input_to_warehouse('NG2061303 WNG2061304')
#         all_visit.input_imei('350644371878407')
#         all_visit.click_check()
#         all_visit.click_submit()
#
#     @allure.story("二级标题")  # 场景名称
#     @allure.title("三级标题")  # 用例名称
#     @allure.description("Transfer Order页面，No Receive状态的调拨单，点击”More Option---->Recall,进行撤回操作")
#     @allure.severity("normal")  # 用例等级
#     @pytest.mark.smoke  # 用例标记
#     def test_001_003(self, drivers):
#         user = LoginPage(drivers)
#         user.dcr_login(drivers, "BD291501", "dcr123456")
#         all_visit = TransferOrderPage(drivers)
#         all_visit.click_menu("Inventory Management", "Transfer Order")
#         all_visit.choose_box()  # 勾选框
#         all_visit.click_more_option()  # 点击more option
#         all_visit.click_recall()  # 点击recall
#         all_visit.click_confirm()  # 点击confirm


if __name__ == '__main__':
    pytest.main(['InventoryManagement_TransferOrder.py'])
