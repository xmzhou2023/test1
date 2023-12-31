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
        sleep(2)

    def click_fold(self):
        """Visit Record页面，点击unfold展开筛选条件"""
        self.is_click(user['Fold'])
        sleep(1.5)


    def input_shop_id_query(self, content):
        """Visit Record页面，筛选Shop ID的巡店记录"""
        self.is_click_dcr(user['Shop输入框'])
        self.input_text_dcr(user['Shop输入框2'], txt=content)
        sleep(3)
        self.is_click(user['Select Shop Value'], content)

    def input_submit_start_date(self, content):
        sleep(3)
        Base.presence_sleep_dcr(self, user['Submit Start Date'])
        self.is_click(user['Submit Start Date'])
        sleep(1)
        self.input_text(user['Submit Start Date'], txt=content)

    def click_sales_region(self):
        self.is_click(user['Sales Region'])

    def click_search(self):
        """Visit Record页面，点击Search查询按钮"""
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    def click_reset(self):
        """Visit Record页面，点击Reset重置按钮"""
        self.is_click(user['Reset'])
        self.element_exist(user['Loading'])

    def get_shop_id_text(self):
        """Visit Record页面，获取列表中Shop ID文本属性"""
        Base.presence_sleep_dcr(self, user['获取Shop ID文本'])
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
        """Visit Record页面，获取列表中Operation本属性"""
        operation = self.element_text(user['获取列表Operation文本'])
        return operation

    def get_total_text(self):
        """Visit Record页面，获取列表中Visit Date文本属性"""
        total = self.element_text(user['获取总条数文本'])
        total1 = total[6:]
        return total1

    #巡店记录，导出功能验证
    def click_export(self):
        """Visit Record页面，点击Export导出按钮"""
        Base.presence_sleep_dcr(self, user['Export'])
        self.is_click(user['Export'])
        sleep(2)

    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        self.element_exist(user['Loading'])

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], content)
        sleep(1)
        self.is_click_dcr(user['Task Name value'], content)

    @allure.step("输入Create Date开始日期筛选当天日期的导出记录")
    def export_record_create_date_query(self, start_date):
        self.is_click(user['导出记录筛选创建日期'])
        self.input_text(user['导出记录筛选创建日期'], start_date)
        self.is_click(user['点击筛选标签'], 'Create Date')

    def click_export_search(self):
        """循环点击查询，直到获取到下载状态为COMPLETE """
        down_status = Base.export_download_status(self, user['Export Record Search'], user['获取下载状态文本'])
        return down_status

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
        file_size1 = file_size[0:1]
        return file_size1

    def get_task_user_id_text(self):
        """导出记录页面，获取列表 User ID文本"""
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    def get_create_date_text(self):
        """导出记录页面，获取列表 Create Date文本"""
        create_date = self.element_text(user['获取创建日期文本'])
        create_date1 = create_date[0:10]
        return create_date1

    def get_complete_date_text(self):
        """导出记录页面，获取列表Complete Date文本"""
        complete_date = self.element_text(user['获取完成日期文本'])
        complete_date1 = complete_date[0:10]
        return complete_date1

    def get_export_operation_text(self):
        """导出记录页面，获取列表 Operation文本"""
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    def get_export_time_text(self):
        """导出记录页面，获取列表导出时间文本"""
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    def assert_total(self, total):
        """断言分页总数是否存在数据"""
        if int(total) > 0:
            logging.info("根据门店ID筛选，巡店记录列表中，加载筛选的数据正常，分页总条数Total:{}".format(total))
        else:
            logging.info("根据门店ID筛选，巡店记录列表中，未加载筛选的数据，分页总条数Total:{}".format(total))

    def assert_file_time_size(self, file_size, export_time):
        """断言文件或导出时间是否有数据 """
        if int(file_size) > 0:
            logging.info("Visit Record导出成功，File Size 导出文件大于0M:{}".format(file_size))
        else:
            logging.info("Visit Record导出失败，File Size 导出文件小于0M:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Visit Record导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Visit Record导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))

if __name__ == '__main__':
    pass
