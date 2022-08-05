import allure
import pytest
from project.DRP.page_object.Center_Component import NavPage
from project.CRM.page_object.RC_BasicDataMgt_SymptomGroupMgt import SymPage
from public.base.assert_ui import ValueAssert
import random, string
import pytest, logging
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *
import datetime
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
num = string.ascii_letters + string.digits




@allure.feature("SymptomGroup") # 模块名称
class TestSymptomGroup:

    @pytest.fixture()
    def symp_fixture(self, drivers):
        logging.info("\n这个fixture在每个case前执行一次")
        user = SymPage(drivers)
        user.GoTo_Symp()  # 进入现象组页面
        yield
        logging.info("\n在每个case完成后执行的teardown")

    @allure.story("新增现象组")  # 场景名称,中文
    @allure.title("新增现象组")  # 用例名称
    @allure.description("新增现象组save成功，页面和数据库均有新增的数据")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.skip  # 跳过不执行
    def test_1269692(self, drivers, symp_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name = "".join(random.sample(num, 10))  # 名称使用随机数，以防重复名称添加失败
        user = SymPage(drivers)
        user.Add_Symp(name)  # 添加现象组
        get_record = user.Get_Symp(name)  # 查询添加成功
        ValueAssert.value_assert_equal(get_record, name)  # 判断查询与添加一致
        user = SQL('CRM', 'test')
        shop_data = user.query_db('select symptom_group_name from crm_mdm_symptom_group where symptom_group_name="{}"'.format(name))
        sql_get_name = shop_data[0].get("symptom_group_name")
        ValueAssert.value_assert_equal(sql_get_name, name)  # 判断新增数据存在于数据库
        # 将添加的数据从Enable修改为Disable，以免影响其他人使用；这里之所以带的是Enable，原因是因为它修改前元素定位里含Enable
        user = SymPage(drivers)
        user.Edit_Symp_Status("Enable")

    @allure.story("查询现象组")  # 场景名称
    @allure.title("Key Word精确查询、模糊查询成功")  # 用例名称
    @allure.description("Key Word精确查询、模糊查询成功")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.skip  # 跳过不执行
    def test_1269695(self, drivers, symp_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name = "".join(random.sample(num, 10))
        user = SymPage(drivers)
        user.Add_Symp(name)
        logging.info("步骤1：测试精确查询")
        get_record1 = user.Get_Symp(name)  # 精确查询成功
        ValueAssert.value_assert_equal(get_record1, name)  # 判断查询与输入条件一致
        user = SQL('CRM', 'test')
        symp_data = user.query_db('select symptom_group_name from crm_mdm_symptom_group where symptom_group_name="{}"'.format(name))
        sql_get_name = symp_data[0].get("symptom_group_name")
        ValueAssert.value_assert_equal(sql_get_name, name)  # 判断查询数据存在于数据库
        logging.info("步骤2：测试模糊查询")
        part_name = name[0:4]  # 取名称的前5位，用来模糊查询
        user = SymPage(drivers)
        get_record2 = user.Get_Symp(part_name)  # 模糊查询成功
        ValueAssert.value_assert_In(part_name, get_record2)         # 判断查询返回的名称包含查询的内容

        # 将添加的数据从Enable修改为Disable，以免影响其他人使用
        user = SymPage(drivers)
        user.Edit_Symp_Status("Enable")

    @allure.story("查询现象组")  # 场景名称
    @allure.title("Status查询框，遍历Enable、Disable查询成功")  # 用例名称
    @allure.description("Status查询框，遍历Enable、Disable查询成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.FT  # 用例标记
    @pytest.mark.skip  # 跳过不执行
    def test_1269694(self, drivers, symp_fixture):   # 遍历Satus查询框Enable\Disable查询
        logging.info("步骤1：Enable查询")
        user = SymPage(drivers)
        number1, get_record1 = user.Get_Enable_Status_Symp("Enable")  # 查询Enable的成功
        ValueAssert.value_assert_equal(get_record1, "Enable")  # 判断查询与输入条件一致
        user = SQL('CRM', 'test')
        group_data1 = user.query_db('select count(symptom_group_name) from crm_mdm_symptom_group where is_enable = 1')
        sql_data1 = str(group_data1[0].get("count(symptom_group_name)"))
        logging.info("页面查询出来的数据", number1)
        logging.info("数据库查询出来的数据为", sql_data1)
        ValueAssert.value_assert_equal(number1, sql_data1)  # 判断查询总的Enable数据与数据库里的一致

        logging.info("步骤2：Disable查询")
        user = SymPage(drivers)
        number2, get_record2 = user.Get_Disable_Status_Symp("Disable")  # 查询Disable的成功
        ValueAssert.value_assert_equal(get_record2, "Disable")  # 判断查询与输入条件一致
        user = SQL('CRM', 'test')
        group_data2 = user.query_db('select count(symptom_group_name) from crm_mdm_symptom_group where is_enable = 0')
        sql_data2 = str(group_data2[0].get("count(symptom_group_name)"))
        ValueAssert.value_assert_equal(number2, sql_data2)  # 判断查询总的Disable数据与数据库里的一致


    @allure.story("编辑现象组")  # 场景名称
    @allure.title("编辑现象组名称，save生效")  # 编辑现象组
    @allure.description("编辑现象组名称，save生效")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.FT  # 用例标记
    @pytest.mark.skip  # 跳过不执行
    def test_1269693(self, drivers, symp_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name = "".join(random.sample(num, 10))
        user = SymPage(drivers)
        user.Add_Symp(name)
        user.Get_Symp(name)  # 查询出来方便编辑
        update_name = name[1:9:2]
        user.Edit_Symp(update_name)  # 修改名称
        get_record = user.Get_Symp(update_name)
        ValueAssert.value_assert_equal(get_record, update_name)  # 用修改后的名称查询成功
        # 将添加的数据从Enable修改为Disable，以免影响其他人使用
        user = SymPage(drivers)
        user.Edit_Symp_Status("Enable")

    @allure.story("编辑现象组")  # 场景名称
    @allure.title("更改现象组状态，遍历Enable、Disable,均操作生效")  # 编辑现象组
    @allure.description("更改现象组状态，遍历Enable、Disable,均操作生效")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.FT  # 用例标记
    @pytest.mark.skip  # 跳过不执行
    def test_1272054(self, drivers, symp_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name = "".join(random.sample(num, 10))
        user = SymPage(drivers)
        user.Add_Symp(name)
        user.Get_Symp(name)  # 查询出来方便编辑
        logging.info("步骤1：将现象组状态修改为Disable")
        user = SymPage(drivers)
        user.Edit_Symp_Status("Enable")  # 修改状态为Disable,这里之所以带的是Enable，原因是因为它修改前元素定位里含Enable
        user = SQL('CRM', 'test')
        symp_data = user.query_db('select is_enable from crm_mdm_symptom_group where symptom_group_name="{}"'.format(name))
        sql_get_status = symp_data[0].get("is_enable")  # 通过数据库查询修改后的状态
        ValueAssert.value_assert_equal(sql_get_status, 0)  # 判断修改后的数据库此现象组的状态是为0（Disable）

        logging.info("步骤2：将现象组状态修改为Enable")
        user = SymPage(drivers)
        user.Edit_Symp_Status("Disable")  # 修改状态为Enable
        user = SQL('CRM', 'test')
        symp_data = user.query_db('select is_enable from crm_mdm_symptom_group where symptom_group_name="{}"'.format(name))
        sql_get_status = symp_data[0].get("is_enable")  # 通过数据库查询修改后的状态
        ValueAssert.value_assert_equal(sql_get_status, 1)  # 判断修改后的数据库此现象组的状态是为1（Enable）

        # 将添加的数据从Enable修改为Disable，以免影响其他人使用
        user = SymPage(drivers)
        user.Edit_Symp_Status("Enable")

    @allure.story("导出现象组")  # 场景名称
    @allure.title("导出现象组成功")  # 编辑现象组
    @allure.description("导出现象组成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.FT  # 用例标记
    #@pytest.mark.skip  # 跳过不执行
    def test_1272066(self, drivers, symp_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        user = SymPage(drivers)
        user.Export_Symp()  # 点击导出按钮
        user.GoTo_Task()   # 进入下载任务页面
        user.Download_Symp("Symptom_Group", "Symptom_Group_")  # 下载导出的excel，同时判断文件名正确


    @allure.story("添加现象组")  # 场景名称
    @allure.title("添加现象组后Created Date、CreatedBy、ModifiedOn、ModifiedBy字段值正确")  # 验证字段的值
    @allure.description("添加现象组后Created Date、CreatedBy、ModifiedOn、ModifiedBy字段值正确")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.FT  # 用例标记
    @pytest.mark.skip  # 跳过不执行
    def test_1272248(self, drivers, symp_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name = "".join(random.sample(num, 10))  # 名称使用随机数，以防重复名称添加失败
        user = SymPage(drivers)
        user.Add_Symp(name)  # 添加现象组
        created_date, created_by, modified_on, modified_by = user.Get_Symp_DATE_BY(name)  # 查询添加成功
        now_time = datetime.datetime.now()
        time1_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M')
        ValueAssert.value_assert_In(time1_str, created_date)     # 判断创建的时间约等于当前时间
        ValueAssert.value_assert_In(time1_str, modified_on)     # 判断修改的时间约等于当前时间
        ValueAssert.value_assert_equal(account[5]['username'], modified_by)  # 判断创建人等于当前登录用户
        ValueAssert.value_assert_equal(account[5]['username'], created_by)   # 判断修改人等于当前登录用户








if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
