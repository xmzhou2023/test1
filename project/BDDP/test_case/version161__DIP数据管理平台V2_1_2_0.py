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
class Teststory_2499:
    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("公开报表说明栏501字以内新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域输入业务域==输入业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型总部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28877(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()#idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()#ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()#id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()#id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()#id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").click()#id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(report)#id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()#id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div/div").click()#id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").click()#id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys("陈佳")#id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH, "//span[contains(.,'陈佳杰18649692')]").click()#id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH, "//div[5]/div/div/div/div/input").click()#id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("陈嘉")#id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH, "//span[contains(.,'陈嘉18649432')]").click()#id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH, "//div[6]/div/div/div/div/div").click()#id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH, "//div[6]/div/div/div/div[2]/div[4]/div/div").click()#idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").click()#idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys("郭伟")#ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH, "//span[contains(.,'郭伟18648974')]").click()#id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()#id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()#id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()#id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()#id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys("test1")#id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()#idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH, "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()#idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH, "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()#idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_2797:
    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("公开展示'首页'类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30688(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("公开多类下钻报表类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30689(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("公开卡片单选项指标新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30690(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("公开卡片说明栏20字以内新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择3项指标==输入说明18字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30691(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.248.39.163:10101/")#idbd3cf27c-8585-4ba5-8381-d235f14cee98
        robot.AI_find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input--prefix > .el-input__inner").click()#id873dd024-9b8e-4a86-9ea7-1be3c2065e91
        robot.AI_find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input--prefix > .el-input__inner").send_keys("18653759")#idb705b744-1104-47df-ad64-eb6208ca6886
        robot.AI_find_element(By.CSS_SELECTOR, ".el-input--suffix > .el-input__inner").send_keys("xLily6x")#idde7f200e-d2ff-4f48-9f09-cbfd98301f26
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()#ida2d70b62-043a-49a4-a5f1-f0c574f6306c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("2JYB")#id80e4b3ac-fd56-410d-802d-a0f21c6aa83c
        robot.AI_find_element(By.XPATH, "//button[contains(.,'登录')]").click()#id8ae7d68a-4e0e-41f0-81e2-1da07be1eae5
        robot.AI_find_element(By.CSS_SELECTOR, "#hamburger-container use").click()#ida455c33d-cd2d-48e5-99a9-bf66e185d4b9
        robot.AI_find_element(By.XPATH, "//li[contains(.,'卡片管理')]").click()#id819be31d-e1f9-4481-9c4d-4f8c5b2eb748
        robot.AI_find_element(By.XPATH, "//span[contains(.,'+新建')]").click()#idb259fc7c-c62c-4853-ad7f-43426972ffd9
        robot.AI_find_element(By.XPATH, "//span/i[2]").click()#id6eefae5f-6f81-4e45-8d5f-a4f6a45ac543
        robot.AI_find_element(By.XPATH, "//input").click()#id7675bc2c-97bc-4003-8c23-a9f83a7f39e2
        robot.AI_find_element(By.XPATH, "//body/div[2]/div/div/ul/li/span").click()#id733e264f-409f-438c-860c-adbab3b06e5b
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()#id0c4fd09a-bd47-48fb-8f76-9572f82c1eeb
        robot.AI_find_element(By.XPATH, "//span[contains(.,'测试5')]").click()#idaee48538-e0fd-4398-af6e-069d10bcee4a
        robot.AI_find_element(By.XPATH, "//div[3]/div/div/div/div").click()#id04f28941-04fc-44fd-985d-e6d052a6d848
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()#id7dae952a-5538-4984-9b69-6e8fe7a041e8
        robot.AI_find_element(By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div/div").click()#id38d3f393-8a1c-4efb-8755-114a7972491c
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()#idb782fc43-2e78-4296-8c16-bdf7691cea45
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()#ida5ed3bf8-12b8-41e9-bbf7-d7a2e78ceacd
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()#idbf07d0c5-9b20-4b44-99dd-775b7afbda55
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("陈嘉")#idb1b23502-aaa2-464f-943c-edec89f09dbf
        robot.AI_find_element(By.XPATH, "//span[contains(.,'陈嘉18649432')]").click()#id99fd142c-af80-416f-86a3-9d4ae612616a
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()#id7db42d6d-51d1-4856-b85b-bc7d4132fbe0
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("陈嘉")#id670f4fb3-33ed-436e-9c17-407410840882
        robot.AI_find_element(By.XPATH, "//div[5]/div/div/ul/li[2]/span").click()#id0aefa37b-d8a8-4248-9712-b33c09d742a5
        robot.AI_find_element(By.XPATH, "//div[6]/div/div/div/div/div[2]/input").click()#ida85ddfc9-4eae-4fdf-988b-9d68793cb214
        robot.AI_find_element(By.XPATH, "//div[6]/div/div/div/div[2]/div[4]/div/div").click()#id81c228e5-fbac-4dda-a6e4-2dbb32761554
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").click()#idfeb66049-f2f7-49a5-b58d-9acb078c748d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys("郭伟")#idbe1014f9-4127-40f6-a5e6-b1d907af7186
        robot.AI_find_element(By.XPATH, "//span[contains(.,'郭伟18648974')]").click()#id176dc776-7a0d-420c-b08f-7f0cdb8607de
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()#id5813b835-6415-409c-817b-0077154c754a
        robot.AI_find_element(By.XPATH, "//li[contains(.,'分享')]").click()#id1decd83b-3a76-45e4-b979-df3bcc701eb8
        robot.AI_find_element(By.XPATH, "//form/div").click()#ida38468eb-42eb-4207-b858-4bc4fe5bd74d
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()#idbad517d0-a865-41ee-848d-56824c93d13e
        robot.AI_find_element(By.XPATH, "//button[contains(.,'选择')]").click()#id5e1bc90c-083b-44b6-8b0b-a38b23fb4fdb
        robot.AI_find_element(By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div[2]/div/div/label/span/span").click()#id0eeb066f-3867-460f-b2d8-f977384ea9a4
        robot.AI_find_element(By.XPATH, "//div[2]/div[3]/button/span").click()#id0c0244bd-7b65-46ea-9468-1e744ea81268
        robot.AI_find_element(By.XPATH, "//textarea").click()#id8e65d049-801e-44e7-bb4d-e149bbd931dd
        robot.AI_find_element(By.XPATH, "//textarea").send_keys("销售年情况")#idfb1077c3-5ffa-41ee-a2d4-c7c93fe00d0e
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()#id08a75066-5f43-44ef-9c09-b31e3c01cd00
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys("test")#idc6289502-af33-4620-94fe-df696d45087a
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").click()#id16278250-da7e-4213-8ee1-e0d5c8c8237e
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/textarea").send_keys("kdjflkjlfw")#id47af0a08-5176-485e-8cb1-276dc5c8b97c
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()#idb61adb68-2f38-4b49-9485-4a351657b5d9


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("私有不展示'首页'类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池否==选择下钻报表财务销售经营分析==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30692(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("私有展示'首页'类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池是==选择下钻报表财务销售经营分析==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30693(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("私有多类下钻报表类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30694(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("私有卡片单选项指标新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30695(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("卡片组合总部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30696(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("卡片组合地区部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30697(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("卡片组合事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型事业部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30698(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("卡片组合国家类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型国家==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30699(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("卡片组合地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区部_事业部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30700(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("无首页差异化报表类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化否==选择报表类型总部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30701(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("首页差异化类报表不同用户查看展示验证")  # 用例名称
    @allure.description("分别登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30702(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("PC端报表查看展示验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型pc端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30703(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("大屏端报表查看展示验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型大屏端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==选择报表类型总部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30704(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("外部页面总部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源外部页面==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30705(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("定制总部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型总部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30706(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("定制地区部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型地区部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30707(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("定制事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型事业部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30708(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("定制国家类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型国家==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30709(self, drivers):
        pass


    @allure.story("报表管理中增加角色类型")  # 用户故事名称
    @allure.title("定制地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型地区部_事业部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30710(self, drivers):
        pass


if __name__ == '__main__':
    pass
