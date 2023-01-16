import os

from libs.config.conf import BASE_DIR
from project.MES_DAP.page_object.StatisticalAnalysis_ProjectFPY import ProjectFPY
from project.MES_DAP.page_object.Center_Component import NavPage, PageInfo, ReadData
from project.MES_DAP.test_case.conftest import pro_name
from public.base.assert_ui import DomAssert, SQLAssert, ValueAssert
import pytest
import logging
import allure
import arrow


@pytest.fixture(scope='module', autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往“统计分析-项目直通率”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("统计分析", "项目直通率")
    result = DomAssert(drivers)
    result.assert_url("/dataCenter/ProjectRty")


@allure.feature("统计分析-项目直通率")
class TestQueryProjectFPY:
    query_data = ReadData().read_excel(os.path.join(BASE_DIR, 'project', 'MES_DAP', 'data', 'parametrize.xls'), 'ProjectFPY-Query', 'row', rows=1)
    @allure.story("查询项目直通率")
    @allure.title("必填条件为空，查询失败")
    @allure.description("必填条件为空》查询")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize('workshop_section, start_time, end_time, station, tips', query_data)
    def test_292201(self, drivers, workshop_section, start_time, end_time, station, tips):
        info = ProjectFPY(drivers)
        info.click_reset()
        info.choice_workshop_section(workshop_section)
        info.choice_start_date(str(eval(start_time)) if start_time else start_time)
        info.choice_end_date(str(eval(end_time)) if end_time else end_time)
        info.choice_station(station)
        info.click_search()
        dom = DomAssert(drivers)
        dom.assert_att(tips)

    @allure.story("查询项目直通率")
    @allure.title("按工段、站点、项目查询当日项目直通")
    @allure.description("选择查询条件>点击查询按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("workshop_section, station, project", [("PCBA", "BTI", "H371"), ("组装", "RTI", "X556_H371"), ("包装", "GBL", "X556")])
    def test_290901(self, drivers, workshop_section, station, project):
        info = ProjectFPY(drivers)
        info.click_reset()
        info.choice_workshop_section(workshop_section)
        info.choice_start_date(str(arrow.now().shift(months=-1))[0:10])
        info.choice_end_date(str(arrow.now())[:10])
        info.choice_station(station)
        info.choice_project(project)
        info.click_search()
        page = PageInfo(drivers)
        page_count = page.get_count()
        logging.info(page_count)
        ValueAssert.value_assert_equal(page_count, 1)


@allure.feature("统计分析-项目直通率")
class TestCheckFormData:
    test_data = ReadData().read_excel(os.path.join(BASE_DIR, 'project', 'MES_DAP', 'data', 'parametrize.xls'),
                                       'ProjectFPY_Data', 'row', rows=1)
    @allure.story("查询项目直通率")
    @allure.title("检查各工段半年内某一项目某一站点数据正确性")
    @allure.description("选择查询条件>点击查询按钮>检查列表数据正确性")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("workshop_section, station, project, title, sql", test_data)
    def test_290902(self, drivers, workshop_section, station, project, title, sql):
        info = ProjectFPY(drivers)
        info.click_reset()
        info.choice_workshop_section(workshop_section)
        info.choice_start_date(str(arrow.now().shift(months=-1))[0:10])
        info.choice_end_date(str(arrow.now())[:10])
        info.choice_station(station)
        info.choice_project(project)
        info.click_search()
        value = info.get_cols_values(title)
        db = SQLAssert(pro_name, 'test')
        logging.info(eval(sql))
        for i in range(len(value[title])):
            db.assert_sql(value[title][i], eval(sql))