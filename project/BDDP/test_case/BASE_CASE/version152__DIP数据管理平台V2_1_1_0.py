from datetime import datetime
import time
import allure
import pytest
from selenium.webdriver.common.by import By

from libs.common.action import KeyWord
from project.BDDP.page_object.version161__DIP数据管理平台V2_1_2_0 import UserPage
from public.base.assert_ui import DomAssert


@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_3937:
    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("移动端无报表差异化卡片组合报表类型报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域输入业务域==输入业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型总部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析==登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域输入业务域==输入业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型总部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析==登录PC端后台")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28877(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")
        robot.AI_find_element(By.XPATH,
                              "//div/span[3]/span").click()
        time.sleep(5)

@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_2492:
    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("移动端报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30876(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")
        robot.AI_find_element(By.XPATH,
                              "//div/span[3]/span").click()
        time.sleep(5)


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("PC端报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型pc端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==输入访问地址==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30877(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//li[contains(.,'PC端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', 'PC端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").send_keys(
            "http://10.250.101.147:8605/finb/")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")
        robot.AI_find_element(By.XPATH,
                              "//div/span[3]/span").click()
        time.sleep(5)


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("大屏端报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型大屏端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==输入访问地址==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30878(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'大屏端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '大屏端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").send_keys(
            "http://10.250.101.147:8605/finb/")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")
        robot.AI_find_element(By.XPATH,
                              "//div/span[3]/span").click()
        time.sleep(5)


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("自助分析端报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型自助分析==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==输入访问地址==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30879(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'自助分析')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '自助分析')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").send_keys(
            "http://10.250.101.147:8605/finb/")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")
        robot.AI_find_element(By.XPATH,
                              "//div/span[3]/span").click()
        time.sleep(5)


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无首页差异化报表外部引入类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30880(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无首页差异化报表定制卡片类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择定制==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择私有卡片==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30881(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无首页差异化报表定制卡片、外部引入组合类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择定制==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择私有卡片、输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30883(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//label[3]/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//button[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").send_keys(
            "http://10.250.101.147:8605/finb/")
        # robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        # robot.AI_find_element(By.XPATH,
        #                       "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        # robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合总部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30884(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'总部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合地区部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30885(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型事业部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30886(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'事业部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合国家类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型国家==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30887(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'国家经理')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区部_事业部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30888(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'事业部-地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合总部、地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区部_事业部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30889(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')

        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'总部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入总部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30890(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'总部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入地区部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30891(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")



    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型事业部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30892(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'事业部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")



    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入国家类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型国家部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30893(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'国家经理')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区事业部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30894(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'事业部-地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")



    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入总部、地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部、地区部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30895(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'总部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[11]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[11]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")



    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制总部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型总部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30896(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//label[3]/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'总部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制地区部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型地区部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30897(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//label[3]/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型事业部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30898(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//label[3]/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'事业部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制国家类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型国家==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30899(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//label[3]/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'国家经理')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型地区部_事业部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30900(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//label[3]/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'事业部-地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型卡片组合==修改是否差异化是、修改报表类型国家==修改卡片来源==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30901(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'总部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH, "//td[not(contains(@class,'is-hidden'))]//i[@title='编辑']").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("王佳")
        robot.AI_find_element(By.XPATH, "//li[contains(.,'王佳18646861')]").click()
        DomAssert(drivers).assert_att("王佳18646861")
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'事业部-地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "//button[contains(.,'保存')]").click()
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型外部引入==修改是否差异化是、修改报表类型国家==修改外部链接==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30902(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'事业部-地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH, "//td[not(contains(@class,'is-hidden'))]//i[@title='编辑']").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("王佳")
        robot.AI_find_element(By.XPATH, "//li[contains(.,'王佳18646861')]").click()
        DomAssert(drivers).assert_att("王佳18646861")
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'事业部-地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "//button[contains(.,'保存')]").click()
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型定制==修改是否差异化是、修改报表类型国家==修改卡片来源、外部链接==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30903(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//label[3]/span/span").click()
        robot.AI_find_element(By.XPATH,
                              "//div[9]/div/div/div/span").click()
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'事业部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH, "//td[not(contains(@class,'is-hidden'))]//i[@title='编辑']").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("王佳")
        robot.AI_find_element(By.XPATH, "//li[contains(.,'王佳18646861')]").click()
        DomAssert(drivers).assert_att("王佳18646861")
        robot.AI_find_element(By.XPATH,
                              "(//input[@type='text'])[6]").click()
        robot.AI_find_element(By.XPATH,
                              "//li[contains(.,'事业部-地区部领导')]").click()
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'选择')]").click()
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确定')]").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "//button[contains(.,'保存')]").click()
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无报表差异化卡片组合类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型卡片组合==修改是否差异化否、==修改卡片来源==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30904(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH, "//td[not(contains(@class,'is-hidden'))]//i[@title='编辑']").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("王佳")
        robot.AI_find_element(By.XPATH, "//li[contains(.,'王佳18646861')]").click()
        DomAssert(drivers).assert_att("王佳18646861")
        robot.AI_find_element(By.XPATH, "//button[contains(.,'保存')]").click()
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无报表差异化外部引入类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型外部引入==修改是否差异化否==修改外部链接==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30905(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH, "//td[not(contains(@class,'is-hidden'))]//i[@title='编辑']").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("王佳")
        robot.AI_find_element(By.XPATH, "//li[contains(.,'王佳18646861')]").click()
        DomAssert(drivers).assert_att("王佳18646861")
        robot.AI_find_element(By.XPATH, "//button[contains(.,'保存')]").click()
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")



    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无报表差异化定制类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型定制==修改是否差异化否==修改卡片来源、外部链接==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30906(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,' 外部引入')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[6]").send_keys(
            "http://10.250.101.147:8605/finb/")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[8]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH, "//td[not(contains(@class,'is-hidden'))]//i[@title='编辑']").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("王佳")
        robot.AI_find_element(By.XPATH, "//li[contains(.,'王佳18646861')]").click()
        DomAssert(drivers).assert_att("王佳18646861")
        robot.AI_find_element(By.XPATH, "//button[contains(.,'保存')]").click()
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表启用、停用功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击启用==输入申请原因==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30907(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()  # idefcc705e-c5ad-43ca-8519-00fad0f6f7dd
        robot.AI_find_element(By.XPATH, "//span[contains(.,'我的报表')]").click()  # ide6a0cf83-3168-4add-bb76-2d66f192193b
        robot.AI_find_element(By.XPATH, "//button[contains(.,'+新建')]").click()  # id4fff8401-346a-4585-839a-8d3fa44f393a
        time.sleep(2)
        robot.AI_find_element(By.XPATH, "//input").click()  # id31d7380e-8987-45d6-809c-5846808b2d73
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()  # id4c0658e8-547b-4fae-b587-5d420c7543f9
        user.assert_input('应用类型', '移动端')
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div/div/div/div/input").click()  # id6f8a8fdd-dc10-451d-9cd8-1cac1119feec
        report = '年终报表{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        robot.AI_find_element(By.XPATH, "//div[2]/div/div/div/div/div/input").send_keys(
            report)  # id07dc31ec-2bc2-48a5-98e2-cb979165382f
        user.assert_input('报表名称', report)
        user.click_primary()
        robot.AI_find_element(By.XPATH, "//div[2]/div/span").click()  # id138ec904-3b28-4810-9734-aa269ce2d0bf
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div[2]/div[2]/div[2]/div/div").click()  # id3e443bb4-9070-4b1b-9e37-b251cd057ef9
        user.assert_input('主题域', '经营分析')
        robot.AI_find_element(By.XPATH,
                              "//div[4]/div/div/div/div/input").click()  # id630b7b76-b226-4453-b976-493b0e3d9066
        robot.AI_find_element(By.XPATH, "//div[4]/div/div/div/div/input").send_keys(
            "陈佳")  # id1a973597-8457-4c93-871b-647a5e5d651e
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈佳杰18649692')]").click()  # id1a7ae198-2390-4b8f-ace0-55636a61907b
        user.assert_input('需求提出人', '陈佳杰18649692')
        robot.AI_find_element(By.XPATH,
                              "//div[5]/div/div/div/div/input").click()  # id42296f24-cd45-41bc-8a9e-966e97aaeb31
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys(
            "陈嘉")  # id0ce0acb1-89e3-44b7-b6b6-5ccf9d6b7c59
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'陈嘉18649432')]").click()  # id4b3fac54-014f-4035-8d4f-cf7b9c781a94
        user.assert_input('业务负责人', '陈嘉18649432')
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div/div").click()  # id615ecac7-d00c-4a86-a4cc-9873dd1f520a
        robot.AI_find_element(By.XPATH,
                              "//div[6]/div/div/div/div[2]/div[4]/div/div").click()  # idc44dbecf-ef1c-43a0-bfff-d7bc8a8b37ce
        user.assert_input('业务组织', '深圳传音控股')
        robot.AI_find_element(By.XPATH,
                              "//div[7]/div/div/div/div/input").click()  # idd463308d-a6fb-488d-8fde-7222540b5f9c
        robot.AI_find_element(By.XPATH, "//div[7]/div/div/div/div/input").send_keys(
            "郭伟")  # ideecf3385-26fc-4847-996e-fda2591023b0
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'郭伟18648974')]").click()  # id2d9d92bb-319e-4a41-bb78-9f76f3ad462e
        user.assert_input('IT负责人', '郭伟18648974')
        robot.AI_find_element(By.XPATH, "//span[contains(.,'选择')]").click()  # id013549e9-e331-4a5a-939d-80f4e47bdcc0
        robot.AI_find_element(By.XPATH,
                              "//div[2]/div/div[2]/div/div[2]/div/div/label/span/span").click()  # id4aa7e7a2-3b6b-494f-aef8-dab18caac401
        robot.AI_find_element(By.XPATH, "//span[contains(.,'确定')]").click()  # id50d74e4d-3f2b-4bf7-801f-fdd9c536fd32
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").click()  # id713ef7b3-3abe-41e8-aa83-0e25be558f36
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys(
            "test1")  # id754be369-7f1e-429d-b712-6da425c84027
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("保存成功！")
        DomAssert(drivers).assert_att(report)
        robot.AI_find_element(By.XPATH,
                              "//*[@id='app']/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[11]/div/button[3]/span/i").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'确 定')]").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        DomAssert(drivers).assert_att("申请成功")
        robot.AI_find_element(By.XPATH,
                              "//div[2]/table/tbody/tr/td[11]/div/button[3]/span/i").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        robot.AI_find_element(By.XPATH,
                              "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()
        DomAssert(drivers).assert_att("停用成功")
        robot.AI_find_element(By.XPATH,
                              "//td[not(contains(@class,'is-hidden'))]//i[@title='编辑']").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'保存')]").click()
        # robot.AI_find_element(By.XPATH,
        #                       "//td[not(contains(@class,'is-hidden'))]//i[@title='删除']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        # robot.AI_find_element(By.XPATH,
        #                       "//div[@class='el-message-box__wrapper']//span[normalize-space(text())='确定']").click()  # idaa9f333a-6f7a-4e44-874c-b9ad82f4b7af
        # DomAssert(drivers).assert_att("删除成功")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型全部选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择全部")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30911(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表检索')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'全部')]").click()
        DomAssert(drivers).assert_att("已启用")
        DomAssert(drivers).assert_att("已停用")

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型已启用选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择已启用")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30912(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表检索')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'已启用')]").click()
        DomAssert(drivers).assert_att("已启用")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型已停用选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择已停用")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30913(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表检索')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'已停用')]").click()
        DomAssert(drivers).assert_att("已停用")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表搜索框==选择报表名称、应用类型移动端==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30915(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表检索')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'移动端')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'查询')]").click()
        DomAssert(drivers).assert_att("移动端")


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表模糊搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击模糊搜索框==输入模糊报表名称、应用类型移动==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30916(self, drivers):
        robot = KeyWord(drivers)
        user = UserPage(drivers)
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表管理')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'报表检索')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("情况")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'查询')]").click()
        DomAssert(drivers).assert_att("情况")


if __name__ == '__main__':
    pass
