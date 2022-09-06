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

    def replaceXpath(self, arr, placeholder, replace):
        return tuple([arr[0], arr[1].replace(placeholder, replace)])

    @allure.step("跳转路由")
    def switch_location(self, url):
        super().switch_location(url)

    @allure.step("点击按钮")
    def click(self, locatorText, s=None, replace=''):
        res = user[locatorText]
        if replace:
            res = self.replaceXpath(res, 'placeholder', replace)
        self.is_click(res, s)

    @allure.step("输入框信息录入")
    def input_text(self, locatorText, value, replace):
        """
        replace: xpath里 variable被替换后的值
        value: 输入到文本框的值
        locatorText: 带 variable的xpath
        """
        super().input_text(user[locatorText], value, replace)

    @allure.step("进入iframe")
    def frame_enter(self, xpath):
        return super().frame_enter(user[xpath])
    # def input_text(self, locatorText, value, choice=None):
    #     return super().input_text(user[locatorText], value, choice)

    @allure.step("下拉框信息录入")
    def select_info_input(self, locatorText, value, replace, searchText=False):
        self.is_click(user[locatorText], replace)
        if searchText:
            super().readonly_input_text(user[locatorText], '自动化测试评估', replace)
            self.is_click(user['自动化测试评估方案'], value)

        else:
            self.is_click(user['dropdown-value'], value)

if __name__ == '__main__':
    pass
