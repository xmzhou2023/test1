import allure,random
import pytest,logging
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Add_User import AddUser

@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“POP组织-职员管理”页面")
    user = NavPage(drivers)
    user.click_gotonav("组织","职员管理")

@allure.feature("组织") # 模块名称
class TestAddUser:
    @allure.story("职员管理") # 场景名称
    @allure.title("职员新增")  # 用例名称
    @allure.description("输入必填项新增职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AddUser(drivers)
        user.click_add_button()
        content = 'zwq自动化新增测试账号' + str(random.randint(1,100))
        user.input_username(content)
        user.switch_division('TECNO事业部')
        user.switch_region('China')
        user.switch_role('test1')
        user.switch_country('Nigeria')  # 国家与区域建议不能一样
        user.click_preservation_button(content)  # 这里输入期望结果：新增时输入的员工姓名，断言期望结果与列表显示的最新的员工姓名是否一致


if __name__ == '__main__':
    pytest.main(['Add_User.py'])
