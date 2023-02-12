import allure
import pytest
from project.CRM.page_object.OperationMgt_PolicyAndProfits_ProfitsTypeMgt import *
from project.CRM.page_object.Center_Component import *
from public.base.assert_ui import *
import logging
from project.CRM.page_object.OperationMgt_PolicyAndProfits_WarrantyDurationMgt import *
from project.CRM.page_object.OperationMgt_PolicyAndProfits_PolicyMgt import *
from project.CRM.page_object.OperationMgt_ProjectMgt import *


"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@pytest.fixture(scope='module' , autouse=True)  # 模块名称
def module_fixture(drivers):
    logging.info("模块前置条件，前往operation页面")
    user = NavPage(drivers)
    user.refresh_page()
    user.click_gotonav("OperationMgt", "ProjectMgt")  # 点击菜单
    user= DomAssert(drivers)
    user.assert_url("oprManagement/projectMgt")
    yield
    logging.info("后置条件：收起菜单")
    user = NavPage(drivers)
    user.click_gotonav("OperationMgt")

@allure.feature("Operation_PolicyMgt")  # 模块名称
class TestProjectMgt:
    @allure.story("ProjectMgt_项目管理")  # 场景名称
    @allure.title("项目管理页查询")  # 用例名称
    @allure.description("项目管理页对国家查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProjectPage(drivers)
        user.project_input_criteria(country="IN", brand=None, status=None)
        user.project_click_search()
        sleep(1)
        user = PolicyPage(drivers)
        number = user.get_total()
        user = ProjectPage(drivers)
        sql_num=user.project_sql_search(country="IN", brand=None, status=None)  # 查询sql 数据
        ValueAssert.value_assert_equal(sql_num, int(number))  # 页面数据和sql对比

    @allure.story("ProjectMgt_项目管理")  # 场景名称
    @allure.title("项目管理页查询")  # 用例名称
    @allure.description("项目管理页对brand查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProjectPage(drivers)
        user.project_input_criteria(country=None, brand="TECNO", status=None)
        user.project_click_search()
        sleep(1)
        user = PolicyPage(drivers)
        number = user.get_total()
        user = ProjectPage(drivers)
        sql_num=user.project_sql_search(country=None, brand="TECNO", status=None)  # 查询sql 数据
        ValueAssert.value_assert_equal(sql_num, int(number))  # 页面数据和sql对比

    @allure.story("ProjectMgt_项目管理")  # 场景名称
    @allure.title("项目管理页查询")  # 用例名称
    @allure.description("项目管理页对status查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProjectPage(drivers)
        user.project_input_criteria(country=None, brand=None, status="Enable")  # 输入查询条件
        user.project_click_search()
        sleep(1)
        user = PolicyPage(drivers)
        number = user.get_total()
        user = ProjectPage(drivers)
        sql_num=user.project_sql_search(country=None, brand=None, status="1")  # 查询sql 数据
        ValueAssert.value_assert_equal(sql_num, int(number))

    @allure.story("ProjectMgt_项目管理")  # 场景名称
    @allure.title("项目管理页查询")  # 用例名称
    @allure.description("项目管理页筛选项组合查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProjectPage(drivers)
        user.project_input_criteria(country="RW", brand="itel", status="Disable")  # 输入筛选条件
        user.project_click_search()
        sleep(1)
        user = PolicyPage(drivers)
        number = user.get_total()  # 获取页面total
        user = ProjectPage(drivers)
        sql_num=user.project_sql_search(brand="itel", status="0", country="RW")  # 查询sql 数据
        ValueAssert.value_assert_equal(sql_num, int(number))  # 页面数据和sql对比

    @allure.story("ProjectMgt_项目管理")  # 场景名称
    @allure.title("项目管理页新增正向")  # 用例名称
    @allure.description("项目管理页新增数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProjectPage(drivers)
        user.project_add()
        user.project_input(country="NG", category="TV", StartDate="2022-09-11", EndDate="2022-10-22", txt="DDDD")
        user.project_save()  # 新增数据
        sleep(0.5)
        att = user.get_txt()
        logging.info("文本是{}".format(att))
        if att == "Success":
            logging.info("断言成功并禁用数据")
            user = ProjectPage(drivers)
            user.disable()
        else:
            logging.info("数据重复关闭弹窗")
            user = ProjectPage(drivers)
            user.project_cancel()



    @allure.story("ProjectMgt_项目管理")  # 场景名称
    @allure.title("项目管理页新增异向")  # 用例名称
    @allure.description("项目管理页新增必填校验")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProjectPage(drivers)
        user.project_add()
        user.project_input(country="NG", category="TV", StartDate="2022-09-11", EndDate="2022-10-22", txt="")  # 新增页必填字段为空
        user.project_save()
        user = DomAssert(drivers)
        user.assert_exact_att("Project DescIt cannot be empty")  # 新增页校验必填字段提示
        user = ProjectPage(drivers)
        user.project_cancel()  # 关闭页面

    @allure.story("ProjectMgt_项目管理")  # 场景名称
    @allure.title("项目管理页新增")  # 用例名称
    @allure.description("项目管理页新增页重置")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_007(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProjectPage(drivers)
        user.project_add()
        user.project_input(country="NG", category="TV", StartDate="2022-09-11", EndDate="2022-10-22", txt="DDDD")
        user.project_reset()  # 重置输入内容
        user.project_save()
        user = DomAssert(drivers)
        user.assert_exact_att("Brand CategoryIt cannot be empty")  # 校验必填不能为空
        user = ProjectPage(drivers)
        user.project_cancel()

    @allure.story("ProjectMgt_项目管理")  # 场景名称
    @allure.title("项目管理页新增异向")  # 用例名称
    @allure.description("项目管理页新增数据结束时间大于开始时间")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_008(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProjectPage(drivers)
        user.project_add()
        user.project_input(country="NG", category="TV", StartDate="2022-09-11", EndDate="2022-08-22", txt="dddd")  # 输入错误的结束时间
        user.project_save()  # 点击save
        user = DomAssert(drivers)
        user.assert_exact_att("Project EOSIt cannot be empty")  # 提示时间不能为空
        user = ProjectPage(drivers)
        user.project_cancel()  # 关闭页面

    @allure.story("ProjectMgt_项目管理")  # 场景名称
    @allure.title("项目管理页编辑正向")  # 用例名称
    @allure.description("项目管理页编辑数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_009(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        text = user.get_Numbersletters()  # 获取要输入的文本
        logging.info("文本是{}".format(text))
        user = ProjectPage(drivers)
        user.project_edit()  # 进入编辑页
        user.project_input(country="", category="", StartDate="", EndDate="", txt=text)  # 修改字段
        user.project_editsave()
        user = DomAssert(drivers)
        user.assert_exact_att("Success")  # 校验保存成功
        user = ProjectPage(drivers)
        user.project_edit()  # 再次打开编辑页
        user = DomAssert(drivers)
        user.assert_exact_att(text)  # 确认页面上是否存在修改过的内容


    @allure.story("ProjectMgt_项目管理")  # 场景名称
    @allure.title("项目管理页编辑异向")  # 用例名称
    @allure.description("项目管理编辑页校验必填")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_010(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProjectPage(drivers)
        user.project_edit()  # 进入编辑页
        user.project_input(country="", category="", StartDate="", EndDate="", txt=" ")  # 输入空字符串
        user.project_editsave()
        user = DomAssert(drivers)
        user.assert_exact_att("projectDesc must not be blank")  # 校验必填为空
        user = ProjectPage(drivers)
        user.project_editcancel()







if __name__ == '__main__':
    pytest.main(['project/CRM/test_case/OperationMgt_PolicyAndProfits_ProfitsTypeMgt.py'])
