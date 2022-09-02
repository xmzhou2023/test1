from selenium.webdriver import Keys
from libs.common.read_element import Element
from libs.config.conf import BASE_DIR
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *
from public.base.basics import Base
from libs.common.time_ui import sleep
from libs.common.read_config import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class TransferOrderPage(Base):
    @allure.step("TransferOrder页面，点击Create新增TransferOrder")
    def click_create(self):
        Base.presence_sleep_dcr(self, user['Create'])
        self.is_click(user['Create'])
        sleep(2)

    @allure.step("Create新增TransferOrder页面，点击Transfer From的customer属性")
    def click_transfer_from_customer(self):
        self.is_click(user['Transfer From'])
        sleep(2)
        self.is_click(user['Transfer From Select Customer'], 'BD2915 lhmSubdealer001 ')

    @allure.step("Create新增TransferOrder页面，输入Transfer To的customer属性")
    def click_transfer_to_customer(self):
        self.is_click(user['Transfer To'])
        sleep(2)
        self.is_click(user['Transfer To Select Customer'], 'NG20613 xylSub dealer')

    @allure.step("Create新增TransferOrder页面，输入IMEI属性")
    def input_scan_imei(self, content):
        self.input_text(user['Scan IMEI'], txt=content)

    @allure.step("Create新增TransferOrder页面，Check按钮")
    def click_check(self):
        self.is_click(user['Check'])
        sleep(1.5)

    @allure.step("新增TransferOrder页面，获取scanned检测结果值")
    def get_scanned(self):
        get_scanned = self.element_text(user['Get Scanned Value'])
        return get_scanned

    @allure.step("新增TransferOrder页面，获取Order Detail列表下的 Delivery Quantity数量")
    def get_delivery_quantity(self):
        get_delivery_quantity = self.element_text(user['Get Order Detail Deli Quantity'])
        return get_delivery_quantity

    @allure.step("新增TransferOrder页面，获取Scan Record列表下的imei 字段")
    def get_scan_record_imei(self, imei):
        get_scan_record_imei = self.element_text(user['Get Scan Record IMEI'], imei)
        return get_scan_record_imei

    @allure.step("新增TransferOrder页面，获取Scan Record列表下的Success提示内容")
    def get_scan_record_success(self):
        get_success = self.element_text(user['Get Scan Record Success'])
        return get_success

    @allure.step("Create新增TransferOrder页面，Submit按钮")
    def click_submit(self):
        self.is_click(user['Submit'])
        sleep(0.5)

    @allure.step("Create新增TransferOrder页面，点击提交后，再点击OK确认提交")
    def click_submit_ok(self):
        self.is_click(user['Submit OK'])
        sleep(2)

    @allure.step("获取列表Transfer ID文本")
    def get_transfer_id(self):
        get_transfer_id = self.element_text(user['Get Transfer ID text'])
        return get_transfer_id

    @allure.step("获取列表Order Status状态文本")
    def get_order_status_text(self):
        get_order_status = self.element_text(user['Get Order Status text'])
        return get_order_status

    @allure.step("获取列表Receipt Status状态文本")
    def get_receipt_status_text(self):
        get_receipt_status = self.element_text(user['Get Receipt Status text'])
        return get_receipt_status

    @allure.step("勾选第一条复选框")
    def click_first_checkbox(self):
        self.is_click_dcr(user['Click First CheckBox'])

    @allure.step("点击Confirm Receipt 按钮")
    def click_confirm_receipt(self, context):
        self.is_click(user['Confirm Receipt'])
        sleep(0.5)
        self.is_click(user['Receipt Remark'])
        self.input_text(user['Receipt Remark'], context)
        self.is_click(user['点击确认收货按钮'])
        sleep(0.6)
        self.is_click(user['Confirm receipt or Recall'])

    @allure.step("点击Unfold,展开筛选项")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(1.5)

    @allure.step("输入Transfer ID筛选项条件，进行筛选")
    def input_transfer_id_query(self, context):
        self.input_text(user['点击调拨单筛选项'], context)

    @allure.step("点击Receipt Status收货状态筛选项")
    def click_receipt_status_query(self, status):
        Base.presence_sleep_dcr(self, user['点击收货状态筛选项'])
        self.is_click(user['点击收货状态筛选项'])
        sleep(1)
        self.is_click(user['选中Received状态'], status)

    @allure.step("点击Search按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(3)

    @allure.step("TransferOrder页面，点击more option,点击recall撤回")
    def click_more_option_recall(self):
        self.is_click(user['More Option'])
        sleep(2)
        self.is_click(user['Recall'])

    @allure.step("TransferOrder页面，点击more option,点击recall撤回")
    def click_more_option_recall_confirm(self):
        self.is_click(user['More Option'])
        sleep(2)
        self.is_click(user['Recall'])
        sleep(1)
        self.is_click(user['Confirm receipt or Recall'])
        sleep(0.5)

    @allure.step("TransferOrder页面，获取列表 Order Status状态")
    def get_list_order_status(self, status):
        get_order_status = self.element_text(user['Get list Order Status'], status)
        return get_order_status

    @allure.step("TransferOrder页面，获取列表Receive状态")
    def get_list_receipt_status(self, status):
        get_receipt_status = self.element_text(user['Get list Receipt Status'], status)
        return get_receipt_status

    # @allure.step("Create新增TransferOrder页面，输入TransferTo的warehouse属性")
    # def input_to_warehouse(self, content):
    #     Base.presence_sleep_dcr(self, user['TransferTo'])
    #     self.is_click(user['SelectWarehouse'])
    #     sleep(2)
    #     # self.input_text(user['TransferTo'], txt=content)
    #     # sleep(2.5)
    #     self.is_click(user['lhmSubdealer001 WBD291503'])


    # @allure.step("Create新增TransferOrder页面，输入TransferTo的warehouse属性")
    # def input_to_warehouse(self, content):
    #     self.is_click(user['TransferToWarehouse'])
    #     sleep(2)
    #     self.is_click(user['NG2061303 WNG2061304'])

    #  对No Receive的调拨单进行撤回操作----------------------------------------------------------------------------------------------
    @allure.step("TransferOrder页面，勾选框")
    def choose_box(self):
        Base.presence_sleep_dcr(self, user['撤回复选框勾选'])
        self.is_click(user['撤回复选框勾选'])
        sleep(2)
    #
    # @allure.step("TransferOrder页面，点击more option")
    # def click_more_option(self):
    #     self.is_click(user['More Option'])
    #     sleep(2)
    #
    # @allure.step("TransferOrder页面，点击recall")
    # def click_recall(self):
    #     self.is_click(user['Recall'])
    #     sleep(2)
    #
    # @allure.step("recall TransferOrder页面，点击Confirm")
    # def click_recall_confirm(self):
    #     self.is_click(user['RecallConfirm'])
    #     sleep(2)

    # @allure.step("TransferOrder页面，点击confirm")
    # def click_confirm(self):
    #     #  Base.presence_sleep_dcr(self, user['Confirm'])
    #     self.is_click(user['Confirm'])
    #     sleep(2)

    #  ----------------------------------------------------------------------------------------


    @allure.step("Create新增TransferOrder页面，提交成功之后OK按钮")
    def click_ok(self):
        self.is_click(user['Ok'])
        sleep(2)


if __name__ == '__main__':
    pass
