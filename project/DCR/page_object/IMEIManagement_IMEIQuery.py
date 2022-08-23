import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class IMEIQueryPage(Base):

    @allure.step("选择Box ID单选按钮")
    def click_choose_box_id(self):
        self.is_click(user['选择Box ID单选按钮'])

    @allure.step("点击选择IMEI单选框")
    def click_choose_imei(self):
        self.is_click(user['选择IMEI单选按钮'])


    @allure.step("输入Box ID或IMEI编码")
    def input_code(self, text):
        self.input_text(user['textarea输入框'], text)
        self.is_click(user['Check'])
        sleep(3)

    @allure.step("找到数据来源")
    def get_code(self, type1):
        Base.presence_sleep_dcr(self, user[type1])
        return self.element_text(user[type1])

    @allure.step("关闭IMEI Inventory Query菜单")
    def click_close_imei_inven_query(self):
        self.is_click(user['关闭IMEI Inventory Query菜单'])
        sleep(1.5)

    @allure.step("关闭IMEI Query菜单")
    def click_close_imei_query(self):
        self.is_click(user['关闭IMEI Query菜单'])
        sleep(1.5)

if __name__ == '__main__':
    pass
