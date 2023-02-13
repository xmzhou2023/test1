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

@allure.feature("商品-商品列表") # 模块名称
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

@allure.feature("商品-商品列表") # 模块名称
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

@allure.feature("商品-商品列表")
class TestQuery:
    @allure.story("商品列表")
    @allure.title("查询商品")
    @allure.description("输入日期段，点击查询对应日期段商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_001(self,drivers):
        users = QueryGood(drivers)
        users.querygood("商品列表-开始日期框","2022-08-16","商品列表-结束日期框","2022-08-16")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['日期断言'])
        ValueAssert.value_assert_equal(test[0:10],"2022-08-16")

    @allure.story("商品列表")
    @allure.title("查询商品")
    @allure.description("输入商品名称，点击查询对应商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品列表-商品名称框","TECNO 自动化测试商品 345 1")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['商品名称断言'])
        ValueAssert.value_assert_equal(test,"TECNO 自动化测试商品 345 1")

    @allure.story("商品列表")
    @allure.title("查询商品")
    @allure.description("输入自采标记，点击查询对应自采标记的商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_003(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品列表-自采标记框","否", )
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['自采标记断言'])
        ValueAssert.value_assert_equal(test,"否")

    @allure.story("商品列表")
    @allure.title("查询商品")
    @allure.description("输入区域，点击查询对应区域的商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_004(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品列表-区域框","万州")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['区域断言'])
        ValueAssert.value_assert_equal(test,"共 1 条")

    @allure.story("商品列表")
    @allure.title("查询商品")
    @allure.description("输入区域，点击查询对应区域的商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_005(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品列表-品牌名称框","Infinix")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['品牌名称断言'])
        ValueAssert.value_assert_equal(test,"Infinix")

    @allure.story("商品列表")
    @allure.title("查询商品")
    @allure.description("输入产品名称，点击查询对应产品名称的商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_006(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品列表-产品名称框","自动化测试商品")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['产品名称断言'])
        ValueAssert.value_assert_equal(test,"自动化测试商品")

    @allure.story("商品列表")
    @allure.title("查询商品")
    @allure.description("输入商品状态，点击查询对应商品状态的商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_007(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品列表-商品状态框", "禁用")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['商品状态断言'])
        ValueAssert.value_assert_equal(test, "禁用")

    @allure.story("商品列表")
    @allure.title("查询商品")
    @allure.description("输入IMEI管理状态，点击查询对应状态的商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_008(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品列表-IMEI/SN管理框","是")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['IMEI/SN管理断言'])
        ValueAssert.value_assert_equal(test, "Yes")

    @allure.story("商品列表")
    @allure.title("查询商品")
    @allure.description("输入创建人，点击查询对应创建人的商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_009(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品列表-创建人框","张文强")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['创建人断言'])
        ValueAssert.value_assert_equal(test,"张文强[18651297]")

if __name__ == '__main__':
    pytest.main(['Good_List.py::TestQuery'])
