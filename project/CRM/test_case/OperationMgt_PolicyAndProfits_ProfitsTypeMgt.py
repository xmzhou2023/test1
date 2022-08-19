import allure
import pytest
from project.CRM.page_object.OperationMgt_PolicyAndProfits_ProfitsTypeMgt import *
from project.CRM.page_object.Center_Component import *
from public.base.assert_ui import *
import logging
from project.CRM.page_object.OperationMgt_PolicyAndProfits_WarrantyDurationMgt import *

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@pytest.fixture(scope='module' , autouse=True) # 模块名称
def smodule_setup_fixture(drivers):
    logging.info("模块前置条件，前往operation页面")
    user = NavPage(drivers)
    user.click_gotonav("OperationMgt", "PolicyandProfits", "ProfitsTypeMgt")  # 点击菜单
    user= DomAssert(drivers)
    user.assert_url("policyAndProfits/profitsTypeMgt")

@allure.feature("Operation_ProfitsType") # 模块名称
class TestProfitsTypeMgt:
    @allure.story("ProfitsType") # 场景名称
    @allure.title("政策类型页点击keyword查询")  # 用例名称
    @allure.description("对keyword输入内容查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProfitsType(drivers)
        classname = user.get_columnValue()[2]
        user.search_data(classname,choice=classname)

    @allure.story("ProfitsType") # 场景名称
    @allure.title("政策类型页新增一条数据")  # 用例名称
    @allure.description("新增一条政策类型")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        user.add_click()  # 点击新增按钮
        txt = user.get_Numbersletters()  # 获取输入的文本值（数字+字母格式）
        user = ProfitsType(drivers)
        user.input_profitline(txt)  # 输入内容
        user = OperationPage(drivers)
        user.click_save()
        user = SQL("CRM", "test")  # 链接数据库
        warranty_data = user.query_db('SELECT profits_name FROM crm_mdm_profits_type WHERE profits_name = "{}"'.format(txt))
        sql_get_name = warranty_data[0].get("profits_name")  # 执行sql后获取返回值的第一个值
        ValueAssert.value_assert_equal(sql_get_name , txt)  # 校验获取的sql值与新增值相等
        user = OperationPage(drivers)
        user.disable()  # 禁用数据
        user = DomAssert(drivers)
        user.assert_exact_att("Disabled Successfully!")

    @allure.story("ProfitsType") # 场景名称
    @allure.title("政策类型页修改数据")  # 用例名称
    @allure.description("修改政策类型的数据")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_003(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        user.add_click()  # 点击新增按钮
        txt = user.get_Numbersletters()  # 获取输入的文本值（数字+字母格式）
        user = ProfitsType(drivers)
        user.input_profitline(txt)  # 输入内容
        user = OperationPage(drivers)
        user.click_save()
        user = SQL("CRM", "test")  # 链接数据库
        warranty_data = user.query_db('SELECT profits_name FROM crm_mdm_profits_type WHERE profits_name = "{}"'.format(txt))
        sql_get_name = warranty_data[0].get("profits_name")  # 执行sql后获取返回值的第一个值
        ValueAssert.value_assert_equal(sql_get_name , txt)  # 校验获取的sql值与新增值相等
        user = OperationPage(drivers)
        user.edit()  # 点击编辑按钮
        txt1 = user.get_Numbersletters()  # 获取输入文本
        user = ProfitsType(drivers)
        user.input_profitline(txt1)  # 输入文本
        user = OperationPage(drivers)
        user.click_save()  # 点击保存
        user.disable()  # 禁用数据
        user = DomAssert(drivers)
        user.assert_exact_att("Disabled Successfully!")  # 有禁用校验

    @allure.story("ProfitsType") # 场景名称
    @allure.title("政策类型页校验重复数据")  # 用例名称
    @allure.description("输入已存在的政策类型数据h校验重复")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_004(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        user.add_click()  # 点击新增按钮
        user  = ProfitsType(drivers)
        txt = user.get_columnValue()[2]  # 获取列表中下标2的文本
        user.input_profitline(txt)  # 输入文本内容
        user = OperationPage(drivers)
        user.click_save()
        user = DomAssert(drivers)
        user.assert_exact_att("Profits type name already exists")  # 有重复校验
        user = OperationPage(drivers)
        user.click_cancel()  # 关闭新增弹窗



if __name__ == '__main__':
    pytest.main(['project/CRM/test_case/OperationMgt_PolicyAndProfits_ProfitsTypeMgt.py'])
