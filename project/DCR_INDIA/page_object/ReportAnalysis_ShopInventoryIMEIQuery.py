from libs.common.read_element import Element
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class ShopInventoryIMEIQueryPage(Base):
    """ShopInventoryIMEIQueryPage，生产环境，Shop Inventory IMEI Query 页面元素定位"""
    def click_unfold(self):
        """Shop Inventory IMEI Query页面，点击Unfold展开筛选条件"""
        self.is_click(user['Unfold'])
        sleep(2)

    def input_shop_id(self, content):
        """Shop Inventory IMEI Query页面，输入shop ID，进行筛选"""
        self.is_click_dcr(user['筛选门店'])
        sleep(1)
        self.input_text_dcr(user['筛选门店'], txt=content)
        sleep(3)
        self.is_click_dcr(user['选中筛选门店值'])

    def input_inbound_date(self, content):
        """Shop Inventory IMEI Query页面，输入筛选开始日期"""
        self.is_click(user['Inbound Date Start Time'])
        sleep(1)
        self.input_text(user['Inbound Date Start Time'], txt=content)

    def click_search(self):
        """Shop Inventory IMEI Query页面，点击Search按钮"""
        self.is_click(user['Search'])
        sleep(8)

    def click_reset(self):
        """Shop Inventory IMEI Query页面，点击Search按钮"""
        self.is_click(user['Reset'])
        sleep(7.5)

    def click_fold(self):
        """Shop Inventory IMEI Query页面，点击Fold收起筛选条件按钮"""
        self.is_click(user['Fold'])
        sleep(1)

    def get_total_text(self):
        """Shop Inventory IMEI Query页面，获取分页功能总条数文本"""
        total = self.element_text(user['获取总条数文本'])
        return total

    def get_shop_id_text(self):
        """Shop Inventory IMEI Query页面，获取列表Shop ID文本"""
        shop_id = self.element_text(user['获取Shop ID文本'])
        return shop_id

    def get_shop_name_text(self):
        shop_name = self.element_text(user['获取Shop Name文本'])
        return shop_name

    def get_brand_text(self):
        brand = self.element_text(user['获取Brand文本'])
        return brand

    def get_series_text(self):
        series = self.element_text(user['获取Series文本'])
        return series

    def get_model_text(self):
        model = self.element_text(user['获取Model文本'])
        return model

    def click_export(self):
        self.is_click(user['Export'])
        sleep(1)

    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    def click_close_shop_inventory_imei(self):
        """关闭门店库存IMEI菜单"""
        self.is_click(user['关闭门店库存IMEI菜单'])
        sleep(1)



    # 门店库存IMEI查询记录，导出功能验证
    def click_export(self):
        """Visit Record页面，点击Export导出按钮"""
        self.is_click(user['Export'])

    def click_download_icon(self):
        self.is_click(user['Download Icon'])
        sleep(2.5)

    def click_more(self):
        self.is_click(user['More'])
        sleep(3.5)

    def click_export_search(self):
        self.is_click(user['Export Record Search'])
        sleep(2)

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

    def click_close_shop_inventory_imei(self):
        self.is_click(user['关闭门店库存IMEI菜单'])



if __name__ == '__main__':
    pass