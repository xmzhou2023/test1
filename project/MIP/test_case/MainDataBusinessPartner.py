import logging

import allure
import pytest

from public.base.assert_ui import *
from project.MIP.page_object.Center_Component import NavPage
from project.MIP.page_object.MainDataBusinessPartner import MainDataBusinessPartner


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 主数据-BP 主数据 页面")
    menu = NavPage(drivers)
    menu.click_gotonav("主数据","BP 主数据")
    dom = DomAssert(drivers)
    dom.assert_url("/main-data/business-partner")
    yield
    logging.info("后置条件:返回 首页 页面")
    menu.back_homepage()
    dom.assert_url("/dashboard")


@allure.feature("主数据-BP主数据")
class TestQueryBPData:
    @allure.story("查询功能验证")
    @allure.title("正确录入查询条件，查询BP主数据结果正确")
    @allure.description("正确录入查询条件，查询BP主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        data = MainDataBusinessPartner(drivers)
        data.button_spread()
        data.choice_BPType('0002')
        data.input_BPCode(itemL="CC00000001", itemR="CC00000010")
        data.choice_region('中国')
        data.input_BPName('深圳市鸣合联科技有限公司')
        data.input_contacts('朱凤林')
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(partner_code) from bb_partner where partner_code BETWEEN 'CC00000001' AND 'CC00000010' "
                                    "and partner_name = '深圳市鸣合联科技有限公司' and linker ='朱凤林' and country_code = 'CN'")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_spread()
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("[异常]不选择BP类型，查询失败")
    @allure.description("不选择BP类型，查询失败")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        data = MainDataBusinessPartner(drivers)
        data.button_spread()
        data.choice_BPType()


@allure.feature("主数据-BP主数据")
class TestQueryViewDetails:
    @allure.story("查看详情功能")
    @allure.title("单选BP数据，进入详情页成功")
    @allure.description("单选BP数据CC00000001，进入详情页成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        data = MainDataBusinessPartner(drivers)
        data.button_spread()
        data.choice_BPType('0002')
        data.input_BPCode(itemL="CC00000001",scene="单一物料查询")
        data.button_query()
        data.select_itemData()
        data.button_viewDetails()
        dom = DomAssert(drivers)
        dom.assert_url("/main-data/bpDetail")
        BPCode = data.return_BPCode()
        assert BPCode == "CC00000001",logging.warning("断言失败")
        logging.info("断言成功，详情页BP编码与列表页一致：{}".format(BPCode))
        data.return_BPMianDataPage()

    @allure.story("查看详情功能")
    @allure.title("多选BP数据，进入详情页成功")
    @allure.description("多选BP数据“CC00000001--CC00000010”，进入详情页成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_002(self, drivers):
        data = MainDataBusinessPartner(drivers)
        data.button_spread()
        data.choice_BPType('0002')
        data.input_BPCode(itemL="CC00000001", itemR="CC00000010")
        data.button_query()
        data.select_itemData("全选")
        data.button_viewDetails()
        dom = DomAssert(drivers)
        dom.assert_url("/main-data/bpDetail")
        data.return_BPMianDataPage()

    @allure.story("查看详情功能")
    @allure.title("点击列表中的BP编码，进入详情页成功")
    @allure.description("点击列表中的BP编码CC00000002，进入详情页成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_003(self, drivers):
        data = MainDataBusinessPartner(drivers)
        data.button_spread()
        data.choice_BPType('0002')
        data.input_BPCode(itemL="CC00000002",scene="单一物料查询")
        data.button_query()
        data.hyperlink_BPCode('CC00000002')
        dom = DomAssert(drivers)
        dom.assert_url("/main-data/bpDetail")
        BPCode = data.return_BPCode()
        assert BPCode == "CC00000002",logging.warning("断言失败")
        logging.info("断言成功，详情页BP编码与列表页一致：{}".format(BPCode))
        data.return_BPMianDataPage()

if __name__ == '__main__':
    pytest.main(['project/MIP/testcase/MainDataBusinessPartner.py'])