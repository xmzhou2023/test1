import allure
import pytest

from public.base.assert_ui import *
from project.MIP.page_object.Center_Component import NavPage
from project.MIP.page_object.dashboard import dashboard


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 首页 页面")
    menu = NavPage(drivers)
    # menu.click_gotonav("首页")
    dom = DomAssert(drivers)
    dom.assert_url("/dashboard")
    yield
    logging.info("后置条件:返回 首页 页面")
    menu.back_homepage()
    dom.assert_url("/dashboard")


@allure.feature("首页")
class TestChoiceShortcutMenu:
    @allure.story("点击首页快捷菜单，进入指定菜单页面")
    @allure.title("点击首页快捷菜单，进入指定菜单页面")
    @allure.description("点击首页 物料主数据图标，页面跳转至物料主数据页面")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("munuName,url",[("物料主数据","/main-data/material"),("BP 主数据","/main-data/business-partner")
        ,("价格主数据","/main-data/price"),("我的待办","/process-center/myTodo")])
    @pytest.mark.smoke
    def test_001_001(self, drivers,munuName,url):
        menu = dashboard(drivers)
        menu.choice_shortcutMenu(munuName)
        dom = DomAssert(drivers)
        dom.assert_url(url)
        goto_menu = NavPage(drivers)
        goto_menu.back_homepage()


@allure.feature("首页")
class TestSearchMenu:
    @allure.story("搜索菜单")
    @allure.title("搜索菜单，进入指定菜单页面")
    @allure.description("搜索菜单，进入指定菜单页面")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        menu = dashboard(drivers)
        menu.search_menu("审批流设定","系统管理 > 审批流设定")
        dom = DomAssert(drivers)
        dom.assert_url("/sys/approvalFlowSetting")

    @allure.story("搜索菜单")
    @allure.title("模糊搜索菜单，进入指定菜单页面")
    @allure.description("模糊搜索菜单，进入指定菜单页面")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_002(self, drivers):
        menu = dashboard(drivers)
        menu.search_menu("我的","流程中心 > 我的审批")
        dom = DomAssert(drivers)
        dom.assert_url("/process-center/myApproval")

if __name__ == '__main__':
    pytest.main(['project/MIP/testcase/dashboard.py'])
