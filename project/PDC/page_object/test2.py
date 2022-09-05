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
    def click_menu(self, metatitle, nestmenu):
        self.is_click(user['产品任命'], metatitle)
        logging.info(f'点击产品任命：{metatitle}')
        self.is_click(user['区域产品概述'], nestmenu)
        logging.info(f'点击区域产品概述：{nestmenu}')
        sleep(1)
        self.refresh()

    @allure.step("分发")
    def click_ff(self):
        self.is_click(user['分发'])
        self.refresh()
        sleep(1)

    @allure.step("新增")
    def click_xz(self):
        self.is_click(user['新增'])
        sleep(1)

    @allure.step("分发角色")
    def click_js(self,choice):
        self.is_click(user['分发角色'])
        self.is_click(user['角色'],choice)
        sleep(1)

    @allure.step("分发人员")
    def click_ry(self, choice):
        self.is_click(user['分发人员'])
        self.is_click(user['分发人员-姓名'], choice)
        sleep(1)

    @allure.step("确定")
    def click_qd(self):
        self.is_click(user['确定'])
        sleep(1)

    @allure.step("提交分发")
    def click_tjff(self):
        self.is_click(user['提交分发'])
        sleep(1)

    @allure.step("提交分发确定")
    def click_ffqd(self):
        self.is_click(user['分发确定'])
        sleep(1)

    @allure.step("提交最后确定")
    def click_zhqd(self):
        self.is_click(user['最后确定'])
        sleep(1)
if __name__ == '__main__':
    pass
