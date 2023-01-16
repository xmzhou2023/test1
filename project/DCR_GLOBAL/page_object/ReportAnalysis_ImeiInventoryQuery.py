import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ImeiInventoryQuery(Base):
    """用户类"""

    @allure.step("关闭IMEI库存查询菜单")
    def click_close_imei_inventory_query(self):
        self.is_click(user['关闭IMEI库存查询菜单'])

    @allure.step("点击MaterialID")
    def click_box(self):
        self.is_click(user['MaterialID输入'])


    @allure.step("输入文本,进行筛选")
    def select_content(self, type, content):
        if type == 'Box ID':
            self.is_click(user['Boxid点击'])
            self.input_text(user['Boxid输入'], txt=content)
        elif type == 'Receive Date':
            self.input_text(user['收货日期开始'], txt=content)
            self.input_text(user['收货日期结束'], txt=content)
            self.click_box()
        elif type == 'Activation Date':
            self.input_text(user['激活时间开始'], txt=content)
            self.input_text(user['激活时间结束'], txt=content)
            self.click_box()
        elif type == 'Material ID':
            self.input_text(user['MaterialID输入'], txt=content)
        elif type == 'SAP Customer ID':
            self.input_text(user['SAPCustomerID输入'], txt=content)
        elif type == 'IMEI/SN':
            self.is_click(user['IMEI点击'])
            self.input_text(user['IMEI输入'], txt=content)
        elif type == 'Customer ID':
            self.is_click(user['Customer输入'])
            sleep()
            self.input_text(user['Customer输入'], txt=content)
            self.is_click(user['Customer选择'], content)
        elif type == 'Customer Type':
            self.is_click(user['CustomerType输入'])
            self.is_click(user['CustomerType_Warehouse_Wartype_激活_brand_model_MarketName_Series_Category选择'], content)
        elif type == 'Warehouse ID':
            self.is_click(user['Warehouse输入'])
            sleep()
            self.input_text(user['Warehouse输入'], txt=content)
            self.is_click(user['CustomerType_Warehouse_Wartype_激活_brand_model_MarketName_Series_Category选择'], content)
        elif type == 'Warehouse Type':
            self.is_click(user['WarehouseType输入'])
            self.is_click(user['CustomerType_Warehouse_Wartype_激活_brand_model_MarketName_Series_Category选择'], content)
        elif type == 'Sales Region 3':
            self.is_click(user['SalesRegion输入'])
            self.input_text(user['SalesRegion输入'], txt=content)
            self.is_click(user['SalesRegion选择'], content)
        elif type == 'Activated Or Not':
            self.is_click(user['ActivatedOrNot点击'])
            self.is_click(user['CustomerType_Warehouse_Wartype_激活_brand_model_MarketName_Series_Category选择'], content)
        elif type == 'Brand':
            self.is_click(user['Brand输入'])
            self.is_click(user['CustomerType_Warehouse_Wartype_激活_brand_model_MarketName_Series_Category选择'], content)
            self.click_box()
        elif type == 'Model':
            self.is_click(user['Model点击'])
            self.input_text(user['Model输入'], txt=content)
            sleep()
            self.is_click(user['CustomerType_Warehouse_Wartype_激活_brand_model_MarketName_Series_Category选择'], content)
            self.click_box()
        elif type == 'Market Name':
            self.is_click(user['MarketName点击'])
            self.input_text(user['MarketName输入'], txt=content)
            self.is_click(user['CustomerType_Warehouse_Wartype_激活_brand_model_MarketName_Series_Category选择'], content)
            self.click_box()
        elif type == 'Series':
            self.is_click(user['Series点击'])
            self.input_text(user['Series输入'], txt=content)
            self.is_click(user['CustomerType_Warehouse_Wartype_激活_brand_model_MarketName_Series_Category选择'], content)
            self.click_box()
        elif type == 'Category':
            self.is_click(user['Category点击'])
            self.is_click(user['CustomerType_Warehouse_Wartype_激活_brand_model_MarketName_Series_Category选择'], content)
            self.click_box()
        elif type == 'Dealer Category':
            self.is_click(user['DealerCategory点击'])
            self.input_text(user['DealerCategory输入'], txt=content)
            self.is_click(user['CustomerType_Warehouse_Wartype_激活_brand_model_MarketName_Series_Category选择'], content)
            self.click_box()
        else:
            logging.info('type is wrong,pls check')
        sleep()

    @allure.step("根据表头获取列的class值")
    def get_table_column(self, header):
        attribute = self.get_table_info(user['表头字段'], header, attr='class', sc_element=user['滑动条'])
        logging.info('列元素的属性是%s' % attribute)
        # number=int(attribute[4:])
        return attribute

    @allure.step("获取表格文本")
    def get_table_content(self, content):
        txt = self.element_text(user['表格具体字段'], content)
        return txt

    @allure.step("点击Unfold展开筛选项按钮")
    def click_button(self, txt):
        self.is_click(user['Unfold_Search_Reset按钮'], txt)
        if txt=='Search':
            sleep(5)
        elif txt == 'Reset':
            sleep(3)
        else:
            sleep()

if __name__ == '__main__':
    pass
