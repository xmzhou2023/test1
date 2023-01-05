import logging
import time
from datetime import datetime
from openpyxl import load_workbook
from libs.common.read_element import Element
from libs.config.conf import BASE_DIR
from public.base.basics import Base, random_list
from libs.common.time_ui import sleep
import random
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class PositionManagementPage(Base):
    #新增角色方法
    # @allure.step("Position Management页面，点击Add新增职位按钮")
    # def click_add_position(self):
    #     self.presence_sleep_dcr(user['Add Position Button'])
    #     self.is_click(user['Add Position Button'])
    #     sleep(1)

    @allure.step("Position Management页面，点击Add、Delete、Search、Reset操作按钮")
    def click_operation_button(self, operation_button):
        self.is_click(user['Click Position Operation Button'], operation_button)
        sleep(1)

    @allure.step("随机生成数字")
    def get_number(self):
        num = str(random.randint(10, 1000))
        return num

    @allure.step("Add新增职位页面，输入Position职位名称")
    def add_input_position_name(self, position_name):
        self.presence_sleep_dcr(user['Add Input Position'])
        self.is_click(user['Add Input Position'])
        self.input_text(user['Add Input Position'], position_name)

    @allure.step("Add新增职位页面，选择Enabled or Not启用")
    def add_select_enabled_yes(self):
        self.is_click(user['Add Select Enabled Yes'])

    @allure.step("Add新增职位页面，选择Enabled or Not禁用")
    def add_select_enabled_no(self):
        self.is_click(user['Add Select Enabled No'])

    @allure.step("Add新增职位页面，选择Position Type职位类型：Promoter Group, 出现Flexi or Not选择是")
    def add_position_type_promoter_yes(self, position_type):
        self.is_click(user['Add click Position Type'])
        sleep(0.5)
        self.is_click(user['选择结果精确选择'], position_type)
        if 'Promoter Group' == position_type:
            self.is_click(user['Add Click Flexi or Not Yes'])
        else:
            pass

    @allure.step("Add新增职位页面，选择Position Type职位类型：Promoter Group, 出现Flexi or Not选择否")
    def add_position_type_promoter_no(self, position_type):
        self.is_click(user['Add click Position Type'])
        sleep(0.5)
        self.is_click(user['选择结果精确选择'], position_type)
        if 'Promoter Group' == position_type:
            self.is_click(user['Add Click Flexi or Not No'])
        else:
            pass

    @allure.step("Add新增职位页面，选择Position Type职位类型：Promoter Group, 出现Flexi or Not选择是")
    def add_position_type_supervisor(self, position_type):
        self.is_click(user['Add click Position Type'])
        sleep(0.5)
        self.is_click(user['选择结果精确选择'], position_type)

    @allure.step("Add新增职位页面，输入并选择Default Roles默认角色")
    def add_input_default_roles1(self, roles1, label):
        self.is_click(user['Add Input Default Roles'])
        self.is_click(user['选择结果精确选择'], roles1)
        self.is_click(user['新增点击label标签'], label)

    @allure.step("Add新增职位页面，输入并选择Default Roles默认角色")
    def add_input_default_roles2(self, roles1, roles2, label):
        self.is_click(user['Add Input Default Roles'])
        self.is_click(user['选择结果精确选择'], roles1)
        self.is_click_dcr(user['选择结果精确选择'], roles2)
        self.is_click(user['新增点击label标签'], label)

    @allure.step("Add新增职位页面，输入remark备注")
    def add_input_position_remark(self, remark):
        self.input_text(user['Add Input Remark'], remark)

    @allure.step("Add新增职位页面，点击Save保存按钮")
    def add_position_save_button(self):
        self.is_click_dcr(user['Add Save Button'])

    #筛选角色方法
    @allure.step("Position Management页面，输入Position职位筛选")
    def input_position_query(self, position_name, label):
        self.is_click(user['点击输入框Position'])
        self.input_text(user['输入框输入Position'], position_name)
        self.is_click(user['输入结果精确选择'], position_name)
        #点击label标签名称释法
        self.is_click(user['筛选点击label标签'], label)

    @allure.step("Position Management页面，点击Search查询按钮")
    def click_position_search(self):
        self.is_click(user['Search Position Button'])
        sleep(1)

    @allure.step("断言精确查询结果 Position Management列表，字段列、字段内容是否与预期的字段内容值一致，有滚动条")
    def assert_user_management_field(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格指定列内容'], header, content,
                                                    sc_element=user['水平滚动条'])

    @allure.step("断言模糊查询结果 Position Management列表，字段列、字段内容是否与预期的字段内容值一致，有滚动条")
    def assert_contains_user_management_field(self, header, content):
        DomAssert(self.driver).assert_search_contains_result(user['表格字段'], user['表格指定列内容'], header, content,
                                                             sc_element=user['水平滚动条'])

    #编辑职位
    @allure.step("Position Management页面，点击Edit编辑功能")
    def click_edit_position_button(self):
        self.is_click(user['Edit Position Button'])
        sleep(0.5)


    #删除职位
    @allure.step("Position Management页面，获取列表职位列内容")
    def get_list_position(self, position):
        get_list_position = self.element_text(user['Get List Position'], position)
        return get_list_position

    @allure.step("Position Management页面，点击Search查询按钮")
    def click_delete_position(self, operation_name):
        self.is_click(user['勾选第一个复选框'])
        self.is_click(user['Click Position Operation Button'], operation_name)
        self.presence_sleep_dcr(user['Confirm Delete Button'])
        self.is_click(user['Confirm Delete Button'])

    @allure.step("Position Management页面，获取列表total分页总条数")
    def get_list_total(self):
        get_total = self.element_text(user['Get List Total'])
        get_total1 = get_total[6:]
        return get_total1



if __name__ == '__main__':
    pass