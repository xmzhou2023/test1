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

    def __init__(self, drivers, productType='产成品'):
        super(UserPage, self).__init__(drivers)
        # 产成品 | 单机头
        self.productType = productType
    def replaceXpath(self, arr, placeholder, replace):
        return tuple([arr[0], arr[1].replace(placeholder, replace)])

    @allure.step("查找工号")
    def search_user(self, jobnum=None, name=None):
        if jobnum is not None:
            super().readonly_input_text(user['用户管理-工号输入框'], txt=jobnum)
            sleep(2)
            self.is_click(user['用户管理-工号下拉列表'], jobnum)
        if name is not None:
            super().readonly_input_text(user['用户管理-姓名输入框'], txt=name)
            sleep(2)
            self.is_click(user['用户管理-姓名下拉列表'], name)
        self.is_click(user['用户管理-查询'])
        sleep()

    @allure.step("点击按钮")
    def click(self, locatorText, s=None):
        self.is_click(user[locatorText], s)

    @allure.step("下拉框信息录入")
    def select_info_input(self, locatorText, value, replace, searchText=''):
        self.is_click(user[locatorText], replace)
        if searchText:
            super().readonly_input_text(user[locatorText], searchText, replace)
            self.is_click(user['dropdown-search-value'], value)

        else:
            self.is_click(user['dropdown-value'], value)

    @allure.step("输入框信息录入")
    def readonly_input_text(self, locatorText, value, replace):
        """
        replace: xpath里 variable被替换后的值
        value: 输入到文本框的值
        locatorText: 带 variable的xpath
        """
        super().readonly_input_text(user[locatorText], value, replace)

    @allure.step("获取流程编码")
    def getText(self, productCode=None, s='整机BOM协作'):
        dictMap = {
            "整机BOM协作": "2",
            "单机头BOM协作": "3",
        }
        xpathArr = self.replaceXpath(user['流程编码'], 'placeholder', dictMap[s])
        return self.element_text(xpathArr, productCode)

    @allure.step("进入iframe")
    def switch_iframe(self, path):
        self.frame_enter(user[path])

    def user_selector(self, userSelectLabel, employeeNo):
        """
        userSelector: 用户选择器所在的form label
        employeeNo: 员工工号
        """
        self.is_click(user['form-input'], userSelectLabel)
        # 对话框里的结构是固定的
        self.input_text(user['输入用户名'], employeeNo)
        self.is_click(user['选择用户'], employeeNo)
        self.is_click(user['选择用户-确定'])


    # enter_iframe
    # switch_window 传入索引
    # close_switch 传入索引
    # element_text 获取元素的文字
    # DomAssert(dirvers).assert_att('页面文字')


if __name__ == '__main__':
    pass
