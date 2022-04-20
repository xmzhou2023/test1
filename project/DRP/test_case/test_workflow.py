import pytest

from libs.common.assert_ui import DomAssert, SQLAssert
from project.DRP.page_object.nav import NavPage
from project.DRP.page_object.user import UserPage
from public_libs.unified_login.login import Login

class TestLogin:
    def test_001(self, drivers):
        """用户管理-登录用户"""
        user = Login(drivers)
        user.login(drivers)
        user = DomAssert(drivers)
        user.assert_att("系统管理")
        user.assert_url("http://10.250.112.166:9000/#/dashboard")
        user = SQLAssert(drivers)
        user.assert_sql(word='刘勇', sql='select name_zh from uc_user where enable_flag=1')

    # def test_002(self, drivers):
    #     """用户管理-查询用户"""
    #     user = NavPage(drivers)
    #     user.click_gotonav("系统管理", "用户管理")
    #     user = UserPage(drivers)
    #     user.search_user(jobnum='18650617')
    #     user.reset_account()
    #
    # def test_003(self, drivers):
    #     """用户管理-新建用户"""
    #     user = UserPage(drivers)
    #     user.append_account("18650617")
    #
    # def test_004(self, drivers):
    #     """用户管理-给新用户配置权限"""
    #     user = NavPage(drivers)
    #     user.click_gotonav("系统管理", "用户管理")
    #     user = UserPage(drivers)
    #     user.edit_Permission(
    #         jobnum="88888888",
    #         dimension={
    #             '组织': ['itel事业部', '东非地区部'],
    #             '品牌': ['Infinix', 'itel', 'TECNO'],
    #             '区域': {'Infinix': ['利比亚', '土耳其']}
    #         }
    #     )
if __name__ == '__main__':
    pytest.main(['test_case/test_login.py'])
