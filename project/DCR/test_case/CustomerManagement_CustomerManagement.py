import logging
import allure
import pytest
from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.CustomerManagement_CustomerManagement import CustomerManagementPage
from public.base.assert_ui import DomAssert, ValueAssert
from public.base.assert_ui import SQLAssert
from libs.common.connect_sql import *
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范) TestQueryGlobalCustomers
"""

@allure.feature("客户管理-客户管理(全球)") # 模块名称
class TestAddCustomer:
    @allure.story("新增客户")
    @allure.title("新增二代客户信息")
    @allure.description("新增客户操作成功，列表展示新增的客户信息")
    @allure.severity("normal")
    @pytest.mark.smoke   # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
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
        """第一个参数可为Distributor or Retailer,第二个参数为Customer Name,第三个为SAPID,第四个为Sales Region"""
        add_customer.input_form_basic_info('Sub-dealer', 'Infinix', 'TECNO', customer_name, '深圳')

        """第一个参数为testName,第二个为testNo,第三个为country,第四个为testAddress"""
        add_customer.input_form_contact_info(contact_name, contact_no, email, '深圳2', "南山区深圳湾生态园9B5")

        get_customer_id1 = add_customer.get_customer_id()
        sql = SQLAssert('DCR', 'test')
        sql.assert_sql(get_customer_id1, "select enterprise_code from t_enterprise  where created_by='lhmadmin' order by created_time desc limit 1")

        """筛选新增的客户ID，然后断言客户id、客户name、品牌、联系人、联系电话是否正确"""
        add_customer.input_customer_query(get_customer_id1)
        add_customer.click_search()

        get_customer_id2 = add_customer.get_customer_id()
        get_customer_name = add_customer.get_customer_name()
        get_brand = add_customer.get_brand()

        ValueAssert.value_assert_equal(get_customer_id1, get_customer_id2)
        ValueAssert.value_assert_equal(get_customer_name, customer_name)
        ValueAssert.value_assert_equal("Infinix,TECNO", get_brand)

        get_contact_name = add_customer.get_contact_name()
        get_contact_no = add_customer.get_contact_no()
        get_customer_type = add_customer.get_customer_type('Sub-dealer')

        ValueAssert.value_assert_equal(contact_name, get_contact_name)
        ValueAssert.value_assert_equal(contact_no, get_contact_no,)
        ValueAssert.value_assert_equal("Sub-dealer", get_customer_type)
        add_customer.click_close_customer_mgt()


@allure.feature("客户管理-客户管理(全球)")  #  模块名称
class TestEditCustomer:
    @allure.story("编辑客户")
    @allure.title("编辑二代客户信息")
    @allure.description("编辑客户操作成功，列表筛选该客户ID，客户名称更新为编辑后的信息")
    @allure.severity("normal")
    @pytest.mark.smoke   # 用例标记
    def test_002_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
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
        edit.click_close_customer_mgt()


@allure.feature("客户管理-客户管理(全球)") # 模块名称
class TestDeleteCustomer:
    @allure.story("删除客户")
    @allure.title("删除新建的二代客户信息")
    @allure.description("删除新建的二代客户成功后，列表不展示被删除的客户信息")
    @allure.severity("normal")
    @pytest.mark.smoke   # 用例标记
    def test_003_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        """登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开客户管理菜单"""
        user.click_gotomenu("Customer Management", "Customer Management(Global)")

        delete = CustomerManagementPage(drivers)

        """从数据库查询最近新建的门店ID"""
        user = SQL('DCR', 'test')
        customer_data = user.query_db(
            "select enterprise_code from t_enterprise  where created_by='lhmadmin' order by created_time desc limit 1")
        customer_id = customer_data[0].get("enterprise_code")
        logging.info("从数据库查询Customer ID：{}".format(customer_id))

        """筛选新增的客户ID，然后删除此客户记录"""
        delete.input_customer_query(customer_id)
        delete.click_search()

        """删除新建的客户"""
        delete.delete_customer()
        DomAssert(drivers).assert_att('Successfully')
        delete.click_reset()

        """前端断言，获取列表第一条客户ID，与删除前的客户ID比较，列表不存在删除后的Customer ID"""
        get_customer_id = delete.get_customer_id()
        logging.info("获取列表第一行Customer ID：{}".format(get_customer_id))
        ValueAssert.value_assert_InNot(get_customer_id, customer_id)
        delete.click_close_customer_mgt()


# @allure.feature("客户管理-客户管理(全球)") # 模块名称
# class TestExportCustomer:
#     @allure.story("导出客户")
#     @allure.title("导出筛选后的客户信息")
#     @allure.description("导出筛选后的客户信息，验证导出功能是否正常")
#     @allure.severity("normal")
#     @pytest.mark.smoke   # 用例标记
#     def test_004_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
#         """登录"""
#         user = LoginPage(drivers)
#         user.initialize_login(drivers, "lhmadmin", "dcr123456")
#         """打开客户管理菜单"""
#         user.click_gotomenu("Customer Management", "Customer Management(Global)")
#
#         export = CustomerManagementPage(drivers)




if __name__ == '__main__':
    pytest.main(['CustomerManagement_CustomerManagement.py'])
