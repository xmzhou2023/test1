# -*- coding: utf-8 -*-
# @Time    : 2022-08-02 17:15
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : BasicInfo_BoardParametersSetting.py
# @Software: PyCharm
import allure
from project.MES_DAP.page_object.BasicInfo_BoardParametersSetting import BoardParametersSetting
from project.MES_DAP.page_object.Center_Component import *
from public.base.assert_ui import *
from project.MES_DAP.test_case.conftest import *
import logging


@pytest.fixture(scope='module', autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往“基础信息-看板参数配置”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("基础信息", "看板参数配置")
    result = DomAssert(drivers)
    result.assert_url("/basicData/BoardConfig")


@allure.feature("基础信息-看板参数配置")
class TestSearchParametersSetting:
    @allure.story("查询参数配置")
    @allure.title("条件为空查询信息")
    @allure.description("进入看板参数配置>点击查询按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1029040(self, drivers):
        info = BoardParametersSetting(drivers)
        info.click_reset()
        info.click_search()
        db = SQLAssert(pro_name, 'test')
        page = PageInfo(drivers)
        page_count = page.get_count()
        db.assert_sql_count(page_count, "select count(station_type) from db_pldb_test.project_info pi2;")


@allure.feature("基础信息-看板参数配置")
class TestInsertParametersSetting:
    @pytest.fixture(scope='class', autouse=True)
    def class_teardown_fixture(self, drivers):
        yield
        logging.info("新增类后置条件：删除新增的数据")
        info = BoardParametersSetting(drivers)
        info.choice_workshop_section("PCBA")
        info.choice_model("H371")
        info.choice_line_type("小线")
        info.click_search()
        info.click_del('1')
        info.click_del_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(0, "select count(station_type) from db_pldb_test.project_info pi2 where station_type "
                               "='FE' and project_name = 'H371' and line_classify = '2';")

    @allure.story("新增参数配置")
    @allure.title("所有字段正确填写，新增参数配置成功")
    @allure.description("进入看板参数配置>点击新增按钮>正确填写所有内容>保存")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1099070(self, drivers):
        info = BoardParametersSetting(drivers)
        info.click_insert()
        info.fill_form({"1": "PCBA", "2": "H371", "3": "小线", "4": "10", "5": "2", "6": "12", "7": "95", "8": "100",
                        "9": "100", "10": "100", "11": "0"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "select count(station_type) from db_pldb_test.project_info pi2 where station_type "
                               "='FE' and project_name = 'H371' and line_classify = '2';")


@allure.feature("基础信息-看板参数配置")
class TestEditParametersSetting:
    @pytest.fixture(scope='class', autouse=True)
    def class_fixture(self, drivers):
        logging.info("修改类前置条件：新增数据")
        info = BoardParametersSetting(drivers)
        info.click_insert()
        info.fill_form({"1": "PCBA", "2": "H371", "3": "小线", "4": "10", "5": "2", "6": "12", "7": "95", "8": "100",
                        "9": "100", "10": "100", "11": "0"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "select count(station_type) from db_pldb_test.project_info pi2 where station_type "
                               "='FE' and project_name = 'H371' and line_classify = '2';")
        yield
        logging.info("修改类前置条件：删除数据")
        info = BoardParametersSetting(drivers)
        info.choice_workshop_section("PCBA")
        info.choice_model("H371")
        info.choice_line_type("小线")
        info.click_search()
        info.click_del('1')
        info.click_del_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(0, "select count(station_type) from db_pldb_test.project_info pi2 where station_type "
                               "='FE' and project_name = 'H371' and line_classify = '2';")

    @allure.story("修改参数配置")
    @allure.title("所有字段正确填写，修改参数配置成功")
    @allure.description("进入看板参数配置>查询到需要修改的数据>点击编辑按钮>正确填写所有内容>保存")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1029033(self, drivers):
        info = BoardParametersSetting(drivers)
        info.choice_workshop_section("PCBA")
        info.choice_model("H371")
        info.choice_line_type("小线")
        info.click_search()
        info.click_edit('1')
        info.fill_form({"11": "100"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql("100.000", "select completion_rate from db_pldb_test.project_info pi2 where station_type "
                               "='FE' and project_name = 'H371' and line_classify = '2';")


@allure.feature("基础信息-看板参数配置")
class TestDelParametersSetting:
    @pytest.fixture(scope='class', autouse=True)
    def class_setup_fixture(self, drivers):
        logging.info("删除类前置条件：新增数据")
        info = BoardParametersSetting(drivers)
        info.click_insert()
        info.fill_form({"1": "PCBA", "2": "H371", "3": "小线", "4": "10", "5": "2", "6": "12", "7": "95", "8": "100",
                        "9": "100", "10": "100", "11": "0"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "select count(station_type) from db_pldb_test.project_info pi2 where station_type "
                               "='FE' and project_name = 'H371' and line_classify = '2';")

    @allure.story("删除参数配置")
    @allure.title("查询后删除")
    @allure.description("进入看板参数配置>选择查询条件>点击查询按钮>点击删除按钮>确认")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1029021(self, drivers):
        info = BoardParametersSetting(drivers)
        info.choice_workshop_section("PCBA")
        info.choice_model("H371")
        info.choice_line_type("小线")
        info.click_search()
        info.click_del('1')
        info.click_del_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(0, "select count(station_type) from db_pldb_test.project_info pi2 where station_type "
                               "='FE' and project_name = 'H371' and line_classify = '2';")


# @allure.feature("基础信息-看板参数配置")
# class TestExportParametersSetting:
#     @allure.story("导出参数配置")
#     @allure.title("全量导出参数配置")
#     @allure.description("进入看板参数配置>重置查询条件>查询全量数据>点击导出按钮")
#     @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
#     def test_1273168(self, drivers):
#         info = BoardParametersSetting(drivers)
#         info.click_reset()
#         info.click_search()
#         info.click_export(content="ExportParaConfig")





