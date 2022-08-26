import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_PlatformLibrary import PlatformLibrary


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“DRP数据管理-平台库”页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP数据管理", "平台库")
    user = DomAssert(drivers)
    user.assert_url("/dataManage/platformLibrary")


@allure.feature("DRP数据管理-平台库")
class TestSearchPlatform:
    @allure.story("查询平台")
    @allure.title("按照平台条件过滤平台库信息")
    @allure.description("选择平台选项，查询 平台=HK-CKD 的平台库信息")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        platform = PlatformLibrary(drivers)
        platform.screenCondition("平台")
        platform.screenOption("平台", "HK-CKD")
        platform.queryButton()



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_PlatformLibrary.py'])

