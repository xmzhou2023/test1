import time

import allure
import pytest
from project.POP.page_object.Center_Component import SpecialNavPage
from project.POP.page_object.inventory_WarehouseInformation import WarehouseInformation
from project.POP.test_case.conftest import *
from libs.common.read_element import Element


object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


@pytest.fixture(scope='function', autouse=True)
def setup_module(drivers):
    logging.info("前置条件：进入’库存-仓库信息‘页面")
    nav = SpecialNavPage(drivers)
    nav.click_gotonav("库存", "仓库信息")


@allure.feature("库存-仓库信息")  # 模块名称
class TestAddWarehouse:
    @allure.story("新增分仓")  # 场景名称
    @allure.title("门店新增分仓")  # 用例名称
    @allure.description("给门店新增多个分仓")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = WarehouseInformation(drivers)
        users.warehouse_add('新增')
        num = str(int(time.time()))
        users.warehouse_warehousename('中国' + num)
        sleep()
        users.warehouse_shopname('南京')
        users.warehouse_select()
        users.click_submit('提交')
        sleep(3)
        test = users.element_text(user['新增成功提示'])
        ValueAssert.value_assert_equal(test, '新增成功')

if __name__ == '__main__':
    pytest.main(['inventory_WarehouseInformation.py'])
