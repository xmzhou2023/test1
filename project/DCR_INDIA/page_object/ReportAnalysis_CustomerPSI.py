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
        self.presence_sleep_dcr(user['Sub dealer'])
        self.is_click(user['Sub dealer'])

    def customer_psi_start_date_query(self, start_date):
        """Customer PSI 页面，输入开始Date条件筛选数据"""
        self.is_click(user['Customer PSI Start Date'])
        self.input_text(user['Customer PSI Start Date'], start_date)
        self.is_click(user['点击筛选项label'], 'Date')

    def click_search(self):
        """点击Search查询按钮"""
        self.is_click(user['Search'])
        sleep(3)
        self.element_text(user['Loading'])

    def get_total_text(self):
        """获取分页总条数文本"""
        total = self.element_text(user['获取分页总条数'])
        total1 = total[6:]
        return total1

    def get_sale_regiona_text(self):
        """获取Sales Region2字段文本"""
        Base.presence_sleep_dcr(self, user['获取Sale Regiona文本'])
        sale_region2 = self.element_text(user['获取Sale Regiona文本'])
        return sale_region2

    def get_sale_regionb_text(self):
        """获取Sales Region3字段文本"""
        sale_region3 = self.element_text(user['获取Sale Regionb文本'])
        return sale_region3

    def get_brand_text(self):
        """获取Brand字段文本"""
        brand = self.element_text(user['获取Brand文本'])
        return brand

    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1.5)

    def click_close_customerPSI(self):
        """关闭客户PSI菜单"""
        self.is_click(user['关闭客户PSI菜单'])
        sleep(2)



    #Customer PSI列表数据筛选后，导出操作成功后验证
    def click_export(self):
        """Customer PSI页面，点击Export导出按钮"""
        Base.presence_sleep_dcr(self, user['Export'])
        self.is_click(user['Export'])
        sleep(2)

    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        self.element_text(user['Loading'])


    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], content)
        sleep(1)
        self.is_click_dcr(user['Task Name value'], content)

    @allure.step("输入Create Date 开始日期筛选该任务的导出记录")
    def export_record_create_date_query(self, start_date):
        self.is_click(user['Export Record Create Date'])
        self.input_text(user['Export Record Create Date'], start_date)
        self.is_click(user['点击筛选项label'], 'Create Date')

    def click_export_search(self):
        """循环点击查询，直到获取到下载状态为COMPLETE """
        down_status = Base.export_download_status(self, user['Export Record Search'], user['获取下载状态文本'])
        return down_status

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
        if int(total) > 1:
            logging.info("按日期筛选Distributor Customer PSI后，能正常加载数据，Total{}".format(total))
        else:
            logging.info("按日期筛选Distributor Customer PSI后，未筛选到满足条件的数据，Total1{}".format(total))
        sleep(1)

    def assert_file_time_size(self, file_size, export_time):
        """断言文件或导出时间是否有数据 """
        if int(file_size) > 0:
            logging.info("Customer PSI导出成功，File Size 导出文件大于1KB:{}".format(file_size))
        else:
            logging.info("Customer PSI导出失败，File Size 导出文件小于1KB:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Customer PSI导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Customer PSI导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))
        sleep(1)

if __name__ == '__main__':
    pass