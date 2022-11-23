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

from libs.common.time_ui import now_time


@allure.feature("2022年末需求计划")  # 迭代名称
class Teststory_2760:
    @allure.story("高级搜索优化")  # 用户故事名称
    @allure.title("自动化测试跑流程")  # 用例名称
    @allure.description("登录==创建项目")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18778(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://ipm-uat.transsion.com/")
        robot.AI_find_element(By.LINK_TEXT, "项目管理").click()
        robot.AI_find_element(By.XPATH, "//button[contains(.,' 新增')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()
        robot.AI_find_element(By.XPATH, "//img").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(f"UI自动化{now_time}")
        robot.AI_find_element(By.XPATH, "//button[contains(.,'保存')]").click()


    @allure.story("高级搜索优化")  # 用户故事名称
    @allure.title("IPM流程测试")  # 用例名称
    @allure.description("发起==流程审批==断言")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19625(self, drivers):
        pass


if __name__ == '__main__':
      pass
