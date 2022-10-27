import allure
import pytest

from public.base.assert_ui import *
from project.MIP.page_object.Center_Component import NavPage
from project.MIP.page_object.MainDataCategory import MainDataCategory


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 主数据-类目管理 页面")
    menu = NavPage(drivers)
    menu.click_gotonav("主数据","类目管理")
    dom = DomAssert(drivers)
    dom.assert_url("/main-data/category")
    yield
    logging.info("后置条件:返回 首页 页面")
    menu.back_homepage("主数据")
    dom.assert_url("/dashboard")


@allure.feature("主数据-类目管理")
class TestQueryCategory:
    @allure.story("查询功能验证")
    @allure.title("输入一级类目名称-易耗品，查询结果正确")
    @allure.description("输入类目名称，查询结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        category = MainDataCategory(drivers)
        listValue = category.input_categoryName("易耗品")
        sqlResult = category.get_sqlResult("select category_name from bb_category where category_name = '易耗品'")
        ValueAssert.value_assert_equal(sqlResult,listValue)  # 断言
        category.button_reset()

    @allure.story("查询功能验证")
    @allure.title("输入二级类目名称，查询结果正确")
    @allure.description("输入二级类目名称-手机配件，查询结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        category = MainDataCategory(drivers)
        listValue = category.input_categoryName("手机配件")
        sqlResult = category.get_sqlResult("select category_name from bb_category where category_name = '手机配件'")
        ValueAssert.value_assert_equal(sqlResult,listValue)
        category.button_reset()


@allure.feature("主数据-类目管理")
class TestAddCategory:
    @allure.story("新增功能验证")
    @allure.title("新增一级类目，新增成功")
    @allure.description("新增一级类目，新增成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        category = MainDataCategory(drivers)
        category.button_add()
        category.maintain_category('','测试01','test01','正例')
        listValue = category.input_categoryName("测试01")
        sqlResult = category.get_sqlResult("select category_name from bb_category where category_name = '测试01'")
        ValueAssert.value_assert_equal(sqlResult,listValue)
        category.button_reset()
        category.clear_testData("测试01")

    @allure.story("新增功能验证")
    @allure.title("新增二级类目，新增成功")
    @allure.description("新增二级类目，新增成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_002(self, drivers):
        category = MainDataCategory(drivers)
        category.button_add()
        category.maintain_category('牛','测试01','test01','正例')
        listValue = category.input_categoryName("测试01")
        sqlResult = category.get_sqlResult("select category_name from bb_category where category_name = '测试01'")
        ValueAssert.value_assert_equal(sqlResult,listValue)
        category.button_reset()
        category.clear_testData("测试01")

    @allure.story("新增功能验证")
    @allure.title("[异常]必填项未维护，新增失败")
    @allure.description("必填项未维护，新增失败")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("superiorCategory,name_zh,name_en",[("","",""),("","测试01",""),("","","test01"),("牛","测试01",""),("牛","","test01")])
    @pytest.mark.smoke
    def test_002_003(self, drivers,superiorCategory,name_zh,name_en):
        category = MainDataCategory(drivers)
        category.button_add()
        category.maintain_category(superiorCategory,name_zh,name_en,'反例 必填验证')

    @allure.story("新增功能验证")
    @allure.title("[异常]重复新增，新增保存失败")
    @allure.description("重复新增，新增保存失败")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("superiorCategory,name_zh,name_en",[("","电子产品","No.1"),("","电子产品","electronics"),("","测试01","No.1"),
                                                                 ("精美礼品","小香灯","light"),("精美礼品","小香灯","test01"),("精美礼品","测试01","light"),
                                                                 ("精美礼品","无线耳机","test01"),("精美礼品","测试01","wireless earphone")])
    @pytest.mark.smoke
    def test_002_004(self, drivers,superiorCategory,name_zh,name_en):
        category = MainDataCategory(drivers)
        category.button_add()
        category.maintain_category(superiorCategory,name_zh,name_en,'反例 重复新增')


@allure.feature("主数据-类目管理")
class TestEditCategory:
    @allure.story("编辑功能验证")
    @allure.title("编辑一级类目，编辑保存成功")
    @allure.description("编辑一级类目，编辑保存成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        category = MainDataCategory(drivers)
        category.creat_testData(drivers,"",'测试01','test01')
        category.input_categoryName("测试01")
        category.button_edit("测试01")
        category.edit_categoryInf("测试02","test02")
        listValue = category.input_categoryName("测试02")
        sqlResult = category.get_sqlResult("select category_name from bb_category where category_name = '测试02'")
        ValueAssert.value_assert_equal(sqlResult,listValue)
        category.button_reset()
        category.clear_testData("测试02")

    @allure.story("编辑功能验证")
    @allure.title("编辑二级类目，编辑保存成功")
    @allure.description("编辑二级类目，编辑保存成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        category = MainDataCategory(drivers)
        category.creat_testData(drivers,"牛",'测试01','test01')
        category.input_categoryName("测试01")
        category.button_edit("测试01")
        category.edit_categoryInf("测试02","test02")
        listValue = category.input_categoryName("测试02")
        sqlResult = category.get_sqlResult("select category_name from bb_category where category_name = '测试02'")
        ValueAssert.value_assert_equal(sqlResult,listValue)
        category.button_reset()
        category.clear_testData("测试02")

    @allure.story("编辑功能验证")
    @allure.title("[异常]编辑类目信息，清空必填项，编辑保存失败")
    @allure.description("编辑类目信息，清空必填项，编辑保存失败")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("name_zh,name_en",[(None,"test02"),("测试02",None),(None,None)])
    @pytest.mark.smoke
    def test_003_003(self, drivers,name_zh,name_en):
        category = MainDataCategory(drivers)
        category.creat_testData(drivers,"",'测试01','test01')
        category.input_categoryName("测试01")
        category.button_edit("测试01")
        category.edit_categoryInf(name_zh,name_en,type="反例 必填校验")
        category.clear_testData("测试01")

    @allure.story("编辑功能验证")
    @allure.title("[异常]编辑类目信息，与原类目信息重复，编辑保存失败")
    @allure.description("编辑类目信息，与原类目信息重复，编辑保存失败")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("name_zh,name_en",[("测试01","test01"),("赠品","food"),("牛","No.3-1"),("传音手机","Phone")])
    @pytest.mark.smoke
    def test_003_004(self, drivers,name_zh,name_en):
        category = MainDataCategory(drivers)
        category.creat_testData(drivers,"",'测试01','test01')
        category.input_categoryName("测试01")
        category.button_edit("测试01")
        category.edit_categoryInf(name_zh,name_en,type="反例 重复")
        category.clear_testData("测试01")


@allure.feature("主数据-类目管理")
class TestChangeStatus:
    @allure.story("启用/禁用 功能验证")
    @allure.title("启用状态的类目，点击失效按钮，禁用成功")
    @allure.description("启用状态的类目，点击失效按钮，禁用成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_001(self, drivers):
        category = MainDataCategory(drivers)
        category.creat_testData(drivers,"",'测试01','test01')
        category.input_categoryName("测试01")
        category.button_status("测试01")
        status = category.return_status("测试01")
        ValueAssert.value_assert_equal(status,"失效")
        category.clear_testData("测试01")

    @allure.story("启用/禁用 功能验证")
    @allure.title("禁用状态的类目，点击启用按钮，启用成功")
    @allure.description("禁用状态的类目，点击启用按钮，启用成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_002(self, drivers):
        category = MainDataCategory(drivers)
        category.creat_testData(drivers,"",'测试01','test01')
        category.input_categoryName("测试01")
        category.button_status("测试01")
        """前置条件 造出状态为失效的测试数据"""
        category.button_status("测试01")
        status = category.return_status("测试01")
        ValueAssert.value_assert_equal(status,"启用")
        category.clear_testData("测试01")


if __name__ == '__main__':
    pytest.main(['project/MIP/testcase/MainDataCategory.py'])