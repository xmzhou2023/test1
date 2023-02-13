# -*- coding: utf-8 -*-
# @Time    : 2022-07-29 11:09
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : BasicInfo_DailyProductionPlan.py
# @Software: PyCharm
import logging
import os
from datetime import date

import allure
import pytest

from libs.config.conf import BASE_DIR
from project.MES_DAP.page_object.BasicInfo_DailyProductionPlan import DailyProductionPlan
from project.MES_DAP.page_object.Center_Component import NavPage, PageInfo, ReadData
from project.MES_DAP.test_case.conftest import pro_name
from public.base.assert_ui import DomAssert, SQLAssert


@pytest.fixture(scope='module', autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往“基础信息-日生产计划”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("基础信息", "日生产计划")
    result = DomAssert(drivers)
    result.assert_url("/basicData/ProductionPlan")


@allure.feature("基础信息-日生产计划")
class TestSearchDailyProductionPlan:
    @allure.story("查询日计划")
    @allure.title("条件为空查询信息")
    @allure.description("进入日生产计划>点击查询按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1023960(self, drivers):
        info = DailyProductionPlan(drivers)
        info.click_reset()
        info.input_date(str(date.today()))
        info.click_search()
        db = SQLAssert(pro_name, 'test')
        page = PageInfo(drivers)
        page_count = page.get_count()
        db.assert_sql_count(page_count, "SELECT count(id) FROM db_pldb_test.line_plan where plan_date = '%s';" % date.today())


@allure.feature("基础信息-日生产计划")
class TestImportDailyProductionPlan:
    values = ReadData().read_excel(os.path.join(BASE_DIR, 'project', 'MES_DAP', 'data', 'parametrize.xls'), 'ImportDailyPlan', 'row', rows=1)
    @allure.story("导入日计划")
    @allure.title("导入日计划")
    @allure.description("进入日生产计划>点击【导入计划】按钮")
    @allure.severity("blocker")
    @pytest.mark.parametrize('station_type_code, station_type, file_name', values)
    def test_1023975(self, drivers, station_type_code, station_type, file_name):
        info = DailyProductionPlan(drivers)
        info.click_import()
        info.fill_form({"2": station_type, "3": os.path.join(BASE_DIR, 'project', 'MES_DAP', 'data', file_name)})
        info.click_upload()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "SELECT count(id) FROM db_pldb_test.line_plan where plan_date = '%s' and station_type "
                                        "= '%s' and line_name = '%s';" % (date.today(), station_type_code,
                                                                          file_name.split('.', 1)[0]))


# @allure.feature("基础信息-日生产计划")
# class TestDownloadDailyProductionPlan:
#     @allure.story("下载导入模板")
#     @allure.title("下载导入模板成功")
#     @allure.description("进入日生产计划>点击【下载模板】按钮")
#     @allure.severity("blocker")
#     def test_290601(self, drivers):
#         info = DailyProductionPlan(drivers)
#         info.click_download(content='planNumImport')
#
#
# @allure.feature("基础信息-日生产计划")
# class TestExportDailyProductionPlan:
#     @allure.story("导出日生产计划")
#     @allure.title("导出当日日生产计划成功")
#     @allure.description("进入日生产计划>日期选择当日>点击查询按钮>点击导出按钮")
#     @allure.severity("blocker")
#     def test_290602(self, drivers):
#         info = DailyProductionPlan(drivers)
#         info.input_date(str(date.today()))
#         info.click_search()
#         info.click_export(content='ExportPlan')


