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
@allure.feature("V3_0_1计划")  # 迭代名称
class
    @allure.story("新版DRP权限调整切面部分1")  # 用户故事名称
    @allure.title("测试平台11")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记    
    def test_19966(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.112.166:9000//")#id2fec00db-f7f9-4dd4-9795-0a93768c6d55
        robot.close()

    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台1")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18519(self, drivers):
        pass


    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台2")  # 用例名称
    @allure.description("到用户管理页面查询工号==到用户管理页面查询姓名")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18522(self, drivers):
        pass


    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台3")  # 用例名称
    @allure.description("工号查询==姓名查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18540(self, drivers):
        pass


if __name__ == '__main__':
    pass
