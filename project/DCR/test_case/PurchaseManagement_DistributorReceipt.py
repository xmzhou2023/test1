# from project.DCR.page_object.PurchaseManagement_DistributorReceipt import DitributorReceiptPage
# from project.DCR.page_object.Center_Component import LoginPage
# from public.base.basics import Base
# from public.base.assert_ui import ValueAssert
# from libs.common.time_ui import sleep
# import pytest
# import allure
#
#
# @allure.feature("采购管理-国包收货")
# class TestDistributorReceipt:
#     @allure.story("新增")
#     @allure.title("国包用户进入Distributor Receipt页面，进行“快速收货”操作")
#     @allure.description("国包用户进入Distributor Receipt页面，进行“快速收货”操作")
#     @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
#     def test_001_001(self, drivers):
#         """DCR 国包账号登录"""
#         user = LoginPage(drivers)
#         user.dcr_login(drivers, "BD40344201", "dcr123456")
#         sleep(5)
#
#         """销售管理菜单-出库单-筛选出库单用例"""
#         user.click_gotomenu("Purchase Management", "Distributor Receipt")
#         sleep(6)
#         """调用国包快速收货用例，并断言收货是否成功"""
#         receipt = DitributorReceiptPage(drivers)
#         list_dn = receipt.get_list_dn_text()
#         list_quantity = receipt.get_list_quantity_text()
#         receipt.click_unfold()
#         receipt.input_dn(list_dn)
#         receipt.click_search()
#         receipt.click_first_chekbox()
#         receipt.click_quick_receive()
#
#         dialog_dn = receipt.get_dialog_text_dn()
#         dialog_quantity = receipt.get_dialog_text_quantity()
#
#         """ 增加断言，验证列表获取的DN与快速收货对话框的DN是否一致 """
#         ValueAssert.value_assert_equal(list_dn, dialog_dn)
#         """断言列表获取的quantity与快速收货对话框的quantity是否一致"""
#         ValueAssert.value_assert_equal(list_quantity, dialog_quantity)
#         receipt.click_quick_receive_submit()
#         """断言国包收货成功，状态已更新，列表显示:No Data """
#         success = receipt.get_success_text()
#         ValueAssert.value_assert_equal(success, "Set Up Successfully")
#         receipt.click_reset()
#
#
# @allure.feature("采购管理-查看IMEI详情")
# class TestQueryIMEIDetail:
#     @allure.story("查询")
#     @allure.title("国包用户进入Distributor Receipt页面，收货成功后，查看IMEI详情信息")
#     @allure.description("国包用户进入Distributor Receipt页面，收货成功后，查看IMEI详情信息是否与收货的信息一致")
#     @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
#     def test_002_001(self, drivers):
#         user = LoginPage(drivers)
#         user.dcr_login(drivers, "BD40344201", "dcr123456")
#         sleep(5)
#
#         """销售管理菜单-出库单-筛选出库单用例"""
#         user.click_gotomenu("Purchase Management", "Distributor Receipt")
#         sleep(6)
#
#         receipt = DitributorReceiptPage(drivers)
#         list_dn = receipt.get_list_dn_text()
#         list_quantity = receipt.get_list_quantity_text()
#         sleep(1)
#
#         receipt.click_unfold()
#
#         receipt.input_dn(list_dn)
#         receipt.click_search()
#         receipt.click_imei_detail()
#         imei_detail_dn = receipt.get_text_imei_detail_DN()
#         detail_total = receipt.text_imei_detail_total()
#         """ 断言列表获取的DN，与打开IMEI Detail详情页的DN比较一致 """
#         ValueAssert.value_assert_In(list_dn, imei_detail_dn)
#         """ 断言列表获取的quantity总条数，与打开IMEI Detail详情页的Total总条数比较一致 """
#         ValueAssert.value_assert_In(list_quantity, detail_total)
#         receipt.click_close()
#         receipt.click_reset()
#
# if __name__ == '__main__':
#     pytest.main(['PurchaseManagement_DistributorReceipt.py'])
#
#
#
