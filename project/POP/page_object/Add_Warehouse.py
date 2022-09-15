import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AddWarehouse(Base):
    """新增仓库类"""

    @allure.step("点击仓库新增按钮")
    def click_add(self):
        self.is_click(user['仓库新增按钮'])

    @allure.step("输入仓库名称")
    def input_warehouse_name(self,content):
        self.input_text(user['仓库名称输入框'],content)

    @allure.step("选择门店")
    def switch_shop(self,content,code):
        self.is_click(user['门店选择框'])     # 点击定位到门店选择框
        self.input_text(user['门店选择框'],content)   # 输入门店名下拉框会下拉展示门店
        variable = content + " " + code    # 下拉展示”门店名称 门店编码“ 例如：”我的测试门店 PBD00020“
        self.is_click(user['选择的门店'],variable)  # 根据输入门店下拉展示数据点击对应门店

    @allure.step("选择仓库类型")
    def switch_warehouse_type(self):
        self.is_click(user['仓库类型选择框'])
        self.is_click(user['仓库类型'])

    @allure.step("点击提交")
    def click_submit(self):
        self.is_click(user['仓库信息新增提交按钮'])
        sleep(3)

    @allure.step("断言")
    def assert_warehouse_name(self,expect):
        test = self.element_text(user['新增仓库名称'])
        ValueAssert.value_assert_equal(test,expect)


if __name__ == '__main__':
    pass
