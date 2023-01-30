import time
import random
import allure
from public.base.basics import Base, sleep, random_list
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from libs.config.conf import BASE_DIR
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class InventoryInitializationPage(Base):
    """库存初始化类"""
    @allure.step("点击新增按钮")
    def click_add_initialization(self):
        self.is_click(user['Add'])
        sleep(1.5)

    @allure.step("选中IMEI/SN单选按钮")
    def click_add_imei_sn_radio(self):
        self.is_click(user['IMEI SN Radio'])

    @allure.step("选中Box ID单选按钮")
    def click_add_box_id_radio(self):
        self.is_click(user['Box ID Radio'])

    @allure.step("Create Initialization Order页面，输入IMEI/SN内容")
    def input_scan_imei_sn(self, content):
        self.is_click(user['输入IMEI SN'])
        self.input_text(user['输入IMEI SN'], content)

    @allure.step("Create Initialization Order页面，输入Box ID内容")
    def input_scan_box_id(self, content):
        self.is_click(user['输入Box ID'])
        self.input_text(user['输入Box ID'], content)

    @allure.step("Create Initialization Order页面，点击Check按钮")
    def click_check(self):
        self.is_click(user['点击Check'])
        sleep(1)

    @allure.step("Create Initialization Order页面，获取检查后的Scanned扫码成功数量")
    def get_add_scanned_num(self):
        get_scanned_num = self.element_text(user['Scanned Num'])
        return get_scanned_num

    @allure.step("Create Initialization Order页面，获取检查后的Scan Record Success")
    def get_scan_record_success(self):
        get_scan_record_success = self.element_text(user['Scan Record Success'])
        return get_scan_record_success

    @allure.step("Create Initialization Order页面，点击提交按钮")
    def click_add_submit(self):
        self.is_click(user['Add Submit'])
        sleep(1)

    @allure.step("Create Initialization Order页面，获取Order Detail列表下的No Data")
    def get_order_detail_no_data(self):
        get_no_data = self.element_text(user['Order Detail No Data'])
        return get_no_data

    @allure.step("列表页面，点击Unfold或者Fold展开筛选项")
    def click_unfold_fold(self, unfold_fold):
        self.is_click(user['Unfold_Fold'], unfold_fold)
        sleep(1)

    @allure.step("列表页面，根据imei条件进行筛选数据")
    def input_inventory_imei_query(self, header, content):
        self.is_click(user['点击IMEI输入框'], header)
        self.input_text(user['输入IMEI输入框'], content, header)

    @allure.step("列表页面，点击Search 查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_text(user['Loading'])

    @allure.step("IMEI Detail详情页面，获取Total分页总数")
    def get_imei_detail_total(self):
        get_total = self.element_text(user['Get IMEI Detail Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("列表页面，获取Total分页总数")
    def get_list_total(self):
        get_total = self.element_text(user['Get List Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("新建IMEI的初始化库存操作步骤, 暂时不用勿删")
    def create_initialization_imei_operation(self, imei_sn, imei_sn1):
        self.click_add_initialization()
        self.click_add_imei_sn()
        """输入仓库已存在的IMEI，检查失败"""
        self.input_scan_imei_sn(imei_sn)
        self.click_check()
        get_scanned_num = self.get_add_scanned_num()
        ValueAssert.value_assert_equal('0', get_scanned_num)
        DomAssert(self.driver).assert_att('Already in warehouse')
        """输入仓库不存在的IMEI，检查成功"""
        self.input_scan_imei_sn(imei_sn1)
        self.click_check()
        get_scanned_num = self.get_add_scanned_num()
        ValueAssert.value_assert_equal('1', get_scanned_num)
        DomAssert(self.driver).assert_att('Success')
        DomAssert(self.driver).assert_att(imei_sn1)
        self.click_add_submit()

    @allure.step("列表点击IMEI Detail按钮，打开详情页")
    def click_imei_detail_button(self):
        self.is_click(user['点击IMEI Detail'])
        sleep(1)

    @allure.step("IMEI Detail页面，关闭IMEI详情页")
    def click_close_imei_detail(self):
        self.is_click(user['关闭IMEI Detail'])

    @allure.step("断言：列表筛选结果")
    def assert_Query_result(self, header, content):
        """
        :param header: 需要获取的指定字段
        :param content: 需要断言的值
        """
        logging.info('开始断言：Inventory Initialization列表筛选结果')
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格内容'], header, content, sc_element=user['滚动条'], h_element=user['表头文本'])




if __name__ == '__main__':
    pass
