import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging

from sync import BASE_DIR
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class Bloc_add(Base):

    @allure.step("进入薪酬配置界面")
    def click_menu(self):
        self.is_click(user['菜单'])
        self.is_click(user['薪酬管理'])
        self.is_click(user['薪酬配置'])
        sleep(1)
        self.refresh()

    ##新增集团方案

    @allure.step("点击集团方案")
    def click_Bloc(self):
        self.is_click(user['集团方案'])

    @allure.step("集团方案新增")
    def add_Bloc(self):
        sleep(1)
        self.is_click(user['新增'])

    @allure.step("输入新增集团方案编码")
    def Bloc_Code(self, txt):
        self.input_text(user['集团方案编码'], txt)

    @allure.step("输入集团方案名称")
    def Bloc_Name(self, txt):
        self.input_text(user['集团方案名称'], txt)
        sleep(1)

    @allure.step("输入新增集团方案生效日期")
    def Bloc_Date(self, num):
        self.readonly_input_text(user['生效日期'], num)
        self.is_click(user['集团方案名称'])

    @allure.step("选择新增集团方案状态")
    def Bloc_Status(self, info):
        self.is_click(user['状态选择'])
        # self.scroll_into_view(user['状态'], info)
        self.is_click(user['状态'], info)

    @allure.step("点击确定")
    def Bloc_Confirm(self):
        sleep(1)
        self.is_click(user['确定'])

    #  DomAssert(self.driver).assert_att('请输入4位方案编码，由数字、字母组成')

    @allure.step("删除所新增的集团方案")
    def Bloc_delete(self, info):
        self.refresh()
        self.is_click_tbm(user['删除'], info)
        self.is_click(user['确'])
    #  DomAssert(self.driver).assert_exact_att('删除成功')
    # self.refresh()

if __name__ == '__main__':
    pass
