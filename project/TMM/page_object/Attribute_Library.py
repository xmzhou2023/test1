import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AttributeLibraryPage(Base):
    """属性库"""

    @allure.step("进入属性库页面")
    def goto_AttributeLibrary(self):
        self.is_click(user['业务配置'])
        AttributeLibrary = self.find_element(user['属性库模块']).text
        sleep(1)
        self.is_click(user['属性库模块'])
        self.move_house(self.driver)
        sleep(1)
        return AttributeLibrary

    @allure.step("新增属性")
    def AddAttribute(self, AttributeName, AttributeId, EntityName):
        AttrStowButton = self.element_exist(user['属性收起按钮'], EntityName)
        if AttrStowButton:
            self.is_click(user['属性收起按钮'], EntityName)
        sleep(2)
        Attr = self.element_exist(user['属性'], AttributeName)
        while Attr:
            AttributeName = AttributeName + '1'
            AttributeId = AttributeId + '1'
            Attr = self.element_exist(user['属性'], AttributeName)
        sleep(2)
        self.hover(user['实体'], EntityName)
        self.is_click(user['属性新增按钮'], EntityName)
        self.input_text(user['属性新增输入框'], AttributeName)
        self.hover(user['属性新增输入框'])
        self.is_click(user['属性新增确认按钮'])
        SapId = self.find_element(user['SAP属性编码title']).text
        self.input_text(user['SAP属性编码输入框'], AttributeId)
        self.is_click(user['属性保存按钮'])
        sleep(1)
        return SapId


    @allure.step("编辑属性")
    def EditAttribute(self, AttrName, AttrDescribe, EntityName):
        AttrStowButton = self.element_exist(user['属性收起按钮'], EntityName)
        if AttrStowButton:
            self.is_click(user['属性收起按钮'], EntityName)
        sleep(2)
        element = self.find_element(user['属性名称按钮'], AttrName)
        self.driver.execute_script("arguments[0].click();", element)
        SapId = self.find_element(user['SAP属性编码title']).text
        self.input_text(user['属性描述输入框'], AttrDescribe)
        self.is_click(user['属性保存按钮'])
        sleep(1)
        return SapId

    @allure.step("属性搜索")
    def SearchAttribute(self, AttrName):
        sleep(1)
        self.is_click(user['搜索按钮'])
        self.input_text(user['搜索输入框'], AttrName)
