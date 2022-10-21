import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class QueryCountry(Base):
    """查询国家类"""

    @allure.step("输入国家")
    def input_country(self,country):
        self.is_click_tbm(user['国家城市输入框'])
        sleep(1)
        self.input_text(user['国家城市输入框'],country)
        sleep(2)
        self.is_click_tbm(user['选择国家'],country)

    @ allure.step("查询国家")
    def query_country(self):
        self.is_click_tbm(user['查询按钮'])

class ExportCountryCity(Base):
    """导出国家城市列表类"""

    @allure.step("点击导出按钮")
    def click_export(self):
        self.is_click_tbm(user['导出'])


if __name__ == '__main__':
    pass
