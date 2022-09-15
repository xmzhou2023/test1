import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AddUser(Base):
    """新增职员类"""

    @allure.step("点击新增按钮")
    def click_add_button(self):
        self.is_click(user['新增按钮'])

    @allure.step("输入用户名")
    def input_username(self,content):
        self.input_text(user['用户名输入框'],content)

    @allure.step("选择归属组织")
    def switch_division(self,variable):
        self.is_click(user['归属组织选择框'])
        self.is_click(user['职员组织'],variable)

    @allure.step("选择区域")
    def switch_region(self,variable):
        self.is_click(user['区域选择框'])
        self.input_text(user['区域选择框'],variable)
        self.is_click(user['职员区域'],variable)

    @allure.step("选择角色")
    def switch_role(self,variable):
        self.is_click(user['角色选择框'])
        self.input_text(user['角色选择框'],variable)
        self.is_click(user['职员角色'],variable)

    @allure.step("选择国家")
    def switch_country(self, variable):
        self.is_click(user['国家选择框'])
        self.input_text(user['国家选择框'], variable)
        self.is_click(user['国家'],variable)
        sleep(3)

    @allure.step("点击保存按钮并断言新增成功")
    def click_preservation_button(self,expect):
        self.is_click(user['保存按钮'])
        sleep(3)
        # 断言
        test = self.element_text(user['列表页新增用户名字段'])
        ValueAssert.value_assert_equal(test,expect)
if __name__ == '__main__':
    pass
