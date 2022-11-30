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
    menu.back_homepage()
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
        requestCap.input_itemCode("41500201924")
        requestCap.choice_brand("INFINIX")
        requestCap.choice_status("删除")
        requestCap.button_query()
        listNum = requestCap.get_listNum()
        sqlNum = requestCap.get_sqlResult("select count(mat_code) from mm_req_list_limit where mat_code = '41500201924'and enable_flag ='0';")
        ValueAssert.value_assert_equal(listNum, sqlNum)
        requestCap.button_reset()


@allure.feature("主数据-请购上限管理")
class TestAddRequestCap:
    @allure.story("新增功能验证")
    @allure.title("合法维护，新增数据成功")
    @allure.description("合法维护，新增数据成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        requestCap = MainDataRequestCap(drivers)
        requestCap.button_newly()
        requestCap.add_info("41500100034", "200")
        requestCap.input_itemCode("41500100034")
        requestCap.choice_status("启用")
        requestCap.button_query()
        listNum = requestCap.get_listNum()
        sqlNum = requestCap.get_sqlResult("select count(mat_code) from mm_req_list_limit where mat_code = '41500100034' and enable_flag ='1';")
        ValueAssert.value_assert_equal(listNum, sqlNum)
        requestCap.button_reset()
        requestCap.clear_testData("41500100034")

    @allure.story("新增功能验证")
    @allure.title("[异常]重复新增，新增失败")
    @allure.description("重复新增物料41500100034，新增失败")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_002(self, drivers):
        requestCap = MainDataRequestCap(drivers)
        requestCap.create_testData(drivers,"41500100034", "200")
        requestCap.button_newly()
        requestCap.add_info("41500100034", "200")
        requestCap.input_itemCode("41500100034")
        requestCap.choice_status("启用")
        requestCap.button_query()
        listNum = requestCap.get_listNum()
        sqlNum = requestCap.get_sqlResult("select count(mat_code) from mm_req_list_limit where mat_code = '41500100034' and enable_flag ='1';")
        ValueAssert.value_assert_equal(listNum, 1)
        ValueAssert.value_assert_equal(sqlNum, 1)
        requestCap.button_reset()
        requestCap.clear_testData("41500100034")

    @allure.story("新增功能验证")
    @allure.title("[异常]必填项未维护，新增失败")
    @allure.description("必填项未维护，新增失败")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("itemcode,num",[("",""),("41500100034",""),("","200")])
    @pytest.mark.smoke
    def test_002_003(self, drivers, itemcode,num):
        requestCap = MainDataRequestCap(drivers)
        requestCap.button_newly()
        requestCap.add_info(itemcode,num,"反例")


@allure.feature("主数据-请购上限管理")
class TestEditRequestCap:
    @allure.story("编辑功能验证")
    @allure.title("合法编辑物料信息，编辑保存成功")
    @allure.description("合法编辑物料信息，编辑保存成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        requestCap = MainDataRequestCap(drivers)
        requestCap.create_testData(drivers,"41500100034", "200")
        requestCap.query_testData(drivers,"41500100034", "TECNO", "启用")
        requestCap.button_edit()
        requestCap.edit_info("123")
        requestCap.button_query()
        sqlNum = requestCap.get_sqlResult("select limit_box from mm_req_list_limit where mat_code = '41500100034' and enable_flag ='1';")
        ValueAssert.value_assert_equal(sqlNum, 123)
        requestCap.button_reset()
        requestCap.clear_testData("41500100034")

    @allure.story("编辑功能验证")
    @allure.title("[异常]未做修改，编辑保存失败，提示信息正确")
    @allure.description("未做修改，编辑保存失败，提示信息正确")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        requestCap = MainDataRequestCap(drivers)
        requestCap.create_testData(drivers,"41500100034", "200")
        requestCap.query_testData(drivers,"41500100034", "TECNO", "启用")
        requestCap.button_edit()
        requestCap.edit_info("200")
        requestCap.button_query()
        sqlNum = requestCap.get_sqlResult("select limit_box from mm_req_list_limit where mat_code = '41500100034' and enable_flag ='1';")
        ValueAssert.value_assert_equal(sqlNum, 200)
        requestCap.button_reset()
        requestCap.clear_testData("41500100034")

    @allure.story("编辑功能验证")
    @allure.title("[异常]清空维护项，编辑保存失败，提示信息正确")
    @allure.description("清空维护项，编辑保存失败，提示信息正确")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_003(self, drivers):
        requestCap = MainDataRequestCap(drivers)
        requestCap.create_testData(drivers,"41500100034", "200")
        requestCap.query_testData(drivers,"41500100034", "TECNO", "启用")
        requestCap.button_edit()
        requestCap.edit_info("",type='反例')
        requestCap.button_reset()
        requestCap.clear_testData("41500100034")


@allure.feature("主数据-请购上限管理")
class TestChangeRequestCapStatus:
    @allure.story("修改状态功能验证")
    @allure.title("将启用状态的物料改为禁用，状态修改成功")
    @allure.description("将启用状态的物料改为禁用，状态修改成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_001(self, drivers):
        requestCap = MainDataRequestCap(drivers)
        requestCap.create_testData(drivers,"41500100034", "200")
        requestCap.query_testData(drivers,"41500100034", "TECNO", "启用")
        requestCap.button_changeStatus()
        requestCap.query_testData(drivers,"41500100034", "TECNO", "删除")
        listNum = requestCap.get_listNum()
        sqlNum = requestCap.get_sqlResult("select count(mat_code) from mm_req_list_limit where mat_code = '41500100034'and enable_flag ='0';")
        ValueAssert.value_assert_equal(listNum, sqlNum)
        requestCap.button_reset()
        requestCap.clear_testData("41500100034","删除")