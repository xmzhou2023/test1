import allure
import pytest
from project.POP.page_object.Organization_Material import QueryMore,QueryMaterial,ExportMaterial
from project.POP.page_object.Center_Component import NavPage
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP商品-物料信息”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("商品","物料信息")

@allure.feature("商品-物料信息") # 模块名称
class TestQueryMaterial:
    @allure.story("物料信息") # 场景名称
    @allure.title("根据商品名称查询物料")  # 用例名称
    @allure.description("输入创建日期段，查询对应时间下的物料信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self,drivers):
        users = QueryMaterial(drivers)
        users.querymaterial("开始日期框","2022-11-30","结束日期框","2022-11-30")
        sleep(2)
        # 断言--查询出的商品编码与查询的一致
        test = users.element_text(user['日期断言'])
        ValueAssert.value_assert_equal(test[0:10],"2022-11-30")

    @allure.story("物料信息")  # 场景名称
    @allure.title("根据商品名称查询物料")  # 用例名称
    @allure.description("输入是否绑定商品，查询对应物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        users = QueryMaterial(drivers)
        users.querymaterial("是否绑定商品框","是")
        sleep(2)
        # 断言--查询出的商品编码与查询的一致
        test = users.element_text(user['是否绑定商品断言'])
        ValueAssert.value_assert_equal(test,"是")

    @allure.story("物料信息")  # 场景名称
    @allure.title("根据商品名称查询物料")  # 用例名称
    @allure.description("输入商品名称，查询对应商品名称的物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):
        users = QueryMaterial(drivers)
        users.querymaterial("商品名称框","PA00007465")
        sleep(2)
        # 断言--查询出的商品编码与查询的一致
        test = users.element_text(user['商品名称断言'])
        ValueAssert.value_assert_equal(test,"Infinix SMART 5 64+3 QUETZAL CYAN")

    @allure.story("物料信息")  # 场景名称
    @allure.title("根据商品名称查询物料")  # 用例名称
    @allure.description("输入品牌名称，查询对应品牌的物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):
        users = QueryMaterial(drivers)
        users.querymaterial("品牌名称框","Infinix")
        sleep(2)
        # 断言--查询出的商品编码与查询的一致
        test = users.element_text(user['品牌名称断言'])
        ValueAssert.value_assert_equal(test,"Infinix")

    @allure.story("物料信息")  # 场景名称
    @allure.title("根据商品名称查询物料")  # 用例名称
    @allure.description("输入市场名称，查询对应市场的物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):
        users = QueryMaterial(drivers)
        users.querymaterial("市场名称框","T920")
        sleep(3)
        # 断言--查询出的商品编码与查询的一致
        test = users.element_text(user['市场名称断言'])
        ValueAssert.value_assert_equal(test,"T920")

    @allure.story("物料信息")  # 场景名称
    @allure.title("根据商品名称查询物料")  # 用例名称
    @allure.description("输入物料名称，查询对应物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):
        users = QueryMaterial(drivers)
        users.querymaterial("物料名称框","12019565")
        sleep(2)
        # 断言--查询出的商品编码与查询的一致
        test = users.element_text(user['物料名称断言'])
        ValueAssert.value_assert_equal(test,"Infinix X6511B A1 POLAR BLACK CS 32+2")

@allure.feature("商品-物料信息") # 模块名称
class TestQueryMore:
    @allure.story("物料信息") # 场景名称
    @allure.title("查看更多筛选条件")  # 用例名称
    @allure.description("点击更多，查看更多筛选条件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_002_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = QueryMore(drivers)
        users.click_more()
        sleep(0.5)
        # 断言--断言页面是否存在更多筛选条件页--筛选
        DomAssert(drivers).assert_exact_att('筛选')
        # 筛选断言后点击重置关闭筛选更多页面
        users.refresh()
        sleep(3)

@allure.feature("商品-物料信息") # 模块名称
class TestExportMaterial:
    @allure.story("物料信息") # 场景名称
    @allure.title("导出物料信息")  # 用例名称
    @allure.description("点击导出，导出物料信息列表成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_003_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = ExportMaterial(drivers)
        users.click_export()
        sleep(0.5)
        # 断言--导出成功提示内容
        test = users.element_text(user['导出成功提示'])
        ValueAssert.value_assert_equal(test, '创建导出任务成功！')

if __name__ == '__main__':
    pytest.main(['Organization_Material.py::TestQueryMaterial'])
