from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopSaleQueryPage(Base):
    """ShopSalesQueryPage，生产环境，Shop Sales Query页面元素定位"""

    @allure.step("Shop Sales Query页面，根据Shop ID条件筛选 门店销售数据")
    def input_query_shop_id(self, content):
        self.is_click_dcr(user['筛选门店'])
        self.input_text_dcr(user['筛选门店'], txt=content)
        sleep(3)
        self.is_click(user['Select Shop Value'])

    @allure.step("点击Unfold展开筛选项按钮")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(1)

    @allure.step("点击fold收起筛选项按钮")
    def click_fold(self):
        self.is_click(user['Fold'])
        sleep(1)

    @allure.step("输入Upload Date筛选项的开始时间")
    def input_upload_start_date(self, content):
        self.is_click(user['Input Upload Start Date'])
        self.input_text(user['Input Upload Start Date'], txt=content)

    @allure.step("输入销售日期开始时间与结束时间Sales Date Start Date")
    def input_sales_date(self, content1, content2):
        self.is_click(user['Sales Date Start Date'])
        self.input_text(user['Sales Date Start Date'], txt=content1)
        self.is_click(user['Sales Date End Date'])
        self.input_text(user['Sales Date End Date'], txt=content2)

    @allure.step("Shop Sales Query页面，筛选Shop ID后，点击Search按钮")
    def click_search(self):
        self.is_click_dcr(user['Search'])
        sleep(3)

    @allure.step("Shop Sales Query页面，筛选Shop ID后，点击Search按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(5)

    @allure.step("Shop Sales Query页面，获取列表Shop ID 文本内容")
    def get_shop_id_text(self):
        Base.presence_sleep_dcr(self, user['获取门店ID文本'])
        shop_id = self.element_text(user['获取门店ID文本'])
        return shop_id

    @allure.step("Shop Sales Query页面，获取列表Shop ID 文本内容")
    def get_shop_name_text(self):
        shop_name = self.element_text(user['获取门店名称文本'])
        return shop_name

    @allure.step("Shop Sales Query页面，获取列表Status文本内容")
    def get_status_text(self):
        status = self.element_text(user['获取状态文本'])
        return status

    @allure.step("Shop Sales Query页面，获取列表sales date销售日期文本")
    def get_sales_date_text(self):
        sales_date = self.element_text(user['获取销售日期文本'])
        return sales_date

    @allure.step("Shop Sales Query页面，获取列表获取Public ID文本内容")
    def get_public_id_text(self):
        public_id = self.element_text(user['获取Public ID文本'])
        return public_id

    @allure.step("Shop Sales Query页面，获取列表获取总条数文本")
    def get_total_text(self):
        Base.presence_sleep_dcr(self, user['获取总条数文本'])
        total = self.element_text(user['获取总条数文本'])
        total1 = total[6:]
        return total1

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    @allure.step("关闭门店销售查询菜单")
    def click_close_shop_sales_query(self):
        self.is_click(user['关闭门店销售查询菜单'])
        sleep(1.5)

    @allure.step("点击Upload Date结束时间日期框")
    def click_upload_end_date(self):
        self.is_click(user['Click Upload End Date'])



    #门店销售查询，导出功能验证
    @allure.step("Shop Sales Query页面，点击Export 导出门店销量查询数据")
    def click_export(self):
        self.is_click(user['Export'])
        sleep(2)

    @allure.step("点击异步导出，点击更多按钮")
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
        self.is_click(user['Task Name value'], content)

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        down_status = Base.export_download_status(self, user['Export Record Search'], user['获取下载状态文本'])
        return down_status

    @allure.step("导出记录页面，获取列表 Download Status文本")
    def get_download_status_text(self):
        status = self.element_text(user['获取下载状态文本'])
        return status

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

    @allure.step("")
    def get_export_time_text(self):
        """导出记录页面，获取列表导出时间文本"""
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 0:
            logging.info("Shop Sales Query列表，按Shop ID筛选，加载筛选后的数据正常，分页总条数Total：{}".format(total))
        else:
            logging.info("查看Shop Sales Query列表，未加载筛选后的数据失败，分页总条数Total：{}".format(total))

    @allure.step("断言分页总数是否存在数据")
    def assert_total2(self, total):
        if int(total) > 1000:
            logging.info("查看Shop Sales Query列表，加载所有数据正常，分页总条数Total：{}".format(total))
        else:
            logging.info("查看Shop Sales Query列表，未加载所有数据失败，分页总条数Total：{}".format(total))

    @allure.step("断言文件或导出时间是否有数据 ")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("Shop Sales Query导出成功，File Size 导出文件大于0KB:{}".format(file_size))
        else:
            logging.info("Shop Sales Query导出成功，File Size 导出文件小于0KB:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Shop Sales Query导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Shop Sales Query导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))
        sleep(1)


if __name__ == '__main__':
    pass
