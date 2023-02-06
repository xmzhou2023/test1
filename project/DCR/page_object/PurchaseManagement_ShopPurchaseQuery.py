import random
import time

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

class ShopPurchaseQuery(Base):
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
            self.is_click_tbm(user['菜单'], content[i])
            logging.info('点击菜单：{}'.format(content[i]))
        self.refresh()
        self.element_exist(user['Loading'])

    @allure.step("点击Unfold 展开筛选项")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        logging.info('点击Unfold 展开筛选项')

    @allure.step("user management页面，输入查询条件")
    def input_search(self, header, content):
        """
        @header： 输入框名称
        @content： 输入内容
        """
        textarea_list = ['IMEI']
        country_list = ['Sales Region']
        Date_list = ['Create Date', 'Inbound Date', 'Activated Date']
        fuzzySelect_list = ['Shop', 'Belong MD', 'Public ID', 'Supplier']
        exactSelect_list = ['Status', 'Gender', 'SP/FP', 'Source', 'Activation Status', 'First Category']
        inputSelect_list = ['Brand', 'Model', 'Item', 'Manpower Type', 'Market Name', 'Country', 'Activation Country', 'Delivery Country']
        inputSelect_list2 = ['Retailer', 'Creator']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in textarea_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框3'], content, header)
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
                self.is_click_tbm(user['输入框名称'], header)
            elif header in inputSelect_list2:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
            elif header in Date_list:
                createDate = content.split('To')
                for i in range(len(createDate)):
                    self.input_text(user['时间输入框'], createDate[i], header, i+1)
                    self.is_click_tbm(user['输入框名称'], header)
            else:
                logging.error('请输入正确的查询条件')
                raise ValueError('请输入正确的查询条件')

    @allure.step("点击搜索功能")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

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
                                                             index=1,  sc_element=user['滚动条'], h_element=user['表头文本'])
    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        if content != '':
            logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
            id_list = ['Shop', 'Belong MD', 'Supplier', 'Retailer']
            Date_list = ['Create Date', 'Inbound Date', 'Activated Date']
            if header in id_list:
                self.assert_Query_result(f'{header} ID', content)
            elif header == 'Sales Region':
                country = content.split('_')
                for i in range(3):
                    assert_result = False
                    column = self.get_table_info(user['menu表格字段'], f'{header} {3 - i}', sc_element=user['滚动条'],
                                                index=1, h_element=user['表头文本'])
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
            elif header in Date_list:
                if header == 'Activated Date':
                    column = self.get_table_info(user['menu表格字段'], 'Activation Date', sc_element=user['滚动条'],
                                                 index=1, h_element=user['表头文本'])
                else:
                    column = self.get_table_info(user['menu表格字段'], header, sc_element=user['滚动条'],
                                                 index=1, h_element=user['表头文本'])
                contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
                createDate = content.split('To')
                for i in contents:
                    # timeArray = time.strptime(i, "%Y-%m-%d %H:%M:%S")
                    # a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.mktime(timeArray) + 28800))
                    logging.info(f'实际时间：{i}')
                    # logging.info(f'修正时区后时间：{a}')
                    try:
                        assert createDate[0] <= i <= createDate[1] + ' 23:59:59'
                        logging.info(f'断言成功：创建时间：{i} 在筛选时间 {content} 区间')
                    except:
                        logging.info(f'断言失败：创建时间：{i} 与筛选时间 {content} 不符')
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
        if 'First Category' in list_random:
            if 'Brand' not in list_random:
                list_random.remove('First Category')
        if 'Item' in list_random:
            if 'Brand' not in list_random:
                list_random.remove('Item')
        logging.info(f'随机组合：输入框：{list_random}')
        for i in list_random:
            logging.info(f'随机组合：{i} 输入框输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_random:
            self.assert_search_result(i, kwargs[i])

    @allure.step("重置ShopPurchaseQuery导入数据")
    def reset_ShopPurchaseQuery_import(self, imei):
        """ShopPurchaseQuery页面点击指定imei复选框，删除"""
        logging.info('开始重置ShopPurchaseQuery导入数据')
        self.click_menu("Purchase Management", "Shop Purchase Query")
        self.click_unfold()
        self.input_search('IMEI', imei)
        self.input_search('Status', 'Committed')
        self.click_search()
        total_text = self.element_text(user['Total'])
        total = total_text[total_text.index(' ')+1:]
        logging.info(total_text)
        if total != '0':
            self.click_checkbox(imei)
            self.click_cancel()
            DomAssert(self.driver).assert_att('Cancel success')
            sleep(3)

    @allure.step("点击复选框")
    def click_checkbox(self, content):
        """
        :param content: 指定值，如imei
        """
        rowid = self.get_table_info(user['指定行'], content, attr='rowid', sc_element=user['滚动条'])
        self.is_click_tbm(user['指定复选框'], rowid, content)
        logging.info(f'点击 {content} 复选框')

    @allure.step("点击取消")
    def click_cancel(self):
        self.is_click_tbm(user['Cancel'])
        self.is_click_tbm(user['Confirm'])
        logging.info('点击取消')

    @allure.step("点击Import按钮")
    def click_import(self):
        self.is_click(user['Import'])
        logging.info('点击Import按钮')
        self.click_upload()

    @allure.step("点击Export按钮")
    def click_export(self):
        self.is_click(user['Export'])
        logging.info('点击Export按钮')

    @allure.step("点击Upload按钮")
    def click_upload(self):
        self.is_click(user['Upload'])
        logging.info('点击upload按钮')
        sleep(2)

    @allure.step("导入文件")
    def import_file(self, name):
        """
        :param name： 传入存放在data文件夹里的文件名
        """
        file_path = os.path.join(BASE_DIR, 'project', 'DCR', 'data', name)
        logging.info("文件地址：{}".format(file_path))
        self.upload_file(user['导入'], file_path)
        logging.info("导入文件：{}".format(file_path))

    @allure.step("断言：导入成功状态")
    def assert_import_success(self):
        logging.info("开始断言：导入成功状态")
        DomAssert(self.driver).assert_control(user['导入成功状态'])

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

    def get_Record_info(self, menu, name, header):
        """
        :param menu: 输入菜单名
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        """
        for i in range(20):
            ac_menu = self.element_text(user['当前菜单'])
            if ac_menu != menu:
                self.click_menu('Basic Data Management', menu)
            column = self.get_table_info(user['Record表格字段'], header, h_element=user['表头文本'])
            content = self.element_text(user['表格指定列内容'], name, column)
            logging.info(f'获得 {menu} 页面 {name} 文件 {header} 字段内容 {content}')
            return content

    @allure.step("断言：Record导入结果")
    def assert_Record_result(self, menu, name, header, result=None):
        """
        :param menu: 菜单
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        :param result: 需要断言的值 比如状态，数量，时间
        """
        logging.info(f'开始断言：{menu} Record导入结果')
        ac_result = self.get_Record_info(menu, name, header)
        if header == 'File Size':
            ValueAssert.value_assert_IsNot(ac_result, '0B')
        else:
            ValueAssert.value_assert_In(result, ac_result)


if __name__ == '__main__':
    pass
