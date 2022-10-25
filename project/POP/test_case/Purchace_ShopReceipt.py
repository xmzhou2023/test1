import allure
import pytest
import logging

from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Purchace_ShopReceipt import ShopReceipt
from project.POP.test_case.conftest import *
from libs.common.read_element import Element

object_name = os.path.basename(__file__).split('.')[0]
users = Element(pro_name, object_name)
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""
@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("前置条件：进入’采购-门店收货单‘页面")
    userss = NavPage(drivers)
    userss.click_gotonav("采购", "门店收货单")


@allure.feature("采购") # 模块名称
class TestUtil:
    @allure.story("门店收货单") # 场景名称
    @allure.title('ShopReceipt')  # 用例名称
    @allure.description("新增自采收货：添加单个或者多个商品进行收货") #用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_100_100(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ShopReceipt(drivers)
        user.receipt_click_menu_self_purchase('自采收货')
        user.receipt_select_shop('TECNO江北旗舰店')
        user.receipt_select_goods('礼品1123')
        user.receipt_search_goods('查询')
        user.receipt_add_goods()
        user.receipt_click_submit('提交')
        sleep()
        test = user.element_text(users['新增自采收货'])
        ValueAssert.value_assert_equal(test, '提交成功')

if __name__ == '__main__':
    pytest.main(['Purchace_ShopReceipt.py::TestUtil::test_100_100'])
