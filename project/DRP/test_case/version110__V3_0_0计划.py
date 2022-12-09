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
import allure
@allure.feature("V3_0_0计划")  # 迭代名称
class Teststory_1786:
    @allure.story("DRP2国家销售版增加【日志】功能")  # 用户故事名称
    @allure.title("DRP管理DRP2国家销售版增加【日志】功能查看")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gtDRP管理gtDRP2国家销售版进入页面。==选择一条数据，点击【查看】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10565(self, drivers):
        pass


@allure.feature("V3_0_0计划")  # 迭代名称
class Teststory_1811:
    @allure.story("DRP提报批量提交功能支持校验oneworks审批流程是否已经发起")  # 用户故事名称
    @allure.title("DRP提报未发起流程DRP提报批量提交不成功")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gtDRP提报gtDRP提报进入页面。==选择单个已经保存模板未发起审批流程的国家，点击【批量提交】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10573(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.112.166:9000/")#id0fc2a292-ab04-44a8-bb41-7a780c686f8b
        robot.AI_find_element(By.XPATH, "(//button[@type='button'])[6]").click()#id421fb9ad-e01a-411b-9102-40feb4a0a47f



    @allure.story("DRP提报批量提交功能支持校验oneworks审批流程是否已经发起")  # 用户故事名称
    @allure.title("DRP提报未发起流程DRP提报批量提交部分国家未提交审批流程")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gtDRP提报gtDRP提报进入页面==选择多个已经保存的提报模板，其中有未发起审批流程的国家，点击【批量提交】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10575(self, drivers):
        pass


if __name__ == '__main__':
    pass
