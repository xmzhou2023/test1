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
    def readonly_input_text(self, locatorText, value, replace):
        """
        replace: xpath里 variable被替换后的值
        value: 输入到文本框的值
        locatorText: 带 variable的xpath
        """
        # self.input_text(user[locatorText], value, replace)
        super().readonly_input_text(user[locatorText], value, replace)

    def input_text(self, locatorText, value, choice=None):
        return super().input_text(user[locatorText], value, choice)

    @allure.step("下拉框信息录入")
    def select_info_input(self, locatorText, value, replace, searchText=''):
        self.is_click(user[locatorText], replace)
        if searchText:
            super().readonly_input_text(user[locatorText], searchText, replace)
            self.is_click(user['dropdown-search-value'], value)

        else:
            self.is_click(user['dropdown-value'], value)


    # def select_info_input(self, locatorText, value, replace, searchText=''):
    #     self.is_click(user[locatorText], replace)
    #     if searchText:
    #         super().readonly_input_text(user[locatorText], searchText, replace)
    #         self.is_click(user['dropdown-search-value'], value)
    #
    #     else:
    #         self.is_click(user['dropdown-value'], value)

if __name__ == '__main__':
    pass
