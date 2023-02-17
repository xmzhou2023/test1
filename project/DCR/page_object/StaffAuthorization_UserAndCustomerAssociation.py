import random

import allure, os

from libs.config.conf import BASE_DIR
from public.base.basics import Base, sleep, random_list
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class UserAndCustomerAssociation(Base):
    """用户类"""

    def input_text(self, locator, txt, *choice):
        """输入文本"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        ele.clear()
        ele.send_keys(txt)
        logging.info("输入文本：{}".format(txt))

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

    @allure.step("输入查询条件")
    def input_search(self, header, content):
        input_list = ['User', 'Customer']
        country_list = ['Sales Region']
        exactSelect_list = ['Brand']
        inputSelect_list = ['Customer Type', 'Customer Categroy', 'Country']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in input_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框2'], content, header)
            elif header in exactSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
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

    @allure.step("断言：页面查询结果")
    def assert_Query_result(self, header, content):
        """
        :param header: 需要获取的指定字段
        :param content: 需要断言的值
        """
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_result(user['menu表格字段'], user['表格内容'], header, content,
                                                    sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("点击Search 查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("点击Unfold 展开筛选项")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        logging.info('点击Unfold 展开筛选项')

    @allure.step("判断空值")
    def assert_None(self, result):
        try:
            assert result == '', logging.warning("断言失败: 该值不为None | x:{}".format(result))
            logging.info("断言成功: 该值为None | x:{}".format(result))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
        if header == 'Sales Region':
            country = content.split('_')
            for i in range(3):
                assert_result = False
                column = self.get_table_info(user['menu表格字段'], f'{header} {3 - i}', sc_element=user['滚动条'],
                                             h_element=user['表头文本'])
                contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
                for j in contents:
                    if ''.join(j.split()) != '':
                        ValueAssert.value_assert_equal(j, country[2])
                        assert_result = True
                    else:
                        logging.info(f'{header} {3 - i} 区域为空，继续比对上级区域')
                        break
                if assert_result:
                    logging.info('断言结束')
                    break
        elif header == 'Have Superior or Not':
            column = self.get_table_info(user['menu表格字段'], f"{header.split(' ')[1]} ID", sc_element=user['滚动条'],
                                         h_element=user['表头文本'])
            contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
            if content == 'Yes':
                for i in contents:
                    ValueAssert.value_assert_IsNoneNot(i)
            elif content == 'No':
                for i in contents:
                    self.assert_None(''.join(i.split()))
        elif header == 'Have Shop or Not':
            column = self.get_table_info(user['menu表格字段'], f"{header.split(' ')[1]} Code", sc_element=user['滚动条'],
                                         h_element=user['表头文本'])
            contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
            if content == 'Yes':
                for i in contents:
                    ValueAssert.value_assert_IsNoneNot(i)
            elif content == 'No':
                for i in contents:
                    self.assert_None(''.join(i.split()))
        elif header == 'Employee Name':
            self.assert_Query_result('User Name', content)
        elif header == 'User' or header == 'Customer':
            self.assert_Query_result(f'{header} ID', content)
        else:
            self.assert_Query_result(header, content)

    @allure.step("组合查询 组合方法")
    def random_Query_Method(self, kwargs):
        list_query = []
        num = random.randint(3, 8)
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        # list_random = random_list(list_query, num)
        # logging.info(f'随机组合：输入框：{list_random}')
        for i in list_query:
            logging.info(f'随机组合：{i} 输入框输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_query:
            self.assert_search_result(i, kwargs[i])

    @allure.step("点击Upload按钮")
    def click_upload(self):
        self.is_click(user['Upload'])
        logging.info('点击upload按钮')

    @allure.step("点击Import按钮")
    def click_import(self):
        self.is_click(user['Import'])
        logging.info('点击Import按钮')
        self.click_upload()

    @allure.step("导入门店")
    def import_file(self, name):
        file_path = os.path.join(BASE_DIR, 'project', 'DCR', 'data', name)
        logging.info("文件地址：{}".format(file_path))
        self.upload_file(user['导入'], file_path)
        self.assert_import_success()

    @allure.step("点击Save按钮")
    def click_save(self):
        self.is_click(user['Save'])
        logging.info('点击Save按钮')

    @allure.step("点击Confirm按钮")
    def click_confirm(self):
        self.is_click(user['Confirm'])
        logging.info('点击Confirm按钮')
        sleep(2)
        self.refresh()

    @allure.step("断言：导入成功状态")
    def assert_import_success(self):
        DomAssert(self.driver).assert_control(user['导入成功状态'])

    @allure.step("获得Record指定内容")
    def get_Record_info(self, menu, name, header):
        """
        :param menu: 菜单名
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        """
        for i in range(20):
            ac_menu = self.element_text(user['当前菜单'])
            if ac_menu != menu:
                self.click_menu('Basic Data Management', menu)
            column = self.get_table_info(user['表格字段'], header, h_element=user['表头文本'])
            content = self.element_text(user['表格指定列内容'], name, column)
            logging.info(f'获得 {menu} 页面 {name} 文件 {header} 字段内容 {content}')
            return content

    @allure.step("断言：导入导出Record结果")
    def assert_Record_result(self, menu, name, header, result=None):
        """
        :param menu: 菜单
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        :param result: 需要断言的值 比如状态，数量，时间
        """
        ac_result = self.get_Record_info(menu, name, header)
        if header == 'File Size':
            ValueAssert.value_assert_IsNot(ac_result, '0B')
        else:
            ValueAssert.value_assert_In(result, ac_result)

    @allure.step("重置用户与客户关系")
    def reset_Association(self, uid):
        """
        :param uid: 输入user id
        """
        if self.element_exist(user['NoData']) is False:
            self.click_CheckBox(uid)
            self.click_function_button('Delete')
            self.click_Delete()
            self.assert_NoData()

    @allure.step("点击功能按钮")
    def click_function_button(self, function):
        """
        @function： 需要点击的功能按钮，具体如下：
        Export, Import, Delete
        """
        logging.info(f'点击功能按钮： {function}')
        self.is_click(user['功能按钮'], function)
        if function == 'Import':
            self.click_upload()


    @allure.step("点击指定复选框")
    def click_CheckBox(self, uid, header='User ID'):
        """
        @UID： UID 默认传入userid，username或其他唯一内容也可以传
        """
        column = self.get_table_info(user['表格字段'], header, h_element=user['表头文本'])
        self.is_click_tbm(user['指定复选框'], column, uid)
        logging.info(f'点击 {uid} 复选框')

    @allure.step("点击确定删除按钮")
    def click_Delete(self):
        self.is_click(user['确定删除'])
        logging.info('点击确定删除按钮')

    @allure.step("断言：用户授权页面存在NoData")
    def assert_NoData(self):
        logging.info('开始断言：用户授权页面存在NoData')
        DomAssert(self.driver).assert_control(user['NoData'])


if __name__ == '__main__':
    pass
