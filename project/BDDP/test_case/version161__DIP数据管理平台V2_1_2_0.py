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

from project.BDDP.page_object.version161__DIP数据管理平台V2_1_2_0 import kapianguanli
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
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()


    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("私有无首页卡片池卡片新建验证")  # 用例名称
    @allure.description(
    "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30690(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        time.sleep(1)
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_open()
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("公开有首页卡片池卡片新建验证")  # 用例名称
    @allure.description(
    "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择3项指标==输入说明18字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择3项指标==输入说明18字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30691(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.click_homepage()
        user.click_report()
        user.click_report1()
        user.click_report2()
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain01()
        user.click_card_explain01()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("多类下钻报表类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30874(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.click_homepage()
        user.click_report()
        user.click_report1()
        time.sleep(2)
        user.click_report01()
        user.click_report2()
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain01()
        user.click_card_explain01()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()


    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("私有有首页卡片池类型卡片新建验证")  # 用例名称
    @allure.description(
    "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池否==选择下钻报表财务销售经营分析==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有是==选择首页卡片池是==选择下钻报表财务销售经营分析==选择分析指标选项==输入说明==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30692(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_open()
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.click_homepage()
        user.click_report()
        user.click_report1()
        user.click_report01()
        user.click_report2()
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain01()
        user.click_card_explain01()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        time.sleep(2)
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(2)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("公开卡片无指标新建验证")  # 用例名称
    @allure.description(
    "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池否==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池否==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30860(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        time.sleep(2)
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("私有无指标卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30861(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_open()
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        time.sleep(2)
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("多选项指标卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30875(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targer2()
        user.click_targersure()
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        time.sleep(2)
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("PC端卡片新建验证")  # 用例名称
    @allure.description(
     "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型PC端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池否==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30922(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        # DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.input_content('应用类型', 'PC端')
        user.assert_input('应用类型', 'PC端')
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        time.sleep(2)
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("大屏端卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型PC端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30923(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.input_content('应用类型', '大屏端')
        user.assert_input('应用类型', '大屏端')
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        time.sleep(2)
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("自助分析端卡片新建验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型PC端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开否==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30924(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.input_content('应用类型', '自助分析')
        user.assert_input('应用类型', '自助分析')
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        time.sleep(2)
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片修改功能验证")  # 用例名称
    @allure.description(
        "登录PC端后台管理系统==选择已新建成功的卡片==点击编辑==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改卡片组件==修改是否公开==修改首页卡片池==修改下钻报表财务销售经营分析、供应链库存金额==修改分析指标选择2项指标==输入说明18字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30862(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        time.sleep(2)
        user.click_editor()
        user.input_content('需求提出人', '18646861')
        user.assert_input('需求提出人', '王佳18646861')
        user.input_content('业务负责人', '18646861')
        user.assert_input('业务负责人', '王佳18646861')
        user.input_content('IT负责人', '18653497')
        user.assert_input('IT负责人', '郭程18653497')
        user.click_save_editor()
        DomAssert(drivers).assert_att('编辑卡片成功')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片查看按钮功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的卡片==点击查看")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30864(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        # DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        # user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        time.sleep(2)
        user.click_check()
        user.click_check_quit()
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片启用、停用按钮功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的卡片==点击查看")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30864(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('卡片名称', '测试5')
        user.assert_input('卡片名称', '测试5')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        DomAssert(drivers).assert_att('经营分析')
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_card()
        user.click_share()
        DomAssert(drivers).assert_att('分享')
        user.click_targer()
        user.click_targer1()
        user.click_targersure()
        user.click_explain()
        user.click_explain1()
        user.assert_input('新建说明', '销售年情况')
        user.click_card_explain()
        user.click_card_explain1()
        user.click_card_name()
        user.click_card_name1()
        user.click_created()
        DomAssert(drivers).assert_att('新建卡片成功！')
        DomAssert(drivers).assert_att('测试5')
        time.sleep(2)
        user.click_start()
        user.click_start1()
        user.click_stop()
        user.click_stop1()
        user.click_editor()
        time.sleep(2)
        user.click_save_editor()
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择全部")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30867(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        user.click_initiate_code()
        DomAssert(drivers).assert_att("已启用")
        time.sleep(2)
        user.click_stop_code()
        DomAssert(drivers).assert_att("已停用")
        time.sleep(2)
        user.click_all_code()
        DomAssert(drivers).assert_att("已启用")
        DomAssert(drivers).assert_att("已停用")
        user.click_close_card()
        time.sleep(1)
        user.click_close()



    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片类型搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片搜索框==选择卡片名称、应用类型移动端==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30871(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_menu('卡片管理')
        time.sleep(2)
        user.click_card_code_search()
        user.click_card_code_search1()
        time.sleep(1)
        user.click_search()
        user.click_reset()
        user.click_input_code()
        user.click_input_code1()
        user.click_search()
        DomAssert(drivers).assert_att("移动端")
        time.sleep(1)
        user.click_close_card()
        time.sleep(1)
        user.click_close()



@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_2499:
    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("新建无首页卡片池的角色功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击角色管理新建==输入角色名称==输入角色说明==拥有首页卡片池否==选择菜单报表授权==输入关联用户==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30917(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_system()
        user.click_role()
        user.click_add()
        user.click_rolename()
        time.sleep(1)
        user.click_describe()
        time.sleep(1)
        user.click_menubar()
        user.click_menubar1()
        user.click_savereport()
        user.click_user()
        user.click_user1()
        user.click_user2()
        user.click_user3()
        user.click_save()
        DomAssert(drivers).assert_att("添加角色成功")
        time.sleep(2)
        user.click_rolereset()
        user.click_deleterole()
        user.click_close_role()
        time.sleep(2)
        user.click_close_tables()



    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("新建有首页卡片池的角色功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击角色管理新建==输入角色名称==输入角色说明==拥有首页卡片池是==选择菜单报表授权==输入关联用户==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30918(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_system()
        user.click_role()
        user.click_add()
        time.sleep(1)
        user.click_rolename()
        time.sleep(1)
        user.click_describe()
        time.sleep(1)
        user.click_menubar()
        user.click_menubar1()
        user.click_savereport()
        user.click_user()
        user.click_user1()
        user.click_user2()
        user.click_user3()
        user.click_home_card()
        user.click_home_card1()
        user.click_select()
        user.click_home_card2()
        user.click_save()
        DomAssert(drivers).assert_att("添加角色成功")
        time.sleep(2)
        user.click_rolereset()
        user.click_deleterole()
        user.click_close_role()
        time.sleep(2)
        user.click_close_tables()



    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("批量授权角色")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已有的角色，点击编辑==修改角色名称==修改角色说明==修改拥有首页卡片池否==修改菜单报表授权==修改关联用户==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30920(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_system()
        user.click_role()
        user.click_add()
        time.sleep(1)
        user.click_rolename()
        time.sleep(1)
        user.click_describe()
        time.sleep(1)
        user.click_menubar()
        user.click_menubar1()
        user.click_savereport()
        user.click_user01()
        time.sleep(2)
        user.click_paste
        time.sleep(2)
        user.click_paste1()
        time.sleep(1)
        user.click_paste2()
        user.click_save()
        DomAssert(drivers).assert_att("添加角色成功")
        time.sleep(2)
        user.click_rolereset()
        user.click_deleterole()
        user.click_close_role()
        time.sleep(2)
        user.click_close_tables()



    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("修改角色功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已有的角色，点击编辑==修改角色名称==修改角色说明==修改拥有首页卡片池否==修改菜单报表授权==修改关联用户==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30919(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_system()
        user.click_role()
        user.click_add()
        time.sleep(1)
        user.click_rolename()
        time.sleep(1)
        user.click_describe()
        time.sleep(1)
        user.click_menubar()
        user.click_menubar1()
        user.click_savereport()
        user.click_user()
        user.click_user1()
        user.click_user2()
        user.click_user3()
        user.click_home_card()
        user.click_home_card1()
        user.click_select()
        user.click_home_card2()
        user.click_save()
        DomAssert(drivers).assert_att("添加角色成功")
        user.click_edit_role()
        user.click_user()
        user.click_user1()
        user.click_user02()
        user.click_user2()
        user.click_user3()
        user.click_save()
        DomAssert(drivers).assert_att("编辑角色成功")
        time.sleep(2)
        user.click_rolereset()
        user.click_deleterole()
        user.click_close_role()
        time.sleep(2)
        user.click_close_tables()



    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("角色类型搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击角色搜索框==输入搜索字段==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30921(self, drivers):
        time.sleep(15)
        user = kapianguanli(drivers)
        user.click_system()
        user.click_role()
        user.click_search_role()
        user.click_search_role1()
        user.click_close_role()
        time.sleep(2)
        user.click_close_tables()


if __name__ == '__main__':
    pass
