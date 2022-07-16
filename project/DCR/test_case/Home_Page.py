from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert
from project.DCR.page_object.Home_Page import HomePagePage
import logging
from libs.common.time_ui import sleep
import datetime
import pytest
import allure


@allure.feature("Home Page")
class TestQueryUserMgtCard:
    @allure.story("查询")
    @allure.title("查看Homepage首页，User Management& Authorization卡片维度数据")
    @allure.description("查看Homepage首页，User Management& Authorization卡片的各维度数据")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Home Page")

        page_user_mgt = HomePagePage(drivers)
        page_user_mgt.click_time_period()
        page_user_mgt.click_search()
        user_mgt_card = page_user_mgt.get_user_mgt_authorization()
        ValueAssert.value_assert_equal(user_mgt_card, "User Management & Authorization")

        no_auth_cust_shop = page_user_mgt.get_no_auth_cust_wh_shop()
        if int(no_auth_cust_shop) > 1:
            logging.info("User Management & Authorization卡片，加载No Auth Customer WH Shop指标的值正常：{}".format(no_auth_cust_shop))
        else:
            logging.info("User Management & Authorization卡片，加载No Auth Customer WH Shop指标的值不正常：{}".format(no_auth_cust_shop))

        country_above_auth = page_user_mgt.get_country_and_above_authority()
        if int(country_above_auth) > 1:
            logging.info("User Management & Authorization卡片，加载Country And Above Authority指标的值正常：{}".format(country_above_auth))
        else:
            logging.info("User Management & Authorization卡片，加载Country And Above Authority指标的值不正常：{}".format(country_above_auth))

        trans_day_no_login = page_user_mgt.get_trans_days_no_login()
        if int(trans_day_no_login) > 1:
            logging.info("User Management & Authorization卡片，加载Transsion Days No Login指标的值正常：{}".format(trans_day_no_login))
        else:
            logging.info("User Management & Authorization卡片，加载Transsion Days No Login指标的值不正常：{}".format(trans_day_no_login))

        no_menu = page_user_mgt.get_no_menu()
        if int(no_menu) > 1:
            logging.info("User Management & Authorization卡片，加载No menu指标的值正常：{}".format(no_menu))
        else:
            logging.info("User Management & Authorization卡片，加载No menu指标的值不正常：{}".format(no_menu))

        no_auth_cust = page_user_mgt.get_no_auth_cust_wh()
        if int(no_auth_cust) > 1:
            logging.info("User Management & Authorization卡片，加载No Auth Customer WH指标的值正常：{}".format(no_auth_cust))
        else:
            logging.info("User Management & Authorization卡片，加载No Auth Customer WH指标的值不正常：{}".format(no_auth_cust))

        cust_day_no_login = page_user_mgt.get_cust_days_no_login()
        if int(cust_day_no_login) > 1:
            logging.info("User Management & Authorization卡片，加载Customer Days No Login指标的值正常：{}".format(cust_day_no_login))
        else:
            logging.info("User Management & Authorization卡片，加载Customer Days No Login指标的值不正常：{}".format(cust_day_no_login))
        page_user_mgt.click_close_export_record()
        page_user_mgt.click_close_user_management()


@allure.feature("首页")
class TestExportUserMgtCard:
    @allure.story("导出")
    @allure.title("Homepage首页，导出User Management& Authorization卡片维度数据")
    @allure.description("Homepage首页的，导出User Management& Authorization卡片的各维度数据")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        export = HomePagePage(drivers)
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        export.click_user_mgt_export()
        export.click_download_icon()
        export.click_more()
        down_status = export.click_export_search()

        #down_status = export.get_download_status_text()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()

        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        create_date1 = create_date[0:10]
        complete_date = export.get_complete_date_text()
        complete_date1 = complete_date[0:10]
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "User management")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date1, today)
        ValueAssert.value_assert_equal(complete_date1, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)


@allure.feature("Home Page")
class TestQueryAbnormalDataCard:
    @allure.story("查询")
    @allure.title("Homepage首页，查询Abnormal Data卡片维度数据")
    @allure.description("Homepage首页，查询Abnormal Data卡片的各维度数据")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_003_001(self, drivers):
        abnormal = HomePagePage(drivers)
        abnormal_text = abnormal.get_abnormal_data_text()
        infiltration_sale_text = abnormal.get_infiltration_sales_text()

        ValueAssert.value_assert_equal("Abnormal Data", abnormal_text)
        ValueAssert.value_assert_In("Infiltration Sales", infiltration_sale_text)

        dist_deli_pcs = abnormal.get_dist_deli_date()
        if int(dist_deli_pcs) > 0:
            logging.info("Abnormal Data卡片，加载Distributor Delivery Date指标的值加载正常：{}".format(dist_deli_pcs))
        else:
            logging.info("Abnormal Data卡片，加载Distributor Delivery Date指标的值加载不正常：{}".format(dist_deli_pcs))

        sub_deal_deli_pcs = abnormal.get_sub_deal_deli_date()
        if int(sub_deal_deli_pcs) > 0:
            logging.info("Abnormal Data卡片，加载Sub-dealer Delivery Date指标的值加载正常：{}".format(sub_deal_deli_pcs))
        else:
            logging.info("Abnormal Data卡片，加载Sub-dealer Delivery Date指标的值加载不正常:{}".format(sub_deal_deli_pcs))

        factory_deli_pcs = abnormal.get_factory_deli_date()
        if int(factory_deli_pcs) > 0:
                logging.info("Abnormal Data卡片，加载Factory Delivery Date指标的值加载正常：{}".format(factory_deli_pcs))
        else:
                logging.info("Abnormal Data卡片，加载Factory Delivery Date指标的值加载不正常：{}".format(factory_deli_pcs))

        shop_sale_pcs = abnormal.get_shop_sales_date()
        if int(shop_sale_pcs) > 0:
            logging.info("Abnormal Data卡片，加载Shop Sales Date指标的值加载正常:{}".format(shop_sale_pcs))
        else:
            logging.info("Abnormal Data卡片，加载Shop Sales Date指标的值加载不正常：{}".format(shop_sale_pcs))

        infiltration_sale_pcs = abnormal.get_infiltration_sales_pcs()
        if int(infiltration_sale_pcs) > 0:
            logging.info("Abnormal Data卡片，加载SAP delivery country is different from activation指标的值加载正常：{}".format(infiltration_sale_pcs))
        else:
            logging.info("Abnormal Data卡片，加载SAP delivery country is different from activation指标的值加载不正常：{}".format(infiltration_sale_pcs))



if __name__ == '__main__':
    pytest.main(['Home_Page.py'])