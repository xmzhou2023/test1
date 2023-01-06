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
        robot.AI_get("http://10.248.39.163:10101/")#id342a3158-c32a-4fe4-9f42-b82700902c7f
        robot.AI_find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) use").click()#id7aea1037-1642-4e22-8af2-a83712db0edd
        robot.AI_find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input--prefix > .el-input__inner").click()#idca56c186-ac86-43d0-96bf-22cde2452264
        robot.AI_find_element(By.XPATH, "//input[@type='text']").send_keys("18653759")#id8f400179-f15f-4031-a069-4c27b2bf22f3
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/input").send_keys("xLily6x")#id5a7d026f-c517-480d-87f1-88e9a5e94518
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()#idc22ece48-10a7-4284-a867-e62c70a53e8c
        robot.AI_find_element(By.XPATH, "//span/div/div").click()#idfd0e9271-24e2-4f5c-a009-2d86b24fda5c
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/input").click()#id29c89e81-b1f8-47ec-90b1-2699ccfe9005
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("ngtk")#id4b0d34e5-2c96-47b1-95ac-5f2d5ce0ba26
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys(Keys.ENTER)#id7da8b345-afab-4955-bd9a-702a8847cfa3
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()#idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()#ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()#id4fff8401-346a-4585-839a-8d3fa44f393a
        robot.AI_find_element(By.XPATH, "//input").click()#id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()#id4c0658e8-547b-4fae-b587-5d420c7543f9
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").click()#id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys("年终报表")#id07dc31ec-2bc2-48a5-98e2-cb979165382f
        robot.AI_find_element(By.XPATH, "//div[2]/input").click()#id7cd46395-f4f9-4809-a0ae-05434a7618e0
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()#id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div/div").click()#id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        robot.AI_find_element(By.XPATH, "//form/div/div[4]").click()#idb72bb9c3-1ee8-40f5-83a6-300c24fdffc1
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").click()#id782dea48-ede7-4040-af40-bd9391684a21
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").click()#id75205d2b-9869-49a1-af7a-72b4c5923358
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").click()#id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys("陈佳")#id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH, "//span[contains(.,'陈佳杰18649692')]").click()#id1a7ae198-2390-4b8f-ace0-55636a61907b
        robot.AI_find_element(By.XPATH, "//div[5]/div/div/div/div/input").click()#id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("陈嘉")#id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH, "//span[contains(.,'陈嘉18649432')]").click()#id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        robot.AI_find_element(By.XPATH, "//div[6]/div/div/div/div/div").click()#id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH, "//div[6]/div/div/div/div[2]/div[4]/div/div").click()#idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").click()#idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys("郭伟")#ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH, "//span[contains(.,'郭伟18648974')]").click()#id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()#id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()#id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()#id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()#id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys("test1")#id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()#idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af


if __name__ == '__main__':
    pass
