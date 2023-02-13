import time
import json
import requests
from selenium.webdriver import ActionChains

from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class BPM_authorized_Page(Base):
    pass  # 编辑分管授权_保存成功提示

    @allure.step("流程授权面，在权限搜索输入框输入查询内容")
    def input_name(self, content):
        self.input_text(user['权限搜索输入框'], txt=content)

    @allure.step("流程授权面，点击——第一行权限描述a链接")
    def click_Link(self):
        self.is_click_tbm(user['第一行权限描述a链接'])

    @allure.step("流程授权_编辑分管授权界面，点击_选择流程按钮")
    def click_choose(self):
        self.is_click_tbm(user['选择流程按钮'])

    @allure.step("流程授权_选择流程界面_输入框输入文字")
    def input_process(self, content):
        self.input_text(user['选择流程_输入框'], txt=content)

    @allure.step("点击_选择流程界面下的_查询按钮")
    def click_InquireA(self):
        self.is_click_tbm(user['选择流程_查询按钮'])

    @allure.step("点击_查询出的流程第一行勾选框")
    def click_tick(self):
        self.is_click_tbm(user['查询出的流程第一行勾选框'])

    @allure.step("点击选择流程下的_确定")
    def click_yes(self):
        self.is_click_tbm(user['选择流程_确定'])

    @allure.step("流程定义界面，点击编辑分管授权_流程名称的全部")
    def click_all(self):
        self.is_click_tbm(user['编辑分管授权_流程名称的全部'])

    @allure.step("流程定义界面，点击编辑分管授权_保存按钮")
    def click_save(self):
        self.is_click_tbm(user['编辑分管授权_保存'])

    @allure.step("点击流程授权的保存按钮，判断流程授权是否成功，")
    def ismodeling_authorized(self):
        itexis = self.element_exist(user["编辑分管授权_保存成功提示"])
        return itexis

    @allure.step("控制键盘，直接点击任意想点击的键盘，一般用于点回车")
    def keyboard(self, drivers, value):
        """控制键盘，直接点击任意想点击的键盘"""
        ActionChains(drivers).send_keys(value).perform()
