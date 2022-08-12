from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *
import logging

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class InboundReceiptPage(Base):
    """InboundReceiptPage类"""
    def input_salesOrder(self, content):
        """快速收货页面，输入销售单ID条件筛选"""
        self.input_text(user['Input Sales Order ID'], txt=content)

    def input_deliveryOrder(self, content):
        """快速收货页面，输入出库单ID条件筛选"""
        self.input_text(user['Input Delivery Order ID'], txt=content)

    def click_deliver_Order(self):
        """快速收货页面，点击出库单ID筛选输入框"""
        self.is_click(user['Input Delivery Order ID'])

    def click_search(self):
        """快速收货页面，点击Search"""
        self.is_click(user['Search'])
        sleep(2)

    def text_salesOrder(self):
        """获取列表第一个销售单ID"""
        salesorder = self.element_text(user['获取列表第一个销售单ID'])
        return salesorder

    def text_deliveryOrder(self):
        """获取列表第一个出库单ID"""
        deliveryorder = self.element_text(user['获取列表第一个出库单ID'])
        return deliveryorder

    def select_checkbox(self):
        """快速收货页面，勾选第一个复选框"""
        Base.presence_sleep_dcr(self, user['收货第一个复选框'])
        self.is_click_dcr(user['收货第一个复选框'])

    def click_quick_received(self):
        """快速收货页面，点击Quick Received按钮"""
        self.is_click_dcr(user['快速收货按钮'])
        sleep(2)

    def click_save(self):
        """快速收货页面，点击Save按钮"""
        Base.presence_sleep_dcr(self, user['保存'])
        self.is_click(user['保存'])

    def get_successfully_text(self):
        """快速收货页面，提交成功后获取提交成功提示语"""
        success = self.element_text(user['获取收货成功提示'])
        return success

    def text_status(self):
        """快速收货页面，获取列表第一条记录的最新状态"""
        Base.presence_sleep_dcr(self, user['获取列表状态'])
        status = self.element_text(user['获取列表状态'])
        return status

    def click_reset(self):
        """快速收货页面，点击Reset重置按钮"""
        self.is_click(user['Reset'])
        sleep(4)

    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(2)

    def click_fold(self):
        self.is_click(user['Fold'])
        sleep(1)

    def input_delivery_date(self, content):
        """ 输入出库单日期条件，进行筛选操作 """
        self.is_click(user['Input Delivery Start Date'])
        self.input_text_dcr(user['Input Delivery Start Date'], txt=content)
        sleep(0.5)

    def click_select_brand(self):
        """ 输入品牌条件，进行筛选操作 """
        self.is_click_dcr(user['Click Select Brand'])
        sleep(1.5)
        self.is_click(user['Select itel'])
        self.is_click(user['Select TECNO'])

    def get_delivery_date_text(self):
        """获取列表Delivery Date文本"""
        delivery_date = self.element_text(user['Get Delivery Date'])
        return delivery_date

    def get_status_text(self):
        """获取列表Status文本"""
        status = self.element_text(user['Get Status'])
        return status

    def get_product_text(self):
        """获取列表Product文本"""
        product = self.element_text(user['Get Product'])
        return product

    def get_itel_text(self):
        """获取列表Product文本"""
        itel = self.element_text(user['Get Item'])
        return itel

    def get_brand_text(self):
        """获取列表Product文本"""
        brand = self.element_text(user['Get Brand'])
        return brand


    def get_total_text(self):
        """获取列表total文本"""
        total = self.element_text(user['Get Total Text'])
        total1 = int(total[7:])
        return total1

    def click_imei_detail(self):
        """Inbound Receipt列表点击 IMEI Detail按钮"""
        self.is_click(user['IMEI Detail'])
        sleep(1)

    def get_please_select_record(self):
        """获得请选择记录提示语"""
        select_record = self.element_text(user['Get Please select a record'])
        return select_record

    @allure.step("快速收货页面，点击关闭Inbound Receipt菜单")
    def click_close_inbound_receipt(self):
        self.is_click(user['关闭二代收货菜单'])
        sleep(2)

    @allure.step("快速收货页面，点击关闭IMEI Detail窗口")
    def click_close_inbound_imei_detail(self):
        self.is_click(user['关闭二代收货IMEI Detail'])
        sleep(2)


    #IMEI Detail页面元素定位方法
    def get_imei_detail_material_id(self):
        """获取IMEI Detail页面 material_id字段内容"""
        Base.presence_sleep_dcr(self, user['Get IMEI Detail Material ID'])
        material = self.element_text(user['Get IMEI Detail Material ID'])
        return material

    def get_imei_detail_product(self):
        """获取IMEI Detail页面 Product字段内容"""
        product = self.element_text(user['Get IMEI Detail Product'])
        return product

    def get_imei_detail_itel(self):
        """获取IMEI Detail页面 itel字段内容"""
        item = self.element_text(user['Get IMEI Detail Item'])
        return item

    def get_imei_detail_brand(self):
        """获取IMEI Detail页面 Brand字段内容"""
        brand = self.element_text(user['Get IMEI Detail Brand'])
        return brand

    def get_imei_detail_imei(self):
        """获取IMEI Detail页面 IMEI字段内容"""
        imei = self.element_text(user['Get IMEI'])
        return imei

    def get_imei_detail_total(self):
        """获取IMEI Detail页面 total字段内容"""
        total = self.element_text(user['Get IMEI Detail Total'])
        total1 = total[6:]
        return total1

    def get_imei_detail_export(self):
        """获取IMEI Detail页面 Export字段内容"""
        get_export = self.element_text(user['Get IMEI Detail Export'])
        return get_export

    def assert_total(self, total):
        if total > 0:
            logging.info("Inbound Receipt列表，分页总条数为{}".format(total))
        else:
            logging.info("Inbound Receipt列表，分页总条数为{}".format(total))
        sleep(1)

    def assert_total_imei_detail(self, total1):
        if int(total1) > 0:
            logging.info("查看Inbound Receipt列表，加载IMEI详情数据正常，分页总条数Total：{}".format(total1))
        else:
            logging.info("查看Inbound Receipt列表，加载IMEI详情数据失败，分页总条数Total：{}".format(total1))

if __name__ == '__main__':
    pass