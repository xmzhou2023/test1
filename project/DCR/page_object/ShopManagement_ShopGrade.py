import random
import time

import allure, os
from public.base.basics import Base, sleep, random_list
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopGrade(Base):
    """用户类"""

    @allure.step("点击Search 查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("点击Add")
    def click_add(self):
        self.is_click(user['Add'])

    @allure.step("输入新增门店信息")
    def input_add_info(self, header, content):
        if header == 'Brand' or header == 'Country':
            self.is_click(user['Add输入框'], header)
            self.input_text(user['Add输入框'], content, header)
            self.is_click_tbm(user['输入结果精确选择'], content)
            self.is_click_tbm(user['输入框名称'], header)
        elif header == 'Statistical Dimension':
            self.is_click(user['StatisticalDimension'], content)
        elif header == 'Agree Auto Calculate':
            self.is_click(user['AgreeAutoCalculate'], content)

    @allure.step("新增门店等级")
    def input_ShopGrade(self, name, range1, type='add'):
        if type == 'add':
            self.is_click_tbm(user['AddAdd'])
        Namecolumn = self.get_table_info(user['ShopGradeList'], 'Grade Name')
        self.is_click_tbm(user['GradeName输入框'], Namecolumn)
        self.input_text(user['GradeName输入框'], name, Namecolumn)
        self.is_click_tbm(user['输入结果精确选择'], name)
        Rangecolumn = self.get_table_info(user['ShopGradeList'], 'Monthly Sales Range')
        for i in range(len(range1.split('-'))):
            self.input_text(user['MonthlySalesRange输入框'], range1.split('-')[i], Rangecolumn, i+1)

    @allure.step("点击save按钮")
    def click_save(self):
        self.is_click(user['AddSave'])

    @allure.step("查找菜单")
    def click_menu(self, *content):
        self.refresh()
        self.is_click_tbm(user['菜单栏'])
        self.refresh()
        for i in range(len(content)):
            self.is_click_tbm(user[f'菜单{i + 1}'], content[i])
            logging.info('点击菜单：{}'.format(content[i]))
        self.refresh()
        self.element_exist(user['Loading'])

    def input_text(self, locator, txt, *choice):
        """输入文本"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        ele.clear()
        ele.send_keys(txt)
        logging.info("输入文本：{}".format(txt))

    @allure.step("输入查询条件")
    def input_search(self, header, content):
        exactSelect_list = ['Brand', 'Country']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in exactSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            else:
                logging.error('请输入正确的查询条件')
                raise ValueError('请输入正确的查询条件')

    @allure.step("断言：页面查询结果")
    def assert_Query_result(self, header, content):
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['menu表格字段'], user['表格内容'], header, content,
                                                             sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("组合查询 组合方法")
    def random_Query_Method(self, kwargs):
        list_query = []
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        for i in list_query:
            logging.info(f'随机组合：{i} 输入框输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_query:
            self.assert_Query_result(i, kwargs[i])

    @allure.step("点击指定复选框")
    def click_checkbox(self, brand):
        self.is_click_tbm(user['指定复选框'], brand)

    @allure.step("点击删除")
    def click_delete(self):
        self.is_click_tbm(user['Delete'])
        self.is_click_tbm(user['Confirm'])

    @allure.step("编辑")
    def click_edit(self, brand):
        self.is_click(user['Edit'], brand)


if __name__ == '__main__':
    pass
