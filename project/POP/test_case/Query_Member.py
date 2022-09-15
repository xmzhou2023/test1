import allure
import pytest
from project.POP.page_object.Query_Member import QueryMember
from public.base.assert_ui import *
from project.POP.page_object.Center_Component import NavPage

@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“POP会员-会员信息”页面")
    user = NavPage(drivers)
    user.click_gotonav("会员","会员信息")

@allure.feature("会员") # 模块名称
class TestQueryMember:
    @allure.story("会员信息") # 场景名称
    @allure.title("查询会员")  # 用例名称
    @allure.description("输入单个手机号查询对应会员数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = QueryMember(drivers)
        user.input_phone('18323585901')
        user.click_query()
        user.assert_phone('18323585901')


if __name__ == '__main__':
    pytest.main(['Query_Member.py'])
