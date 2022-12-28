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
@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_2499:
    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("公开报表说明栏501字以内新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域输入业务域==输入业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型总部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28877(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.101.147:8929/")#id963e2ef2-2363-4be9-aa8f-a3f7369d3f1c
        robot.AI_find_element(By.CSS_SELECTOR, ".menu-wrapper:nth-child(4) .el-menu-item").click()#id7781ac13-b302-444a-936e-141fb04657f7
        element = robot.AI_find_element(By.CSS_SELECTOR, ".menu-wrapper:nth-child(4) .el-menu-item")#id755d52d0-bb01-49af-8f19-38b7ec6dac81
        actions = ActionChains(drivers)
        actions.move_to_element(element).perform()
        element = robot.AI_find_element(By.CSS_SELECTOR, "body")#id0aa2ff85-7a78-494d-acd6-d4f2918676d3
        actions = ActionChains(drivers)
        actions.move_to_element(element).perform()
        robot.AI_find_element(By.CSS_SELECTOR, ".creatBtn > span").click()#iddb0a181f-1f03-4f45-b000-2288675a2806
        robot.AI_find_element(By.CSS_SELECTOR, ".el-col:nth-child(1) .el-select__caret").click()#ida2201acc-ae9c-4c79-a7b2-d41e364b28d1
        robot.AI_find_element(By.CSS_SELECTOR, ".hover > span").click()#id7a1011f2-ded1-47ed-b326-9f91904c6dde
        robot.AI_find_element(By.CSS_SELECTOR, ".el-col:nth-child(2) .el-select__caret").click()#id5700be7c-939c-43bf-b865-f0c5ba51aedd
        robot.AI_find_element(By.CSS_SELECTOR, ".hover:nth-child(1)").click()#id9b0307ff-1692-44f7-9caa-858c3e1efcf1
        robot.AI_find_element(By.CSS_SELECTOR, ".el-col:nth-child(3) input").click()#idbd47b3fb-1893-4402-8c4f-89c832f8e336
        robot.AI_find_element(By.CSS_SELECTOR, ".el-tree-node:nth-child(1) .el-tree-node__expand-icon").click()#id728ee0a5-213e-44da-90b6-fa6b2e81bf01
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()#iddb2a629c-a0ab-4831-9cd0-497a40a5152c
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").send_keys("陈嘉")#idea4f6708-d123-47be-873d-b9105aa800c7
        robot.AI_find_element(By.CSS_SELECTOR, ".hover").click()#id29a31d99-846b-4b87-9067-6af8e20cde2c
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()#id09f8da5e-a83b-4b4b-8e51-29a0fac0645c
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").send_keys("陈嘉")#id7d940467-4596-4d67-87d2-f5f4e9543709
        robot.AI_find_element(By.CSS_SELECTOR, ".hover > span").click()#id756c42fe-8134-4999-a892-eb61420dfcbc
        robot.AI_find_element(By.CSS_SELECTOR, ".el-col:nth-child(6) input").click()#ida10b2563-da75-4ec0-9c88-d0019f9be08f
        robot.AI_find_element(By.CSS_SELECTOR, "#\\31 672144188308 > .el-tree-node:nth-child(4) .custom-tree-node").click()#idf9ad2a2d-db70-470a-9eb3-c3cf070e5db9
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()#id0b91761e-6d64-41a8-986c-0900393b102f
        robot.AI_find_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").send_keys("郭伟")#idf9c0e2d8-bbd1-42f5-bc33-b618be02401e
        robot.AI_find_element(By.CSS_SELECTOR, ".hover").click()#id25422ec4-cc3b-47ec-9722-23f1093fed05
        robot.AI_find_element(By.CSS_SELECTOR, ".el-input:nth-child(2) > .el-input__inner").click()#id1b2fa179-a541-465d-95e8-46fc95b1a391
        robot.AI_find_element(By.CSS_SELECTOR, ".hover").click()#id88c28012-cc0d-4abe-adcb-b5647d977388
        robot.AI_find_element(By.CSS_SELECTOR, ".el-card:nth-child(1) > .el-card__body").click()#idda10ed5c-2129-4e27-b596-d34e3ecec1e0
        robot.AI_find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-input > .el-input__inner").click()#id26e37108-4cfd-4107-abe3-47476808a206
        robot.AI_find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-input > .el-input__inner").send_keys("test")#id7bfd10d2-7a63-450b-a49a-0927615f96fd


if __name__ == '__main__':
    pass
