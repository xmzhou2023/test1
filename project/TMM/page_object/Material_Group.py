import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class MaterialGroupPage(Base):
    """物料组"""

    @allure.step("进入物料组页面")
    def goto_MaterialGroup(self):
        self.is_click(user['业务配置'])
        MaterialGroup = self.find_element(user['物料组模块']).text
        self.is_click(user['物料组模块'])
        self.is_click(user['物料组查询按钮'])
        sleep(1)
        return MaterialGroup

    @allure.step("实体名称查询")
    def EntityNameQuery(self, EntityName):
        self.is_click(user['实体名称查询下拉框'])
        self.is_click(user['实体名称下拉选项'], EntityName)
        self.is_click(user['物料组查询按钮'])
        sleep(1)


    @allure.step("物料组查询")
    def MaterialGroupQuery(self, MaterialGroup):
        self.input_text(user['物料组查询输入框'], MaterialGroup)
        self.is_click(user['物料组查询按钮'])
        sleep(1)

    @allure.step("物料组名称查询")
    def MaterialGroupNameQuery(self, MaterialGroupName):
        self.input_text(user['物料组名称查询输入框'], MaterialGroupName)
        self.is_click(user['物料组查询按钮'])
        sleep(1)

    @allure.step("数据来源查询")
    def DataFromQuery(self, DataFrom):
        self.is_click(user['数据来源查询下拉框'])
        self.is_click(user['数据来源下拉选项'], DataFrom)
        self.is_click(user['物料组查询按钮'])
        sleep(1)

    @allure.step("查询重置")
    def Reset(self):
        self.is_click(user['重置按钮'])
        sleep(1)

    @allure.step("新增物料组")
    def AddMaterialGroup(self,EntityName,MaterialGroup,MaterialGroupName,MaterialGroupDescribe):
        self.is_click(user['物料组新增按钮'])
        AddMaterialGroupTitle = self.find_element(user['新增弹窗title']).text
        self.is_click(user['新增实体名称下拉框'])
        self.is_click(user['新增实体名称下拉选项'], EntityName)
        self.input_text(user['新增物料组输入框'], MaterialGroup)
        self.input_text(user['新增物料组名称输入框'], MaterialGroupName)
        self.input_text(user['新增物料组描述输入框'], MaterialGroupDescribe)
        self.is_click(user['新增保存按钮'])
        sleep(1)
        return AddMaterialGroupTitle


    @allure.step("查看物料组")
    def MaterialGroupView(self):
        self.is_click(user['物料组查看按钮'])
        ViewMaterialGroupTitle = self.find_element(user['查看弹窗title']).text
        self.is_click(user['查看返回按钮'])
        sleep(1)
        return ViewMaterialGroupTitle

    @allure.step("刷新SAP最新物料组")
    def MaterialGroupFresh(self):
        sleep(5)
        self.is_click(user['刷新SAP最新物料组按钮'])
        sleep(1)