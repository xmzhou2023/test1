import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
from project.POP.page_object.Center_Component import NavPage
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class Query_shop(Base):
    """查看门店类"""

    @allure.step("前往菜单")
    def click_organization(self,variable):
        #点击组织输入框,点击Tecno
        self.is_click(user["组织下拉按钮"])
        self.is_click(user["TECNO组织"],variable)

    def click_shop(self,variable):
        #点击门店输入框，输入仙桃体专店
        self.is_click(user["门店列表输入框"])
        self.input_text(user["门店列表输入框"],variable)
        self.is_click(user["门店"],variable)


    @allure.step("点击查询")
    def click_query(self,expect):
        #点击查询按钮
        self.is_click(user["查询按钮"])
        #断言
        test = self.element_text(user["门店名称"])
        ValueAssert.value_assert_equal(test, expect)



if __name__ == '__main__':
    pass
