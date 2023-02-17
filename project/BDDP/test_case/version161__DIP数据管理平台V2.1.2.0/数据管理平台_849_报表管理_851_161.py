import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from libs.common.action import KeyWord
from datetime import datetime
import allure
from project.BDDP.page_object.数据管理平台_卡片管理 import kapianguanli
from public.base.assert_ui import DomAssert


@allure.feature("数据管理平台_849_报表管理_851")  # 迭代名称
class Teststory_2499:
    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("新建无首页卡片池的角色功能验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击角色管理新建;步骤3:输入角色名称;步骤4:输入角色说明;步骤5:拥有首页卡片池否;步骤6:选择菜单报表授权;步骤7:输入关联用户;步骤8:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30917(self, drivers):
        user = kapianguanli(drivers)
        user.click_system()
        user.click_role()
        user.click_add()
        user.click_rolename()
        time.sleep(1)
        user.click_describe()
        time.sleep(1)
        user.click_menubar()
        user.click_menubar1()
        user.click_savereport()
        user.click_user()
        user.click_user1()
        user.click_user2()
        user.click_user3()
        user.click_save()
        DomAssert(drivers).assert_att("添加角色成功")
        time.sleep(2)
        user.click_rolereset()
        user.click_deleterole()
        user.click_close_role()
        time.sleep(2)
        user.click_close_tables()


    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("新建有首页卡片池的角色功能验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击角色管理新建;步骤3:输入角色名称;步骤4:输入角色说明;步骤5:拥有首页卡片池是;步骤6:选择菜单报表授权;步骤7:输入关联用户;步骤8:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30918(self, drivers):
        time.sleep(20)
        user = kapianguanli(drivers)
        user.click_system()
        user.click_role()
        user.click_add()
        time.sleep(1)
        user.click_rolename()
        time.sleep(1)
        user.click_describe()
        time.sleep(1)
        user.click_menubar()
        user.click_menubar1()
        user.click_savereport()
        user.click_user()
        user.click_user1()
        user.click_user2()
        user.click_user3()
        user.click_home_card()
        user.click_home_card1()
        user.click_select()
        user.click_home_card2()
        user.click_save()
        DomAssert(drivers).assert_att("添加角色成功")
        time.sleep(2)
        user.click_rolereset()
        user.click_deleterole()
        user.click_close_role()
        time.sleep(2)
        user.click_close_tables()


    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("修改角色功能验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:选择已有的角色，点击编辑;步骤3:修改角色名称;步骤4:修改角色说明;步骤5:修改拥有首页卡片池否;步骤6:修改菜单报表授权;步骤7:修改关联用户;步骤8:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30919(self, drivers):
        time.sleep(20)
        user = kapianguanli(drivers)
        user.click_system()
        user.click_role()
        user.click_add()
        time.sleep(1)
        user.click_rolename()
        time.sleep(1)
        user.click_describe()
        time.sleep(1)
        user.click_menubar()
        user.click_menubar1()
        user.click_savereport()
        user.click_user()
        user.click_user1()
        user.click_user2()
        user.click_user3()
        user.click_home_card()
        user.click_home_card1()
        user.click_select()
        user.click_home_card2()
        user.click_save()
        DomAssert(drivers).assert_att("添加角色成功")
        user.click_edit_role()
        user.click_user()
        user.click_user1()
        user.click_user02()
        user.click_user2()
        user.click_user3()
        user.click_save()
        DomAssert(drivers).assert_att("修改成功")
        time.sleep(2)
        user.click_rolereset()
        user.click_deleterole()
        user.click_close_role()
        time.sleep(2)
        user.click_close_tables()


    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("删除角色功能验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:选择已有的角色，点击编辑;步骤3:点击删除;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30920(self, drivers):
        time.sleep(20)
        user = kapianguanli(drivers)
        user.click_system()
        user.click_role()
        user.click_add()
        time.sleep(1)
        user.click_rolename()
        time.sleep(1)
        user.click_describe()
        time.sleep(1)
        user.click_menubar()
        user.click_menubar1()
        user.click_savereport()
        user.click_user01()
        time.sleep(2)
        user.click_paste()
        time.sleep(2)
        user.click_paste1()
        time.sleep(1)
        user.click_paste2()
        user.click_save()
        DomAssert(drivers).assert_att("添加角色成功")
        time.sleep(2)
        user.click_rolereset()
        user.click_deleterole()
        user.click_close_role()
        time.sleep(2)
        user.click_close_tables()


    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("角色类型搜索功能验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击角色搜索框;步骤3:输入搜索字段;步骤4:点击搜索;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30921(self, drivers):
        # time.sleep(20)
        user = kapianguanli(drivers)
        user.click_system()
        user.click_role()
        user.click_search_role()
        user.click_search_role1()
        user.click_close_role()
        time.sleep(2)
        user.click_close_tables()


if __name__ == '__main__':
    pass
