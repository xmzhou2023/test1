import logging
import time
from datetime import datetime

from project.DCR.page_object.StaffAuthorization_UserManagement import UserManagementPage
from public.base.assert_ui import SQLAssert
from libs.common.connect_sql import *
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert, DomAssert
from public.base.basics import Base
from libs.common.time_ui import sleep
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
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

@allure.feature("员工授权-用户管理")
class TestQueryUser:
    @allure.story("查询用户")
    @allure.title("用户管理页面，查询用户列表所有用户数据加载")
    @allure.description("用户管理页面，查询用户列表所有用户数据加载")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """用户授权-用户管理-查询用户管理列表数据用例"""
        user.click_gotomenu("Staff & Authorization", "User Management")

        """用户管理页面，获取列表字段内容"""
        query_user = UserManagementPage(drivers)
        get_list_user_id = query_user.get_text_user_id()
        logging.info("获取列表User ID字段内容：{}".format(get_list_user_id))
        get_list_user_name = query_user.get_text_user_name()
        get_list_brand = query_user.input_get_data("Get list Brand")
        get_list_sales_region1 = query_user.input_get_data("Get list Sales Region1")
        get_list_country = query_user.input_get_data("Get list Country")
        get_total = query_user.get_total()

        """断言查询的列表数据是否存在，分页下面的总条数是否有数据"""
        ValueAssert.value_assert_IsNoneNot(get_list_user_id)
        ValueAssert.value_assert_IsNoneNot(get_list_user_name)
        ValueAssert.value_assert_IsNoneNot(get_list_brand)
        ValueAssert.value_assert_IsNoneNot(get_list_sales_region1)
        ValueAssert.value_assert_IsNoneNot(get_list_country)
        query_user.assert_total(get_total)

        """根据用户筛选用户信息"""
        query_user.input_query_User(get_list_user_id)
        """点击查询按钮"""
        query_user.click_search()

        get_list_user_id2 = query_user.get_text_user_id()
        get_list_user_name2 = query_user.get_text_user_name()
        get_list_brand2 = query_user.input_get_data("Get list Brand")
        get_total2 = query_user.get_total()
        ValueAssert.value_assert_equal(get_list_user_id, get_list_user_id2)
        ValueAssert.value_assert_equal(get_list_user_name, get_list_user_name2)
        ValueAssert.value_assert_IsNoneNot(get_list_brand2)
        ValueAssert.value_assert_equal(get_total2, '1')
        #query_user.click_close_user_mgt()


@allure.feature("员工授权-用户管理")
class TestAddEditQuitTranssionUser:
    @allure.story("用户管理业务流程")
    @allure.title("用户管理页面，新增、编辑、离职传音用户")
    @allure.description("用户管理页面，新增、编辑、离职传音用户能正常运行")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Staff & Authorization", "User Management")

        """新建传音员工账号 用例"""
        """随机生成数字"""
        add_transsion = UserManagementPage(drivers)
        userid = add_transsion.user_id_random()
        logging.info("打印新建传音员工时，输入的user id{}".format(userid))
        username = add_transsion.user_name_random()
        logging.info("打印新建传音员工时，输入的user name{}".format(username))
        add_transsion.click_add_user()
        add_transsion.click_staff_type_value("Transsion Staff")
        add_transsion.input_user_id(userid)

        add_transsion.input_add_user_name(username)

        add_transsion.input_sales_region("Barisal")
        add_transsion.input_country_city("Barisal")
        add_transsion.click_select_brand()
        add_transsion.input_superior("lhmadmin")
        add_transsion.input_position_transsion("lhmTecno促销员")
        add_transsion.input_email("646195353@163.com")
        num = add_transsion.user_id_random()
        add_transsion.input_contact_no("13762513" + num)
        add_transsion.click_gender_female("Female")
        add_transsion.click_add_user_submit()

        add_transsion.click_search()
        """根据输入的Shop ID筛选新建的门店ID后，断言列表是否存在新建门店"""
        add_transsion.input_query_User(userid)
        add_transsion.click_search()
        """首先根据新建的User ID筛选，然后获取列表新增的User ID，User name，进行断言比较是否存在新建的用户"""
        user_id = add_transsion.get_text_user_id()
        user_name = add_transsion.get_text_user_name()
        logging.info("获取用户管理列表User Name字段内容：{}".format(user_name))
        ValueAssert.value_assert_equal(user_id, userid)
        ValueAssert.value_assert_equal(user_name, username)
        """查询数据库用户表的userid,username是否存在断言"""
        sql_asser = SQLAssert('DCR', 'test')
        sql_asser.assert_sql(user_id,
                             "select USER_CODE from t_user where created_by = 'lhmadmin' order by created_time desc limit 1")
        sql_asser.assert_sql(user_name,
                             "select USER_NAME from t_user where created_by= 'lhmadmin'  order by created_time desc limit 1")
        sleep(1)

        """ 编辑传音用户 """
        """筛选用户后，点击Search，进行编辑"""
        username = add_transsion.user_name_random()
        add_transsion.click_edit()
        add_transsion.input_edit_user_name(username)
        add_transsion.click_edit_trans_brand()
        add_transsion.click_user_name()
        add_transsion.input_email("646167867@qq.com")
        num = add_transsion.number_radom()
        add_transsion.input_contact_no("15814025" + num)
        add_transsion.click_gender_female("Male")
        add_transsion.click_add_user_submit()
        DomAssert(drivers).assert_att("Set Up Successfully")
        sleep(3)

        """调用断言 编辑的用户在列表是否更新成功"""
        """首先根据新建或编辑的User ID，然后获取列表新增的User ID，User name，进行断言比较是否存在新建的用户"""
        user_id1 = add_transsion.get_text_user_id()
        user_name = add_transsion.get_text_user_name()
        """断言修改后的用户ID 与用户名是否存在相同值"""
        ValueAssert.value_assert_equal(userid, user_id)
        ValueAssert.value_assert_equal(user_name, username)
        """查询数据库用户表的userid,username是否存在断言"""
        sqlasser = SQLAssert('DCR', 'test')
        sqlasser.assert_sql(user_id,
                            "select USER_CODE from t_user where created_by = 'lhmadmin' order by created_time desc limit 1")
        sqlasser.assert_sql(user_name,
                            "select USER_NAME from t_user where created_by= 'lhmadmin'  order by created_time desc limit 1")
        sleep(1)

        """ 离职传音用户 """
        add_transsion.click_first_checkbox()
        add_transsion.click_more_option_quit()
        """用户离职是否成功，断言"""
        DomAssert(drivers).assert_att("Disabled Successfully")
        #点击重置按钮，断言列表是否不存在被删除的用户
        add_transsion.click_reset()
        user_id2 = add_transsion.get_text_user_id()
        ValueAssert.value_assert_IsNot(user_id1, user_id2)

    @allure.story("用户管理")
    @allure.title("新建代理员工，User ID输入内部员工时，提示报错，使用非内部员工数字能创建成功。")
    @allure.description("新建代理员工，staff type选择Dealer Staff，使用输入User ID是内部员工时，提示失败，然后使用非内部员工数字能成功。")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_002(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击用户管理菜单"""
        UserID = '18650493'
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        add.click_add_user()
        """User ID输入内部员工 提示报错"""
        add.input_Job_Information('User ID', UserID)
        DomAssert(drivers).assert_att(f'{UserID}, user center has been detected. Please change the staff type to Transsion Staff or change the user ID')
        """使用非内部员工数字 创建用户"""
        UserID = str(int(time.time()))
        add.input_Job_Information('Belong To Customer', 'SN405554')
        add.input_Job_Information('User ID', UserID)
        add.input_Job_Information('User Name', '非内部员工数字')
        add.input_Job_Information('Sales Region', 'Kaolack')
        add.input_Job_Information('Country/City', 'Kaolack')
        add.input_Job_Information('Position', 'wjk管理')
        add.input_Job_Information('Superior', '18650493')
        add.input_Job_Information('Brand', 'Infinix')
        add.input_Personal_Information('Gender', 'Male')
        add.click_add_user_submit()
        add.input_search('User ID', UserID)
        add.click_search()
        add.assert_User_Exist('User ID', UserID)
        add.click_checkbox(UserID)
        add.click_more_option_quit()
        DomAssert(drivers).assert_att('Disabled Successfully')

    @allure.story("用户管理")
    @allure.title("已离职员工，不允许新增")
    @allure.description("新增在HR已离职的员工，不允许新增，提示信息为“员工已在用户中心离职，不允许新增”")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_003(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击用户管理菜单"""
        UserID = '18650494'
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        add.click_add_user()
        """User ID输入内部已辞职员工 提示报错"""
        add.input_Job_Information('User ID', UserID)
        DomAssert(drivers).assert_att("The staff has resigned in the user center and can't be added")

    @allure.story("用户管理")
    @allure.title("传音员工，用户类型、用户ID、姓名、性别、个人邮箱、语言、入职日期字段置灰不可编辑")
    @allure.description("页面编辑传音员工，用户类型、用户ID、姓名、性别、个人邮箱、语言、入职日期字段置灰不可编辑")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_004(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击用户管理菜单"""
        userID = '18650493'
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        """筛选传音员工"""
        add.click_reset()
        add.input_search('User ID', userID)
        add.click_search()
        """点击编辑 代理员工的ID/所属客户置灰不可编辑"""
        add.click_Edit('18650493')
        add.assert_input_edit('Staff Type')
        add.assert_input_edit('Hire Date')
        add.assert_input_edit('User ID')
        add.assert_input_edit('User Name')
        add.assert_input_edit('Email')
        add.assert_input_edit('Gender')
        add.assert_input_edit('Native Language')
        add.click_Cancel()

    @allure.story("用户管理")
    @allure.title("代理员工的员工类型、ID、所属客户置灰不可编辑")
    @allure.description("页面进入代理员工编辑页，员工类型、ID、所属客户置灰不可编辑")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_005(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击用户管理菜单"""
        userID = 'SN400001'
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        """筛选代理员工"""
        add.input_search('User ID', userID)
        add.click_search()
        """点击编辑 代理员工的ID/所属客户置灰不可编辑"""
        add.click_Edit(userID)
        add.assert_input_edit('Staff Type')
        add.assert_input_edit('Belong To Customer')
        add.assert_input_edit('User ID')
        add.click_Cancel()

    @allure.story("用户管理")
    @allure.title("已离职员工不可编辑")
    @allure.description("用户中心已离职的员工编辑提示：该用户已在用户中心离职，不能编辑")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_006(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击用户管理菜单"""
        UserID = '18645293'
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        """筛选已离职员工"""
        add.click_unfold()
        add.input_search('User ID', UserID)
        add.input_search('Staff Status', 'Off Service')
        add.click_search()
        """点击编辑 保存 提示用户已离职不可编辑"""
        add.click_Edit(UserID)
        add.click_add_user_submit()
        DomAssert(drivers).assert_att("This user has left the user center and cannot edit")

    @allure.story("用户管理")
    @allure.title("批导编辑传音员工，编辑用户类型失败；编辑已离职员工失败；编辑个人信息不生效")
    @allure.description("批导编辑传音员工，编辑用户类型失败；编辑已离职员工失败；批导编辑传音员工姓名、性别、个人邮箱、语言、入职日期字段不生效")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_007(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击用户管理菜单"""
        UserID = '18650493'
        today = datetime.now().strftime('%Y-%m-%d')
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        """点击导入"""
        add.click_EditImport()
        add.import_file('传音员工批导_离职员工_用户类型_个人信息.xlsx')
        add.assert_import_success()
        add.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        add.click_confirm()
        """断言:导入结果，成功数量1:编辑个人信息成功但不生效，失败数量2:编辑用户类型失败；编辑已离职员工失败；"""
        add.assert_Record_result('Import Record', '传音员工批导_离职员工_用户类型_个人信息.xlsx', 'Total', '3')
        add.assert_Record_result('Import Record', '传音员工批导_离职员工_用户类型_个人信息.xlsx', 'Success', '1')
        add.assert_Record_result('Import Record', '传音员工批导_离职员工_用户类型_个人信息.xlsx', 'Failed', '2')
        add.assert_Record_result('Import Record', '传音员工批导_离职员工_用户类型_个人信息.xlsx', 'Import Date', today)
        """断言:编辑个人信息不生效"""
        add.click_menu("Staff & Authorization", "User Management")
        add.click_unfold()
        add.input_search('User ID', UserID)
        add.click_search()
        add.click_Edit(UserID)
        add.assert_user_Information('User Name', '翁佳柯')
        add.assert_user_Information('Hire Date', '2021-12-30')
        add.assert_user_Information('Email', 'JIAKE.WENG@TRANSSION.COM')
        add.assert_user_Information('Gender', 'Male')

    @allure.story("用户管理")
    @allure.title("批导编辑员工信息成功生效")
    @allure.description("支持导入编辑员工信息，检查成功的（比如职位）")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_008(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """变量"""
        suffix = datetime.now().strftime("%Y%m%d%H%M%S")
        DealerName = 'wjkDealerImport' + suffix
        TranssionName = 'wjk传音员工' + suffix
        ContactNo = 'ContactNo' + suffix
        DealerID = 'SN40000301'
        TranssionInternalID = '18650493'
        TranssionExternalID = 'wjkTS004'
        user_list = 'SN40000301,18650493,wjkTS004'
        today = datetime.now().strftime('%Y-%m-%d')
        """点击用户管理菜单"""
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        """点击导入"""
        add.click_EditImport()
        add.Edit_User_file('员工批导_编辑信息成功.xlsx', DealerID, 'User Name', DealerName)
        add.Edit_User_file('员工批导_编辑信息成功.xlsx', TranssionExternalID, 'User Name', TranssionName)
        add.Edit_User_file('员工批导_编辑信息成功.xlsx', DealerID, 'Contact No.', ContactNo)
        add.Edit_User_file('员工批导_编辑信息成功.xlsx', TranssionExternalID, 'Contact No.', ContactNo)
        add.Edit_User_file('员工批导_编辑信息成功.xlsx', TranssionInternalID, 'Contact No.', ContactNo)
        add.EditImport_file('员工批导_编辑信息成功.xlsx')
        add.assert_import_success()
        add.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        add.click_confirm()
        """断言:导入结果，成功数量3:编辑个人信息成功"""
        add.assert_Record_result('Import Record', '员工批导_编辑信息成功.xlsx', 'Total', '3')
        add.assert_Record_result('Import Record', '员工批导_编辑信息成功.xlsx', 'Success', '3')
        add.assert_Record_result('Import Record', '员工批导_编辑信息成功.xlsx', 'Import Date', today)
        """筛选用户"""
        add.click_menu("Staff & Authorization", "User Management")
        add.click_unfold()
        add.input_search('User ID', user_list)
        add.click_search()
        """断言:代理员工编辑个人信息生效"""
        add.click_Edit(DealerID)
        add.assert_user_Information('User Name', DealerName)
        add.assert_user_Information('Contact No.', ContactNo)
        add.click_Cancel()
        """断言:传音内部员工编辑个人信息生效"""
        add.click_Edit(TranssionInternalID)
        add.assert_user_Information('Contact No.', ContactNo)
        add.click_Cancel()
        """断言:传音外部员工编辑个人信息生效"""
        add.click_Edit(TranssionExternalID)
        add.assert_user_Information('User Name', TranssionName)
        add.assert_user_Information('Contact No.', ContactNo)
        add.click_Cancel()

    @allure.story("用户管理")
    @allure.title("用户复职后，能正常访问DCR系统")
    @allure.description("用户离职又复职后，能正常登录DCR系统,访问不同菜单，不会出现token失效的问题")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_009(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击用户管理菜单"""
        UserID = 'wjkTS003'
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        """复职用户"""
        add.enable_user_Method(UserID)
        """登录复职用户账号 访问DCR系统 点击菜单Add进入创建页面然后取消"""
        user.initialize_login(drivers, UserID, "xLily6x")
        add.click_menu("Staff & Authorization", "User Management")
        add.click_Add()
        add.click_Cancel()
        add.click_menu("Customer Management", "Customer Management (global)")
        add.click_Add()
        add.click_Cancel()
        add.click_menu("Shop Management", "Shop Management (global)")
        add.click_Add()
        add.click_Cancel()
        add.click_menu("Sales Management", "Sales Order")
        add.click_Add()
        add.click_Cancel()
        """停职用户"""
        add.click_menu("Staff & Authorization", "User Management")
        add.disable_user_Method(UserID)

    @allure.story("用户管理")
    @allure.title("内部员工不能直接重置成功")
    @allure.description("内部员工不能直接重置，提示报错")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_010(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击用户管理菜单"""
        userID = '18650493'
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        """重置密码"""
        add.input_search('User ID', userID)
        add.click_search()
        add.click_checkbox(userID)
        add.click_function_button('Reset Password')
        """断言：提示内部用户不可以重置密码"""
        DomAssert(drivers).assert_att("Transsion account can't be reset password in the DCR")
        add.refresh()

    @allure.story("用户管理")
    @allure.title("新建员工，输入内部员工ID自动同步信息")
    @allure.description("新建传音员工，staff type选择Transsion Staff，能自动同步姓名、入职日期信息")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_011(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击用户管理菜单"""
        userID = '18650493'
        userName = '翁佳柯'
        hireDate = '2021-12-30'
        email = 'JIAKE.WENG@TRANSSION.COM'
        gender = 'Male'
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        add.click_add_user()
        add.input_Job_Information('Staff Type', 'Transsion Staff')
        add.input_Job_Information('User ID', userID)
        add.assert_user_Information('User Name', userName)
        add.assert_user_Information('Hire Date', hireDate)
        add.assert_user_Information('Email', email)
        add.assert_user_Information('Gender', gender)

    @allure.story("用户管理")
    @allure.title("已离职员工不能重置密码以及登录系统")
    @allure.description("操作用户离职，已离职的员工不能重置密码,离职后用户不能登录系统")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_002_012(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击用户管理菜单"""
        userID = 'wjkTS003'
        pwd = 'xLily6x'
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        """离职用户"""
        add.disable_user_Method(userID)
        """筛选离职用户，重置密码"""
        add.click_reset()
        add.click_unfold()
        add.input_search('User ID', userID)
        add.input_search('Staff Status', 'Off Service')
        add.click_search()
        add.click_checkbox(userID)
        add.click_function_button('Reset Password', confirm='No')
        """断言：已离职的员工不能重置密码"""
        DomAssert(drivers).assert_att("Disable account can't be reset password,pls enable it first;")
        """离职员工账号登录系统"""
        user.click_loginOut()
        user.input_account(userID)
        user.input_passwd(pwd)
        user.click_loginsubmit()
        """断言：已离职的员工不能登录系统"""
        DomAssert(drivers).assert_att("The user has resigned in DCR!")


@allure.feature("员工授权-用户管理")
class TestAddEditQuitDealerUser:
    @allure.story("用户管理业务流程")
    @allure.title("用户管理页面，新增、编辑、离职代理用户")
    @allure.description("用户管理页面，新增、编辑、离职代理用户能正常运行")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Staff & Authorization", "User Management")

        """新建国包代理员工"""
        dealer_user = UserManagementPage(drivers)
        dealer_user.click_add_user()
        username = dealer_user.user_name_random()
        dealer_user.click_staff_type_value("Dealer Staff")
        dealer_user.input_belong_to_cust("UG4019912")
        dealer_user.input_add_user_name(username)
        dealer_user.input_sales_region("Barisal")
        dealer_user.input_country_city("Barisal")
        dealer_user.click_select_brand()
        dealer_user.input_position_dealer("lhm二代")
        dealer_user.input_superior('lhmadmin')
        dealer_user.input_email("646195353@163.com")
        num = dealer_user.number_radom()
        dealer_user.input_contact_no("13896785" + num)
        dealer_user.click_gender_female('Female')
        dealer_user.click_add_user_submit()

        dealer_user.click_search()
        """筛选用户后，点击Search，进行断言门店列表是否存在新建的门店ID"""
        dealer_user.input_query_User(username)
        dealer_user.click_search()

        """首先根据新建的User ID筛选，然后获取列表新增的User ID，User name，进行断言比较是否存在新建的用户"""
        user = SQL('DCR', 'test')
        result = user.query_db(
            "select u.USER_CODE  from  t_user as u,t_employee as e  where  u.ID=e.U_ID  and  e.created_by='lhmadmin'  order by e.created_time desc limit 1")
        userid = result[0].get('USER_CODE')

        user_id = dealer_user.get_text_user_id()
        user_name = dealer_user.get_text_user_name()
        ValueAssert.value_assert_equal(user_id, userid)
        ValueAssert.value_assert_equal(user_name, username)
        """查询数据库用户表的userid,username是否存在断言"""
        sql_asser = SQLAssert('DCR', 'test')
        sql_asser.assert_sql(user_id,
                             "select u.USER_CODE  from  t_user as u,t_employee as e  where  u.ID=e.U_ID  and  e.created_by='lhmadmin'  order by e.created_time desc limit 1")
        sql_asser.assert_sql(user_name,
                             "select u.USER_NAME  from  t_user as u,t_employee as e  where  u.ID=e.U_ID  and  e.created_by='lhmadmin'  order by e.created_time desc limit 1")
        sleep(1)

        """ 编辑代理员工 """
        """筛选用户后，点击Search，进行编辑操作"""
        username = dealer_user.user_name_random()
        logging.info("打印编辑代理员工时，输入的User Name{}".format(username))
        dealer_user.click_edit()
        dealer_user.input_edit_user_name(username)
        dealer_user.click_edit_dealer_brand()
        """点击user name属性，将光标从品牌字段移开"""
        dealer_user.click_user_name()
        dealer_user.input_email("821367855@qq.com")
        num = dealer_user.number_radom()
        dealer_user.input_contact_no("13914021" + num)
        dealer_user.click_gender_female("Male")
        dealer_user.click_add_user_submit()
        """编辑成功后，页面是否弹出编辑成功提示语"""
        DomAssert(drivers).assert_att("Set Up Successfully")
        sleep(3)
        """调用断言 编辑的用户在列表是否更新成功"""
        """首先根据新建或编辑的User ID，然后获取列表新增的User ID，User name，进行断言比较是否存在新建的用户"""
        user_id1 = dealer_user.get_text_user_id()
        user_name = dealer_user.get_text_user_name()
        """断言修改后的用户ID与用户名称是否存在相同值"""
        ValueAssert.value_assert_equal(user_id1, userid)
        ValueAssert.value_assert_equal(user_name, username)
        """查询数据库用户表的userid,username是否存在断言"""
        sqlasser = SQLAssert('DCR', 'test')
        sqlasser.assert_sql(user_id,
                            "select u.USER_CODE  from  t_user as u,t_employee as e  where  u.ID=e.U_ID  and  e.created_by='lhmadmin'  order by e.created_time desc limit 1")
        sqlasser.assert_sql(user_name,
                            "select u.USER_NAME  from  t_user as u,t_employee as e  where  u.ID=e.U_ID  and  e.created_by='lhmadmin'  order by e.created_time desc limit 1")
        sleep(1)

        """ 离职代理员工 """
        dealer_user.click_first_checkbox()
        dealer_user.click_more_option_quit()
        """用户离职是否成功，断言"""
        DomAssert(drivers).assert_att("Disabled Successfully")
        """点击重置按钮，断言列表是否不存在被删除的用户"""
        dealer_user.click_reset()
        user_id2 = dealer_user.get_text_user_id()
        ValueAssert.value_assert_IsNot(user_id1, user_id2)


@allure.feature("员工授权-用户管理")
class TestExportUser:
    @allure.story("导出用户")
    @allure.title("用户管理页面，导出筛选的用户数据")
    @allure.description("用户管理页面，导出筛选的用户数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_004_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """用户授权-用户管理-查询用户管理列表数据用例"""
        user.click_gotomenu("Staff & Authorization", "User Management")

        export = UserManagementPage(drivers)
        """根据获取列表的user ID进行筛选用户"""
        get_user_id = export.get_text_user_id()
        export.input_query_User(get_user_id)
        export.click_search()

        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        """点击导出"""
        export.click_export()
        export.click_download_more()
        export.input_task_name("User management")
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "User management")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_user_mgt()


@allure.feature("员工授权-用户管理")
class TestImportUser:
    @allure.story("导入用户")
    @allure.title("用户管理页面，导入用户操作，查询列表是否存在导入的客户")
    @allure.description("用户管理页面，导入用户成功后，查看列表是否展示导入的用户信息；然后删除导入的用户操作")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_005_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """用户授权-用户管理-查询用户管理列表数据用例"""
        user.click_gotomenu("Staff & Authorization", "User Management")
        upload = UserManagementPage(drivers)

        """User Management页面，导入前获取列表筛选的User ID，如果能筛选到1条记录，先删除已存在的用户"""
        upload.delete_repetitive_user()

        upload.click_import()
        upload.click_import_save()
        DomAssert(drivers).assert_att('Please upload first.')
        sleep(1)
        upload.upload_true_file('UserTemplate.xlsx')
        """循环点击查询，直到获取到导入记录状态为Upload Successfully"""
        upload.click_import_status_search()

        today = Base(drivers).get_datetime_today()
        """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
        get_file_name = upload.get_import_file_name()
        get_status = upload.get_import_status()
        get_total = upload.get_import_total()
        get_success = upload.get_import_success()
        get_failed = upload.get_import_failed()
        get_import_date = upload.get_import_import_date()
        ValueAssert.value_assert_equal('UserTemplate.xlsx', get_file_name)
        ValueAssert.value_assert_equal('Upload Successfully', get_status)
        ValueAssert.value_assert_equal('1', get_total)
        ValueAssert.value_assert_equal('1', get_success)
        ValueAssert.value_assert_equal('0', get_failed)
        ValueAssert.value_assert_equal(today, get_import_date)
        """关闭当前打开的导入记录菜单"""
        menu = LoginPage(drivers)
        menu.click_close_open_menu()

        """根据导入的客户ID，筛选导入的数据，然后进行删除操作"""
        upload.input_query_User('smarttest102')
        upload.click_search()

        """断言User Salary Management 页面，是否加载导入成的数据"""
        get_user_id1 = upload.get_text_user_id()
        get_user_name = upload.get_text_user_name()
        get_staff_status = upload.get_list_staff_status()
        get_brand = upload.get_list_brand()
        get_country = upload.get_list_country()
        get_position = upload.get_list_position()
        logging.info("打印获取用户管理列表User ID字段内容：{}".format(get_user_id1))
        logging.info("打印获取用户管理列表User Name字段内容：{}".format(get_user_name))
        logging.info("打印获取用户管理列表Staff Status字段内容：{}".format(get_staff_status))
        logging.info("打印获取用户管理列表Brand字段内容：{}".format(get_brand))
        logging.info("打印获取用户管理列表Country字段内容：{}".format(get_country))
        logging.info("打印获取用户管理列表Position字段内容：{}".format(get_position))
        ValueAssert.value_assert_equal('smarttest102', get_user_id1)
        ValueAssert.value_assert_equal('smart_test102', get_user_name)
        ValueAssert.value_assert_equal('On Service', get_staff_status)
        ValueAssert.value_assert_equal('TECNO', get_brand)
        ValueAssert.value_assert_equal('Bangladesh', get_country)
        ValueAssert.value_assert_equal('lhm店长', get_position)

        """ 在数据库表中，删除导入的用户 """
        sql1 = SQL('DCR', 'test')
        sql1.delete_db(
            "delete from t_user where USER_CODE ='smarttest102'")
        sql1.delete_db(
            "delete from t_employee where EMP_CODE ='smarttest102'")


# @allure.feature("员工授权-用户管理")
# class TestResetPasswordUser:
#     @allure.story("用户重置密码")
#     @allure.title("用户管理页面，筛选用户然后重置密码；然后使用重置的密码登录，设置新密码")
#     @allure.description("用户管理页面，筛选用户然后重置密码；然后使用重置的密码登录，设置新密码，最后新密码登录")
#     @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
#     def test_006_001(self, drivers):
#         """ lhmadmin管理员账号登录"""
#         user = LoginPage(drivers)
#         user.initialize_login(drivers, "lhmadmin", "dcr123456")
#
#         """用户授权-用户管理-查询用户管理列表数据用例"""
#         user.click_gotomenu("Staff & Authorization", "User Management")
#
#         reset = UserManagementPage(drivers)
#         reset.input_query_User('EG4463901')
#         reset.click_search()
#         reset.click_first_checkbox()
#         reset.click_more_reset_password()
#         """断言是否弹出设置成功提示"""
#         DomAssert(drivers).assert_att("Set Up Successfully")
#         sleep(1.5)
#         """重置密码成功后，使用该账号登录，设置新的密码"""
#         user.initialize_login(drivers, "EG4463901", "EG4463901")
#
#         """该用户登录时，弹出设置新密码窗口，输入新密码及确认新密码，点击保存"""
#         reset.input_new_password_save("dcr123456")
#         DomAssert(drivers).assert_att("Save successfully!")
#         reset.click_save_successfully_ok()
#
#         """弹出登录页面，输入新的密码，点击登录按钮"""
#         reset.input_login_password("dcr123456")
#         reset.click_login()
#         """验证登录成功后，页面是否存在首页菜单"""
#         DomAssert(drivers).assert_att("Home Page-Customer")


if __name__ == '__main__':
    pytest.main(['StaffAuthorization_UserManagement.py'])


