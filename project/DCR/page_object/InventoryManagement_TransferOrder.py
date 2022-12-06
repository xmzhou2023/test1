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
        self.presence_sleep_dcr(user['Create'])
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
        self.input_text(user['Scan IMEI'], content)

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
        self.is_click(user['Transfer Order Submit'])
        sleep(0.5)

    @allure.step("Create新增TransferOrder页面，点击提交后，再点击OK确认提交")
    def click_submit_ok(self):
        self.is_click(user['Transfer Order Submit OK'])
        sleep(2.6)

    @allure.step("Transfer Order列表获取Transfer ID文本")
    def get_list_transfer_order_id(self):
        self.presence_sleep_dcr(user['Get list Transfer Order ID'])
        get_transfer_id = self.element_text(user['Get list Transfer Order ID'])
        return get_transfer_id

    @allure.step("Transfer Order列表获取Order Status状态文本")
    def get_list_transfer_order_status(self):
        self.presence_sleep_dcr(user['Get list Transfer Order Status'])
        get_order_status = self.element_text(user['Get list Transfer Order Status'])
        return get_order_status

    @allure.step("获取列表Receipt Status状态文本")
    def get_list_transfer_receipt_status(self):
        self.presence_sleep_dcr(user['Get list Transfer Receipt Status'])
        get_receipt_status = self.element_text(user['Get list Transfer Receipt Status'])
        return get_receipt_status

    @allure.step("勾选第一条复选框")
    def click_transfer_order_checkbox(self):
        self.presence_sleep_dcr(user['Transfer Order Click CheckBox'])
        self.is_click(user['Transfer Order Click CheckBox'])

    @allure.step("勾选Transfer ID记录后，点击Confirm Receipt按钮,进行确认收货操作")
    def click_transfer_confirm_receipt(self, context, confirm_receipt):
        self.is_click(user['Transfer Order Confirm Receipt'])
        sleep(1)
        self.input_text(user['Transfer Order Receipt Remark'], context)
        self.is_click(user['Transfer Confirm Receipt Button'], confirm_receipt)
        sleep(0.6)
        self.is_click(user['Transfer Confirm receipt or Recall'])

    @allure.step("勾选Transfer ID记录后，点击Return Goods按钮,进行退货操作")
    def click_transfer_return_goods(self, context, return_button):
        self.is_click(user['Transfer Order Confirm Receipt'])
        sleep(1)
        self.input_text(user['Transfer Order Receipt Remark'], context)
        self.is_click(user['Transfer Return Goods Button'], return_button)
        sleep(0.6)
        self.is_click(user['Transfer Confirm receipt or Recall'])

    @allure.step("未勾选记录时，点击Confirm Receipt 按钮,进行确认收货操作")
    def click_confirm_receipt1(self):
        self.is_click(user['Transfer Order Confirm Receipt'])



    @allure.step("Transfer Order列表，点击Confirm Receipt收货按钮,弹出收货窗口，然后关闭收货窗口")
    def close_transfer_receipt_remark(self):
        self.is_click(user['Close Transfer Receipt Remark'])


    @allure.step("点击Unfold,展开筛选项")
    def click_unfold(self):
        self.presence_sleep_dcr(user['Unfold'])
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("按Create Date字段筛选，Received 状态的数据")
    def input_transfer_create_start_date(self, create_date):
        self.presence_sleep_dcr(user['Create Start Date'])
        self.is_click(user['Create Start Date'])
        self.input_text(user['Create Start Date'], create_date)

    @allure.step("Transfer Order页面，输入Transfer ID筛选项条件，进行筛选")
    def input_transfer_order_id_query(self, context):
        self.input_text(user['Transfer Order Transfer ID Query'], context)

    @allure.step("点击Receipt Status收货状态筛选项")
    def click_transfer_receipt_status_query(self, status):
        self.presence_sleep_dcr(user['Transfer Receipt Status query'])
        self.is_click(user['Transfer Receipt Status query'])
        sleep(0.6)
        self.is_click(user['Transfer Select Received Status'], status)

    @allure.step("点击Search按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(1)

    @allure.step("Transfer Order页面，获取列表Total分页总条数")
    def get_transfer_order_list_total(self):
        get_list_total = self.element_text(user['Get list Transfer Order Total'])
        get_list_total1 = get_list_total[6:]
        return get_list_total1

    @allure.step("Transfer Order页面，获取IMEI Detail详情页Total分页总条数")
    def get_transfer_detail_total(self):
        self.presence_sleep_dcr(user['Get Transfer Detail Total'])
        get_detail_total = self.element_text(user['Get Transfer Detail Total'])
        get_detail_total1 = get_detail_total[6:]
        return get_detail_total1

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
        self.is_click(user['Transfer Confirm receipt or Recall'])
        sleep(0.5)

    @allure.step("点击IMEI Detail查询详情按钮")
    def click_transfer_imei_detail(self):
        self.is_click(user['Click Transfer IMEI Detail'])
        sleep(1.5)

    @allure.step("点击IMEI Detail查询详情按钮")
    def close_transfer_imei_detail(self):
        self.is_click(user['Close Transfer IMEI Detail'])

    def get_list_field(self, flag):
        self.scroll_into_view(user[flag])
        self.presence_sleep_dcr(user[flag])
        get_field = self.element_text(user[flag])
        return get_field


    #  对No Receive的调拨单进行撤回操作----------------------------------------------------------------------------------------------
    @allure.step("TransferOrder页面，勾选框")
    def choose_box(self):
        self.presence_sleep_dcr(user['撤回复选框勾选'])
        self.is_click(user['撤回复选框勾选'])
        sleep(2)

    @allure.step("Create新增TransferOrder页面，提交成功之后OK按钮")
    def click_ok(self):
        self.is_click(user['Ok'])
        sleep(2)

    @allure.step("Transfer Order页面，未点击Upload按钮，直接点击Save，提示请上传文件")
    def click_transfer_order_import(self):
        self.is_click(user['Transfer More Option'])
        sleep(0.5)
        self.is_click(user['Transfer Order Import'])
        sleep(1)
        self.is_click(user['Transfer Order Import Save'])

    @allure.step("Transfer Order页面，点击Import导入功能")
    def click_import_upload_save(self, file1):
        self.is_click(user['Transfer Order Import Upload'])
        sleep(2)
        ele = self.driver.find_element('xpath', "//button//..//input[@name='file']")
        ele.send_keys(file1)
        sleep(1.5)
        self.is_click(user['Transfer Order Import Save'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Transfer Order Upload Confirm'])
        self.is_click(user['Transfer Order Upload Confirm'])
        sleep(1)

    @allure.step("导入客户模板-上传正确的文件")
    def upload_true_file(self, file1):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', file1)
        logging.info("打印上传的客户模块文件path：{}".format(path1))
        self.click_import_upload_save(path1)

    @allure.step("Import Record页面，输入导入时间")
    def input_import_date(self, start_date):
        self.presence_sleep_dcr(user['Input Import Date'])
        self.is_click(user['Input Import Date'])
        self.input_text(user['Input Import Date'], start_date)


if __name__ == '__main__':
    pass
