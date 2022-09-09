import time
import random
import allure
import pytest
from project.SRM.page_object.PerformanceAppraisal_SupplyCategory import Performance



@pytest.fixture(scope="module", autouse=True)
def valuecode_module_fixture(drivers):
    app = Performance(drivers)
    app.PerformanceAppraisal()
    # print("进入供应商绩效考核模块")
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
    print("关闭评估代码供货品类配置")


@allure.feature("供应商绩效考核")  # 模块名称
class TestAppraisal:

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据评估代码搜索-搜索结果正确")  # 用例名称
    @allure.description("根据评估代码进行搜索-搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_SearcCcode_001(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.search_code("T0007")
        # num = app.search_code_number()
        # assert "显示 1 到 6 总共6个项目"  in num, '搜索结果不正确'

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据评估代码查询-查询结果正确")  # 用例名称
    @allure.description("根据评估代码进行模糊查询-查询结果正确")
    @allure.severity("normal")  # 用例等级
    def test_SearcCcode_002(self, valuecode_fixture,drivers):
        app = Performance(drivers)
        app.search_code("a0101")


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据评估代码查询-查询结果正确")  # 用例名称
    @allure.description("查询不存在评估代码-查询结果正确")
    @allure.severity("normal")  # 用例等级
    def test_SearcCcode_003(self,valuecode_fixture, drivers):
        app = Performance(drivers)
        app.search_code("A01")



    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建关闭")  # 用例名称
    @allure.description("点击新建--关闭")
    @allure.severity("normal")  # 用例等级
    def test_creat_close(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.creat_SupplyCategory()
        creat_title = app.get_title_creat()
        assert "新增供货品类配置" in creat_title,"未打开新建界面"
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


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建成功")  # 用例名称
    @allure.description("点击新建--选择物料评估代码--确定--新建成功")
    @allure.severity("normal")  # 用例等级
    def test_creat_successful(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        a = str(random.randint(1000, 9999))
        app.creat_select_code("{}{}".format("H", a))
        # app.creat_select_code("H0701")
        app.creat_select_material()
        app.creat_select_rule()
        app.creat_SelectOK()
        alert_text = app.get_alert_text()
        assert "操作成功" in alert_text, "新建失败"
        app.close_alert()


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("修改评估代码评分规则")  # 用例名称
    @allure.description("查询指定代码-修改数据的评分规则--修改成功")
    @allure.severity("normal")  # 用例等级
    def test_change_rule(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.change_rule("H0101")


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("导出模板")  # 用例名称
    @allure.description("导出模板")
    @allure.severity("normal")  # 用例等级
    def test_export_template(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.export_template()

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
    def test_next_page(self, valuecode_fixture, drivers):
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

    #
    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("点击上一页")  # 用例名称
    @allure.description("点击上一页-到上一页")
    @allure.severity("normal")  # 用例等级
    def test_previous_page(self, valuecode_fixture, drivers):
        app = Performance(drivers)
        app.previous_page("5")
        page = app.current_page()
        assert "显示 301 到 400 总共" in page, "跳转到上一页失败"
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




if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])