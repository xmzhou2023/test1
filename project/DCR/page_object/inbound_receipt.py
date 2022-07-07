from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class InboundReceiptPage(Base):
    """InboundReceiptPage类"""
    def input_salesOrder(self, content):
        """快速收货页面，输入销售单ID条件筛选"""
        self.input_text(user['Sales Order ID'], txt=content)

    def input_deliveryOrder(self, content):
        """快速收货页面，输入出库单ID条件筛选"""
        self.input_text(user['Delivery Order ID'], txt=content)

    def click_search(self):
        """快速收货页面，点击Search"""
        self.is_click(user['Search'])

    def text_salesOrder(self):
        """获取列表第一个销售单ID"""
        salesorder = self.element_text(user['获取列表第一个销售单ID'])
        return salesorder

    def text_deliveryOrder(self):
        """获取列表第一个出库单ID"""
        deliveryorder = self.element_text(user['获取列表第一个出库单ID'])
        return deliveryorder


    def checkbox(self):
        """快速收货页面，勾选第一个复选框"""
        self.is_click_dcr(user['收货第一个复选框'])

    def click_quick_received(self):
        """快速收货页面，点击Quick Received按钮"""
        self.is_click_dcr(user['快速收货按钮'])
        sleep(1)

    def click_save(self):
        """快速收货页面，点击Save按钮"""
        self.is_click(user['保存'])
        sleep(2)

    def get_successfully_text(self):
        """快速收货页面，提交成功后获取提交成功提示语"""
        success = self.element_text(user['获取收货成功提示'])
        return success

    def text_status(self):
        """快速收货页面，获取列表第一条记录的最新状态"""
        status = self.element_text(user['获取列表状态'])
        return status

    def click_reset(self):
        """快速收货页面，点击Reset重置按钮"""
        self.is_click(user['Reset'])


if __name__ == '__main__':
    pass