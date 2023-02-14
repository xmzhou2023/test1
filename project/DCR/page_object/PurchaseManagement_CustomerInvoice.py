import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
from libs.common.connect_sql import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class CustomerInvoiceQuery(Base):
    """用户类"""

    @allure.step("关闭CustomerInvoice页面菜单")
    def click_close_customer_invoice(self,content):
        self.is_click(user['关闭页面菜单'],content)

    @allure.step("点击MaterialID")
    def click_material_id(self):
        self.is_click(user['MaterialID点击输入'])

    @allure.step("点击IMEI Detail")
    def click_detail(self):
        self.is_click(user['IMEI Detail点击'])

    @allure.step("关闭IMEI Detail")
    def clos_detail(self):
        self.is_click(user['关闭DN弹窗页面'])

    @allure.step("根据表头获取列的class值")
    def get_table_column(self, header):
        attribute = self.get_table_info(user['表头字段'], header, attr='class')
        logging.info('列元素的属性是%s' % attribute)
        # number=int(attribute[4:])
        return attribute

    @allure.step("根据表头获取详情页面列的class值")
    def get_detail_column(self, header):
        self.is_click(user['点击IMEIDetail'])
        sleep()
        attribute = self.get_table_info(user['表头字段'], header, attr='class')
        logging.info('列元素的属性是%s' % attribute)
        # number=int(attribute[4:])
        return attribute
        """注意在调试时，看下是否需要关闭IMEIDetail详情页面"""

    @allure.step("获取表格文本")
    def get_table_content(self, content):
        txt = self.element_text(user['表格具体字段'], content)
        return txt

    @allure.step("获取Total数值文本")
    def get_total_content(self):
        txt = self.element_text(user['Total结果'])
        logging.info('the total txt is %s' % txt)
        return txt[6:]

    @allure.step("获取详情页Total数值文本")
    def get_total_detail(self):
        txt = self.element_text(user['跳转页面total'])
        logging.info('the total txt is %s' % txt)
        return int(txt[6:])

    @allure.step("获取IMEI文本")
    def get_table_detail(self, content1, content2):
        txt = self.element_text(user['DN页面IMEI'], content1, content2)
        return txt

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

    @allure.step("点击详情页导出按钮")
    def click_detail_export(self):
        self.is_click(user['跳转页面Export'])
        sleep(10)

    @allure.step("点击选择框，选中数据")
    def click_check_box(self):
        self.is_click(user['选择框'])

    @allure.step("输入DN，提交")
    def input_dn(self,content):
        self.input_text(user['同步DN输入'], txt=content)
        self.is_click(user['同步DN页submit'])
        sleep(2)

    @allure.step("获取下载进度值")
    def get_download_value(self):
        attribute = self.get_table_info(user['下载进度条'], attr='aria-valuenow')
        logging.info('下载进度值是%s' % attribute)
        # number=int(attribute[4:])
        return int(attribute)

    @allure.step("获取下载进度值")
    def get_download_detail(self):
        attribute = self.get_table_info(user['跳转页下载进度条'], attr='aria-valuenow')
        logging.info('下载进度值是%s' % attribute)
        # number=int(attribute[4:])
        return int(attribute)


    @allure.step("输入文本,进行筛选")
    def select_content(self, type, content):
        #Customer，Box本页面有条件，但无结果展示，无法断言
        if type == 'Model':
            self.is_click(user['Model点击'])
            self.input_text(user['Model输入'], txt=content)
            self.is_click(user['Model选择'], content)
            self.is_click(user['MaterialID点击输入'])
        elif type == 'Customer':
            self.is_click(user['Customer点击'])
            self.input_text(user['Customer输入'], txt=content)
            self.is_click(user['Customer选择'], content)
        elif type == 'Material ID':
            self.input_text(user['MaterialID点击输入'], txt=content)
        elif type == 'DN':
            self.input_text(user['DN点击输入'], txt=content)
        elif type == 'SAP Delivery Date':
            self.input_text(user['SAPDeliveryDate开始'], txt=content)
            self.input_text(user['SAPDeliveryDate结束'], txt=content)
            self.is_click(user['MaterialID点击输入'])
        elif type == 'SAP Customer ID':
            self.input_text(user['SAPCustomerID点击输入'], txt=content)
        elif type == 'Brand':
            self.is_click(user['Brand点击'])
            self.is_click(user['Brand_Category_Country_Role_Staff选择'], content)
            self.is_click(user['MaterialID点击输入'])
        elif type == 'Category':
            self.is_click(user['Category点击'])
            self.is_click(user['Brand_Category_Country_Role_Staff选择'], content)
            self.is_click(user['MaterialID点击输入'])
        elif type == 'IMEI':
            self.is_click(user['IMEI点击'])
            self.input_text(user['IMEI输入'], txt=content)
        elif type == 'Box':
            self.is_click(user['Box点击'])
            self.input_text(user['Box输入'], txt=content)
        elif type == 'Market Name':
            self.is_click(user['MarketName点击'])
            self.input_text(user['MarketName输入'], txt=content)
            self.is_click(user['MarketName选择'], content)
            self.is_click(user['MaterialID点击输入'])
        elif type == 'Customer Region3':
            self.is_click(user['CustomerRegion输入'])
            self.input_text(user['CustomerRegion输入'],txt=content)
            logging.info('click Customer Region3  right')
            self.is_click(user['CustomerRegion_Status选择'], content)
            self.is_click(user['MaterialID点击输入'])
        elif type == 'Status':
            self.is_click(user['Status点击'])
            if content != 'Finished':
                self.is_click(user['CustomerRegion_Status选择'], content)
            self.is_click(user['MaterialID点击输入'])
        else:
            logging.info('type is wrong,pls check')
        sleep()

class CustomerInvoiceSql(Base):
    """用户类"""

    @allure.step("在数据库中，删除DN")
    def delete_dn(self,content):
        dnsql=SQL('DCR', 'test')
        sql1="delete from t_enter_sap_dn where vbeln='%s'"%content
        sql2 =f"delete from t_enter_sap_detail where vbeln='{content}'"
        sql3="delete from t_enter_sap_primary_order where vbeln='{}'".format(content)
        dnsql.delete_db(sql1)
        dnsql.delete_db(sql2)
        dnsql.delete_db(sql3)
        sleep()



if __name__ == '__main__':
    pass
