from project.DCR.page_object.SalesManagement_ShopSalesQuery import ShopSaleQueryPage
import logging
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base,random_list
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
import datetime
import pytest
import allure
import random

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_shop_sale_fixture(drivers):
    yield
    close = ShopSaleQueryPage(drivers)
    close.click_close_shop_sales_query()

@pytest.fixture(scope='function')
def function_export_fixture(drivers):
    yield
    close = ShopSaleQueryPage(drivers)
    close.click_close_export_record()
    close.click_close_shop_sales_query()

@allure.feature("销售管理-门店销售查询")
class TestShopSalesQuery:
    @allure.story("查询门店销量")
    @allure.title("门店销售查询页面，查询门店销售查询列表数据加载")
    @allure.description("考勤记录页面，查询门店销售查询列表数据加载，断言数据加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_shop_sale_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开销售管理-打开门店销售查询页面"""
        user.click_gotomenu("Sales Management", "Shop Sales Query")

        """查看Shop Sales Query门店销量上报 列表数据加载是否正常"""
        shop_sales = ShopSaleQueryPage(drivers)
        shop_sales.input_upload_start_date("2022-11-01")
        shop_sales.click_search()

        shop_id = shop_sales.get_shop_id_text()
        shop_name = shop_sales.get_shop_name_text()
        status = shop_sales.get_status_text()
        sales_date = shop_sales.get_sales_date_text()
        public_id = shop_sales.get_public_id_text()
        total = shop_sales.get_total_text()

        """Shop Sales Query页面，增加断言 对比列表字段与分页总条数是否有数据"""
        ValueAssert.value_assert_IsNoneNot(shop_id)
        ValueAssert.value_assert_IsNoneNot(status)
        ValueAssert.value_assert_IsNoneNot(shop_name)
        ValueAssert.value_assert_IsNoneNot(sales_date)
        ValueAssert.value_assert_IsNoneNot(public_id)
        shop_sales.assert_total2(total)
        #shop_sales.click_close_shop_sales_query()

    @allure.story("查询门店销量1")
    @allure.title("门店销售查询页面，查询门店销售查询列表，查询结果和条件一致")
    @allure.description("门店销售查询页面，查询门店销售查询列表数据加载，断言数据加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_shop_sale_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开销售管理-打开门店销售查询页面"""
        user.click_gotomenu("Sales Management", "Shop Sales Query")
        page = ShopSaleQueryPage(drivers)
        page.click_unfold()

        """查看Shop Sales Query按shopID查询"""
        page.input_upload_date("2022-12-01","2022-12-06")
        page.input_query_shop_id('BD026690')
        page.click_search()
        result=page.get_table_txt(2)
        ValueAssert.value_assert_equal('BD026690',result)
        page.click_reset()

        """查看Shop Sales Query按销量状态查询"""
        page.input_upload_date('2022-10-01', '2022-10-30')
        page.input_status('Deleted')
        page.click_search()
        col_num = page.get_table_column('Status')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('Deleted', result_date)
        page.click_reset()

        """查看Shop Sales Query按sales date查询"""
        page.input_upload_date("2022-10-01", "2022-10-30")
        page.input_sales_date("2022-06-23","2022-06-23")
        page.click_search()
        col_num = page.get_table_column('Sales Date')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('2022-06-23', result_date)
        page.click_reset()

        """查看Shop Sales Query按Manpower Type查询"""
        page.input_upload_date('2022-10-01', '2022-10-30')
        page.input_manpower('Manned')
        page.click_search()
        col_num = page.get_table_column('Manpower Type')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_In('Manned', result_date)
        page.click_reset()

        """查看Shop Sales Query按Image Type查询"""
        page.input_upload_date('2022-10-01', '2022-10-30')
        page.input_image_type('Zone Shop')
        page.click_search()
        col_num = page.get_table_column('Image Type')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('Zone Shop', result_date)
        page.click_reset()

        """查看Shop Sales Query按Brand查询"""
        page.input_upload_date("2022-10-01", "2022-10-30")
        page.input_brand('TECNO')
        page.click_search()
        col_num = page.get_table_column('Brand')
        result_date = page.get_table_content(col_num)
        ValueAssert.value_assert_equal('TECNO', result_date)
        page.click_reset()

        """查看Shop Sales Query按 Series查询"""
        page.input_upload_date("2022-10-01", "2022-10-30")
        page.input_series('SPARK')
        page.click_imei()
        page.click_search()
        col_num = page.get_table_column('Series')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('SPARK', result_date)
        page.click_reset()

        """查看Shop Sales Query按SP/FP查询"""
        page.input_upload_date("2022-10-01", "2022-10-30")
        page.input_sp_fp('Smart')
        page.click_search()
        col_num = page.get_table_column('SP/FP')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('Smart', result_date)
        page.click_reset()

        """查看Shop Sales Query按model查询"""
        page.input_upload_date("2022-12-01","2022-12-06")
        page.input_model('P701')
        page.click_search()
        col_num = page.get_table_column('Model')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('P701', result_date)
        page.click_reset()

        """查看Shop Sales Query按model type查询"""
        page.input_upload_date("2022-11-01","2022-12-10")
        page.input_model_type('High-Ends')
        page.click_search()
        col_num = page.get_table_column('Model Type')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('High-Ends', result_date)
        page.click_reset()

        """查看Shop Sales Query按项目查询"""
        page.input_upload_date("2022-10-01","2022-10-30")
        page.input_item('KE5 32+2')
        page.click_search()
        col_num = page.get_table_column('Item')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('KE5 32+2', result_date)
        page.click_reset()

        """查看Shop Sales Query按Market Name查询"""
        page.input_upload_date("2022-10-01", "2022-10-30")
        page.input_market_name('SPARK 7')
        page.click_search()
        col_num = page.get_table_column('Market Name')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('SPARK 7', result_date)
        page.click_reset()

        """查看Shop Sales Query按IMEI查询"""
        page.input_upload_date("2022-09-01","2022-09-30")
        page.input_imei('353045312677832')
        page.click_search()
        col_num = page.get_table_column('IMEI/SN')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('353045312677832', result_date)
        page.click_reset()

        """查看Shop Sales Query按Activation Status查询"""
        page.input_upload_date("2022-10-01", "2022-10-30")
        page.input_activation_status('Not Activated')
        page.click_search()
        col_num = page.get_table_column('Activation Status')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('Not Activated', result_date)
        page.click_reset()

    @allure.story("查询门店销量2")
    @allure.title("门店销售查询页面，查询门店销售查询列表，查询结果和条件一致")
    @allure.description("门店销售查询页面，查询门店销售查询列表数据加载，断言数据加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_shop_sale_fixture')
    def test_001_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开销售管理-打开门店销售查询页面"""
        user.click_gotomenu("Sales Management", "Shop Sales Query")
        page = ShopSaleQueryPage(drivers)
        page.click_unfold()

        """查看Shop Sales Query按Activation Country查询"""
        page.input_upload_date('2022-10-01', '2022-10-30')
        page.input_activation_country('Bangladesh')
        page.click_imei()
        page.click_search()
        col_num = page.get_table_column('Activation Country')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('Bangladesh', result_date)
        page.click_reset()

        """查看Shop Sales Query按Activation Date查询"""
        page.input_upload_date('2022-10-01', '2022-10-30')
        page.input_activattion_date('2022-09-06', '2022-09-06')
        page.click_search()
        col_num = page.get_table_column('Activation Date')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('2022-09-06', result_date)
        page.click_reset()

        """查看Shop Sales Query按Delivery Country查询"""
        page.input_upload_date('2022-10-01', '2022-10-30')
        page.input_delivery_country('Bangladesh')
        page.click_search()
        col_num = page.get_table_column('Delivery Country')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('Bangladesh', result_date)
        page.click_reset()

        """查看Shop Sales Query按销量达成查询"""
        page.input_upload_date('2022-10-01', '2022-10-30')
        page.input_achieve_ornot('Yes')
        page.click_search()
        col_num = page.get_table_column('Achieve or Not')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('Yes', result_date)
        page.click_reset()

        """查看Shop Sales Query按Country查询"""
        page.input_upload_date('2022-10-01', '2022-10-30')
        page.input_sale_country('Bangladesh')
        page.click_imei()
        page.click_search()
        col_num = page.get_table_column('Country')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('Bangladesh', result_date)
        page.click_reset()

        """查看Shop Sales Query按城市级别查询"""
        page.input_upload_date("2022-10-01", "2022-10-30")
        page.input_city_tier('T1')
        page.click_search()
        col_num = page.get_table_column('City Tier')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('T1', result_date)
        page.click_reset()

        """查看Shop Sales Query按销售区域查询"""
        page.input_upload_date("2022-12-01","2022-12-06")
        page.input_sales_region('Bangladesh')
        page.click_search()
        col_num = page.get_table_column('Sales Region 2')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('Bangladesh', result_date)
        page.click_reset()

        """查看Shop Sales Query按Uploader ID查询"""
        page.input_upload_date("2022-10-01", "2022-10-30")
        page.input_uploaderid('qiulian1')
        page.click_search()
        col_num = page.get_table_column('Uploader ID')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('qiulian1', result_date)
        page.click_reset()

        """查看Shop Sales Query按Position查询"""
        page.input_upload_date("2022-10-01", "2022-10-30")
        page.input_position('CJP督导')
        page.click_search()
        col_num = page.get_table_column('Position')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('CJP督导', result_date)
        page.click_reset()

        """查看Shop Sales Query按Upload Type查询"""
        page.input_upload_date('2022-10-01', '2022-10-30')
        page.input_upload_type('App Input')
        page.click_search()
        col_num = page.get_table_column('Upload Type')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('App Input', result_date)
        page.click_reset()

        """查看Shop Sales Query按Supplier查询"""
        page.input_upload_date('2022-08-01', '2022-08-30')
        page.input_supplier('PK100039')
        page.click_search()
        col_num = page.get_table_column('Supplier ID')
        result_date=page.get_table_content(col_num)
        ValueAssert.value_assert_equal('PK100039', result_date)
        page.click_reset()


    @allure.story("随机查询门店销量")
    @allure.title("门店销售查询页面，随机组合查询条件，查询门店销售查询列表，查询结果和条件一致")
    @allure.description("门店销售查询页面，随机组合查询条件，查询门店销售查询列表数据加载，断言数据加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_shop_sale_fixture')
    def test_001_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开销售管理-打开门店销售查询页面"""
        user.click_gotomenu("Sales Management", "Shop Sales Query")
        page = ShopSaleQueryPage(drivers)
        page.click_unfold()

        """查看Shop Sales Query按Supplier查询"""
        page.input_upload_date('2022-01-01', '2022-10-30')
        #列表顺序要和表格顶部字段顺序一致
        list_query=['shopid','status','saledate','ManpowerType','ImageType','Brand','Series','SP/FP','Model','ModelType','Item','MarketName','IMEI/SN','ActivationStatus','ActivationCountry','ActivationDate','DeliveryCountry','AchieveorNot','Country','CityTier','SalesRegion2','UploaderID','Position','UploadType','SupplierID']
        num=random.randint(3,8)
        list_random=random_list(list_query,num)
        logging.info('the query condition is %s'%list_random)
        for i in list_random:
            if i == 'shopid':
                page.input_query_shop_id('SD123329')
            elif i == 'status':
                page.input_status('Committed')
            elif i == 'saledate':
                page.input_sales_date('2022-09-21', '2022-09-30')
            elif i == 'ManpowerType':
                page.input_manpower('Manned-Flexi')
            elif i == 'ImageType':
                page.input_image_type('Zone Shop')
            elif i == 'Brand':
                page.input_brand('TECNO')
            elif i == 'Series':
                page.input_series('SPARK')
                page.click_imei()
            elif i == 'SP/FP':
                page.input_sp_fp('Smart')
            elif i == 'Model':
                page.input_model('KG6')
            elif i == 'ModelType':
                page.input_model_type('Mid-Ends')
                page.click_imei()
            elif i == 'Item':
                page.input_item('KG6 64+2')
                page.click_imei()
            elif i == 'MarketName':
                page.input_market_name('SPARK 8')
                page.click_imei()
            elif i == 'IMEI/SN':
                page.input_imei('350100248561825')
            elif i == 'ActivationStatus':
                page.input_activation_status('Activated')
            elif i == 'ActivationCountry':
               page.input_activation_country('Gabon')
               page.click_imei()
            elif i == 'ActivationDate':
                page.input_activattion_date('2022-01-01', '2022-01-24')
            elif i == 'DeliveryCountry':
                page.input_delivery_country('United Arab Emirates')
            elif i == 'AchieveorNot':
                page.input_achieve_ornot('No')
            elif i == 'Country':
                page.input_sale_country('DB3')
            elif i == 'CityTier':
                page.input_city_tier('T1')
            elif i == 'SalesRegion2':
                page.input_sales_region('DB3')
            elif i == 'UploaderID':
                page.input_uploaderid('qiulian1')
            elif i == 'Position':
                page.input_position('二期督导')
                page.click_imei()
            elif i == 'UploadType':
                page.input_upload_type('App Scan')
            else:
                page.input_supplier('PK100039')

        page.click_search()

        for i in list_random:
            if i == 'shopid':
                col_num = page.get_table_column('Shop ID')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('SD123329', result_date)
            elif i == 'status':
                col_num = page.get_table_column('Status')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('Deleted', result_date)
            elif i == 'saledate':
                col_num = page.get_table_column('Sales Date')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('2022-09-27', result_date)
            elif i == 'ManpowerType':
                col_num = page.get_table_column('Manpower Type')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('Manned-Flexi', result_date)
            elif i == 'ImageType':
                col_num = page.get_table_column('Image Type')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('Zone Shop', result_date)
            elif i == 'Brand':
                col_num = page.get_table_column('Brand')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('TECNO', result_date)
            elif i == 'Series':
                col_num = page.get_table_column('Series')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('SPARK', result_date)
            elif i == 'SP/FP':
                col_num = page.get_table_column('SP/FP')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('Smart', result_date)
            elif i == 'Model':
                col_num = page.get_table_column('Model')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('KG6', result_date)
            elif i == 'ModelType':
                col_num = page.get_table_column('Model Type')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('Mid-Ends', result_date)
            elif i == 'Item':
                col_num = page.get_table_column('Item')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('KG6 64+2', result_date)
            elif i == 'MarketName':
                col_num = page.get_table_column('Market Name')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('SPARK 8', result_date)
            elif i == 'IMEI/SN':
                col_num = page.get_table_column('IMEI/SN')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('350100248561825', result_date)
            elif i == 'ActivationStatus':
                col_num = page.get_table_column('Activation Status')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('Activated', result_date)
            elif i == 'ActivationCountry':
                col_num = page.get_table_column('Activation Country')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('Gabon', result_date)
            elif i == 'ActivationDate':
                col_num = page.get_table_column('Activation Date')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('2022-01-24', result_date)
            elif i == 'DeliveryCountry':
                col_num = page.get_table_column('Delivery Country')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('United Arab Emirates', result_date)
            elif i == 'AchieveorNot':
                col_num = page.get_table_column('Achieve or Not')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('No', result_date)
            elif i == 'Country':
                col_num = page.get_table_column('Country')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('DB3', result_date)
            elif i == 'CityTier':
                col_num = page.get_table_column('City Tier')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('T1', result_date)
            elif i == 'SalesRegion2':
                col_num = page.get_table_column('Sales Region 2')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('DB3', result_date)
            elif i == 'UploaderID':
                col_num = page.get_table_column('Uploader ID')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('qiulian1', result_date)
            elif i == 'Position':
                col_num = page.get_table_column('Position')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('二期督导', result_date)
            elif i == 'UploadType':
                col_num = page.get_table_column('Upload Type')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('App Scan', result_date)
            else:
                col_num = page.get_table_column('Supplier ID')
                result_date = page.get_table_content(col_num)
                ValueAssert.value_assert_equal('PK100039', result_date)
        page.click_reset()



@allure.feature("销售管理-门店销售查询")
class TestExportShopSalesQuery:
    @allure.story("导出门店销量")
    @allure.title("门店销售查询页面，按销售开始与结束日期查询 门店销售查询记录，并导出筛选后的数据")
    @allure.description("门店销售查询页面，按销售开始与结束日期查询 门店销售查询记录，并导出筛选后的数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开销售管理-打开门店销售查询页面"""
        user.click_gotomenu("Sales Management", "Shop Sales Query")
        """实例化对象类"""
        export = ShopSaleQueryPage(drivers)
        base = Base(drivers)
        today = base.get_datetime_today()

        export.click_unfold()
        """首先按日期筛选门店销量数据"""
        export.input_upload_start_date("2022-11-01")
        export.click_upload_end_date()
        export.input_sales_date("2022-11-01", today)
        export.click_fold()
        export.click_search()
        total = export.get_total_text()
        """Shop Sales Query页面，增加断言 对比列表字段与分页总条数是否有数据"""
        export.assert_total(total)

        #筛选销售日期后，点击导出功能
        export.click_export()
        export.click_download_more()
        export.input_task_name("Shop Sales Query")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Shop Sales Query")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_shop_sales_query()

@allure.feature("销售管理-门店销售查询")
class TestImportShopSalesQuery:
    @allure.story("门店销量上报")
    @allure.title("导入门店销量上报成功")
    @allure.description("导入门店销量上报，符合条件导入成功，不符合条件导入失败")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures()
    def test_003_001(self, drivers):
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SenegalwjkPromoterInfinix", "xLily6x")
        """打开销售管理-打开门店销售查询页面"""

        """点击导入"""
        user = ShopSaleQueryPage(drivers)
        user.click_menu("Sales Management", "Shop Sales Query")
        user.reset_ShopSalesQuery_import('356514117190074')
        menu.click_gotomenu("Purchase Management", "Shop Purchase Query")
        user.reset_ShopPurchaseQuery_import('356514117190074')
        user.click_menu("Sales Management", "Shop Sales Query")
        user.click_import()
        user.import_ShopSalesQuery_file('销量上报1个条件2个不符合条件.xlsx')
        """断言文件导入成功"""
        user.assert_import_success()
        user.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        user.click_confirm()
        """断言ImportRecord页面结果"""
        user.assert_ImportRecord_result('销量上报1个条件2个不符合条件.xlsx', 'Status', 'Upload Successfully')
        user.assert_ImportRecord_result('销量上报1个条件2个不符合条件.xlsx', 'Total', '3')
        user.assert_ImportRecord_result('销量上报1个条件2个不符合条件.xlsx', 'Success', '1')
        user.assert_ImportRecord_result('销量上报1个条件2个不符合条件.xlsx', 'Failed', '2')
        user.assert_ImportRecord_result('销量上报1个条件2个不符合条件.xlsx', 'Import Date', today)
        """断言ShopPurchaseQuery页面结果"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_ShopPurchaseQuery_query('IMEI', '356514117190074')
        user.input_ShopPurchaseQuery_query('Status', 'Committed')
        user.click_search()
        user.assert_Query_result('IMEI', '356514117190074')
        """断言Shop Sales Query页面结果"""
        user.click_menu("Sales Management", "Shop Sales Query")
        user.click_unfold()
        user.input_ShopSalesQuery_query('IMEI/SN', '356514117190074')
        user.click_search()
        user.assert_Query_result('IMEI/SN', '356514117190074')
        """Shop Sales Query页面点击指定imei复选框，删除"""
        user.click_checkbox('356514117190074')
        user.click_delete()
        DomAssert(drivers).assert_att('Deleted Successfully')
        """断言ShopPurchaseQuery页面自动取消"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_ShopPurchaseQuery_query('IMEI', '356514117190074')
        user.click_search()
        user.assert_Query_result('Status', 'Canceled')
        """！！！！！！删除后再次导入！！！！！"""
        user.click_menu("Sales Management", "Shop Sales Query")
        user.refresh()
        user.click_import()
        user.import_ShopSalesQuery_file('销量上报1个条件2个不符合条件.xlsx')
        """断言文件导入成功"""
        user.assert_import_success()
        user.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        user.click_confirm()
        """断言ImportRecord页面结果"""
        user.assert_ImportRecord_result('销量上报1个条件2个不符合条件.xlsx', 'Status', 'Upload Successfully')
        user.assert_ImportRecord_result('销量上报1个条件2个不符合条件.xlsx', 'Total', '3')
        user.assert_ImportRecord_result('销量上报1个条件2个不符合条件.xlsx', 'Success', '1')
        user.assert_ImportRecord_result('销量上报1个条件2个不符合条件.xlsx', 'Failed', '2')
        user.assert_ImportRecord_result('销量上报1个条件2个不符合条件.xlsx', 'Import Date', today)
        """断言ShopPurchaseQuery页面结果"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_ShopPurchaseQuery_query('IMEI', '356514117190074')
        user.input_ShopPurchaseQuery_query('Status', 'Committed')
        user.click_search()
        user.assert_Query_result('IMEI', '356514117190074')
        """断言Shop Sales Query页面结果"""
        user.click_menu("Sales Management", "Shop Sales Query")
        user.click_unfold()
        user.input_ShopSalesQuery_query('IMEI/SN', '356514117190074')
        user.click_search()
        user.assert_Query_result('IMEI/SN', '356514117190074')
        """Shop Sales Query页面点击指定imei复选框，删除"""
        user.click_checkbox('356514117190074')
        user.click_delete()
        DomAssert(drivers).assert_att('Deleted Successfully')
        """断言ShopPurchaseQuery页面自动取消"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_ShopPurchaseQuery_query('IMEI', '356514117190074')
        user.click_search()
        user.assert_Query_result('Status', 'Canceled')

    @allure.story("门店销量上报")
    @allure.title("门店入库自动激活转销量")
    @allure.description("已配置自动转销量，库存上报后，自动转门店销量上报")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures()
    def test_003_002(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SenegalwjkPromoterTECNO", "xLily6x")
        """库存上报"""
        user = ShopSaleQueryPage(drivers)
        """检查imei是否已经库存上报&销量上报"""
        menu.click_gotomenu("Sales Management", "Shop Sales Query")
        user.reset_ShopSalesQuery_import('358870660738380')
        menu.click_gotomenu("Purchase Management", "Shop Purchase Query")
        user.reset_ShopPurchaseQuery_import('358870660738380')
        user.refresh()
        user.click_import()
        user.import_file('Shop+Stock+In+Template配置自动上报销量.xlsx')
        user.assert_import_success()
        user.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        user.click_confirm()
        """断言ImportRecord页面结果"""
        user.assert_ImportRecord_result('Shop+Stock+In+Template配置自动上报销量.xlsx', 'Status', 'Upload Successfully')
        user.assert_ImportRecord_result('Shop+Stock+In+Template配置自动上报销量.xlsx', 'Total', '1')
        user.assert_ImportRecord_result('Shop+Stock+In+Template配置自动上报销量.xlsx', 'Success', '1')
        # user.assert_ImportRecord_result('Shop+Stock+In+Template配置自动上报销量.xlsx', 'Import Date', '2022-11-21')
        """断言ShopSalesQuery页面是否自动上报"""
        menu.click_gotomenu("Sales Management", "Shop Sales Query")
        user.click_unfold()
        user.input_ShopSalesQuery_query('IMEI/SN', '358870660738380')
        user.click_search()
        user.assert_Query_result('Status', 'Committed')
        user.assert_Query_result('IMEI/SN', '358870660738380')
        """Shop Sales Query页面点击指定imei复选框，删除"""
        user.click_checkbox('358870660738380')
        user.click_delete()
        DomAssert(drivers).assert_att('Deleted Successfully')
        """Shop Purchase Query页面点击指定imei复选框，删除"""
        menu.click_gotomenu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_ShopPurchaseQuery_query('IMEI', '358870660738380')
        user.input_ShopPurchaseQuery_query('Status', 'Committed')
        user.click_search()
        user.click_checkbox('358870660738380')
        user.click_cancel()
        DomAssert(drivers).assert_att('Cancel success')

    @allure.story("门店销量导出")
    @allure.title("门店销量导出")
    @allure.description("门店销量导出")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures()
    def test_003_003(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "qiulian1", "xLily6x")
        """库存上报"""
        user = ShopSaleQueryPage(drivers)
        """检查imei是否已经库存上报&销量上报"""
        menu.click_gotomenu("Sales Management", "Shop Sales Query")
        user.click_export()
        DomAssert(drivers).assert_att('Create successful , will auto downloaded , please wait')
        menu.click_gotomenu("Basic Data Management", "Export Record")
        user.assert_Record_result('Export Record', 'Shop Sales Query', 'Download Status', 'COMPLETE')
        user.assert_Record_result('Export Record', 'Shop Sales Query', 'File Size')


if __name__ == '__main__':
    pytest.main(['SalesManagement_ShopSalesQuery.py'])
