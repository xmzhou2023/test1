import allure,logging
import pytest,random
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Add_GoodParameter import AddGoodParam

@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“POP商品-商品参数”页面")
    user = NavPage(drivers)
    user.click_gotonav("商品","商品参数")

@allure.feature("商品") # 模块名称
class TestAddGoodParam:
    @allure.story("商品参数") # 场景名称
    @allure.title("商品参数新增")  # 用例名称
    @allure.description("输入必填项新增商品参数")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user= AddGoodParam(drivers)
        user.click_add()
        content = '测试新增参数' + str(random.randint(1, 100))
        user.input_paramname(content)
        user.switch_category()
        user.switch_display_form("单选框")
        user.switch_order("1")
        user.input_parameters("参数值1","参数值2","参数值3")
        user.click_submit()
        user.sql_assert(1,content)

if __name__ == '__main__':
    pytest.main(['Add_GoodParameter.py'])
