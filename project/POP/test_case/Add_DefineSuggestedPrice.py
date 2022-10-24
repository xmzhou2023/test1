import logging

import allure
import pytest
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Add_DefineSuggestedPrice import *
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
    logging.info("模块前置条件：前往“商品-定义建议价格”页面")
    user = NavPage(drivers)
    user.click_gotonav("商品","定义建议价格")


@allure.feature("定义建议价格") # 模块名称
class TestAdd_DefineSuggestedPrice:
    @allure.story("新增商品建议价格") # 场景名称
    @allure.title("点击新增")  # 用例名称
    @allure.description("输入商品建议价格")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = AddDefineSuggestedPrice(drivers)
        users.click_button("新增")
        users.click_productname("PA00005438")
        users.click_addbutton("1000","INDIA")
        users.sql_priceassert(1,"5623","7255")

    def test_001_002(self,drivers):
        users = AddDefineSuggestedPrice(drivers)
        users.click_commodityname("TECNO POP 3 16+1 CHAMPAGNE GOLD")
        users.click_search()
        users.click_tickbox()
        users.click_button("编辑")
        users.click_edit_price("500")



if __name__ == '__main__':
    pytest.main(['Add_DefineSuggestedPrice.py::TestAdd_DefineSuggestedPrice::test_001_003'])
    # pytest.main(['Add_DefineSuggestedPrice.py'])
