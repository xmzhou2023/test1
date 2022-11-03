import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class CenterComponent(Base):
    """用户类"""

    def hover(self,locator, *choice):
        """鼠标悬停"""
        sleep(1)
        element = self.find_element(locator, *choice)
        # 创建Action对象
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(1)

    @allure.step("筛选")
    def assess_search(self):
        self.is_click(user['筛选按钮'])

    @allure.step("输入筛选条件")
    def assess_inputinfo(self,name):
        self.input_text(user['测评类型筛选项'], name)

    @allure.step("点击查询按钮")
    def click_searchbutton(self):
        self.is_click(user['查询按钮'])
        self.is_click(user['关闭按钮'])

    @allure.step("断言查询结果")
    def assert_search(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格内容'], header, content)


if __name__ == '__main__':
    pass
