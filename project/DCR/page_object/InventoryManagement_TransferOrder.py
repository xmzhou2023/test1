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

    @allure.step("Create新增TransferOrder页面，输入Transfer From的customer属性")
    def click_transfer_from_customer(self, customer):
        self.is_click(user['Transfer From'])
        sleep(1.5)
        self.is_click(user['Transfer From Select Customer'], customer)

    @allure.step("Create新增TransferOrder页面，输入Transfer From的warehouse属性")
    def click_transfer_from_warehouse(self, warehouse):
        self.is_click(user['Transfer From Warehouse'])
        sleep(1.5)
        self.is_click_dcr(user['Transfer From Select Warehouse'], warehouse)

    @allure.step("Create新增TransferOrder页面，输入Transfer To的customer属性")
    def click_transfer_to_customer(self, customer):
        self.is_click(user['Transfer To'])
        sleep(1.5)
        self.is_click(user['Transfer To Select Customer'], customer)

    @allure.step("Create新增TransferOrder页面，输入Transfer To的warehouse属性")
    def click_transfer_to_warehouse(self, warehouse):
        self.is_click(user['Transfer To Warehouse'])
        sleep(1.5)
        self.is_click_dcr(user['Transfer To Select Warehouse'], warehouse)

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
    def get_list_transfer_id(self):
        Base.presence_sleep_dcr(self, user['Get list Transfer ID'])
        get_transfer_id = self.element_text(user['Get list Transfer ID'])
        return get_transfer_id

    @allure.step("获取列表Order Status状态文本")
    def get_list_order_status(self):
        Base.presence_sleep_dcr(self, user['Get list Order Status'])
        get_order_status = self.element_text(user['Get list Order Status'])
        return get_order_status

    @allure.step("获取列表Receipt Status状态文本")
    def get_list_receipt_status(self):
        get_receipt_status = self.element_text(user['Get list Receipt Status'])
        return get_receipt_status

    @allure.step("勾选第一条复选框")
    def click_first_checkbox(self):
        self.is_click_dcr(user['Click First CheckBox'])

    @allure.step("勾选记录后，点击Confirm Receipt按钮,进行确认收货操作")
    def click_confirm_receipt(self, context):
        self.is_click(user['Confirm Receipt'])
        sleep(1)
        self.input_text(user['Receipt Remark'], context)
        self.is_click(user['点击确认收货按钮'])
        sleep(0.6)
        self.is_click(user['Confirm receipt or Recall'])

    @allure.step("未勾选记录时，点击Confirm Receipt 按钮,进行确认收货操作")
    def click_confirm_receipt1(self):
        self.is_click(user['Confirm Receipt'])

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
        sleep(0.6)
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

    @allure.step("点击IMEI Detail查询详情按钮")
    def click_imei_detail(self):
        self.is_click_dcr(user['IMEI Detail'])
        sleep(3)

    @allure.step("点击IMEI Detail查询详情按钮")
    def click_close_imei_detail(self):
        self.is_click(user['Close IMEI Detail'])
        sleep(1)


    def get_list_field(self, flag):
        self.scroll_into_view(user[flag])
        get_field = self.element_text(user[flag])
        return get_field


    #  对No Receive的调拨单进行撤回操作----------------------------------------------------------------------------------------------
    @allure.step("TransferOrder页面，勾选框")
    def choose_box(self):
        Base.presence_sleep_dcr(self, user['撤回复选框勾选'])
        self.is_click(user['撤回复选框勾选'])
        sleep(2)


    @allure.step("Create新增TransferOrder页面，提交成功之后OK按钮")
    def click_ok(self):
        self.is_click(user['Ok'])
        sleep(2)


if __name__ == '__main__':
    pass
