import allure
import pytest
from project.CRM.page_object.OperationMgt_PolicyAndProfits_WarrantyDurationMgt import *
from project.CRM.page_object.Center_Component import *
from public.base.assert_ui import *
import logging

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""
@pytest.fixture(scope='module' , autouse=True) # 模块名称
def module_fixture(drivers):
    logging.info("模块前置条件，前往operation页面")
    user = NavPage(drivers)
    user.refresh_page()  # 刷新菜单
    user.click_gotonav("OperationMgt", "PolicyandProfits", "WarrantyDurationMgt")  # 点击菜单
    user= DomAssert(drivers)
    user.assert_url("/policyAndProfits/warrantyDurationMgt")
    yield
    logging.info("后置条件：收起菜单")
    user = NavPage(drivers)
    user.click_gotonav("OperationMgt")

@allure.feature("政策与权益")  # 模块名称
class TestWarrantyDurationMgt:
    @allure.story("WarrantyDurationMgt")  # 场景名称
    @allure.title("页面筛选框查询")  # 用例名称
    @allure.description("筛选框KeyWord查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        classname = user.get_warrantyname()[1]
        user.search_data(classname, choice=classname)  # 在保修期限基础数据页筛选框进行搜索

    @allure.story("WarrantyDurationMgt")  # 场景名称
    @allure.title("异常场景重复数据校验")  # 用例名称
    @allure.description("点击ADD按钮新增一条已存在的数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        classname = user.get_warrantyname()[0]  # 获取已存在的classname值
        user.add_duplicate(classname)  # 新增一条已存在的数据
        user.click_save()
        user = DomAssert(drivers)
        user.assert_exact_att("Warranty duration already exists")  # 校验有重复错误提示
        user = OperationPage(drivers)
        user.click_cancel()  # 关闭弹窗

    @allure.story("WarrantyDurationMgt")  # 场景名称
    @allure.title("正向场景新增数据")  # 用例名称
    @allure.description("点击ADD按钮新增一条数据，校验新增成功后并禁用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_003(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        name = user.get_Numbers()  # 获取输入文本
        user.add_click()
        user.input_WarrantyDuration(txt=name)  # 新增一条数据
        user = SQL("CRM", "test")  # 链接数据库
        warranty_data = user.query_db('SELECT warranty_name FROM crm_mdm_warranty_duration WHERE warranty_name ="{}"'.format(name))
        sql_get_name = warranty_data[0].get("warranty_name")  # 执行sql后获取返回值的第一个值
        ValueAssert.value_assert_equal(sql_get_name , name)  # 校验获取的sql值与新增值相等
        user = OperationPage(drivers)
        user.disable()  # 新增数据点击禁用
        user = DomAssert(drivers)
        user.assert_exact_att("Disabled Successfully!")

    @allure.story("WarrantyDurationMgt")  # 场景名称
    @allure.title("异常场景新增数据校验")  # 用例名称
    @allure.description("新增页Duration Days只允许输入数字校验")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_004(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        name1 = user.get_Numbersletters()  # 获取输入文本
        user.add_click()
        user.input_WarrantyDuration(txt=name1)  # 新增一条异常数据
        user = DomAssert(drivers)
        user.assert_exact_att("Only positive integers greater than or equal to 0 can be entered!")  # 断言页面上存在报错提示
        user = OperationPage(drivers)
        user.click_cancel()  # 关闭新增弹窗

    @allure.story("WarrantyDurationMgt")  # 场景名称
    @allure.title("正向场景编辑数据")  # 用例名称
    @allure.description("点击编辑按钮进行编辑保存并禁用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_005(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        name = user.get_Numbers()
        user.add_click()  # 点击新增
        user.input_WarrantyDuration(txt=name)  # 新增一条数据
        user = SQL("CRM", "test")  # 链接数据库
        warranty_data = user.query_db('SELECT warranty_name FROM crm_mdm_warranty_duration WHERE warranty_name ="{}"'.format(name))
        sql_get_name = warranty_data[0].get("warranty_name")  # 执行sql后获取返回值的第一个值
        ValueAssert.value_assert_equal(sql_get_name , name)  # 校验获取的sql值与新增值相等
        user = OperationPage(drivers)
        user.edit()  # 编辑数据
        user.input_WarrantyDuration(txt=name)  # 输入正常文本，点击保存
        user.disable()  # 禁用数据
        user = DomAssert(drivers)
        user.assert_exact_att("Disabled Successfully!")

    @allure.story("WarrantyDurationMgt")  # 场景名称
    @allure.title("异常场景编辑时在durationdays输入非数字的文本数据")  # 用例名称
    @allure.description("点击编辑按钮进行编辑并禁用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_006(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        name = user.get_Numbers()
        user.add_click()  # 点击新增
        user.input_WarrantyDuration(txt=name)  # 新增一条数据并保存
        user = SQL("CRM", "test")  # 链接数据库
        warranty_data = user.query_db('SELECT warranty_name FROM crm_mdm_warranty_duration WHERE warranty_name ="{}"'.format(name))
        sql_get_name = warranty_data[0].get("warranty_name")  # 执行sql后获取返回值的第一个值
        ValueAssert.value_assert_equal(sql_get_name , name)  # 校验获取的sql值与新增值相等
        user = OperationPage(drivers)
        user.edit()  # 编辑数据
        name1=user.get_Numbersletters()
        user.input_WarrantyDuration(txt=name1)  # 输入错误文本，点击保存报错
        user = DomAssert(drivers)
        user.assert_exact_att("Only positive integers greater than or equal to 0 can be entered!")  # 断言页面上存在报错提示
        user = OperationPage(drivers)
        user.click_cancel()  # 关闭新增弹窗
        user.disable()  # 禁用数据
        user = DomAssert(drivers)
        user.assert_exact_att("Disabled Successfully!")

    @allure.story("WarrantyDurationMgt")  # 场景名称
    @allure.title("异常场景编辑时输入重复的数据")  # 用例名称
    @allure.description("点击编辑按钮进行编辑并提示有重复报错提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_007(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        user.edit()  # 编辑数据
        classname = user.get_warrantyname()[3]
        user.input_WarrantyDuration(txt=classname)  # 输入已存在数据
        user = DomAssert(drivers)
        user.assert_exact_att("Warranty duration already exists")  # 校验有重复错误提示
        user = OperationPage(drivers)
        user.click_cancel()  # 关闭弹窗


if __name__ == '__main__':

    pytest.main(['project/CRM/test_case/OperationMgt_PolicyAndProfits_WarrantyDurationMgt.py'])