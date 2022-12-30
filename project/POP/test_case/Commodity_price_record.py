import allure
import pytest
from project.POP.page_object.Commodity_price_record import *

@pytest.fixture(scope='function', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“商品-商品价格记录”页面")
    user = NavPage(drivers)
    user.click_gotonav("商品", "商品价格记录")

@allure.feature("商品价格记录") # 模块名称
class TestQueryCommodityPrice:
    @allure.story("商品价格记录") # 场景名称
    @allure.title("查询商品价格记录")  # 用例名称
    @allure.description("输入商品名称，点击查询对应定义价格记录数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = QueryCommodityPrice(drivers)
        users.querycommodityprice("商品价格记录-商品名称框","PA00005434")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['商品名称断言'])
        ValueAssert.value_assert_equal(test,"itel A22 8+1 CHAMPAGNE GOLD")

if __name__ == '__main__':
    pytest.main(['Commodity_price_record.py::TestQueryCommodityPrice'])
