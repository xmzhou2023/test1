# -*- coding: utf-8 -*-
import allure,random,time
import pytest,logging
from project.POP.page_object.Center_Component import *
from project.POP.page_object.Organization_EmployeeManagement import *
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP组织-职员管理”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("组织","职员管理")

@allure.feature("组织-职员管理") # 模块名称
class Testqueryuser:
    @allure.story("职员管理") # 场景名称
    @allure.title("职员管理查询")  # 用例名称
    @allure.description("输入用户查询职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):
        users = QueryUser(drivers)
        users.queryuser("用户框","张文强")
        sleep(5)
        # 断言
        test = users.element_text(user['员工姓名断言'])
        ValueAssert.value_assert_equal(test,"张文强")

    @allure.story("职员管理")  # 场景名称
    @allure.title("职员管理查询")  # 用例名称
    @allure.description("输入角色查询对应角色职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        users = QueryUser(drivers)
        users.queryuser("角色框", "保安")
        sleep(5)
        # 断言
        test = users.element_text(user['角色断言'])
        ValueAssert.value_assert_equal(test, "保安")

    @allure.story("职员管理")  # 场景名称
    @allure.title("职员管理查询")  # 用例名称
    @allure.description("输入状态查询对应状态职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):
        users = QueryUser(drivers)
        users.queryuser("状态框", "禁用")
        sleep(5)
        # 断言
        test = users.element_text(user['状态断言'])
        ValueAssert.value_assert_equal(test, "禁用")

    @allure.story("职员管理")  # 场景名称
    @allure.title("职员管理查询")  # 用例名称
    @allure.description("输入门店查询对应门店的职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):
        users = QueryUser(drivers)
        users.queryuser("门店框","星期五的门店")
        sleep(5)
        # 断言
        test = users.element_text(user['门店断言'])
        ValueAssert.value_assert_equal(test, "星期五的门店")

    @allure.story("职员管理")  # 场景名称
    @allure.title("职员管理查询")  # 用例名称
    @allure.description("输入员工类型查询对应类型的职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):
        users = QueryUser(drivers)
        users.queryuser("员工类型框", "传音员工")
        sleep(5)
        # 断言
        test = users.element_text(user['员工类型断言'])
        ValueAssert.value_assert_equal(test, "传音员工")

    @allure.story("职员管理")  # 场景名称
    @allure.title("职员管理查询")  # 用例名称
    @allure.description("输入国家查询对应国家的职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):
        users = QueryUser(drivers)
        users.queryuser("国家框", "Uganda")
        sleep(5)
        # 断言
        test = users.element_text(user['国家断言'])
        ValueAssert.value_assert_equal(test,"Uganda")

    @allure.story("职员管理")  # 场景名称
    @allure.title("职员管理查询")  # 用例名称
    @allure.description("输入区域查询对应区域的职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_007(self, drivers):
        users = QueryUser(drivers)
        users.queryuser("区域框", "大理")
        sleep(5)
        # 断言
        test = users.element_text(user['区域断言'])
        ValueAssert.value_assert_equal(test, "大理")


@allure.feature("组织-职员管理") # 模块名称
class TestAddUser:
    @allure.story("职员管理") # 场景名称
    @allure.title("职员新增")  # 用例名称
    @allure.description("输入必填项新增职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_002_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = AddUser(drivers)
        users.click_add_button()
        content = 'zwq测试账号' + str(int(time.time()))
        users.input_username(content)
        users.switch_division('TECNO事业部')
        users.switch_region('China')
        users.switch_role('test1')
        users.switch_country('Malta')  # 国家与区域建议不能一样
        users.switch_superior('18651297')
        users.switch_shop('PCN00192')
        # users.click_preservation_button()  # 这里输入期望结果：新增时输入的员工姓名，断言期望结果与列表显示的最新的员工姓名是否一致
        # sleep(0.5)
        # # 断言
        # test = users.element_text(user['列表页新增用户名字段'])
        # ValueAssert.value_assert_equal(test,content)
        # sleep(3)


        # for i in range(19,21):
        #     users.click_add_button()
        #     content = 'xhr考勤测试账号' + str(i)
        #     role = "xhr_test" + str(i)
        #     users.input_username(content)
        #     users.switch_division('oraimo')
        #     users.switch_region('China')
        #     users.switch_role(role)
        #     users.switch_country('China')  # 国家与区域建议不能一样
        #     users.switch_superior('18651297')
        #     users.switch_shop('PCN00192')
        #     users.click_preservation_button()  # 这里输入期望结果：新增时输入的员工姓名，断言期望结果与列表显示的最新的员工姓名是否一致
        #     sleep(0.5)
            # # 断言
            # # test = users.element_text(user['列表页新增用户名字段'])
            # # ValueAssert.value_assert_equal(test,content)
            # sleep(3)

    @allure.story("职员管理")  # 场景名称
    @allure.title("职员姓名不输入新增")  # 用例名称
    @allure.description("职员姓名不输入，其余必填项合法输入，点击提交，页面友好提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self,drivers):
        users = AddUser(drivers)
        users.click_add_button()
        users.switch_division('TECNO事业部')
        users.switch_region('重庆')
        users.switch_role('保安')
        users.switch_country('China')  # 国家与区域建议不能一样
        users.click_preservation_button()
        # 断言
        test = users.element_text(user['必填项不填提示'])
        # 设置预期的结果
        expect = "此项为必填项"
        ValueAssert.value_assert_equal(test,expect)
        sleep(5)

@allure.feature("组织-职员管理") # 模块名称
class TestExportEmployee:
    @allure.story("职员管理")  # 场景名称
    @allure.title("导出职员管理列表")  # 用例名称
    @allure.description("点击导出，导出职员管理列表")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = ExportEmployee(drivers)
        users.click_export()
        sleep(0.5)
        # 断言--提示：XXXX导出成功
        test = users.element_text(user['导出成功提示'])
        ValueAssert.value_assert_equal(test,'创建导出任务成功！')

if __name__ == '__main__':
    pytest.main(['Organization_EmployeeManagement.py::TestAddUser::test_002_002'])
