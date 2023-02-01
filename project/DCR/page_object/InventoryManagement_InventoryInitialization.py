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

    #筛选列表信息
    @allure.step("Inventory Initialization列表页面，点击Unfold或者Fold展开筛选项")
    def click_unfold_fold(self, unfold_fold):
        self.is_click(user['Unfold_Fold'], unfold_fold)
        sleep(1)

    @allure.step("Inventory Initialization列表页面，根据imei条件进行筛选数据")
    def input_initial_imei_query(self, header, content):
        self.is_click(user['点击IMEI输入框'], header)
        self.input_text(user['输入IMEI输入框'], content, header)

    @allure.step("Inventory Initialization列表页面，根据initial id条件进行筛选数据")
    def input_initial_id_query(self, header, content):
        self.input_text(user['输入框'], content, header)

    @allure.step("Inventory Initialization页面，根据Customer条件进行筛选数据")
    def input_initial_customer_query(self, header, content, values):
        self.is_click(user['输入框'], header)
        self.input_text(user['输入框'], content, header)
        self.presence_sleep_dcr(user['选中模糊结果值'], values)
        self.is_click(user['选中模糊结果值'], values)

    @allure.step("Inventory Initialization页面，根据Customer Type条件进行筛选数据")
    def input_initial_customer_type_query(self, header, content):
        self.is_click(user['输入框'], header)
        self.input_text(user['输入框'], content, header)
        self.presence_sleep_dcr(user['选中精确结果值'], content)
        self.is_click(user['选中精确结果值'], content)

    @allure.step("Inventory Initialization页面，根据Warehouse条件进行筛选数据")
    def input_initial_warehouse_query(self, header, content):
        self.is_click(user['输入框'], header)
        self.input_text(user['输入框'], content, header)
        self.presence_sleep_dcr(user['选中模糊结果值'], content)
        self.is_click(user['选中模糊结果值'], content)

    @allure.step("Inventory Initialization页面，根据model条件进行筛选数据")
    def input_initial_model_query(self, header, content):
        self.is_click(user['Model输入框'])
        self.input_text_dcr(user['输入框2'], content, header)
        self.presence_sleep_dcr(user['选中精确结果值'], content)
        self.is_click(user['选中精确结果值'], content)
        self.is_click(user['点击筛选label'], header)

    @allure.step("Inventory Initialization页面，根据brand条件进行筛选数据")
    def input_initial_brand_query(self, header, content):
        self.is_click(user['Brand输入框'])
        self.input_text(user['输入框2'], content, header)
        self.presence_sleep_dcr(user['选中精确结果值'], content)
        self.is_click(user['选中精确结果值'], content)
        self.is_click(user['点击筛选label'], header)

    @allure.step("Inventory Initialization页面，根据market_name条件进行筛选数据")
    def input_initial_market_name_query(self, header, content):
        self.is_click(user['Market Name输入框'])
        self.input_text(user['输入框2'], content, header)
        self.presence_sleep_dcr(user['选中精确结果值'], content)
        self.is_click(user['选中精确结果值'], content)
        self.is_click(user['点击筛选label'], header)

    @allure.step("Inventory Initialization页面，根据Country条件进行筛选数据")
    def input_initial_country_query(self, header, content):
        self.is_click(user['Country输入框'])
        self.input_text(user['输入框2'], content, header)
        self.presence_sleep_dcr(user['选中精确结果值'], content)
        self.is_click(user['选中精确结果值'], content)
        self.is_click(user['点击筛选label'], header)

    @allure.step("Inventory Initialization页面，点击Search 查询按钮")
    def click_search_reset(self, content):
        self.is_click(user['Search_Reset'], content)
        self.element_text(user['Loading'])

    @allure.step("Inventory Initialization页面，获取Initial ID字段的内容")
    def get_initial_id_text(self):
        initial_id = self.find_element(user['获取列表Initial ID表头'])
        get_initial_id_class = initial_id.get_attribute('class')
        get_initial_id = self.element_text(user['获取列表Initial ID内容'], get_initial_id_class)
        return get_initial_id


    @allure.step("IMEI Detail详情页面，获取Total分页总数")
    def get_imei_detail_total(self):
        get_total = self.element_text(user['Get IMEI Detail Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("列表页面，获取列表Total分页总数")
    def get_list_total(self):
        get_total = self.element_text(user['Get List Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("新建IMEI的初始化库存操作步骤, 暂时不用勿删")
    def create_initialization_imei_operation(self, imei_sn, imei_sn1):
        self.click_add_initialization()
        self.click_add_imei_sn_radio()
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
        DomAssert(self.driver).assert_search_contains_result(user['表格字段'], user['表格内容'], header, content, sc_element=user['滚动条'], h_element=user['表头文本'])

    #导入操作
    @allure.step("Inventory Initialization页面，点击Import 导入功能")
    def click_initial_import(self, import_upload):
        self.is_click(user['Import_upload'], import_upload)
        sleep(1)

    @allure.step("导入客户模板-上传文件")
    def upload_true_file(self, file1):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', file1)
        logging.info("打印上传的Inventory Initialization模板文件path：{}".format(path1))
        self.click_import_upload_save(path1)

    @allure.step("点击导入后，上传文件")
    def click_import_upload_save(self, file1):
        self.is_click(user['Import_upload'], 'Upload')
        sleep(3)
        ele = self.driver.find_element('xpath', "//button//..//input[@name='file']")
        ele.send_keys(file1)
        sleep(1.5)
        self.is_click(user['Import Save'])
        sleep(2)
        self.presence_sleep_dcr(user['Upload Confirm'])
        self.is_click(user['Upload Confirm'])
        sleep(1)


    @allure.step("通过数据库删除导入的初始化数据")
    def delete_import_initial_data(self, initial_id, imei):
        logging.info("开始删除库存初始化，导入的数据")
        sql1 = SQL('DCR', 'test')
        sql1.delete_db(f"delete from t_warehouse_initial_imei where initial_id='{initial_id}' and imei='{imei}'")
        sql1.delete_db(f"delete from t_warehouse_initial_ticket where initial_id='{initial_id}'")
        sql1.delete_db(f"delete from t_channel_warehouse_current_stock where imei='{imei}'")


    #导出操作
    @allure.step("初始化库存列表，点击导出功能")
    def click_initial_list_export(self):
        self.is_click(user['Export'])
        sleep(1)

    @allure.step("初始化库存列表，进入IMEI Detail详情页，点击导出功能")
    def click_imei_detail_export(self):
        self.is_click(user['IMEI Detail Export'])
        sleep(1)

    @allure.step("获取下载进度值")
    def get_download_value(self):
        attribute = self.get_table_info(user['下载进度条'], attr='aria-valuenow')
        logging.info('下载进度值是%s' % attribute)
        return int(attribute)

if __name__ == '__main__':
    pass
