from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class HomePagePage(Base):
    """HomePagePage类，测试环境，首页HomePage页面元素定位"""

    @allure.step("根据Time Period条件筛选")
    def click_time_period(self):
        self.presence_sleep_dcr(user['Input Time Period'])
        self.is_click(user['Input Time Period'])
        sleep(1)
        self.is_click(user['选择月份'])

    @allure.step("点击Search查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_text(user['Loading'])

    @allure.step("点击Search查询按钮")
    def get_user_mgt_authorization(self):
        """获取 User Management & Authorization卡片文本 """
        user_mgt_authoriza = self.element_text(user['Get User Management Authorization'])
        return user_mgt_authoriza

    @allure.step("获取No Auth Customer WH Shop维度的统计数")
    def get_no_auth_cust_wh_shop(self):
        no_auth_cust_shop = self.element_text(user['Get No Auth Customer WH Shop'])
        if int(no_auth_cust_shop) > 1:
            logging.info("User Management & Authorization卡片，加载No Auth Customer WH Shop指标的值正常：{}".format(no_auth_cust_shop))
        else:
            logging.info("User Management & Authorization卡片，加载No Auth Customer WH Shop指标的值为0：{}".format(no_auth_cust_shop))

    @allure.step("获取Country And Above Authority维度的统计数")
    def get_country_and_above_authority(self):
        country_above_auth = self.element_text(user['Get Country And Above Authority'])
        if int(country_above_auth) > 1:
            logging.info("User Management & Authorization卡片，加载Country And Above Authority指标的值正常：{}".format(country_above_auth))
        else:
            logging.info("User Management & Authorization卡片，加载Country And Above Authority指标的值为0：{}".format(country_above_auth))

    @allure.step("获取Transsion Days No Login维度的统计数")
    def get_trans_days_no_login(self):
        trans_days_no_login = self.element_text(user['Get Transsion Days No Login'])
        if int(trans_days_no_login) > 1:
            logging.info("User Management & Authorization卡片，加载Transsion Days No Login指标的值正常：{}".format(trans_days_no_login))
        else:
            logging.info("User Management & Authorization卡片，加载Transsion Days No Login指标的值为0：{}".format(trans_days_no_login))

    @allure.step("获取No menu维度的统计数")
    def get_no_menu(self):
        trans_no_menu = self.element_text(user['Get No menu'])
        if int(trans_no_menu) > 1:
            logging.info("User Management & Authorization卡片，加载No menu指标的值正常：{}".format(trans_no_menu))
        else:
            logging.info("User Management & Authorization卡片，加载No menu指标的值为0：{}".format(trans_no_menu))

    @allure.step("获取No Auth Customer WH维度的统计数")
    def get_no_auth_cust_wh(self):
        no_auth_cust = self.element_text(user['Get No Auth Customer WH'])
        if int(no_auth_cust) > 1:
            logging.info("User Management & Authorization卡片，加载No Auth Customer WH指标的值正常：{}".format(no_auth_cust))
        else:
            logging.info("User Management & Authorization卡片，加载No Auth Customer WH指标的值为0：{}".format(no_auth_cust))

    @allure.step("获取Customer Days No Login维度的统计数")
    def get_cust_days_no_login(self):
        cust_days_no_login = self.element_text(user['Get Customer Days No Login'])
        if int(cust_days_no_login) > 1:
            logging.info("User Management & Authorization卡片，加载Customer Days No Login指标的值正常：{}".format(cust_days_no_login))
        else:
            logging.info("User Management & Authorization卡片，加载Customer Days No Login指标的值为0：{}".format(cust_days_no_login))

    @allure.step("点击用户管理卡片的 导出 功能")
    def click_user_mgt_export(self):
        self.is_click(user['User Management Export'])
        sleep(3)


    """查看Abnormal Data 指标定位"""
    @allure.step("获取abnormal data 文本内容")
    def get_abnormal_data_text(self):
        self.presence_sleep_dcr(user['Get Abnormal Data'])
        abnormal_text = self.element_text(user['Get Abnormal Data'])
        return abnormal_text

    @allure.step("获取Abnormal Data指标，国包出库单激活日期")
    def get_dist_deli_date(self):
        dist_deli_date = self.element_text(user['Get Dist Delivery Date Activation'])
        if int(dist_deli_date) > 0:
            logging.info("Abnormal Data卡片，加载Distributor Delivery Date指标的值加载正常：{}".format(dist_deli_date))
        else:
            logging.info("Abnormal Data卡片，加载Distributor Delivery Date指标的值加载为0：{}".format(dist_deli_date))

    @allure.step("获取Abnormal Data指标，二代出库单激活日期")
    def get_sub_deal_deli_date(self):
        sub_deal_deli_date = self.element_text(user['Get Subdealer Delivery Activation'])
        if int(sub_deal_deli_date) > 0:
            logging.info("Abnormal Data卡片，加载Sub-dealer Delivery Date指标的值加载正常：{}".format(sub_deal_deli_date))
        else:
            logging.info("Abnormal Data卡片，加载Sub-dealer Delivery Date指标的值加载为0:{}".format(sub_deal_deli_date))

    @allure.step("获取Abnormal Data指标，工厂出库单激活日期")
    def get_factory_deli_date(self):
        factory_deli_date = self.element_text(user['Get Factory Delivery Activation'])
        if int(factory_deli_date) > 0:
            logging.info("Abnormal Data卡片，加载Factory Delivery Date指标的值加载正常：{}".format(factory_deli_date))
        else:
            logging.info("Abnormal Data卡片，加载Factory Delivery Date指标的值加载为0：{}".format(factory_deli_date))

    @allure.step("获取Abnormal Data指标，门店销量激活日期")
    def get_shop_sales_date(self):
        shop_sales_date = self.element_text(user['Get Shop Sales Activation'])
        if int(shop_sales_date) > 0:
            logging.info("Abnormal Data卡片，加载Shop Sales Date指标的值加载正常:{}".format(shop_sales_date))
        else:
            logging.info("Abnormal Data卡片，加载Shop Sales Date指标的值加载为0：{}".format(shop_sales_date))

    @allure.step("获取Abnormal Data指标，门店销量激活日期")
    def get_infiltration_sales_pcs(self):
        infiltration_sales_pcs = self.element_text(user['Get Infiltration Sales PCS'])
        if int(infiltration_sales_pcs) > 0:
            logging.info("Abnormal Data卡片，加载SAP delivery country is different from activation指标的值加载正常：{}".format(infiltration_sales_pcs))
        else:
            logging.info("Abnormal Data卡片，加载SAP delivery country is different from activation指标的值加载不正常：{}".format(infiltration_sales_pcs))

    @allure.step("获取Abnormal Data指标，Infiltration Sales文本内容")
    def get_infiltration_sales_text(self):
        infiltration_sales_text = self.element_text(user['Get Infiltration Sales Text'])
        return infiltration_sales_text

    @allure.step("点击导出Abnormal Data指标数据")
    def click_export_abnormal_data(self):
        self.is_click(user['Abnormal Data Export'])
        sleep(1)



    #HomePage首页，导出功能验证
    @allure.step("点击导出查看more更多按钮")
    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        self.element_text(user['Loading'])

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], content)
        sleep(2)
        self.is_click(user['Task Name value'], content)


    @allure.step("导出记录页面，点击Search按钮")
    def click_export_search(self):
        down_status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
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
        """导出记录页面，获取列表 User ID文本"""
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    @allure.step("导出记录页面，获取列表 Create Date文本")
    def get_create_date_text(self):
        """导出记录页面，获取列表 Create Date文本"""
        self.scroll_into_view(user['获取创建日期文本'])
        create_date = self.element_text(user['获取创建日期文本'])
        create_date1 = create_date[0:10]
        return create_date1

    @allure.step("导出记录页面，获取列表Complete Date文本")
    def get_complete_date_text(self):
        """导出记录页面，获取列表Complete Date文本"""
        complete_date = self.element_text(user['获取完成日期文本'])
        complete_date1 = complete_date[0:10]
        return complete_date1

    @allure.step("导出记录页面，获取列表 Operation文本")
    def get_export_operation_text(self):
        sleep(1)
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("关闭导出记录菜单页面")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])

    @allure.step("关闭用户管理菜单页面")
    def click_close_user_management(self):
        self.is_click(user['关闭用户管理菜单'])


    """查询Sub-dealer Management 指标数据"""
    @allure.step("获取Sub-dealer Management文本内容")
    def get_sub_dealer_management(self):
        sub_dealer = self.element_text(user['Get Sub dealer Management'])
        return sub_dealer

    @allure.step("获取Total Sub dealer指标值内容")
    def get_total_sub_dealer_value(self):
        total_sub_dealer = self.element_text(user['Get Total Sub dealer'])
        if int(total_sub_dealer) > 0:
            logging.info("Sub-dealer Management卡片，加载Total Sub dealer指标的值加载正常：{}".format(total_sub_dealer))
        else:
            logging.info("Sub-dealer Management卡片，加载Total Sub dealer指标的值加载为0：{}".format(total_sub_dealer))

    @allure.step("获取Number of rebated user指标值内容")
    def get_number_of_rebated_user(self):
        number_of_rebated = self.element_text(user['Get Number of rebated user'])
        if int(number_of_rebated) > 0:
            logging.info("Sub-dealer Management卡片，加载Number of rebated user指标的值加载正常：{}".format(number_of_rebated))
        else:
            logging.info("Sub-dealer Management卡片，加载Number of rebated user指标的值加载为0：{}".format(number_of_rebated))

    @allure.step("获取Days No Stock In Out指标值内容")
    def get_days_no_stock_in_out(self):
        days_no_stock_in = self.element_text(user['Get Days No Stock In Out'])
        if int(days_no_stock_in) > 0:
            logging.info("Sub-dealer Management卡片，加载Days No Stock In Out指标的值加载正常：{}".format(days_no_stock_in))
        else:
            logging.info("Sub-dealer Management卡片，加载Days No Stock In Out指标的值加载为0：{}".format(days_no_stock_in))

    @allure.step("获取No Permission Seller Buyer指标值内容")
    def get_no_permission_seller_buyer(self):
        no_permission = self.element_text(user['Get No Permission Seller Buyer'])
        if int(no_permission) > 0:
            logging.info("Sub-dealer Management卡片，加载No Permission Seller Buyer指标的值加载正常：{}".format(no_permission))
        else:
            logging.info("Sub-dealer Management卡片，加载No Permission Seller Buyer指标的值加载为0：{}".format(no_permission))


    @allure.step("点击Sub dealer Management导出功能")
    def click_sub_dealer_export(self):
        export = self.is_click(user['Sub dealer Management Export'])
        return export

    @allure.step("点击关闭 Customer Management global菜单")
    def click_close_customer_mgt(self):
        self.is_click(user['关闭客户管理菜单'])



    """Distributor Management 指标数据"""
    @allure.step("获取Distributor Management文本内容")
    def get_distributor_management(self):
        distributor = self.element_text(user['Get Distributor Management'])
        return distributor

    @allure.step("获取Total Distributor 指标值")
    def get_total_distributor(self):
        total_dist = self.element_text(user['Get Total Distributor'])
        if int(total_dist) > 0:
            logging.info("Distributor Management卡片，加载Total Distributor指标的值加载正常：{}".format(total_dist))
        else:
            logging.info("Distributor Management卡片，加载Total Distributor指标的值加载为0：{}".format(total_dist))
        sleep(0.5)

    @allure.step("获取Dist Number of rebated user指标值")
    def get_dist_number_of_rebated_user(self):
        dist_number_of_rebated = self.element_text(user['Get Dist Number of rebated user'])
        if int(dist_number_of_rebated) > 0:
            logging.info("Distributor Management卡片，加载Number of rebated user指标的值加载正常：{}".format(dist_number_of_rebated))
        else:
            logging.info("Distributor Management卡片，加载Number of rebated user指标的值加载为0：{}".format(dist_number_of_rebated))
        sleep(0.5)

    @allure.step("获取Dist Days No Stock in Out指标值")
    def get_dist_days_no_stock_in_out(self):
        dist_days_no_stock = self.element_text(user['Get Dist Days No Stock in Out'])
        if int(dist_days_no_stock) > 0:
            logging.info("Distributor Management卡片，加载Days No Stock in Out指标的值加载正常：{}".format(dist_days_no_stock))
        else:
            logging.info("Distributor Management卡片，加载Days No Stock in Out指标的值加载为0：{}".format(dist_days_no_stock))
        sleep(0.5)

    @allure.step("获取Dist No Permission Buyer指标值")
    def get_dist_no_permission_buyer(self):
        dist_no_permission = self.element_text(user['Get Dist No Permission Buyer'])
        if int(dist_no_permission) > 0:
            logging.info("Distributor Management卡片，加载No Permission Buyer指标的值加载正常：{}".format(dist_no_permission))
        else:
            logging.info("Distributor Management卡片，加载No Permission Buyer指标的值加载为0：{}".format(dist_no_permission))
        sleep(0.5)

    @allure.step("点击Distributor Management 指标的 Export导出功能")
    def click_distributor_export(self):
        self.is_click(user['Distributor Management Export'])


    """Shop Management 指标定位"""
    @allure.step("获取Shop Management文本内容")
    def get_shop_management_text(self):
        shop_mgt = self.element_text(user['Get Shop Management'])
        return shop_mgt

    @allure.step("获取Total Shop指标值")
    def get_total_shop(self):
        total_shop = self.element_text(user['Get Total Shop'])
        if int(total_shop) > 0:
            logging.info("Shop Management卡片，加载Total Shop指标的值加载正常：{}".format(total_shop))
        else:
            logging.info("Shop Management卡片，加载Total Shop指标的值加载为0：{}".format(total_shop))


    @allure.step("获取Shop Number of rebated user指标值")
    def get_shop_number_of_rebated_user(self):
        shop_number = self.element_text(user['Get Shop Number of rebated user'])
        if int(shop_number) > 0:
            logging.info("Shop Management卡片，加载Number of rebated user指标的值加载正常：{}".format(shop_number))
        else:
            logging.info("Shop Management卡片，加载Number of rebated user指标的值加载为0：{}".format(shop_number))
        sleep(0.5)

    @allure.step("获取Total Shop指标值")
    def get_shop_days_no_upload_sales(self):
        self.presence_sleep_dcr(user['Get Shop Days No Upload Sales'])
        shop_days_no_upload = self.element_text(user['Get Shop Days No Upload Sales'])
        if int(shop_days_no_upload) > 0:
            logging.info("Shop Management卡片，加载Days No Upload Sales指标的值加载正常：{}".format(shop_days_no_upload))
        else:
            logging.info("Shop Management卡片，加载Days No Upload Sales指标的值加载为0：{}".format(shop_days_no_upload))
        sleep(0.5)

    @allure.step("点击Shop Management Export导出按钮")
    def click_shop_export(self):
        self.is_click(user['Shop Management Export'])
        sleep(1)

    @allure.step("关闭Shop Management global菜单")
    def click_close_shop_mgt(self):
        self.is_click(user['关闭门店管理菜单'])


    @allure.step("断言文件下载时长")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("User Management & Authorization卡片数据导出成功，File Size 导出文件大于M:{}".format(file_size))
        else:
            logging.info("User Management & Authorization卡片数据导出失败，File Size 导出时间小于M:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("User Management & Authorization卡片数据导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("User Management & Authorization卡片数据导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))


if __name__ == '__main__':
    pass








