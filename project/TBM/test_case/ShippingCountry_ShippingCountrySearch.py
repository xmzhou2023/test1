import pytest
import datetime
from public.base.assert_ui import *
from project.TBM.page_object.ShippingCountry_ShippingCountrySearch import ShippingCountrySearch


@allure.feature("出货国家-出货国家查询")
class TestCreateProcess:
    @allure.story("创建流程")
    @allure.title("出货国家查询页面，发起变更产品，跳转发起流程页面")
    @allure.description("进入出货国家查询页面，品牌暂时选择infinix，点击查询，勾选几条，点击变更产品，提示变更产品的产品经理不是当前登录人，是否继续？，点击【是】，提示变更产品的项目名称不一致，是否继续？点击【是】，跳转至单据发起流程页面")
    @allure.severity("normal")
    @pytest.mark.UT # 用例标记
    def test_001_001(self, drivers):
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_shipping_country_search_condition('品牌', 'Infinix')
        user.input_shipping_country_search_condition('项目名称', '12232eeee')
        user.click_shipping_country_search_search()
        user.click_shipping_country_search_checkbox('12232eeee')
        user.input_shipping_country_search_condition('品牌', 'Infinix')
        user.input_shipping_country_search_condition('项目名称', 'vsdfgvs')
        user.click_shipping_country_search_search()
        user.click_shipping_country_search_checkbox('vsdfgvs')
        user.click_shipping_country_search_change('变更产品')
        user.assert_shipping_country_search_change_tip()
        DomAssert(drivers).assert_att('单据发起流程')

    @allure.story("创建流程") # 场景名称
    @allure.title("变更产品流程发起成功")  # 用例名称
    @allure.description("进入单据发起流程页面，修改产品定义信息，选择汇签/抄送人员，点击提交，提示请求成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers): # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_shipping_country_search_condition('品牌', 'Infinix')
        user.input_shipping_country_search_condition('项目名称', '项目名称test2022-07-14-14:44:47')
        user.click_shipping_country_search_search()
        user.click_shipping_country_search_checkbox('项目名称test2022-07-14-14:44:47')
        user.click_shipping_country_search_change('变更产品')
        user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-07-14-14:44:47')
        querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
        user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'市场名称test{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'项目名称test{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+6')
        user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
        user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '1G')
        user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'G70')
        user.click_oneworks_shipping_country_search_product_definition_info_confirm()
        user.select_shipping_country_flow_signatory('汇签人员', '李小素')
        user.click_shipping_country_flow_add_submit()
        process_code = user.get_shipping_country_flow_info('项目名称test2022-07-14-14:44:47')[2]
        user.delete_shipping_country_flow(process_code)


@allure.feature("出货国家-出货国家查询")  # 模块名称
class TestTheProcessOfExaminationAndApproval:
    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部管理员审核成功")  # 用例名称
    @allure.description("产品部管理员审核: 点击同意，提示请求成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_shipping_country_search_condition('品牌', 'Infinix')
        user.input_shipping_country_search_condition('项目名称', '项目名称test2022-07-14-14:44:47')
        user.click_shipping_country_search_search()
        user.click_shipping_country_search_checkbox('项目名称test2022-07-14-14:44:47')
        user.click_shipping_country_search_change('变更产品')
        user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-07-14-14:44:47')
        querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本3')
        user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'市场名称test{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'项目名称test{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '128+8')
        user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
        user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '3G')
        user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'MT6762D')
        user.click_oneworks_shipping_country_search_product_definition_info_confirm()
        user.select_shipping_country_flow_signatory('汇签人员', '李小素')
        user.click_shipping_country_flow_add_submit()
        DomAssert(drivers).assert_att('请求成功')
        process_code = user.get_shipping_country_flow_info('项目名称test2022-07-14-14:44:47')[2]
        user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
        user.delete_shipping_country_flow(process_code)

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部汇签审核成功")  # 用例名称
    @allure.description("产品部汇签：点击同意，提示请求成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_shipping_country_search_condition('品牌', 'Infinix')
        user.input_shipping_country_search_condition('项目名称', '项目名称test2022-07-14-14:44:47')
        user.click_shipping_country_search_search()
        user.click_shipping_country_search_checkbox('项目名称test2022-07-14-14:44:47')
        user.click_shipping_country_search_change('变更产品')
        user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-07-14-14:44:47')
        querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本3')
        user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'市场名称test{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'项目名称test{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+6')
        user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
        user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '3G')
        user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'MT6762D')
        user.click_oneworks_shipping_country_search_product_definition_info_confirm()
        user.select_shipping_country_flow_signatory('汇签人员', '李小素')
        user.click_shipping_country_flow_add_submit()
        DomAssert(drivers).assert_att('请求成功')
        process_code = user.get_shipping_country_flow_info('项目名称test2022-07-14-14:44:47')[2]
        user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
        user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
        user.delete_shipping_country_flow(process_code)

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品经理修改审核成功")  # 用例名称
    @allure.description("产品经理修改：产品定义信息：点击编辑，修改信息后，点击确定，点击同意")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_shipping_country_search_condition('品牌', 'Infinix')
        user.input_shipping_country_search_condition('项目名称', '项目名称test2022-07-14-14:44:47')
        user.click_shipping_country_search_search()
        user.click_shipping_country_search_checkbox('项目名称test2022-07-14-14:44:47')
        user.click_shipping_country_search_change('变更产品')
        user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-07-14-14:44:47')
        user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
        user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', '修改市场名称')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', '修改项目名称')
        user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
        user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
        user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '2G')
        user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'G70')
        user.click_oneworks_shipping_country_search_product_definition_info_confirm()
        user.select_shipping_country_flow_signatory('汇签人员', '李小素')
        user.click_shipping_country_flow_add_submit()
        DomAssert(drivers).assert_att('请求成功')
        process_code = user.get_shipping_country_flow_info('项目名称test2022-07-14-14:44:47')[2]
        user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
        user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
        user.assert_shipping_country_flow_my_todo_node(process_code, '产品经理修改', True)
        user.enter_shipping_country_flow_onework_edit(process_code)
        user.click_oneworks_shipping_country_search_product_definition_info_edit('修改项目名称')
        querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本3')
        user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'修改市场名称{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目名称',  f'修改项目名称{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '256+8')
        user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '印度市场')
        user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '3G')
        user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'MT6762D')
        user.click_oneworks_shipping_country_search_product_definition_info_confirm()
        user.click_onework_shipping_country_flow_agree()
        DomAssert(drivers).assert_att('审核通过')
        user.quit_shipping_country_flow_onework()
        user.delete_shipping_country_flow(process_code)

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部管理员复核审核成功")  # 用例名称
    @allure.description("产品部管理员复核：点击同意，提示请求成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_shipping_country_search_condition('品牌', 'Infinix')
        user.input_shipping_country_search_condition('项目名称', '项目名称test2022-07-14-14:44:47')
        user.click_shipping_country_search_search()
        user.click_shipping_country_search_checkbox('项目名称test2022-07-14-14:44:47')
        user.click_shipping_country_search_change('变更产品')
        querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-07-14-14:44:47')
        user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
        user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'修改市场名称{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'修改项目名称{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '128+8')
        user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
        user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '4G')
        user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'MT6580P')
        user.click_oneworks_shipping_country_search_product_definition_info_confirm()
        user.select_shipping_country_flow_signatory('汇签人员', '李小素')
        user.click_shipping_country_flow_add_submit()
        DomAssert(drivers).assert_att('请求成功')
        process_code = user.get_shipping_country_flow_info('项目名称test2022-07-14-14:44:47')[2]
        user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
        user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
        user.assert_shipping_country_flow_my_todo_node(process_code, '产品经理修改', True)
        user.enter_shipping_country_flow_onework_edit(process_code)
        user.click_oneworks_shipping_country_search_product_definition_info_edit(f'修改项目名称{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本3')
        querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'修改市场名称test{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'修改项目名称test{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '256+8')
        user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '印度市场')
        user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '2G')
        user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'MT6762D')
        user.click_oneworks_shipping_country_search_product_definition_info_confirm()
        user.click_onework_shipping_country_flow_agree()
        DomAssert(drivers).assert_att('审核通过')
        user.quit_shipping_country_flow_onework()
        user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员复核')
        user.delete_shipping_country_flow(process_code)

    @allure.story("流程审批")  # 场景名称
    @allure.title("变更产品成功,单据状态已变为审批通过")  # 用例名称
    @allure.description("变更产品：抄送-自动抄送，不需要操作：出货国家-出货国家流程，查看单据状态已变为审批通过")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_shipping_country_search_condition('品牌', 'Infinix')
        user.input_shipping_country_search_condition('项目名称', '项目名称test2022-07-12-14:22:55')
        user.click_shipping_country_search_search()
        user.click_shipping_country_search_checkbox('项目名称test2022-07-12-14:22:55')
        user.click_shipping_country_search_change('变更产品')
        querytime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        user.click_oneworks_shipping_country_search_product_definition_info_edit('项目名称test2022-07-12-14:22:55')
        user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
        user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', f'修改市场名称{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', f'修改项目名称{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
        user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
        user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '3G')
        user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'MT6580P')
        user.click_oneworks_shipping_country_search_product_definition_info_confirm()
        user.select_shipping_country_flow_signatory('汇签人员', '李小素')
        user.click_shipping_country_flow_add_submit()
        DomAssert(drivers).assert_att('请求成功')
        process_code = user.get_shipping_country_flow_info('项目名称test2022-07-12-14:22:55')[2]
        user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
        user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
        user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
        user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
        user.assert_shipping_country_flow_my_application_node(process_code, '抄送', True)
        user.assert_flow_compelete(process_code)
        document_status = user.get_shipping_country_flow_info('项目名称test2022-07-12-14:22:55')[6]
        ValueAssert.value_assert_equal(document_status, '审批通过')
        user.refresh_webpage_click_menu()
        user.input_shipping_country_search_condition('品牌', 'Infinix')
        user.input_shipping_country_search_condition('项目名称', f'修改项目名称{querytime}')
        user.click_shipping_country_search_search()
        user.click_shipping_country_search_checkbox(f'修改项目名称{querytime}')
        user.click_shipping_country_search_change('变更产品')
        user.click_oneworks_shipping_country_search_product_definition_info_edit(f'修改项目名称{querytime}')
        user.edit_oneworks_shipping_country_search_product_definition_info('全球版本', '版本2')
        user.edit_oneworks_shipping_country_search_product_definition_info('市场名称', '市场名称test2022-07-12-14:22:55')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目名称', '项目名称test2022-07-12-14:22:55')
        user.edit_oneworks_shipping_country_search_product_definition_info('MEMORY', '64+8')
        user.edit_oneworks_shipping_country_search_product_definition_info('BANDSTRATEGY', '公开市场')
        user.edit_oneworks_shipping_country_search_product_definition_info('项目经理', '李小素')
        user.edit_oneworks_shipping_country_search_product_definition_info('aaa', '4G')
        user.edit_oneworks_shipping_country_search_product_definition_info('bbb', 'G70')
        user.click_oneworks_shipping_country_search_product_definition_info_confirm()
        user.select_shipping_country_flow_signatory('汇签人员', '李小素')
        user.click_shipping_country_flow_add_submit()
        DomAssert(drivers).assert_att('请求成功')
        process_code = user.get_shipping_country_flow_info(f'修改项目名称{querytime}')[2]
        user.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
        user.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
        user.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
        user.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
        sleep(60)


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
