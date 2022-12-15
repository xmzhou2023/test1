import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.xHR.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class DimensionScheme(CenterComponent):
    """维度方案"""

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

    @allure.step("点击维度方案")
    def menu(self):
        self.refresh()
        self.hover_click(user['悬停xHR'])
        sleep(1)
        self.is_click(user['测评中心'])
        self.is_click(user['维度方案'])
        sleep(3)

    @allure.step("新增")
    def dimension_add(self):
        self.is_click(user['新增按钮'])

    @allure.step("输入名称")
    def input_demensionname(self, name):
        self.input_text(user['输入名称'], name)

    @allure.step("选择类型")
    def select_set(self, a, b):
        self.is_click(user['输入框'], a)
        self.is_click(user['设置选项值'], b)


    @allure.step("保存")
    def click_save(self):
        self.is_click(user['确定按钮'])

    @allure.step("勾选选项")
    def check_box(self, name):
        self.is_click(user['勾选复选框'], name)

    @allure.step("删除")
    def delete_dimension(self):
        self.is_click(user['删除'])
        self.is_click(user['二次确认'])





if __name__ == '__main__':
    pass
