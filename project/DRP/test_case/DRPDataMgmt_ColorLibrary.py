import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_ColorLibrary import ColorLibrary


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“DRP数据管理-颜色库”页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP数据管理", "颜色库")
    user = DomAssert(drivers)
    user.assert_url("/dataManage/colorLibrary")


@allure.feature("DRP数据管理-颜色库")
class TestSearchColor:
    @allure.story("查询颜色")
    @allure.title("按照颜色条件过滤颜色库信息")
    @allure.description("输入颜色，查询 颜色=123 的颜色库信息")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        color = ColorLibrary(drivers)
        color.screenOption("颜色","123")
        color.queryButton()
        # color.screenAssert("颜色","123")



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_ColorLibrary.py'])
