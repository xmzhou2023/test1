import allure
import pytest
from project.POP.page_object.Query_user import Queryuser
from public.base.assert_ui import *
from project.POP.page_object.Center_Component import NavPage

@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“POP组织-职员管理”页面")
    user = NavPage(drivers)
    user.click_gotonav("组织","职员管理")

@allure.feature("组织") # 模块名称
class Testqueryuser:
    @allure.story("职员管理") # 场景名称
    @allure.title("职员管理查询")  # 用例名称
    @allure.description("输入用户查询职员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = Queryuser(drivers)
        user.input_username("张文强","张文强 18651297")
        user.click_query("张文强")   # 期望值用户姓名与输入查询的用户姓名一致
if __name__ == '__main__':
    pytest.main(['Query_user.py'])
