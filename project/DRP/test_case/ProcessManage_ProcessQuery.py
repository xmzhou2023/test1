import logging

import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.ProcessManage_ProcessQuery import ProcessQuery


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 DRP流程管理-流程查询 页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP流程管理", "流程查询")
    dom = DomAssert(drivers)
    dom.assert_url("/processManage/processQuery")
    yield
    logging.info("后置条件:关闭 DRP流程管理-流程查询 页面")
    user.close_page()
    dom.assert_url("/dashboard")


@allure.feature("DRP流程管理-流程查询")
class TestSearchProcess:
    @allure.story("查询流程")
    @allure.title("选择流程分类查询")
    @allure.description("选择流程分类查询，查询结果正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        process = ProcessQuery(drivers)
        beforeListNum = process.return_listNum()
        process.choice_queryCondition("流程分类","itel事业部")
        process.query_button()
        afterListNum = process.return_listNum()
        ValueAssert.value_assert_Notequal(beforeListNum,afterListNum)
        # 清空查询条件
        process.reset_button()

    @allure.story("查询流程")
    @allure.title("维护所有查询条件 查询")
    @allure.description("维护所有查询条件 ，查询结果正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        process = ProcessQuery(drivers)
        beforeListNum = process.return_listNum()
        process.choice_queryCondition("流程分类","TECNO事业部")
        process.choice_queryCondition("流程名称","TECNO事业部巴基斯坦审批")
        process.choice_queryCondition("节点名称","巴基斯坦-TECNO品牌经理")
        process.choice_queryCondition("节点类型","提报节点")
        process.choice_queryCondition("品牌","TECNO")
        process.choice_queryCondition("国家","巴基斯坦")
        process.choice_queryCondition("负责人","邓佳鑫")
        process.choice_queryCondition("系统角色","品牌经理")
        process.query_button()
        afterListNum = process.return_listNum()
        ValueAssert.value_assert_Notequal(beforeListNum,afterListNum)
        # 清空查询条件
        process.reset_button()

    @allure.story("查询流程")
    @allure.title("[异常]查询结果为空 列表显示暂无数据")
    @allure.description("[异常]查询结果为空 列表显示暂无数据")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        process = ProcessQuery(drivers)
        process.choice_queryCondition("流程分类","TECNO事业部")
        process.choice_queryCondition("品牌","TECNO")
        process.choice_queryCondition("国家","贝宁")
        process.query_button()
        afterListNum = process.return_listNum()
        assert afterListNum == 0,logging.warning("页面列表数据，断言失败，查询结果{}不等于0".format(afterListNum))
        logging.info("页面列表数据，断言成功，查询结果{}等于0".format(afterListNum))
        txt = process.assert_listNum_Null()
        assert txt == "暂无数据",logging.warning("页面列表数据，断言失败，查询结果{}不是 暂无数据".format(txt))
        logging.info("页面列表数据，断言成功，查询结果{}等于 暂无数据".format(txt))
        # 清空查询条件
        process.reset_button()


@allure.feature("DRP流程管理-流程查询")
class TestResetFunction:
    @allure.story("重置按钮功能")
    @allure.title("点击重置按钮，清空查询条件，列表显示全部数据")
    @allure.description("点击重置按钮，清空查询条件，列表显示全部数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        process = ProcessQuery(drivers)
        beforeListNum = process.return_listNum()
        process.choice_queryCondition("流程分类","TECNO事业部")
        process.choice_queryCondition("品牌","TECNO")
        process.choice_queryCondition("国家","贝宁")
        process.query_button()
        process.reset_button()
        afterListNum = process.return_listNum()
        ValueAssert.value_assert_equal(beforeListNum,afterListNum)


@allure.feature("DRP流程管理-流程查询")
class TestExportFunction:
    @allure.story("导出按钮功能")
    @allure.title("点击导出按钮，导出全部流程信息，列表显示全部数据")
    @allure.description("点击重置按钮，情况查询条件，列表显示全部数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.skip
    def test_003_001(self, drivers):
        process = ProcessQuery(drivers)
        process.export_button("process_info_export")

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/ProcessManage_ProcessQuery.py'])
