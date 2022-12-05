import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AddRole(Base):
    """新增角色类"""

    @allure.step("点击新增")
    def click_add(self):
        self.scroll_into_view(user['新增按钮'])
        self.is_click_tbm(user['新增按钮'])

    @allure.step("输入角色名称")
    def input_rolename(self,rolename):
        self.is_click_tbm(user['角色名称输入框'])
        self.input_text(user['角色名称输入框'],rolename)

    @allure.step("选择角色组")
    def switch_role(self,role):
        self.is_click_tbm(user['角色组选择框'])
        self.is_click_tbm(user['选择角色'],role)

    @allure.step("输入备注")
    def input_remarks(self,remark):
        self.is_click_tbm(user['备注框'])
        self.input_text(user['备注框'],remark)

    @allure.step("点击提交")
    def click_submit(self):
        self.is_click_tbm(user['提交按钮'])

    @allure.step("新增数据删除")
    def delete_data(self,role):
        self.is_click_tbm(user['选择新增的角色组'],role)
        sleep(2)
        self.is_click_tbm(user['禁用按钮'])
        sleep(2)
        self.is_click_tbm(user['二次弹窗确定'])

    @allure.step("关闭弹窗")
    def click_close(self):
        self.is_click_tbm(user['关闭弹窗按钮'])

class DisableRole(Base):
    """禁用角色类"""

    @allure.step("选择角色禁用")
    def disable_role(self, role):
        self.is_click_tbm(user['选择新增的角色组'], role)
        sleep(2)
        self.is_click_tbm(user['禁用按钮'])
        sleep(2)
        self.is_click_tbm(user['二次弹窗确定'])

class EditRole(Base):
    """编辑角色类"""
    @allure.step("选择角色")
    def switch_role(self,role):
        self.is_click_tbm(user['选择角色组'],role)
        sleep(3)

    @allure.step("点击编辑")
    def click_edit(self):
        self.is_click_tbm(user['编辑按钮'])

    @allure.step("编辑角色名称")
    def input_rolename(self, rolename):
        self.is_click_tbm(user['角色名称输入框'])
        self.input_text(user['角色名称输入框'], rolename)

    @allure.step("编辑提交")
    def click_submit(self):
        self.is_click_tbm(user['编辑提交按钮'])



if __name__ == '__main__':
    pass
