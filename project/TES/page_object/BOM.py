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

    @allure.step("点击菜单")
    def click_muen(self):
        self.is_click(user['一级菜单'])
        self.is_click(user['二级菜单'])
        sleep(1)

    def click(self, locatorText):
        self.is_click_tbm(user[locatorText])

    def BOM_select_info_input(self, locatorStr1, locatorStr2, searchText = None):
        # self.readonly_input_text(user[locatorText], text)
        # 要先点一下再输入值, 上面的方法不行
        self.is_click(user[locatorStr1])
        if searchText:
            self.input_text(user[locatorStr1], searchText)
        self.is_click(user[locatorStr2])

    def jump_to(self, target):
        self.switch_location(target)

    def normal_input(self, locatorText, text):
        self.readonly_input_text(user[locatorText], text)


    # enter_iframe
    # switch_window 传入索引
    # close_switch 传入索引
    # element_text 获取元素的文字
    # DomAssert(dirvers).assert_att('页面文字')

if __name__ == '__main__':
    pass
