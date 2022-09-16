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
import allure
from public.data.unified_login.unified import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.SystemMgmt_UserMgmt import UserPage
@allure.feature("系统管理-用户管理")
class TestSearchUser: # Test+(增，删，改，查，导入（上传），导出（下载）)
    @allure.story("查询用户")
    @allure.title("根据姓名查询用户")
    @allure.description("在输入框输入用户工号18650617,进行查询")
    @allure.severity("minor")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        pass
    @allure.story("查询用户")
    @allure.title("重置用户查询条件")
    @allure.description("在输入框输入用户工号或名称，然后重置清除")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        """用户管理-查询用户"""
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "用户管理")
        user = UserPage(drivers)
        user.search_user(jobnum=account[0]['usernum'])
        user.reset_account()
@allure.feature("系统管理-用户管理")
class TestAppendUser:
    @allure.story("新建用户")
    @allure.title("根据姓名查询用户并添加456")
    @allure.description("查询工号为18650893，并添加该用户到系统")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        drivers.get("http://10.250.113.16/")
        drivers.set_window_size(1936, 1056)
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-menu-item > .el-tooltip")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        drivers.find_element(By.CSS_SELECTOR, ".is-opened .svg-icon").click()
        drivers.find_element(By.CSS_SELECTOR, ".is-opened > .el-submenu__title").click()
        drivers.find_element(By.CSS_SELECTOR, ".el-menu--vertical:nth-child(13) .menu-wrapper:nth-child(4) span").click()
        drivers.find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()
        drivers.find_element(By.CSS_SELECTOR, ".hover").click()
        drivers.find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()
        drivers.find_element(By.CSS_SELECTOR, ".hover").click()
        drivers.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(1) > span").click()
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
