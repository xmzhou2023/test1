import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_MonSalesOrder import MonSalesOrder


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“DRP数据管理-月度销售订单”页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP数据管理", "月度销售订单")
    user = DomAssert(drivers)
    user.assert_url("/dataManage/monSalesOrder")


@allure.feature("DRP数据管理-月度销售订单")
class TestSearchMonSalesOrder:
    @allure.story("查询月度销售订单数据")
    @allure.title("按照提报周期 查询")
    @allure.description("选择提报周期 查询月度销售订单数据 结果正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        monSalesOrder = MonSalesOrder(drivers)
        monSalesOrder.choose_reportedCycle("2022","二月")
        monSalesOrder.query_button()
        assertValue = monSalesOrder.get_listText("itel")
        assertSQL = monSalesOrder.SQL_assert("2022","2","itel")
        assert assertValue == assertSQL ,logging.warning("断言失败")
        logging.info("断言成功，提报数量相等 {}，{}".format(assertValue,assertSQL))
        monSalesOrder.reset_button()

    @allure.story("查询月度销售订单数据")
    @allure.title("按照品牌 查询")
    @allure.description("选择品牌 查询月度销售订单数据 结果正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        monSalesOrder = MonSalesOrder(drivers)
        monSalesOrder.choose_reportedCycle("2022","二月")
        monSalesOrder.choose_brand("itel")
        monSalesOrder.query_button()
        assertValue = monSalesOrder.get_listText("itel")
        assertSQL = monSalesOrder.SQL_assert("2022","2","itel")
        assert assertValue == assertSQL ,logging.warning("断言失败")
        logging.info("断言成功，提报数量相等 {}，{}".format(assertValue,assertSQL))
        monSalesOrder.reset_button()

@allure.feature("DRP数据管理-月度销售订单")
class TestSearchReset:
    @allure.story("重置按钮功能")
    @allure.title("点击重置按钮，列表展示所在年的所有月度销售订单")
    @allure.description("点击重置按钮，列表展示所在年（2022）的所有月度销售订单")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        monSalesOrder = MonSalesOrder(drivers)
        monSalesOrder.reset_button()
        assertValue = monSalesOrder.retrun_listNum()
        assertSQL = monSalesOrder.SQL_assert("2022")
        assert assertValue == assertSQL ,logging.warning("断言失败")
        logging.info("断言成功，提报数量相等 {}，{}".format(assertValue,assertSQL))

@allure.feature("DRP数据管理-月度销售订单")
class TestCheckDetails:
    @allure.story("查看按钮功能")
    @allure.title("点击查看按钮，页面跳转至 月度销售订单查看 页签")
    @allure.description("点击查看按钮，页面跳转至 月度销售订单查看 页签，列表展示全部机型数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        monSalesOrder = MonSalesOrder(drivers)
        monSalesOrder.choose_reportedCycle("2022","一月")
        monSalesOrder.choose_brand("itel")
        monSalesOrder.query_button()
        monSalesOrder.check_details()
        url = DomAssert(drivers)
        url.assert_url("/dataManage/monSalesOrder/view?fyear={}&fmonth={}&brandCode={}".format("2022",1,"itel"))
        monSalesOrder.close_tab("月度销售订单查看")

    @allure.story("编辑按钮功能")
    @allure.title("点击编辑按钮，页面跳转至 月度销售订单编辑 页签")
    @allure.description("点击编辑按钮，页面跳转至 月度销售订单编辑 页签，列表展示全部机型数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        monSalesOrder = MonSalesOrder(drivers)
        monSalesOrder.choose_reportedCycle("2022","二月")
        monSalesOrder.choose_brand("itel")
        monSalesOrder.query_button()
        monSalesOrder.check_details()
        url = DomAssert(drivers)
        url.assert_url("/dataManage/monSalesOrder/edit?fyear={}&fmonth={}&brandCode={}".format("2022",2,"itel"))
        monSalesOrder.close_tab("月度销售订单编辑")



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_MonClearMission.py'])