import allure,logging
import pytest,random
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Add_Warehouse import AddWarehouse

@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“POP库存-仓库信息”页面")
    user = NavPage(drivers)
    user.click_gotonav("库存","仓库信息")


@allure.feature("库存") # 模块名称
class TestAddWarehouse:
    @allure.story("仓库信息") # 场景名称
    @allure.title("仓库新增")  # 用例名称
    @allure.description("输入必填项新增仓库成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self,drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AddWarehouse(drivers)
        user.click_add()
        content = "zwq测试新增仓库" + str(random.randint(1,1000))
        user.input_warehouse_name(content)
        user.switch_shop('不差钱的门店','PCN00149')
        user.switch_warehouse_type()
        user.click_submit()
        user.assert_warehouse_name(content)


if __name__ == '__main__':
    pytest.main(['Add_Warehouse.py'])
