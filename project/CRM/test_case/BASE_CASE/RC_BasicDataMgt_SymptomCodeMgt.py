import allure
import pytest
from project.DRP.page_object.Center_Component import NavPage
from project.CRM.page_object.RC_BasicDataMgt_SymptomCodeMgt import SymCodePage
from project.CRM.page_object.RC_BasicDataMgt_SymptomGroupMgt import SymPage
from project.CRM.page_object.Center_Component import NavPage
from public.base.assert_ui import ValueAssert
import random, string
import pytest, logging
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *
from datetime import *
pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import math
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
    user = SymCodePage(drivers)
    user.GoTo_refresh()
    user = NavPage(drivers)
   # user.refresh_page()
    user.list_search(content='Symptom Group Mgt')
    user = SymPage(drivers)
   # user.GoTo_Symp()
    name_group = "".join(random.sample(num, 6))  # 名称使用随机数，以防重复名称添加失败
    user.Add_Symp(name_group)  # 添加现象码时需要现象组
    logging.info("前往RC中的Basic Data Mgt的Symptom Code Mgt")
    user = SymCodePage(drivers)
    user.Close_Page()  # 关闭现象组页面
    user = SymCodePage(drivers)
    user.GoTo_refresh()
    user = NavPage(drivers)
   # user.refresh_page()
    user.list_search(content='Symptom Code Mgt')
    #user.GoTo_Symp_Code()  # 进入现象码页面
    result = DomAssert(drivers)
    result.assert_url("/repairCenter/RPCbasicDataMgt/symptomCodeMgt")
    name_code = "".join(random.sample(num, 6))  # 名称使用随机数，以防重复名称添加失败
    name_description = "auto_test"+"".join(random.sample(num, 6))  # 描述使用随机数，以防重复名称添加失败
    user = SymCodePage(drivers)
    user.Add_Symp_Code(name_code, name_group, name_description)
    yield name_code, name_group, name_description
    logging.info("\n在当前模块完成后执行的teardown")
    # 删除添加的数据，恢复环境
    user = SQL('CRM', 'test')
    user.query_db(
        'delete  from crm_mdm_symptom where symptom_code="{}"'.format(name_code))
    user.query_db(
        'delete  from crm_mdm_symptom_group where symptom_group_name="{}"'.format(name_group))
    logging.info("后置条件:合起菜单")
    user = SymCodePage(drivers)
    user.Close_Page()  # 关闭页面
    user = SymPage(drivers)
    user.Close_Up_First_Menu("Repair Center")  # 合起菜单



@allure.feature("SymptomCode")  # 现象码页面
class TestAddSymptomCode:
    @pytest.fixture(scope='module',autouse=True)
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
    def test_1617(self, drivers, module_fixture, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
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
    def test_1618(self, drivers, module_fixture, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name_code, get_record_group, _ = module_fixture  # 获取现象组用于添加现象码
        user = SymCodePage(drivers)
        name = "".join(random.sample(num, 6))  # 名称使用随机数
        name_description = "auto_test" + "".join(random.sample(num, 6))
        user.Add_Symp_Code_Not_Save(name, get_record_group, name_description)  # #打开添加页面，输入各项数据
        user.Close_Symp("Add")  # 关闭添加界面 ，添加不成功
        get_record = user.Get_No_Data(name)  # 查询
        ValueAssert.value_assert_equal(get_record, "No Data")  # 判断查询为空


    @allure.story("新增现象码")  # 场景名称,中文
    @allure.title("Save&Add按钮：点击后校验并保存记录，窗口清空")  # 用例名称
    @allure.description("Save&Add按钮：点击后校验并保存记录，窗口清空")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.UT  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_1619(self, drivers, module_fixture, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name_code, get_record_group, _ = module_fixture  # 获取现象组用于添加现象码
        user = SymCodePage(drivers)
        name = "".join(random.sample(num, 6))  # 名称使用随机数
        name_description = "auto_test" + "".join(random.sample(num, 6))
        user.SaveAdd_Symp_Code(name, get_record_group, name_description)  # #打开添加页面，输入各项数据
        code_null_tip, grouping_null_tip, description_tip = user.All_Is_Empty()
        ValueAssert.value_assert_In("CodeCannot Be Empty", code_null_tip)  # 判断Save&Add按钮点击后窗口有清空
        ValueAssert.value_assert_In("GroupingCannot Be Empty", grouping_null_tip)  # 判断Save&Add按钮点击后窗口清空
        ValueAssert.value_assert_In("description is required", description_tip)  # 判断Save&Add按钮点击后窗口清空
        user.Close_Code("Add")  # 关闭添加界面
        get_record, _, _ = user.Get_Symp_Code(name)  # 查询添加成功
        ValueAssert.value_assert_equal(get_record, name)  # 判断查询与添加一致
        # 删除添加的code，恢复环境
        user = SQL('CRM', 'test')
        user.query_db(
            'delete  from crm_mdm_symptom where symptom_code="{}"'.format(name))


    @allure.story("新增现象码")  # 场景名称,中文
    @allure.title("Grouping:必填项，取值》Symptom Group Mgt的有效的Grouping")  # 用例名称
    @allure.description("Grouping:必填项，取值》Symptom Group Mgt的有效的Grouping")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.UT  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_1620(self, drivers, module_fixture, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name_code, get_record_group, _ = module_fixture  # 获取现象组用于添加现象码
        user = SymCodePage(drivers)
        user.Close_Page()  # 关闭页面
        user = SymPage(drivers)
        user.Close_Up_First_Menu("Repair Center")  # 合起菜单
       # user.GoTo_Symp()
        user = SymCodePage(drivers)
        user.GoTo_refresh()
        user = NavPage(drivers)
       # user.refresh_page()
        user.list_search(content='Symptom Group Mgt')
        name_group1 = "".join(random.sample(num, 6))  # 名称使用随机数，以防重复名称添加失败
        user = SymPage(drivers)
        user.Add_Symp(name_group1)
        logging.info("步骤1：添加界面，Grouping下拉框能搜索出Symptom Group Mgt的enable的Grouping")
        user = SymCodePage(drivers)
        user.Close_Page()  # 关闭页面
        #user.GoTo_Symp_Code()  # 进入现象码页面
        user = SymCodePage(drivers)
        user.GoTo_refresh()
        user = NavPage(drivers)
       # user.refresh_page()
        user.list_search(content='Symptom Code Mgt')
        user = SymCodePage(drivers)
        group_name1 = user.Add_Interface_Grouping(get_record_group)  # 添加界面搜索前置条件中的group
        ValueAssert.value_assert_equal(group_name1, get_record_group)  # Grouping下拉框能搜索出的group名称正确
        user.Close_Symp("Add")  # 关闭添加界面
        group_name2 = user.Add_Interface_Grouping(name_group1)  # 添加界面搜索刚刚添加的group
        ValueAssert.value_assert_equal(group_name2, name_group1)  # Grouping下拉框能搜索出的group名称正确
        user.Close_Symp("Add")  # 关闭添加界面
        logging.info("步骤2：添加界面，Grouping下拉框无法搜索出Symptom Group Mgt的disable的Grouping")
        user = SymPage(drivers)
        user.Close_Page()  # 关闭页面
        #user.GoTo_Symp()  # 进入现象组页面
        user = SymCodePage(drivers)
        user.GoTo_refresh()
        user = NavPage(drivers)
      #  user.refresh_page()
        user.list_search(content='Symptom Group Mgt')
        user = SymPage(drivers)
        user.Get_Symp(name_group1)
        user.Edit_Symp_Status("Enable")  # 将group disable
        user = SymCodePage(drivers)
        user.Close_Page()  # 关闭页面
        user = SymCodePage(drivers)
        user.GoTo_refresh()
        user = NavPage(drivers)
       # user.refresh_page()
        user.list_search(content='Symptom Code Mgt')
        user = SymCodePage(drivers)
        #user.GoTo_Symp_Code()  # 进入现象码页面
        group_name1 = user.Add_No_Grouping(name_group1)  # 添加界面搜索状态为disable的grouping
        logging.info(group_name1)
        ValueAssert.value_assert_equal(group_name1, "No data")  # 搜索无数据
        # 恢复环境
        user.Close_Code("Add")  # 关闭添加界面
        # 删除添加的code
        user = SQL('CRM', 'test')
        user.query_db(
            'delete  from crm_mdm_symptom_group where symptom_group_name="{}"'.format(name_group1))



    @allure.story("新增现象码")  # 场景名称,中文
    @allure.title("Code：必填项，校验唯一性，重复添加有报错")  # 用例名称
    @allure.description("Code：必填项，校验唯一性，重复添加有报错")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.UT  # 用例标记
    #@pytest.mark.skip  # 跳过不执行
    def test_1621(self, drivers, module_fixture, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name_code, _, _ = module_fixture
        user = SymCodePage(drivers)
        get_record_name, get_record_group, _ = user.Get_Symp_Code(name_code)  # 查询已有的现象码
        repeat_tip = user.Repeat_Add_Code(get_record_name, get_record_group, "auto_add_repeat")  # 再次重复添加已有的现象码
        ValueAssert.value_assert_equal(repeat_tip, "Symptom code Data exist")  # 判断提示正确
        user.Close_Symp("Add")  # 关闭添加界面

    @allure.story("新增现象码")  # 场景名称
    @allure.title("CreatedBy：显示名字；CreatedOn：取值创建时间，精确到秒")  # 验证字段的值
    @allure.description("CreatedBy：显示名字；CreatedOn：取值创建时间，精确到秒")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_1622(self, module_fixture, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        name_code, name_group, _ = module_fixture
        user = SymCodePage(drivers)
        name_code2 = "".join(random.sample(num, 10))  # 名称使用随机数，以防重复名称添加失败
        name_description = "auto_test" + "".join(random.sample(num, 6))  # 描述使用随机数，以防重复名称添加失败
        user.Add_Symp_Code(name_code2, name_group, name_description)
        created_date, created_by, modified_on, modified_by = user.Get_Code_DATE_BY(name_code2)  # 查询添加的时间、和创建人
        now_time = datetime.now()  # 获取当前时间
        created_date_linux = datetime.strptime(created_date, '%Y-%m-%d %H:%M:%S')+timedelta(hours=8)  # Linux的时间少8个小时,需要加上
        created_date1 = datetime.strptime(created_date, '%Y-%m-%d %H:%M:%S')
        logging.info(created_date1)
        time_difference = int((now_time - created_date1).total_seconds())  # 获取时间差
        time_difference_linux = int((now_time - created_date_linux).total_seconds())  # 获取linux环境时间差
        time_difference1 =math.fabs(time_difference)
        time_difference2 =math.fabs(time_difference_linux)
        logging.info(time_difference1)
        logging.info(type(time_difference1))

        if time_difference1 <= 60:
            logging.info("断言成功: 创建时间与当前时间相差没超过1分钟 | 创建时间:{} 当前时间:{}".format(created_date1, now_time))
        elif time_difference2 <= 60:
            logging.info("断言成功: 创建时间与当前时间相差没超过1分钟 | 创建时间:{} 当前时间:{}".format(created_date_linux, now_time))
        else:
            logging.warning("创建时间与当前时间相差超过1分钟 | 创建时间:{} 当前时间:{}".format(created_date1, now_time))
            assert False, '创建时间与当前时间相差超过1分钟'

        ValueAssert.value_assert_equal(account[7]['username'], created_by)  # 判断创建人等于当前登录用户
        # 删除添加的code，恢复环境
        user = SQL('CRM', 'test')
        user.query_db(
            'delete  from crm_mdm_symptom where symptom_code="{}"'.format(name_code2))



@allure.feature("SymptomCode")  # 模块名称
class TestGetSymptomGroup:
    @pytest.fixture(scope='module',autouse=True)
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
   # @pytest.mark.skip  # 跳过不执行
    def test_1623(self, drivers, module_fixture, class_fixture):  # 用例名称取名规范'test+场景编号+用例编号'
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
    def test_1301(self, drivers):   # 遍历Satus查询框Enable\Disable查询
        logging.info("步骤1：Enable查询")
        user = SymCodePage(drivers)
        total1, current_num1, get_record1 = user.Get_Status_Code("Enable")  # 查询Enable的成功
        for i in range(0, current_num1):
            ValueAssert.value_assert_equal(get_record1[i], "Enable")  ##判断查询出来的数据状态为Enable
        # user = SQL('CRM', 'test')
        # group_data1 = user.query_db('select count(symptom_code) from crm_mdm_symptom where is_enable = 1')
        # sql_data1 = str(group_data1[0].get("count(symptom_code)"))
        # ValueAssert.value_assert_equal(total1, sql_data1)  # 判断查询总的Enable数据与数据库里的一致
        logging.info("步骤2：Disable查询")
        user = SymCodePage(drivers)
        total2, current_num2, get_record2 = user.Get_Status_Code("Disable")  # 查询Disable的成功
        for i in range(0, current_num2):
            ValueAssert.value_assert_equal(get_record2[i], "Disable")  ##判断查询出来的数据状态为Disable

        # user = SQL('CRM', 'test')
        # group_data2 = user.query_db('select count(symptom_code) from crm_mdm_symptom where is_enable = 0')
        # sql_data2 = str(group_data2[0].get("count(symptom_code)"))
        # ValueAssert.value_assert_equal(total2, sql_data2)  # 判断查询总的Disable数据与数据库里的一致
        ## 恢复为默认查询条件
        user = SymCodePage(drivers)
        user.Code_Clear_Get()

    @allure.story("查询现象码")  # 场景名称
    @allure.title("列表各个字段名称正确")  # 用例名称
    @allure.description("列表各个字段名称正确")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_1625(self, drivers):   # 校验列表各个字段名称正确
        logging.info("步骤1：校验列表各个字段名称正确")
        user = SymCodePage(drivers)
        num, list_data = user.Get_List_Header()
        logging.info(num)
        logging.info(list_data)
        list_expect_data = ['Seq', 'Operate', 'Code', 'Description', 'Grouping', 'CreatedOn', 'CreatedBy', 'ModifiedOn', 'ModifiedBy']
        ValueAssert.value_assert_equal(num, 9)
        for i in range(0, num):
            ValueAssert.value_assert_equal(list_data[i], list_expect_data[i])



@allure.feature("SymptomCode")
class TestEditSymptomCode:
    @pytest.fixture(scope='module',autouse=True)
    def class_fixture(self, drivers):
        logging.info("\n这个fixture在每个case前执行一次")
        yield
        logging.info("\n在每个case完成后执行的teardown")
        user = SymCodePage(drivers)
        user.Code_Clear_Get()

    @allure.story("编辑现象码")  # 场景名称
    @allure.title("编辑现象码，修改Enable/Disable状态成功")  # 编辑现象组
    @allure.description("编辑现象码，修改Enable/Disable状态成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_1302(self, drivers, module_fixture, class_fixture):  # 用例名称取名规范'test+场景编号+用例编号'
        name_code, _, _ = module_fixture
        user = SymCodePage(drivers)
        user.Get_Symp_Code(name_code)  # 查询出来方便编辑
        logging.info("步骤1：将现象码状态修改为Disable")
        user = SymCodePage(drivers)
        user.Edit_Code_Status("Enable")  # 修改状态为Disable,这里之所以带的是Enable，原因是因为它修改前元素定位里含Enable
        user = SQL('CRM', 'test')
        code_data = user.query_db(
            'select is_enable from crm_mdm_symptom where symptom_code="{}"'.format(name_code))
        sql_get_status = code_data[0].get("is_enable")  # 通过数据库查询修改后的状态
        ValueAssert.value_assert_equal(sql_get_status, 0)  # 判断修改后的数据库此现象组的状态是为0（Disable）

        logging.info("步骤2：将现象码状态修改为Enable")
        user = SymCodePage(drivers)
        user.Get_Disable_Status_Code("Disable")  # 查询Disable的成功
        user.Edit_Code_Status("Disable")  # 修改状态为Enable
        user = SQL('CRM', 'test')
        code_data = user.query_db(
            'select is_enable from crm_mdm_symptom where symptom_code="{}"'.format(name_code))
        sql_get_status = code_data[0].get("is_enable")  # 通过数据库查询修改后的状态
        ValueAssert.value_assert_equal(sql_get_status, 1)  # 判断修改后的数据库此现象组的状态是为1（Enable）

    @allure.story("编辑现象码")  # 场景名称
    @allure.title("Edit按钮：显示同新增，Code的值置灰不可改动，其余字段可修改")  # 编辑现象组
    @allure.description("Edit按钮：显示同新增，Code的值置灰不可改动，其余字段可修改")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_1626(self, drivers, module_fixture, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        name_code1, name_group, _ = module_fixture
        user = SymCodePage(drivers)
        name_code2 = "".join(random.sample(num, 10))  # 名称使用随机数，以防重复名称添加失败
        name_description = "auto_test" + "".join(random.sample(num, 6))  # 描述使用随机数，以防重复名称添加失败
        user.Add_Symp_Code(name_code2, name_group, name_description)
        user = SymCodePage(drivers)
        user.Get_Symp_Code(name_code2)  # 查询出来方便编辑
        logging.info("步骤1：修改现象码描述")
        update_description = name_description[4:14]
        user.Edit_Code_Description(update_description)  # 修改描述
        get_record3, get_group3, get_description3 = user.Get_Symp_Code(name_code2)
        ValueAssert.value_assert_equal(get_description3, update_description)  # 判断修改描述成功

        logging.info("步骤1：修改现象码所属现象组")
        user.Close_Page()  # 关闭现象码页面
        user = SymCodePage(drivers)
        user.GoTo_refresh()
        user = NavPage(drivers)
        #user.refresh_page()
        user.list_search(content='Symptom Group Mgt')
        user = SymPage(drivers)
        #user.GoTo_Symp()
        update_group = "".join(random.sample(num, 6))  # 名称使用随机数，以防重复名称添加失败
        user.Add_Symp(update_group)  # 更换现象码的现象组需要现象组
        user.Close_Page()  # 关闭现象组页面
        user = SymCodePage(drivers)
        user.GoTo_refresh()
        user = NavPage(drivers)
       # user.refresh_page()
        user.list_search(content='Symptom Code Mgt')
        user = SymCodePage(drivers)
        #user.GoTo_Symp_Code()  # 进入现象码页面
        user.Get_Symp_Code(name_code2)  # 查询出来方便编辑
        user.Edit_Code_Grouping(update_group)  # 修改现象组
        get_record4, get_group4, get_description4 = user.Get_Symp_Code(name_code2)
        ValueAssert.value_assert_equal(get_group4, update_group)  # 判断修改描述成功
        # 删除新增的现象码和现象组
        user = SQL('CRM', 'test')
        user.query_db(
            'delete  from crm_mdm_symptom where symptom_code="{}"'.format(name_code2))
        user.query_db(
            'delete  from crm_mdm_symptom_group where symptom_group_name="{}"'.format(update_group))

    @allure.story("编辑现象码")  # 场景名称
    @allure.title("ModifiedBy：显示修改人名字；ModifiedOn：取值修改时间，精确到秒")  # 验证字段的值
    @allure.description("ModifiedBy：显示修改人名字；ModifiedOn：取值修改时间，精确到秒")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_1101(self, module_fixture, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        name_code1, name_group, _ = module_fixture
        user = SymCodePage(drivers)
        name_code2 = "".join(random.sample(num, 10))  # 名称使用随机数，以防重复名称添加失败
        name_description = "auto_test" + "".join(random.sample(num, 6))  # 描述使用随机数，以防重复名称添加失败
        user.Add_Symp_Code(name_code2, name_group, name_description)
        user = SymCodePage(drivers)
        user.Get_Symp_Code(name_code2)  # 查询出来方便编辑
        update_description = name_description[9:14]
        user.Edit_Code_Description(update_description)  # 修改描述
        created_date, created_by, modified_on, modified_by = user.Get_Code_DATE_BY(name_code2)  # 查询修改的时间、和修改人
        now_time = datetime.now()  # 获取当前时间
        modified_on_linux = datetime.strptime(modified_on, '%Y-%m-%d %H:%M:%S')+timedelta(hours=8)  # 将Linux的时间少8个小时
        modified_on1 = datetime.strptime(modified_on, '%Y-%m-%d %H:%M:%S')
        logging.info(modified_on1)
        time_difference = int((now_time - modified_on1).total_seconds())  # 获取时间差
        time_difference_linux = int((now_time - modified_on_linux).total_seconds())  # 获取时间差
        time_difference1 =math.fabs(time_difference)  # 将时间差取绝对值
        time_difference2 =math.fabs(time_difference_linux)  # 将时间差取绝对值
        logging.info(time_difference1)
        logging.info(type(time_difference1))

        if time_difference1 <= 60:
            logging.info("断言成功: 修改时间与当前时间相差没有超过1分钟 | 修改时间:{} 当前时间:{}".format(modified_on1, now_time))

        elif time_difference2 <= 60:
            logging.info("断言成功: 修改时间与当前时间相差没有超过1分钟 | 修改时间:{} 当前时间:{}".format(modified_on_linux, now_time))

        else:
            logging.warning("修改时间与当前时间相差超过1分钟 | 修改时间:{} 当前时间:{}".format(modified_on1, now_time))
            assert False, '修改时间与当前时间相差超过1分钟'

        ValueAssert.value_assert_equal(account[7]['username'], modified_by)  # 判断修改人等于当前登录用户
        # 删除新增数据，恢复环境
        user = SQL('CRM', 'test')
        user.query_db(
            'delete  from crm_mdm_symptom where symptom_code="{}"'.format(name_code2))


@allure.feature("SymptomCode")  # 模块名称
class TestExportSymptomCode:
    @allure.story("导出现象码")  # 场景名称
    @allure.title("导出现象码成功")  # 编辑现象组
    @allure.description("导出现象码成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip  # 跳过不执行
    def test_1627(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = SymCodePage(drivers)
        user.Export_Symp()  # 点击导出按钮
        user.Close_Page()  # 关闭现象码页面
        user.GoTo_Task()   # 进入下载任务页面
        user.Download_Symp_Code("Symptom_Code", "Symptom_Code")  # 下载导出的excel，同时判断文件名正确

        user.Close_Page()  # 关闭下载页面
       # user.GoTo_Symp_Code()  # 回到现象组页面
        user = NavPage(drivers)
        user.list_search(content='Symptom Group Mgt')





if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
