import allure
import pytest
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Query_GoodDetail import Query_GoodDetail
from public.base.assert_ui import *

@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“POP商品-商品参数”页面")
    user = NavPage(drivers)
    user.click_gotonav("商品","商品参数")

@allure.feature("商品") # 模块名称
class TestQueryDetail:
    @allure.story("商品参数") # 场景名称
    @allure.title("商品参数详情查看")  # 用例名称
    @allure.description("点击商品参数列表详情，正常查看参数详情页")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self,drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = Query_GoodDetail(drivers)
        user.click_detail('参数详情')

if __name__ == '__main__':
    pytest.main(['Query_GoodDetail.py'])
