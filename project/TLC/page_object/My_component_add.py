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

    @allure.step('导航菜单')
    def click_menu(self, fType, sType):
        self.mouse_hover(user['一级菜单'], fType)
        self.is_click(user['二级菜单'], sType)
        self.refresh()

    @allure.step('处理输入')
    def input(self, yaml, txt, choice=None):
        self.input_text(user[yaml], txt, choice)

    @allure.step('处理点击')
    def click(self, yaml, choice = None):
        sleep(1)
        self.is_click_dcr(user[yaml], choice)
        sleep(2)

    @allure.step('hover')
    def hover(self, ymal, choice = None):
        self.mouse_hover(user[ymal], choice)



if __name__ == '__main__':
    pass
