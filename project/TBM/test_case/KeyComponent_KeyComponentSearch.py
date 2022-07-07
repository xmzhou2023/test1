# import allure
# import pytest
# import datetime
# from libs.common.time_ui import sleep
# from project.TBM.page_base.assert_ui import *
# from project.TBM.page_object.ShippingCountry_ShippingCountrySearch import ShippingCountrySearch
#
# """
#     用例等级说明:
#         blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
#         critical级别: 临界缺陷(功能点缺失)
#         normal级别:普通缺陷(数值计算错误)
#         minor级别: 次要缺陷(界面错误与UI需求不符)
#         trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
# """
#
# @allure.feature("出货国家-出货国家查询") # 模块名称
# class TestCreateProcess:
#     @allure.story("创建流程") # 场景名称
#     @allure.title("出货国家查询页面，发起变更产品，跳转发起流程页面")  # 用例名称
#     @allure.description("进入出货国家查询页面，品牌暂时选择infinix，点击查询，勾选几条，点击变更产品，提示变更产品的产品经理不是当前登录人，"
#                         "是否继续？，点击【是】，提示变更产品的项目名称不一致，是否继续？点击【是】，跳转至单据发起流程页面")
#     @allure.severity("normal")  # 用例等级
#     @pytest.mark.smoke # 用例标记
#     def test_001_001(self, drivers): # 用例名称取名规范'test+场景编号+用例编号'
#         """
#         回归测试用例：001
#         用例：进入出货国家查询页面，品牌暂时选择infinix，点击查询，勾选几条，点击变更产品，提示变更产品的产品经理不是当前登录人，
#             是否继续？，点击【是】，提示变更产品的项目名称不一致，是否继续？点击【是】，跳转至单据发起流程页面
#         """
#         user = ShippingCountrySearch(drivers)
#         user.refresh_webpage_click_menu()
#         user.input_shipping_country_search_condition('品牌', 'Infinix')
#         user.input_shipping_country_search_condition('项目名称', '12232eeee')
#         user.click_shipping_country_search_search()
#         user.click_shipping_country_search_checkbox('12232eeee')
#         user.input_shipping_country_search_condition('品牌', 'Infinix')
#         user.input_shipping_country_search_condition('项目名称', 'vsdfgvs')
#         user.click_shipping_country_search_search()
#         user.click_shipping_country_search_checkbox('vsdfgvs')
#         user.click_shipping_country_search_change('变更产品')
#         user.assert_shipping_country_search_change_tip()
#         DomAssert(drivers).assert_att('单据发起流程')
#
#     @allure.story("创建流程") # 场景名称
#     @allure.title("变更产品流程发起成功")  # 用例名称
#     @allure.description("进入单据发起流程页面，修改产品定义信息，选择汇签/抄送人员，点击提交，提示请求成功")
#     @allure.severity("normal")  # 用例等级
#     @pytest.mark.smoke # 用例标记
#     def test_001_002(self, drivers): # 用例名称取名规范'test+场景编号+用例编号'
#         user = ShippingCountrySearch(drivers)
#         user.refresh_webpage_click_menu()
#         user.input_shipping_country_search_condition('品牌', 'Infinix')
#         user.input_shipping_country_search_condition('项目名称', '出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_search()
#         user.click_shipping_country_search_checkbox('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_change('变更产品')
#         user.click_oneworks_shipping_country_search_product_definition_info_edit('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#         user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
#         user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'市场名称test{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'项目名称test{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
#         user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
#         user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '1G')
#         user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'G70')
#         user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#         user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#         user.click_shipping_country_flow_add_submit()
#         process_code = user.get_shipping_country_flow_info('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')[2]
#         user.delete_shipping_country_flow(process_code)
#
# @allure.feature("出货国家-出货国家查询")  # 模块名称
# class TestCreateProcess:
#     @allure.story("审批流程")  # 场景名称
#     @allure.title("产品部管理员审核成功")  # 用例名称
#     @allure.description("产品部管理员审核：点击同意，提示请求成功")
#     @allure.severity("normal")  # 用例等级
#     @pytest.mark.smoke  # 用例标记
#     def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
#         """
#         回归测试用例：002
#         用例：产品部管理员审核：点击同意，提示请求成功
#         """
#         user = ShippingCountrySearch(drivers)
#         user.refresh_webpage_click_menu()
#         user.input_shipping_country_search_condition('品牌', 'Infinix')
#         user.input_shipping_country_search_condition('项目名称', '出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_search()
#         user.click_shipping_country_search_checkbox('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_change('变更产品')
#         user.click_oneworks_shipping_country_search_product_definition_info_edit('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#         user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
#         user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'市场名称test{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'项目名称test{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
#         user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
#         user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '1G')
#         user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'G70')
#         user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#         user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#         user.click_shipping_country_flow_add_submit()
#         process_code = user.get_shipping_country_flow_info('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')[2]
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#         #     user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#         #     user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
#         #     user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
#         user.delete_shipping_country_flow(process_code)
#
#
#     def test_004(self, drivers, logins):
#         """
#         回归测试用例：002
#         用例：产品部汇签：点击同意，提示请求成功
#         """
#         user = ShippingCountrySearch(drivers)
#         user.refresh_webpage_click_menu()
#         user.input_shipping_country_search_condition('品牌', 'Infinix')
#         user.input_shipping_country_search_condition('项目名称', '出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_search()
#         user.click_shipping_country_search_checkbox('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_change('变更产品')
#         user.click_oneworks_shipping_country_search_product_definition_info_edit('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#         user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
#         user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'市场名称test{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'项目名称test{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
#         user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
#         user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '2G')
#         user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'G70')
#         user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#         user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#         user.click_shipping_country_flow_add_submit()
#         process_code = user.get_shipping_country_flow_info('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')[2]
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#         user.delete_shipping_country_flow(process_code)
#
#     def test_005(self, drivers, logins):
#         """
#         回归测试用例：002
#         用例：产品经理修改：产品定义信息：点击编辑，修改信息后，点击确定，点击同意
#         """
#         user = ShippingCountrySearch(drivers)
#         user.refresh_webpage_click_menu()
#         user.input_shipping_country_search_condition('品牌', 'Infinix')
#         user.input_shipping_country_search_condition('项目名称', '出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_search()
#         user.click_shipping_country_search_checkbox('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_change('变更产品')
#         user.click_oneworks_shipping_country_search_product_definition_info_edit('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
#         user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', '修改市场名称')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', '修改项目名称')
#         user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
#         user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
#         user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '2G')
#         user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'G70')
#         user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#         user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#         user.click_shipping_country_flow_add_submit()
#         process_code = user.get_shipping_country_flow_info('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')[2]
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#         user.assert_shipping_country_flow_my_todo_node(process_code, '产品经理修改', True)
#         user.enter_shipping_country_flow_onework_edit(process_code)
#         user.click_oneworks_shipping_country_search_product_definition_info_edit('修改项目名称')
#         querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#         user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本3')
#         user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'修改市场名称{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目名称',  f'修改项目名称{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '256+8')
#         user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '印度市场')
#         user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '3G')
#         user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'MT6762D')
#         user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#         user.click_onework_shipping_country_flow_agree()
#         DomAssert(drivers).assert_att('审核通过')
#         user.quit_shipping_country_flow_onework()
#         user.delete_shipping_country_flow(process_code)
#
#     def test_006(self, drivers, logins):
#         """
#         回归测试用例：002
#         用例：产品部管理员复核：点击同意，提示请求成功
#         """
#         user = ShippingCountrySearch(drivers)
#         user.refresh_webpage_click_menu()
#         user.input_shipping_country_search_condition('品牌', 'Infinix')
#         user.input_shipping_country_search_condition('项目名称', '出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_search()
#         user.click_shipping_country_search_checkbox('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_change('变更产品')
#         querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#         user.click_oneworks_shipping_country_search_product_definition_info_edit('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')
#         user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
#         user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'修改市场名称{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'修改项目名称{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
#         user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
#         user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '1G')
#         user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'G70')
#         user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#         user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#         user.click_shipping_country_flow_add_submit()
#         process_code = user.get_shipping_country_flow_info('出货国家查询-变更产品-部分流程-自动化测试项目-项目名称')[2]
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#         user.assert_shipping_country_flow_my_todo_node(process_code, '产品经理修改', True)
#         user.enter_shipping_country_flow_onework_edit(process_code)
#         user.click_oneworks_shipping_country_search_product_definition_info_edit(f'修改项目名称{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本3')
#         querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#         user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'修改市场名称test{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'修改项目名称test{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '256+8')
#         user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '印度市场')
#         user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '2G')
#         user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'MT6762D')
#         user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#         user.click_onework_shipping_country_flow_agree()
#         DomAssert(drivers).assert_att('审核通过')
#         user.quit_shipping_country_flow_onework()
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员复核')
#         user.delete_shipping_country_flow(process_code)
#
#     def test_007(self, drivers, logins):
#         """
#         回归测试用例：002
#         用例：项目经理审批：点击同意，提示请求成功
#         """
#         user = ShippingCountrySearch(drivers)
#         user.refresh_webpage_click_menu()
#         user.input_shipping_country_search_condition('品牌', 'Infinix')
#         user.input_shipping_country_search_condition('项目名称', '出货国家查询-变更产品-全流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_search()
#         user.click_shipping_country_search_checkbox('出货国家查询-变更产品-全流程-自动化测试项目-项目名称')
#         user.click_shipping_country_search_change('变更产品')
#         querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#         user.click_oneworks_shipping_country_search_product_definition_info_edit('出货国家查询-变更产品-全流程-自动化测试项目-项目名称')
#         user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
#         user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'修改市场名称{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'修改项目名称{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
#         user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
#         user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '3G')
#         user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'MT6580P')
#         user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#         user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#         user.click_shipping_country_flow_add_submit()
#         process_code = user.get_shipping_country_flow_info('出货国家查询-变更产品-全流程-自动化测试项目-项目名称')[2]
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#         user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
#         user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
#         sleep(60)
#         user.refresh_webpage_click_menu()
#         user.input_shipping_country_search_condition('品牌', 'Infinix')
#         user.input_shipping_country_search_condition('项目名称',  f'修改项目名称{querytime}')
#         user.click_shipping_country_search_search()
#         user.click_shipping_country_search_checkbox( f'修改项目名称{querytime}')
#         user.click_shipping_country_search_change('变更产品')
#         user.click_oneworks_shipping_country_search_product_definition_info_edit( f'修改项目名称{querytime}')
#         user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
#         user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', '出货国家查询-变更产品-全流程-自动化测试项目-市场名称')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', '出货国家查询-变更产品-全流程-自动化测试项目-项目名称')
#         user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
#         user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
#         user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
#         user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '4G')
#         user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'G70')
#         user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#         user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#         user.click_shipping_country_flow_add_submit()
#         process_code = user.get_shipping_country_flow_info(f'修改项目名称{querytime}')[2]
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#         user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#         user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
#         user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
#         sleep(60)
#
#         def test_008(self, drivers, logins):
#             """
#             回归测试用例：002
#             用例：变更产品：抄送（自动抄送，不需要操作）：出货国家-出货国家流程，查看单据状态已变为审批通过
#             """
#             user = ShippingCountrySearch(drivers)
#             user.refresh_webpage_click_menu()
#             user.input_shipping_country_search_condition('品牌', 'Infinix')
#             user.input_shipping_country_search_condition('项目名称', '出货国家查询-变更产品-全流程-自动化测试项目-项目名称')
#             user.click_shipping_country_search_search()
#             user.click_shipping_country_search_checkbox('出货国家查询-变更产品-全流程-自动化测试项目-项目名称')
#             user.click_shipping_country_search_change('变更产品')
#             querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#             user.click_oneworks_shipping_country_search_product_definition_info_edit('出货国家查询-变更产品-全流程-自动化测试项目-项目名称')
#             user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
#             user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'修改市场名称{querytime}')
#             user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'修改项目名称{querytime}')
#             user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
#             user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
#             user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
#             user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '3G')
#             user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'MT6580P')
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#             user.click_shipping_country_flow_add_submit()
#             process_code = user.get_shipping_country_flow_info('出货国家查询-变更产品-全流程-自动化测试项目-项目名称')[2]
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
#             user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
#             user.assert_shipping_country_flow_my_application_node(process_code, '抄送', True)
#             sleep(60)
#             user.assert_shipping_country_flow_my_application_flow(process_code, '审批完成')
#             document_status = user.get_shipping_country_flow_info('出货国家查询-变更产品-全流程-自动化测试项目-项目名称')[6]
#             ValueAssert(drivers).value_assert_equal('审批通过', document_status)
#             user.refresh_webpage_click_menu()
#             user.input_shipping_country_search_condition('品牌', 'Infinix')
#             user.input_shipping_country_search_condition('项目名称', f'修改项目名称{querytime}')
#             user.click_shipping_country_search_search()
#             user.click_shipping_country_search_checkbox(f'修改项目名称{querytime}')
#             user.click_shipping_country_search_change('变更产品')
#             user.click_oneworks_shipping_country_search_product_definition_info_edit(f'修改项目名称{querytime}')
#             user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
#             user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', '出货国家查询-变更产品-全流程-自动化测试项目-市场名称')
#             user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', '出货国家查询-变更产品-全流程-自动化测试项目-项目名称')
#             user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
#             user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
#             user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
#             user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '4G')
#             user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'G70')
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#             user.click_shipping_country_flow_add_submit()
#             process_code = user.get_shipping_country_flow_info(f'修改项目名称{querytime}')[2]
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
#             user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
#
#         def test_990(self, drivers, logins):
#             """
#             回归测试用例：00X
#             用例：流程未配置区域：发起变更国家流程，东亚EE1更改为●；再次发起变更国家流程，东亚EE1更改为●，点击提交提示重复
#             """
#             user = ShippingCountrySearch(drivers)
#             """发起变更国家流程，东亚EE1更改为●"""
#             user.refresh_webpage_click_menu()
#             user.input_shipping_country_search_condition('品牌', 'Infinix')
#             user.input_shipping_country_search_condition('项目名称', '项目名称test2022-06-23-17:54:34')
#             user.click_shipping_country_search_search()
#             user.click_shipping_country_search_checkbox('项目名称test2022-06-23-17:54:34')
#             user.click_shipping_country_search_change('变更国家')
#             user.click_shipping_country_search_change_select('东亚')
#             user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-06-23-17:54:34')
#             user.edit_shipping_country_search_product_definition_ctyinfo('EE1', '●')
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#             user.click_shipping_country_flow_add_submit()
#             DomAssert(drivers).assert_att('请求成功')
#             """再次发起变更国家流程，东亚EE1更改为●"""
#             user.refresh_webpage_click_menu()
#             user.input_shipping_country_search_condition('品牌', 'Infinix')
#             user.input_shipping_country_search_condition('项目名称', '项目名称test2022-06-23-17:54:34')
#             user.click_shipping_country_search_search()
#             user.click_shipping_country_search_checkbox('项目名称test2022-06-23-17:54:34')
#             user.click_shipping_country_search_change('变更国家')
#             user.click_shipping_country_search_change_select('东亚')
#             user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-06-23-17:54:34')
#             user.edit_shipping_country_search_product_definition_ctyinfo('EE1', '●')
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#             user.click_shipping_country_flow_add_submit()
#             DomAssert(drivers).assert_att('第1行产品国家【EE1】已经存在流程中单据')
#             process_code = user.get_shipping_country_flow_info('项目名称test2022-06-23-17:54:34')[2]
#             user.delete_shipping_country_flow(process_code)
#
#         def test_991(self, drivers, logins):
#             """
#             回归测试用例：00Y
#             用例：流程未配置区域：发起变更国家流程，东亚EE1更改为●；再次发起变更国家流程，中国更改为●，
#                 点击提交，流程走到项目经理修改，将东亚EE1更改为●，点击提交提示重复
#             """
#             user = ShippingCountrySearch(drivers)
#             """发起变更国家流程，东亚EE1更改为●"""
#             user.refresh_webpage_click_menu()
#             user.input_shipping_country_search_condition('品牌', 'Infinix')
#             user.input_shipping_country_search_condition('项目名称', '项目名称test')
#             user.click_shipping_country_search_search()
#             user.click_shipping_country_search_checkbox('项目名称test')
#             user.click_shipping_country_search_change('变更国家')
#             user.click_shipping_country_search_change_select('东亚')
#             user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test')
#             user.edit_shipping_country_search_product_definition_ctyinfo('EE1', '●')
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#             user.click_shipping_country_flow_add_submit()
#             DomAssert(drivers).assert_att('请求成功')
#             process_code1 = user.get_shipping_country_flow_info('项目名称test')[2]
#             """再次发起变更国家流程，中国更改为●"""
#             user.refresh_webpage_click_menu()
#             user.input_shipping_country_search_condition('品牌', 'Infinix')
#             user.input_shipping_country_search_condition('项目名称', '项目名称test')
#             user.click_shipping_country_search_search()
#             user.click_shipping_country_search_checkbox('项目名称test')
#             user.click_shipping_country_search_change('变更国家')
#             user.click_shipping_country_search_change_select('东亚')
#             user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test')
#             user.edit_shipping_country_search_product_definition_ctyinfo('中国', '●')
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#             user.click_shipping_country_flow_add_submit()
#             DomAssert(drivers).assert_att('请求成功')
#             """流程走到项目经理修改"""
#             process_code = user.get_shipping_country_flow_info('项目名称test')[2]
#             user.enter_shipping_country_flow_onework_edit(process_code)
#             user.click_onework_shipping_country_flow_agree()
#             DomAssert(drivers).assert_att('审核通过')
#             user.quit_shipping_country_flow_onework()
#             user.assert_shipping_country_flow_my_todo_node(process_code, '产品部汇签', True)
#             user.enter_shipping_country_flow_onework_edit(process_code)
#             user.click_onework_shipping_country_flow_agree()
#             DomAssert(drivers).assert_att('审核通过')
#             user.quit_shipping_country_flow_onework()
#             user.assert_shipping_country_flow_my_todo_node(process_code, '产品经理修改', True)
#             user.enter_shipping_country_flow_onework_edit(process_code)
#             """将东亚EE1更改为●，点击提交提示重复"""
#             user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test')
#             user.edit_shipping_country_search_product_definition_ctyinfo('EE1', '●')
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.click_onework_shipping_country_flow_agree()
#             user.enter_shipping_country_search_onework_iframe()
#             DomAssert(drivers).assert_att('第1行产品国家【EE1】已经存在流程中单据')
#             user.quit_shipping_country_flow_onework()
#             user.delete_shipping_country_flow(process_code)
#             user.delete_shipping_country_flow(process_code1)
#
#         def test_992(self, drivers, logins):
#             """
#             回归测试用例：00Y
#             用例：流程未配置区域：  发起流程 EE1更改为 ●，走完流程检查EE1是否为 ●；
#                                 发起流程 乍得更改为 ●，走完流程检查乍得是否为 ●；
#                                 发起流程 中国更改为 ●，走完流程检查中国是否为 ●；
#             """
#             user = ShippingCountrySearch(drivers)
#             """发起流程 EE1更改为 ●，走完流程检查EE1是否为 ●；"""
#             user.refresh_webpage_click_menu()
#             user.input_shipping_country_search_condition('品牌', 'Infinix')
#             user.input_shipping_country_search_condition('项目名称', '项目名称test2022-06-27-14:11:03')
#             user.click_shipping_country_search_search()
#             user.check_reset_shipping_country_search_cty_status('项目名称test2022-06-27-14:11:03', '东亚')
#             user.click_shipping_country_search_checkbox('项目名称test2022-06-27-14:11:03')
#             user.click_shipping_country_search_change('变更国家')
#             user.click_shipping_country_search_change_select('东亚')
#             user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-06-27-14:11:03')
#             user.edit_shipping_country_search_product_definition_ctyinfo('EE1', '●')
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#             user.click_shipping_country_flow_add_submit()
#             DomAssert(drivers).assert_att('请求成功')
#             process_code = user.get_shipping_country_flow_info('项目名称test2022-06-27-14:11:03')[2]
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
#             user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
#             country_status = user.get_shipping_country_search_cty_status('项目名称test2022-06-27-14:11:03')
#             ValueAssert(drivers).value_assert_equal('●', country_status[0])
#             """发起流程 乍得更改为 ●，走完流程检查乍得是否为 ●；"""
#             user.refresh_webpage_click_menu()
#             user.input_shipping_country_search_condition('品牌', 'Infinix')
#             user.input_shipping_country_search_condition('项目名称', '项目名称test2022-06-27-14:11:03')
#             user.click_shipping_country_search_search()
#             user.click_shipping_country_search_checkbox('项目名称test2022-06-27-14:11:03')
#             user.click_shipping_country_search_change('变更国家')
#             user.click_shipping_country_search_change_select('东亚')
#             user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-06-27-14:11:03')
#             user.edit_shipping_country_search_product_definition_ctyinfo('乍得', '●')
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#             user.click_shipping_country_flow_add_submit()
#             DomAssert(drivers).assert_att('请求成功')
#             process_code = user.get_shipping_country_flow_info('项目名称test2022-06-27-14:11:03')[2]
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
#             user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
#             country_status = user.get_shipping_country_search_cty_status('项目名称test2022-06-27-14:11:03')
#             ValueAssert(drivers).value_assert_equal('●', country_status[1])
#             """发起流程 中国更改为 ●，走完流程检查中国是否为 ●；"""
#             user.refresh_webpage_click_menu()
#             user.input_shipping_country_search_condition('品牌', 'Infinix')
#             user.input_shipping_country_search_condition('项目名称', '项目名称test2022-06-27-14:11:03')
#             user.click_shipping_country_search_search()
#             user.click_shipping_country_search_checkbox('项目名称test2022-06-27-14:11:03')
#             user.click_shipping_country_search_change('变更国家')
#             user.click_shipping_country_search_change_select('东亚')
#             user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-06-27-14:11:03')
#             user.edit_shipping_country_search_product_definition_ctyinfo('中国', '●')
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#             user.click_shipping_country_flow_add_submit()
#             DomAssert(drivers).assert_att('请求成功')
#             process_code = user.get_shipping_country_flow_info('项目名称test2022-06-27-14:11:03')[2]
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
#             user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
#             country_status = user.get_shipping_country_search_cty_status('项目名称test2022-06-27-14:11:03')
#             ValueAssert(drivers).value_assert_equal('●', country_status[2])
#             """将东亚所有区域状态重置为空"""
#             user.refresh_webpage_click_menu()
#             user.input_shipping_country_search_condition('品牌', 'Infinix')
#             user.input_shipping_country_search_condition('项目名称', '项目名称test2022-06-27-14:11:03')
#             user.click_shipping_country_search_search()
#             user.click_shipping_country_search_checkbox('项目名称test2022-06-27-14:11:03')
#             user.click_shipping_country_search_change('变更国家')
#             user.click_shipping_country_search_change_select('东亚')
#             user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-06-27-14:11:03')
#             user.edit_shipping_country_search_product_definition_closd_ctyinfo()
#             user.click_oneworks_shipping_country_search_product_definition_info_confirm()
#             user.select_shipping_country_flow_signatory('汇签人员', '李小素')
#             user.click_shipping_country_flow_add_submit()
#             DomAssert(drivers).assert_att('请求成功')
#             process_code = user.get_shipping_country_flow_info('项目名称test2022-06-27-14:11:03')[2]
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
#             user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
#             user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
#
# if __name__ == '__main__':
#     pytest.main(['project/DRP/testcase/run_code.py'])
