# -*- coding: utf-8 -*-
# @Time    : 2022-08-02 17:15
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : BasicInfo_BoardParametersSetting.py
# @Software: PyCharm
import allure
from project.MES_DAP.page_object.BasicInfo_ProductionLineInfoSetting import ProductionLineInfoSetting
from project.MES_DAP.page_object.Center_Component import *
from public.base.assert_ui import *
from project.MES_DAP.test_case.conftest import *
import logging


@pytest.fixture(scope='module', autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往“基础信息-产线信息配置”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("基础信息", "产线信息配置")
    result = DomAssert(drivers)
    result.assert_url("/basicData/ProductionLineConfig")


@allure.feature("基础信息-产线信息配置")
class TestSearchProductionLineInfoSetting:
    @allure.story("查询产线信息配置")
    @allure.title("查询PCBA工段产线信息配置")
    @allure.description("进入产线信息配置>工段选择PCBA>点击查询按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1028958(self, drivers):
        info = ProductionLineInfoSetting(drivers)
        info.choice_workshop_section('PCBA')
        info.click_search()
        db = SQLAssert(pro_name, 'test')
        page = PageInfo(drivers)
        page_count = page.get_count()
        db.assert_sql_count(page_count, "select count(id) from db_pldb_test.line_info li where station_type = 'FE'; " )


@allure.feature("基础信息-产线信息配置")
class TestInsertProductionLineInfoSetting:
    @pytest.fixture(scope='class', autouse=True)
    def class_teardown_fixture(self, drivers):
        yield
        logging.info("新增类后置条件：删除新增的数据")
        info = ProductionLineInfoSetting(drivers)
        info.choice_workshop_section("PCBA")
        info.choice_line("p1")
        info.choice_line_type("小线")
        info.click_search()
        info.click_del('1')
        info.click_del_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(0, "select count(id) from db_pldb_test.line_info li where station_type = 'FE' and line_no "
                               "='100047';")

    @allure.story("新增产线信息配置")
    @allure.title("所有字段正确填写，新增参数配置成功")
    @allure.description("进入产线信息配置>点击新增按钮>正确填写所有内容>保存")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1028931(self, drivers):
        info = ProductionLineInfoSetting(drivers)
        info.click_insert()
        info.fill_form({"1": "PCBA", "2": "p1", "4": "李四", "5": "安露", "6": "王五一", "7": "95", "8": "100",
                        "9": "100", "10": "100"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "select count(id) from db_pldb_test.line_info li where station_type = 'FE' and line_no "
                               "='100047';")


@allure.feature("基础信息-产线信息配置")
class TestEditProductionLineInfoSetting:
    @pytest.fixture(scope='class', autouse=True)
    def class_fixture(self, drivers):
        logging.info("修改类前置条件：新增数据")
        info = ProductionLineInfoSetting(drivers)
        info.click_insert()
        info.fill_form({"1": "PCBA", "2": "p1", "4": "李四", "5": "安露", "6": "王五一", "7": "95", "8": "100",
                        "9": "100", "10": "100"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "select count(id) from db_pldb_test.line_info li where station_type = 'FE' and line_no "
                               "='100047';")
        yield
        logging.info("修改类前置条件：删除数据")
        info = ProductionLineInfoSetting(drivers)
        info.choice_workshop_section("PCBA")
        info.choice_line("p1")
        info.choice_line_type("小线")
        info.click_search()
        info.click_del('1')
        info.click_del_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(0, "select count(id) from db_pldb_test.line_info li where station_type = 'FE' and line_no "
                               "='100047';")

    @allure.story("修改产线信息配置")
    @allure.title("所有字段正确填写，修改参数配置成功")
    @allure.description("进入产线信息配置>查询要修改的数据>点击修改按钮>正确填写所有内容>保存")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1028949(self, drivers):
        info = ProductionLineInfoSetting(drivers)
        info.choice_workshop_section("PCBA")
        info.choice_line("p1")
        info.choice_line_type("小线")
        info.click_search()
        info.click_edit('1')
        info.fill_form({"10": "0"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql("0", "select uph from db_pldb_test.line_info li where station_type = 'FE' and line_no ='100047';")


@allure.feature("基础信息-产线信息配置")
class TestDelProductionLineInfoSetting:
    @pytest.fixture(scope='class', autouse=True)
    def class_setup_fixture(self, drivers):
        logging.info("删除类前置条件：新增数据")
        info = ProductionLineInfoSetting(drivers)
        info.click_insert()
        info.fill_form({"1": "PCBA", "2": "p1", "4": "李四", "5": "安露", "6": "王五一", "7": "95", "8": "100",
                        "9": "100", "10": "100"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "select count(id) from db_pldb_test.line_info li where station_type = 'FE' and line_no "
                               "='100047';")

    @allure.story("删除产线信息配置")
    @allure.title("查询后删除")
    @allure.description("进入产线信息配置>选择查询条件>点击查询按钮>点击删除按钮>确认")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1028933(self, drivers):
        info = ProductionLineInfoSetting(drivers)
        info.choice_workshop_section("PCBA")
        info.choice_line("p1")
        info.choice_line_type("小线")
        info.click_search()
        info.click_del('1')
        info.click_del_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(0, "select count(id) from db_pldb_test.line_info li where station_type = 'FE' and line_no "
                               "='100047';")


@allure.feature("基础信息-产线信息配置")
class TestExportProductionLineInfoSetting:
    @allure.story("导出产线信息配置")
    @allure.title("按工段导出产线信息配置")
    @allure.description("进入产线信息配置>重置查询条件>选择PCBA工段>查询全量数据>点击导出按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1028962(self, drivers):
        info = ProductionLineInfoSetting(drivers)
        info.click_reset()
        info.choice_workshop_section('PCBA')
        info.click_search()
        info.click_export(content="ExportLineConfig")





