import allure
import pytest

from public.base.assert_ui import *
from project.MIP.page_object.Center_Component import NavPage
from project.MIP.page_object.MainDataRequestCap import MainDataRequestCap


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 主数据-请购上限管理 页面")
    menu = NavPage(drivers)
    menu.click_gotonav("主数据","请购上限管理")
    dom = DomAssert(drivers)
    dom.assert_url("/main-data/requestCap")
    yield
    logging.info("后置条件:返回 首页 页面")
    menu.back_homepage("主数据")
    dom.assert_url("/dashboard")


@allure.feature("主数据-请购上限管理")
class TestQueryRequestCap:
    @allure.story("查询功能验证")
    @allure.title("输入查询项，查询结果正确")
    @allure.description("输入查询项，查询结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        requestCap = MainDataRequestCap(drivers)
        requestCap.input_itemCode("41500100034")
        requestCap.choice_brand("TECNO")
        requestCap.choice_status("删除")
        requestCap.button_query()
        listNum = requestCap.get_listNum()
        sqlNum = requestCap.get_sqlResult("select count(mat_code) from mm_req_list_limit where mat_code = '41500100034';")
        ValueAssert.value_assert_equal(listNum, sqlNum)
        requestCap.button_reset()


@allure.feature("主数据-请购上限管理")
class TestAddRequestCap:
    @allure.story("新增功能验证")
    @allure.title("合法维护，新增数据成功")
    @allure.description("合法维护，新增数据成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        requestCap = MainDataRequestCap(drivers)
        requestCap.button_newly()

        requestCap.input_itemCode("41500100034")
        requestCap.choice_brand("TECNO")
        requestCap.choice_status("删除")
        requestCap.button_query()
        listNum = requestCap.get_listNum()
        sqlNum = requestCap.get_sqlResult("select count(mat_code) from mm_req_list_limit where mat_code = '41500100034';")
        ValueAssert.value_assert_equal(listNum, sqlNum)
        requestCap.button_reset()