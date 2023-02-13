import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class DistributorReceiptQuery(Base):
    """DistributorReceipt查询类"""

    @allure.step("关闭DistributorReceipt查询菜单")
    def click_close_distributor_receipt_query(self):
        self.is_click(user['关闭DistributorReceipt查询菜单'])

    @allure.step("点击MaterialID")
    def click_dn(self):
        self.is_click(user['DN输入'])

    @allure.step("点击IMEI Detail")
    def click_detail(self):
        self.is_click(user['点击IMEIDetail'])

    @allure.step("关闭IMEI Detail")
    def clos_detail(self):
        self.is_click(user['关闭IMEIDetail'])

    @allure.step("根据表头获取列的class值")
    def get_table_column(self, header):
        attribute = self.get_table_info(user['表头字段'], header, attr='class')
        logging.info('列元素的属性是%s' % attribute)
        # number=int(attribute[4:])
        return attribute

    @allure.step("根据表头获取列的class值")
    def get_detail_column(self, header):
        self.is_click(user['点击IMEIDetail'])
        sleep()
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
        logging.info('the total txt is %s'%txt)
        return txt[6:]

    @allure.step("获取详情页Total数值文本")
    def get_total_detail(self):
        txt = self.element_text(user['详情页total'])
        logging.info('the total txt is %s'%txt)
        return int(txt[6:])

    @allure.step("获取IMEI文本")
    def get_table_detail(self, content1, content2):
        txt = self.element_text(user['详情页IMEI'], content1, content2)
        return txt

    @allure.step("点击Unfold展开筛选项按钮")
    def click_button(self, txt):
        self.is_click(user['Unfold_Search_Reset按钮'], txt)
        if txt == 'Search':
            sleep(5)
        elif txt == 'Reset':
            sleep(3)
        else:
            sleep()

    @allure.step("输入文本,进行筛选")
    def select_content(self, type, content):
        # Customer，Box本页面有条件，但无结果展示，无法断言
        if type == 'Model':
            self.is_click(user['Model点击'])
            self.input_text(user['Model输入'], txt=content)
            sleep(2)
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
            self.click_dn()
        elif type == 'Customer':
            self.is_click(user['Customer点击'])
            self.input_text(user['Customer输入'], txt=content)
            sleep(2)
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
        elif type == 'Material ID':
            self.input_text(user['MaterialID输入'], txt=content)
        elif type == 'DN':
            self.input_text(user['DN输入'], txt=content)
        elif type == 'SAP Delivery Date':
            self.input_text(user['SAPDeliveryDate开始'], txt=content)
            self.input_text(user['SAPDeliveryDate结束'], txt=content)
            self.click_dn()
        elif type == 'SAP Customer ID':
            self.input_text(user['SAPCustomerID输入'], txt=content)
        elif type == 'Brand':
            self.is_click(user['Brand点击'])
            sleep()
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
            self.click_dn()
        elif type == 'Category':
            self.is_click(user['Category点击'])
            sleep()
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
            self.click_dn()
        elif type == 'IMEI':
            self.is_click(user['IMEI点击'])
            self.input_text(user['IMEI输入'], txt=content)
        elif type == 'Market Name':
            self.is_click(user['MarketName点击'])
            self.input_text(user['MarketName输入'], txt=content)
            sleep(2)
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
            self.click_dn()
        elif type == 'Customer Region3':
            self.is_click(user['CustomerRegion点击'])
            self.input_text(user['CustomerRegion点击'], txt=content)
            sleep(2)
            self.is_click(user['CustomerRegion输入'], content)
        elif type == 'Delivery Country':
            self.is_click(user['Country点击'])
            self.input_text(user['Country输入'], txt=content)
            sleep(2)
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
            self.click_dn()
        elif type == 'Status':
            self.is_click(user['Status点击'])
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], 'Receiving')
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], 'On Transit')
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
            self.click_dn()
        else:
            logging.info('type is wrong,pls check')
        sleep()


if __name__ == '__main__':
    pass
