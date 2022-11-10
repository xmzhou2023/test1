from libs.common.read_element import Element
import logging
from libs.common.connect_sql import *
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class SalesOrderPage(Base):
    """SalesOrderPage销售订单页面定位方法"""

    @allure.step("Sales Order页面，点击Add新增销售单按钮")
    def click_add_sales(self):
        self.is_click(user['Add'])
        sleep(1.5)

    @allure.step("Add新增销售单页面，输入Sales Buyer属性")
    def input_sales_buyer(self, content):
        self.presence_sleep_dcr(user['Buyer'])
        self.is_click(user['Buyer'])
        self.input_text(user['Buyer'], txt=content)
        sleep(1)
        self.is_click(user['Buyer value'])

    @allure.step("新增销售单页面，输入Brand属性")
    def input_sales_brand(self, content):
        self.is_click(user['Brand'])
        self.input_text(user['Brand'], txt=content)
        sleep(1)
        self.is_click(user['Brand value'])

    @allure.step("新增销售单页面，输入product属性")
    def input_sales_product(self, content):
        self.is_click(user['product'])
        self.input_text(user['product'], txt=content)
        sleep(3)
        self.is_click(user['product value'], content)

    @allure.step("新增销售单页面，输入Quantity属性")
    def input_sales_quantity(self, content):
        self.is_click(user['Quantity'])
        self.input_text(user['Quantity'], txt=content)

    @allure.step("新建销售单页面，点击提交按钮")
    def click_submit(self):
        """新建销售单页面，点击提交按钮"""
        self.is_click_dcr(user['Submit Sales'])
        sleep(1)

    @allure.step("新建销售单页面，点击提交后，然后点击确认OK按钮")
    def click_submit_OK(self):
        self.presence_sleep_dcr(user['保存成功确认OK'])
        self.is_click(user['保存成功确认OK'])
        sleep(3)

    @allure.step("销售单页面，按销售单ID条件筛选")
    def input_sales_order_ID(self, content):
        self.is_click(user['按销售单ID筛选'])
        self.input_text(user['按销售单ID筛选'], txt=content)
        sleep(2)

    @allure.step("销售单页面，点击Search查询按钮")
    def click_search(self):
        """销售单页面，点击Search查询按钮"""
        self.is_click(user['Sales Order Search'])
        sleep(2)

    @allure.step("销售单页面，获取销售单ID文本")
    def get_text_sales_id(self):
        self.presence_sleep_dcr(user['获取Sales Order ID文本'])
        sales_order_id = self.element_text(user['获取Sales Order ID文本'])
        return sales_order_id

    @allure.step("销售单页面，获取销售单状态文本")
    def get_sales_status_text(self, status):
        self.presence_sleep_dcr(user['获取列表Status文本'], status)
        status = self.element_text(user['获取列表Status文本'], status)
        return status


    """勾选新建的销售单，直接出库"""
    @allure.step("勾选新建的 第一条销售单ID")
    def click_checkbox_orderID(self):
        self.is_click_dcr(user['勾选第一条销售单ID'])

    @allure.step("点击Delivery button出库按钮")
    def click_Delivery_button(self):
        self.is_click(user['Delivery button'])
        sleep(2)

    # @allure.step("Delivery Order页面，进入iframe")
    # def Sales_Delivery_iframe(self):
    #     iframe2 = self.find_element(user['Sales Delivery iframe'])
    #     self.driver.switch_to.frame(iframe2)
    #     sleep(1)

    @allure.step("新建出库单页面，输入Payment Mode支持方式属性")
    def input_Payment_Mode(self, content):
        self.presence_sleep_dcr(user['Payment Mode'])
        self.is_click(user['Payment Mode'])
        self.input_text(user['Payment Mode'], txt=content)
        self.presence_sleep_dcr(user['Payment Mode value'], content)
        self.is_click(user['Payment Mode value'], content)
        sleep(1)

    @allure.step("新建出库单页面，输入IMEI属性")
    def input_imei(self, content):
        self.is_click(user['Input IMEI'])
        self.input_text(user['Input IMEI'], txt=content)
        sleep(1)

    @allure.step("新建出库单页面，点击check检查IMEI按钮")
    def click_check(self):
        self.is_click_dcr(user['Check'])
        sleep(2)

    @allure.step("Add新增出库单页面，点击check后，右侧Delivery Quan属性下显示出库数量")
    def get_delivery_quantity(self):
        get_deli_quantity = self.element_text(user['Get Delivery Quantity'])
        return get_deli_quantity

    @allure.step("Add新增出库单页面，点击check后，Order Detail列表Delivery Quan属性下显示出库数量")
    def get_order_detail_deli_quantity(self):
        get_order_deli_quantity = self.element_text(user['Get Order Detail Deli Quantity'])
        return get_order_deli_quantity

    @allure.step("Add新增出库单页面，点击check后，Scan Record扫码记录下侧显示Success")
    def get_Deli_Scan_Record_Success(self):
        self.presence_sleep_dcr(user['Get Delivery Scan Record Success'])
        scan_record_success = self.element_text(user['Get Delivery Scan Record Success'])
        return scan_record_success

    @allure.step("Add新增出库单页面，点击check后，Scan Record扫码记录下侧出现显示IMEI")
    def get_Deli_Scan_Record_IMEI(self, imei):
        self.presence_sleep_dcr(user['Get Delivery Scan Record IMEI'], imei)
        scan_record_imei = self.element_text(user['Get Delivery Scan Record IMEI'], imei)
        return scan_record_imei

    @allure.step("新建出库单页面，点击Submit Delivery提交出库单按钮")
    def click_submit_delivery(self):
        self.is_click_dcr(user['Submit Delivery'])
        sleep(2)


    #筛选IMEI Inventory Query页面，product对应的IMEI 元素定位
    @allure.step("IMEI Inventory Query页面，点击Unfold展开筛选按钮")
    def click_unfold(self):
        self.is_click(user['IMEI Inventory Unfold'])
        sleep(1.5)

    @allure.step("IMEI Inventory Query页面，输入material字段 ")
    def input_material_id(self, content1):
        self.presence_sleep_dcr(user['Material ID'])
        self.is_click(user['Material ID'])
        self.input_text(user['Material ID'], txt=content1)

    @allure.step("IMEI库存页面，输入Warehouse查询仓库下的IMEI")
    def input_warehouse_query(self, warehouse):
        self.is_click(user['Warehouse'])
        self.input_text(user['Warehouse'], warehouse)
        sleep(2.5)
        self.presence_sleep_dcr(user['Select Warehouse Value'], warehouse)
        self.is_click_dcr(user['Select Warehouse Value'], warehouse)


    @allure.step("IMEI库存页面，根据Brand 查询仓库下的IMEI")
    def select_brand_query(self, brand):
        self.is_click(user['IMEI库存点击Brand'])
        self.is_click(user['IMEI库存select brand'], brand)

    @allure.step("IMEI Inventory Query页面，点击查询按钮")
    def click_inventory_search(self):
        self.is_click(user['IMEI库存查询按钮'])
        sleep(4.5)

    @allure.step("IMEI Inventory Query页面，获取列表IMEI文本内容")
    def get_text_imei_inventory(self):
        self.presence_sleep_dcr(user['获取IMEI文本内容'])
        imei = self.element_text(user['获取IMEI文本内容'])
        return imei

    @allure.step("刷新页面")
    def click_refresh(self, drivers):
        Base(drivers).refresh()

    @allure.step("关闭Sales Order销售单菜单")
    def click_close_sales_order(self):
        self.is_click(user['关闭销售单菜单'])
        sleep(1)

    @allure.step("关闭IMEI Inventory query菜单")
    def click_close_imei_inventory(self):
        self.is_click(user['关闭IMEI Inventory Query'])
        sleep(1)


class InboundReceiptPage(Base):
    """InboundReceiptPage快速收货定位方法"""

    @allure.step("快速收货页面，输入销售单ID条件筛选")
    def input_salesOrder(self, content):
        self.input_text(user['Sales Order ID'], txt=content)

    @allure.step("快速收货页面，输入出库单ID条件筛选")
    def input_deliveryOrder(self, content):
        self.input_text(user['Delivery Order ID'], txt=content)

    @allure.step("快速收货页面，点击Search")
    def click_search(self):
        self.is_click(user['Inbound Receipt Search'])
        sleep(5)

    @allure.step("获取列表第一个销售单ID")
    def get_text_salesOrder(self):
        self.presence_sleep_dcr(user['获取列表第一个销售单ID'])
        salesorder = self.element_text(user['获取列表第一个销售单ID'])
        return salesorder

    @allure.step("获取列表第一个出库单ID")
    def get_text_deliveryOrder(self):
        delivery_order = self.element_text(user['获取列表第一个出库单ID'])
        return delivery_order

    @allure.step("快速收货页面，勾选第一个复选框")
    def click_checkbox(self):
        self.presence_sleep_dcr(user['第一个复选框'])
        self.is_click_dcr(user['第一个复选框'])

    @allure.step("快速收货页面，点击Quick Received按钮")
    def click_quick_received(self):
        """快速收货页面，点击Quick Received按钮"""
        self.is_click_dcr(user['快速收货按钮'])
        sleep(2)

    @allure.step("快速收货页面，点击Save按钮")
    def click_save(self):
        self.is_click_dcr(user['保存'])
        sleep(0.7)

    @allure.step("快速收货页面，提交成功后获取提交成功提示语")
    def get_successfully_text(self):
        success = self.element_text(user['获取收货成功提示'])
        return success

    @allure.step("快速收货页面，获取列表第一条记录的最新状态")
    def get_text_status(self):
        self.presence_sleep_dcr(user['获取第一个Status'])
        status = self.element_text(user['获取第一个Status'])
        return status

    @allure.step("快速收货页面，点击Reset重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])

    @allure.step("快速收货页面，点击关闭Inbound Receipt菜单")
    def click_close_inbound_receipt(self):
        self.is_click(user['关闭二代收货菜单'])
        sleep(1)


if __name__ == '__main__':
    pass