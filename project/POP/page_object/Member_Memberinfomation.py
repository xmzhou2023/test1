import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class QueryMember(Base):
    """查询会员类"""

    @allure.step("输入单个手机号")
    def input_phone(self,phone):
        self.is_click(user['手机输入框'])
        # sleep(5)
        self.input_text(user['输入手机号'],phone)
        sleep(2)
        self.is_click(user['手机号'],phone)

    @allure.step("点击查询")
    def click_query(self):
        self.is_click(user['查询按钮'])


if __name__ == '__main__':
    pass
