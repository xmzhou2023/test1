from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class DeliveryOrderPage(Base):
    """DeliveryOrderPage类，生产环境，Delivery Order页面元素定位"""
    def click_unfold(self):
        """点击Unfold展开筛选条件"""
        self.is_click(user['Unfold'])
        sleep(3)

    def click_fold(self):
        """点击Fold 合拢筛选条件"""
        self.is_click(user['Fold'])
        sleep(1)

    def input_delivery_date(self, content1, content2):
        """输入Delivery Date开始与结束日期筛选"""
        Base.presence_sleep_dcr(self, user['Delivery Start Date'])
        self.is_click(user['Delivery Start Date'])
        self.readonly_input_text(user['Delivery Start Date'], content1)
        self.is_click(user['Delivery End Date'])
        self.readonly_input_text(user['Delivery End Date'], content2)

    def click_status_input_box(self):
        """点击 Status输入框"""
        self.is_click(user['点击状态输入框'])

    def click_search(self):
        """点击Search查询按钮"""
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    def get_total_text(self):
        """获取Total分页总条数文本"""
        total = self.element_text(user['Total'])
        total1 = total[6:]
        return total1

    def get_sales_order_text(self):
        """获取列表Sales Order ID文本内容"""
        Base.presence_sleep_dcr(self, user['Get Sales Order ID Text'])
        sales_order = self.element_text(user['Get Sales Order ID Text'])
        return sales_order

    def get_delivery_order_text(self):
        """获取列表Delivery Order ID文本内容"""
        delivery_order = self.element_text(user['Get Delivery Order ID Text'])
        return delivery_order

    def get_delivery_date_text(self):
        """获取列表Delivery Date文本内容"""
        deli_date = self.element_text(user['Get Delivery Date Text'])
        return deli_date

    def get_status_text(self):
        """获取列表Status文本内容"""
        status = self.element_text(user['Get Status Text'])
        return status

    def get_no_data(self):
        """ 出库单页面，no Data文本内容 """
        get_no_data = self.element_text(user['No Data'])
        return get_no_data

    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    def click_close_delivery_order(self):
        """出库单页面，关闭出库单菜单"""
        self.is_click(user['关闭出库单菜单'])
        sleep(2)


    #Delivery Order列表数据筛选后，导出操作成功后验证
    def click_export(self):
        """Delivery Order页面，点击导出功能"""
        Base.find_element(self, user['Click Export'])
        self.is_click(user['Click Export'])
        sleep(2)

    def click_download_more(self):
        """点击more更多按钮"""
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
        status = self.find_element(user['获取下载状态文本'])
        while status != "COMPLETE":
            status1 = self.element_text(user['获取下载状态文本'])
            return status1

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
            logging.info("查看Delivery Order列表，加载数据正常，分页总记录数：{}".format(total))
        else:
            logging.info("查看Delivery Order列表，加载数据失败，分页总记录数：{}".format(total))
        sleep(1)

    def assert_file_time_size(self, file_size, export_time):
        """断言文件或导出时间是否有数据 """
        if int(file_size) > 0:
            logging.info("Delivery Order导出成功，File Size 导出文件大于1KB:{}".format(file_size))
        else:
            logging.info("Delivery Order导出失败，File Size 导出文件小于1KB:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Delivery Order导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Delivery Order导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))


if __name__ == '__main__':
    pass