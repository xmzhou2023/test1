from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AssetManagement_AssetCounting import AssetCountingPage
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
class TestQueryAssetCounting:
    @allure.story("资产统计页面")
    @allure.title("资产统计页面，根据筛选条件查询资产统计数据")
    @allure.description("资产统计页面，根据品牌、国家、状态查询资产统计数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    @pytest.mark.UT
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """资产管理-打开资产统计页面"""
        user.click_gotomenu("Asset Management", "Asset Counting")

        query = AssetCountingPage(drivers)
        query.query_asset_counting('Bangladesh', 'TECNO', 'Available', 'Manned')
        query.click_search()

        """断言获取列表数据，与筛选条件比较是否一致"""
        get_total = query.get_total()
        """断言分页总数是否存在数据"""
        if int(get_total) >= 1:
            get_brand = query.get_list_field_content('Get list Brand')
            get_country = query.get_list_field_content('Get list Country')
            get_shop_id = query.get_list_field_content('Get list Shop ID')
            get_manpower = query.get_list_field_content('Get list Manpower Type')
            get_status = query.get_list_field_content('Get list Status')
            get_asset_cn = query.get_list_field_content('Get list Asset Name CN')
            get_asset_en = query.get_list_field_content('Get list Asset Name EN')
            get_picture = query.get_list_field_content('Get list Picture')

            ValueAssert.value_assert_equal('TECNO', get_brand)
            ValueAssert.value_assert_equal('Bangladesh', get_country)
            ValueAssert.value_assert_IsNoneNot(get_shop_id)
            ValueAssert.value_assert_equal('Manned', get_manpower)
            ValueAssert.value_assert_equal('Available', get_status)
            ValueAssert.value_assert_IsNoneNot(get_asset_cn)
            ValueAssert.value_assert_IsNoneNot(get_asset_en)
            ValueAssert.value_assert_IsNoneNot(get_picture)
            logging.info("资产统计页面，分页总条数大于0，未查询到考勤记录数Total:{}:".format(get_total))

            query.click_picture()
            get_asset_photo = query.get_list_field_content('Get Asset Photo')
            ValueAssert.value_assert_equal('Asset Photo', get_asset_photo)
            query.close_asset_photo()
        else:
            logging.info("资产统计页面，分页总条数为0，未查询到考勤记录数Total:{}:".format(get_total))

if __name__ == '__main__':
    pytest.main(['AssetManagement_AssetCounting.py'])
