from project.DCR.page_object.StaffAuthorization_UserManagement import UserManagementPage
from public.base.assert_ui import SQLAssert
from libs.common.connect_sql import *
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
import random
import pytest
import allure


@allure.feature("员工授权-用户管理")
class TestAddEditQuitTranssionUser():
    @allure.story("业务流程")
    @allure.title("用户管理页面，新增、编辑、离职传音用户")
    @allure.description("用户管理页面，新增、编辑、离职传音用户")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")
        sleep(5)
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Staff & Authorization", "User Management")
        sleep(5)
        """新建传音员工账号 用例"""
        """随机生成数字"""
        user = UserManagementPage(drivers)
        userid = user.user_id_random()
        username = user.user_name_random()
        num = str(random.randint(1, 100))
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
        user.input_contact_no("138625134" + num)
        user.click_gender_female()
        user.click_add_user_submit()
        sleep(1)
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
        userid = user.get_text_user_id()
        """筛选用户后，点击Search，进行编辑"""
        user.input_query_User(userid, userid)
        user.click_search()
        num = str(random.randint(1, 100))
        username = user.user_name_random()
        sleep(1)
        user.click_edit()
        user.input_user_name(username)
        user.click_edit_brand()
        user.input_email("646167867@qq.com")
        user.input_contact_no("158140253" + num)
        user.click_add_user_submit()
        """调用断言 编辑的用户在列表是否更新成功"""
        """首先根据新建或编辑的User ID，然后获取列表新增的User ID，User name，进行断言比较是否存在新建的用户"""
        user_id = user.get_text_user_id()
        user_name = user.get_text_user_name()
        """断言修改后的用户名是否存在相同值"""
        ValueAssert.value_assert_equal(user_name, username)
        """查询数据库用户表的userid,username是否存在断言"""
        sqlasser = SQLAssert('DCR', 'test')
        sqlasser.assert_sql(user_id,
                            "select USER_CODE from t_user where created_by = 'lhmadmin' order by created_time desc limit 1")
        sqlasser.assert_sql(user_name,
                            "select USER_NAME from t_user where created_by= 'lhmadmin'  order by created_time desc limit 1")
        sleep(1)

        """ 离职传音用户 """
        userid1 = user.get_text_user_id()
        user.click_first_checkbox()
        user.click_more_option()
        user.click_quit()
        user.click_yes()
        #sleep(0.5)
        """用户离职是否成功，断言"""
        #success = user.get_text_delete_success()
        DomAssert.assert_exact_att("Disabled Successfully")
        # 点击重置按钮，断言列表是否不存在被删除的用户
        user.click_reset()
        userid2 = user.get_text_user_id()
        ValueAssert.value_assert_IsNot(userid1, userid2)
        sleep(1)
        user.click_close_user_mgt()
        sleep(2)


@allure.feature("员工授权-用户管理")
class TestAddEditQuitDealerUser():
    @allure.story("业务流程")
    @allure.title("用户管理页面，新增、编辑、离职代理用户")
    @allure.description("用户管理页面，新增、编辑、离职代理用户")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """销售管理菜单-出库单-筛选出库单用例"""
        menu = LoginPage(drivers)
        menu.click_gotomenu("Staff & Authorization", "User Management")
        sleep(5)
        """新建国包代理员工"""
        dealer_user = UserManagementPage(drivers)
        num = str(random.randint(1, 100))
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
        dealer_user.input_contact_no("138625134" + num)
        dealer_user.click_gender_female()
        dealer_user.click_add_user_submit()
        sleep(1)
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
        userid = dealer_user.get_text_user_id()
        """筛选用户后，点击Search，进行编辑操作"""
        dealer_user.input_query_User(userid, userid)
        dealer_user.click_search()
        num = str(random.randint(1, 100))
        username = dealer_user.user_name_random()
        sleep(1)
        dealer_user.click_edit()

        dealer_user.input_user_name(username)
        dealer_user.click_edit_dealer_brand()
        dealer_user.input_email("656167855@qq.com")
        dealer_user.input_contact_no("158140258" + num)
        dealer_user.click_add_user_submit()
        sleep(2)
        """调用断言 编辑的用户在列表是否更新成功"""
        """首先根据新建或编辑的User ID，然后获取列表新增的User ID，User name，进行断言比较是否存在新建的用户"""
        user_id = dealer_user.get_text_user_id()
        user_name = dealer_user.get_text_user_name()
        """断言修改后的用户名是否存在相同值"""
        ValueAssert.value_assert_equal(user_name, username)

        """查询数据库用户表的userid,username是否存在断言"""
        sqlasser = SQLAssert('DCR', 'test')
        sqlasser.assert_sql(user_id,
                            "select u.USER_CODE  from  t_user as u,t_employee as e  where  u.ID=e.U_ID  and  e.created_by='lhmadmin'  order by e.created_time desc limit 1")
        sqlasser.assert_sql(user_name,
                            "select u.USER_NAME  from  t_user as u,t_employee as e  where  u.ID=e.U_ID  and  e.created_by='lhmadmin'  order by e.created_time desc limit 1")
        sleep(1)

        """ 离职代理员工 """
        userid1 = dealer_user.get_text_user_id()
        dealer_user.click_first_checkbox()
        dealer_user.click_more_option()
        dealer_user.click_quit()
        dealer_user.click_yes()
        """用户离职是否成功，断言"""
        #success = dealer_user.get_text_delete_success()
        DomAssert.assert_exact_att("Disabled Successfully")
        """点击重置按钮，断言列表是否不存在被删除的用户"""
        dealer_user.click_reset()
        userid2 = dealer_user.get_text_user_id()
        ValueAssert.value_assert_IsNot(userid1, userid2)
        sleep(1)

if __name__ == '__main__':
    pytest.main(['StaffAuthorization_UserManagement.py'])


