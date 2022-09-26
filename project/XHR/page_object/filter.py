import time

import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class Filter(Base):
    """用户类"""

    @allure.step("进入职员管理")
    def click_menu(self, metatitle):
        self.is_click(user['XHR'])
        self.is_click(user['一级菜单'], metatitle)
        logging.info(f'点击一级菜单：{metatitle}')
        time.sleep(1)
        self.is_click(user['职员管理'])
        logging.info(f'点击二级菜单：职员管理')

    @allure.step("点击筛选按钮")
    def click_filter(self):
        self.is_click(user['筛选按钮'])

    @allure.step("输入筛选数据")
    def input_filter_info(self, txt, location, choice=None):
        if location == '计划转正日期':
            self.input_text(user['开始日期'], txt, location)
            self.input_text(user['结束日期'], txt, location)
        elif location == "员工组" or location == "员工状态":
            self.is_click(user['筛选公共'], location)
            self.is_click(user['员工组或员工状态'], txt)
        else:
            self.input_text(user['筛选公共'], txt, location)

    @allure.step("点击查询")
    def click_search(self, location):
        time.sleep(1)
        self.is_click(user["查询和重置"], location)

    @allure.step("点击叉号")
    def click_error(self):
        self.is_click(user['叉号'])
        time.sleep(1)

    @allure.step("点击更多")
    def click_more(self, location):
        self.is_click(user['勾选'])
        time.sleep(1)
        self.is_click(user['更多'])
        self.is_click(user['导出'], location)

    @allure.step("重置")
    def click_reset(self, location):
        self.is_click(user['筛选按钮'])
        self.is_click(user["查询和重置"], location)
        self.is_click(user['叉号'])

if __name__ == '__main__':
    pass
