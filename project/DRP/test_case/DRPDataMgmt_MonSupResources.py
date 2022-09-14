import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_MonSupResources import MonSupResources


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“DRP数据管理-颜色库”页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP数据管理", "月度供应资源")
    user = DomAssert(drivers)
    user.assert_url("/dataManage/monSupResources")


@allure.feature("DRP数据管理-月度供应资源")
class TestSearchMonSupResources:
    @allure.story("查询月度供应资源数据")
    @allure.title("按照颜提报周期 查询")
    @allure.description("选择颜提报周期 查询月度供应资源数据 结果正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        monSupResources = MonSupResources(drivers)
        monSupResources.choose_reportedCycle("2022","二月")
        monSupResources.query_button()
        assertValue = monSupResources.get_listText("itel")
        assertSQL = monSupResources.SQL_assert("2022","2","itel")
        assert assertValue == assertSQL ,logging.warning("断言失败")
        logging.info("断言成功，提报机型数量相等 {}，{}".format(assertValue,assertSQL))

    @allure.story("查询月度供应资源数据")
    @allure.title("按照品牌 查询")
    @allure.description("选择品牌 查询月度供应资源数据 结果正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        monSupResources = MonSupResources(drivers)
        monSupResources.choose_reportedCycle("2022","二月")
        monSupResources.choose_brand("itel")
        monSupResources.query_button()
        assertValue = monSupResources.get_listText("itel")
        assertSQL = monSupResources.SQL_assert("2022","2","itel")
        assert assertValue == assertSQL ,logging.warning("断言失败")
        logging.info("断言成功，提报机型数量相等 {}，{}".format(assertValue,assertSQL))

@allure.feature("DRP数据管理-月度供应资源")
class TestSearchReset:
    @allure.story("重置按钮功能")
    @allure.title("点击重置按钮，列表展示所在年的所有月度供应资源")
    @allure.description("点击重置按钮，列表展示所在年（2022）的所有月度供应资源")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        monSupResources = MonSupResources(drivers)
        monSupResources.reset_button()
        assertValue = monSupResources.retrun_listNum()
        assertSQL = monSupResources.SQL_assert("2022")
        assert assertValue == assertSQL ,logging.warning("断言失败")
        logging.info("断言成功，提报机型数量相等 {}，{}".format(assertValue,assertSQL))

@allure.feature("DRP数据管理-月度供应资源")
class TestCheckDetails:
    @allure.story("查看按钮功能")
    @allure.title("点击查看按钮，页面跳转至 月度供应资源查看 页签")
    @allure.description("点击查看按钮，页面跳转至 月度供应资源查看 页签，列表展示全部机型数据")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        monSupResources = MonSupResources(drivers)
        monSupResources = MonSupResources(drivers)
        monSupResources.choose_reportedCycle("2022","二月")
        monSupResources.choose_brand("itel")
        monSupResources.query_button()
        assertValue = monSupResources.get_listText("itel")
        monSupResources.check_details()
        assertValue1 = monSupResources.retrun_listNum()
        url = DomAssert(drivers)
        url.assert_url("/dataManage/monSupResources/view?fyear={}&fmonth={}&brandCode={}".format("2022",2,"itel"))
        assert assertValue == assertValue1 ,logging.warning("断言失败")
        logging.info("断言成功，提报机型数量相等 {}，{}".format(assertValue,assertValue1))
        monSupResources.close_tab()





if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_MonSupResources.py'])