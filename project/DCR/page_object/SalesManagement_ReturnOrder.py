from libs.common.read_element import Element
import logging
from public.base.basics import Base
from libs.common.time_ui import sleep
from public.base.assert_ui import ValueAssert
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ReturnOrderPage(Base):
    """ReturnOrderPage 类"""

    @allure.step("进入退货单列表页，iframe")
    def return_order_iframe(self):
        """进入退货单列表页，iframe"""
        iframe = self.find_element(user['退货单列表iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)

    @allure.step("进入新增退货单页面，iframe")
    def add_return_order_iframe(self):
        iframe = self.find_element(user['新增退货单iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)

    @allure.step("退出iframe")
    def exit_iframe(self):
        """退出iframe"""
        self.driver.switch_to.parent_frame()
        sleep(2)

    @allure.step("退货单页面，点击Add")
    def click_Add(self):
        self.is_click(user['Add'])
        sleep(3)

    @allure.step("退货单页面，点击退货到卖家")
    def click_Return_Type(self):
        Base.presence_sleep_dcr(self, user['Return To Seller'])
        self.is_click(user['Return To Seller'])

    @allure.step("退货单页面，点击单选按钮退货单")
    def radio_Delivery_order(self):
        self.is_click(user['Radio Delivery order'])

    @allure.step("退货单页面，输入IMEI")
    def input_Delivery_order(self, content):
        self.is_click(user['Input Delivery Order'])
        self.input_text(user['Input Delivery Order'], txt=content)
        sleep(1)

    @allure.step("退货单页面，点击Check")
    def click_Check(self):
        self.is_click_dcr(user['Click Check'])
        sleep(2)

    @allure.step("退货单页面，点击check获取结果 Succeed文本")
    def get_text_Record(self):
        record = self.element_text(user['Get Scan Record'])
        return record

    @allure.step("退货单页面，点击Submit")
    def click_Submit(self):
        self.is_click_dcr(user['Submit'])

    @allure.step("获取提交退货成功提示语")
    def get_submit_success_text(self):
        submit_success = self.element_text(user['获取退货成功提示'])
        return submit_success

    @allure.step("退货单列表页面，筛选出库单ID")
    def input_Delivery_Orderid(self, content):
        Base.presence_sleep_dcr(self, user['Input Delivery Order ID'])
        self.is_click(user['Input Delivery Order ID'])
        self.input_text(user['Input Delivery Order ID'], txt=content)

    @allure.step("退货单列表页面，点击Search")
    def click_Search(self):
        self.is_click(user['Search'])
        sleep(2)

    @allure.step("退货单列表页面， 获取第筛选后的第一个出库单ID")
    def get_text_deliveryID(self):
        Base.presence_sleep_dcr(self, user['获取列表第一个出库单'])
        deliveryorder = self.element_text(user['获取列表第一个出库单'])
        return deliveryorder

    @allure.step("获取退货单列表，退货状态")
    def get_return_status(self):
        Base.presence_sleep_dcr(self, user['获取列表退货状态'])
        return_status = self.element_text(user['获取列表退货状态'])
        return return_status

    @allure.step("退货单列表页面，第一个复选框勾选")
    def click_checkbox(self):
        Base.presence_sleep_dcr(self, user['退货复选框勾选'])
        self.is_click(user['退货复选框勾选'])

    @allure.step("退货单列表页面，点击Approve按钮")
    def click_Approve_button(self):
        self.is_click(user['Approve button'])

    @allure.step("退货单列表页面，输入退货评价")
    def input_remark(self, content):
        self.is_click(user['Remark'])
        self.input_text(user['Remark'], txt=content)
        sleep(1)

    @allure.step("是否确认退货对话框，输入是否同意退货")
    def click_agree(self):
        self.is_click(user['Agree'])

    @allure.step("退货单列表页面， 获取退货成功后的第一个Status Approved")
    def get_text_Status(self):
        Base.presence_sleep_dcr(self, user['获取列表退货状态'])
        status = self.element_text(user['获取列表退货状态'])
        return status

    @allure.step("获取审批成功提示语")
    def get_Approval_Success(self):
        success = self.element_text(user['Approval Successfully'])
        return success


if __name__ == '__main__':
    pass
