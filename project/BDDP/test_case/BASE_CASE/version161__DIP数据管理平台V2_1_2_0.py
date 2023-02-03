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
from datetime import datetime

import allure

from project.BDDP.page_object.version161__DIP数据管理平台V2_1_2_0 import UserPage
from public.base.assert_ui import DomAssert


@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_2798:
    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("公开无首页卡片池类型卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30689(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[normalize-space(text())='移动端']").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        DomAssert(drivers).assert_att('移动端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")
        time.sleep(5)
    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("私有无首页卡片池卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30690(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[normalize-space(text())='移动端']").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        DomAssert(drivers).assert_att('移动端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "//label[normalize-space(text())='是否公开']/..//span").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")
        robot.AI_find_element(By.XPATH,
                              "//div/span[3]/span").click()
        time.sleep(5)

    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("公开有首页卡片池卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择3项指标==输入说明18字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择3项指标==输入说明18字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30691(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[normalize-space(text())='移动端']").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        DomAssert(drivers).assert_att('移动端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//label[normalize-space(text())='首页卡片池']/..//span").click()
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[12]/div/div/div/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/label/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div[2]/div[3]/button[1]").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        user.click_card()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "//input[@placeholder='请输入卡片英文名称']").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("私有有首页卡片池类型卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池否==选择下钻报表财务销售经营分析==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有是==选择首页卡片池是==选择下钻报表财务销售经营分析==选择分析指标选项==输入说明==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30692(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[normalize-space(text())='移动端']").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        DomAssert(drivers).assert_att('移动端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "//label[normalize-space(text())='是否公开']/..//span").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//label[normalize-space(text())='首页卡片池']/..//span").click()
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[12]/div/div/div/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/label/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div[2]/div[3]/button[1]").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        user.click_card()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "//input[@placeholder='请输入卡片英文名称']").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("公开卡片无指标新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池否==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池否==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30860(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[normalize-space(text())='移动端']").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        DomAssert(drivers).assert_att('移动端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//label[normalize-space(text())='首页卡片池']/..//span").click()
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        user.click_card()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "//input[@placeholder='请输入卡片英文名称']").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("私有无指标卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30861(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[normalize-space(text())='移动端']").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        DomAssert(drivers).assert_att('移动端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "//label[normalize-space(text())='是否公开']/..//span").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//label[normalize-space(text())='首页卡片池']/..//span").click()
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        user.click_card()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "//input[@placeholder='请输入卡片英文名称']").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("多选项指标卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30875(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[normalize-space(text())='移动端']").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        DomAssert(drivers).assert_att('移动端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//label[normalize-space(text())='首页卡片池']/..//span").click()
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[12]/div/div/div/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/label/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/label/span/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div[2]/div[3]/button[1]").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        user.click_card()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "//input[@placeholder='请输入卡片英文名称']").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("PC端卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型PC端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池否==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30922(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'PC端')]").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        user.assert_input('应用类型', 'PC端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        user.assert_input('卡片名称', '测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        user.click_card()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "//input[@placeholder='请输入卡片英文名称']").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("大屏端卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型PC端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30923(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'大屏端')]").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        user.assert_input('应用类型', '大屏端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        user.assert_input('卡片名称', '测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        user.click_card()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "//input[@placeholder='请输入卡片英文名称']").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("自助分析端卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型PC端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开否==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30924(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'自助分析')]").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        user.assert_input('应用类型', '自助分析端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        user.assert_input('卡片名称', '测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        user.click_card()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "//input[@placeholder='请输入卡片英文名称']").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片修改功能验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==选择已新建成功的卡片==点击编辑==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改卡片组件==修改是否公开==修改首页卡片池==修改下钻报表财务销售经营分析、供应链库存金额==修改分析指标选择2项指标==输入说明18字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30862(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[normalize-space(text())='移动端']").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        DomAssert(drivers).assert_att('移动端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='编辑']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[4]").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[4]").clear()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈佳杰")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[5]").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[5]").clear()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "王佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'王佳18646861')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('业务负责人', '王佳18646861')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/div").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH,
                              "//*[@id='app']/div/div[2]/section/div/div/div[1]/div[2]/h3/form/div/div[7]/div/div/div/div[1]/div[1]").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        DomAssert(drivers).assert_att('易为控股')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("编辑卡片成功！")
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片查看按钮功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的卡片==点击查看")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30864(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//body/div[2]/div/div/ul/li/span").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idb782fc43-2e78-4296-8c16-bdf7691cea45
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # ida5ed3bf8-12b8-41e9-bbf7-d7a2e78ceacd
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/ul/li[2]/span").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/table/tbody/tr/td[11]/div/button/span/i").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div/span[3]/span").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片启用、停用按钮功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的卡片==点击查看")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30864(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//body/div[2]/div/div/ul/li/span").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idb782fc43-2e78-4296-8c16-bdf7691cea45
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # ida5ed3bf8-12b8-41e9-bbf7-d7a2e78ceacd
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/ul/li[2]/span").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//*[@id='app']/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[11]/div/button[3]/span/i").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[3]/div/div[3]/div/button[2]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("申请成功")
        robot.AI_find_element(By.XPATH,
                              "//div[2]/table/tbody/tr/td[11]/div/button[3]/span/i").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("停用成功")
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='编辑']").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片类型全部选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择全部")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30867(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'全部')]").click()
        DomAssert(drivers).assert_att("已启用")
        DomAssert(drivers).assert_att("已停用")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片类型已启用选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择已启用")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30868(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'已启用')]").click()
        DomAssert(drivers).assert_att("已启用")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片类型已停用选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择已停用")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30869(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'已停用')]").click()
        DomAssert(drivers).assert_att("已停用")

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片类型搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片搜索框==选择卡片名称、应用类型移动端==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30871(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/input").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'PC端')]").click()
        robot.AI_find_element(By.XPATH, "//button[contains(.,'查询')]").click()
        DomAssert(drivers).assert_att("PC端")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'重置')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/input").click()
        robot.AI_find_element(By.XPATH, "//div[2]/input").send_keys("移动")
        robot.AI_find_element(By.XPATH, "//button[contains(.,'查询')]").click()

    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("多类下钻报表类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30874(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()  # id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # idb259fc7c-c62c-4853-ad7f-43426972ffd9
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[normalize-space(text())='移动端']").click()  # id733e264f-409f-438c-860c-adbab3b06e5b
        DomAssert(drivers).assert_att('移动端')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()  # id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()  # idaee48538-e0fd-4398-af6e-069d10bcee4a
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()  # id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id7dae952a-5538-4984-9b69-6e8fe7a041e8
        DomAssert(drivers).assert_att('经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()  # idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
            "陈嘉")  # idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id99fd142c-af80-416f-86a3-9d4ae612616a
        user.assert_input('需求提出人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()  # id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH,
                              "//div[contains(@x-placement,'start')]//span[contains(.,'陈嘉18649432')]").click()  # id0aefa37b-d8a8-4248-9712-b33c09d742a5
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # id81c228e5-fbac-4dda-a6e4-2dbb32761554
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()  # idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys(
            "郭伟")  # idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id176dc776-7a0d-420c-b08f-7f0cdb8607de
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()  # id1decd83b-3a76-45e4-b979-df3bcc701eb8
        DomAssert(drivers).assert_att('分享')
        robot.AI_find_element(By.XPATH, "//label[normalize-space(text())='首页卡片池']/..//span").click()
        robot.AI_find_element(By.XPATH, "//form/div").click()  # ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()  # id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div/div[2]/div/div/label/span/span").click()  # id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/label/span/span").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[12]/div/div/div/button/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/label/span").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div[2]/div[3]/button[1]").click()  # id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()  # id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")  # idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        user.assert_input('新建说明', '销售年情况')
        user.click_card()  # id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "//input[@placeholder='请输入卡片英文名称']").send_keys(
            "test")  # idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/textarea").click()  # id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys(
            "kdjflkjlfw")  # id47af0a08-5176-485e-8cb1-276dc5c8b97c
        user.assert_input('英文属性说明', 'kdjflkjlfw')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # idb61adb68-2f38-4b49-9485-4a351657b5d9
        DomAssert(drivers).assert_att("新建卡片成功！")
        DomAssert(drivers).assert_att('测试5')
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_2499:
    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("新建无首页卡片池的角色功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击角色管理新建==输入角色名称==输入角色说明==拥有首页卡片池否==选择菜单报表授权==输入关联用户==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30917(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//div[7]/li/div").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//div[7]/li/ul/div[3]/a/li").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH,
                              "//div[@id='app']/div/div[2]/section/div/div/div/div[2]/h3/form/div/div/div/div/div/input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//input[@type='text']").send_keys(
            "SMR002")  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('角色名称', 'SMR002')
        robot.AI_find_element(By.XPATH,
                              "//textarea").click()
        robot.AI_find_element(By.XPATH,
                              "//textarea").send_keys("月预估出货")
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div/div[2]/div[2]/div/label/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//div[@id='app']/div/div[2]/section/div/div/div/div[2]/h3/form/div/div[5]/div/div/div/div[3]/div/div[2]/div[3]/button").click()
        DomAssert(drivers).assert_att("月预估出货")
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/input").click()
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/input").send_keys("18653759")
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'周晓敏18653759')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/button[2]").click()
        DomAssert(drivers).assert_att("周晓敏18653759")
        DomAssert(drivers).assert_att("添加角色成功")
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()
        robot.AI_find_element(By.XPATH,
                              "//button[contains(.,'确定')]").click()
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("新建有首页卡片池的角色功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击角色管理新建==输入角色名称==输入角色说明==拥有首页卡片池是==选择菜单报表授权==输入关联用户==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30918(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//div[7]/li/div").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//div[7]/li/ul/div[3]/a/li").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH,
                              "//div[@id='app']/div/div[2]/section/div/div/div/div[2]/h3/form/div/div/div/div/div/input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//input[@type='text']").send_keys(
            "SMR002")  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('角色名称', 'SMR002')
        robot.AI_find_element(By.XPATH,
                              "//textarea").click()
        robot.AI_find_element(By.XPATH,
                              "//textarea").send_keys("月预估出货")
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//button[contains(.,'确定')]").click()
        DomAssert(drivers).assert_att("移动驾驶舱测试3")
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/button").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div/div[2]/div[2]/div/label/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[3]/div/div[2]/div[3]/button").click()
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").send_keys("18653759")
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'周晓敏18653759')]").click()
        DomAssert(drivers).assert_att("周晓敏18653759")
        robot.AI_find_element(By.XPATH,
                              "//button[contains(.,'保存')]").click()
        DomAssert(drivers).assert_att("添加角色成功")
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()
        robot.AI_find_element(By.XPATH,
                              "//button[contains(.,'确定')]").click()
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("修改角色功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已有的角色，点击编辑==修改角色名称==修改角色说明==修改拥有首页卡片池否==修改菜单报表授权==修改关联用户==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30919(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//div[7]/li/div").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//div[7]/li/ul/div[3]/a/li").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH,
                              "//div[@id='app']/div/div[2]/section/div/div/div/div[2]/h3/form/div/div/div/div/div/input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//input[@type='text']").send_keys(
            "SMR002")  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('角色名称', 'SMR002')
        robot.AI_find_element(By.XPATH,
                              "//textarea").click()
        robot.AI_find_element(By.XPATH,
                              "//textarea").send_keys("月预估出货")
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div/div[2]/div[2]/div/label/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//div[@id='app']/div/div[2]/section/div/div/div/div[2]/h3/form/div/div[5]/div/div/div/div[3]/div/div[2]/div[3]/button").click()
        DomAssert(drivers).assert_att("月预估出货")
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/input").click()
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/input").send_keys("18653759")
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'周晓敏18653759')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/button[2]").click()
        DomAssert(drivers).assert_att("周晓敏18653759")
        DomAssert(drivers).assert_att("添加角色成功")
        robot.AI_find_element(By.XPATH,
                              "//div[2]/table/tbody/tr/td[7]/div/button/span/i").click()
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[@id='app']/div/div[2]/section/div/div/div/div[2]/h3/form/div/div[5]/div/div/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()
        DomAssert(drivers).assert_att("月预估出货")
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'保存')]").click()
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()
        robot.AI_find_element(By.XPATH,
                              "//button[contains(.,'确定')]").click()
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("角色类型搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击角色搜索框==输入搜索字段==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30921(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//div[7]/li/div").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//div[7]/li/ul/div[3]/a/li").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//input").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//input").send_keys("mr002")  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//*[@id='app']/div/div[2]/section/div/div/div/div/div[2]/div/button[1]/span").click
        DomAssert(drivers).assert_att("MR002")

if __name__ == '__main__':
    pass
