from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *
import logging

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class InboundReceiptPage(Base):
    """InboundReceiptPage类"""

    @allure.step("快速收货页面，输入销售单ID条件筛选")
    def input_salesOrder(self, content):
        """快速收货页面，输入销售单ID条件筛选"""
        self.input_text(user['Input Sales Order ID'], txt=content)

    @allure.step("快速收货页面，输入出库单ID条件筛选")
    def input_deliveryOrder(self, content):
        """快速收货页面，输入出库单ID条件筛选"""
        self.input_text(user['Input Delivery Order ID'], txt=content)

    @allure.step("快速收货页面，点击出库单ID筛选输入框")
    def click_deliver_Order(self):
        self.is_click(user['Input Delivery Order ID'])

    @allure.step("快速收货页面，点击Search")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(4)

    @allure.step("获取列表第一个销售单ID")
    def text_salesOrder(self):
        Base.presence_sleep_dcr(self, user['获取列表第一个销售单ID'])
        salesorder = self.element_text(user['获取列表第一个销售单ID'])
        return salesorder

    @allure.step("获取列表第一个出库单ID")
    def text_deliveryOrder(self):
        deliveryorder = self.element_text(user['获取列表第一个出库单ID'])
        return deliveryorder

    @allure.step("快速收货页面，勾选第一个复选框")
    def select_checkbox(self):
        Base.presence_sleep_dcr(self, user['收货第一个复选框'])
        self.is_click_dcr(user['收货第一个复选框'])

    @allure.step("快速收货页面，点击Quick Received按钮")
    def click_quick_received(self):
        self.is_click_dcr(user['快速收货按钮'])
        sleep(2)

    @allure.step("点击快速收货按钮后，弹出快速收货窗口，有多个仓库时需要选择仓库")
    def input_select_warehouse(self, warehouse):
        Base.presence_sleep_dcr(self, user['Quick Received select Warehouse'])
        self.is_click(user['Quick Received select Warehouse'])
        self.input_text(user['Quick Received select Warehouse'], txt=warehouse)
        sleep(1.5)
        self.is_click(user['Select Warehouse Value'], warehouse)

    @allure.step("快速收货页面，点击Save按钮")
    def click_save(self):
        Base.presence_sleep_dcr(self, user['保存'])
        self.is_click(user['保存'])
        sleep(0.6)

    @allure.step("快速收货页面，提交成功后获取提交成功提示语")
    def get_successfully_text(self):
        success = self.element_text(user['获取收货成功提示'])
        return success

    @allure.step("快速收货页面，获取列表第一条记录的最新状态")
    def text_status(self):
        Base.presence_sleep_dcr(self,user['获取列表状态'])
        status = self.element_text(user['获取列表状态'])
        return status

    @allure.step("快速收货页面，点击Reset重置按钮")
    def click_reset(self):
        """快速收货页面，点击Reset重置按钮"""
        self.is_click(user['Reset'])
        sleep(8)

    @allure.step("快速收货页面，点击Unfold展开筛选按钮")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("快速收货页面，点击Fold收起筛选按钮")
    def click_fold(self):
        self.is_click(user['Fold'])
        sleep(1)

    @allure.step("输入出库单日期条件，进行筛选操作")
    def input_delivery_date(self, content):
        self.is_click(user['Input Delivery Start Date'])
        self.input_text_dcr(user['Input Delivery Start Date'], txt=content)
        sleep(0.5)

    @allure.step("输入品牌条件，进行筛选操作")
    def click_select_brand(self):
        self.is_click_dcr(user['Click Select Brand'])
        sleep(1.5)
        self.is_click(user['Select TECNO'])
        self.is_click(user['Select itel'])

    @allure.step("获取列表Delivery Date文本")
    def get_delivery_date_text(self):
        delivery_date = self.element_text(user['Get Delivery Date'])
        return delivery_date

    @allure.step("获取收货页面，列表Status文本")
    def get_status_text(self):
        status = self.element_text(user['Get Status'])
        return status

    @allure.step("获取列表Product文本")
    def get_product_text(self):
        Base.presence_sleep_dcr(self, user['Get Product'])
        product = self.element_text(user['Get Product'])
        return product

    @allure.step("获取列表Product文本")
    def get_itel_text(self):
        itel = self.element_text(user['Get Item'])
        return itel

    @allure.step("获取列表Product文本")
    def get_brand_text(self):
        brand = self.element_text(user['Get Brand'])
        return brand

    @allure.step("获取列表total文本")
    def get_total_text(self):
        total = self.element_text(user['Get Total Text'])
        total1 = int(total[7:])
        return total1

    @allure.step("Inbound Receipt列表点击 IMEI Detail按钮")
    def click_imei_detail(self):
        self.is_click(user['IMEI Detail'])
        sleep(2)

    @allure.step("获取请选择记录提示语")
    def get_please_select_record(self):
        """获取请选择记录提示语"""
        select_record = self.element_text(user['Get Please select a record'])
        return select_record


    #IMEI Detail页面元素定位方法
    @allure.step("获取IMEI Detail页面 material_id字段内容")
    def get_imei_detail_material_id(self):
        Base.presence_sleep_dcr(self, user['Get IMEI Detail Material ID'])
        material = self.element_text(user['Get IMEI Detail Material ID'])
        return material

    @allure.step("获取IMEI Detail页面 Product字段内容")
    def get_imei_detail_product(self):
        product = self.element_text(user['Get IMEI Detail Product'])
        return product

    @allure.step("获取IMEI Detail页面 itel字段内容")
    def get_imei_detail_itel(self):
        item = self.element_text(user['Get IMEI Detail Item'])
        return item

    @allure.step("获取IMEI Detail页面 Brand字段内容")
    def get_imei_detail_brand(self):
        brand = self.element_text(user['Get IMEI Detail Brand'])
        return brand

    @allure.step("获取IMEI Detail页面 IMEI字段内容")
    def get_imei_detail_imei(self):
        imei = self.element_text(user['Get IMEI'])
        return imei

    @allure.step("获取IMEI Detail页面 total字段内容")
    def get_imei_detail_total(self):
        """获取IMEI Detail页面 total字段内容"""
        total = self.element_text(user['Get IMEI Detail Total'])
        total1 = total[6:7]
        return total1

    @allure.step("获取IMEI Detail页面 Export字段内容")
    def get_imei_detail_export(self):
        get_export = self.element_text(user['Get IMEI Detail Export'])
        return get_export

    @allure.step("断言 列表取分页总数判断是否有数据")
    def assert_total(self, total):
        if total > 0:
            logging.info("Inbound Receipt列表，分页总条数为{}".format(total))
        else:
            logging.info("Inbound Receipt列表，分页总条数为{}".format(total))
        sleep(1)

    @allure.step("断言 获取IMEI详情页，判断是否有数据")
    def assert_total_imei_detail(self, total1):
        if int(total1) > 0:
            logging.info("查看Inbound Receipt列表，加载IMEI详情数据正常，分页总条数Total：{}".format(total1))
        else:
            logging.info("查看Inbound Receipt列表，加载IMEI详情数据失败，分页总条数Total：{}".format(total1))


if __name__ == '__main__':
    pass