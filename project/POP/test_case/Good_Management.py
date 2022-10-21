import allure,logging
import pytest,random
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Good_Management import AddGood
from public.base.assert_ui import *

@pytest.fixture(scope='class', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP商品-商品管理”页面")
    user = NavPage(drivers)
    user.click_gotonav("商品","商品管理")

@allure.feature("商品") # 模块名称
class TestAddGood:
    @allure.story("商品管理") # 场景名称
    @allure.title("商品新增")  # 用例名称
    @allure.description("输入必填项新增商品成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AddGood(drivers)
        user.click_add()
        content = "zwq新增测试商品" + str(random.randint(1,1000))
        user.input_productname(content)
        user.switch_category('qwz')
        user.switch_region('China')
        user.switch_brand('TECNO')
        user.switch_imei('否')
        user.add_goodinfo()
        user.click_preserve()
        # 断言--新增后页面返回商品管理页面判定页面是否存在商品管理字段
        DomAssert(drivers).assert_exact_att('商品管理')


if __name__ == '__main__':
    pytest.main(['Good_Management.py'])
