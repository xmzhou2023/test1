import allure
import pytest
import logging

from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Purchace_ShopReceipt import ShopReceipt,QueryReceipt
from project.POP.test_case.conftest import *
from libs.common.read_element import Element

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("前置条件：进入’采购-门店收货单‘页面")
    nav = NavPage(drivers)
    nav.click_gotonav("采购", "门店收货单")


@allure.feature("采购") # 模块名称
class TestPurchaseReceipt:
    @allure.story("门店收货单") # 场景名称
    @allure.title("ShopReceipt")  # 用例名称
    @allure.description("新增自采收货：添加单个或者多个商品进行收货") #用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = ShopReceipt(drivers)
        users.receipt_click_menu_self_purchase('自采收货')
        users.receipt_select_shop('TECNO江北旗舰店')
        users.receipt_select_goods('礼品1123')
        users.receipt_search_goods('查询')
        users.receipt_add_goods()
        users.receipt_click_submit('提交')
        sleep()
        test = users.element_text(user['新增自采收货'])
        ValueAssert.value_assert_equal(test, '提交成功')

@allure.feature("采购") # 模块名称
class TestQueryReceipt:
    @allure.story("门店收货单")  # 场景名称
    @allure.title("ShopReceipt")  # 用例名称
    @allure.description("新增自采收货：添加单个或者多个商品进行收货")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self,drivers):
        users = QueryReceipt(drivers)
        users.input_receiptnum("PI221026000001")
        users.click_query()

        # 断言-查询的收货单与输入的一致
        test = users.element_text(user['查询收货单号'])
        ValueAssert.value_assert_equal(test,"PI221026000001")






if __name__ == '__main__':
    pytest.main(['Purchace_ShopReceipt.py::TestQueryReceipt::test_002_001'])
