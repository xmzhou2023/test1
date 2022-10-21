import allure
import pytest
from project.POP.page_object.Good_List import GoodSearch
from project.POP.page_object.Center_Component import NavPage
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP商品-商品列表”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("商品","商品列表")

@allure.feature("商品") # 模块名称
class TestGoodSearch:
    @allure.story("商品列表") # 场景名称
    @allure.title("搜索对应类目下商品")  # 用例名称
    @allure.description("输入类目名，列表搜索出对应类目下商品")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = GoodSearch(drivers)
        users.input_goodcategory("qwz")
        sleep(0.5)
        # 断言--列表展示对应类目下商品
        test = users.element_text(user['列表展示商品类目'])
        ValueAssert.value_assert_equal(test,"qwz")


if __name__ == '__main__':
    pytest.main(['Good_List.py'])
