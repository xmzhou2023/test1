import allure
import pytest
from project.POP.page_object.Member_Memberinfomation import *
from project.POP.page_object.Center_Component import NavPage
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP会员-会员信息”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("会员","会员信息")

@allure.feature("会员") # 模块名称
class TestQueryMember:
    @allure.story("会员信息") # 场景名称
    @allure.title("查询会员")  # 用例名称
    @allure.description("输入单个手机号查询对应会员数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = QueryMember(drivers)
        users.input_phone('18323585901')
        users.click_query()
        sleep(0.5)
        # 断言--输入手机号点击查询后列表展示手机号与输入的手机号一致
        test = users.element_text(user['查询后手机号'])
        ValueAssert.value_assert_equal(test,'18323585901')


if __name__ == '__main__':
    pytest.main(['Member_Memberinfomation.py'])
