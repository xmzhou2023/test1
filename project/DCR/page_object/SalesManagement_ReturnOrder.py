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


    @allure.step("退货单页面，输入Delivery Order ID")
    def input_Delivery_order(self, content):
        self.is_click(user['Input Delivery Order'])
        self.input_text(user['Input Delivery Order'], txt=content)
        sleep(1)

    @allure.step("退货单页面，点击Check")
    def click_Check(self):
        self.is_click_dcr(user['Click Check'])
        sleep(3.5)

    @allure.step("退货单页面，点击check获取结果 Succeed文本")
    def get_text_Record(self):
        record = self.element_text(user['Get Scan Record'])
        return record

    @allure.step("退货单页面，点击Submit")
    def click_Submit(self):
        self.is_click(user['Submit'])

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
        sleep(3)

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
        sleep(3)

    @allure.step("退货单列表页面，输入退货评价")
    def input_remark(self, content):
        Base.presence_sleep_dcr(self, user['Remark'])
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


    """无码申请退货"""
    @allure.step("新建退货页面，点击无码单选按钮")
    def click_radio_quantity(self):
        self.is_click(user['Radio Quantity'], "Quantity")
        sleep(2)

    @allure.step("新建退货页面，输入退货的客户")
    def input_quantity_customer(self, content):
        Base.presence_sleep_dcr(self, user['Quantity Customer'])
        self.is_click(user['Quantity Customer'])
        self.input_text(user['Quantity Customer'], txt=content)
        sleep(2)
        self.is_click(user['Quantity Customer value'], "BD2915 lhmSubdealer001")

    @allure.step("新建退货页面，输入退货的出库单ID")
    def input_quantity_delivery_order(self, content):
        self.is_click(user['Quantity Delivery Order ID'])
        self.input_text(user['Quantity Delivery Order ID'], txt=content)
        sleep(2)
        self.is_click(user['Quantity Delivery Order ID value'], content)

    @allure.step("新建退货页面，输入退货的product")
    def click_quantity_product(self, content):
        self.is_click(user['Quantity Product'])
        sleep(2)
        self.is_click(user['Quantity Product value'], content)

    @allure.step("新建退货页面，输入退货的数量")
    def input_return_quantity(self, content):
        self.is_click(user['Return Quantity'])
        self.input_text(user['Return Quantity'], txt=content)
        sleep(1)

    @allure.step("新建退货页面，切换无码退货单选按钮，点击Chek后，获取Delivery Order ID")
    def get_quantity_deli_order_text(self, content):
        get_quantity_deli = self.element_text(user['Get Quantity Delivery Order Text'], content)
        return get_quantity_deli

    @allure.step("新建退货页面，切换无码退货单选按钮，点击Chek后，获取Seller ID")
    def get_quantity_seller_id_text(self, content):
        get_seller_id = self.element_text(user['Get Quantity Seller ID Text'], content)
        return get_seller_id

    @allure.step("新建退货页面，切换无码退货单选按钮，点击Chek后，获取Buyer ID")
    def get_quantity_buyer_id_text(self, content):
        get_buyer_id = self.element_text(user['Get Quantity Buyer ID Text'], content)
        return get_buyer_id

    @allure.step("退货页面，点击关闭退货菜单")
    def click_close_return_order(self):
        self.is_click(user['关闭退货菜单'])
        sleep(2)

if __name__ == '__main__':
    pass
