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

    @allure.step("查找工号")
    def click_primary(self):
        self.is_click_tbm(user['主题域'])

    @allure.step("查找工号")
    def assert_input(self, header, content):
        if header == '主题域' or header == '业务组织':
            ac_content = self.element_text(user['输入框内容2'], header)
            ValueAssert.value_assert_equal(ac_content, content)
        elif header == '新建说明':
            ac_content = self.element_input_text(user['输入框内容3'], header)
            ValueAssert.value_assert_equal(ac_content, content)
        elif header == '英文属性说明':
            ac_content = self.element_input_text(user['输入框内容4'], header)
            ValueAssert.value_assert_equal(ac_content, content)
        else:
            ac_content = self.element_input_text(user['输入框内容'], header)
            ValueAssert.value_assert_equal(ac_content, content)

if __name__ == '__main__':
    pass
