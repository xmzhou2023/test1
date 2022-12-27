import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *
from project.POP.page_object.Center_Component import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AddUser(Base):
    """新增职员类"""

    @allure.step("点击新增按钮")
    def click_add_button(self):
        self.is_click_tbm(user['新增按钮'])

    @allure.step("输入用户名")
    def input_username(self,content):
        self.input_text(user['用户名输入框'],content)

    @allure.step("选择归属组织")
    def switch_division(self,variable):
        self.is_click_tbm(user['归属组织选择框'])
        self.input_text(user['归属组织选择框'],variable)
        sleep(2)
        self.is_click_tbm(user['职员组织'],variable)

    @allure.step("选择区域")
    def switch_region(self,variable):
        self.is_click_tbm(user['区域选择框'])
        self.input_text(user['区域选择框'],variable)
        sleep(2)
        self.is_click_tbm(user['职员区域'],variable)

    @allure.step("选择角色")
    def switch_role(self,variable):
        self.is_click_tbm(user['角色选择框'])
        self.input_text(user['角色选择框'],variable)
        sleep(2)
        self.is_click_tbm(user['职员角色'],variable)

    @allure.step("选择国家")
    def switch_country(self, variable):
        self.is_click_tbm(user['国家选择框'])
        self.input_text(user['国家选择框'], variable)
        sleep(2)
        self.is_click_tbm(user['国家'],variable)
        sleep(3)

    @allure.step("选择上级")
    def switch_superior(self,superior):
        self.is_click_tbm(user['上级输入框'])
        self.input_text(user['上级输入框'],superior)
        sleep(5)
        self.is_click_tbm(user['上级'],superior)

    @allure.step("选择门店")
    def switch_shop(self, shop):
        self.is_click_tbm(user['门店输入框'])
        self.input_text(user['门店输入框'],shop)
        sleep(5)
        self.is_click_tbm(user['门店'],shop)


    @allure.step("点击保存按钮功")
    def click_preservation_button(self):
        self.is_click_tbm(user['保存按钮'])
        sleep(5)

class QueryUser(Page_Operation,General_button):
    """按条件查询员工"""
    select_list1 = {"用户框":"员工","角色框":"角色","状态框":"状态","门店框":"门店1"}
    select_list2 = {"员工类型框":"员工类型","国家框":"国家1","区域框":"区域"}
    def queryuser(self,select,content):
        if select in self.select_list1:
            self.single_condition_input_boxquery(select,self.select_list1[select],content)
            sleep()
            self.query()
        elif select in self.select_list2:
            self.more()
            sleep()
            self.single_condition_input_boxquery(select,self.select_list2[select],content)
            sleep()
            self.more_query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")

class ExportEmployee(Base):
    """导出职员管理类"""

    @allure.step("点击导出")
    def click_export(self):
        self.is_click_tbm(user['导出'])

if __name__ == '__main__':
    pass
