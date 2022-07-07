from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class SalesOrderPage(Base):
    """SalesOrderPage页面定位方法"""
    def sales_iframe(self):
        """Sales Order页面，进入iframe"""
        iframe = self.find_element(user['Sales Order iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)

    def sales_iframe_add(self):
        """打开Add新建销售单页面，进入iframe"""
        iframe = self.find_element(user['Add Sales Order iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(2)

    def exit_iframe(self):
        """退出iframe"""
        self.driver.switch_to.parent_frame()
        sleep(1)

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
        self.is_click(user['Search'])
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
        self.is_click(user['Unfold'])
        sleep(1)

    def input_material_id(self, content1):
        self.is_click(user['Material ID'])
        self.input_text(user['Material ID'], txt=content1)
        sleep(1)


    def click_inventory_search(self):
        self.is_click(user['IMEI库存查询按钮'])
        sleep(3)

    def get_text_imei_inventory(self):
        imei = self.element_text(user['获取IMEI文本内容'])
        return imei


if __name__ == '__main__':
    pass