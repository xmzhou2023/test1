import logging
import allure
import pytest
from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.CustomerManagement_CustomerManagement import CustomerManagementPage
from public.base.assert_ui import DomAssert, ValueAssert
from public.base.assert_ui import SQLAssert
from libs.common.connect_sql import *
from libs.common.time_ui import sleep
from public.base.basics import Base
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范) 删除功能屏蔽了，注释了删除用例
"""

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_customer_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@pytest.fixture(scope='function')
def function_export_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    for i in range(2):
        get_menu_class = menu.get_open_menu_class()
        class_value = "tags-view-item router-link-exact-active router-link-active active"
        if class_value == str(get_menu_class):
            menu.click_close_open_menu()
            sleep(1)

@allure.feature("客户管理-客户管理(全球)")  # 模块名称
class TestQueryGlobalCustomers:
    @allure.story("查询客户")
    @allure.title("查询客户列表所以数据加载，然后筛选客户信息是否加载正常")
    @allure.description("查询客户列表所以数据加载，然后筛选客户信息是否加载正常")
    @allure.severity("normal")
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_customer_fixture')
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        """登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开客户管理菜单"""
        user.click_gotomenu("Customer Management", "Customer Management(Global)")
        query = CustomerManagementPage(drivers)
        get_cust_name = query.get_customer_name()
        get_cust_id = query.get_customer_id()
        get_list_brand = query.get_list_field("Get list Brand")
        get_list_ware_id = query.get_list_field("Get Warehouse ID")
        get_list_ware_name = query.get_list_field("Get Warehouse Name")
        get_all_total = query.get_list_total()
        logging.info("打印客户列表总分页数：{}".format(get_all_total))
        ValueAssert.value_assert_IsNoneNot(get_cust_name)
        ValueAssert.value_assert_IsNoneNot(get_cust_id)
        ValueAssert.value_assert_IsNoneNot(get_list_brand)
        ValueAssert.value_assert_IsNoneNot(get_list_ware_id)
        ValueAssert.value_assert_IsNoneNot(get_list_ware_name)
        query.assert_total2(get_all_total)
        """获取列表的客户ID，然后筛选此客户信息，是否加载正常"""
        get_query_cust_id = query.get_customer_id()
        query.input_customer_query(get_query_cust_id)
        query.click_search()
        get_query_cust_name = query.get_customer_name()
        get_query_cust_id = query.get_customer_id()
        get_query_list_brand = query.get_list_field("Get list Brand")
        get_query_list_ware_id = query.get_list_field("Get Warehouse ID")
        get_query_list_ware_name = query.get_list_field("Get Warehouse Name")
        get_query_total = query.get_list_total()
        logging.info("打印客户列表筛选后的总分页数：{}".format(get_query_total))
        ValueAssert.value_assert_IsNoneNot(get_query_cust_name)
        ValueAssert.value_assert_IsNoneNot(get_query_cust_id)
        ValueAssert.value_assert_IsNoneNot(get_query_list_brand)
        ValueAssert.value_assert_IsNoneNot(get_query_list_ware_id)
        ValueAssert.value_assert_IsNoneNot(get_query_list_ware_name)
        query.assert_total1(get_query_total)
        #query.click_close_customer_mgt()

    @allure.story("查询用户")
    @allure.title("随机条件组合查询")
    @allure.description("用户管理页面，查询用户列表所有用户数据加载")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_002(self, drivers):
        """变量"""
        query_dict = {
            'Customer': 'caron2301',
            'Contact Name': 'caron2301',
            'Sales Region': 'Kaolack',
            'Country/City': '深圳2',
            'Customer Type': 'Distributor',
            'Customer Grade': 'A-W',
            'SAP Customer ID': 'caron2301',
            'Whether use DCR system': 'Yes',
            'Customer Category': '',
            'Brand': 'TECNO',
            'Status': 'Enable',
            'Channel Sales Manager': '',
            'User': 'CNCARON230101',
            'Warehouse': 'WCNcaron230101',
        }
        add = CustomerManagementPage(drivers)
        add.click_menu("Customer Management", "Customer Management (global)")
        add.click_unfold()
        add.random_Query_Method(query_dict)


@allure.feature("客户管理-客户管理(全球)")
class TestAddCustomer:
    @allure.story("新增客户")
    @allure.title("新增二代客户信息")
    @allure.description("新增客户操作成功，列表展示新增的客户信息")
    @allure.severity("normal")
    @pytest.mark.smoke
    @pytest.mark.usefixtures('function_customer_fixture')
    def test_002_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        """登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开客户管理菜单"""
        user.click_gotomenu("Customer Management", "Customer Management(Global)")
        add_customer = CustomerManagementPage(drivers)
        """点击Add新增客户按钮"""
        add_customer.click_add()
        """客户名称前缀后面随机生成数字"""
        customer_name = add_customer.cus_name_random()
        logging.info("打印生成的Customer Name{}".format(customer_name))
        email = add_customer.email_random()
        logging.info("打印生成的Email{}".format(email))
        contact_name = add_customer.contact_name_random()
        logging.info("打印生成的Contact Name{}".format(contact_name))
        contact_no = add_customer.contact_no_random()
        logging.info("打印生成的Contact No{}".format(contact_no))

        """新建客户填写Basic Info基本信息"""
        """第一个参数可为Distributor or Retailer,第二个参数为品牌，第三个参数为Customer Name,第四个为Sales Region，第五个为SAPID"""
        add_customer.input_form_basic_info('Sub-dealer', 'Infinix', 'TECNO', customer_name, 'Barisal-Wucong')

        """第一个参数为testName,第二个为testNo,第三个为emily,第四个为country,第四个为testAddress"""
        add_customer.input_form_contact_info(contact_name, contact_no, email, 'Barisal Sadar', "南山区深圳湾生态园9B5")
        add_customer.click_search()
        get_customer_id1 = add_customer.get_customer_id()
        sql = SQLAssert('DCR', 'test')
        sql.assert_sql(get_customer_id1, "select enterprise_code from t_enterprise  where created_by='lhmadmin' order by created_time desc limit 1")

        """筛选新增的客户ID，然后断言客户id、客户name、品牌、联系人、联系电话是否正确"""
        add_customer.input_customer_query(get_customer_id1)
        """点击查询按钮"""
        add_customer.click_search()
        get_customer_id2 = add_customer.get_customer_id()
        get_customer_name = add_customer.get_customer_name()
        get_brand = add_customer.get_list_new_brand()
        ValueAssert.value_assert_equal(get_customer_id1, get_customer_id2)
        ValueAssert.value_assert_equal(get_customer_name, customer_name)
        ValueAssert.value_assert_equal("Infinix,TECNO", get_brand)
        get_contact_name = add_customer.get_contact_name()
        get_contact_no = add_customer.get_contact_no()
        get_customer_type = add_customer.get_customer_type('Sub-dealer')
        ValueAssert.value_assert_equal(contact_name, get_contact_name)
        ValueAssert.value_assert_equal(contact_no, get_contact_no,)
        ValueAssert.value_assert_equal("Sub-dealer", get_customer_type)
        #add_customer.click_close_customer_mgt()


@allure.feature("客户管理-客户管理(全球)")  #  模块名称
class TestEditCustomer:
    @allure.story("编辑客户")
    @allure.title("编辑二代客户信息")
    @allure.description("编辑客户操作成功，列表筛选该客户ID，客户名称更新为编辑后的信息")
    @allure.severity("normal")
    @pytest.mark.smoke   # 用例标记
    @pytest.mark.usefixtures('function_customer_fixture')
    def test_003_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        """登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开客户管理菜单"""
        user.click_gotomenu("Customer Management", "Customer Management(Global)")
        edit = CustomerManagementPage(drivers)
        """从数据库查询最近新建的门店ID"""
        user = SQL('DCR', 'test')
        customer_data = user.query_db(
            "select enterprise_code from t_enterprise  where created_by='lhmadmin' order by created_time desc limit 1")
        customer_id = customer_data[0].get("enterprise_code")
        logging.info("从数据库查询Customer ID：{}".format(customer_id))

        """筛选新增的客户ID，然后编辑客户name、联系人、联系电话信息"""
        edit.input_customer_query(customer_id)
        edit.click_search()
        """随机生成数据客户名称、联系人、联系电话"""
        customer_name = edit.cus_name_random()
        contact_name = edit.contact_name_random()
        contact_no = edit.contact_no_random()
        """编辑客户信息操作"""
        edit.edit_form_info(customer_name, contact_name, contact_no)
        """数据库断言，查询数据库是否存在修改后的客户名称"""
        sql1 = SQLAssert('DCR', 'test')
        sql1.assert_sql(customer_name, "select enterprise_name from t_enterprise  where created_by='lhmadmin' order by created_time desc limit 1")
        """前端断言，客户列表是否更新修改后的信息"""
        get_customer_name = edit.get_customer_name()
        get_contact_name = edit.get_contact_name()
        get_contact_no = edit.get_contact_no()
        ValueAssert.value_assert_equal(customer_name, get_customer_name)
        ValueAssert.value_assert_equal(contact_name, get_contact_name)
        ValueAssert.value_assert_equal(contact_no, get_contact_no)
        #edit.click_close_customer_mgt()


# @allure.feature("客户管理-客户管理(全球)")  #  模块名称
# class TestDeleteCustomer:
    # @allure.story("删除客户")
    # @allure.title("删除新建的二代客户信息")
    # @allure.description("删除新建的二代客户成功后，列表不展示被删除的客户信息")
    # @allure.severity("normal")
    # @pytest.mark.smoke   # 用例标记
    # @pytest.mark.usefixtures('function_customer_fixture')
    # def test_004_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
    #     """登录"""
    #     user = LoginPage(drivers)
    #     user.initialize_login(drivers, "lhmadmin", "dcr123456")
    #     """打开客户管理菜单"""
    #     user.click_gotomenu("Customer Management", "Customer Management(Global)")
    #
    #     delete = CustomerManagementPage(drivers)
    #
    #     """从数据库查询最近新建的门店ID"""
    #     user = SQL('DCR', 'test')
    #     customer_data = user.query_db(
    #         "select enterprise_code from t_enterprise  where created_by='lhmadmin' order by created_time desc limit 1")
    #     customer_id = customer_data[0].get("enterprise_code")
    #     logging.info("从数据库查询Customer ID：{}".format(customer_id))
    #
    #     """筛选新增的客户ID，然后删除此客户记录"""
    #     delete.input_customer_query(customer_id)
    #     delete.click_search()
    #
    #     """删除新建的客户"""
    #     delete.delete_customer()
    #     DomAssert(drivers).assert_att('Successfully')
    #     delete.click_reset()
    #
    #     """前端断言，获取列表第一条客户ID，与删除前的客户ID比较，列表不存在删除后的Customer ID"""
    #     get_customer_id = delete.get_customer_id()
    #     logging.info("获取列表第一行Customer ID：{}".format(get_customer_id))
    #     ValueAssert.value_assert_InNot(get_customer_id, customer_id)
    #     #delete.click_close_customer_mgt()


    # @allure.story("删除客户")
    # @allure.title("删除有绑定订单数据的客户，不能被删除")
    # @allure.description("删除有绑定订单数据的客户，提示：不能被删除")
    # @allure.severity("normal")
    # @pytest.mark.smoke
    # @pytest.mark.usefixtures('function_customer_fixture')
    # def test_004_002(self, drivers):
    #     """登录"""
    #     user = LoginPage(drivers)
    #     user.initialize_login(drivers, "lhmadmin", "dcr123456")
    #     """打开客户管理菜单"""
    #     user.click_gotomenu("Customer Management", "Customer Management(Global)")
    #
    #     delete2 = CustomerManagementPage(drivers)
    #     """筛选新增的客户ID，然后删除此客户记录"""
    #     delete2.input_customer_query('BD403442')
    #     delete2.click_search()
    #     delete2.delete_have_records_customer()
    #     get_customer_id = delete2.get_customer_id()
    #     get_customer_name = delete2.get_customer_name()
    #     ValueAssert.value_assert_equal('BD403442', get_customer_id)
    #     ValueAssert.value_assert_IsNoneNot(get_customer_name)


@allure.feature("客户管理-客户管理(全球)") # 模块名称
class TestExportCustomer:
    @allure.story("导出客户")
    @allure.title("导出筛选后的客户信息")
    @allure.description("导出筛选后的客户信息，验证导出功能是否正常")
    @allure.severity("normal")
    @pytest.mark.smoke   # 用例标记
    @pytest.mark.usefixtures('function_export_fixture')
    def test_005_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        """登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开客户管理菜单"""
        user.click_gotomenu("Customer Management", "Customer Management(Global)")
        export = CustomerManagementPage(drivers)
        """获取当天日期"""
        today = Base(drivers).get_datetime_today()
        """获取列表的客户ID，然后筛选此客户，进行导出操作"""
        get_cust_id = export.get_customer_id()
        export.input_customer_query(get_cust_id)
        export.click_search()
        """点击导出"""
        export.click_export()
        export.click_download_more()
        export.input_task_name("Customer Management (global)")
        export.export_record_create_start_date(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        user_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_operation_text()
        """断言导出记录列表，是否生成一条导出成功的记录"""
        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Customer Management (global)")
        ValueAssert.value_assert_equal(user_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_customer_mgt()


@allure.feature("客户管理-客户管理(全球)") # 模块名称
class TestDisableCustomer:
    @allure.story("禁用客户")
    @allure.title("禁用客户")
    @allure.description("筛选需要禁用的客户，然后点击禁用功能，查看该客户状态是否更新为Disable状态")
    @allure.severity("normal")
    @pytest.mark.RT   # 用例标记
    @pytest.mark.usefixtures('function_customer_fixture')
    def test_006_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        """登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开客户管理菜单"""
        user.click_gotomenu("Customer Management", "Customer Management(Global)")
        disable = CustomerManagementPage(drivers)
        """筛选待禁用的客户ID"""
        disable.input_customer_query('EC402067')
        disable.click_search()
        """点击更多里的禁用操作"""
        disable.click_more_option_disable()
        DomAssert(drivers).assert_att("Successfully")
        """断言禁用操作后，列表状态是否更新为Disable状态"""
        disable.assert_customer_query_result('Customer ID', 'EC402067')
        disable.assert_customer_query_result('Status', 'Disable')


    @allure.story("启用客户")
    @allure.title("启用客户")
    @allure.description("筛选需要启用的客户，然后点击启用功能，查看该客户状态是否更新为Enable状态")
    @allure.severity("normal")
    @pytest.mark.RT  # 用例标记
    @pytest.mark.usefixtures('function_customer_fixture')
    def test_006_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        """登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开客户管理菜单"""
        user.click_gotomenu("Customer Management", "Customer Management(Global)")
        enable = CustomerManagementPage(drivers)
        """筛选待启用的客户ID"""
        enable.input_customer_query('EC402067')
        enable.click_search()
        """点击更多里的启用操作"""
        enable.click_more_option_enable()
        DomAssert(drivers).assert_att("Successfully")
        """断言启用操作后，列表状态是否更新为Enable状态"""
        enable.assert_customer_query_result('Customer ID', 'EC402067')
        enable.assert_customer_query_result('Status', 'Enable')


@allure.feature("客户管理-客户管理(全球)")
class TestImportCustomer:
    @allure.story("导入客户操作")
    @allure.title("导入客户操作，然后删除导入的客户操作")
    @allure.description("导入客户成功后，查看列表是否展示导入的客户信息；然后删除导入的客户操作")
    @allure.severity("normal")
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_customer_fixture')
#     def test_008_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
#         user = LoginPage(drivers)
#         user.initialize_login(drivers, "lhmadmin", "dcr123456")
#         """打开客户管理菜单"""
#         user.click_gotomenu("Customer Management", "Customer Management(Global)")
#
#         upload = CustomerManagementPage(drivers)
#         upload.click_import()
#         upload.click_import_save()
#         DomAssert(drivers).assert_att('Please upload first.')
#         sleep(1)
#         upload.upload_true_file('CustomerTemplate.xlsx')
#         upload.click_import_record_search()
#
#         today = Base(drivers).get_datetime_today()
#         """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
#         get_file_name = upload.get_import_file_name()
#         get_status = upload.get_import_status()
#         get_total = upload.get_import_total()
#         get_success = upload.get_import_success()
#         get_failed = upload.get_import_failed()
#         get_import_date = upload.get_import_import_date()
#         ValueAssert.value_assert_equal('CustomerTemplate.xlsx', get_file_name)
#         ValueAssert.value_assert_equal('Upload Successfully', get_status)
#         ValueAssert.value_assert_equal('1', get_total)
#         ValueAssert.value_assert_equal('1', get_success)
#         ValueAssert.value_assert_equal('0', get_failed)
#         ValueAssert.value_assert_equal(today, get_import_date)
#         """关闭当前打开的菜单"""
#         user.click_close_open_menu()
#         """根据导入的客户ID，筛选导入的数据，进行断言列表是否存在导入的数据"""
#         upload.input_customer_query('Cus_test_itel')
#         upload.click_search()
#
#         """断言User Salary Management 页面，是否加载导入成的数据"""
#         get_brand = upload.get_list_brand()
#         get_cus_id = upload.get_customer_id()
#         get_cus_name = upload.get_customer_name()
#         get_contact_name = upload.get_contact_name()
#         get_contact_no = upload.get_contact_no()
#         ValueAssert.value_assert_equal('itel', get_brand)
#         ValueAssert.value_assert_IsNoneNot(get_cus_id)
#         ValueAssert.value_assert_equal('Cus_test_itel', get_cus_name)
#         ValueAssert.value_assert_equal('test_lhm123', get_contact_name)
#         ValueAssert.value_assert_IsNoneNot(get_contact_no)
#
#         """删除导入的客户数据"""
#         #upload.delete_customer()
#         #DomAssert(drivers).assert_att('Successfully')
#         # """ 在数据库表中，删除导入的客户 """
#         # sql1 = SQL('DCR', 'test')
#         # sql1.delete_db(
#         #     "delete from t_enterprise where enterprise_NAME = 'Cus_test_itel'")


    @allure.story("导入客户操作")
    @allure.title("导入客户操作，输入不存在的销售区域，导入失败")
    @allure.description("导入客户操作，输入不存在的销售区域，导入失败")
    @allure.severity("normal")
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_customer_fixture')
    def test_008_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开客户管理菜单"""
        user.click_gotomenu("Customer Management", "Customer Management(Global)")

        upload = CustomerManagementPage(drivers)
        upload.click_import()
        upload.click_import_save()
        DomAssert(drivers).assert_att('Please upload first.')
        sleep(1)
        upload.upload_true_file('CustomerTemplate_failed.xlsx')
        upload.click_import_record_search()

        today = Base(drivers).get_datetime_today()
        """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
        get_file_name = upload.get_import_file_name()
        get_status = upload.get_import_status()
        get_total = upload.get_import_total()
        get_success = upload.get_import_success()
        get_failed = upload.get_import_failed()
        get_import_date = upload.get_import_import_date()
        ValueAssert.value_assert_equal('CustomerTemplate_failed.xlsx', get_file_name)
        ValueAssert.value_assert_equal('Upload Successfully', get_status)
        ValueAssert.value_assert_equal('1', get_total)
        ValueAssert.value_assert_equal('0', get_success)
        ValueAssert.value_assert_equal('1', get_failed)
        ValueAssert.value_assert_equal(today, get_import_date)
        """关闭当前打开的菜单"""
        user.click_close_open_menu()


if __name__ == '__main__':
    pytest.main(['CustomerManagement_CustomerManagement.py'])
