from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class DitributorReceiptPage(Base):
    """DitributorReceiptPage类"""

    @allure.step("Distributor Receipt页面，进入iframe")
    def distri_receipt_iframe(self):
        iframe = self.find_element(user['iframe Distributor Receipt'])
        self.driver.switch_to.frame(iframe)
        sleep(2)

    @allure.step("退出iframe")
    def exit_iframe(self):
        """退出iframe"""
        self.driver.switch_to.parent_frame()
        sleep(2)

    @allure.step("点击Unfold 展开更多筛选条件")
    def click_unfold(self):
        """点击Unfold 展开更多筛选条件"""
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("国包收货列表页，输入DN条件筛选")
    def input_dn(self, content):
        self.input_text(user['DN输入框'], txt=content)

    @allure.step("勾选列表DN前面第一个复选框")
    def click_first_chekbox(self):
        self.is_click(user['DN前面第一个复选框'])

    @allure.step("点击Quick Receive 快速收货按钮")
    def click_quick_receive(self):
        self.is_click(user['Quick Receive button'])
        sleep(2)

    @allure.step("获取列表 总数量total Quantity文本")
    def get_list_quantity_text(self):
        list_quantity = self.element_text(user['列表第一行Quantity文本'])
        return list_quantity


    @allure.step("获取收货对话框总数量Quantity文本")
    def get_dialog_text_quantity(self):
        dialog_quantity = self.element_text(user['收货对话框Quantity文本'])
        return dialog_quantity

    @allure.step("获取列表第一个DN文本")
    def get_list_dn_text(self):
        list_dn = self.element_text(user['列表第一个DN文本'])
        return list_dn

    @allure.step("获取收货对话框DN文本")
    def get_dialog_text_dn(self):
        dialog_dn = self.element_text(user['收货对话框DN文本'])
        return dialog_dn

    @allure.step("国包收货页面，筛选条件后，点击Search按钮")
    def click_search(self):
        self.is_click(user['国包收货列表Search'])
        sleep(5)

    @allure.step("点击快速收货提交按钮")
    def click_quick_receive_submit(self):
        self.is_click_dcr(user['国包收货Submit'])
        sleep(4)

    @allure.step("国包收货页面，筛选DN收货成功后，获取文本No Data")
    def get_success_text(self):
        get_success = self.element_text(user['Get Successfully Text'])
        return get_success

    @allure.step("国包收货页面，点击Reset按钮")
    def click_reset(self):
        self.is_click(user['国包收货Reset'])
        sleep(4.5)

    @allure.step("国包收货页面，点击IMEI Detail按钮查看IMEI详情信息")
    def click_imei_detail(self):
        Base.presence_sleep_dcr(self, user['点击IMEI Detail'])
        self.is_click(user['点击IMEI Detail'])
        sleep(3)

    @allure.step("打开IMEI Detail页面，获取DN文本内容")
    def get_text_imei_detail_DN(self):
        imei_detail_dn = self.element_text(user['IMEI Detail DN'])
        return imei_detail_dn

    @allure.step("IMEI Detail页面，获取IMEI总条数Total")
    def text_imei_detail_total(self):
        imei_detail_total = self.element_text(user['IMEI Detail Total'])
        return imei_detail_total

    @allure.step("IMEI Detail页面，点击右上角关闭图标，关闭页面")
    def click_close(self):
        self.is_click(user['Close IMEI Detail'])
        sleep(1)


if __name__ == '__main__':
    pass



