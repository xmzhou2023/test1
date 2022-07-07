from libs.common.read_element import Element
import logging
from project.DCR.page_object.inbound_receipt import InboundReceiptPage
from public.base.basics import Base
from libs.common.time_ui import sleep
from public.base.assert_ui import ValueAssert
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class ReturnOrderPage(Base):
    """ReturnOrderPage 类"""

    def return_order_iframe(self):
        """进入退货单列表页，iframe"""
        iframe = self.find_element(user['退货单列表iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)

    def add_return_order_iframe(self):
        """进入新增退货单页面，iframe"""
        iframe = self.find_element(user['新增退货单iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)

    def exit_iframe(self):
        """退出iframe"""
        self.driver.switch_to.parent_frame()
        sleep(2)

    def click_Add(self):
        """退货单页面，点击Add"""
        self.is_click(user['Add'])
        sleep(3)

    def click_Return_Type(self):
        """退货单页面，点击退货到卖家"""
        self.is_click(user['Return To Seller'])

    def radio_Delivery_order(self):
        """退货单页面，点击单选按钮退货单"""
        self.is_click(user['Radio Delivery order'])

    def input_Delivery_order(self, content):
        """退货单页面，输入IMEI"""
        self.is_click(user['Input Delivery Order'])
        self.input_text(user['Input Delivery Order'], txt=content)
        sleep(1)

    def click_Check(self):
        """退货单页面，点击Check"""
        self.is_click_dcr(user['Click Check'])
        sleep(2)

    def get_text_Record(self):
        """退货单页面，点击check获取结果 Succeed文本"""
        record = self.element_text(user['Get Scan Record'])
        return record

    def click_Submit(self):
        """退货单页面，点击Submit"""
        self.is_click_dcr(user['Submit'])

    def get_submit_success_text(self):
        """获取提交退货成功提示语"""
        submit_success = self.element_text(user['获取退货成功提示'])
        return submit_success

    def input_Delivery_Orderid(self, content):
        """退货单列表页面，筛选出库单ID"""
        self.is_click(user['Input Delivery Order ID'])
        self.input_text(user['Input Delivery Order ID'], txt=content)

    def click_Search(self):
        """退货单列表页面，点击Search"""
        self.is_click(user['Search'])
        sleep(1)

    def get_text_deliveryID(self):
        """退货单列表页面， 获取第筛选后的第一个出库单ID"""
        deliveryorder = self.element_text(user['获取列表第一个出库单'])
        return deliveryorder

    def get_return_status(self):
        """获取退货单列表，退货状态"""
        return_status = self.element_text(user['获取列表退货状态'])
        return return_status

    def click_checkbox(self):
        """退货单列表页面，第一个复选框勾选"""
        self.is_click(user['退货复选框勾选'])

    def click_Approve_button(self):
        """退货单列表页面，点击Approve按钮"""
        self.is_click(user['Approve button'])

    def input_remark(self, content):
        """退货单列表页面，输入退货评价"""
        self.is_click(user['Remark'])
        self.input_text(user['Remark'], txt=content)
        sleep(1)

    def click_agree(self):
        """是否确认退货对话框，输入是否同意退货"""
        self.is_click(user['Agree'])

    def get_text_Status(self):
        """退货单列表页面， 获取退货成功后的第一个Status Approved"""
        status = self.element_text(user['获取列表退货状态'])
        return status

    def get_Approval_Success(self):
        success = self.element_text(user['Approval Successfully'])
        return success


if __name__ == '__main__':
    pass
