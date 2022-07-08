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
    def click_add_sales(self):
        """Sales Order页面，点击Add新增销售单按钮"""
        self.is_click(user['Add'])
        sleep(1.5)

    def input_sales_buyer(self, content):
        """Add新增销售单页面，定位Buyer属性"""
        self.is_click(user['Buyer'])
        self.input_text(user['Buyer'], txt=content)
        sleep(1)
        self.is_click(user['Buyer value'])
        sleep(1)

    def input_sales_brand(self, content):
        self.is_click(user['Brand'])
        self.input_text(user['Brand'], txt=content)
        sleep(1)
        self.is_click(user['Brand value'])
        sleep(1)

    def input_sales_product(self, content):
        self.is_click(user['product'])
        self.input_text(user['product'], txt=content)
        sleep(3)
        self.is_click(user['product value'])
        sleep(1)

    def input_sales_quantity(self, content):
        self.is_click(user['Quantity'])
        self.input_text(user['Quantity'], txt=content)

    def click_submit(self):
        """新建销售单页面，点击提交按钮"""
        self.is_click_dcr(user['Submit Sales'])

    def click_submit_OK(self):
        """新建销售单页面，点击确认OK按钮"""
        self.is_click(user['保存成功确认OK'])

    def input_sales_order_ID(self, content):
        """销售单页面，按销售单ID条件筛选"""
        self.is_click(user['按销售单ID筛选'])
        self.input_text(user['按销售单ID筛选'], txt=content)
        sleep(2)

    def click_search(self):
        """销售单页面，点击Search查询按钮"""
        self.is_click(user['Sales Order Search'])
        sleep(2)

    def get_text_sales_id(self):
        """销售单页面，获取销售单ID文本"""
        sales_orde_id = self.element_text(user['获取Sales Order ID文本'])
        return sales_orde_id

    def get_text_sales_status1(self):
        """销售单页面，获取销售单状态文本"""
        status = self.element_text(user['获取Status Pending文本'])
        return status

    def get_text_sales_status2(self):
        """销售单页面，获取销售单状态文本"""
        status = self.element_text(user['获取Status Delivered文本'])
        return status

    """勾选新建的销售单，直接出库"""
    def click_checkbox_orderID(self):
        self.is_click(user['勾选第一条销售单ID'])

    def click_Delivery_button(self):
        self.is_click(user['Delivery button'])

    def Sales_Delivery_iframe(self):
        """Delivery Order页面，进入iframe"""
        iframe2 = self.find_element(user['Sales Delivery iframe'])
        self.driver.switch_to.frame(iframe2)
        sleep(1)

    def input_Payment_Mode(self, content):
        sleep(2)
        self.is_click(user['Payment Mode'])
        self.input_text(user['Payment Mode'], txt=content)
        sleep(2)
        self.is_click(user['Payment Mode value'])
        sleep(1)

    def input_imei(self, content):
        self.is_click(user['Input IMEI'])
        self.input_text(user['Input IMEI'], txt=content)
        sleep(1)

    def click_check(self):
        self.is_click_dcr(user['Check'])
        sleep(1)

    def click_submit_delivery(self):
        self.is_click_dcr(user['Submit Delivery'])
        sleep(3)


    #筛选IMEI Inventory Query页面，product对应的IMEI 元素定位
    def imei_inventory_iframe(self):
        """IMEI Inventory Query页面，进入iframe"""
        imei_iframe = self.find_element(user['imei inventory iframe'])
        self.driver.switch_to.frame(imei_iframe)
        sleep(1)

    def click_unfold(self):
        """ IMEI Inventory Query页面，点击Unfold展开按钮 """
        self.is_click(user['IMEI Inventory Unfold'])
        sleep(1)

    def input_material_id(self, content1):
        """ IMEI Inventory Query页面，输入material字段 """
        self.is_click(user['Material ID'])
        self.input_text(user['Material ID'], txt=content1)
        sleep(1)

    def click_inventory_search(self):
        """ IMEI Inventory Query页面，点击查询按钮 """
        self.is_click(user['IMEI库存查询按钮'])
        sleep(3)

    def get_text_imei_inventory(self):
        """ IMEI Inventory Query页面，获取列表IMEI文本内容 """
        imei = self.element_text(user['获取IMEI文本内容'])
        return imei


class InboundReceiptPage(Base):
    """InboundReceiptPage快速收货定位方法"""
    def input_salesOrder(self, content):
        """快速收货页面，输入销售单ID条件筛选"""
        self.input_text(user['Sales Order ID'], txt=content)

    def input_deliveryOrder(self, content):
        """快速收货页面，输入出库单ID条件筛选"""
        self.input_text(user['Delivery Order ID'], txt=content)

    def click_search(self):
        """快速收货页面，点击Search"""
        self.is_click(user['Inbound Receipt Search'])

    def get_text_salesOrder(self, content):
        """获取列表第一个销售单ID"""
        #salesorder = self.element_text_dcr(user['获取列表第一个销售单ID'], content)
        salesorder = self.element_text(user['获取列表第一个销售单ID'])
        return salesorder

    def get_text_deliveryOrder(self, content):
        """获取列表第一个出库单ID"""
        #deliveryorder = self.element_text_dcr(user['获取列表第一个出库单ID'], content)
        deliveryorder = self.element_text(user['获取列表第一个出库单ID'])
        return deliveryorder

    def click_checkbox(self):
        """快速收货页面，勾选第一个复选框"""
        self.is_click_dcr(user['第一个复选框'])
        sleep(1)

    def click_received(self):
        """快速收货页面，点击Quick Received按钮"""
        self.is_click_dcr(user['快速收货按钮'])
        sleep(1)

    def click_save(self):
        """快速收货页面，点击Save按钮"""
        self.is_click_dcr(user['保存'])
        sleep(2)

    def get_successfully_text(self):
        """快速收货页面，提交成功后获取提交成功提示语"""
        success = self.element_text(user['获取收货成功提示'])
        return success

    def get_text_status(self):
        """快速收货页面，获取列表第一条记录的最新状态"""
        status = self.element_text(user['获取第一个Status'])
        return status

    def click_reset(self):
        """快速收货页面，点击Reset重置按钮"""
        self.is_click(user['Reset'])


if __name__ == '__main__':
    pass