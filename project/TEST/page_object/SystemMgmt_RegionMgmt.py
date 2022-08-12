import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AreaPage(Base):
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

    @allure.step("前往树")
    def goto_tree(self,  *content):
        for i in range(len(content)):
            if i == 0:
                self.is_click(user['tab区域总菜单'],choice=content[0])
                sleep(2)
                self.is_click(user['tab区域菜单一级菜单'],choice=content[0])
                sleep(2)
            elif i == 1:
                self.is_click(user['tab区域菜单二级菜单'],choice=content[1])
                sleep(2)
            elif i == 2:
                self.is_click(user['tab区域菜单三级菜单'],choice=content[2])
                sleep(2)
            elif i == 3:
                self.is_click(user['tab区域菜单四级菜单'],choice=content[3])
                sleep(2)

    @allure.step("区域导出")
    def download_area(self, content):
        self.check_download(user['区域导出'], content)

    @allure.step("编辑区域")
    def edit_area(self,num, content):
        pass

    @allure.step("删除区域")
    def del_area(self):
        self.is_click(user['区域管理-删除'])
        sleep(1)

    @allure.step("确定删除区域")
    def sure_del_area(self):
        self.is_click(user['区域管理-确定删除'])
        sleep(1)

    @allure.step("新增区域")
    def create_area(self):
        self.is_click(user['区域管理-新增按钮'])

    @allure.step("新增输入名称Zh")
    def input_Zh_name(self, content):
        self.input_text(user['区域管理-新增输入Zh'], txt=content)

    @allure.step("新增输入名称En")
    def input_En_name(self, content):
        self.input_text(user['区域管理-新增输入En'], txt=content)

    @allure.step("保存区域")
    def save_area(self):
        self.is_click(user['区域管理-新增保存按钮'])
        sleep(1)

    @allure.step("新增页面搜索框")
    def add_area_search(self, content):
        self.input_text(user['区域管理-添加搜索框'], txt=content)
        sleep(1)

    @allure.step("区域管理-添加保存国家")
    def add_country_area(self):
        self.is_click(user['区域管理-添加按钮'])
        self.is_click(user['区域管理-保存国家'])
        sleep(1)

    @allure.step("区域查询")
    def input_search_name(self, content):
        self.input_text(user['区域管理-查询'], txt=content)

    @allure.step("区域查询")
    def input_search_name(self, content):
        self.input_text(user['区域管理-查询'], txt=content)

if __name__ == '__main__':
    pass
