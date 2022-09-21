import allure
import pytest,logging
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Shop_ShopList import Query_shop
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
    logging.info("模块前置条件：前往“POP商品-商品参数”页面")
    user = NavPage(drivers)
    user.click_gotonav("门店","门店列表")


@allure.feature("门店") # 模块名称
class TestQuery_shop:
    @allure.story("门店列表") # 场景名称
    @allure.title("门店列表查看")  # 用例名称
    @allure.description("点击查询按钮，正常查看门店列表信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = Query_shop(drivers)
        user.click_organization('TECNO事业部')
        user.click_shop('仙桃')
        user.click_query('仙桃体专店')

if __name__ == '__main__':
    pytest.main(['Shop_ShopList.py'])
