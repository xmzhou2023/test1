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

from project.BDDP.page_object.version161__DIP数据管理平台V2_1_2_0 import UserPage
from public.base.assert_ui import DomAssert


@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_2798:
    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("公开无首页卡片池类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30689(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.248.39.163:10100/")#idaac9448f-b803-4887-a254-4292de6b9f6d
        robot.AI_find_element(By.CSS_SELECTOR, ".el-menu--vertical:nth-child(14) .nest-menu:nth-child(1) .el-menu-item").click()#ida76f8c92-7b04-4d10-96b3-469369537b37
        element = robot.AI_find_element(By.CSS_SELECTOR, ".el-menu--vertical:nth-child(14) .nest-menu:nth-child(1) span")#id97eaae4d-a6fd-47e8-8753-4adfd87bf103
        actions = ActionChains(robot)
        actions.move_to_element(element).perform()
        element = robot.AI_find_element(By.CSS_SELECTOR, "body")#idee67642d-901a-4400-b253-490f31db32e7
        actions = ActionChains(robot)
        actions.move_to_element(element, 0, 0).perform()
        robot.AI_find_element(By.CSS_SELECTOR, ".is-opened > .el-submenu__title").click()#idf9464851-9e2f-4cde-88b0-ac8e57cf8a6b
        
        
def test_30921(self, drivers):
        pass


if __name__ == '__main__':
    pass

