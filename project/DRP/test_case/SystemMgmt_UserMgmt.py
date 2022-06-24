import os
import allure
import pytest, sys
from public.data.unified_login.unified import *
from libs.common.assert_ui import DomAssert, SQLAssert, ValueAssert

from project.DRP.page_object.center_Component import NavPage
from project.DRP.page_object.SystemMgmt_UserMgmt import UserPage

@allure.feature("系统管理-用户管理")
class TestSearchUser: # Test+(增，删，改，查，导入（上传），导出（下载）)

    @allure.story("查询用户")
    @allure.title("根据姓名查询用户")
    @allure.description("在输入框输入用户工号'18650617'，进行查询")
    @allure.severity("minor")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        allure.step('步骤细节')
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "用户管理")
        user = UserPage(drivers)
        user.search_user(jobnum=account[0]['username'])

    @allure.story("查询用户")
    @allure.title("重置用户查询条件")
    @allure.description("在输入框输入用户工号或名称，然后重置清除")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        """用户管理-查询用户"""
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "用户管理")
        user = UserPage(drivers)
        user.search_user(jobnum=account[0]['username'])
        user.reset_account()

@allure.feature("系统管理-用户管理")
class TestAppendUser:
    @allure.story("新建用户")
    @allure.title("根据姓名查询用户并添加")
    @allure.description("查询工号为18650893，并添加该用户到系统")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        """用户管理-新建用户"""
        user = UserPage(drivers)
        user.append_account("18650893")

@allure.feature("系统管理-用户管理")
class TestEditUser:
    @allure.story("编辑用户")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_003_001(self, drivers):
        user = UserPage(drivers)
        user.edit_Permission(
            jobnum="18650893",
            dimension={
                '组织': ['itel事业部', '东非地区部'],
                # '品牌': ['Infinix', 'itel', 'TECNO'],
                # '区域': {'Infinix': ['利比亚', '土耳其']}
            }
        )

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])

