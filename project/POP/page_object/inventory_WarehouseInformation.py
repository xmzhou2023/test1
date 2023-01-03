import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
from project.POP.page_object.Center_Component import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class WarehouseInformation(Base):
    """仓库信息类"""

    @allure.step("点击菜单按钮")
    def warehouse_menu(self, button):
        self.is_click(user['菜单按钮'], button)

    @allure.step("填写仓库名称")
    def warehouse_warehouse_name(self, value):
        self.is_click(user['仓库名称'])
        self.input_text(user['仓库名称'], value)

    @allure.step("选择门店")
    def warehouse_shop_name(self, value):
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

    @allure.step("点击搜索/重置按钮")
    def click_search_or_reset(self, button):
        self.is_click(user['查询/重置'], button)

    @allure.step("点击勾选框")
    def click_checkbox(self):
        self.is_click(user['勾选框'])


class SelectWarehouseInformation(Page_Operation,General_button):
    """按条件查询仓库信息"""
    select_list1 = {"仓库框": "仓库名", "仓库状态框": "仓库状态选项", "仓库门店框": "仓库门店名"}

    def query_warehouse_information(self, select, content):
        if select in self.select_list1:
            self.single_condition_input_boxquery(select,self.select_list1[select],content)
            sleep()
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")

if __name__ == '__main__':
    pass
