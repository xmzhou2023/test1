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
num = string.ascii_letters + string.digits

@pytest.fixture(scope='module',autouse=True)
def module_setup_fixture(drivers):
    logging.info("前往RC中的Basic Data Mgt的Symptom Group Mgt")
    user = SymPage(drivers)
    user.GoTo_Symp()  # 进入现象组页面
    result = DomAssert(drivers)
    result.assert_url("/repairCenter/RPCbasicDataMgt/SymptomGroupMgt")
    name = "".join(random.sample(num, 10))  # 名称使用随机数，以防重复名称添加失败
    user.Add_Symp(name)
    return name


@allure.feature("SymptomGroup") # 模块名称
class TestSymptomGroup:
    @pytest.fixture()
    def class_fixture(self, drivers):
        logging.info("\n这个fixture在每个case前执行一次")
        yield
        logging.info("\n在每个case完成后执行的teardown")
        user = SymPage(drivers)
        user.Clear_Get()


    @allure.story("新增现象组")  # 场景名称,中文
    @allure.title("新增现象组")  # 用例名称
    @allure.description("新增现象组save成功，页面和数据库均有新增的数据")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    #@pytest.mark.skip  # 跳过不执行
    def test_1269692(self, drivers, module_setup_fixture, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name = module_setup_fixture  # 前置条件中已执行添加步骤，此用例只判断添加成功
        user = SymPage(drivers)
        get_record = user.Get_Symp(name)  # 查询添加成功
        ValueAssert.value_assert_equal(get_record, name)  # 判断查询与添加一致
        user = SQL('CRM', 'test')
        shop_data = user.query_db('select symptom_group_name from crm_mdm_symptom_group where symptom_group_name="{}"'.format(name))
        sql_get_name = shop_data[0].get("symptom_group_name")
        ValueAssert.value_assert_equal(sql_get_name, name)  # 判断新增数据存在于数据库






if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
