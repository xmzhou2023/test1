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
@allure.feature("B001R001V002SP008")  # 迭代名称
class Teststory_4078:
    @allure.story("用例管理迭代需求CRM试验")  # 用户故事名称
    @allure.title("TranTest自动化测试用例1")  # 用例名称
    @allure.description("123==123==123==步骤1==步骤2==步骤3==步骤一内容==步骤二内容==步骤三内容==步骤一内容==步骤二内容==步骤三内容")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28234(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_gets("http://10.250.112.57/")#idda788124-9c19-4721-b3f8-aeb60ae56576
        robot.AI_finds_element(By.CSS_SELECTOR, ".hamburger").click()#id1c2fa2d8-291f-4de1-9587-9cef384533c3
        robot.AI_finds_element(By.CSS_SELECTOR, "div:nth-child(3) > .el-submenu span:nth-child(2)").click()#id74242fda-1c2a-4b21-870d-30849445aa12
        robot.AI_finds_element(By.CSS_SELECTOR, ".is-opened .nest-menu:nth-child(1) .el-submenu__AI_title() > span").click()#idb194145f-c2f7-451b-938e-9e39e0c6e3f2
        robot.AI_finds_element(By.CSS_SELECTOR, ".is-opened > .el-menu > .nest-menu:nth-child(1) > .el-menu-item").click()#idbc5dd35d-816c-434c-9ca8-6e1412bf69d6
        value = robot.AI_finds_element(By.CSS_SELECTOR, ".el-tooltip .el-input__inner").get_attribute("value")#idb54d6e3c-4893-4631-a99b-75683388c860
        assert value == "rwerewrew"
        value = robot.AI_finds_element(By.CSS_SELECTOR, ".el-tooltip .el-input__inner").get_attribute("value")#idcf78705d-511b-43a5-ba90-e898447bccf8
        assert value == "dfsbcbcv"
        robot.AI_finds_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()#ide648199f-4cc9-456b-bb7e-4c8b3808c13f
        robot.vars["etete"] = robot.AI_title()
        element = robot.AI_finds_element(By.CSS_SELECTOR, ".right-menu-item > .el-button")#id2ce28ebf-a40d-4193-b593-c02dd5e0d44b
        actions = ActionChains(drivers)
        actions.move_to_element(element).perform()
        robot.vars["fdfsdf"] = robot.AI_finds_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").get_attribute("value")#id00b2bf32-221c-4a14-a576-dcf19c886c2c
        WebDriverWait(drivers, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".is-focus > .el-input__inner")))#id3dbdb7a8-e56c-44db-bf84-53e7bc35efde
        WebDriverWait(drivers, 9).until_not(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".is-focus > .el-input__inner")))#ida4a91771-33b8-40c6-842b-d01828bc7fa1
        WebDriverWait(drivers, 9).until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".is-focus > .el-input__inner")))#idd542f91c-a972-4d62-83e3-61d9513fa687
        WebDriverWait(drivers, 9).until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".is-focus > .el-input__inner")))#id82c8882b-7014-42e3-9633-1a7c43f8a35c
        robot.AI_finds_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()#idfb57b4c0-f306-4eda-a77f-d554690001a3
        WebDriverWait(drivers, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".is-focus > .el-input__inner")))#id6ddaa56d-e267-4ada-8174-430cdaf74bbe
        robot.AI_finds_element(By.CSS_SELECTOR, ".el-col:nth-child(1) .el-input__inner").click()#id60fcc01f-0e0c-43b8-8c53-31f4ccbe9fb6
        WebDriverWait(drivers, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".el-col:nth-child(1) .el-input__inner")))#id91c5cfe1-53e1-4d82-8ba1-c9bc486f613e
        WebDriverWait(drivers, 190).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".el-col:nth-child(2) .el-input__inner")))#ida88e4a6c-71e5-4d4d-a7c6-b520444a03a6
        assert robot.AI_finds_element(By.CSS_SELECTOR, ".el-col:nth-child(3) .el-form-item__content > div").is_selected() is True#ide2200cd8-30ba-4141-89d7-d5f1c1312c98
        robot.vars["rerw"] = robot.AI_title()
        robot.AI_finds_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner").click()#ide2200cd8-30ba-4141-89d7-d5f1c1312c98
        element = robot.AI_finds_element(By.CSS_SELECTOR, ".el-col:nth-child(7) .el-form-item__content > div")#idb5f78dd6-2e21-4e46-a0b1-0eb009350436
        assert element.is_enabled() is True
        assert robot.AI_finds_element(By.CSS_SELECTOR, ".el-col:nth-child(7) .el-form-item__content > div").is_selected() is False#id46d7719d-509d-4c77-b818-0bdc85fae9b6
        element = robot.AI_finds_element(By.CSS_SELECTOR, ".is-focus > .el-input__inner")#id46d7719d-509d-4c77-b818-0bdc85fae9b6
        assert element.is_enabled() is False
        WebDriverWait(drivers, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".el-table_3_column_9 .textStyle"), "18645342-熊文敏"))#id306efdaf-7bae-4785-9fc2-510e0185edde
        WebDriverWait(drivers, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".el-table_3_column_9 .textStyle"), "18645342-熊文敏"))#idbfdecce4-f901-4fc4-899d-6066941c7ec3
        elements = robot.AI_finds_elements(By.CSS_SELECTOR, ".is-focus > .el-input__inner")#id79a2d675-2bc1-44d6-8189-0b0968d3b9c0
        assert len(elements) == 0


    @allure.story("用例管理迭代需求CRM试验")  # 用户故事名称
    @allure.AI_title()("传测自动化测试用例2")  # 用例名称
    @allure.description("123==123==123==程序执行步骤一==程序执行步骤二==程序执行步骤三")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28235(self, drivers):
        pass


if __name__ == '__main__':
      pass
