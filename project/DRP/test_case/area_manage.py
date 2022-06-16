import pytest, sys
from public.data.unified_login.unified import *
from libs.common.assert_ui import DomAssert, SQLAssert, ValueAssert
from public.libs.unified_login.login import Login
from project.DRP.page_object.nav import NavPage
from project.DRP.page_object.user import UserPage
from project.DRP.page_object.area_manage import AreaPage
from libs.common.logger_ui import log

class TestSearchArea:

    # 区域管理树实现
    @pytest.mark.skip
    def test_001(self, drivers):
        """用户管理-查询用户"""
        log.info("{} is start".format(sys._getframe().f_code.co_name))
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部','itel事业部','itel事业部','事业部备料')
        # user.reset_account()

    # @pytest.mark.skip
    def test__002(self, drivers):
        log.info("{} is start".format(sys._getframe().f_code.co_name))
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('TECNO事业部')
        user.download_area("drp_dept_export_TECNO")

    # @pytest.mark.RT
    # def test_002(self, drivers):
    #     """用户管理-新建用户"""
    #     log.info("{} is start".format(sys._getframe().f_code.co_name))
    #     user = UserPage(drivers)
    #     user.append_account("18650893")

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/area_manage.py'])
