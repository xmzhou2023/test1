import allure,logging
import pytest,random
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Sales_SalesOrder import *
from public.base.assert_ui import *

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP销售-销售订单”页面")
    user = NavPage(drivers)
    user.click_gotonav("销售","销售订单")

@allure.feature("销售") # 模块名称
class TestSaleBilling:
    @allure.story("销售订单") # 场景名称
    @allure.title("商品销售开单")  # 用例名称
    @allure.description("销售开单输入开单需要的数据，点击收款完成开单")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = SalesBilling(drivers)
        user.click_billing()
        user.switch_shop('Supper Big Shop','PPK00100')
        user.switch_promoter('Wenqiang Zhang','PEEC000010')
        user.input_phone('15001600123')
        user.input_goodscode('11234')
        user.input_price('8888.88')
        user.input_money('666.66','777.77','888.88')
        user.input_remarks('有钱任性','这是一个大款')
        user.click_Collection()
        sleep(0.5)
        # 断言--开单成功跳转销售订单列表断言页面是否存在销售订单编号字段
        DomAssert(drivers).assert_exact_att('销售订单编号')

if __name__ == '__main__':
    pytest.main(['Sales_SalesOrder.py'])
