import allure,logging
import pytest,random
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Stock_Warehouseinfomation import *
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='class', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP库存-仓库信息”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("库存","仓库信息")


@allure.feature("库存") # 模块名称
class TestAddWarehouse:
    @allure.story("仓库信息") # 场景名称
    @allure.title("仓库新增")  # 用例名称
    @allure.description("输入必填项新增仓库成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self,drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = AddWarehouse(drivers)
        users.click_add()
        content = "zwq测试新增仓库" + str(random.randint(1,1000))
        users.input_warehouse_name(content)
        users.switch_shop('不差钱的门店','PCN00149')
        users.switch_warehouse_type()
        users.click_submit()
        # 断言--新增仓库后页面跳转仓库列表断言最新展示仓库名称与新增一直
        test = users.element_text(user['新增仓库名称'])
        ValueAssert.value_assert_equal(test,content)


if __name__ == '__main__':
    pytest.main(['Stock_Warehouseinfomation.py'])
