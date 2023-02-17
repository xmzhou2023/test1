import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


# ---卡片管理----

class baobiaoguanli(Base):
    """用户类"""

    @allure.step("查找工号")
    def search_user(self, jobnum=None, name=None):
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

    @allure.step("查找工号")
    def click_primary(self):
        self.is_click_tbm(user['主题域'])

    @allure.step("点击报表名称")
    def click_card(self):
        self.is_click_tbm(user['报表名称'])

    @allure.step("断言输入框内容")
    def assert_input(self, header, content):
        if header == '主题域' or header == '业务组织':
            ac_content = self.element_text(user['输入框内容2'], header)
            ValueAssert.value_assert_equal(ac_content, content)
        elif header == '新建说明':
            ac_content = self.element_input_text(user['输入框内容3'], header)
            ValueAssert.value_assert_equal(ac_content, content)
        elif header == '英文属性说明':
            ac_content = self.element_input_text(user['输入框内容4'], header)
            ValueAssert.value_assert_equal(ac_content, content)
        # elif header == '卡片名称':
        #     ac_content = self.element_input_text(user['输入框内容5'], header)
        #     ValueAssert.value_assert_equal(ac_content, content)
        else:
            ac_content = self.element_input_text(user['输入框内容'], header)
            ValueAssert.value_assert_equal(ac_content, content)

    @allure.step("点击菜单")
    def click_menu(self):
        self.is_click_tbm(user['菜单'])

    @allure.step("报表管理")
    def click_menu1(self):
        self.is_click(user['报表管理'])

    @allure.step("我的报表")
    def click_menu2(self):
        self.is_click(user['我的报表'])

    @allure.step("点击新建")
    def click_add(self, ):
        self.is_click_tbm(user['新建'])

    @allure.step("报表新建")
    def click_add1(self, ):
        self.is_click_tbm(user['报表新建'])

    @allure.step("点击新建")
    def input_content(self, header, content):
        textarea_list = ['说明']
        fuzzySelect_list = ['需求提出人', '业务负责人', 'IT负责人', 'Supplier']
        exactSelect_list = ['应用类型', '卡片名称']
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in textarea_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框3'], content, header)
            elif header in exactSelect_list:
                self.is_click_tbm(user['输入框内容'], header)
                self.readonly_input_text(user['输入框内容'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in fuzzySelect_list:
                self.is_click_tbm(user['输入框内容'], header)
                self.input_text(user['输入框内容'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
            else:
                logging.error('请输入正确的查询条件')
                raise ValueError('请输入正确的查询条件')

    @allure.step("主题域")
    def click_theme(self):
        self.is_click(user['主题域'])