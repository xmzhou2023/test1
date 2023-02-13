from project.POP.page_object.Shop_Approval import *
from project.POP.page_object.Center_Component import NavPage
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP门店-门店审批”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("门店","门店审批")

@allure.feature("门店-门店审批") # 模块名称
class TestShopApproval:
    @allure.story("门店审批") # 场景名称
    @allure.title("查询门店审批")  # 用例名称
    @allure.description("输入门店，查询对应门店审批数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self,drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = QueryShopApproval(drivers)
        users.queryhopapproval("门店审批-门店框","小鸡专卖店")
        sleep(5)
        # 断言
        test = users.element_text(user['门店断言'])
        ValueAssert.value_assert_equal(test,'小鸡专卖店')

    @allure.story("门店审批")  # 场景名称
    @allure.title("查询门店审批")  # 用例名称
    @allure.description("输入组织，查询对应门店审批数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self,drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = QueryShopApproval(drivers)
        users.queryhopapproval("门店审批-组织框","oraimo")
        sleep(5)
        # 断言
        test = users.element_text(user['组织断言'])
        ValueAssert.value_assert_equal(test,'oraimo')

    @allure.story("门店审批")  # 场景名称
    @allure.title("查询门店审批")  # 用例名称
    @allure.description("输入国家，查询对应门店审批数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self,drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = QueryShopApproval(drivers)
        users.queryhopapproval("门店审批-国家框","China")
        sleep(5)
        # 断言
        test = users.element_text(user['国家断言'])
        ValueAssert.value_assert_equal(test,'China')

    @allure.story("门店审批")  # 场景名称
    @allure.title("查询门店审批")  # 用例名称
    @allure.description("输入审批状态，查询对应门店审批数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = QueryShopApproval(drivers)
        users.queryhopapproval("门店审批-状态框","审批中")
        sleep(5)
        # 断言
        test = users.element_text(user['审批状态断言'])
        ValueAssert.value_assert_equal(test,'审批中')

    @allure.story("门店审批")  # 场景名称
    @allure.title("查询门店审批")  # 用例名称
    @allure.description("输入区域，查询对应区域门店审批数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = QueryShopApproval(drivers)
        users.queryhopapproval("门店审批-区域框","China")
        sleep(5)
        # 断言
        test = users.element_text(user['区域断言'])
        ValueAssert.value_assert_equal(test,'China')

if __name__ == '__main__':
    pytest.main(['Shop_Approval.py'])
