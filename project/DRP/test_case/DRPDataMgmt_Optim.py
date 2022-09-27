import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_Optim import Optim


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 DRP数据管理-集成数据管理 页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP数据管理", "集成数据管理")
    dom = DomAssert(drivers)
    dom.assert_url("/dataManage/optim")
    yield
    logging.info("后置条件:关闭 DRP数据管理-集成数据管理 页面")
    user.close_page()
    dom.assert_url("/dashboard")


@allure.feature("DRP数据管理-集成数据管理-前往菜单")
class TestSearchMenu:
    @allure.story("查询集成数据管理菜单")
    @allure.title("按照菜单名称 精确搜索")
    @allure.description("按照菜单名称 精确查询-订单数据 查询结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        optim = Optim(drivers)
        optim.input_menu("精确搜索", "订单数据")
        optim.clear_menuInputBox()

    @allure.story("查询集成数据管理菜单")
    @allure.title("菜单名称搜索框 支持模糊查询")
    @allure.description("按照菜单名称 模糊查询-渠道 查询结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        optim = Optim(drivers)
        optim.input_menu("模糊搜索", "渠道")
        optim.clear_menuInputBox()

    @allure.story("查询集成数据管理菜单")
    @allure.title("菜单名称搜索框 搜索不存在的菜单")
    @allure.description("按照菜单名称 搜索不存在的菜单 菜单列表展示 暂无数据...")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        optim = Optim(drivers)
        optim.input_menu("模糊搜索", "xxx")
        optim.clear_menuInputBox()

    @allure.story("前往集成数据管理菜单")
    @allure.title("搜索一级库存，进入一级库存页面")
    @allure.description("搜索一级库存，进入一级库存页面 页面信息正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_004(self, drivers):
        optim = Optim(drivers)
        optim.input_menu("精确搜索", "一级库存")
        optim.goto_menu("一级库存")
        optim.clear_menuInputBox()

    @allure.story("前往集成数据管理菜单")
    @allure.title("不通过输入搜索，进入一级库存页面")
    @allure.description("不通过输入搜索，进入一级库存页面 页面信息正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_005(self, drivers):
        optim = Optim(drivers)
        optim.goto_menu("一级库存")


@allure.feature("DRP数据管理-集成数据管理")
class TestSearchOptim:
    @allure.story("查询集成数据管理数据")
    @allure.title("进入历史销售数据菜单页，按月时段 查询集成数据管理数据")
    @allure.description("进入历史销售数据菜单页，查询集成数据管理数据 查询结果正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        optim = Optim(drivers)
        optim.goto_menu("历史销售数据")
        optim.choose_monthOrWeek("月时段")
        optim.choose_timeFrame("2021-八月", "2024-三月")
        optim.choose_brand("itel")
        optim.choose_area("国家", "阿联酋")
        optim.choose_matchState("成功")
        optim.choose_inputMobleType("it2160")
        optim.choose_markName("it2160")
        optim.choose_state(option="MP")
        optim.query_button()
        # assertListNum = optim.retrun_listNum()
        # sqlAssert = optim.SQL_assert(time1="202108", time2="202403", brand="itel", modle="it2160", mark="it2160",
        #                              country="阿联酋")
        # ValueAssert.value_assert_equal(assertListNum, sqlAssert)
        optim.reset_button()

    @allure.story("查询集成数据管理数据")
    @allure.title("历史销售数据菜单页，按周时段，查询集成数据管理数据")
    @allure.description("进入历史销售数据菜单页，查询集成数据管理数据 查询结果正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_002(self, drivers):
        optim = Optim(drivers)
        optim.goto_menu("历史销售数据")
        optim.choose_monthOrWeek("周时段")
        optim.choose_timeFrame("2021-八月-12", "2024-三月-5")
        optim.choose_brand("itel")
        optim.choose_area("国家", "阿联酋")
        optim.choose_matchState("成功")
        optim.choose_inputMobleType("it2160")
        optim.choose_markName("it2160")
        optim.choose_state(option="MP")
        optim.query_button()
        # assertListNum = optim.retrun_listNum()
        # sqlAssert = optim.SQL_assert(timeFrame='周时段', time1="2021W32", time2="2024W10", brand="itel", modle="it2160",
        #                              mark="it2160", country="阿联酋")
        # ValueAssert.value_assert_equal(assertListNum, sqlAssert)
        optim.reset_button()

    @allure.story("查询集成数据管理数据")
    @allure.title("进入历史销售数据菜单页，区域支持多选")
    @allure.description("进入历史销售数据菜单页，区域多选，查询集成数据管理数据 查询结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_003(self, drivers):
        optim = Optim(drivers)
        optim.goto_menu("历史销售数据")
        optim.choose_monthOrWeek("月时段")
        optim.choose_timeFrame("2021-八月", "2024-三月")
        optim.choose_brand("itel")
        optim.choose_area(area="全部区域")
        optim.choose_matchState("成功")
        optim.choose_inputMobleType("it2160")
        optim.choose_markName("it2160")
        optim.choose_state(all= "all")
        optim.query_button()
        # assertListNum = optim.retrun_listNum()
        # sqlAssert = optim.SQL_assert(time1="202108", time2="202403", brand="itel", modle="it2160", mark="it2160")
        # ValueAssert.value_assert_equal(assertListNum, sqlAssert)
        optim.reset_button()


@allure.feature("DRP数据管理-集成数据管理")
class TestRestButton:
    @allure.story("重置按钮")
    @allure.title("进入历史销售数据菜单页，按条件查询后，点击重置按钮，按钮功能正常")
    @allure.description("进入历史销售数据菜单页，按条件查询后，点击重置按钮，查询条件清空，页面列表数据恢复到查询前")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        optim = Optim(drivers)
        optim.goto_menu("历史销售数据")
        optim.choose_monthOrWeek("月时段")
        optim.choose_timeFrame("2021-八月", "2024-三月")
        optim.choose_brand("itel")
        optim.choose_area("国家", "阿联酋")
        optim.choose_matchState("成功")
        optim.choose_inputMobleType("it2160")
        optim.choose_markName("it2160")
        optim.choose_state(option="MP")
        optim.query_button()
        beforeListNum = optim.retrun_listNum()
        optim.reset_button()
        afterListNum = optim.retrun_listNum()
        ValueAssert.value_assert_Notequal(beforeListNum, afterListNum)


@allure.feature("DRP数据管理-集成数据管理")
class TestPullData:
    @allure.story("手动拉取按钮")
    @allure.title("进入历史销售数据菜单页，点击手动拉取按钮，功能正常")
    @allure.description("进入历史销售数据菜单页，点击手动拉取按钮，拉取数据正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_001(self, drivers):
        optim = Optim(drivers)
        optim.goto_menu("历史销售数据")
        optim.pull_button()
        optim.choice_period("月时段")
        optim.chooseForm_timeFrame("2022-八月", "2022-九月")
        optim.notarize_button()





if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_Optim.py'])
