import logging

import allure
import pytest
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Add_DefineSuggestedPrice import *


@pytest.fixture(scope='function', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“商品-定义建议价格”页面")
    user = NavPage(drivers)
    user.click_gotonav("商品", "定义建议价格")


@allure.feature("定义建议价格")  # 模块名称
class TestAdd_DefineSuggestedPrice:
    @allure.story("新增商品建议价格")  # 场景名称
    @allure.title("点击新增")  # 用例名称
    @allure.description("输入商品建议价格")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = AddDefineSuggestedPrice(drivers)
        users.click_button("新增")
        users.click_productname("PA00005438")
        users.click_addbutton("1000", "INDIA")
        sleep(0.5)
        # 断言
        users.sql_priceassert(1, "5623", "7255")

    @allure.story("编辑商品建议价格")  # 场景名称
    @allure.title("查询商品名称，点击编辑，修改价格后保存")  # 用例名称
    @allure.description("输入商品建议价格")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        users = AddDefineSuggestedPrice(drivers)
        users.click_commodityname("TECNO POP 3 16+1 CHAMPAGNE GOLD")
        users.click_search("查询")
        users.click_tickbox()
        users.click_button("编辑")
        users.click_edit_price("500")

        # 数据清理--数据库删除商品价格
        # sql = f'delete FROM `goods_price` WHERE `goods_id` = 5623 AND `area_id`=7255 AND `enabled_flag`=1;'
        # SQL("POP", "test").delete_db(sql)


if __name__ == '__main__':
    # pytest.main(['Add_DefineSuggestedPrice.py::TestAdd_DefineSuggestedPrice::test_001_002'])
    pytest.main(['Add_DefineSuggestedPrice.py'])
