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
    @allure.step('导航菜单')
    def click_menu(self, fType, sType):
        self.mouse_hover(user['一级菜单'], fType)
        self.is_click(user['二级菜单'], sType)
        self.refresh()

    @allure.step('hover')
    def hover(self, ymal, choice=None):
        self.mouse_hover(user[ymal], choice)

    @allure.step('点击')
    def click(self, ymal, choice=None):
        sleep(1)
        self.is_click_dcr(user[ymal], choice)
        sleep(2)

    @allure.step('输入')
    def input(self, ymal, txt, choice=None):
        self.input_text(user[ymal], txt, choice)

    @allure.step('跳转窗口')
    def handle_switch_window(self, n):
        self.switch_window(n)


if __name__ == '__main__':
    pass
