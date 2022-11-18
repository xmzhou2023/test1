from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AssetManagement_AssetMaintenanceHistory import AssetMaintenanceHistoryPage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
import pytest
import allure

"""后置关闭菜单方法  pytest.fixture(scope='作用域' function函数级别  """
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()


@allure.feature("GTM管理-资产维护历史")
class TestQueryAssetMaintenanceHistory:
    @allure.story("资产维护历史")
    @allure.title("资产维护历史页面，根据国家、品牌、状态查询资产维护数据")
    @allure.description("库存不足报告页面，根据品牌、国家、时间查询资产维护历史数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Asset Management", "Asset Maintenance History")

        query = AssetMaintenanceHistoryPage(drivers)
        query.query_asset_maintenance_history('Nigeria', 'Infinix', 'Retire')
        query.click_search()

        """断言获取列表数据，与筛选条件比较是否一致"""
        get_total = query.get_total()
        query.assert_total(get_total)
        get_brand = query.get_list_field_content('Get list Brand')
        get_country = query.get_list_field_content('Get list Country')
        get_status = query.get_list_field_content('Get list Status')
        get_picture = query.get_list_field_content('Get list Picture')
        ValueAssert.value_assert_equal('Infinix', get_brand)
        ValueAssert.value_assert_IsNoneNot(get_country)
        ValueAssert.value_assert_equal('Retire', get_status)
        ValueAssert.value_assert_equal('Picture', get_picture)


if __name__ == '__main__':
    pytest.main(['AssetManagement_AssetMaintenanceHistory.py'])
