import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class Busfields(Base):
    """用户类"""
    @allure.step("查找工号")
    def search_user(self, jobnum=None, name=None):
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
        self.refresh()
        self.is_click(user['xHr'])
        self.is_click(user['中方入职'])
        self.is_click(user['业务字段'])

    @allure.step("点击新增比例按钮")
    def click_NewCandidate(self):
        self.is_click_tbm(user['点击新增'])

    @allure.step("输入文本")
    def input_Proportion(self, type1, txt):
        # input_type = ['月固', '月浮', '季度', '年度']
        self.input_text(user['比例文本框输入'], txt, type1)

    @allure.step("点击停用按钮")
    def input_Deactivate(self, type2):
        self.is_click_tbm(user['点击停用'], type2)

    @allure.step("点击编辑按钮")
    def input_Deiting(self, type3):
        self.is_click_tbm(user['点击编辑'], type3)

    @allure.step("点击删除按钮")
    def input_Deleteing(self, type4):
        self.is_click_tbm(user['点击删除'], type4)
        self.is_click_tbm(user['弹窗删除确定按钮'])

    @allure.step("点击删除按钮")
    def input_Deleteing2(self, type5):
        self.is_click_tbm(user['点击删除'], type5)

    @allure.step("确定按钮")
    def input_Adding(self):
        self.is_click_tbm(user['弹窗新增保存按钮'])

    @allure.step("取消按钮")
    def input_Quing(self):
        self.is_click_tbm(user['弹窗新增取消按钮'])


if __name__ == '__main__':
    pass
