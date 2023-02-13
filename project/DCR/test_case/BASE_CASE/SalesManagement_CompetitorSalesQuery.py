import logging

import allure
import pytest
from project.DCR.page_object.SalesManagement_CompetitorSalesQuery import CompetitorSalesQuery
from public.base.basics import Base
from public.base.assert_ui import ValueAssert,DomAssert
from project.DCR.page_object.Center_Component import LoginPage
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

#后置处理关闭菜单
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()


@allure.feature("销售管理-竞品销售查询") # 模块名称
class TestQueryCompe:
    @allure.story("查询竞品销售信息") # 场景名称
    @allure.title("查询各个常用条件下销售信息")  # 用例名称
    @allure.description("查询后检查结果中是否有对应字段信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开打开销售管理-打开竞品销售查询页面"""
        user.click_gotomenu("Sales Management", "Competitor Sales Query")
        page=CompetitorSalesQuery(drivers)

        #查询上传日期并断言日期和查询结果一致
        page.input_upload_date('2022-09-06','2022-09-06')
        page.click_search()
        result_date=page.get_table_txt(2)    #第2列
        ValueAssert.value_assert_In('2022-09-06',result_date)
        page.click_reset()

        #查询销售区域并断言列表和查询结果一致
        page.select_sale_area('Senegal')
        page.click_search()
        result_area=page.get_table_txt(20)      #第20列
        ValueAssert.value_assert_In('Senegal',result_area)
        page.click_reset()

        # 查询品牌并断言品牌和查询结果一致
        page.select_sale_brand('Acer')
        page.click_search()
        result_date = page.get_table_txt(9)      #第9列
        ValueAssert.value_assert_In('Acer', result_date)
        page.click_reset()


    @allure.story("查询竞品销售信息") # 场景名称
    @allure.title("查询各个不常用条件下的销售信息")  # 用例名称
    @allure.description("查询后检查结果中是否有对应字段信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture') # 用例标记
    def test_001_002(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开打开销售管理-打开竞品销售查询页面"""
        user.click_gotomenu("Sales Management", "Competitor Sales Query")

        page=CompetitorSalesQuery(drivers)
        page.click_unfold()

        #查询上传日期并断言日期和查询结果一致
        page.input_sales_date('2022-09-06','2022-09-06')
        page.click_search()
        result_date=page.get_table_txt(8)    #第八列
        ValueAssert.value_assert_In('2022-09-06',result_date)
        page.click_reset()

        #查询店铺并断言店铺和查询结果一致
        page.select_shop('BD017762')
        page.click_search()
        result_date=page.get_table_txt(3)    #第八列
        ValueAssert.value_assert_In('BD017762',result_date)
        page.click_reset()


class TestExportCompe:
    @allure.story("导出竞品销售信息") # 场景名称
    @allure.title("导出固定条件下的销售信息")  # 用例名称
    @allure.description("导出页面数据保证功能可用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture') # 用例标记
    def test_002_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开打开销售管理-打开竞品销售查询页面"""
        user.click_gotomenu("Sales Management", "Competitor Sales Query")
        page=CompetitorSalesQuery(drivers)
        page.click_unfold()

        #查询上传日期并断言日期和查询结果一致
        page.input_country('Egypt')
        page.click_search()
        result_date=page.get_table_txt(11)    #第11列
        ValueAssert.value_assert_In('Egypt',result_date)
        page.click_reset()
        page.click_export()
        export_txt = page.export_status()
        ValueAssert.value_assert_In('Download...', export_txt)


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
