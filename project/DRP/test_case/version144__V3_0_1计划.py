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
    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台1")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18519(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.112.166:9000/")
        robot.AI_find_element(By.XPATH, "(//button[@type='button'])[6]").click()


    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台2")  # 用例名称
    @allure.description("到用户管理页面查询工号==到用户管理页面查询姓名")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18522(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.112.166:9000/")
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div/div[2]/div/div/ul/div[11]/li/div").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'用户管理')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("1865")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'18653013')]").click()
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/section/div/div/div/form/div/div[3]/button[2]/span").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("黄")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'黄曦蓉')]").click()
        robot.AI_find_element(By.XPATH, "(//button[@type='button'])[7]").click()


    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台3")  # 用例名称
    @allure.description("工号查询==姓名查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18540(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.112.166:9000/")#idf2d0d4b2-8856-43ca-88fc-4289f9a1a177
        robot.AI_find_element(By.CSS_SELECTOR, ".is-opened span").click()#id05432658-1de0-41d1-9c77-5b2f202e5125
        robot.AI_find_element(By.CSS_SELECTOR, ".el-menu--vertical:nth-child(10) .nest-menu:nth-child(1) span").click()#id7522501d-0e13-43bc-ae0e-0214c785668f
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()#id7ac6ae77-2920-4504-8f07-ebaf1494e7a6
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").send_keys("1865")#id7b7df69a-5670-4fb0-a58f-b31f29d9d7eb
        robot.AI_find_element(By.CSS_SELECTOR, ".hover > span").click()#id44cf6396-db87-4e69-b252-a41802f0d340
        robot.AI_find_element(By.CSS_SELECTOR, ".tr-form-item__operate > .is-plain > span").click()#id93fc1e7e-f9f7-4e08-94e3-fe09e933270e
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()#id9b3dbfca-d62f-46a0-8385-7c871893c340
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").send_keys("黄")#ida23ea0da-dba2-4cde-ac1b-e853d97b1f47
        robot.AI_find_element(By.CSS_SELECTOR, ".hover:nth-child(4)").click()#id760afec1-5819-4ef5-9a37-1e4e62cffc14
        robot.AI_find_element(By.CSS_SELECTOR, ".tr-form-item__operate > .is-plain > span").click()#ide0d55e0a-7f50-4af1-b440-9ad9c4e54e55


    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台4")  # 用例名称
    @allure.description("查询工号==查询姓名")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19966(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.112.166:9000//")
        robot.close()


if __name__ == '__main__':
    pass
