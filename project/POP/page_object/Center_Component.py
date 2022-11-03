import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class NavPage(Base):

    @allure.step("前往菜单")
    def click_gotonav(self, *content,):
        """前往菜单"""
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            self.is_click_tbm(user[level[i]])
        sleep(1)
        # 点击重置按钮是为了刷新取消模块浮窗
        self.is_click(user['系统通用重置按钮'])
        sleep(1)


class SpecialNavPage(Base):
    """特殊模块无重置按钮时点击模块的方法，例：角色管理，用户权限"""
    @allure.step("前往菜单")
    def click_gotonav(self, *content,):
        """前往菜单"""
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            self.is_click_tbm(user[level[i]])
        sleep(1)
        # 点击刷新是为了刷新取消模块浮窗
        self.refresh()
        sleep(5)




if __name__ == '__main__':
    pass
    # a = NavPage(driver)
    # a.click_gotonav("组织","职员管理")