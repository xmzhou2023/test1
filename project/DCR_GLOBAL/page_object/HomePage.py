from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class HomePagePage(Base):
    """HomePagePage类，测试环境，首页HomePage页面元素定位"""

    def click_time_period(self):
        """根据Time Period条件筛选"""
        self.is_click(user['Input Time Period'])
        sleep(1)
        self.is_click(user['选择月份'])

    def click_search(self):
        """点击Search查询按钮"""
        self.is_click(user['Search'])

    def get_user_mgt_authorization(self):
        """获取 User Management & Authorization卡片文本 """
        user_mgt_authoriza = self.element_text(user['Get User Management Authorization'])
        return user_mgt_authoriza

    def get_no_auth_cust_wh_shop(self):
        """获取No Auth Customer WH Shop维度的统计数"""
        no_auth_cust_shop = self.element_text(user['Get No Auth Customer WH Shop'])
        return no_auth_cust_shop

    def get_country_and_above_authority(self):
        """获取Country And Above Authority维度的统计数"""
        country_above_authority = self.element_text(user['Get Country And Above Authority'])
        return country_above_authority

    def get_trans_days_no_login(self):
        """获取Transsion Days No Login维度的统计数"""
        trans_days_no_login = self.element_text(user['Get Transsion Days No Login'])
        return trans_days_no_login

    def get_no_menu(self):
        """获取No menu维度的统计数"""
        trans_no_menu = self.element_text(user['Get No menu'])
        return trans_no_menu

    def get_no_auth_cust_wh(self):
        """获取No Auth Customer WH维度的统计数"""
        trans_days_no_login = self.element_text(user['Get No Auth Customer WH'])
        return trans_days_no_login

    def get_cust_days_no_login(self):
        """获取Customer Days No Login维度的统计数"""
        cust_days_no_login = self.element_text(user['Get Customer Days No Login'])
        return cust_days_no_login

    def click_user_mgt_export(self):
        """点击用户管理卡片的"导出"功能"""
        self.is_click(user['User Management Export'])
        sleep(2)



    """ #查看Abnormal Data 指标定位 """
    def get_abnormal_data_text(self):
        """ 获取abnormal data 文本内容 """
        abnormal_text = self.element_text(user['Get Abnormal Data'])
        return abnormal_text

    def get_start_end_date(self):
        """ 获取Abnormal Data指标，开始与结束日期文本 """
        start_end_data = self.element_text(user['Get start and end Data'])
        return start_end_data

    def get_dist_deli_date(self):
        """ 获取Abnormal Data指标，国包出库单激活日期  """
        dist_deli_date = self.element_text(user['Dist Delivery Date Activation'])
        return dist_deli_date

    def get_sub_deal_deli_date(self):
        """ 获取Abnormal Data指标，二代出库单激活日期  """
        sub_deal_deli_date = self.element_text(user['Get Subdealer Delivery Activation'])
        return sub_deal_deli_date

    def get_factory_deli_date(self):
        """ 获取Abnormal Data指标，工厂出库单激活日期 """
        factory_deli_date = self.element_text(user['Get Factory Delivery Activation'])
        return factory_deli_date

    def get_shop_sales_date(self):
        """ 获取Abnormal Data指标，门店销量激活日期 """
        shop_sales_date = self.element_text(user['Get Shop Sales Activation'])
        return shop_sales_date

    def get_infiltration_sales_pcs(self):
        """ 获取Abnormal Data指标，门店销量激活日期 """
        infiltration_sales_pcs = self.element_text(user['Get Infiltration Sales PCS'])
        return infiltration_sales_pcs

    def get_infiltration_sales_text(self):
        """ 获取Abnormal Data指标，门店销量激活日期 """
        infiltration_sales_text = self.element_text(user['Get Infiltration Sales Text'])
        return infiltration_sales_text

    def click_export_abnormal_data(self):
        """ 点击导出 Abnormal Data指标数据"""
        self.is_click(user['Abnormal Data Export'])




    #HomePage首页，导出功能验证
    def click_download_icon(self):
        """点击导出查看更多图标"""
        self.is_click(user['Download Icon'])
        sleep(2)

    def click_more(self):
        """页面点击more按钮"""
        self.is_click(user['More'])
        sleep(3)

    def click_export_search(self):
        """导出记录页面，点击Search按钮"""
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

    def get_user_id_text(self):
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

    def click_close_export_record(self):
        """ 关闭导出记录菜单页面"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    def click_close_user_management(self):
        """ 关闭用户管理菜单页面"""
        self.is_click(user['关闭用户管理菜单'])
        sleep(1)


if __name__ == '__main__':
    pass








