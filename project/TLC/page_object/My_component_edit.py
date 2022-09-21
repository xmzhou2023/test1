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

    @allure.step('点击')
    def click(self, ymal, choice=None, choice2=None):
        sleep(1)
        if choice2 is None:
            self.is_click_dcr(user[ymal], choice)
            sleep(1)
        else:
            locator = user[ymal]
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('filename', choice2)
            sleep(1)
            self.is_click_dcr(Npath, choice)
            sleep(1)

    @allure.step('处理右击')
    def handle_right_click(self, rYaml, cYaml, select):
        sleep(0.5)
        self.mouse_right_click(user[rYaml])
        self.is_click(user[cYaml], select)

    @allure.step('hover')
    def hover(self, ymal, choice=None):
        self.mouse_hover(user[ymal], choice)



if __name__ == '__main__':
    pass
