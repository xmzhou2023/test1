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
        robot.AI_get("http://10.250.112.166:9000/")
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div/div[2]/div/div/ul/div[11]/li/div").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'用户管理')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("1865")
        robot.AI_find_element(By.XPATH, "//li[contains(.,'18650935')]").click()
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/section/div/div/div/form/div/div[3]/button[2]/span").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("黄")
        robot.AI_find_element(By.XPATH, "//li[contains(.,'黄盼盼')]").click()
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/section/div/div/div/form/div/div[3]/button[2]/span").click()


if __name__ == '__main__':
      pass
