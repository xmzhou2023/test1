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
class Teststory_2467:
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
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.112.166:9000/")#id9c450b4f-685c-4e6c-9e8b-36273affc754
        robot.AI_find_element(By.CSS_SELECTOR, ".is-opened > .el-submenu__title").click()#id452b3fde-abeb-411c-8269-b4a2a6321f27
        robot.AI_find_element(By.CSS_SELECTOR, ".el-menu--vertical:nth-child(10) .nest-menu:nth-child(1) span").click()#id6d83538a-592a-49c3-97ba-037e2e16cd2c
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()#id7d1b41b7-baa7-4964-bee4-7bf91dc80c6b
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").send_keys("1865")#id54728dce-691d-40ad-9cd5-fa358910249d
        robot.AI_find_element(By.CSS_SELECTOR, ".hover").click()#id98b7f60f-f0ad-4296-abdd-cf6e80f48f36
        robot.AI_find_element(By.CSS_SELECTOR, ".tr-form-item__operate > .is-plain > span").click()#id6dc82c0c-f823-476b-9fc1-b6daff87b1de
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()#id08c13a00-46fd-4c2d-92a6-92681de58a16
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").send_keys("黄")#idbf971a87-8b37-49e4-aa08-ffc92e0322d2
        robot.AI_find_element(By.CSS_SELECTOR, ".hover:nth-child(2)").click()#id2d74f0d2-edcd-4356-83fd-14582d33efa1
        robot.AI_find_element(By.CSS_SELECTOR, ".tr-form-item__operate > .is-plain > span").click()#id692e7ff6-1c20-4432-adc2-070ff733b8af


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
