from libs.common.read_element import Element
import logging
from public.base.basics import Base
from libs.common.time_ui import sleep
from public.base.assert_ui import ValueAssert
from ..test_case.conftest import *
from public.base.basics import Base, random_list
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ReturnOrderPage(Base):
    """ReturnOrderPage 类"""
    @allure.step("退货单列表页面，点击Search")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("点击退货单unfold")
    def click_unfold(self):
        self.is_click(user['展开折叠'])

    @allure.step("断言：页面查询结果")
    def assert_User_Exist(self, header, content):
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['menu表格字段'], user['表格内容'], header, content, sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("判断空值")
    def assert_None(self, result):
        try:
            assert result == '', logging.warning("断言失败: 该值不为None | x:{}".format(result))
            logging.info("断言成功: 该值为None | x:{}".format(result))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("user management页面，输入查询条件")
    def input_search(self, header, content):
        """
        @header： 输入框名称
        @content： 输入内容
        """
        click_input_list = ['Return Order ID', 'Delivery/DN Order ID']
        input_select_list = ['Brand']
        input_select_all_list1 = ['Status', 'Return Type']
        input_select_all_list22 = ['Model', 'Market Name', 'Seller Country']
        return_date_list = ['Return Date']
        seller_list = ['Seller', 'Buyer']
        warehouse_list = ['Buyer Warehouse Region', 'Seller Warehouse Region']
        imei_list = ['IMEI']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if header in click_input_list:
            self.is_click_dcr(user['输入框'], header)
            self.input_text(user['输入框'], content, header)
        elif header in input_select_list:
            self.is_click_dcr(user['输入框'], header)
            self.is_click(user['输入结果精确选择'], content, header)
            self.is_click(user['点击label标签'], header)
        elif header in input_select_all_list1:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框2'], content, header)
            self.is_click(user['输入结果精确选择'], content)
        elif header in input_select_all_list22:
            self.is_click_dcr(user['输入框'], header)
            self.input_text(user['输入框1'], content, header)
            sleep(1)
            self.is_click(user['输入结果精确选择'], content)
            self.is_click(user['点击label标签'], header)
        elif header in return_date_list:
            self.is_click(user['Input Return Start Date'], header)
            self.input_text(user['Input Return Start Date'], content, header)
            """弹出日历空间后，点击日历标签释法"""
            self.is_click(user['点击label标签'], header)
        elif header in seller_list:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框2'], content, header)
            sleep(1.2)
            self.is_click(user['输入结果模糊选择'], content)
        elif header in warehouse_list:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框'], content, header)
            sleep(0.6)
            self.is_click(user['输入仓库区域精确选择'], header, content)
        elif header in imei_list:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框IMEI'], content, header)
        else:
            logging.error('请输入正确的查询条件')
            raise ValueError('请输入正确的查询条件')


    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
        if header == 'Return Order ID' or header == 'Delivery/DN Order ID':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Return Date':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Status':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Return Type':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Brand':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Model':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Market Name':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Seller':
            self.assert_User_Exist(f'{header} ID', content)
        elif header == 'Seller Country':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Buyer':
            self.assert_User_Exist(f'{header} ID', content)
        elif header == 'Seller Warehouse Region':
            self.assert_User_Exist(f'{header}2', content)
        elif header == 'Buyer Warehouse Region':
            self.assert_User_Exist(f'{header}2', content)
        elif header == 'IMEI':
            self.is_click(user['点击IMEI Detail按钮'])
            sleep(0.5)
            self.assert_User_Exist(f'{header}', content)
            self.is_click(user['关闭IMEI Detail窗口'])
        else:
            self.assert_User_Exist(header, content)


    @allure.step("组合查询 组合方法")
    def random_Query_Method(self, kwargs):
        list_query = []
        num = random.randint(3, 8)
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        list_random = random_list(list_query, num)
        logging.info(f'随机组合：输入框：{list_random}')
        for i in list_random:
            logging.info(f'随机组合：输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_random:
            self.assert_search_result(i, kwargs[i])

    @allure.step("按退货日期条件筛选数据")
    def return_order_return_date_query(self, header, content):
        self.is_click(user['Input Return Start Date'], header)
        self.input_text(user['Input Return Start Date'], content, header)
        """弹出日历空间后，点击日历标签释法"""
        self.is_click(user['点击label标签'], header)

if __name__ == '__main__':
    pass