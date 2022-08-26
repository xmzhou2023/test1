import allure
import pytest
from project.DRP.page_object.Center_Component import NavPage
from project.CRM.page_object.RC_BasicDataMgt_SymptomCodeMgt import SymCodePage
from project.CRM.page_object.RC_BasicDataMgt_SymptomGroupMgt import SymPage
from public.base.assert_ui import ValueAssert
import random, string
import pytest, logging
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *
from datetime import *
pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""
num = string.digits

@pytest.fixture(scope='module',autouse=True)
def module_fixture(drivers):
    logging.info("前往现象组组页面添加现象组")  # 添加现象码前需要现象组
    user = SymPage(drivers)
    user.GoTo_Symp()
    name_group = "".join(random.sample(num, 6))  # 名称使用随机数，以防重复名称添加失败
    user.Add_Symp(name_group)  # 添加现象码时需要现象组
    logging.info("前往RC中的Basic Data Mgt的Symptom Code Mgt")
    user = SymCodePage(drivers)
    user.Close_Page()  # 关闭现象组页面
    user.GoTo_Symp_Code()  # 进入现象码页面
    result = DomAssert(drivers)
    result.assert_url("/repairCenter/RPCbasicDataMgt/symptomCodeMgt")
    name_code = "".join(random.sample(num, 6))  # 名称使用随机数，以防重复名称添加失败
    name_description = "auto_test"+"".join(random.sample(num, 6))  # 名称使用随机数，以防重复名称添加失败
    user.Add_Symp_Code(name_code, name_group, name_description)
    yield name_code, name_group, name_description
    logging.info("\n在当前模块完成后执行的teardown")

    user = SQL('CRM', 'test')
    user.query_db(
        'delete  from crm_mdm_symptom where symptom_code="{}"'.format(name_code))
    user.query_db(
        'delete  from crm_mdm_symptom_group where symptom_group_name="{}"'.format(name_group))


@allure.feature("SymptomCode")  # 现象码页面
class TestAddSymptomCode:
    @pytest.fixture()
    def class_fixture(self, drivers):
        logging.info("\n这个fixture在每个case前执行一次")
        yield
        logging.info("\n在每个case完成后执行的teardown")
        user = SymCodePage(drivers)
        user.Code_Clear_Get()


    @allure.story("新增现象码")  # 场景名称,中文
    @allure.title("新增现象码save成功，页面和数据库均有新增的数据")  # 用例名称
    @allure.description("新增现象码save成功，页面和数据库均有新增的数据")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    #@pytest.mark.skip  # 跳过不执行
    def test_1035798(self, drivers, module_fixture, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name_code, _, _ = module_fixture  # 前置条件中已执行添加步骤，此用例只判断添加成功
        user = SymCodePage(drivers)
        get_record, _, _ = user.Get_Symp_Code(name_code)  # 查询添加成功
        ValueAssert.value_assert_equal(get_record, name_code)  # 判断查询与添加一致
        user = SQL('CRM', 'test')
        shop_data = user.query_db('select symptom_code from crm_mdm_symptom where symptom_code="{}"'.format(name_code))
        sql_get_name = shop_data[0].get("symptom_code")
        ValueAssert.value_assert_equal(sql_get_name, name_code)  # 判断新增数据存在于数据库

    @allure.story("新增现象码")  # 场景名称,中文
    @allure.title("X按钮：点击关闭该窗口")  # 用例名称
    @allure.description("X按钮：点击关闭该窗口")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.UT  # 用例标记
    #@pytest.mark.skip  # 跳过不执行
    def test_1035800(self, drivers, module_fixture, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name_code, get_record_group,_ = module_fixture  # 获取现象组用于添加现象码
        user = SymCodePage(drivers)
        name = "".join(random.sample(num, 6))  # 名称使用随机数
        name_description = "auto_test" + "".join(random.sample(num, 6))
        user.Add_Symp_Code_Not_Save(name, get_record_group, name_description)  # #打开添加页面，输入各项数据
        user.Close_Symp("Add")  # 关闭添加界面 ，添加不成功
        get_record = user.Get_No_Data(name)  # 查询
        ValueAssert.value_assert_equal(get_record, "No Data")  # 判断查询为空

    @allure.story("新增现象码")  # 场景名称,中文
    @allure.title("Code：必填项，校验唯一性，重复添加有报错")  # 用例名称
    @allure.description("Code：必填项，校验唯一性，重复添加有报错")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.UT  # 用例标记
    #@pytest.mark.skip  # 跳过不执行
    def test_1035793(self, drivers, module_fixture, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name_code, _, _ = module_fixture
        user = SymCodePage(drivers)
        get_record_name, get_record_group, _ = user.Get_Symp_Code(name_code)  # 查询已有的现象码
        repeat_tip = user.Repeat_Add_Code(get_record_name, get_record_group, "auto_add_repeat")  # 再次重复添加已有的现象码
        ValueAssert.value_assert_equal(repeat_tip, "Symptom code Data exist")  # 判断提示正确
        user.Close_Symp("Add")  # 关闭添加界面


@allure.feature("SymptomCode")  # 模块名称
class TestGetSymptomGroup:
    @pytest.fixture()
    def class_fixture(self, drivers):
        logging.info("\n这个fixture在每个case前执行一次")
        yield
        logging.info("\n在每个case完成后执行的teardown")
        user = SymCodePage(drivers)
        user.Code_Clear_Get()

    @allure.story("查询现象码")  # 场景名称
    @allure.title("Keyword：Code/Description 支持模糊查询")  # 用例名称
    @allure.description("Keyword：Code/Description 支持模糊查询")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    #@pytest.mark.skip  # 跳过不执行
    def test_1035789(self, drivers, module_fixture, class_fixture):  # 用例名称取名规范'test+场景编号+用例编号'
            name_code, name_group, description = module_fixture
            user = SymCodePage(drivers)
            logging.info("步骤1：测试精确查询code")
            get_record1, get_group, get_description = user.Get_Symp_Code(name_code)  # 精确查询成功
            ValueAssert.value_assert_equal(get_record1, name_code)  # 判断查询与输入条件一致
            user = SQL('CRM', 'test')
            shop_data = user.query_db(
                'select symptom_code  from crm_mdm_symptom where symptom_code="{}"'.format(name_code))
            sql_get_name = shop_data[0].get("symptom_code")
            ValueAssert.value_assert_equal(sql_get_name, get_record1)  # 判断查询数据存在于数据库
            logging.info("步骤2：测试精确查询description")
            user = SymCodePage(drivers)
            get_record2, get_group2, get_description2 = user.Get_Symp_Code(description)  # 精确查询成功
            ValueAssert.value_assert_equal(get_description2, description)  # 判断查询与输入条件一致
            user = SQL('CRM', 'test')
            shop_data = user.query_db(
                'select description  from crm_mdm_symptom where description="{}"'.format(description))
            sql_get_description1 = shop_data[0].get("description")
            ValueAssert.value_assert_equal(sql_get_description1, get_description2)  # 判断查询数据存在于数据库

            logging.info("步骤3：测试code模糊查询")
            part_name = name_code[0:4]  # 取名称的前5位，用来模糊查询
            user = SymCodePage(drivers)
            get_record3, _, _ = user.Get_Symp_Code(part_name)  # 模糊查询成功
            ValueAssert.value_assert_In(part_name, get_record2)  # 判断查询返回的名称包含查询的内容
            user = SQL('CRM', 'test')
            shop_data = user.query_db(
                'select symptom_code  from crm_mdm_symptom where symptom_code="{}"'.format(get_record3))
            sql_get_name = shop_data[0].get("symptom_code")
            ValueAssert.value_assert_equal(sql_get_name, get_record3)  # 判断查询数据存在于数据库

            logging.info("步骤4：测试description模糊查询")
            part_description = description[0:4]  # 取名称的前5位，用来模糊查询
            user = SymCodePage(drivers)
            get_record4, get_group4, get_description4 = user.Get_Symp_Code(part_description)  # 模糊查询成功
            ValueAssert.value_assert_In(part_description, get_description4)  # 判断查询返回的名称包含查询的内容
            user = SQL('CRM', 'test')
            shop_data = user.query_db(
                'select description  from crm_mdm_symptom where description="{}"'.format(get_description4))
            sql_get_description2 = shop_data[0].get("description")
            ValueAssert.value_assert_equal(sql_get_description2, get_description4)  # 判断查询数据存在于数据库

    @allure.story("查询现象码")  # 场景名称
    @allure.title("Status:Enable/Disable")  # 用例名称
    @allure.description("Status:Enable/Disable")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    #@pytest.mark.skip  # 跳过不执行
    def test_1035791(self, drivers):   # 遍历Satus查询框Enable\Disable查询
        logging.info("步骤1：Enable查询")
        user = SymCodePage(drivers)
        number1, get_record1, __ = user.Get_Enable_Status_Code("Enable")  # 查询Enable的成功
        ValueAssert.value_assert_equal(get_record1, "Enable")  # 判断查询与输入条件一致
        user = SQL('CRM', 'test')
        group_data1 = user.query_db('select count(symptom_code) from crm_mdm_symptom where is_enable = 1')
        sql_data1 = str(group_data1[0].get("count(symptom_code)"))
        ValueAssert.value_assert_equal(number1, sql_data1)  # 判断查询总的Enable数据与数据库里的一致

        logging.info("步骤2：Disable查询")
        user = SymCodePage(drivers)
        number2, get_record2 = user.Get_Disable_Status_Code("Disable")  # 查询Disable的成功
        ValueAssert.value_assert_equal(get_record2, "Disable")  # 判断查询与输入条件一致
        user = SQL('CRM', 'test')
        group_data2 = user.query_db('select count(symptom_code) from crm_mdm_symptom where is_enable = 0')
        sql_data2 = str(group_data2[0].get("count(symptom_code)"))
        ValueAssert.value_assert_equal(number2, sql_data2)  # 判断查询总的Disable数据与数据库里的一致
        ## 恢复为默认查询条件
        user = SymCodePage(drivers)
        user.Code_Clear_Get()


class TestExportSymptomCode:
    @allure.story("导出现象码")  # 场景名称
    @allure.title("导出现象码成功")  # 编辑现象组
    @allure.description("导出现象码成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip  # 跳过不执行
    def test_1272066(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = SymCodePage(drivers)
        user.Export_Symp()  # 点击导出按钮
        user.Close_Page()  # 关闭现象码页面
        user.GoTo_Task()   # 进入下载任务页面
        user.Download_Symp_Code("Symptom_Code", "Symptom_Code")  # 下载导出的excel，同时判断文件名正确

        user.Close_Page()  # 关闭下载页面
        user.GoTo_Symp_Code()  # 回到现象组页面





if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
