from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class CustomerPSIPage(Base):
    """CustomerPSIPage类，生产环境，Customer PSI页面元素定位"""

    def input_query_date(self, content1, content2):
        """输入开始与结束日期筛选"""
        self.is_click(user['Start Date'])
        self.input_text(user['Start Date'], txt=content1)
        sleep(1)
        self.is_click(user['End Date'])
        self.input_text(user['End Date'], txt=content2)

    def click_distributor(self):
        """点击Distributor按钮筛选国包数据"""
        self.is_click(user['Distributor'])

    def click_sub_dealer(self):
        """点击Sub-dealer按钮筛选二代数据"""
        self.is_click(user['Sub-dealer'])
        sleep(1)

    def click_search(self):
        """点击Search查询按钮"""
        self.is_click(user['Search'])

    def get_total_text(self):
        """获取分页总条数文本"""
        total = self.element_text(user['获取分页总条数'])
        return total

    def get_sales_region2_text(self):
        """获取Sales Region2字段文本"""
        sale_region2 = self.element_text(user['获取Sales Region2文本'])
        return sale_region2

    def get_sales_region3_text(self):
        """获取Sales Region3字段文本"""
        sale_region3 = self.element_text(user['获取Sales Region3文本'])
        return sale_region3

    def get_brand_text(self):
        """获取Brand字段文本"""
        brand = self.element_text(user['获取Brand文本'])
        return brand

    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    def click_close_customerPSI(self):
        """关闭客户PSI菜单"""
        self.is_click(user['关闭客户PSI菜单'])
        sleep(1)


    #Customer PSI列表数据筛选后，导出操作成功后验证
    def click_export(self):
        """Customer PSI页面，点击Export导出按钮"""
        self.is_click(user['Export'])

    def click_download_icon(self):
        self.is_click(user['Download Icon'])
        sleep(2)

    def click_more(self):
        self.is_click(user['More'])
        sleep(3.5)

    def click_export_search(self):
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