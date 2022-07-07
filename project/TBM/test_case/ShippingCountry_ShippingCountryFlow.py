import datetime
import allure
import pytest
from libs.common.time_ui import sleep
from public.base.assert_ui import *
from project.TBM.page_object.ShippingCountry_ShippingCountryFlow import ShippingCountryFlow

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("出货国家-出货国家流程") # 模块名称
class TestCreateProcess:
    @allure.story("创建流程") # 场景名称
    @allure.title("创建流程成功")  # 用例名称
    @allure.description("项目信息随便填，产品定义信息随便填（品牌暂时选择Infinix），选择汇签/抄送人员，点击提交，提示请求成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        querytime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        user.click_shipping_country_flow_add()
        user.input_shipping_country_flow_add_item_info('品牌', 'Infinix')
        user.input_shipping_country_flow_add_item_info('项目', f'项目名称{querytime}')
        user.click_shipping_country_flow_add()
        user.input_shipping_country_flow_add_product_definition_info('全球版本','版本1')
        user.input_shipping_country_flow_add_product_definition_info('市场名称', f'市场名称{querytime}')
        user.input_shipping_country_flow_add_product_definition_info('项目名称', f'项目名称{querytime}')
        user.input_shipping_country_flow_add_product_definition_info('MEMORY', '128+8')
        user.input_shipping_country_flow_add_product_definition_info('BANDSTRATEGY', '拉美市场')
        user.input_shipping_country_flow_add_product_definition_info('项目经理', '李小素')
        user.input_shipping_country_flow_add_product_definition_info('aaa', '2G')
        user.input_shipping_country_flow_add_product_definition_info('bbb', 'MT6761')
        user.click_shipping_country_flow_product_definition_confirm()
        user.select_shipping_country_flow_signatory('汇签人员', '李小素')
        user.click_shipping_country_flow_add_submit()
        DomAssert(drivers).assert_att('请求成功')
        process_code = user.get_shipping_country_flow_info(f'项目名称{querytime}')[2]
        user.delete_shipping_country_flow(process_code)

@allure.feature("出货国家-出货国家流程")  # 模块名称
class TestTheProcessOfExaminationAndApproval:

    @pytest.fixture(scope='function', autouse=True)
    def add_machine_bom_cooperation(self, drivers):
        logging.info('开始前置操作')
        global api_response
        user = ShippingCountryFlow(drivers)
        api_response = user.api_shipping_country_flow_add()
        yield
        logging.info('开始后置操作')
        user.api_shipping_country_flow_delete(api_response[1], api_response[2])

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部管理员审核成功")  # 用例名称
    @allure.description("出货国家：产品部管理员审核,点击同意，提示请求成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.assert_shipping_country_flow_my_todo_node(api_response[0], '产品部管理员审核', True)
        user.enter_shipping_country_flow_onework_edit(api_response[0])
        user.click_onework_shipping_country_flow_agree()
        DomAssert(drivers).assert_att('请求成功')
        user.quit_shipping_country_flow_onework()
        user.assert_shipping_country_flow_my_todo_node(api_response[0], '产品部汇签', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部汇签审核成功")  # 用例名称
    @allure.description("出货国家：产品部汇签,点击同意，提示请求成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.shipping_country_flow_product_department_administrator_review(api_response[0])
        user.enter_shipping_country_flow_onework_edit(api_response[0])
        user.click_onework_shipping_country_flow_agree()
        DomAssert(drivers).assert_att('请求成功')
        user.quit_shipping_country_flow_onework()
        user.assert_shipping_country_flow_my_todo_node(api_response[0], '产品经理修改', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品经理修改审核成功")  # 用例名称
    @allure.description("出货国家：产品经理修改, 产品定义信息：点击编辑，修改信息后，点击确定，点击同意")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_003(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.shipping_country_flow_product_department_administrator_review(api_response[0])
        user.shipping_country_flow_product_department_sign(api_response[0])
        user.enter_shipping_country_flow_onework_edit(api_response[0])
        querytime2 = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        user.input_oneworks_shipping_country_flow_product_definition_info('全球版本', '版本2')
        user.input_oneworks_shipping_country_flow_product_definition_info('市场名称', f'市场名称{querytime2}')
        user.input_oneworks_shipping_country_flow_product_definition_info('项目名称', f'项目名称{querytime2}')
        user.input_oneworks_shipping_country_flow_product_definition_info('MEMORY', '64+8')
        user.input_oneworks_shipping_country_flow_product_definition_info('BANDSTRATEGY', '公开市场')
        user.input_oneworks_shipping_country_flow_product_definition_info('项目经理', '李小素')
        user.input_oneworks_shipping_country_flow_product_definition_info('aaa', '1G')
        user.input_oneworks_shipping_country_flow_product_definition_info('bbb', 'G70')
        user.click_onework_shipping_country_flow_agree()
        DomAssert(drivers).assert_att('请求成功')
        user.quit_shipping_country_flow_onework()
        user.assert_shipping_country_flow_my_todo_node(api_response[0], '产品部管理员复核', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部管理员复核审核成功")  # 用例名称
    @allure.description("出货国家：产品部管理员复核 ,点击同意，提示请求成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_004(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.shipping_country_flow_product_department_administrator_review(api_response[0])
        user.shipping_country_flow_product_department_sign(api_response[0])
        user.shipping_country_flow_product_manager_modification(api_response[0])
        user.enter_shipping_country_flow_onework_edit(api_response[0])
        user.click_onework_shipping_country_flow_agree()
        DomAssert(drivers).assert_att('请求成功')
        user.quit_shipping_country_flow_onework()
        user.assert_shipping_country_flow_my_todo_node(api_response[0], '项目经理审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("项目经理审批审核成功")  # 用例名称
    @allure.description("出货国家：项目经理审批,点击同意，提示请求成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_005(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.shipping_country_flow_product_department_administrator_review(api_response[0])
        user.shipping_country_flow_product_department_sign(api_response[0])
        user.shipping_country_flow_product_manager_modification(api_response[0])
        user.shipping_country_flow_product_department_administrator_re_review(api_response[0])
        user.enter_shipping_country_flow_onework_edit(api_response[0])
        user.click_onework_shipping_country_flow_agree()
        DomAssert(drivers).assert_att('请求成功')
        user.quit_shipping_country_flow_onework()

    @allure.story("流程审批")  # 场景名称
    @allure.title("项目经理审批审核成功后，流程结束，状态变为审批通过")  # 用例名称
    @allure.description("出货国家:抄送（自动抄送，不需要操作）,出货国家-出货国家流程，查看单据状态已变为审批通过")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_006(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.shipping_country_flow_product_department_administrator_review(api_response[0])
        user.shipping_country_flow_product_department_sign(api_response[0])
        user.shipping_country_flow_product_manager_modification(api_response[0])
        user.shipping_country_flow_product_department_administrator_re_review(api_response[0])
        user.enter_shipping_country_flow_onework_edit(api_response[0])
        user.click_onework_shipping_country_flow_agree()
        DomAssert(drivers).assert_att('请求成功')
        user.quit_shipping_country_flow_onework()
        user.assert_shipping_country_flow_my_application_node(api_response[0], '抄送', True)
        sleep(60)
        user.assert_shipping_country_flow_my_application_flow(api_response[0], '审批完成')
        document_status = user.get_shipping_country_flow_info(api_response[0])[6]
        ValueAssert(drivers).value_assert_equal('审批通过', document_status)

if __name__ == '__main__':
    pytest.main(['ShippingCountry_ShippingCountryFlow.py'])
