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


@allure.feature("商品-定义建议价格")  # 模块名称
class TestAdd_DefineSuggestedPrice:
    @allure.story("定义建议价格")  # 场景名称
    @allure.title("点击新增")  # 用例名称
    @allure.description("输入商品建议价格")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = AddDefineSuggestedPrice(drivers)
        users.click_button("新增")
        users.click_productname("PA00005438")
        users.click_addbutton("1000", "INDIA")
        sleep(2)
        # 断言
        users.sql_priceassert(1, "5623", "7255")

    @allure.story("定义建议价格")  # 场景名称
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
        sql = f'delete FROM `pop_data_db`.`goods_price` WHERE `goods_id` = 5623 AND `area_id`=7255 AND `enabled_flag`=1;'
        SQL("POP", "test").delete_db(sql)

@allure.feature("商品-定义建议价格")  # 模块名称
class TestQuery:
    @allure.story("定义建议价格")
    @allure.title("查询定义建议价格")
    @allure.description("输入日期段，点击查询对应日期段定义建议价格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_002_001(self,drivers):
        users = QueryGoodSugPrice(drivers)
        users.querygoodprice("定义建议价格-开始日期框","2022-11-11","定义建议价格-结束日期框","2022-11-11")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['日期断言'])
        ValueAssert.value_assert_equal(test[0:10],"2022-11-11")

    @allure.story("定义建议价格")
    @allure.title("查询定义建议价格")
    @allure.description("输入商品名称，点击查询对应商品定义建议价格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_002_002(self,drivers):
        users = QueryGoodSugPrice(drivers)
        users.querygoodprice("定义建议价格-商品名称框","TECNO POP 3 16+1 CHAMPAGNE GOLD")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['商品名称断言'])
        ValueAssert.value_assert_equal(test,"TECNO POP 3 16+1 CHAMPAGNE GOLD")

    @allure.story("定义建议价格")
    @allure.title("查询定义建议价格")
    @allure.description("输入品牌名称，点击查询对应品牌定义建议价格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_002_003(self, drivers):
        users = QueryGoodSugPrice(drivers)
        users.querygoodprice("定义建议价格-品牌名称框","Infinix")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['品牌名称断言'])
        ValueAssert.value_assert_equal(test,"Infinix")

    @allure.story("定义建议价格")
    @allure.title("查询定义建议价格")
    @allure.description("输入产品名称，点击查询对应产品名称定义建议价格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_002_004(self,drivers):
        users = QueryGoodSugPrice(drivers)
        users.querygoodprice("定义建议价格-产品名称框","F3")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['产品名称断言'])
        ValueAssert.value_assert_equal(test,"F3")

    @allure.story("定义建议价格")
    @allure.title("查询定义建议价格")
    @allure.description("输入区域，点击查询对应区域商品定义建议价格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_002_005(self,drivers):
        users = QueryGoodSugPrice(drivers)
        users.querygoodprice("定义建议价格-区域框","万州")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['区域断言'])
        ValueAssert.value_assert_equal(test,"万州")

    @allure.story("定义建议价格")
    @allure.title("查询定义建议价格")
    @allure.description("输入自采标记状态，点击查询对应状态定义建议价格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_002_006(self, drivers):
        users = QueryGoodSugPrice(drivers)
        users.querygoodprice("定义建议价格-自采标记框","是")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['自采标记断言'])
        ValueAssert.value_assert_equal(test,"是")

    @allure.story("定义建议价格")
    @allure.title("查询定义建议价格")
    @allure.description("输入创建人，点击查询对应创建人的定义建议价格数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_002_007(self, drivers):
        users = QueryGoodSugPrice(drivers)
        users.querygoodprice("定义建议价格-创建人框","张文强")
        sleep(2)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['创建人断言'])
        ValueAssert.value_assert_equal(test,"张文强[18651297]")

@allure.feature("商品-定义建议价格")  # 模块名称
class TestExportPrice:
    @allure.story("定义建议价格")  # 场景名称
    @allure.title("根据品牌名称查询后导出")  # 用例名称
    @allure.description("导出")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_001(self,drivers):
        users = ExportPrice(drivers)
        users.click_brandname("TECNO")
        users.click_search("查询")
        sleep(2)
        users.click_export("导出")
        test = users.element_text(user['导出提示'])
        ValueAssert.value_assert_equal(test, '创建导出任务成功！')


if __name__ == '__main__':
    pytest.main(['Add_DefineSuggestedPrice.py::TestAdd_DefineSuggestedPrice::test_001_001'])
