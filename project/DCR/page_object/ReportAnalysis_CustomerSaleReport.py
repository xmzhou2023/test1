from libs.common.read_element import Element
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class CustomerSalesReportPage(Base):
    """InSCShopSalesQueryPage，印度生产环境，Shop Sales Query页面元素定位"""

    @allure.step("Shop Sales Query页面，进入iframe")
    def iframe_customer_sales_report(self):
        self.frame_enter(user['iframe Customer Sales Report'])
        sleep(1)

    @allure.step("退出iframe")
    def iframe_exit(self):
        self.frame_exit()
        sleep(1)

    @allure.step("输入客户销售报表开始与结束日期")
    def input_date(self, content1, content2):
        self.is_click(user['客户销售报表开始日期'])
        self.input_text(user['客户销售报表开始日期'], txt=content1)
        sleep(1)
        self.is_click(user['客户销售报表结束日期'])
        self.input_text(user['客户销售报表结束日期'], txt=content2)

    @allure.step("点击Search查询按钮")
    def click_search(self):
        self.is_click_dcr(user['Search'])
        sleep(6)

    @allure.step("点击Reset重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])

    @allure.step("获取出库总数文本")
    def get_delivery_sum_text(self):
        self.scroll_into_view(user['获取出库数量文本'])
        Base.presence_sleep_dcr(self, user['获取出库数量文本'])
        delivery_total = self.element_text(user['获取出库数量文本'])
        delivery_total1 = int(delivery_total)
        return delivery_total1

    @allure.step("获取实际销售总数文本")
    def get_actual_sales_sum_text(self):
        self.scroll_into_view(user['获取实际销售数量文本'])
        actual_sales = self.element_text(user['获取实际销售数量文本'])
        actual_sales1 = int(actual_sales)
        return actual_sales1

    @allure.step("获取退货总数文本")
    def get_return_sum_text(self):
        self.scroll_into_view(user['获取退货数量文本'])
        return_total = self.element_text(user['获取退货数量文本'])
        return_total1 = int(return_total)
        return return_total1


if __name__ == '__main__':
    pass
