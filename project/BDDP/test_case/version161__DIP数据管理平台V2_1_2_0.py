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
    @allure.title("新建无首页卡片池的角色功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击角色管理新建==输入角色名称==输入角色说明==拥有首页卡片池否==选择菜单报表授权==输入关联用户==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30917(self, drivers):
        pass


    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("新建有首页卡片池的角色功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击角色管理新建==输入角色名称==输入角色说明==拥有首页卡片池是==选择菜单报表授权==输入关联用户==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30918(self, drivers):
        pass


    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("修改角色功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已有的角色，点击编辑==修改角色名称==修改角色说明==修改拥有首页卡片池否==修改菜单报表授权==修改关联用户==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30919(self, drivers):
        pass


    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("删除角色功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已有的角色，点击编辑==点击删除")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30920(self, drivers):
        pass


    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("角色类型搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击角色搜索框==输入搜索字段==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30921(self, drivers):
        pass


@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_2798:
    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("公开卡片无项指标新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池否==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池否==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30860(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("私有无项指标卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30861(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的卡片==点击编辑==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改卡片组件==修改是否公开==修改首页卡片池==修改下钻报表财务销售经营分析、供应链库存金额==修改分析指标选择2项指标==输入说明18字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30862(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片启用功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的卡片==点击启用==输入申请原因==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30863(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片查看功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的卡片==点击查看")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30864(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片停用功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的卡片==点击停用")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30865(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片已启用的卡片删除功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已启用的卡片==点击编辑==修改卡片信息==保证后再点击删除")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30866(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片类型全部选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择全部")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30867(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片类型已启用选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择已启用")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30868(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片类型已停用选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择已停用")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30869(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("首页卡片池下钻报表搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==搜索下钻报表财务销售经营分析、供应链库存金额")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30870(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片类型搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片搜索框==选择卡片名称、应用类型移动端==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30871(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("卡片模糊搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击模糊搜索框==输入模糊卡片名称、应用类型移动==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30872(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("私有展示'首页'类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池是==选择下钻报表财务销售经营分析==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30873(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("私有多类下钻报表类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30874(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("私有卡片单选项指标新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30875(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("PC端无首页卡片池公开卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型PC端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池否==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30922(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("PC端有首页卡片池公开卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型PC端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30923(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("PC端有首页卡片池私有卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型PC端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开否==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30924(self, drivers):
        pass


    @allure.story("卡片管理增加是否进入首页卡片池")  # 用户故事名称
    @allure.title("PC端无首页卡片池私有卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型PC端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开否==选择首页卡片池否==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择多项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30925(self, drivers):
        pass


@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_3937:
    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("无报表差异化卡片组合报表类型报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域输入业务域==输入业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型总部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析==登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域输入业务域==输入业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型总部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析==登录PC端后台")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28877(self, drivers):
        pass


    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("公开无首页卡片池类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30689(self, drivers):
        pass


    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("私有无首页卡片池卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择一项指标==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30690(self, drivers):
        pass


    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("公开有首页卡片池卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开公开==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择3项指标==输入说明18字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否公开是==选择首页卡片池是==选择下钻报表财务销售经营分析、供应链库存金额==选择分析指标选择3项指标==输入说明18字==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30691(self, drivers):
        pass


    @allure.story("BI单点登录插件改造")  # 用户故事名称
    @allure.title("私有有首页卡片池类型卡片新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有私有==选择首页卡片池否==选择下钻报表财务销售经营分析==选择分析指标选项==输入说明499字==配置英文属性卡片名销售明细，说明销售各类明细==登录PC端后台管理系统==点击卡片管理新建==选择卡片名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择卡片组件分享==选择是否私有是==选择首页卡片池是==选择下钻报表财务销售经营分析==选择分析指标选项==输入说明==配置英文属性卡片名销售明细，说明销售各类明细")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30692(self, drivers):
        pass


if __name__ == '__main__':
    pass
