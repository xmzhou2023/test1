import time
import random
import allure
import pytest
from project.SRM.page_object.PerformanceAppraisal import Performance
from public.base.assert_ui import DomAssert, ValueAssert, SQLAssert
from libs.common.connect_sql import SQL


@pytest.fixture(scope="module", autouse=True)
def valuecode_module_fixture(drivers):
    app = Performance(drivers)
    app.PerformanceAppraisal()
    print("进入供应商绩效考核模块")
    yield
    app = Performance(drivers)
    app.MinWindows()
    print("供应商绩效考核测试结束")

@pytest.fixture(scope="class" )
def valuecode_fixture(drivers):
    app = Performance(drivers)
    # app.PerformanceAppraisal()
    app.enter_SupplyCategory()
    print("进入评估代码供货品类配置功能")
    # appraisal_page_title = app.appraisal_page_title()
    # assert "供应商绩效考核" in appraisal_page_title, "未进入到供应商绩效考核"
    yield
    app.close_valuecode_page()
    app.frame_back()
    print("关闭评估代码供货品类配置")


@pytest.fixture(scope="class" )
def PersonManage_fixture(drivers):
    app = Performance(drivers)
    app.enter_PersonManage()
    print("进入人员配置管理界面")
    yield
    app.close_PersonManage()
    print("关闭评估代码人员管理配置")



@pytest.fixture(scope="class" )
def ValueTemplate_fixture(drivers):
    app = Performance(drivers)
    app.enter_Value_Template()
    print("进入评估模板模块")
    yield
    app.close_Value_Template()
    print("关闭评估模板模块")



@allure.feature("供应商绩效考核")  # 模块名称
class TestAppraisal:

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据评估代码搜索-搜索结果正确")  # 用例名称
    @allure.description("根据评估代码进行搜索-搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_SearchCode_001(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.search_code("T0007")
        # DomAssert.assert_point_att()
        # ValueAssert.value_assert_equal()
        # num = app.search_code_number()
        # assert "显示 1 到 6 总共6个项目"  in num, '搜索结果不正确'

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据评估代码查询-查询结果正确")  # 用例名称
    @allure.description("根据评估代码进行模糊查询-查询结果正确")
    @allure.severity("normal")  # 用例等级
    def test_Searchcode_002(self, valuecode_fixture,drivers):
        app = Performance(drivers)
        app.search_code("a0101")


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据评估代码查询-查询结果正确")  # 用例名称
    @allure.description("查询不存在评估代码-查询结果正确")
    @allure.severity("normal")  # 用例等级
    def test_Searchcode_003(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.search_code("A01")

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据物料小类查询-查询结果正确")  # 用例名称
    @allure.description("查询正确物料小类-查询结果正确")
    @allure.severity("normal")  # 用例等级
    def test_Search_Cate01(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.search_cate("大电流BTB")
        sql1 = SQL("SRM", "test")
        sql_val1 = "select count(materialCateLevel3Name) from evaluate_supply_category_configuration where materialCateLevel3Name='大电流BTB'"
        result = sql1.query_db(sql_val1)
        a = result[0]
        b = a["count(materialCateLevel3Name)"]
        print(b)
        search_val = app.search_cate_number()
        print(search_val)
        ValueAssert.value_assert_In(str(b),search_val)
        app.Clear_input("评估代码供货品类配置-物料小类查询输入框")
        app.frame_back()


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据物料小类模糊查询-查询结果正确")  # 用例名称
    @allure.description("模糊查询物料小类-查询结果正确")
    @allure.severity("normal")  # 用例等级
    def test_Search_Cate02(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.search_cate("IOT")
        sql1 = SQL("SRM", "test")
        sql_val1 = "select count(materialCateLevel3Name) " \
                   "from evaluate_supply_category_configuration where materialCateLevel3Name like '%IOT%'"
        result = sql1.query_db(sql_val1)
        a = result[0]
        b = a["count(materialCateLevel3Name)"]
        print(b)
        search_val = app.search_cate_number()
        print(search_val)
        ValueAssert.value_assert_In(str(b), search_val)
        app.Clear_input("评估代码供货品类配置-物料小类查询输入框")
        app.frame_back()



    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据物料小类和代码组合查询-查询结果正确")  # 用例名称
    @allure.description("物料小类和代码组合查询-查询结果正确")
    @allure.severity("normal")  # 用例等级
    def test_Search_combine(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.search_cate_code("A0207", "大电流BTB")
        sql1 = SQL("SRM", "test")
        sql_val1 = "select count(materialCateLevel3Name) " \
                   "from evaluate_supply_category_configuration where materialCateLevel3Name = '大电流BTB' and evaluatedCode = 'A0207'"
        result = sql1.query_db(sql_val1)
        a = result[0]
        b = a["count(materialCateLevel3Name)"]
        print(b)
        search_val = app.search_cate_number()
        print(search_val)
        ValueAssert.value_assert_In(str(b), search_val)
        app.Clear_input("评估代码供货品类配置-物料小类查询输入框")
        app.Clear_input("评估代码供货品类配置-评估代码查询输入框")
        app.frame_back()



    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建关闭")  # 用例名称
    @allure.description("点击新建--关闭")
    @allure.severity("normal")  # 用例等级
    def test_creat_close(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.creat_SupplyCategory()
        creat_title = app.get_title_creat()
        assert "新增供货品类配置" in creat_title, "未打开新建界面"
        app.creat_SupplyCategory_close()


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建取消")  # 用例名称
    @allure.description("点击新建--取消")
    @allure.severity("normal")  # 用例等级
    def test_creat_cancel(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.creat_SupplyCategory()
        creat_title = app.get_title_creat()
        assert "新增供货品类配置" in creat_title, "未打开新建界面"
        app.creat_SupplyCategory_cancel()

#
    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建成功")  # 用例名称
    @allure.description("点击新建--选择物料评估代码--确定--新建成功")
    @allure.severity("normal")  # 用例等级
    def test_create_successful(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        a = str(random.randint(100, 999))
        app.creat_select_code("{}{}".format("H8", a))
        # app.create_select_code("H0701")
        app.creat_select_material()
        app.creat_select_rule()
        app.creat_SelectOK()
        alert_text = app.get_alert_text()
        assert "操作成功" in alert_text, "新建失败"
        app.close_alert()
        sql = SQL("SRM", 'test')
        a = sql.query_db("select * from evaluate_supply_category_configuration where evaluatedCode like '%H8%'")
        print(a)
        sql.delete_db("delete from  evaluate_supply_category_configuration  where evaluatedCode like '%H8%'")
        a = sql.query_db("select * from evaluate_supply_category_configuration where evaluatedCode like '%H8%'")
        print(a)



    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建失败")  # 用例名称
    @allure.description("点击新建-不填内容--点击确定--新建失败")
    @allure.severity("normal")  # 用例等级
    def test_create_fail(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.create_fail_blank()
        prompt = app.create_fail_prompt()
        assert "请填写评估代码" in prompt, "新建不填内容未提示错误"
        app.close_fail()

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("修改评估代码评分规则")  # 用例名称
    @allure.description("查询指定代码-修改数据的评分规则--修改成功")
    @allure.severity("normal")  # 用例等级
    def test_change_rule(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.change_rule("C0001")

    # 此功能已经删除
    # @allure.story("估代码供货品类配置")  # 场景名称
    # @allure.title("导出模板")  # 用例名称
    # @allure.description("导出模板")
    # @allure.severity("normal")  # 用例等级
    # def test_export_template(self, valuecode_fixture, drivers):
    #     app = Performance(drivers)
    #     app.export_template()



    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("跳转到某一页")  # 用例名称
    @allure.description("输入数字页码，跳转到相应页")
    @allure.severity("normal")  # 用例等级
    def test_input_page(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.input_page("3")
        time.sleep(1)
        page = app.current_page()
        assert "显示 201 到 300 总共" in page, "跳转到某一页失败"
        app.Frameback()

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("点击下一页")  # 用例名称
    @allure.description("首页点击下一页-到第二页")
    @allure.severity("normal")  # 用例等级
    def test_next_page(self, valuecode_fixture,drivers):
        app = Performance(drivers)
        app.next_page("1")
        page = app.current_page()
        assert "显示 101 到 200 总共" in page, "跳转到下一页失败"
        app.Frameback()

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("点击尾页")  # 用例名称
    @allure.description("首页尾页-跳转到尾页")
    @allure.severity("normal")  # 用例等级
    def test_end_page(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.input_page("1")
        app.end_page()

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("点击上一页")  # 用例名称
    @allure.description("点击上一页-到上一页")
    @allure.severity("normal")  # 用例等级
    def test_previous_page(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.previous_page("4")
        page = app.current_page()
        assert "显示 201 到 300 总共" in page, "跳转到上一页失败"
        app.Frameback()

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("点击首页")  # 用例名称
    @allure.description("点击首页-跳转到首页")
    @allure.severity("normal")  # 用例等级
    def test_first_page(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.first_page("2")
        page = app.current_page()
        assert "显示 1 到 100 总共" in page, "跳转到首页失败"
        app.Frameback()


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("筛选列表评估代码列")  # 用例名称
    @allure.description("点击评估代码表头筛选-筛选结果正确")
    @allure.severity("normal")  # 用例等级
    def test_screening_valuecode(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.screening_valuecode()


@allure.feature("供应商绩效考核")  # 模块名称
class TestPersonManage:
    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("新建评估代码人员配置")  # 用例名称
    @allure.description("新建评估代码人员配置--成功")
    @allure.severity("normal")  # 用例等级
    def test_create_001(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.create_success_code()
        me = app.create_success_mess()
        assert "操作成功" in me, "未新建成功"
        app.create_success_mess_close()
        sql = SQL("SRM", 'test')
        num = sql.query_db(
            "select * from evaluator_code_configuration where evaluatedCode ='A0101' AND supplierClass = '2'")
        print(num)
        sql.delete_db("delete from  evaluator_code_configuration where evaluatedCode ='A0101' AND supplierClass = '2'")


    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("新建评估代码人员配置不填内容-新增失败")  # 用例名称
    @allure.description("新建评估代码人员配置失败--不填所有内容")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke
    def test_create_002(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.create_blank_all()
        mess = app.get_message()
        assert "请选择评估代码" in mess, "未选评估代码未提示报错"
        app.get_message_close()
        app.enter_iframe()
        app.create_cancel()

    #
    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("新建评估代码人员配置不填内容-新增失败")  # 用例名称
    @allure.description("新建评估代码人员配置失败--不填供应商账号")
    @allure.severity("normal")  # 用例等级
    def test_create_003(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.create_blank_elsnumber()
        me = app.get_blank_massage()
        assert "至少一项不能为空" in me, "未提示为空内容"
        app.close_blank_mass()
        app.enter_iframe()
        app.create_cancel()

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("新建评估代码人员配置不填评估人-新增失败")  # 用例名称
    @allure.description("新建评估代码人员配置失败--不填评估人")
    @allure.severity("normal")  # 用例等级
    def test_create_004(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.create_blank_evaluator()
        me = app.get_blank_massage()
        assert "至少一项不能为空" in me, "未提示为空内容"
        app.close_blank_mass()
        app.enter_iframe()
        app.create_cancel()


    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("新建评估代码人员配置不只填部分评估人-新增失败")  # 用例名称
    @allure.description("新建评估代码人员配置失败--只填成本评估人")
    @allure.severity("normal")  # 用例等级
    def test_create_005(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.create_blank_evaluator01()
        me = app.get_blank_massage01()
        assert "不允许添加相同有效的评估代码+业务类型+供应商账号" in me, "未提示为空内容"
        app.close_blank_mass()
        app.create_cancel01()

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("新建评估代码人员配置不只填部分评估人-新增失败")  # 用例名称
    @allure.description("新建评估代码人员配置失败--只填成本，交付评估人")
    @allure.severity("normal")  # 用例等级
    def test_create_006(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.create_blank_evaluator02()
        me = app.get_blank_massage01()
        assert "不允许添加相同有效的评估代码+业务类型+供应商账号" in me, "未提示为空内容"
        app.close_blank_mass()
        app.create_cancel01()


    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("输入正确评估代码搜索--搜索结果正确")  # 用例名称
    @allure.description("输入正确评估代码搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_code1(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.person_search_code("A0101")

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("输入错误评估代码搜索--搜索结果正确")  # 用例名称
    @allure.description("输入错误评估代码搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_code2(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.clear_input_code()
        app.person_search_code("Z0101")
        app.clear_input_code()

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("选择业务类型为2G搜索--搜索结果正确")  # 用例名称
    @allure.description("选择业务类型为2G搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_type1(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.select_type_2G()
        app.select_type_blank()

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("选择业务类型为手机搜索--搜索结果正确")  # 用例名称
    @allure.description("选择业务类型为手机搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_type2(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.select_type_phone()
        app.select_type_blank()

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("选择业务类型为新业务搜索--搜索结果正确")  # 用例名称
    @allure.description("选择业务类型为新业务搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_type3(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.select_type_newservice()
        app.select_type_blank()

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("选择业务类型为配件搜索--搜索结果正确")  # 用例名称
    @allure.description("选择业务类型为配件搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_type4(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.select_type_accessory()
        app.select_type_blank()

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("选择业务类型为综合搜索--搜索结果正确")  # 用例名称
    @allure.description("选择业务类型为综合搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_type5(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.select_type_synthesis()
        app.select_type_blank()

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("选择业务类型为外研搜索--搜索结果正确")  # 用例名称
    @allure.description("选择业务类型为外研搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_type6(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.select_type_foreign()
        # db = SQLAssert(pro_name, 'test')
        # app = Performance(drivers)
        # page_count = app.get_search_count()
        # db.assert_sql_count(page_count, "select count() from ")
        app.select_type_blank()





    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("选择业务类型为空白搜索--搜索结果正确")  # 用例名称
    @allure.description("选择业务类型为空白搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_type7(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.select_type_blank()
        # app.get_search_count()

    # 10月14日
    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("根据供应商账号搜索--搜索结果正确")  # 用例名称
    @allure.description("输入正确供应商账号搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_els(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.search_els_number("860129")
        app.clear_search_elsnumber()


    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("根据供应商账号加评估代码搜索--搜索结果正确")  # 用例名称
    @allure.description("输入正确供应商账号和评估代码搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_combined(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.search_code_elsnumber("A0101", "862048")
        app.clear_input_code()
        app.clear_search_elsnumber()
        # db = SQLAssert("SRM", 'test')
        # page_count = app.get_search_count()
        # db.assert_sql( , "selct")
        # db.assert_sql_count(page_count, "select count(evaluatedCodeNumber) from evaluator_code_configuration where evaluatedCode = "A0101" and toElsAccount = "862048" ")

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("根据供应商类别加评估代码搜索--搜索结果正确")  # 用例名称
    @allure.description("输入正确供应商类别和评估代码搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_code_category(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.search_code_category("A0101")
        app.clear_input_code()
        app.select_type_blank()

    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("根据供应商账号加供应商类别搜索--搜索结果正确")  # 用例名称
    @allure.description("输入正确供应商类别和供应商账号搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_elsnumber_category(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.search_elsnumber_category("862131")
        app.select_type_blank()
        app.clear_search_elsnumber()



    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("根据供应商账号加评估代码加供应商类别搜索--搜索结果正确")  # 用例名称
    @allure.description("输入正确供应商账号加评估代码加供应商类别搜索--搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_all(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.search_all_combined("A0101", "862048")
        app.clear_input_code()
        app.select_type_blank()
        app.clear_search_elsnumber()


    @allure.story("评估代码管理人员配置")  # 场景名称
    @allure.title("筛选列表评估代码--筛选结果正确")  # 用例名称
    @allure.description("列表第一页评估代码进行筛选--筛选结果正确")
    @allure.severity("normal")  # 用例等级
    def test_pick_code(self, drivers, PersonManage_fixture):
        app = Performance(drivers)
        app.pick_code()




@allure.feature("供应商绩效考核")  # 模块名称
class TestValueTemplate:

    @allure.story("评估模板管理")  # 场景名称
    @allure.title("查询评估模板编号")  # 用例名称
    @allure.description("根据正确评估模板查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke
    def test_search_template_number01(self, drivers, ValueTemplate_fixture):
        app = Performance(drivers)
        app.search_template("NO202004090002")

    @allure.story("评估模板管理")  # 场景
    @allure.title("查询评估模板编号")  # 用例名称
    @allure.description("根据错误评估模板查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke
    def test_search_template_number02(self, drivers, ValueTemplate_fixture):
        app = Performance(drivers)
        app.search_template("NO202004090")


    @allure.story("评估模板管理")  # 场景
    @allure.title("查询评估模板")  # 用例名称
    @allure.description("根据评估模板模糊查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke
    def test_search_template_name01(self, drivers, ValueTemplate_fixture):
        app = Performance(drivers)
        app.search_template_name("年度绩效考核")


    @allure.story("评估模板管理")  # 场景
    @allure.title("查询评估模板")  # 用例名称
    @allure.description("根据评估模板精准查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke
    def test_search_template_name02(self, drivers, ValueTemplate_fixture):
        app = Performance(drivers)
        app.search_template_name("供应商季度绩效考核（家电类）")

    @allure.story("评估模板管理")  # 场景
    @allure.title("评估模板+编号组合查询")  # 用例名称
    @allure.description("根据评估模板+编号组合查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke
    def test_search_template_combined(self, drivers, ValueTemplate_fixture):
        app = Performance(drivers)
        app.search_template_combined("NO202007020005", "供应商季度绩效考核（家电类）")









if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])