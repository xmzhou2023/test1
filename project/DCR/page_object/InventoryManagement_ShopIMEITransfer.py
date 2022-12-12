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
        sleep(1.5)

    @allure.step("输入转入店铺名称")
    def input_to_shop_transfer(self, info1):
        self.presence_sleep_dcr(user['Transfer To Shop Name'])
        self.is_click(user['Transfer To Shop Name'])
        self.input_text(user['Transfer To Shop Name'], info1)
        sleep(2)
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
        self.is_click(user['Shop IMEI Transfer Add Submit'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Shop IMEI Transfer Add Submit OK'])
        self.is_click(user['Shop IMEI Transfer Add Submit OK'])
        sleep(3.5)

    @allure.step("获取列表 Transfer ID 文本内容")
    def get_list_transfer_id(self):
        self.presence_sleep_dcr(user['Get Shop IMEI Transfer ID'])
        get_transfer = self.element_text(user['Get Shop IMEI Transfer ID'])
        return get_transfer

    @allure.step("获取列表Transfer ID文本内容, 带参数定位")
    def get_list_transfer_id_text(self, transfer_id):
        get_transfer = self.element_text(user['Get Shop IMEI Transfer ID content'], transfer_id)
        return get_transfer

    @allure.step("获取Shop IMEI Transfer列表Status文本内容")
    def get_list_transfer_status_text(self):
        get_status = self.element_text(user['Get Shop IMEI Transfer Status'])
        return get_status

    @allure.step("获取Shop IMEI Transfer列表To Shop文本内容")
    def get_list_to_shop_text(self):
        self.scroll_into_view(user['Get Shop IMEI Transfer To Shop ID'])
        get_to_shop = self.element_text(user['Get Shop IMEI Transfer To Shop ID'])
        return get_to_shop

    @allure.step("获取列表Creator ID文本内容")
    def get_list_creator_id_text(self):
        get_creator_id = self.element_text(user['Get list Shop IMEI Transfer Creator ID'])
        return get_creator_id

    @allure.step("Shop IMEI Transfer列表，输入To Shop进行筛选")
    def input_to_shop_query(self, to_shop):
        self.is_click_dcr(user['Shop IMEI Transfer query To Shop'])
        self.input_text_dcr(user['Shop IMEI Transfer query To Shop'], to_shop)
        sleep(2)
        self.presence_sleep_dcr(user['选中筛选门店'], to_shop)
        self.is_click(user['选中筛选门店'], to_shop)

    @allure.step("Shop IMEI Transfer列表，输入状态进行筛选")
    def input_status_query(self, status):
        self.is_click(user['Shop IMEI Transfer query Status'])
        self.input_text(user['Shop IMEI Transfer query Status'], status)
        sleep(1.5)
        self.presence_sleep_dcr(user['选中筛选状态'], status)
        self.is_click(user['选中筛选状态'], status)


    @allure.step("Shop IMEI Transfer列表，输入Transfer ID文本框条件是进行筛选")
    def shop_imei_transfer_input_query(self, position1, position2, parameter):
        self.is_click(user[position1])
        self.input_text(user[position2], parameter)

    @allure.step("Shop IMEI Transfer列表，输入Creator字段文本框条件进行筛选")
    def shop_imei_transfer_input_select_query(self, position1, position2, position3, parameter1, parameter2):
        self.is_click(user[position1])
        self.input_text(user[position2], parameter1)
        sleep(1.5)
        self.presence_sleep_dcr(user[position3], parameter2)
        self.is_click(user[position3], parameter2)


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
        self.is_click_dcr(user['勾选全选复选框'])

    @allure.step("点击Approve或 reject按钮")
    def click_approve_reject(self, choose):
        self.is_click(user['Approve reject按钮'], choose)
        sleep(1.5)

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

    @allure.step("点击Reject按钮,输入拒绝原因，点击OK")
    def input_reject_reason(self, reason, cancel_or_yes):
        self.is_click(user['输入拒绝原因'])
        self.input_text(user['输入拒绝原因'], txt=reason)
        self.is_click(user['Yes Cancel按钮'], cancel_or_yes)

    @allure.step("点击Reset按钮")
    def click_shop_imei_transfer_reset(self):
        self.is_click(user['Reset Button'])
        sleep(4)

    @allure.step("获取Shop IMEI Transfer列表，Total分页总条数")
    def get_list_total_text(self):
        get_status = self.element_text(user['Get Shop IMEI Transfer Total'])
        get_status1 = get_status[6:]
        return get_status1

    @allure.step("断言分页总条数，是否存在分页数据")
    def assert_total(self, total):
        if int(total) >= 1:
            logging.info("打印获取门店IMEI调店页面，的分页总条数{}".format(total))
        else:
            logging.info("打印获取门店IMEI调店页面，的分页总条数{}".format(total))

    @allure.step("筛选Create Date创建日期")
    def shop_imei_transfer_create_date_query(self, start_date, end_date):
        self.is_click(user['Shop IMEI Transfer Create Start Date'])
        self.input_text(user['Shop IMEI Transfer Create Start Date'], start_date)
        self.is_click(user['Shop IMEI Transfer Create End Date'])
        self.input_text(user['Shop IMEI Transfer Create End Date'], end_date)

    @allure.step("点击筛选Create Date创建日期，释放光标")
    def click_create_end_date(self):
        self.is_click(user['Shop IMEI Transfer Create End Date'])

    @allure.step("勾选第一条记录的复选框")
    def click_first_checkbox(self):
        self.is_click_dcr(user['勾选第一条复选框'])

    @allure.step("获取Shop IMEI Transfer列表字段内容")
    def get_list_field_text(self, field):
        self.scroll_into_view(user[field])
        self.presence_sleep_dcr(user[field])
        get_field = self.element_text(user[field])
        return get_field



    @allure.step("断言 Shop IMEI Transfer列表，字段列、字段内容是否与预期的字段内容值一致，有滚动条")
    def assert_shop_imei_transfer_field(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格指定列内容'], header, content, sc_element=user['水平滚动条'])

    @allure.step("断言 Shop IMEI Transfer列表，字段列、字段内容是否与预期的字段内容值一致，无滚动条")
    def assert_shop_imei_transfer_field2(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格指定列内容'], header, content, attr='class', index='0')


if __name__ == '__main__':
    pass
