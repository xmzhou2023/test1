import allure
import pytest
from public.base.assert_ui import DomAssert

from project.DRP.page_object.center_Component import NavPage
from project.DRP.page_object.SystemMgmt_RegionMgmt import AreaPage

@allure.feature("系统管理-区域管理")
class TestSearchArea:

    @allure.story("前往区域")
    @allure.title("前往主菜单")
    @allure.description("前往主菜单‘itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user1 = DomAssert(drivers)
        user1.assert_url("/systemManage/areaManage")
        user2 = AreaPage(drivers)
        user2.goto_tree('itel事业部','itel事业部','itel事业部','事业部备料')

    @pytest.mark.RT
    @allure.story("前往区域")
    @allure.title("前往二级菜单")
    @allure.description("前往二级菜单‘itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部','itel事业部')


    @allure.story("前往区域")
    @allure.title("前往三级菜单")
    @allure.description("前往三级菜单‘itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_001_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部','itel事业部','itel事业部')


    @allure.story("前往区域")
    @allure.title("前往四级菜单")
    @allure.description("前往四级菜单‘itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部','itel事业部','itel事业部','事业部备料')

@allure.feature("系统管理-区域管理")
class TestExportArea:

    @allure.story("导出区域")
    @allure.title("导出区域数据")
    @allure.description("导出区域数据‘itel事业部’")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部')
        user.download_area("drp_dept_export_itel")

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/area_manage.py'])

