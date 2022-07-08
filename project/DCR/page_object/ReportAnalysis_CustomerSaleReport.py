from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class CustomerSalesReportPage(Base):
    """InSCShopSalesQueryPage，印度生产环境，Shop Sales Query页面元素定位"""

    def iframe_customer_sales_report(self):
        """Shop Sales Query页面，进入iframe"""
        self.frame_enter(user['iframe Customer Sales Report'])
        sleep(1)

    def iframe_exit(self):
        """退出iframe"""
        self.frame_exit()
        sleep(1)

    def input_date(self, content1, content2):
        """输入客户销售报表开始与结束日期"""
        self.is_click(user['客户销售报表开始日期'])
        self.input_text(user['客户销售报表开始日期'], txt=content1)
        sleep(1)
        self.is_click(user['客户销售报表结束日期'])
        self.input_text(user['客户销售报表结束日期'], txt=content2)

    def click_search(self):
        """点击Search查询按钮"""
        self.is_click_dcr(user['Search'])
        sleep(3)

    def click_reset(self):
        """点击Reset重置按钮"""
        self.is_click(user['Reset'])

    def get_delivery_sum_text(self):
        """获取出库总数文本"""
        delivery_total = self.element_text(user['获取出库数量文本'])
        return delivery_total

    def get_actual_sales_sum_text(self):
        """获取实际销售总数文本"""
        actual_sales = self.element_text(user['获取实际销售数量文本'])
        return actual_sales

    def get_return_sum_text(self):
        """获取退货总数文本"""
        return_total = self.element_text(user['获取退货数量文本'])
        return return_total



