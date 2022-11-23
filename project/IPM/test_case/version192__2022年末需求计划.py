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
@allure.feature("2022年末需求计划")  # 迭代名称
class Teststory_2760:
    @allure.story("高级搜索优化")  # 用户故事名称
    @allure.title("自动化测试跑流程")  # 用例名称
    @allure.description("登录==创建项目")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18778(self, drivers):
        pass


    @allure.story("高级搜索优化")  # 用户故事名称
    @allure.title("IPM流程测试")  # 用例名称
    @allure.description("发起==流程审批==断言")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19625(self, drivers):
        robot = KeyWord(drivers)
        time.sleep(round(timeout / 1000))
        wh_now = robot.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
          return set(wh_now).difference(set(wh_then)).pop()


if __name__ == '__main__':
      pass
