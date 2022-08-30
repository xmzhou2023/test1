import time

import allure
import pytest

from project.SRM.page_object.PerformanceAppraisal_SupplyCategory import Performance





@pytest.fixture(scope="class",autouse=True)
def fixture(drivers):
    print("开始测试供应商绩效考核模块")
    yield
    app = Performance(drivers)
    app.MinWindows()


@allure.feature("供应商绩效考核") # 模块名称
class TestAppraisal:
    @allure.story("进入供应商绩效考核") # 场景名称
    @allure.title("进入供应商绩效考核")  # 用例名称
    @allure.description("进入供应商绩效考核模块")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_enter_PerformanceAppraisal(self, drivers):
        app = Performance(drivers)
        app.PerformanceAppraisal()
        appraisal_page_title = app.appraisal_page_title()
        assert "供应商绩效考核" in appraisal_page_title,"未进入到供应商绩效考核"


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("进入估代码供货品类配置页面")  # 用例名称
    @allure.description("进入评估代码供货品类配置页面成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_enter_SupplyCategory(self, drivers):
        app = Performance(drivers)
        app.enter_SupplyCategory()
        SupplyCategory_title = app.title_SupplyCategory()
        assert "评估代码供货品类配置" in SupplyCategory_title,"未进入到评估代码供货品类配置页面"


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置--点击新建")  # 用例名称
    @allure.description("评估代码供货品类配置--点击新建--出现弹窗")
    @allure.severity("normal")  # 用例等级
    def test_creat_SupplyCategory(self, drivers):
        app = Performance(drivers)
        app.creat_SupplyCategory()
        creat_title = app.get_title_creat()
        assert "新增供货品类配置" in creat_title,"未打开新建界面"


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建关闭")  # 用例名称
    @allure.description("点击新建--关闭")
    @allure.severity("normal")  # 用例等级
    def test_creat_close(self, drivers):
        app = Performance(drivers)
        app.creat_SupplyCategory_close()

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建取消")  # 用例名称
    @allure.description("点击新建--取消")
    @allure.severity("normal")  # 用例等级
    def test_creat_cancel(self, drivers):
        app = Performance(drivers)
        app.creat_SupplyCategory_cancel()

    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("评估代码供货品类配置新建成功")  # 用例名称
    @allure.description("点击新建--选择物料评估代码--确定--新建成功")
    @allure.severity("normal")  # 用例等级
    def test_creat_successful(self,drivers):
        app = Performance(drivers)
        app.creat_select_code("H0101")
        app.creat_select_material()
        app.creat_select_rule()
        app.creat_SelectOK()
        time.sleep(3)
        alert_text = app.get_alert_text()
        assert "操作成功" in alert_text, "新建失败"


    @allure.story("估代码供货品类配置")  # 场景名称
    @allure.title("根据评估代码搜索-搜索结果正确")  # 用例名称
    @allure.description("根据评估代码进行搜索-搜索结果正确")
    @allure.severity("normal")  # 用例等级
    def test_search_code(self,drivers):
        app = Performance(drivers)
        app.search_code("H0101")
        # num = app.search_code_number()
        # assert "总共1个项目"  in num, '搜索结果不正确'

    #
    # @allure.story("估代码供货品类配置")  # 场景名称
    # @allure.title("根据物料小类搜索-搜索结果正确")  # 用例名称
    # @allure.description("根据列表存在的物料小类进行搜索-搜索结果正确")
    # @allure.severity("normal")  # 用例等级
    # def test_search_code(self,drivers):
    #     app = Performance(drivers)
    #     app.search_code("电容屏")





if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
