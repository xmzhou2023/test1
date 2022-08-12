# -*- coding: utf-8 -*-
# @Time    : 2022-08-02 17:15
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : BasicInfo_BoardParametersSetting.py
# @Software: PyCharm
import allure
from project.MES_DAP.page_object.BasicInfo_BoardUserSetting import BoardUserSetting
from project.MES_DAP.page_object.Center_Component import *
from public.base.assert_ui import *
from project.MES_DAP.test_case.conftest import *
import logging
import os


@pytest.fixture(scope='module', autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往“基础信息-看板人员维护”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("基础信息", "看板人员维护")
    result = DomAssert(drivers)
    result.assert_url("/basicData/BoardPeroson")


@allure.feature("基础信息-看板人员维护")
class TestSearchBoardUserSetting:
    @allure.story("查询看板人员")
    @allure.title("条件为空查询信息")
    @allure.description("进入看板人员>点击查询按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1029070(self, drivers):
        info = BoardUserSetting(drivers)
        info.click_search()
        db = SQLAssert(pro_name, 'test')
        page = PageInfo(drivers)
        page_count = page.get_count()
        db.assert_sql_count(page_count, "SELECT count(EMP_ID) FROM db_pldb_test.dt_pv_employees WHERE ORG_ID like "
                                        "'1000%' and DUTY_ID like '600%';")


@allure.feature("基础信息-看板人员维护")
class TestInsertBoardUserSetting:
    @allure.story("新增看板人员")
    @allure.title("所有字段正确填写，新增看板人员成功")
    @allure.description("进入看板人员维护>点击新增按钮>正确填写所有内容>上传图片>保存")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1029050(self, drivers):
        info = BoardUserSetting(drivers)
        info.click_insert()
        print(os.path.join(os.path.join(os.path.abspath('..'),'data'),'headimg.jpeg'))
        info.fill_form({"1": "19950109", "2": "测试", "3": "1888888888", "4": "组装产线",
                        "5": "拉长", "6": os.path.join(os.path.abspath('.'), 'project/MES_DAP/data/headimg.jpeg')})
        info.click_form_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(1, "SELECT count(EMP_ID) FROM db_pldb_test.dt_pv_employees WHERE EMP_CODE ='19950109';")


@allure.feature("基础信息-看板人员维护")
class TestDelBoardUserSetting:
    @allure.story("删除看板人员")
    @allure.title("查询后删除")
    @allure.description("进入看板参数配置>选择查询条件>点击查询按钮>点击删除按钮>确认")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1029059(self, drivers):
        info = BoardUserSetting(drivers)
        info.input_job_number("19950109")
        info.input_name("测试")
        info.choice_post("拉长")
        info.click_search()
        info.click_del('1')
        info.click_del_accept()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(0, "SELECT count(EMP_ID) FROM db_pldb_test.dt_pv_employees WHERE EMP_CODE ='19950109';")


@allure.feature("基础信息-看板人员维护")
class TestExportBoardUserSetting:
    @allure.story("导出看板人员")
    @allure.title("全量导出看板人员")
    @allure.description("进入看板人员维护>重置查询条件>查询全量数据>点击导出按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_1029085(self, drivers):
        info = BoardUserSetting(drivers)
        info.click_reset()
        info.click_search()
        info.click_export(content="ExportUser")