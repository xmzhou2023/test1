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
from project.BDDP.page_object.数据管理平台_卡片管理 import kapianguanli
from public.base.assert_ui import DomAssert


@allure.feature("数据管理平台_849_卡片管理_850")  # 迭代名称
class Teststory_3937:
    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("无报表差异化卡片组合报表类型报表新建验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域输入业务域;步骤5:输入业务负责人.业务组织IT负责人;步骤6:选择页面来源定制;步骤7:选择报表首页差异化是;步骤8:选择报表类型总部;步骤9:进入角色管理中心进行数据授权;步骤10:来源卡片财务销售事业分析部私有化卡片;步骤11:访问地址:输入外部地址;步骤12:选择指标财务销售事业分析部;步骤13:说明销售事业公析;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28877(self, drivers):
        pass


    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("公开无首页卡片池类型卡片新建验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击卡片管理新建;步骤3:选择卡片名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择卡片组件分享;步骤7:选择是否公开是;步骤8:选择首页卡片池否;步骤9:选择下钻报表财务销售经营分析供应链库存金额;步骤10:选择分析指标选项;步骤11:输入说明;步骤12:配置英文属性卡片名销售明细，说明销售各类明细;")  # 用例描述
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
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击卡片管理新建;步骤3:选择卡片名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择卡片组件分享;步骤7:选择是否公开否;步骤8:选择首页卡片池否;步骤9:选择下钻报表财务销售经营分析供应链库存金额;步骤10:选择分析指标选择一项指标;步骤11:输入说明;步骤12:配置英文属性卡片名销售明细，说明销售各类明细;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30690(self, drivers):
        time.sleep(30)
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
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击卡片管理新建;步骤3:选择卡片名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择卡片组件分享;步骤7:选择是否公开是;步骤8:选择首页卡片池是;步骤9:选择下钻报表财务销售经营分析供应链库存金额;步骤10:选择分析指标选择3项指标;步骤11:输入说明18字;步骤12:配置英文属性卡片名销售明细，说明销售各类明细;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30691(self, drivers):
        time.sleep(30)
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



    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("私有有首页卡片池类型卡片新建验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击卡片管理新建;步骤3:选择卡片名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择卡片组件分享;步骤7:选择是否私有是;步骤8:选择首页卡片池是;步骤9:选择下钻报表财务销售经营分析;步骤10:选择分析指标选项;步骤11:输入说明;步骤12:配置英文属性卡片名销售明细，说明销售各类明细;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30692(self, drivers):
        time.sleep(30)
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



if __name__ == '__main__':
      pass
