import time
import random
import allure
import pytest
from project.SRM.page_object.PerformanceAppraisal_SupplyCategory import Performance


@pytest.fixture(scope="class",autouse=True)
def fixture(drivers):
    app = Performance(drivers)
    app.PerformanceAppraisal()
    app.enter_SupplyCategory()
    # appraisal_page_title = app.appraisal_page_title()
    # assert "供应商绩效考核" in appraisal_page_title, "未进入到供应商绩效考核"
    yield
    app = Performance(drivers)
    app.MinWindows()


@allure.feature("供应商绩效考核") # 模块名称
class TestAppraisal:


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据评估代码搜索-搜索结果正确")  # 用例名称
    @allure.description("根据评估代码进行搜索-搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_SearcCcode_001(self,drivers):
        app = Performance(drivers)
        app.search_code("T0007")
        # num = app.search_code_number()
        # assert "显示 1 到 6 总共6个项目"  in num, '搜索结果不正确'

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据评估代码查询-查询结果正确")  # 用例名称
    @allure.description("根据评估代码进行模糊查询-查询结果正确")
    @allure.severity("normal")  # 用例等级
    def test_SearcCcode_002(self, drivers):
        app = Performance(drivers)
        app.search_code("a0101")


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据评估代码查询-查询结果正确")  # 用例名称
    @allure.description("查询不存在评估代码-查询结果正确")
    @allure.severity("normal")  # 用例等级
    def test_SearcCcode_003(self, drivers):
        app = Performance(drivers)
        app.search_code("A01")



    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建关闭")  # 用例名称
    @allure.description("点击新建--关闭")
    @allure.severity("normal")  # 用例等级
    def test_creat_close(self, drivers):
        app = Performance(drivers)
        app.creat_SupplyCategory()
        creat_title = app.get_title_creat()
        assert "新增供货品类配置" in creat_title,"未打开新建界面"
        app.creat_SupplyCategory_close()


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建取消")  # 用例名称
    @allure.description("点击新建--取消")
    @allure.severity("normal")  # 用例等级
    def test_creat_cancel(self, drivers):
        app = Performance(drivers)
        app.creat_SupplyCategory()
        creat_title = app.get_title_creat()
        assert "新增供货品类配置" in creat_title, "未打开新建界面"
        app.creat_SupplyCategory_cancel()


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建成功")  # 用例名称
    @allure.description("点击新建--选择物料评估代码--确定--新建成功")
    @allure.severity("normal")  # 用例等级
    def test_creat_successful(self, drivers):
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
    def test_change_rule(self, drivers):
        app = Performance(drivers)
        app.change_rule("H0101")

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("导出模板")  # 用例名称
    @allure.description("导出模板")
    @allure.severity("normal")  # 用例等级
    def test_export_template(self, drivers):
        app = Performance(drivers)
        app.export_template()


    # @allure.story("估代码供货品类配置")  # 场景名称
    # @allure.title("点击下一页")  # 用例名称
    # @allure.description("首页点击下一页-到第二页")
    # @allure.severity("normal")  # 用例等级
    # def test_next_page(self, drivers):
    #     app = Performance(drivers)
    #     app.next_page()





if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
