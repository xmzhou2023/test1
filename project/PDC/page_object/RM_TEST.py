import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserPage(Base):
    """用户类"""

    @allure.step("查找工号")
    def search_user(self, jobnum=None,name=None):
        if jobnum is not None:
            self.readonly_input_text(user['用户管理-工号输入框'], txt=jobnum)
            sleep(2)
            self.is_click(user['用户管理-工号下拉列表'], jobnum)
        if name is not None:
            self.readonly_input_text(user['用户管理-姓名输入框'], txt=name)
            sleep(2)
            self.is_click(user['用户管理-姓名下拉列表'], name)
        self.is_click(user['用户管理-查询'])
        sleep()

    @allure.step("点击菜单")
    def click_menu(self):
        self.is_click_tbm(user['一级菜单'])
        self.is_click_tbm(user['二级菜单'])
        self.refresh()

    @allure.step("分发操作")
    def click_distr(self):
        self.is_click_tbm(user['分发操作'])
        self.is_click_tbm(user['RM分发'])
        self.refresh()

    @allure.step("新增")
    def click_add(self):
        self.is_click_tbm(user['新增'])
        self.is_click_tbm(user['新增-分发角色'])
        self.is_click_tbm(user['分发角色-IT运维人员'])
        self.is_click_tbm(user['新增-分发人员'])
        self.is_click_tbm(user['新增-权限'])
        self.is_click_tbm(user['查看下载'])
        self.is_click_tbm(user['新增-确认'])

if __name__ == '__main__':
    pass
