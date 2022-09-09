import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

# class UserPage(Base):
#     """用户类"""
#
#     @allure.step("查找工号")
#     def search_user(self, jobnum=None,name=None):
#         if jobnum is not None:
#             self.readonly_input_text(user['用户管理-工号输入框'], txt=jobnum)
#             sleep(2)
#             self.is_click(user['用户管理-工号下拉列表'], jobnum)
#         if name is not None:
#             self.readonly_input_text(user['用户管理-姓名输入框'], txt=name)
#             sleep(2)
#             self.is_click(user['用户管理-姓名下拉列表'], name)
#         self.is_click(user['用户管理-查询'])
#         sleep()


class Tool(Base):
    @allure.step('点击')
    # TODO: yaml
    def click(self, yaml, choice=None):
        sleep(0.5)
        self.is_click(user[yaml], choice)

    @allure.step('点击新增按钮下的文件夹')
    def click_addButton_select(self):
        self.is_click(user['新增文件夹'])

    @allure.step('点击我的空间或公共空间')
    def click_space(self, Type):
        self.is_click(user['空间'], Type)

    @allure.step('导航菜单')
    def click_menu(self, fType, sType):
        self.mouse_hover(user['一级菜单'], fType)
        self.is_click(user['二级菜单'], sType)
        self.refresh()

    @allure.step('hover新增按钮')
    def hover(self):
        self.mouse_hover(user['新增'])
        self.is_click(user['新增文件夹'])

    @allure.step('双击元素')
    def double_click(self, yaml):
        self.double_click(user[yaml])

    @allure.step('点击确定')
    def confirm_click(self):
        self.is_click(user['添加-确定'])

    @allure.step('输入框')
    def input(self, type, txt, yamlStr=None):
        self.input_text(user[type], txt, yamlStr)

    @allure.step('右键点击')
    def handle_button_right_click(self):
        self.mouse_right_click(user['文件Item'])
        self.is_click(user['右键操作'])

    @allure.step('readonly输入')
    def readonly_input(self, yaml, txt):
        self.readonly_input_text(user[yaml], txt)

if __name__ == '__main__':
    pass
