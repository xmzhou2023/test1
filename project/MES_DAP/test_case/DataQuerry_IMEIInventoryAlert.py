import time

from libs.config.conf import BASE_DIR
from project.MES_DAP.page_object.DataQuerry_IMEIInventoryAlert import IMEIInventoryAlert
from project.MES_DAP.page_object.Center_Component import NavPage, PageInfo, ReadData
from project.MES_DAP.test_case.conftest import pro_name
from public.base.assert_ui import DomAssert, SQLAssert
import pytest
import logging
import allure
from datetime import date


@pytest.fixture(scope="module", autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往“数据查询-码段库存预警”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("数据查询", "码段库存预警")
    result = DomAssert(drivers)
    result.assert_url("/dataQuery/codeWaning")


@allure.feature("数据查询-码段库存预警")
class TestCheckIMEIInventoryAlert:
    @allure.story("检查码段库存预警列表内容")
    @allure.title("不选择日期，校验指定项目IMEI总数、库存数")
    @allure.description("切换tab到IMEI库存预警》选择项目》查询》检查该项目IMEI总数、库存数")
    @allure.severity("blocker")
    @pytest.mark.parametrize("check_col", ["IMEI总数", "IMEI库存数"])
    def test_291601(self, drivers, check_col):
        info = IMEIInventoryAlert(drivers)
        info.switch_tab("IMEI库存预警")
        info.click_reset("pane-first")
        info.choice_project("pane-first", "X556_H371")
        info.click_search("pane-first")
        time.sleep(2)
        values = info.get_cols_values("市场", "频段配置", check_col, tab="pane-first")
        db = SQLAssert(pro_name, 'test')
        for i in range(len(values[check_col])):
            if check_col == "IMEI总数":
                db.assert_sql(values[check_col][i], "select count(xhir.IMEI1) from db_pldb_test.x556_h371_imei_record xhir "
                                                "join db_pldb_test.t_bb_basedata tbb on xhir.market = tbb.ITEM_NO where "
                                                "tbb.NAME = '%s' and xhir.band_config = '%s';" % (values["市场"][i],
                                                                                                  values["频段配置"][i]))
            elif check_col == "IMEI库存数":
                db.assert_sql(values[check_col][i], "select count(xhir.IMEI1) from db_pldb_test.x556_h371_imei_record xhir "
                                                "join db_pldb_test.t_bb_basedata tbb on xhir.market = tbb.ITEM_NO where "
                                                "tbb.NAME = '%s' and xhir.band_config = '%s' and xhir.is_print = 0;" % (
                                                                                values["市场"][i], values["频段配置"][i]))

    @allure.story("检查码段库存预警列表内容")
    @allure.title("不选择日期，校验指定项目MAC总数、库存数")
    @allure.description("切换tab到MAC库存预警》选择项目》查询》检查该项目MAC总数")
    @allure.severity("blocker")
    @pytest.mark.parametrize("title", ["MAC总数", "MAC库存数"])
    def test_291602(self, drivers, title):
        info = IMEIInventoryAlert(drivers)
        info.switch_tab("MAC库存预警")
        info.click_reset("pane-second")
        info.choice_project("pane-second", "X556_H371")
        info.click_search("pane-second")
        time.sleep(2)
        values = info.get_cols_values("项目名", title, tab="pane-second")
        db = SQLAssert(pro_name, 'test')
        for i in range(len(values[title])):
            if title == "MAC总数":
                db.assert_sql(values[title][i], "select count(Wifi_MAC) from db_pldb_test.x556_h371_mac_record xhmr;")
            elif title == "MAC库存数":
                db.assert_sql(values[title][i], "select count(Wifi_MAC) from db_pldb_test.x556_h371_mac_record xhmr where write_time is null and SN = '';")

    @allure.story("检查码段库存预警列表内容")
    @allure.title("不选择日期，校验指定项目Chipid总数、库存数")
    @allure.description("切换tab到Chipid库存预警》选择项目》查询》检查该项目Chipid总数")
    @allure.severity("blocker")
    @pytest.mark.parametrize("check_col", ["Chipid总数", "Chipid库存数"])
    def test_291603(self, drivers, check_col):
        info = IMEIInventoryAlert(drivers)
        info.switch_tab("Chipid库存预警")
        info.click_reset("pane-third")
        info.choice_project("pane-third", "X556_H371")
        info.click_search("pane-third")
        time.sleep(2)
        values = info.get_cols_values("项目名", check_col, tab="pane-third")
        db = SQLAssert(pro_name, 'test')
        for i in range(len(values[check_col])):
            if check_col == "Chipid总数":
                db.assert_sql(values[check_col][i], "select count(Chipid) from db_pldb_test.x556_h371_Chipid;")
            elif check_col == "Chipid库存数":
                db.assert_sql(values[check_col][i], "select count(Chipid) from db_pldb_test.x556_h371_Chipid where SN = '';")