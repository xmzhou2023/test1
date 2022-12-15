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
    @allure.description("输入商品名称，查询物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self,drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = QueryMaterial(drivers)
        users.input_good("itel L4050 BLACK","PA00010262")
        users.click_query()
        sleep(0.5)
        # 断言--查询出的商品编码与查询的一致
        test = users.element_text(user['查询商品编码'])
        ValueAssert.value_assert_equal(test,"PA00010262")

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
    pytest.main(['Organization_Material.py'])
