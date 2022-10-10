import pytest
from datetime import datetime
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
        user.input_condition('品牌', 'Infinix')
        user.input_condition('项目名称', '12232eeee')
        user.click_search()
        user.click_checkbox('12232eeee')
        user.input_condition('品牌', 'Infinix')
        user.input_condition('项目名称', 'vsdfgvs')
        user.click_search()
        user.click_checkbox('vsdfgvs')
        user.click_change('变更产品')
        user.assert_change_tip()
        DomAssert(drivers).assert_att('单据发起流程')

    @allure.story("创建流程") # 场景名称
    @allure.title("变更产品流程发起成功")  # 用例名称
    @allure.description("进入单据发起流程页面，修改产品定义信息，选择汇签/抄送人员，点击提交，提示请求成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers): # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_condition('品牌', 'Infinix')
        user.input_condition('项目名称', '项目名称test2022-08-12-06:34:16')
        user.click_search()
        user.click_checkbox('项目名称test2022-08-12-06:34:16')
        user.click_change('变更产品')
        user.click_oneworks_product_definition_info_edit('项目名称test2022-08-12-06:34:16')
        querytime = datetime.now().strftime('%Y%m%d%H%M%S')
        user.input_product_definition_info('全球版本', '版本3')
        user.input_product_definition_info('市场名称', f'市场名称test{querytime}')
        user.input_product_definition_info('项目名称', f'项目名称test{querytime}')
        user.input_product_definition_info('MEMORY', '64+6')
        user.input_product_definition_info('BAND STRATEGY', '拉美市场')
        user.input_product_definition_info('项目经理', '李小素')
        user.input_product_definition_info('摄像头', '摄像头')
        user.input_product_definition_info('型号', '型号')
        user.input_product_definition_info('新增', '新增')
        user.input_product_definition_info('再增', '2G')
        user.input_product_definition_info('配色', '魅海蓝/Aqua Blue')
        user.input_product_definition_info('尺寸', 'MT6762D')
        user.click_oneworks_product_definition_info_confirm()
        user.select_signatory('汇签人员', '李小素')
        user.click_add_submit()
        user.assert_toast()
        process_code = user.get_info('项目名称test2022-08-12-06:34:16')[2]
        user.delete_shipping_country_search(process_code)

    @allure.story("创建流程")
    @allure.title("变更已有产品成功")
    @allure.description("选择一条数据点击变更国家，进入变更国家页面，点击变更已有产品，选择一个产品，页面上会多一条选择的产品")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_condition('品牌', 'Infinix')
        user.input_condition('项目名称', '出货国家查询变更产品部分流程')
        user.click_search()
        user.click_checkbox('出货国家查询变更产品部分流程')
        user.click_change('变更国家')
        user.click_change_select('东亚')
        user.click_products()
        user.search_products('市场名称', '出货国家查询-变更产品-全流程-自动化测试项目-市场名称')
        user.select_products('出货国家查询-变更产品-全流程-自动化测试项目-市场名称')
        user.assert_change_success('出货国家查询-变更产品-全流程-自动化测试项目-市场名称')

    @allure.story("创建流程")
    @allure.title("查看版本记录，显示不同的版本")
    @allure.description("选中一条数据点击市场名称进入，进入后点击查看版本记录，会弹出页面，显示不同的版本")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_condition('品牌', 'Infinix')
        user.input_condition('项目名称', '出货国家查询变更产品自动化全流程测试')
        user.click_search()
        user.click_TableLink('出货国家查询变更产品自动化全流程测试')
        user.click_ChangeHistory('查看版本记录')
        user.assert_VersionHistory()

    @allure.story("创建流程")
    @allure.title("查看变更记录，显示变更数据")
    @allure.description("选中一条数据点击市场名称进入，进入后点击查看变更记录，会弹出新页面，显示变更数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_condition('品牌', 'Infinix')
        user.input_condition('项目名称', '出货国家查询变更产品自动化全流程测试')
        user.click_search()
        user.click_TableLink('出货国家查询变更产品自动化全流程测试')
        user.click_ChangeHistory('查看变更记录')
        user.assert_ChangeHistory()

    @allure.story("创建流程")
    @allure.title("批量编辑出货/认证备份，变成成功")
    @allure.description("选中一条数据点击变更国家，进入变更国家页面再次点击变更已有产品，选择多个产品后，点击批量修改，会出现批量修改弹出框，，选择国家区域后，再选择出货/认证备份全部为出货，确定后，所有的产品选择的国家区域都为出货")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_condition('品牌', 'Infinix')
        user.input_condition('项目名称', '出货国家查询变更产品部分流程')
        user.click_search()
        user.click_checkbox('出货国家查询变更产品部分流程')
        user.click_change('变更国家')
        user.click_change_select('东亚')
        user.click_products()
        user.search_products('市场名称', '出货国家查询-变更产品-全流程-自动化测试项目-市场名称')
        user.select_products('出货国家查询-变更产品-全流程-自动化测试项目-市场名称')
        user.click_InfoCheckBox()
        user.click_Bulk_Editing()
        user.select_Bulk_Editing_cty('柬埔寨')
        user.select_Bulk_Editing_status('●')
        user.select_Bulk_Editing_confirm()
        user.select_Bulk_Editing_cancel()
        # user.assert_search_result('中国', '✔')
        user.assert_search_result('柬埔寨', '●')

@allure.feature("出货国家-出货国家查询")  # 模块名称
class TestTheProcessOfExaminationAndApproval:
    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部管理员审核成功")  # 用例名称
    @allure.description("产品部管理员审核: 点击同意，提示请求成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_001(self, drivers, SaleCountry_ProductChange_API):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage()
        user.onework_agree_flow(SaleCountry_ProductChange_API[0], '产品部汇签')

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部汇签审核成功")  # 用例名称
    @allure.description("产品部汇签：点击同意，提示请求成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_002(self, drivers, SaleCountry_ProductChange_Audit_API):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage()
        user.onework_agree_flow(SaleCountry_ProductChange_Audit_API[0], '产品经理修改')

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品经理修改审核成功")  # 用例名称
    @allure.description("产品经理修改：产品定义信息：点击编辑，修改信息后，点击确定，点击同意")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_003(self, drivers, SaleCountry_ProductChange_Join_API):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(SaleCountry_ProductChange_Join_API[0])
        user.click_oneworks_product_definition_info_edit('出货国家查询变更产品部分流程')
        querytime = datetime.now().strftime('%Y%m%d%H%M%S')
        user.input_product_definition_info('全球版本', '版本2')
        user.input_product_definition_info('市场名称', f'修改市场名称{querytime}')
        user.input_product_definition_info('项目名称',  f'修改项目名称{querytime}')
        user.input_product_definition_info('MEMORY', '128+8')
        user.input_product_definition_info('BAND STRATEGY', '公开市场')
        user.input_product_definition_info('aaa', '2G')
        user.input_product_definition_info('bbb', 'MT6762D')
        user.click_oneworks_product_definition_info_confirm()
        user.click_onework_agree()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(SaleCountry_ProductChange_Join_API[0], '产品部管理员复核', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部管理员复核审核成功")  # 用例名称
    @allure.description("产品部管理员复核：点击同意，提示请求成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_004(self, drivers, SaleCountry_ProductChange_managerModify_API):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage()
        user.onework_agree_flow(SaleCountry_ProductChange_managerModify_API[0], '项目经理审批')

    @allure.story("流程审批")  # 场景名称
    @allure.title("变更产品成功,单据状态已变为审批通过")  # 用例名称
    @allure.description("变更产品：抄送-自动抄送，不需要操作：出货国家-出货国家流程，查看单据状态已变为审批通过")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_005(self, drivers, SaleCountry_ProductChange_All_API):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage()
        user.onework_agree_flow(SaleCountry_ProductChange_All_API[0], '产品部汇签')
        user.onework_agree_flow(SaleCountry_ProductChange_All_API[0], '产品经理修改')
        user.onework_agree_flow(SaleCountry_ProductChange_All_API[0], '项目经理审批')
        user.onework_agree_flow(SaleCountry_ProductChange_All_API[0])
        user.assert_my_application_node(SaleCountry_ProductChange_All_API[0], '抄送', True)
        user.assert_flow_compelete(SaleCountry_ProductChange_All_API[0])
        document_status = user.get_info(SaleCountry_ProductChange_All_API[0])[6]
        ValueAssert.value_assert_equal(document_status, '审批通过')


@allure.feature("出货国家-出货国家查询")
class TestCreateProcessExceptionScenario:
    @allure.story("创建流程异常场景")
    @allure.title("【xxxxx】产品存在在途单据【xxxxxx】")
    @allure.description("选中一条数据点击变更产品，进行发起后，再次选中该条数据点击进行变更产品，不能进行发起，并提示【xxxxx】产品存在在途单据【xxxxxx】")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_001(self, drivers, SaleCountry_ProductChange_API):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_condition('品牌', 'Infinix')
        user.input_condition('项目名称', '出货国家查询变更产品部分流程')
        user.click_search()
        user.click_checkbox('出货国家查询变更产品部分流程')
        user.click_change('变更产品')
        DomAssert(drivers).assert_att(f'【出货国家查询变更产品部分流程_出货国家查询变更产品部分流程_128+8_拉美市场】产品存在在途单据【{SaleCountry_ProductChange_API[0]}】')

    @allure.story("创建流程异常场景")
    @allure.title("第1行产品国家【xxxxx】已经存在流程中单据【xxxxxxx】！")
    @allure.description("选中一条数据点击变更国家，进行发起后，再次选中该条数据点击变更国家还是变更一样的国家，发起时会给出提示第1行产品国家【xxxxx】已经存在流程中单据【xxxxxxx】！")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_002(self, drivers, SaleCountry_CountryChange_API):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountrySearch(drivers)
        user.refresh_webpage_click_menu()
        user.input_condition('品牌', 'Infinix')
        user.input_condition('项目名称', '出货国家查询变更产品部分流程')
        user.click_search()
        user.click_checkbox('出货国家查询变更产品部分流程')
        user.click_change('变更国家')
        user.click_change_select('东亚')
        user.edit_product_definition_ctyinfo('出货国家查询变更产品部分流程', '中国', '●')
        user.click_add_submit()
        DomAssert(drivers).assert_att(f'第1行产品国家【中国】已经存在流程中单据【{SaleCountry_CountryChange_API[0]}】！')




if __name__ == '__main__':
    pytest.main(['ShippingCountry_ShippingCountrySearch.py'])
