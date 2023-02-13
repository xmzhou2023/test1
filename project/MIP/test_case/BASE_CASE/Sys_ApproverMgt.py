import allure
import pytest

from public.base.assert_ui import *
from project.MIP.page_object.Center_Component import NavPage
from project.MIP.page_object.Sys_ApproverMgt import SysApproverMgt


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 系统管理-审批人管理 页面")
    menu = NavPage(drivers)
    menu.click_gotonav("系统管理", "审批人管理")
    dom = DomAssert(drivers)
    dom.assert_url("/sys/approverMgt")
    yield
    logging.info("后置条件:返回 首页 页面")
    menu.back_homepage()
    dom.assert_url("/dashboard")


@allure.feature("系统管理-审批人管理")
class TestQueryApproverMgt:
    @allure.story("查询功能验证")
    @allure.title("输入查询项，查询结果正确")
    @allure.description("输入查询项，查询结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        set = SysApproverMgt(drivers)
        set.choice_brand("TECNO")
        set.choice_organization("地区部")
        set.input_approver("隆江")
        set.choice_approveNode("国家经理")
        set.choice_area("阿联酋")
        set.button_query()
        listNum = set.get_listNum()
        ValueAssert.value_assert_equal(listNum, 1)
        set.button_reset()


@allure.feature("系统管理-审批人管理")
class TestAddApproverMgt:
    @allure.story("新增功能验证")
    @allure.title("新建审批人信息，新增保存成功")
    @allure.description("新建审批人信息，新增保存成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        set = SysApproverMgt(drivers)
        set.button_Add()
        set.edit_approverinf("INFINIX", "地区部", "阿富汗", "国家经理", "隆江")
        set.button_save()
        listNum = set.query_testdata(drivers, "INFINIX", "地区部", "隆江", "国家经理", "阿富汗")
        sqlNum = set.get_sqlResult(
            "select count(*) from process_user_manage WHERE node_name = '国家经理' and approve_user_name "
            "='隆江' and brand_code ='02' and country_code ='AF' and group_id = '1';")
        ValueAssert.value_assert_equal(sqlNum, listNum)
        set.button_reset()
        set.clear_testData("国家经理", "隆江", "INFINIX", "阿富汗", "地区部")

    @allure.story("新增功能验证")
    @allure.title("[异常]必填项未维护，新增失败")
    @allure.description("必填项未维护，新增失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("brand, group, area, nodeName, approver",
                             [("", "", "", "", ""), ("INFINIX", "", "", "", ""), ("INFINIX", "地区部", "", "", ""),
                              ("INFINIX", "地区部", "阿富汗", "", ""), ("INFINIX", "地区部", "阿富汗", "国家经理", "")])
    @pytest.mark.smoke
    def test_002_002(self, drivers, brand, group, area, nodeName, approver):
        set = SysApproverMgt(drivers)
        set.button_Add()
        set.edit_approverinf(brand, group, area, nodeName, approver)
        set.button_save()


@allure.feature("系统管理-审批人管理")
class TestEditApproverMgt:
    @allure.story("编辑功能验证")
    @allure.title("编辑审批人信息，编辑保存成功")
    @allure.description("编辑审批人信息，编辑保存成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        set = SysApproverMgt(drivers)
        set.creat_testdata(drivers,"INFINIX", "地区部", "阿富汗", "国家经理", "隆江")
        set.query_testdata(drivers, "INFINIX", "地区部", "隆江", "国家经理", "阿富汗")
        set.button_edit()
        set.edit_approverinf("ITEL", "", "", "", "")
        set.button_save()
        set.button_reset()
        listNum = set.query_testdata(drivers, "ITEL", "地区部", "隆江", "国家经理", "阿富汗")
        sqlNum = set.get_sqlResult(
            "select count(*) from process_user_manage WHERE node_name = '国家经理' and approve_user_name "
            "='隆江' and brand_code ='03' and country_code ='AF' and group_id = '1';")
        ValueAssert.value_assert_equal(sqlNum, listNum)
        set.button_reset()
        set.clear_testData("国家经理", "隆江", "ITEL", "阿富汗", "地区部")
