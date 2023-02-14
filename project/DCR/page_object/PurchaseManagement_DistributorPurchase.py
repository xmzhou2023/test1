import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class DistributorPurchaseQuery(Base):
    """用户类"""

    @allure.step("关闭DistributorPurchase页面菜单")
    def click_close_distributor_purchase(self,content):
        self.is_click(user['关闭页面菜单'],content)

    @allure.step("点击MaterialID")
    def click_customer(self):
        self.is_click(user['Customer点击'])

    @allure.step("点击Unfold，Search等选项按钮")
    def click_button(self, txt):
        self.is_click(user['Export_Unfold_Search_Reset按钮'], txt)
        if txt == 'Search':
            self.element_exist(user['Loading'])
        elif txt == 'Reset':
            self.element_exist(user['Loading'])
        elif txt == 'Export':
            sleep(10)
        else:
            sleep()

    @allure.step("点击Confirm，Ccandel选项按钮")
    def click_action_button(self, txt):
        self.is_click(user['确认或取消'], txt)

    @allure.step("点击选择框，选中数据")
    def click_check_box(self):
        self.is_click(user['选择框'])

    @allure.step("根据表头获取列的class值")
    def get_table_column(self, header):
        attribute = self.get_table_info(user['表头字段'], header, attr='class')
        logging.info('列元素的属性是%s' % attribute)
        # number=int(attribute[4:])
        return attribute

    @allure.step("获取表格文本")
    def get_table_content(self, content):
        txt = self.element_text(user['表格具体字段'], content)
        return txt

    @allure.step("获取Total数值文本")
    def get_total_content(self):
        txt = self.element_text(user['Total结果'])
        logging.info('the total txt is %s' % txt)
        return txt[6:]

    @allure.step("输入文本,进行筛选")
    def select_content(self, type, content):
        # Customer，Box本页面有条件，但无结果展示，无法断言
        if type == 'Model':
            self.is_click(user['Model点击'])
            self.input_text(user['Model输入'], txt=content)
            self.is_click(user['Customer_Model_Status选择'], content)
            self.is_click(user['活动页面'])
        elif type == 'Customer ID':
            self.is_click(user['Customer点击'])
            self.input_text(user['Customer输入'], txt=content)
            self.is_click(user['Customer_Model_Status选择'], content)
        elif type == 'Status':
            self.is_click(user['Status点击'])
            self.is_click(user['Customer_Model_Status选择'], content)
        elif type == 'Order ID':
            self.is_click(user['Orderid点击'])
            self.input_text(user['Orderid输入'], txt=content)
        elif type == 'Brand':
            self.is_click(user['Brand点击'])
            self.is_click(user['Brands选择'], content)
            self.is_click(user['活动页面'])
        elif type == 'Order Date':
            self.input_text(user['创建日期开始'], txt=content)
            self.input_text(user['创建日期结束'], txt=content)
            self.is_click(user['活动页面'])
        else:
            logging.info('type is wrong,pls check')
        sleep()

    @allure.step("新增页面，输入不同值")
    def add_distributor_purchase(self,type,content):
        if type == 'Customer':
            self.is_click(user['新增页面Customer输入'])
            self.input_text(user['新增页面Customer输入'], txt=content)
            self.is_click(user['Customer_Model_Status选择'], content)
        elif type == 'date':
            self.is_click(user['新增页面发货日期'])
            self.input_text(user['新增页面发货日期'], txt=content)
            self.is_click(user['活动页面'])
        elif type == 'Brand':
            self.is_click(user['新增页面Brand点击'])
            self.is_click(user['Customer_Model_Status选择'], content)
        elif type == 'product':
            self.is_click(user['新增页面Product点击'])
            self.input_text(user['新增页面Product点击'], txt=content)
            self.is_click(user['Customer_Model_Status选择'], content)
        elif type == 'quantity':
            self.is_click(user['新增页面Quantity点击'])
            self.input_text(user['新增页面Quantity点击'], txt=content)
        else:
            logging.info('type is wrong,pls check')
        sleep()

    @allure.step("点击submit提交")
    def add_submit(self):
        self.is_click(user['点击submit'])

if __name__ == '__main__':
    pass
