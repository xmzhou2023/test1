import allure
import pytest
from project.POP.page_object.Good_List import *
from project.POP.page_object.Center_Component import NavPage
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP商品-商品列表”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("商品","商品列表")

@allure.feature("商品") # 模块名称
class TestGoodSearch:
    @allure.story("商品列表") # 场景名称
    @allure.title("搜索对应类目下商品")  # 用例名称
    @allure.description("输入类目名，列表搜索出对应类目下商品")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = GoodSearch(drivers)
        users.input_goodcategory("qwz")
        sleep(0.5)
        # 断言--列表展示对应类目下商品
        test = users.element_text(user['列表展示商品类目'])
        ValueAssert.value_assert_equal(test,"qwz")

@allure.feature("商品") # 模块名称
class TestExportList:
    @allure.story("商品列表")  # 场景名称
    @allure.title("导出商品列表")  # 用例名称
    @allure.description("点击导出，商品列表导出成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = ExportList(drivers)
        users.click_export()
        sleep(0.5)
        # 断言-导出成功提示
        test = users.element_text(user['导出成功提示'])
        ValueAssert.value_assert_equal(test, "创建导出任务成功！")

@allure.feature("商品")
class TestQuery:
    @allure.story("商品列表")
    @allure.title("查询商品")
    @allure.description("输入商品名称，点击查询对应商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_001(self,drivers):
        users = QueryGood(drivers)
        users.input_goodname("Huaweiphone")
        users.click_query()

        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['查询商品名称'])
        ValueAssert.value_assert_equal(test,"TECNO Huaweiphone 18g")


if __name__ == '__main__':
    pytest.main(['Good_List.py::TestQuery'])
