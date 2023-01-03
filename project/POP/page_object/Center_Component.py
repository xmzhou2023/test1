import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *
from public.base.basics import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class NavPage(Base):
    """随机点击菜单模块"""

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
        sleep(3)
        # 点击重置按钮是为了刷新取消模块浮窗
        self.is_click(user['重置按钮'])
        sleep(5)

class SpecialNavPage(Base):
    """特殊模块无重置按钮时点击模块的方法，例：角色管理，用户权限"""
    @allure.step("前往菜单")
    def click_gotonav(self, *content):
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

# 页面通用按钮
class General_button(Base):
    """页面通用按钮点击"""
    @allure.step("点击查询")
    def query(self):
        self.is_click_tbm(user['查询按钮'])

    @allure.step("点击新增")
    def add(self):
        self.is_click_tbm(user['新增按钮'])

    @allure.step("点击更多")
    def more(self):
        self.is_click_tbm(user['更多按钮'])

    @allure.step("点击重置")
    def reset(self):
        self.is_click_tbm(user['重置按钮'])

    @allure.step("点击更多查询")
    def more_query(self):
        self.is_click_tbm(user['更多查询'])

class Page_Operation(Base):
    """页面操作流程"""

    @allure.step("页面输入查询条件")   # 输入框条件查询
    def single_condition_input_boxquery(self,ele1,ele2,content):
        self.is_click_tbm(user[ele1])
        sleep()
        self.input_text(user[ele1],content)
        sleep()
        self.is_click_tbm(user[ele2],content)
        sleep()

    @allure.step("页面输入日期段")
    def date_range(self,ele1,ele2,startdate,enddate):
        self.is_click_tbm(user[ele1])
        sleep()
        self.input_text(user[ele1],startdate)
        sleep()
        self.is_click_tbm(user[ele2])
        sleep()
        self.input_text(user[ele2],enddate)

    @allure.step("页面输入框内容输入新增")
    def add_input_box(self,ele,content):
        self.input_text(user[ele], content)
        sleep()

    @allure.step("页面输入选择框新增")
    def add_input_selection_box(self,ele1,ele2,content):
        self.is_click_tbm(user[ele1])
        sleep()
        self.input_text(user[ele1],content)
        sleep()
        self.is_click_tbm(user[ele2],content)
        sleep()


if __name__ == '__main__':
    pass
    # a = NavPage(driver)
    # a.click_gotonav("组织","职员管理")