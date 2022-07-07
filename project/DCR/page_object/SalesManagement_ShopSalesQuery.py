from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class ShopSaleQueryPage(Base):
    """ShopSalesQueryPage，生产环境，Shop Sales Query页面元素定位"""
    def input_query_shop_id(self, content):
        """Shop Sales Query页面，根据Shop ID条件筛选 门店销售数据"""
        self.is_click_dcr(user['筛选门店'])
        self.input_text_dcr(user['筛选门店'], txt=content)
        sleep(3)
        self.is_click(user['Select Shop Value'])

    def click_unfold(self):
        """点击Unfold展开筛选项按钮"""
        self.is_click(user['Unfold'])
        sleep(1)

    def click_fold(self):
        """ 点击fold收起筛选项按钮 """
        self.is_click(user['Fold'])
        sleep(1)

    def input_upload_start_date(self, content):
        """ 输入Upload Date筛选项的开始时间 """
        self.is_click(user['Input Upload Start Date'])
        self.input_text(user['Input Upload Start Date'], txt=content)

    def input_sales_date(self, content1, content2):
        self.is_click(user['Sales Date Start Date'])
        self.input_text(user['Sales Date Start Date'], txt=content1)
        self.is_click(user['Sales Date End Date'])
        self.input_text(user['Sales Date End Date'], txt=content2)


    def click_search(self):
        """Shop Sales Query页面，筛选Shop ID后，点击Search按钮"""
        self.is_click_dcr(user['Search'])
        sleep(5)

    def click_reset(self):
        """Shop Sales Query页面，筛选Shop ID后，点击Search按钮"""
        self.is_click(user['Reset'])
        sleep(6)

    def get_shop_id_text(self):
        """Shop Sales Query页面，获取列表Shop ID 文本内容"""
        shop_id = self.element_text(user['获取门店ID文本'])
        return shop_id

    def get_shop_name_text(self):
        """Shop Sales Query页面，获取列表Shop ID 文本内容"""
        shop_name = self.element_text(user['获取门店名称文本'])
        return shop_name

    def get_status_text(self):
        """Shop Sales Query页面，获取列表Status文本内容"""
        status = self.element_text(user['获取状态文本'])
        return status

    def get_sales_date_text(self):
        """Shop Sales Query页面，获取列表Status文本内容"""
        sales_date = self.element_text(user['获取销售日期文本'])
        return sales_date

    def get_public_id_text(self):
        """Shop Sales Query页面，获取列表Status文本内容"""
        public_id = self.element_text(user['获取Public ID文本'])
        return public_id

    def get_total_text(self):
        """Shop Sales Query页面，获取列表Status文本内容"""
        total = self.element_text(user['获取总条数文本'])
        return total

    def click_export(self):
        """Shop Sales Query页面，点击Export 导出门店销量查询数据"""
        self.is_click(user['Export'])

    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    def click_close_shop_sales_query(self):
        """ 关闭门店销售查询菜单 """
        self.is_click(user['关闭门店销售查询菜单'])
        sleep(1)



    #门店销售查询，导出功能验证
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
