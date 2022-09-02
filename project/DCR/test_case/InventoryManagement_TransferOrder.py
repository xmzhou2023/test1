# import logging
# import allure
# import pytest
# from libs.common.connect_sql import SQL
# from project.DCR.page_object.Center_Component import LoginPage
# from project.DCR.page_object.InventoryManagement_TransferOrder import TransferOrderPage
# """
#     用例等级说明:
#         blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
#         critical级别: 临界缺陷(功能点缺失)
#         normal级别:普通缺陷(数值计算错误)
#         minor级别: 次要缺陷(界面错误与UI需求不符)
#         trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
# """
#
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
#
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
#
#     pass
#
#
# if __name__ == '__main__':
#     pytest.main(['project/DRP/testcase/run_code.py'])
