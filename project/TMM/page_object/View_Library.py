import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ViewLibraryPage(Base):
    """视图库"""

    @allure.step("进入视图库页面")
    def goto_ViewLibrary(self):
        self.is_click(user['业务配置'])
        ViewLibrary = self.find_element(user['视图库模块']).text
        self.is_click(user['视图库模块'])
        sleep(1)
        self.move_house(self.driver)
        sleep(1)
        return ViewLibrary

    @allure.step("新增视图")
    def AddView(self, ViewName ,EntityName):
        ViewStowButton = self.element_exist(user['视图收起按钮'], EntityName)
        if ViewStowButton:
            self.is_click(user['视图收起按钮'], EntityName)
        sleep(1)
        view = self.element_exist(user['视图'], ViewName)
        while view:
            ViewName = ViewName + '1'
            view = self.element_exist(user['视图'], ViewName)
        self.hover(user['实体'], EntityName)
        self.is_click(user['视图新增按钮'], EntityName)
        self.input_text(user['视图新增输入框'], ViewName)
        self.hover(user['视图新增输入框'])
        self.is_click(user['视图新增确认按钮'])
        ViewButton = self.find_element(user['默认视图设置按钮']).text
        self.is_click(user['视图保存按钮'])
        return ViewButton

    @allure.step("编辑视图")
    def EditView(self, ViewName):
        self.input_text(user['视图名称输入框'], ViewName)
