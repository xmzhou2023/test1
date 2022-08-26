# -*- coding: utf-8 -*-
# @Time    : 2022-08-02 17:15
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : BasicInfo_BoardParametersSetting.py
# @Software: PyCharm
import allure
from project.MES_DAP.page_object.BssicInfo_FingerPrintCodes import BssicInfo_FingerPrintCodes
from project.MES_DAP.page_object.Center_Component import *
from public.base.assert_ui import *
from project.MES_DAP.test_case.conftest import *
import logging


@pytest.fixture(scope='module', autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往“基础信息-FingerPrint版本库”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("基础信息", "Fingerprint 版本库")
    result = DomAssert(drivers)
    result.assert_url("/basicData/FingerprintCodes")


@allure.feature("基础信息-FingerPrint版本库")
class TestSearchBssicInfo_FingerPrintCodes:
    @allure.story("查询FingerPrint版本")
    @allure.title("查询PCBA工段FingerPrint版本")
    @allure.description("进入FingerPrint版本库>点击查询按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1279691(self, drivers):
        info = BssicInfo_FingerPrintCodes(drivers)
        info.click_search()
        db = SQLAssert(pro_name, 'test')
        page = PageInfo(drivers)
        page_count = page.get_count()
        db.assert_sql_count(page_count, "SELECT count(id) FROM db_pldb_test.fingerprint_mgr;" )


@allure.feature("基础信息-FingerPrint版本库")
class TestInsertBssicInfo_FingerPrintCodes:
    @pytest.fixture(scope='class', autouse=True)
    def class_teardown_fixture(self, drivers):
        yield
        logging.info("新增类后置条件：删除新增的数据")
        info = BssicInfo_FingerPrintCodes(drivers)
        info.choice_band_section("Tecno")
        info.choice_model("SA1")
        info.choice_pcba("A245")
        info.click_search()
        info.click_del('1')
        info.click_del_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(0, "SELECT count(id) FROM db_pldb_test.fingerprint_mgr where brand = 'Tecno' and model ="
                               " 'SA1' and main_board = 'A245';")

    @allure.story("新增FingerPrint版本")
    @allure.title("所有字段正确填写，新增参数配置成功")
    @allure.description("进入FingerPrint版本库>点击新增按钮>正确填写所有内容>保存")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1279692(self, drivers):
        info = BssicInfo_FingerPrintCodes(drivers)
        info.click_insert()
        info.fill_form({"1": "Tecno", "2": "SA1", "3": "A245", "4": "111", "5": "10"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "SELECT count(id) FROM db_pldb_test.fingerprint_mgr where brand = 'Tecno' and model ="
                               " 'SA1' and main_board = 'A245';")


@allure.feature("基础信息-FingerPrint版本库")
class TestEditBssicInfo_FingerPrintCodes:
    @pytest.fixture(scope='class', autouse=True)
    def class_fixture(self, drivers):
        logging.info("修改类前置条件：新增数据")
        info = BssicInfo_FingerPrintCodes(drivers)
        info.click_insert()
        info.fill_form({"1": "Tecno", "2": "SA1", "3": "A245", "4": "111", "5": "10"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "SELECT count(id) FROM db_pldb_test.fingerprint_mgr where brand = 'Tecno' and model ="
                               " 'SA1' and main_board = 'A245';")
        yield
        logging.info("修改类前置条件：删除数据")
        info = BssicInfo_FingerPrintCodes(drivers)
        info.choice_band_section("Tecno")
        info.choice_model("SA1")
        info.choice_pcba("A245")
        info.click_search()
        info.click_del('1')
        info.click_del_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(0, "SELECT count(id) FROM db_pldb_test.fingerprint_mgr where brand = 'Tecno' and model ="
                               " 'SA1' and main_board = 'A245';")

    @allure.story("修改FingerPrint版本")
    @allure.title("所有字段正确填写，修改参数配置成功")
    @allure.description("进入FingerPrint版本库>查询要修改的数据>点击修改按钮>正确填写所有内容>保存")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1279694(self, drivers):
        info = BssicInfo_FingerPrintCodes(drivers)
        info.choice_band_section("Tecno")
        info.choice_model("SA1")
        info.choice_pcba("A245")
        info.click_search()
        info.click_edit('1')
        info.fill_form({"5": "20"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql("20", "select limit_qty from db_pldb_test.fingerprint_mgr where brand = 'Tecno' and model = "
                            "'SA1' and main_board = 'A245';")


@allure.feature("基础信息-FingerPrint版本库")
class TestDelBssicInfo_FingerPrintCodes:
    @pytest.fixture(scope='class', autouse=True)
    def class_setup_fixture(self, drivers):
        logging.info("删除类前置条件：新增数据")
        info = BssicInfo_FingerPrintCodes(drivers)
        info.click_insert()
        info.fill_form({"1": "Tecno", "2": "SA1", "3": "A245", "4": "111", "5": "10"})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "SELECT count(id) FROM db_pldb_test.fingerprint_mgr where brand = 'Tecno' and model ="
                               " 'SA1' and main_board = 'A245';")

    @allure.story("删除FingerPrint版本")
    @allure.title("查询后删除")
    @allure.description("进入FingerPrint版本库>选择查询条件>点击查询按钮>点击删除按钮>确认")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1279693(self, drivers):
        info = BssicInfo_FingerPrintCodes(drivers)
        info.choice_band_section("Tecno")
        info.choice_model("SA1")
        info.choice_pcba("A245")
        info.click_search()
        info.click_del('1')
        info.click_del_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(0, "SELECT count(id) FROM db_pldb_test.fingerprint_mgr where brand = 'Tecno' and model ="
                               " 'SA1' and main_board = 'A245';")


@allure.feature("基础信息-FingerPrint版本库")
class TestExportBssicInfo_FingerPrintCodes:
    @allure.story("导出FingerPrint版本")
    @allure.title("按工段导出FingerPrint版本")
    @allure.description("进入FingerPrint版本库>重置查询条件>查询全量数据>点击导出按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1279695(self, drivers):
        info = BssicInfo_FingerPrintCodes(drivers)
        info.click_reset()
        info.click_search()
        info.click_export(content="FingerprintCodes")





