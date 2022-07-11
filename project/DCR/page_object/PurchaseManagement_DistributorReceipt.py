from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class DitributorReceiptPage(Base):
    """DitributorReceiptPage类"""

    def distri_receipt_iframe(self):
        """Distributor Receipt页面，进入iframe"""
        iframe = self.find_element(user['iframe Distributor Receipt'])
        self.driver.switch_to.frame(iframe)
        sleep(2)

    def exit_iframe(self):
        """退出iframe"""
        self.driver.switch_to.parent_frame()
        sleep(2)

    def click_unfold(self):
        """点击Unfold 展开更多筛选条件"""
        self.is_click(user['Unfold'])
        sleep(2)

    def input_dn(self, content):
        """国包收货列表页，输入DN条件筛选"""
        self.input_text(user['DN输入框'], txt=content)

    def click_first_chekbox(self):
        """勾选列表DN前面第一个复选框"""
        self.is_click(user['DN前面第一个复选框'])

    def click_quick_receive(self):
        """点击Quick Receive 快速收货按钮"""
        self.is_click(user['Quick Receive button'])
        sleep(2)

    def get_list_quantity_text(self):
        """获取列表 总数量total Quantity文本"""
        list_quantity = self.element_text(user['列表第一行Quantity文本'])
        return list_quantity

    def get_dialog_text_quantity(self):
        """获取收货对话框总数量Quantity文本"""
        dialog_quantity = self.element_text(user['收货对话框Quantity文本'])
        return dialog_quantity

    def get_list_dn_text(self):
        """获取列表第一个DN文本"""
        list_dn = self.element_text(user['列表第一个DN文本'])
        return list_dn

    def get_dialog_text_dn(self):
        """获取收货对话框DN文本"""
        dialog_dn = self.element_text(user['收货对话框DN文本'])
        return dialog_dn

    def click_search(self):
        """国包收货页面，筛选条件后，点击Search按钮"""
        self.is_click(user['国包收货列表Search'])
        sleep(5)

    def click_quick_receive_submit(self):
        """点击快速收货提交按钮"""
        self.is_click_dcr(user['国包收货Submit'])
        sleep(4)

    def get_success_text(self):
        """国包收货页面，筛选DN收货成功后，获取文本No Data """
        get_success = self.element_text(user['Get Successfully Text'])
        return get_success

    def click_reset(self):
        """国包收货页面，点击Reset按钮"""
        self.is_click(user['国包收货Reset'])
        sleep(4.5)

    def click_imei_detail(self):
        """国包收货页面，点击IMEI Detail按钮查看IMEI详情信息"""
        self.is_click(user['点击IMEI Detail'])
        sleep(3)

    def get_text_imei_detail_DN(self):
        """打开IMEI Detail页面，获取DN文本内容"""
        imei_detail_dn = self.element_text(user['IMEI Detail DN'])
        return imei_detail_dn

    def text_imei_detail_total(self):
        """IMEI Detail页面，获取IMEI总条数Total"""
        imei_detail_total = self.element_text(user['IMEI Detail Total'])
        return imei_detail_total

    def click_close(self):
        """IMEI Detail页面，点击右上角关闭图标，关闭页面"""
        self.is_click(user['Close IMEI Detail'])
        sleep(1)



    # def distributor_receipt(self):
    #     """国包收货用例"""
    #     #self.distri_receipt_iframe()
    #     list_dn = self.get_list_text_dn()
    #     list_quantity = self.get_list_quantity_text()
    #     self.click_unfold()
    #     self.input_dn(list_dn)
    #     self.click_search()
    #
    #     self.click_first_chekbox()
    #     self.click_quick_receive()
    #
    #     dialog_dn = self.get_dialog_text_dn()
    #     dialog_quantity = self.get_dialog_text_quantity()
    #
    #     if list_dn == dialog_dn:
    #         logging.info('验证列表获取的 DN与快速收货对话框的DN比较一致'.format(dialog_dn))
    #         if list_quantity == dialog_quantity:
    #             """快速收货，点击提交"""
    #             self.click_quick_receive_submit()
    #             logging.info('验证列表获取的 quantity与快速收货对话框的 quantity比较一致'.format(dialog_quantity))
    #         else:
    #             logging.info('验证列表获取的 quantity与快速收货对话框的 quantity比较不一致'.format(dialog_quantity))
    #     else:
    #         logging.info('验证列表获取的 DN与快速收货对话框的DN比较不一致'.format(dialog_dn))
    #
    #     no_data = self.get_text_nodata()
    #     if no_data == "No Data":
    #         logging.info('验证国包收货成功，状态已更新，列表不展示已收货状态的记录'.format(no_data))
    #     else:
    #         logging.info('验证国包收货失败，状态未更新，列表还展示On Transit 状态的记录'.format(no_data))
    #     sleep(1)
    #     self.click_reset()
    #     self.exit_iframe()

    # def check_imei_detail(self):
    #     #self.distri_receipt_iframe()
    #     list_dn = self.get_list_text_dn()
    #     list_quantity = self.get_list_quantity_text()
    #     sleep(1)
    #     #self.click_unfold()
    #     self.input_dn(list_dn)
    #     self.click_search()
    #
    #     self.click_imei_detail()
    #     imei_detail_dn = self.get_text_imei_detail_DN()
    #     detail_total = self.text_imei_detail_total()
    #
    #     if list_dn in imei_detail_dn:
    #         logging.info('验证列表获取的DN，与打开IMEI Detail详情页的DN比较一致'.format(imei_detail_dn))
    #         if list_quantity in detail_total:
    #             logging.info('验证列表获取的quantity总条数，与打开IMEI Detail详情页的Total总条数比较一致'.format(detail_total))
    #         else:
    #             logging.info('验证列表获取的DN，与打开IMEI Detail详情页的DN比较不一致'.format(detail_total))
    #     else:
    #         logging.info('验证列表获取的DN，与打开IMEI Detail详情页的DN比较不一致'.format(imei_detail_dn))
    #
    #     self.click_close()
    #     self.click_reset()
    #     self.exit_iframe()

if __name__ == '__main__':
    pass



