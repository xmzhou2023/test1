import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_PlatformLibrary import PlatformLibrary


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 DRP数据管理-平台库 页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP数据管理", "平台库")
    dom = DomAssert(drivers)
    dom.assert_url("/dataManage/platformLibrary")
    yield
    logging.info("后置条件:关闭 DRP数据管理-平台库 页面")
    user.close_page()
    dom.assert_url("/dashboard")

@allure.feature("DRP数据管理-平台库")
class TestSearchPlatform:
    @allure.story("查询平台")
    @allure.title("按照平台条件过滤平台库信息")
    @allure.description("选择平台选项，查询 平台=埃塞转出口 的平台库信息")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        platform = PlatformLibrary(drivers)
        platform.screenOption("平台","埃塞转出口")
        platform.queryButton()
        platform.screenAssert("平台","埃塞转出口")
        platform.resetButton()


    @allure.story("查询物料状态")
    @allure.title("按照物料状态 条件过滤平台库信息")
    @allure.description("选择物料状态选项，查询 物料状态=整机 的平台库信息")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        platform = PlatformLibrary(drivers)
        platform.screenOption("物料状态","整机")
        platform.queryButton()
        platform.screenAssert("物料状态","整机")
        platform.resetButton()

    @allure.story("查询可用状态")
    @allure.title("按照可用状态 条件过滤平台库信息")
    @allure.description("选择可用状态选项，查询 可用状态=启用 的平台库信息")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        platform = PlatformLibrary(drivers)
        platform.screenOption("可用状态","启用")
        platform.queryButton()
        platform.screenAssert("可用状态","启用")
        platform.resetButton()


    @allure.story("组合条件查询 平台、物料状态、可用状态")
    @allure.title("按照组合条件过滤平台库信息")
    @allure.description("选择可用状态选项，查询 平台=HK-整机 物料状态=整机 可用状态=启用 的平台库信息")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_004(self, drivers):
        platform = PlatformLibrary(drivers)
        platform.screenOption("平台","HK-整机")
        platform.screenOption("物料状态","整机")
        platform.screenOption("可用状态","启用")
        platform.queryButton()
        platform.screenAssert("平台","HK-整机")
        platform.resetButton()

    @allure.story("异常 查询结果为空")
    @allure.title("按照组合条件过滤平台库信息，查询结果无数据")
    @allure.description("选择可用状态选项，查询 平台=HK-整机 物料状态=CKD 平台库信息，查询结果无数据展示")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_005(self, drivers):
        platform = PlatformLibrary(drivers)
        platform.screenOption("平台","HK-整机")
        platform.screenOption("物料状态","CKD")
        platform.queryButton()
        platform.exceptionAssert()
        platform.resetButton()

    @allure.story("查询重置")
    @allure.title("先按条件查询平台信息，点击重置按钮，清空查询条件")
    @allure.description("先按条件查询平台信息，点击重置按钮，清空查询条件，列表展示全部数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_006(self, drivers):
        platform = PlatformLibrary(drivers)
        platform.precondition(drivers)
        before = platform.listAssert()
        platform.resetButton()
        after = platform.listAssert()
        ValueAssert.value_assert_Notequal(before, after)





if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_PlatformLibrary.py'])

