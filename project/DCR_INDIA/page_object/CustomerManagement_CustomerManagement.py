import random

import allure, os
from public.base.basics import Base, sleep, random_list
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class CustomerManagementPage(Base):
    """用户类"""

    @allure.step("客户列表页面，点击Search 查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("查找菜单")
    def click_menu(self, *content):
        self.refresh()
        self.is_click_tbm(user['菜单栏'])
        self.refresh()
        for i in range(len(content)):
            self.is_click_tbm(user[f'菜单{i+1}'], content[i])
            logging.info('点击菜单：{}'.format(content[i]))
        self.refresh()
        self.element_exist(user['Loading'])

    @allure.step("点击Unfold 展开筛选项")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(1)
        logging.info('点击Unfold 展开筛选项')

    @allure.step("user management页面，输入查询条件")
    def input_search(self, header, content):
        """
        @header： 输入框名称
        @content： 输入内容
        """
        input_list = ['SAP Customer ID']
        country_list = ['Sales Region', 'Country/City']
        fuzzySelect_list = ['User', 'Customer', 'Warehouse', 'Channel Sales Manager']
        exactSelect_list = ['Customer Type', 'Customer Grade', 'Whether use DCR system', 'Status', 'Contact Name']
        inputSelect_list = ['Customer Category', 'Brand']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in input_list:
                self.input_text(user['输入框'], content, header)
            elif header in exactSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in fuzzySelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框2'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
            elif header in country_list:
                country = content.split('_')
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], country[2], header)
                self.is_click_tbm(user['地区选择框'], country[0], country[1], country[2])
            elif header in inputSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框4'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            else:
                logging.error('请输入正确的查询条件')
                raise ValueError('请输入正确的查询条件')

    @allure.step("判断空值")
    def assert_None(self, result):
        try:
            assert result == '', logging.warning("断言失败: 该值不为None | x:{}".format(result))
            logging.info("断言成功: 该值为None | x:{}".format(result))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("断言：页面查询结果")
    def assert_Query_result(self, header, content):
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['menu表格字段'], user['表格内容'], header, content,
                                                             sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
        if header == 'Customer' or header == 'User' or header == 'Warehouse':
            self.assert_Query_result(f'{header} ID', content)
        elif header == 'Sales Region':
            country = content.split('_')
            for i in range(3):
                assert_result = False
                column = self.get_table_info(user['menu表格字段'], f'{header} {3 - i}', sc_element=user['滚动条'],
                                             h_element=user['表头文本'])
                contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
                for j in contents:
                    if j != '':
                        ValueAssert.value_assert_equal(j, country[2])
                        assert_result = True
                    else:
                        logging.info(f'{header} {3 - i} 区域为空，继续比对上级区域')
                        break
                if assert_result:
                    logging.info('断言结束')
                    break
        elif header == 'Country/City':
            country = content.split('_')
            self.assert_Query_result(f'City', country[2])
        elif header == 'Staff Type':
            column = self.get_table_info(user['menu表格字段'], 'Belong To Customer ID', sc_element=user['滚动条'],
                                         h_element=user['表头文本'])
            contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
            if content == 'Dealer Staff':
                for i in contents:
                    ValueAssert.value_assert_IsNoneNot(i)
            elif content == 'Transsion Staff':
                for i in contents:
                    self.assert_None(i)
        elif header == 'Contact Name':
            column = self.get_table_info(user['menu表格字段'], header, sc_element=user['滚动条'],
                                         h_element=user['表头文本'])
            contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
            for i in contents:
                try:
                    assert content.lower() in i.lower()
                    logging.info("断言成功，结果:{}包含指定内容:{}".format(i, content))
                except:
                    logging.error("断言失败，结果:{}不包含指定内容:{}".format(i, content))
                    raise
        else:
            self.assert_Query_result(header, content)

    @allure.step("组合查询 组合方法")
    def random_Query_Method(self, kwargs):
        list_query = []
        num = random.randint(3, 8)
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        list_random = random_list(list_query, num)
        if 'Customer Grade' in list_random and 'Customer Type' not in list_random:
            list_random.remove('Customer Grade')
        logging.info(f'随机组合：输入框：{list_random}')
        for i in list_random:
            logging.info(f'随机组合：{i} 输入框输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_random:
            self.assert_search_result(i, kwargs[i])


if __name__ == '__main__':
    pass
