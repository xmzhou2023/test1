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
        sleep(1.5)

    #  同个客户不同仓库调拨-------------------------------------------------------------------------
    @allure.step("Create新增TransferOrder页面，输入TransferTo的warehouse属性")
    def input_to_warehouse(self, content):
        # Base.presence_sleep_dcr(self, user['TransferTo'])  等待
        self.is_click(user['SelectWarehouse'])
        sleep(2)
        # self.input_text(user['TransferTo'], txt=content)
        # sleep(2.5)
        self.is_click(user['lhmSubdealer001 WBD291503'])

    #  同级客户之间调拨----------------------------------------------------------------------------------------------
    @allure.step("Create新增TransferOrder页面，输入TransferTo的customer属性")
    def input_to_customer(self, content):
        self.is_click(user['TransferToCustomer'])
        sleep(2)
        self.is_click(user['NG20613 xylSub dealer'])

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

    @allure.step("TransferOrder页面，点击more option")
    def click_more_option(self):
        self.is_click(user['More Option'])
        sleep(2)

    @allure.step("TransferOrder页面，点击recall")
    def click_recall(self):
        self.is_click(user['Recall'])
        sleep(2)

    @allure.step("recall TransferOrder页面，点击Confirm")
    def click_recall_confirm(self):
        self.is_click(user['RecallConfirm'])
        sleep(2)

    # @allure.step("TransferOrder页面，点击confirm")
    # def click_confirm(self):
    #     #  Base.presence_sleep_dcr(self, user['Confirm'])
    #     self.is_click(user['Confirm'])
    #     sleep(2)

    #  ----------------------------------------------------------------------------------------
    @allure.step("Create新增TransferOrder页面，IMEI属性")
    def input_imei(self, content):
        self.input_text(user['ScanIMEI'], txt=content)

    @allure.step("Create新增TransferOrder页面，Check按钮")
    def click_check(self):
        # self.is_click_dcr(user['Check'])
        self.is_click(user['Check'])
        sleep(1)

    @allure.step("Create新增TransferOrder页面，Submit按钮")
    def click_submit(self):
        self.is_click(user['Submit'])
        sleep(1)

    @allure.step("Create新增TransferOrder页面，提交成功之后OK按钮")
    def click_ok(self):
        self.is_click(user['Ok'])
        sleep(2)


if __name__ == '__main__':
    pass
