import allure
import pytest
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Supplier_Management import *
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP组织-供应商管理”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("组织","供应商管理")

@allure.feature("组织-供应商管理") # 模块名称
class TestQuerySupplier:
    @allure.story("供应商管理") # 场景名称
    @allure.title("查询卖家姓名")  # 用例名称
    @allure.description("根据卖家姓名查询供应商信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = SupplierManagement(drivers)
        users.querysupplier("卖家名称框","BD405358")
        sleep(2)
        # 断言-查询卖家编码与输入编码一致
        test = users.element_text(user['卖家名称断言'])
        ValueAssert.value_assert_equal(test,"刘书美国包")

    @allure.story("供应商管理")  # 场景名称
    @allure.title("查询卖家类型")  # 用例名称
    @allure.description("根据卖家类型查询供应商信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = SupplierManagement(drivers)
        users.querysupplier("卖家类型框","国包")
        sleep(2)
        # 断言--查询的卖家类型与输入的一致
        test = users.element_text(user['卖家类型断言'])
        ValueAssert.value_assert_equal(test,"国包")

    @allure.story("供应商管理")  # 场景名称
    @allure.title("查询卖家国家")  # 用例名称
    @allure.description("根据卖家国家查询供应商信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = SupplierManagement(drivers)
        users.querysupplier("卖家国家框","Bangladesh")
        sleep(2)
        # 断言--查询的卖家类型与输入的一致
        test = users.element_text(user['卖家国家断言'])
        ValueAssert.value_assert_equal(test, "Bangladesh")

    @allure.story("供应商管理")  # 场景名称
    @allure.title("查询门店")  # 用例名称
    @allure.description("根据门店查询供应商信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = SupplierManagement(drivers)
        users.querysupplier("供应商门店框","Wanzhou Popcorn")
        sleep(10)
        # 断言--查询的门店与输入的一致
        test = users.element_text(user['供应商门店断言'])
        ValueAssert.value_assert_equal(test,"Wanzhou Popcorn")

    @allure.step("供应商管理")
    @allure.title("验证更多筛选条件框")  # 用例名称
    @allure.description("点击更多，弹出更多筛选条件框")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = SupplierManagement(drivers)
        users.click_more()
        # 断言--弹窗页面有筛选字样
        DomAssert(drivers).assert_exact_att('筛选')
        # 页面清理关闭筛选字样
        users.click_close()

    @allure.story("供应商管理")  # 场景名称
    @allure.title("查询门店国家")  # 用例名称
    @allure.description("根据门店国家查询供应商信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = SupplierManagement(drivers)
        users.click_more()
        users.querysupplier("门店国家框","Bangladesh")
        sleep(2)
        # 断言--查询的卖家类型与输入的一致
        test = users.element_text(user['门店国家断言'])
        ValueAssert.value_assert_equal(test, "Bangladesh")

    @allure.story("供应商管理")  # 场景名称
    @allure.title("查询归属机构")  # 用例名称
    @allure.description("根据归属机构查询供应商信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_007(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = SupplierManagement(drivers)
        users.click_more()
        users.querysupplier("归属机构框","TECNO事业部")
        sleep(2)
        # 断言--查询的卖家类型与输入的一致
        test = users.element_text(user['归属组织断言'])
        ValueAssert.value_assert_equal(test, "TECNO事业部")



@allure.feature("组织-供应商管理") # 模块名称
class TestExportSupplier:
    @allure.story("供应商管理") # 场景名称
    @allure.title("导出供应商管理")  # 用例名称
    @allure.description("导出供应商管理列表")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_002_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = ExportSupplier(drivers)
        users.click_export()
        sleep(0.5)
        # 断言--导出成功提示
        test = users.element_text(user['导出成功提示'])
        ValueAssert.value_assert_equal(test,"创建导出任务成功！")

if __name__ == '__main__':
    pytest.main(['Supplier_Management.py::TestQuerySupplier'])
