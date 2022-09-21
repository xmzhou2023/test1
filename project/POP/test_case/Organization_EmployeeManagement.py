# -*- coding: utf-8 -*-
import allure,random
import pytest,logging
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Organization_EmployeeManagement import *

from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“POP组织-职员管理”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("组织","职员管理")

@allure.feature("组织") # 模块名称
class Testqueryuser:
    @allure.story("职员管理") # 场景名称
    @allure.title("职员管理查询")  # 用例名称
    @allure.description("输入用户查询职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = Queryuser(drivers)
        users.input_username("张文强","张文强 18651297")
        users.click_query()   # 期望值用户姓名与输入查询的用户姓名一致
        # 断言
        test = users.element_text(user['员工姓名'])
        ValueAssert.value_assert_equal(test,"张文强")



@allure.feature("组织") # 模块名称
class TestAddUser:
    @allure.story("职员管理") # 场景名称
    @allure.title("职员新增")  # 用例名称
    @allure.description("输入必填项新增职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = AddUser(drivers)
        users.click_add_button()
        content = 'zwq测试账号' + str(random.randint(1,100))
        users.input_username(content)
        users.switch_division('TECNO事业部')
        users.switch_region('China')
        users.switch_role('test1')
        users.switch_country('Malta')  # 国家与区域建议不能一样
        users.click_preservation_button()  # 这里输入期望结果：新增时输入的员工姓名，断言期望结果与列表显示的最新的员工姓名是否一致
        # 断言
        test = users.element_text(user['列表页新增用户名字段'])
        ValueAssert.value_assert_equal(test,content)
        sleep(5)

    @allure.story("职员管理")  # 场景名称
    @allure.title("职员姓名不输入新增")  # 用例名称
    @allure.description("职员姓名不输入，其余必填项合法输入，点击提交，页面友好提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self,drivers):
        users = AddUser(drivers)
        users.click_add_button()
        users.switch_division('TECNO事业部')
        users.switch_region('China')
        users.switch_role('test1')
        users.switch_country('Malta')  # 国家与区域建议不能一样
        users.click_preservation_button()
        # 断言
        test = users.element_text(user['必填项不填提示'])
        # 设置预期的结果
        expect = "此项为必填项"
        ValueAssert.value_assert_equal(test,expect)
        sleep(5)
if __name__ == '__main__':
    pytest.main(['Organization_EmployeeManagement.py'])
