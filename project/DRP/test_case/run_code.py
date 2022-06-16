import pytest, sys
from public.data.unified_login.unified import *
from libs.common.assert_ui import DomAssert, SQLAssert
from public.libs.unified_login.login import Login
from project.DRP.page_object.nav import NavPage
from project.DRP.page_object.user import UserPage
from libs.common.logger_ui import log

class TestLogin:

    @pytest.mark.smoke
    def test_001(self, drivers):
        """用户管理-查询用户"""
        log.info("{} is start".format(sys._getframe().f_code.co_name))
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "用户管理")
        user = UserPage(drivers)
        user.search_user(jobnum=account[0]['username'])
        user.reset_account()

    # @pytest.mark.RT
    # def test_002(self, drivers):
    #     """用户管理-新建用户"""
    #     log.info("{} is start".format(sys._getframe().f_code.co_name))
    #     user = UserPage(drivers)
    #     user.append_account("18650893")
    #
    # @pytest.mark.smoke
    # def test_003(self, drivers):
    #     """用户管理-给新用户配置权限"""
    #     log.info("{} is start".format(sys._getframe().f_code.co_name))
    #     user = UserPage(drivers)
    #     user.edit_Permission(
    #         jobnum="18650893",
    #         dimension={
    #             '组织': ['itel事业部', '东非地区部'],
    #             # '品牌': ['Infinix', 'itel', 'TECNO'],
    #             # '区域': {'Infinix': ['利比亚', '土耳其']}
    #         }
    #     )
if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
