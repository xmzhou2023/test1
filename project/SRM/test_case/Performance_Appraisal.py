import allure
import pytest

from project.SRM.page_object.Performance_Appraisal import Performance
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

#
# @pytest.fixture(scope="class")
# def test_enter_PerformanceAppraisal(self, drivers):
#     app = Performance(drivers)
#     app.PerformanceAppraisal()
#     appraisal_page_title = app.appraisal_page_title()
#     assert "供应商绩效考核" in appraisal_page_title, "未进入到供应商绩效考核"
#     yield
#     app.minimize()


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
    #
    # def test_seach(self,drivers):
    #     app = Performance(drivers)
    #     app.search()



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
