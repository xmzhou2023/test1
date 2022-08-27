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
        self.is_click(user['一级菜单'], metatitle)
        logging.info(f'点击一级菜单：{metatitle}')
        self.is_click(user['二级菜单'], nestmenu)
        logging.info(f'点击二级菜单：{nestmenu}')
        sleep(1)
        self.refresh()

    @allure.step("输入制作类型")
    def input_make(self, txt):
        self.readonly_input_text(user['制作类型查询'], txt)
        sleep()

    @allure.step("点击查询按钮")
    def click_search(self):
        self.is_click(user['查询按钮'])
        sleep()

    # @allure.step("点击查询按钮")
    # def click_search(self, txt):
    #     self.is_click(user['查询按钮'])
    #     sleep()
if __name__ == '__main__':
    pass
