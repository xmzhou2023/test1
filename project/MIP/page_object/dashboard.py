import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import random
import string

object_name = os.path.basename(__file__).split('.')[0]
menu = Element(pro_name, object_name)


class dashboard(Base):
    """首页"""

    @allure.step("选择首页快捷菜单")
    def choice_shortcutMenu(self, Menu):
        if Menu == "物料主数据":
            self.is_click(menu['快捷菜单'],1,1)
        elif Menu == "BP 主数据":
            self.is_click(menu['快捷菜单'],1,2)
        elif Menu == "价格主数据":
            self.is_click(menu['快捷菜单'],1,3)
        elif Menu == "我的待办":
            self.is_click(menu['快捷菜单'],2,1)
        else:
            logging.info("输入有误，首页无此菜单项")
        logging.info("选择快捷菜单：{}".format(Menu))
        sleep(0.5)

    @allure.step("搜索菜单")
    def search_menu(self, Menu,exactmenu):
        self.is_click(menu['菜单搜索按钮'])
        self.input_text(menu['菜单搜索输入框'],Menu)
        option = self.find_elements(menu['菜单下拉选项'])
        lis = []
        for i in range(len(option)):
            lis.append(option[i].text)
        if exactmenu in lis:
            num = lis.index(exactmenu) + 1
            self.is_click(menu['选择菜单下拉选项'],str(num))
            logging.info("选择菜单：{}".format(exactmenu))
        else:
            self.is_click(menu['可输入下拉框'])
            logging.info("下拉列表无{}此选项，请重新选择".format(exactmenu))
        sleep(1)

if __name__ == '__main__':
    pass
