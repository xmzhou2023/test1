import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class WarehouseInformation(Base):
    """仓库信息类"""

    @allure.step("点击新增")
    def warehouse_add(self, button):
        self.is_click(user['菜单按钮'], button)

    @allure.step("填写仓库名称")
    def warehouse_warehousename(self, value):
        self.is_click(user['仓库名称'])
        self.input_text(user['仓库名称'], value)

    @allure.step("选择门店")
    def warehouse_shopname(self, value):
        self.is_click(user['门店'])
        sleep(3)
        self.input_text(user['门店'], value)
        sleep(3)
        self.is_click(user['选择门店'], value)

    @allure.step("选择仓库")
    def warehouse_select(self):
        self.is_click(user['仓库'])
        sleep()
        self.is_click(user['选择仓库类型'])

    @allure.step("点击提交")
    def click_submit(self, button):
        self.is_click(user['提交/取消'], button)


if __name__ == '__main__':
    pass
