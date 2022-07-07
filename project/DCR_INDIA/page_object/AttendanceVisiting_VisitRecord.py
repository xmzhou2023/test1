from libs.common.read_element import Element
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)


class VisitRecordPage(Base):
    """VisitRecordPage类，生产环境，Visit Record巡店记录页面元素定位"""
    def click_unfold(self):
        """Visit Record页面，点击unfold展开筛选条件"""
        self.is_click(user['Unfold'])
        sleep(1.5)

    def click_fold(self):
        """Visit Record页面，点击unfold展开筛选条件"""
        self.is_click(user['Fold'])
        sleep(1.5)

    def input_shop_id_query(self, content):
        """Visit Record页面，筛选Shop ID的巡店记录"""
        self.is_click_dcr(user['Input Query Shop'])
        self.input_text_dcr(user['Input Query Shop'], txt=content)
        sleep(3)
        self.is_click(user['Select Shop Value'])

    def input_submit_start_date(self, content):
        self.is_click(user['Submit Start Date'])
        sleep(1)
        self.input_text(user['Submit Start Date'], txt=content)

    def click_sales_region(self):
        self.is_click(user['Sales Region'])

    def click_search(self):
        """Visit Record页面，点击Search查询按钮"""
        self.is_click(user['Search'])
        sleep(5)

    def click_reset(self):
        """Visit Record页面，点击Reset重置按钮"""
        self.is_click(user['Reset'])
        sleep(5)

    def get_shop_id_text(self):
        """Visit Record页面，获取列表中Shop ID文本属性"""
        shop_id = self.element_text(user['获取Shop ID文本'])
        return shop_id

    def get_submit_date_text(self):
        """Visit Record页面，获取列表中submit time文本属性"""
        submit_date = self.element_text(user['获取Submit Date文本'])
        return submit_date

    def get_visit_date_text(self):
        """Visit Record页面，获取列表中Visit Date文本属性"""
        visit_date = self.element_text(user['获取Visit Date文本'])
        return visit_date

    def get_view_operation_text(self):
        """Visit Record页面，获取列表中Visit Date文本属性"""
        operation = self.element_text(user['Operation'])
        return operation

    def get_total_text(self):
        """Visit Record页面，获取列表中Visit Date文本属性"""
        total = self.element_text(user['获取总条数文本'])
        return total

    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    def click_close_visit_record(self):
        """Visit Record页面，点击关闭菜单"""
        self.is_click(user['关闭巡店记录菜单'])
        sleep(1)


    #巡店记录，导出功能验证
    def iframe_export_record(self):
        """Export Record页面，进入iframe"""
        self.frame_enter(user['iframe Export Record'])
        sleep(1)

    def click_export(self):
        """Visit Record页面，点击Export导出按钮"""
        self.is_click(user['Export'])

    def click_download_icon(self):
        self.is_click(user['Download Icon'])
        sleep(2)

    def click_more(self):
        self.is_click(user['More'])
        sleep(3)

    def click_export_search(self):
        self.is_click(user['Export Record Search'])
        sleep(3)

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
