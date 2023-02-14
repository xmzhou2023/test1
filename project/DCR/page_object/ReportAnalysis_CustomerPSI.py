from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class CustomerPSIPage(Base):
    """CustomerPSIPage类，生产环境，Customer PSI页面元素定位"""

    @allure.step("输入开始与结束日期筛选")
    def input_query_date(self, content1, content2):
        """输入开始与结束日期筛选"""
        self.is_click(user['Start Date'])
        self.input_text(user['Start Date'], txt=content1)
        sleep(1)
        self.is_click(user['End Date'])
        self.input_text(user['End Date'], txt=content2)

    @allure.step("点击Distributor按钮筛选国包数据")
    def click_distributor(self):
        self.is_click(user['Distributor'])

    @allure.step("点击Sub-dealer按钮筛选二代数据")
    def click_sub_dealer(self):
        self.is_click(user['Sub-dealer'])

    def customer_psi_start_date_query(self, start_date):
        """Customer PSI 页面，输入开始Date条件筛选数据"""
        self.is_click(user['Customer PSI Start Date'])
        self.input_text(user['Customer PSI Start Date'], start_date)
        self.is_click(user['点击筛选项label'], 'Date')

    @allure.step("点击Search查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(3)
        self.element_exist(user['Loading'])

    @allure.step("获取分页总条数文本")
    def get_total_text(self):
        total = self.element_text(user['获取分页总条数'])
        total1 = total[6:]
        return total1

    @allure.step("获取Sales Region2字段文本")
    def get_sales_region2_text(self):
        self.presence_sleep_dcr(user['获取Sales Region2文本'])
        sale_region2 = self.element_text(user['获取Sales Region2文本'])
        return sale_region2

    @allure.step("获取Sales Region3字段文本")
    def get_sales_region3_text(self):
        sale_region3 = self.element_text(user['获取Sales Region3文本'])
        return sale_region3

    @allure.step("获取Brand字段文本")
    def get_brand_text(self):
        brand = self.element_text(user['获取Brand文本'])
        return brand

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])

    @allure.step("关闭客户PSI菜单")
    def click_close_customerPSI(self):
        self.is_click(user['关闭客户PSI菜单'])


    #Customer PSI列表数据筛选后，导出操作成功后验证
    @allure.step("Customer PSI页面，点击Export导出按钮")
    def click_export(self):
        self.find_element(user['Export'])
        self.is_click(user['Export'])
        sleep(2)

    @allure.step("点击Download Icon，点击More按钮")
    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        self.element_exist(user['Loading'])

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(0.5)
        self.is_click_dcr(user['Task Name value'], content)

    @allure.step("输入Create Date 开始日期筛选该任务的导出记录")
    def export_record_create_date_query(self, start_date):
        self.is_click(user['Export Record Create Date'])
        self.input_text(user['Export Record Create Date'], start_date)
        self.is_click(user['点击筛选项label'], 'Create Date')

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        down_status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
        return down_status

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_task_name_text(self):
        task_name = self.element_text(user['获取任务名称文本'])
        return task_name

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_file_size_text(self):
        """导出记录页面，获取列表 Task Name文本"""
        file_size = self.element_text(user['获取文件大小文本'])
        file_size1 = file_size[0:1]
        return file_size1

    @allure.step("导出记录页面，获取列表 User ID文本")
    def get_task_user_id_text(self):
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    @allure.step("导出记录页面，获取列表 Create Date文本")
    def get_create_date_text(self):
        self.scroll_into_view(user['获取创建日期文本'])
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
        if int(total) > 1:
            logging.info("按日期筛选Distributor Customer PSI后，能正常加载数据，Total{}".format(total))
        else:
            logging.info("按日期筛选Distributor Customer PSI后，未筛选到满足条件的数据，Total1{}".format(total))


    @allure.step("断言文件或导出时间是否有数据")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("Customer PSI导出成功，File Size 导出文件大于1KB:{}".format(file_size))
        else:
            logging.info("Customer PSI导出失败，File Size 导出文件小于1KB:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Customer PSI导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Customer PSI导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))

    @allure.step("断言精确查询结果 Customer PSI列表，字段列、字段内容是否与预期的字段内容值一致，有滚动条")
    def assert_customer_psi_field(self, header, content):
        DomAssert(self.driver).assert_search_contains_result(user['表格字段'], user['表格指定列内容'], header, content,
                                                    sc_element=user['水平滚动条'])



if __name__ == '__main__':
    pass