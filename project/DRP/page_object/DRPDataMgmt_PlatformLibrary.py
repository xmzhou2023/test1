import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class PlatformLibrary(Base):
    """平台库"""

    @allure.step("选择指定选项")
    def screenOption(self, condition,option):
        self.is_click(user['查询条件'],condition)
        self.is_click(user['下拉选项'], option)
        logging.info("系列：{}".format(option))

    @allure.step("点击查询按钮")
    def queryButton(self):
        self.is_click(user['查询按钮'])
        logging.info("点击查询按钮")

    @allure.step("清空查询条件")
    def query_clear(self,condition,num):
        self.is_click(user['查询条件'],condition)
        self.is_click(user['清空查询条件'],num)
        logging.info("清空查询条件：{}".format(condition))


    @allure.step("查询结果断言")
    def screenAssert(self,condition, value):
        if condition == "平台":
            assertvalue = self.element_text(user['平台列表'],"3")
            ValueAssert.value_assert_equal(assertvalue,value)
        if condition == "物料状态":
            assertvalue = self.element_text(user['平台列表'], "4")
            ValueAssert.value_assert_equal(assertvalue,value)
        if condition == "可用状态":
            assertvalue = self.element_text(user['平台列表'], "1")
            ValueAssert.value_assert_equal(assertvalue,value)

    @allure.step("查询结果断言")
    def exceptionAssert(self):
        value = self.element_text(user['暂无数据(断言)'])
        ValueAssert.value_assert_equal(value,"暂无数据")

    @allure.step("前置条件 - 按照条件过滤平台库")
    def precondition(self,drivers):
        platform = PlatformLibrary(drivers)
        platform.screenOption("平台","HK-整机")
        platform.screenOption("物料状态","整机")
        platform.screenOption("可用状态","启用")
        platform.queryButton()

    @allure.step("点击重置按钮")
    def resetButton(self):
        self.is_click(user['重置按钮'])
        logging.info("点击重置按钮")

    @allure.step("列表数据断言")
    def listAssert(self):
        return self.element_text(user['数据条数（断言）'])






if __name__ == '__main__':
    pass



