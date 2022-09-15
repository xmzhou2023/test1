import allure, os,time
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class Queryuser(Base):
    """查询员工类"""


    @allure.step("输入用户")
    def input_username(self,content,usernamecode):
        self.is_click(user['列表用户名输入框'])
        self.input_text(user['列表用户名输入框'],content)
        self.is_click(user['员工'],usernamecode)

    @allure.step('点击查询')
    def click_query(self,expect):
        self.is_click(user['查询按钮'])
        # 断言
        test = self.element_text(user['员工姓名'])
        ValueAssert.value_assert_equal(test,expect)


if __name__ == '__main__':
    pass
