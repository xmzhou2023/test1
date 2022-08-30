import pytest
from public.base.assert_ui import *
from project.TBM.page_object.KeyComponent_KeyComponentFlow import KeyComponentsFlow


@allure.feature("Test_模块中文名称")  # 模块名称
class TestCreateProcess:
    @allure.story("测试场景1")  # 场景名称
    @allure.title("用例名称1")  # 用例名称
    @allure.description("测试用例描述1")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.add_item_info()
        user.add_business_review()
        user.click_submit()
        user.assert_toast()
        process_code = user.get_info()[1]
        user.delete_flow(process_code)


@allure.feature("Test_模块中文名称")  # 模块名称
class TestTheProcessOfExaminationAndApproval:
    @allure.story("测试场景2")  # 场景名称
    @allure.title("用例名称1")  # 用例名称
    @allure.description("测试用例描述2")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_001(self, drivers):
        pass


    @allure.story("测试场景2")  # 场景名称
    @allure.title("用例名称2")  # 用例名称
    @allure.description("测试用例描述3")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_002(self, drivers):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage()
        user.click_onework_unfold('摄像头+闪光灯')
        user.click_onework_module('CTP')
        user.click_onework_code_add()
        user.click_onework_material_add('CTP(1供)')
        user.click_onework_material_pending_code('CTP(1供)')
        user.input_onework_material_details('物料属性', '属性test')
        user.scroll_onework_material_param()
        user.input_onework_material_parameter('技术类型', 'GFF', False)
        user.input_onework_material_parameter('CG颜色', 'CG颜色test')
        user.input_onework_material_parameter('接口类型', '接口类型test')
        user.input_onework_material_parameter('连接方式', '焊接', False)
        user.click_onework_agree()
        user.assert_toast()
        user.quit_oneworks()


if __name__ == '__main__':
    pytest.main(['Test_module.py'])
