from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class DitributorReceiptPage(Base):
    """DitributorReceiptPage类"""

    @allure.step("Distributor Receipt页面，进入iframe")
    def distri_receipt_iframe(self):
        iframe = self.find_element(user['iframe Distributor Receipt'])
        self.driver.switch_to.frame(iframe)
        sleep(2)

    @allure.step("退出iframe")
    def exit_iframe(self):
        """退出iframe"""
        self.driver.switch_to.parent_frame()
        sleep(2)

    @allure.step("点击Unfold 展开更多筛选条件")
    def click_unfold(self):
        """点击Unfold 展开更多筛选条件"""
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("国包收货列表页，输入DN条件筛选")
    def input_dn(self, content):
        self.input_text(user['DN输入框'], txt=content)

    @allure.step("勾选列表DN前面第一个复选框")
    def click_first_chekbox(self):
        self.is_click(user['DN前面第一个复选框'])

    @allure.step("点击Quick Receive 快速收货按钮")
    def click_quick_receive(self):
        self.is_click(user['Quick Receive button'])
        sleep(2)

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
    def click_search(self):
        self.is_click(user['国包收货列表Search'])
        sleep(5)

    @allure.step("点击快速收货提交按钮")
    def click_quick_receive_submit(self):
        self.is_click_dcr(user['国包收货Submit'])
        sleep(4)

    @allure.step("国包收货页面，筛选DN收货成功后，获取文本No Data")
    def get_success_text(self):
        get_success = self.element_text(user['Get Successfully Text'])
        return get_success

    @allure.step("国包收货页面，点击Reset按钮")
    def click_reset(self):
        self.is_click(user['国包收货Reset'])
        sleep(4.5)

    @allure.step("国包收货页面，点击IMEI Detail按钮查看IMEI详情信息")
    def click_imei_detail(self):
        self.presence_sleep_dcr(user['点击IMEI Detail'])
        self.is_click(user['点击IMEI Detail'])
        sleep(3)

    @allure.step("打开IMEI Detail页面，获取DN文本内容")
    def get_text_imei_detail_DN(self):
        imei_detail_dn = self.element_text(user['IMEI Detail DN'])
        return imei_detail_dn

    @allure.step("IMEI Detail页面，获取IMEI总条数Total")
    def text_imei_detail_total(self):
        imei_detail_total = self.element_text(user['IMEI Detail Total'])
        return imei_detail_total

    @allure.step("IMEI Detail页面，点击右上角关闭图标，关闭页面")
    def click_close(self):
        self.is_click(user['Close IMEI Detail'])
        sleep(1)


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

    @allure.step("点击Unfold展开筛选项按钮")
    def click_button(self, txt):
        self.is_click(user['Unfold_Search_Reset按钮'], txt)
        if txt=='Search':
            sleep(5)
        elif txt == 'Reset':
            sleep(3)
        else:
            sleep()

    @allure.step("输入文本,进行筛选")
    def select_content(self, type, content):
        #Customer，Box本页面有条件，但无结果展示，无法断言
        if type == 'Model':
            self.is_click(user['Model点击'])
            self.input_text(user['Model输入'], txt=content)
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
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
            self.is_click(user['Model_Brand_Category_MarName_Country_Status选择'], content)
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



