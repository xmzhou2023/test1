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
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18519(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.248.39.163:10101/")
        robot.AI_find_element(By.XPATH, "//div[@id='sidebar-containerId']/div/div/div/ul/div[2]/li/div").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'Call Center')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'Repair Center')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'JS Mgt')]").click()
        robot.AI_find_element(By.XPATH, "//div[@id='sidebar-containerId']/div/div/div/ul/div[4]/li/ul/div/li/ul/div/li").click()
        robot.AI_find_element(By.XPATH, "//div[@id='main-containerId']/section/div/div/div[2]/button/span").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'Carry In')]").click()
        element = robot.AI_find_element(By.XPATH, "(//button[@type='button'])[5]")
        actions = ActionChains(robot)
        actions.move_to_element(element).perform()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys("xpath编辑功能(后端)")
        robot.AI_find_element(By.XPATH, "//div[@id='el-collapse-content-9751']/div/div/form/div/div/div/div/div/span/span/i").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[25]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'End User')]").click()


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
        robot.AI_get("http://10.250.112.166:9000/")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'系统管理')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'用户管理')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("1865")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'18650935')]").click()
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/section/div/div/div/form/div/div[3]/button[2]/span").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("黄")
        robot.AI_find_element(By.XPATH, "//li[contains(.,'黄文超')]").click()
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/section/div/div/div/form/div/div[3]/button[2]/span").click()


    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台4")  # 用例名称
    @allure.description("查询工号==查询姓名")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19966(self, drivers):
        pass


if __name__ == '__main__':
      pass
