import time
import json
import requests
from libs.common.read_element import Element
from project.OA.page_object.OA_login import OAdnluPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from public.libs.unified_login.login import Login
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class BPM_PCform_Page(Base):
    """
    PC表单界面操作
    """

    @allure.step("点击PC表单下的【添加_设置分类_导入导出_批量更新按钮】按钮")
    def click_add(self, variables):
        self.is_click_tbm(user['添加_设置分类_导入导出_批量更新按钮'], variables)

    @allure.step("选择业务对象_输入框输入文字")
    def input_enter(self, content):
        self.input_text(user['选择业务对象_搜索输入框'], txt=content)

    @allure.step("选择业务对象_点击【查询_重置】按钮")
    def click_Inquire(self, variables):
        self.is_click_tbm(user['查询_重置按钮'], variables)

    @allure.step("选择业务对象_点击第一列勾选框")
    def click_tick(self):
        self.is_click_tbm(user['选择业务对象_第一列勾选框'])

    @allure.step("选择业务对象_点击确定按钮")
    def click_yes(self):
        self.is_click_tbm(user['选择业务对象_确定按钮'])

    @allure.step("选择表单模板弹窗_点击模板生成按钮")
    def click_template(self):
        self.is_click_tbm(user['模板生成'])

    @allure.step("选择表单模板弹窗_点击确定按钮")
    def click_template_ok(self):
        self.is_click_tbm(user['初始化模板_确定'])

    @allure.step("PC表单设计_保存按钮")
    def click_save(self):
        self.is_click_tbm(user['PC表单设计_保存按钮'])

    @allure.step("判断PC表单保存是否成功")
    def ismodeling_save(self):
        itexis = self.element_exist(user["PC表单设计_保存成功提示语"])
        return itexis

    @allure.step("PC表单_输入框输入文字")
    def input_PCenter(self, content):
        self.input_text(user['PC表单输入框'], txt=content)

    @allure.step("PC表单设计_点击搜索按钮")
    def click_PCrelease(self):
        self.is_click_tbm(user['PC表单输入框_搜索按钮'])

    @allure.step("PC表单设计_点击方框一行名称文")
    def click_name(self):
        self.is_click_tbm(user['PC表单_选择方框一行名称文'])

    @allure.step("PC表单设计_发布按钮")
    def click_release(self):
        self.is_click_tbm(user['PC表单设计_发布'])

    @allure.step("判断PC表单第一次发布是否成功")
    def ismodeling_release(self):
        itexis = self.element_exist(user["PC表单设计_第一次发布版本成功提示语"])
        return itexis
