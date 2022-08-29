from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class VisitRecordPage(Base):
    """VisitRecordPage类，生产环境，Visit Record巡店记录页面元素定位"""

    @allure.step("Visit Record页面，点击unfold展开筛选条件")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("Visit Record页面，点击unfold展开筛选条件")
    def click_fold(self):
        self.is_click(user['Fold'])
        sleep(1)

    @allure.step("Visit Record页面，筛选Shop ID的巡店记录")
    def input_shop_id_query(self, content):
        self.is_click_dcr(user['Input Query Shop'])
        self.input_text_dcr(user['Input Query Shop'], txt=content)
        sleep(3)
        self.is_click(user['Select Shop Value'])

    @allure.step("Visit Record页面，输入Submit Start Date")
    def input_submit_start_date(self, content):
        sleep(3)
        Base.presence_sleep_dcr(self, user['Submit Start Date'])
        self.is_click(user['Submit Start Date'])
        sleep(1)
        self.input_text(user['Submit Start Date'], txt=content)

    @allure.step("Visit Record页面，点击Sales Region输入框")
    def click_sales_region(self):
        self.is_click(user['Sales Region'])

    @allure.step("Visit Record页面，点击Search查询按钮")
    def click_search(self):
        """Visit Record页面，点击Search查询按钮"""
        self.is_click(user['Search'])
        sleep(3)

    @allure.step("Visit Record页面，点击Reset重置按钮")
    def click_reset(self):
        """Visit Record页面，点击Reset重置按钮"""
        self.is_click(user['Reset'])
        sleep(4)

    @allure.step("Visit Record页面，获取列表中Shop ID文本属性")
    def get_shop_id_text(self):
        """Visit Record页面，获取列表中Shop ID文本属性"""
        Base.presence_sleep_dcr(self, user['获取Shop ID文本'])
        shop_id = self.element_text(user['获取Shop ID文本'])
        return shop_id

    @allure.step("Visit Record页面，获取列表中submit time文本属性")
    def get_submit_date_text(self):
        """Visit Record页面，获取列表中submit time文本属性"""
        submit_date = self.element_text(user['获取Submit Date文本'])
        return submit_date

    @allure.step("Visit Record页面，获取列表中Visit Date文本属性")
    def get_visit_date_text(self):
        """Visit Record页面，获取列表中Visit Date文本属性"""
        visit_date = self.element_text(user['获取Visit Date文本'])
        return visit_date

    @allure.step("Visit Record页面，获取列表中Visit Date文本属性")
    def get_view_operation_text(self):
        operation = self.element_text(user['Operation'])
        return operation

    @allure.step("Visit Record页面，获取列表中Visit Date文本属性")
    def get_total_text(self):
        total = self.element_text(user['获取总条数文本'])
        total1 = total[6:]
        return total1

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    @allure.step("Visit Record页面，点击关闭Visit Record菜单")
    def click_close_visit_record(self):
        self.is_click(user['关闭巡店记录菜单'])
        sleep(1)


    #巡店记录，导出功能验证
    @allure.step("Visit Record页面，点击Export导出按钮")
    def click_export(self):
        """Visit Record页面，点击Export导出按钮"""
        Base.presence_sleep_dcr(self, user['Export'])
        self.is_click(user['Export'])
        sleep(2)

    @allure.step("点击Download Icon，点击More更多按钮")
    def click_download_more(self):
        self.is_click(user['Download Icon'])
        sleep(1)
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        sleep(5)

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(2)
        self.is_click_dcr(user['Task Name value'], content)

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        down_status = Base.export_download_status(self, user['Export Record Search'], user['获取下载状态文本'])
        return down_status

    @allure.step("导出记录页面，获取列表 Download Status文本")
    def get_download_status_text(self):
        status = self.find_element(user['获取下载状态文本'])
        while status != "COMPLETE":
            status1 = self.element_text(user['获取下载状态文本'])
            return status1

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_task_name_text(self):
        task_name = self.element_text(user['获取任务名称文本'])
        return task_name

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_file_size_text(self):
        file_size = self.element_text(user['获取文件大小文本'])
        file_size1 = file_size[0:1]
        return file_size1

    @allure.step("导出记录页面，获取列表 User ID文本")
    def get_task_user_id_text(self):
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    @allure.step("导出记录页面，获取列表 Create Date文本")
    def get_create_date_text(self):
        create_date = self.element_text(user['获取创建日期文本'])
        create_date1 = create_date[0:10]
        return create_date1

    @allure.step("导出记录页面，获取列表Complete Date文本")
    def get_complete_date_text(self):
        complete_date = self.element_text(user['获取完成日期文本'])
        complete_date1 = complete_date[0:10]
        return complete_date1

    @allure.step("导出记录页面，获取列表 Operation文本")
    def get_export_operation_text(self):
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 0:
            logging.info("根据门店ID筛选，巡店记录列表中，加载筛选的数据正常，分页总条数Total:{}".format(total))
        else:
            logging.info("根据门店ID筛选，巡店记录列表中，未加载筛选的数据，分页总条数Total:{}".format(total))

    @allure.step("断言文件或导出时间是否有数据")
    def assert_file_time_size(self, file_size, export_time):
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
