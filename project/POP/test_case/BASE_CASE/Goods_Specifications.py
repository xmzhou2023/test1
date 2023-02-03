import allure,logging
import pytest,random,time
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Goods_Specifications import QueryGoodSpecifications
from public.base.assert_ui import *
from project.POP.test_case.conftest import *
from libs.common.read_element import Element
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP商品-商品规格”页面")
    user = NavPage(drivers)
    user.click_gotonav("商品","商品规格")

@allure.feature("商品-商品规格")
class TestQuery:
    @allure.story("商品规格")
    @allure.title("查询商品规格")
    @allure.description("输入日期段，点击查询对应日期段商品规格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_001_001(self,drivers):
        users = QueryGoodSpecifications(drivers)
        users.querygood("商品规格-开始日期框","2022-11-07","商品规格-结束日期框","2022-11-07")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['日期断言'])
        ValueAssert.value_assert_equal(test[0:10],"2022-11-07")

    @allure.story("商品规格")
    @allure.title("查询商品规格")
    @allure.description("输入规格名称，点击查询对应规格名称的商品规格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        users = QueryGoodSpecifications(drivers)
        users.querygood("商品规格-规格名称框","测试规格")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['规格名称断言'])
        ValueAssert.value_assert_equal(test,"测试规格")

    @allure.story("商品规格")
    @allure.title("查询商品规格")
    @allure.description("输入规格状态，点击查询对应规格状态的商品规格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        users = QueryGoodSpecifications(drivers)
        users.querygood("商品规格-规格状态框","启用")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['规格状态断言'])
        ValueAssert.value_assert_equal(test,"启用")

    @allure.story("商品规格")
    @allure.title("查询商品规格")
    @allure.description("输入创建人，点击查询对应创建人的商品规格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_001_004(self, drivers):
        users = QueryGoodSpecifications(drivers)
        users.querygood("商品规格-创建人框","张文强")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['创建人断言'])
        ValueAssert.value_assert_equal(test,"张文强[18651297]")



if __name__ == '__main__':
    pytest.main(['Goods_Specifications.py::TestQuery'])
