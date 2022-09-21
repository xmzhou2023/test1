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


class EmployeeFiles(Base):
    """用户类"""

    @allure.step("进入职员管理")
    def click_menu(self, metatitle):
        self.is_click(user['XHR'])
        self.is_click(user['一级菜单'], metatitle)
        logging.info(f'点击一级菜单：{metatitle}')
        time.sleep(1)
        self.is_click(user['职员管理'])
        logging.info(f'点击二级菜单：职员管理')
        time.sleep(5)

    @allure.step("点击员工档案")
    def click_files(self):
        self.is_click(user['员工档案'])

    @allure.step("导出档案")
    def export_files(self):
        self.is_click(user['导出档案'])

    @allure.step("导出Excel")
    def export_excel(self):
        self.is_click(user['导出Excel'])


if __name__ == '__main__':
    pass
