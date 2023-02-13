import logging

from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class DitributorReceiptPage(Base):
    """DitributorReceiptPage类"""
    @allure.step("点击Unfold 展开更多筛选条件")
    def click_unfold(self):
        """点击Unfold 展开更多筛选条件"""
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("国包收货列表页，输入DN条件筛选")
    def input_dn_query(self, content):
        self.input_text(user['DN输入框'], content)

    @allure.step("勾选列表DN前面第一个复选框")
    def click_first_checkbox(self):
        self.is_click(user['DN前面第一个复选框'])

    @allure.step("点击Quick Receive快速收货功能按钮")
    def click_quick_receive_button(self):
        self.is_click(user['Quick Receive button'])
        sleep(1.5)

    @allure.step("国包收货页面，一键收货操作后，点击提交按钮")
    def click_quick_receive_submit(self):
        self.is_click(user['国包收货Submit'])

    @allure.step("打开快速收货对话框，获取Quick Receive下的DN字段内容")
    def get_quick_receive_dn(self):
        get_dn = self.element_text(user['Get Quick Receive DN'])
        return get_dn

    @allure.step("国包收货页面，一键收货的DN数据")
    def get_quick_receive_quantity(self):
        get_quantity = self.element_text(user['Get Quick Receive Quantity'])
        return get_quantity

    @allure.step("获取列表 总数量total Quantity文本")
    def get_list_quantity_text(self):
        self.scroll_into_view(user['列表第一行Quantity文本'])
        list_quantity = self.element_text(user['列表第一行Quantity文本'])
        return list_quantity

    @allure.step("获取收货对话框总数量Quantity文本")
    def get_dialog_text_quantity(self):
        dialog_quantity = self.element_text(user['收货对话框Quantity文本'])
        return dialog_quantity

    @allure.step("获取列表第一个DN文本")
    def get_list_dn_text(self):
        list_dn = self.element_text(user['列表第一个DN文本'])
        return list_dn

    @allure.step("获取收货对话框DN文本")
    def get_dialog_text_dn(self):
        dialog_dn = self.element_text(user['收货对话框DN文本'])
        return dialog_dn

    @allure.step("国包收货页面，筛选条件后，点击Search按钮")
    def click_search_reset(self, search_reset):
        self.is_click(user['Search_Reset'], search_reset)
        self.element_text(user['Loading'])

    @allure.step("国包收货页面，删除一键收货的DN数据")
    def delete_dist_receipt_dn_data(self, dn_code):
        logging.info("国包收货后，开始删除一键收货的DN相关数据")
        sql1 = SQL('DCR', 'test')
        result = sql1.query_db(f"select inbound_code from t_channel_inbound_ticket where order_code = '{dn_code}'")
        inbound_code = result[0].get("inbound_code")
        logging.info("打印查询t_channel_inbound_ticket表inbound_code字段的值:{}".format(inbound_code))
        sql1.delete_db(f"delete from t_channel_inbound_detail where inbound_code= '{inbound_code}'")
        sql1.delete_db(f"delete from t_channel_inbound_imei where inbound_code= '{inbound_code}'")
        sql1.delete_db(f"delete from t_channel_inbound_ticket where order_code= '{dn_code}'")
        sql1.delete_db(f"delete from t_channel_warehouse_current_stock where imei in (select imei1 from t_enter_sap_detail where vbeln='{dn_code}')")
        sql1.change_db(f"update t_enter_sap_dn set state=1 where vbeln='{dn_code}'")


    @allure.step("国包收货页面，删除扫码收货的IMEI数据")
    def delete_dist_receipt_imei_data(self, imei):
        logging.info("国包收货页面，扫码IMEI入库后，开始删除扫码IMEI的相关数据")
        sql2 = SQL('DCR', 'test')
        result = sql2.query_db(f"select inbound_code from t_channel_inbound_imei where imei1='{imei}'")
        inbound_code = result[0].get("inbound_code")
        logging.info("打印查询t_channel_inbound_imei表inbound_code字段的值:{}".format(inbound_code))
        sql2.delete_db(f"delete from t_channel_inbound_detail where inbound_code= '{inbound_code}'")
        sql2.delete_db(f"delete from t_channel_inbound_imei where inbound_code= '{inbound_code}'")
        sql2.delete_db(f"delete from t_channel_inbound_ticket where inbound_code= '{inbound_code}'")
        sql2.delete_db(f"delete from t_channel_warehouse_current_stock where IMEI ='{imei}'")
        sql2.change_db(f"update t_enter_sap_detail set r_qty=0 where imei1='{imei}'")

    @allure.step("国包收货页面，删除扫码收货的Box ID数据")
    def delete_dist_receipt_box_id_data(self, box_id):
        logging.info("国包收货页面，扫码IMEI入库后，开始删除扫码IMEI的相关数据")
        sql3 = SQL('DCR', 'test')
        result_vbeln = sql3.query_db(f"select vbeln from t_enter_sap_detail where boxid='{box_id}'")
        vbeln = result_vbeln[0].get("vbeln")
        logging.info("打印查询t_enter_sap_detail表vbeln字段的值:{}".format(vbeln))
        result_inbound_code = sql3.query_db(f"select inbound_code from t_channel_inbound_ticket where order_code='{vbeln}'")
        inbound_code = result_inbound_code[0].get("inbound_code")
        logging.info("打印查询t_channel_inbound_ticket表inbound_code字段的值:{}".format(inbound_code))
        sql3.delete_db(f"delete from t_channel_inbound_detail where  inbound_code= '{inbound_code}'")
        sql3.delete_db(f"delete from t_channel_inbound_imei where  inbound_code= '{inbound_code}'")
        sql3.delete_db(f"delete from  t_channel_inbound_ticket where inbound_code= '{inbound_code}'")
        sql3.delete_db(f"delete from t_channel_warehouse_current_stock  where IMEI in (select imei1 from t_enter_sap_detail where boxid='{box_id}')")
        sql3.change_db(f"update t_enter_sap_detail set r_qty=0 where  boxid='{box_id}'")


    @allure.step("国包收货页面，删除同步的DN数据")
    def delete_dist_sync_dn_date(self, dn_data):
        logging.info("开始删除国包收货 DN同步后的数据")
        sql2 = SQL('DCR', 'test')
        sql2.delete_db(f"delete from t_enter_sap_detail where vbeln='{dn_data}'")
        sql2.delete_db(f"delete from t_enter_sap_dn where vbeln='{dn_data}'")


    #扫码IMEI与SN收货
    @allure.step("国包收货页面，点击More Option下的Stock in by Scan扫码收货功能")
    def click_more_option_stock_in_by_scan(self):
        self.mouse_hover_click(user['More Option'])
        Base.presence_sleep_dcr(self, user['More Option Stock in by Scan'])
        self.is_click(user['More Option Stock in by Scan'])
        sleep(1.5)

    @allure.step("N10005登录，进入国包收货页面，没有more Option更多，直接点击Stock in by Scan扫码按钮")
    def click_stock_in_by_scan_button(self):
        self.is_click(user['点击Stock in by Scan'])
        sleep(1.5)


    @allure.step("国包收货页面，打开创建Inbound Order，输入IMEI进行扫码收货操作")
    def create_inbound_order_imei(self, customer, imei1):
        """输入Customer并选择客户"""
        self.is_click(user['Create Inbound Customer点击'])
        self.input_text(user['Create Inbound Customer点击'], customer)
        self.presence_sleep_dcr(user['Create Inbound Customer下拉选择值'], customer)
        self.is_click(user['Create Inbound Customer下拉选择值'], customer)
        self.is_click(user['点击label标签'], 'Customer')
        """扫码输入IMEI或SN"""
        self.input_text(user['Scan Input IMEI or BoxID'], imei1)
        self.is_click(user['点击Check'])
        """断言是否检查通过"""
        get_scanned = self.element_text(user['Get Scanned number'])
        get_order_detail_scanned = self.element_text(user['Get Order Detail Scanned number'])
        get_scan_record_imei = self.element_text(user['Get Scan Record IMEI'], imei1)
        get_success = self.element_text(user['Get Scan Record Success'])
        ValueAssert.value_assert_equal('1', get_scanned)
        ValueAssert.value_assert_equal(get_scanned, get_order_detail_scanned)
        ValueAssert.value_assert_equal(imei1, get_scan_record_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        self.is_click(user['Create Inbound Click Submit'])


    @allure.step("国包收货页面，打开创建Inbound Order，输入IMEI进行扫码收货操作")
    def create_inbound_order_imei2(self, imei2):
        """使用国包账号登录，默认加载该账号的Customer ID与仓库"""
        """扫码输入IMEI或SN"""
        self.input_text(user['Scan Input IMEI or BoxID'], imei2)
        self.is_click(user['点击Check'])
        """断言是否检查通过"""
        get_scanned = self.element_text(user['Get Scanned number'])
        get_order_detail_scanned = self.element_text(user['Get Order Detail Scanned number'])
        get_scan_record_imei = self.element_text(user['Get Scan Record IMEI'], imei2)
        get_success = self.element_text(user['Get Scan Record Success'])
        ValueAssert.value_assert_equal('1', get_scanned)
        ValueAssert.value_assert_equal(get_scanned, get_order_detail_scanned)
        ValueAssert.value_assert_equal(imei2, get_scan_record_imei)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        self.is_click(user['Create Inbound Click Submit'])

    @allure.step("国包收货页面，打开创建Inbound Order，输入IMEI进行扫码收货操作")
    def create_inbound_order_box_id(self, box_id):
        """使用国包账号登录，默认加载该账号的Customer ID与仓库"""
        """扫码输入IMEI或SN"""
        self.input_text(user['Scan Input IMEI or BoxID'], box_id)
        self.is_click(user['点击Check'])
        sleep(5)
        """断言是否检查通过"""
        get_scanned = self.element_text(user['Get Scanned number'])
        get_order_detail_scanned = self.element_text(user['Get Order Detail Scanned number'])
        get_success = self.element_text(user['Get Scan Record Success'])
        ValueAssert.value_assert_equal('40', get_scanned)
        ValueAssert.value_assert_equal(get_scanned, get_order_detail_scanned)
        ValueAssert.value_assert_In('Success', get_success)
        """点击提交按钮"""
        self.is_click(user['Create Inbound Click Submit'])


    #同步DN
    @allure.step("国包收货页面，点击More Option下的 sync DN同步功能")
    def click_more_option_sync_dn(self):
        self.mouse_hover_click(user['More Option'])
        Base.presence_sleep_dcr(self, user['More Option Sync DN'])
        self.is_click(user['More Option Sync DN'])
        sleep(1.5)
        """断言对话框是否存在Sync DN标题"""
        get_sync_dn_text = self.element_text(user['Get Sync DN Text'])
        ValueAssert.value_assert_equal('Sync DN', get_sync_dn_text)

    @allure.step("国包收货页面，打开同步DN页面，输入DN")
    def input_sync_dn(self, content):
        self.input_text(user['Sync DN Input DN'], content)

    @allure.step("获取输入框disabled属性是否等于disabled")
    def get_input_attribute_disabled_state(self, content):
        get_disabled = self.find_element(user[content])
        get_disabled1 = get_disabled.get_attribute('disabled')
        return get_disabled1

    @allure.step("国包收货页面，打开同步DN页面，输入DN后，判断下面的输入框是否为禁用状态，然后点击提交")
    def click_sync_dn_submit(self):
        """输入DN后，获取Customer ID、Date、Country输入框是否为disabled禁用状态"""
        get_customer_id = self.get_input_attribute_disabled_state('Get Customer ID label disabled')
        get_date = self.get_input_attribute_disabled_state('Get Date label disabled')
        get_country = self.get_input_attribute_disabled_state('Get Country label disabled')
        if 'true' in str(get_customer_id) and 'true' in str(get_date) and 'true' in str(get_country):
            logging.info("打印customer id、date、country输入框为禁用状态，不可输入")
            """点击同步DN的提交"""
            self.is_click(user['Sync DN Click Submit'])

    @allure.step("国包收货页面，筛选DN收货成功后，获取文本No Data")
    def get_success_text(self):
        get_success = self.element_text(user['Get Successfully Text'])
        return get_success

    @allure.step("国包收货页面，点击IMEI Detail按钮查看IMEI详情信息")
    def click_imei_detail(self):
        self.presence_sleep_dcr(user['点击IMEI Detail'])
        self.is_click(user['点击IMEI Detail'])
        sleep(1)
        self.element_text(user['Loading'])

    @allure.step("打开IMEI Detail页面，获取DN文本内容")
    def get_imei_detail_dn_text(self):
        imei_detail_dn = self.element_text(user['Get IMEI Detail DN'])
        return imei_detail_dn

    @allure.step("IMEI Detail页面，获取IMEI总条数Total")
    def text_imei_detail_total(self):
        imei_detail_total = self.element_text(user['Get IMEI Detail Total'])
        imei_detail_total1 = imei_detail_total[6:]
        return imei_detail_total1

    @allure.step("IMEI Detail页面，点击Export导出按钮")
    def click_distri_imei_detail_export(self):
        self.is_click(user['IMEI Detail Export'])
        sleep(1)

    @allure.step("IMEI Detail页面，点击右上角关闭图标，关闭页面")
    def click_imei_detail_close(self):
        self.is_click(user['Close IMEI Detail'])

    @allure.step("获取IMEI Detail详情页 下载进度值")
    def get_imei_detail_download_value(self):
        attribute = self.get_table_info(user['导出详情下载进度条'], attr='aria-valuenow')
        logging.info('下载进度值是%s' % attribute)
        return int(attribute)


    #导入导出
    def click_import_export(self, import_export):
        self.is_click(user['import_export'], import_export)
        sleep(1)

    @allure.step("获取列表导出下载进度值")
    def get_list_download_value(self):
        attribute = self.get_table_info(user['导出列表下载进度条'], attr='aria-valuenow')
        logging.info('下载进度值是%s' % attribute)
        return int(attribute)

    #单个条件查询
    @allure.step("Distributor Receipt页面，按Model字段筛选")
    def input_receipt_model_query(self, content):
        self.is_click(user['Model点击'])
        self.input_text(user['Model输入'], content)
        self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
        self.is_click(user['点击label标签'], 'Model')

    @allure.step("Distributor Receipt页面，按material id字段筛选")
    def input_material_id_query(self, content):
        self.input_text(user['MaterialID输入'], content)

    @allure.step("Distributor Receipt页面，按sap customer id字段筛选")
    def input_sap_customer_id_query(self, content):
        self.input_text(user['SAPCustomerID输入'], content)

    @allure.step("Distributor Receipt页面，按sap_delivery_date字段筛选")
    def input_sap_delivery_date_query(self, content):
        self.input_text(user['SAPDeliveryDate开始'], content)
        self.input_text(user['SAPDeliveryDate结束'], content)
        self.is_click(user['点击label标签'], 'SAP Delivery Date')

    @allure.step("Distributor Receipt页面，按brand字段筛选")
    def input_brand_query(self, content):
        self.is_click(user['Brand点击'])
        self.is_click(user['下拉框选择值'], content)
        self.is_click(user['点击label标签'], 'Brand')

    @allure.step("Distributor Receipt页面，按category字段筛选")
    def input_category_query(self, content, header):
        self.is_click(user['Category点击'])
        self.input_text(user['Category输入'], content, header)
        self.presence_sleep_dcr(user['下拉框选择值'], content)
        self.is_click(user['下拉框选择值'], content)
        self.is_click(user['点击label标签'], 'Category')

    @allure.step("Distributor Receipt页面，按imei字段筛选")
    def input_imei_query(self, content):
        self.is_click(user['IMEI点击'])
        self.input_text(user['IMEI输入'], content)

    @allure.step("Distributor Receipt页面，按imei字段筛选")
    def input_box_id_query(self, content):
        self.is_click(user['Box点击'])
        self.input_text(user['Box输入'], content)

    @allure.step("Distributor Receipt页面，按imei字段筛选")
    def input_market_name_query(self, content):
        self.is_click(user['MarketName点击'])
        self.input_text(user['MarketName输入'], content)
        self.presence_sleep_dcr(user['下拉框选择值'], content)
        self.is_click(user['下拉框选择值'], content)
        self.is_click(user['点击label标签'], 'Market Name')

    @allure.step("Distributor Receipt页面，按country字段筛选")
    def input_country_query(self, content, header):
        self.is_click(user['Country点击'])
        self.input_text(user['Country输入'], content)
        self.presence_sleep_dcr(user['下拉框选择值'], content)
        self.is_click(user['下拉框选择值'], content, header)
        self.is_click(user['点击label标签'], 'Country')

    @allure.step("Distributor Receipt页面，按status字段筛选")
    def input_status_query(self, content, content2, content3, header):
        self.is_click(user['Status点击'])
        self.is_click(user['下拉框选择值'], content, header)
        self.is_click(user['下拉框选择值'], content2, header)
        self.is_click(user['下拉框选择值'], content3, header)
        self.is_click(user['点击label标签'], 'Status')


    @allure.step("断言：列表页面查询结果")
    def assert_query_result(self, header, content):
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['menu表格字段'], user['表格内容'], header, content, sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("断言：页面查询结果")
    def assert_query_imei_detail_result(self, header, content):
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['menu表格字段'], user['表格内容'], header, content, h_element=user['IMEI Detail表头文本'])



class DistributorReceiptQuery(Base):
    """DistributorReceipt查询类"""
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

    @allure.step("根据表头获取详情页面列的class值")
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
            self.element_text(user['Loading'])
        elif txt == 'Reset':
            self.element_text(user['Loading'])
        else:
            sleep()

    @allure.step("输入文本,进行筛选")
    def select_content(self, type, content):
        #Customer，Box本页面有条件，但无结果展示，无法断言
        if type == 'Model':
            self.is_click(user['Model点击'])
            self.input_text(user['Model输入'], txt=content)
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
            self.is_click(user['点击label标签'], 'Model')
        elif type == 'Customer':
            self.is_click(user['Customer点击'])
            self.input_text(user['Customer输入'], txt=content)
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
        elif type == 'Material ID':
            self.input_text(user['MaterialID输入'], txt=content)
        elif type == 'DN':
            self.input_text(user['DN输入'], txt=content)
        elif type == 'SAP Delivery Date':
            self.input_text(user['SAPDeliveryDate开始'], txt=content)
            self.input_text(user['SAPDeliveryDate结束'], txt=content)
            self.is_click(user['DN输入'])
        elif type == 'SAP Customer ID':
            self.input_text(user['SAPCustomerID输入'], txt=content)
        elif type == 'Brand':
            self.is_click(user['Brand点击'])
            self.is_click(user['下拉框选择值'], content)
            self.click_dn()
        elif type == 'Category':
            self.is_click(user['Category点击'])
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
            self.click_dn()
        elif type == 'IMEI':
            self.is_click(user['IMEI点击'])
            self.input_text(user['IMEI输入'], txt=content)
        elif type == 'Market Name':
            self.is_click(user['MarketName点击'])
            self.input_text(user['MarketName输入'], txt=content)
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
            self.click_dn()
        elif type == 'Customer Region3':
            self.is_click(user['CustomerRegion点击'])
            logging.info('click Customer Region3  wrong')
            self.input_text(user['CustomerRegion点击'],txt=content)
            logging.info('click Customer Region3  right')
            self.is_click(user['CustomerRegion输入'], content)
        elif type == 'Delivery Country':
            self.is_click(user['Country点击'])
            self.input_text(user['Country输入'], txt=content)
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
        elif type == 'Status':
            self.is_click(user['Status点击'])
            #self.is_click(user['Status输入'])
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], 'Receiving')
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], 'On Transit')
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
            self.click_dn()
        else:
            logging.info('type is wrong,pls check')
        sleep()


if __name__ == '__main__':
    pass



