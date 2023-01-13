import allure,logging
import pytest,random,time
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Good_Management import AddGood,ExportGood,QueryGood
from public.base.assert_ui import *
from project.POP.test_case.conftest import *
from libs.common.read_element import Element
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP商品-商品管理”页面")
    user = NavPage(drivers)
    user.click_gotonav("商品","商品管理")

@allure.feature("商品-商品管理") # 模块名称
class TestAddGood:
    @allure.story("商品管理") # 场景名称
    @allure.title("商品新增")  # 用例名称
    @allure.description("输入必填项新增商品成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AddGood(drivers)
        user.click_add()
        content = "zwq新增测试商品" + str(int(time.time()))
        user.input_productname(content)
        user.switch_category('qwz')
        user.switch_region('China')
        user.switch_brand('TECNO')
        user.switch_imei('否')
        user.add_goodinfo()
        user.click_preserve()
        sleep(0.5)
        # 断言--新增后页面返回商品管理页面判定页面是否存在商品管理字段
        DomAssert(drivers).assert_exact_att('商品管理')

@allure.feature("商品-商品管理") # 模块名称
class TestExportGood:
    @allure.story("商品管理") # 场景名称
    @allure.title("商品管理导出")  # 用例名称
    @allure.description("点击导出，商品管理列表导出成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_002_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = ExportGood(drivers)
        users.click_export()
        sleep(0.5)
        #断言-导出成功提示
        test = users.element_text(user['导出成功提示'])
        ValueAssert.value_assert_equal(test,"创建导出任务成功！")

@allure.feature("商品-商品管理")
class TestQuery:
    @allure.story("商品管理")
    @allure.title("查询商品")
    @allure.description("输入日期段，点击查询对应日期段商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_001(self,drivers):
        users = QueryGood(drivers)
        users.querygood("商品管理-开始日期框","2022-08-16","商品管理-结束日期框","2022-08-16")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['日期断言'])
        ValueAssert.value_assert_equal(test[0:10],"2022-08-16")

    @allure.story("商品管理")
    @allure.title("查询商品")
    @allure.description("输入产品名称，点击查询对应产品名的商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品管理-产品名称框","自动化测试商品")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['产品名称断言'])
        ValueAssert.value_assert_equal(test,"自动化测试商品")

    @allure.story("商品管理")
    @allure.title("查询商品")
    @allure.description("输入自采标记，点击查询对应标记商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_003(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品管理-自采标记框", "否")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['自采标记断言'])
        ValueAssert.value_assert_equal(test, "否")

    @allure.story("商品管理")
    @allure.title("查询商品")
    @allure.description("输入区域，点击查询对应区域商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_004(self,drivers):
        users = QueryGood(drivers)
        users.querygood("商品管理-区域框","万州")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['区域断言'])
        ValueAssert.value_assert_equal(test,"共 1 条")

    @allure.story("商品管理")
    @allure.title("查询商品")
    @allure.description("输入区域，点击查询对应区域商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_005(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品管理-品牌名称框", "Infinix")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['品牌名称断言'])
        ValueAssert.value_assert_equal(test, "Infinix")

    @allure.story("商品管理")
    @allure.title("查询商品")
    @allure.description("输入IMEI是否管理，点击查询对应商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_006(self,drivers):
        users = QueryGood(drivers)
        users.querygood("商品管理-IMEI/SN管理框","否")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['IMEI/SN管理断言'])
        ValueAssert.value_assert_equal(test,"否")

    @allure.story("商品管理")
    @allure.title("查询商品")
    @allure.description("输入创建人，点击查询对应创建人的商品数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_003_007(self, drivers):
        users = QueryGood(drivers)
        users.querygood("商品管理-创建人框","张文强")
        sleep(3)
        # 断言--查询商品名称与输入的商品名称一致
        test = users.element_text(user['创建人断言'])
        ValueAssert.value_assert_equal(test,"张文强[18651297]")

if __name__ == '__main__':
    pytest.main(['Good_Management.py::TestQuery'])
