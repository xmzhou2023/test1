import os
import time
from libs.config.conf import BASE_DIR
from project.MES_DAP.page_object.DataQuerry_SoftwareOfflineUpgradeTable import SoftwareOfflineUpgradele
from project.MES_DAP.page_object.Center_Component import NavPage, PageInfo, ReadData
from project.MES_DAP.test_case.conftest import pro_name
from public.base.assert_ui import DomAssert, SQLAssert
import pytest
import logging
import allure


@pytest.fixture(scope="module", autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往“数据查询-软件离线升级跟踪表”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("数据查询", "软件离线升级跟踪表")
    result = DomAssert(drivers)
    result.assert_url("/dataQuery/offlineUpgrade")


@allure.feature("数据查询-软件离线升级跟踪表")
class TestSearchSoftwareOfflineUpgradeLog:
    @allure.story("查询软件离线升级记录")
    @allure.title("必填条件为空查询失败")
    @allure.description("必填条件（品牌、项目、主板、机型）为空查询")
    @allure.severity("blocker")
    @pytest.mark.parametrize("brand, project, pcba, model", [('', '', '', ''), ('Infinix', '', '', ''), ('Infinix', 'X556_H371', '', ''), ('Infinix', 'X556_H371', 'H371', '')])
    def test_292101(self, drivers, brand, project, pcba, model):
        data = SoftwareOfflineUpgradele(drivers)
        data.choice_brand(brand)
        data.choice_project(project)
        data.choice_pcba(pcba)
        data.choice_model(model)
        data.click_search()
        dom = DomAssert(drivers)
        dom.assert_att("不能为空")

    values = ReadData().read_excel(os.path.join(BASE_DIR, 'project', 'MES_DAP', 'data', 'parametrize.xls'), 'SoftwareOfflineUpgradeLog', 'row', rows=1)
    @allure.story("查询软件离线升级记录")
    @allure.title("必填条件不为空，正确返回查询结果")
    @allure.description("选择必填条件：品牌、PCBA》依次选择其他条件查询")
    @allure.severity("blocker")
    @pytest.mark.parametrize("brand, project, pcba, model, start_date, end_date, sn, sql", values)
    def test_292102(self, drivers, brand, project, pcba, model, sn, start_date, end_date, sql):
        data = SoftwareOfflineUpgradele(drivers)
        data.click_reset()
        data.choice_brand(brand)
        data.choice_project(project)
        data.choice_pcba(pcba)
        data.choice_model(model)
        data.input_sn(sn)
        data.choice_start_date(start_date)
        data.choice_end_date(end_date)
        data.click_search()
        count = PageInfo(drivers).get_count()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(count, sql)


