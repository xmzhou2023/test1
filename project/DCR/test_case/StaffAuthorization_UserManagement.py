from project.DCR.page_object.StaffAuthorization_UserManagement import UserManagementPage
from public.base.assert_ui import SQLAssert
from libs.common.connect_sql import *
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
import pytest
import allure


@allure.feature("员工授权-用户管理")
class TestAddEditQuitTranssionUser:
    @allure.story("用户管理业务流程")
    @allure.title("用户管理页面，新增、编辑、离职传音用户")
    @allure.description("用户管理页面，新增、编辑、离职传音用户")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    def test_001_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Staff & Authorization", "User Management")

        """新建传音员工账号 用例"""
        """随机生成数字"""
        user = UserManagementPage(drivers)
        userid = user.user_id_random()
        username = user.user_name_random()
        user.click_add_user()
        user.click_transsion_staff()
        user.input_user_id(userid)
        user.input_user_name(username)
        user.input_sales_region("Barisal")
        user.input_country_city("Barisal")
        user.click_select_brand()
        user.input_position_transsion("lhmTecno促销员")
        user.input_superior("lhmadmin")
        user.input_email("623536126@qq.com")
        num = user.user_id_random()
        user.input_contact_no("13762513" + num)
        user.click_gender_female()
        user.click_add_user_submit()

        user.click_search()
        """根据输入的Shop ID筛选新建的门店ID后，断言列表是否存在新建门店"""
        user.input_query_User(userid, userid)
        user.click_search()
        """首先根据新建的User ID筛选，然后获取列表新增的User ID，User name，进行断言比较是否存在新建的用户"""
        user_id = user.get_text_user_id()
        user_name = user.get_text_user_name()
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
        username = user.user_name_random()
        user.click_edit()
        user.input_user_name(username)
        user.click_edit_brand()
        user.input_email("646167867@qq.com")
        num = user.number_radom()
        user.input_contact_no("15814025" + num)
        user.click_add_user_submit()
        domassert = DomAssert(drivers)
        domassert.assert_att("Set Up Successfully")
        sleep(3)

        """调用断言 编辑的用户在列表是否更新成功"""
        """首先根据新建或编辑的User ID，然后获取列表新增的User ID，User name，进行断言比较是否存在新建的用户"""
        user_id1 = user.get_text_user_id()
        user_name = user.get_text_user_name()
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
        user.click_first_checkbox()
        user.click_more_option()
        user.click_quit()
        user.click_yes()
        """用户离职是否成功，断言"""
        domassert.assert_att("Disabled Successfully")
        #点击重置按钮，断言列表是否不存在被删除的用户
        user.click_reset()
        user_id2 = user.get_text_user_id()
        ValueAssert.value_assert_IsNot(user_id1, user_id2)
        user.click_close_user_mgt()


@allure.feature("员工授权-用户管理")
class TestAddEditQuitDealerUser:
    @allure.story("用户管理业务流程")
    @allure.title("用户管理页面，新增、编辑、离职代理用户")
    @allure.description("用户管理页面，新增、编辑、离职代理用户")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    def test_002_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Staff & Authorization", "User Management")

        """新建国包代理员工"""
        dealer_user = UserManagementPage(drivers)
        dealer_user.click_add_user()
        username = dealer_user.user_name_random()
        dealer_user.click_dealer_staff()
        dealer_user.input_belong_to_cust("UG4019912")
        dealer_user.input_user_name(username)
        dealer_user.input_sales_region("Barisal")
        dealer_user.input_country_city("Barisal")
        dealer_user.click_select_brand()
        dealer_user.input_position_dealer("lhm二代")
        dealer_user.input_email("646195353@163.com")
        num = dealer_user.number_radom()
        dealer_user.input_contact_no("13896785" + num)
        dealer_user.click_gender_female()
        dealer_user.click_add_user_submit()

        dealer_user.click_search()
        """筛选用户后，点击Search，进行断言门店列表是否存在新建的门店ID"""
        dealer_user.input_query_User(username, username)
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
        dealer_user.click_edit()
        dealer_user.input_user_name(username)
        dealer_user.click_edit_dealer_brand()
        dealer_user.input_email("656167855@qq.com")
        num = dealer_user.number_radom()
        dealer_user.input_contact_no("15814021" + num)
        dealer_user.click_add_user_submit()
        """编辑成功后，页面是否弹出编辑成功提示语"""
        domassert = DomAssert(drivers)
        domassert.assert_att("Set Up Successfully")
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
        dealer_user.click_more_option()
        dealer_user.click_quit()
        dealer_user.click_yes()
        """用户离职是否成功，断言"""
        dom = DomAssert(drivers)
        dom.assert_att("Disabled Successfully")
        """点击重置按钮，断言列表是否不存在被删除的用户"""
        dealer_user.click_reset()
        user_id2 = dealer_user.get_text_user_id()
        ValueAssert.value_assert_IsNot(user_id1, user_id2)
        dealer_user.click_close_user_mgt()


if __name__ == '__main__':
    pytest.main(['StaffAuthorization_UserManagement.py'])


