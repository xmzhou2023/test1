import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopIMEITransferPage(Base):
    """用户类"""
    @allure.step("点击新增按钮")
    def click_add_imei_transfer(self):
        self.is_click(user['Add IMEI Transfer'])
        sleep(2)

    @allure.step("输入转入店铺名称")
    def input_shop_transfer(self, info1):
        self.presence_sleep_dcr(user['Transfer To Shop Name'])
        self.is_click(user['Transfer To Shop Name'])
        self.input_text(user['Transfer To Shop Name'], info1)
        sleep(3)
        self.presence_sleep_dcr(user['Transfer To Shop Name value'], info1)
        self.is_click(user['Transfer To Shop Name value'], info1)

    @allure.step("输入ScanIMEI")
    def input_scan_imei(self, imei):
        self.input_text(user['Scan IMEI Name'], imei)

    @allure.step("点击check按钮")
    def click_check(self):
        self.is_click(user['Check Scan IMEI'])
        sleep(3)

    @allure.step("点击check按钮后，扫码IMEI是否成功，获取Scan Record记录里的IMEI")
    def get_scan_record_imei(self, imei):
        self.presence_sleep_dcr(user['Get Scan Record IMEI'], imei)
        get_imei = self.element_text(user['Get Scan Record IMEI'], imei)
        return get_imei

    @allure.step("点击check按钮后，扫码IMEI是否成功，获取Scan Record记录里的Success")
    def get_scan_record_success(self):
        get_success = self.element_text(user['Get Scan Record Success'], 'Success')
        return get_success

    @allure.step("点击check按钮后，扫码IMEI是否成功，获取Scanned为1的值")
    def get_scanned_value(self):
        self.presence_sleep_dcr(user['Get Scanned Value'], '1')
        get_scanned = self.element_text(user['Get Scanned Value'], '1')
        return get_scanned

    @allure.step("点击check按钮后，扫码IMEI是否成功，获取Rrder Detail Scanned为1的值")
    def get_order_detail_scanned(self):
        get_order_detail_scanned = self.element_text(user['Get Order Detail Scanned'])
        return get_order_detail_scanned

    @allure.step("点击Submit")
    def click_add_submit_ok(self):
        self.is_click(user['Add Submit'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Add OK'])
        self.is_click(user['Add OK'])
        sleep(3.5)

    @allure.step("获取列表Status文本内容")
    def get_list_transfer_id_text(self):
        self.presence_sleep_dcr(user['Get list Transfer ID Text'])
        get_transfer = self.element_text(user['Get list Transfer ID Text'])
        return get_transfer

    @allure.step("获取列表Status文本内容")
    def get_list_status_text(self, status):
        get_status = self.element_text(user['Get List Status Text'], status)
        return get_status

    @allure.step("获取列表To Shop文本内容")
    def get_list_to_shop_text(self, shop):
        self.scroll_into_view(user['Get List To Shop ID Text'], shop)
        get_to_shop = self.element_text(user['Get List To Shop ID Text'], shop)
        return get_to_shop

    @allure.step("获取列表Creator ID文本内容")
    def get_list_creator_id_text(self):
        get_creator_id = self.element_text(user['Get list Creator ID Text'])
        return get_creator_id

    @allure.step("Shop IMEI Transfer列表，输入To Shop进行筛选")
    def input_to_shop_query(self, to_shop):
        self.is_click_dcr(user['筛选门店'])
        self.input_text_dcr(user['筛选门店'], txt=to_shop)
        sleep(2)
        self.presence_sleep_dcr(user['选中筛选门店'], to_shop)
        self.is_click(user['选中筛选门店'], to_shop)

    @allure.step("Shop IMEI Transfer列表，输入状态进行筛选")
    def input_status_query(self, status):
        self.is_click(user['筛选状态'])
        self.input_text(user['筛选状态'], txt=status)
        sleep(1.5)
        self.presence_sleep_dcr(user['选中筛选状态'], status)
        self.is_click(user['选中筛选状态'], status)

    @allure.step("筛选出To Shop与pending状态的记录")
    def search_shop_pending(self, shop, status):
        self.is_click(user['unfold按钮'])
        sleep(2)
        self.input_to_shop_query(shop)
        self.input_status_query(status)
        self.is_click(user['search按钮'])
        sleep(3)

    @allure.step("点击Unfold展开按钮")
    def click_unfold(self):
        self.is_click(user['unfold按钮'])
        sleep(2)


    @allure.step("点击Search按钮")
    def click_search(self):
        self.is_click(user['search按钮'])
        sleep(3)

    @allure.step("点击Checkbox勾选全选复选框")
    def click_check_box(self):
        self.is_click(user['勾选全选复选框'])

    @allure.step("点击Approve或 reject按钮")
    def click_approve_reject(self, choose):
        self.is_click(user['Approve reject按钮'], choose)

    @allure.step("筛选出pending")
    def search_pending(self):
        self.is_click(user['unfold按钮'])
        sleep(2)
        self.is_click(user['Status条件筛选'])
        sleep(3)
        self.is_click(user['Pending按钮'])
        sleep(1)
        self.is_click(user['search按钮'])
        sleep(2)

    @allure.step("点击Approve，弹出弹窗Yes/Cancel按钮，点击OK审核通过")
    def click_approve_yes_ok(self, choose, yes_cancel):
        self.is_click(user['Approve reject按钮'], choose)
        sleep(1)
        self.is_click(user['Yes Cancel按钮'], yes_cancel)
        sleep(0.6)
        self.is_click(user['Approve OK按钮'])
        sleep(1)

    @allure.step("点击Reject按钮,输入拒绝原因，点击OK")
    def input_reject_reason(self, reason):
        self.is_click(user['输入拒绝原因'])
        self.input_text(user['输入拒绝原因'], txt=reason)
        self.is_click(user['Yes Cancel按钮'], 'Yes')
        sleep(1)
        self.is_click(user['Reject OK按钮'])

    @allure.step("点击Reset按钮")
    def click_reset(self):
        self.is_click(user['Reset 按钮'])
        sleep(4.5)

    @allure.step("获取Total分页总条数")
    def get_total_text(self):
        get_status = self.element_text(user['Get Total'])
        get_status1 = get_status[6:]
        return get_status1

    @allure.step("断言分页总条数，是否存在分页数据")
    def assert_total(self, total):
        if int(total) >= 1:
            logging.info("打印获取门店IMEI调店页面，的分页总条数{}".format(total))
        else:
            logging.info("打印获取门店IMEI调店页面，的分页总条数{}".format(total))

    @allure.step("筛选Create Date创建日期")
    def input_create_date_query(self, date):
        self.is_click(user['Create Start Date'])
        self.input_text(user['Create Start Date'], txt=date)

    @allure.step("点击筛选Create Date创建日期，释放光标")
    def click_create_end_date(self):
        self.is_click(user['Create End Date'])

    @allure.step("勾选第一条记录的复选框")
    def click_first_checkbox(self):
        self.is_click_dcr(user['勾选第一条复选框'])


if __name__ == '__main__':
    pass
