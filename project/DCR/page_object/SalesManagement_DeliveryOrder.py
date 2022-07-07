from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class DeliveryOrderPage(Base):

    """DeliveryOrderPage类，Delivery Order页面，查询与新建出库单功能 元素定位"""
    def input_salesorder(self, content):
        """出库单页面，输入销售订单号"""
        self.input_text(user['Input Sales Order ID'], txt=content)
        sleep(1)

    def input_deliveryorder(self, content):
        """出库单页面，输入出库订单号"""
        self.input_text(user['Input Delivery Order ID'], txt=content)
        sleep(1)

    def click_search(self):
        """出库单页面，点击Search"""
        self.is_click(user['Search'])
        sleep(1)

    def click_reset(self):
        """出库单页面，点击Reset"""
        self.is_click(user['Reset'])
        sleep(2)

    def click_add(self):
        """出库单页面，点击Add新增出库单"""
        self.is_click(user['新增出库单'])
        sleep(3.5)

    def input_sub_buyer(self, content):
        """Add新增出库单页面，输入国包账号的Buyer属性"""
        self.is_click(user['Buyer'])
        self.input_text(user['Buyer'], txt=content, )
        sleep(2)
        self.is_click(user['Buyer sub value'])

    def input_retail_buyer(self, content):
        """Add新增出库单页面，输入二代账号的Buyer属性"""
        self.is_click(user['Buyer'])
        self.input_text(user['Buyer'], txt=content, )
        sleep(2)
        self.is_click(user['Buyer retail value'])

    def input_deli_pay_mode(self, content):
        """Add新增出库单页面，payment mode属性"""
        self.is_click(user['payment mode'])
        self.input_text(user['payment mode'], txt=content)
        sleep(1)
        self.is_click(user['payment mode Online'])

    def input_imei(self, content):
        """Add新增出库单页面，IMEI属性"""
        self.input_text(user['Input IMEI'], txt=content)

    def click_check(self):
        """Add新增出库单页面，Check按钮"""
        self.is_click_dcr(user['Check'])
        sleep(1)

    def click_submit(self):
        """Add新增出库单页面，Submit按钮"""
        self.is_click_dcr(user['Submit'])
        sleep(2)

    def get_text_submit(self):
        """Add新增出库单页面，Submit按钮"""
        submit = self.element_text(user['Submit'])
        return submit

    def get_text_submit_affirm(self):
        """Add新增出库单页面，确认Submit按钮"""
        affirm = self.element_text(user['Affirm Submit'])
        return affirm

    def click_submit_affirm(self):
        """Add新增出库单页面，确认Submit按钮"""
        self.is_click(user['Affirm Submit'])
        sleep(1)

    def text_sales_order(self):
        """获取出库单列表的 销售单ID文本"""
        sales_order = self.element_text(user['Get Sales Order ID Text'])
        return sales_order

    def text_delivery_order(self):
        """获取出库单列表的 出库单ID文本"""
        delivery_order = self.element_text(user['Get Delivery Order ID Text'])
        return delivery_order

    def text_delivery_Status(self):
        """获取出库单列表的 Status文本"""
        delivery_status = self.element_text(user['Get Status Text'])
        return delivery_status



    """DeliveryOrderPage类，测试环境，Delivery Order页面查询与导出功能元素定位"""
    def click_export(self):
        """Delivery Order页面，点击导出功能"""
        self.is_click(user['Click Export'])

    def click_unfold(self):
        """点击Unfold展开筛选条件"""
        self.is_click(user['Unfold'])
        sleep(2)

    def click_fold(self):
        """点击Fold 合拢筛选条件"""
        self.is_click(user['Fold'])
        sleep(1)

    def input_delivery_date(self, content1, content2):
        """输入Delivery Date开始与结束日期筛选"""
        self.is_click(user['Delivery Start Date'])
        self.input_text(user['Delivery Start Date'], txt=content1)
        sleep(1)
        self.is_click(user['Delivery End Date'])
        self.input_text(user['Delivery End Date'], txt=content2)

    def click_status_input_box(self):
        """点击 Status输入框"""
        self.is_click(user['点击状态输入框'])

    def get_total_text(self):
        """获取Total分页总条数文本"""
        total = self.element_text(user['Total'])
        return total

    def get_delivery_date_text(self):
        """获取列表Delivery Date文本内容"""
        deli_date = self.element_text(user['Get Delivery Date Text'])
        return deli_date

    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    def click_close_delivery_order(self):
        """出库单页面，关闭出库单菜单"""
        self.is_click(user['关闭出库单菜单'])

    def get_no_data(self):
        """ 出库单页面，no Data文本内容 """
        get_no_data = self.element_text(user['No Data'])
        return get_no_data


    #Delivery Order列表数据筛选后，导出操作成功后验证
    def click_download_icon(self):
        self.is_click(user['Download Icon'])
        sleep(2)

    def click_more(self):
        """点击more更多按钮"""
        self.is_click(user['More'])
        sleep(3)

    def click_export_search(self):
        """导出页面，点击Search按钮"""
        self.is_click(user['Export Record Search'])

    def get_download_status_text(self):
        """导出记录页面，获取列表 Download Status文本"""
        status = self.element_text(user['获取下载状态文本'])
        return status

    def get_task_name_text(self):
        """导出记录页面，获取列表 Task Name文本"""
        task_name = self.element_text(user['获取任务名称文本'])
        return task_name

    def get_file_size_text(self):
        """导出记录页面，获取列表 Task Name文本"""
        file_size = self.element_text(user['获取文件大小文本'])
        return file_size

    def get_task_user_id_text(self):
        """导出记录页面，获取列表 User ID文本"""
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    def get_create_date_text(self):
        """导出记录页面，获取列表 Create Date文本"""
        create_date = self.element_text(user['获取创建日期文本'])
        return create_date

    def get_complete_date_text(self):
        """导出记录页面，获取列表Complete Date文本"""
        complete_date = self.element_text(user['获取完成日期文本'])
        return complete_date

    def get_export_operation_text(self):
        """导出记录页面，获取列表 Operation文本"""
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    def get_export_time_text(self):
        """导出记录页面，获取列表导出时间文本"""
        export_time = self.element_text(user['获取导出时间'])
        return export_time


if __name__ == '__main__':
    pass