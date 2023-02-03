import allure, os
import pytest, logging, random, time
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Inventory_InventoryQuery import Inventory_Query
from libs.common.read_element import Element
from project.POP.test_case.conftest import *


object_name = os.path.basename(__file__).split('.')[0]  # 获取当前的文件是xxx.py文件，以.分割返回为[”xxx”,"py"]取第一个字符即文件名
user = Element(pro_name, object_name)




@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP库存-库存查询”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("库存","仓库查询")


@allure.feature("库存-库存查询")  # 模块名称
class TestInventoryQuery:
    @allure.story("库存查询")  # 场景名称
    @allure.title("门店库存查询")  # 用例名称
    @allure.description("点击查询按钮，正常查看门店列表库存信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self,drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = Inventory_Query(drivers)
        users.click_shop('西藏')
        users.click_query('西藏')
        sleep(0.5)
        # 断言
        test = users.element_text(user['门店名称'])
        ValueAssert.value_assert_equal(test, '西藏')


if __name__ == '__main__':
    pytest.main(['Inventory_InventoryQuery.py'])