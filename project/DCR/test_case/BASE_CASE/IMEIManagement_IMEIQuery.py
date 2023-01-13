import allure
import pytest
import logging
from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.IMEIManagement_IMEIQuery import IMEIQueryPage
from public.base.assert_ui import ValueAssert
from public.base.basics import Base
from libs.common.time_ui import sleep

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_imei_query_fixture(drivers):
    yield
    close = IMEIQueryPage(drivers)
    close.click_close_imei_query()

@allure.feature("IMEI管理-IMEI查询") # 模块名称
class TestBoxIDQuery:
    @allure.story("查询Box ID")
    @allure.title("查询Box ID")
    @allure.description("从IMEI库存页面，获取列表Box ID ,在IMEI Query页面，查询Box ID，信息是否正确")
    @allure.severity("normal")
    @pytest.mark.smoke
    @pytest.mark.usefixtures('function_imei_query_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")

        imei_query = IMEIQueryPage(drivers)
        get_box_id = imei_query.get_code('获取BOXID数据')
        logging.info("获取IMEI Inventory Query页面，列表的Box ID字段:{}".format(get_box_id))
        imei_query.click_close_imei_inven_query()

        Base(drivers).refresh()
        user.click_gotomenu("IMEI Management", "IMEI Query")
        imei_query.click_choose_box_id()
        imei_query.input_code(get_box_id)

        """获取列表查询后的数据，进行断言"""
        get_list_box = imei_query.get_code('获取列表Box ID')
        ValueAssert.value_assert_equal(get_list_box, get_box_id)
        #imei_query.click_close_imei_query()


@allure.feature("IMEI管理-IMEI查询") # 模块名称
class TestIMEIQuery:
    @allure.story("查询IMEI")
    @allure.title("查询IMEI")
    @allure.description("从IMEI库存页面，获取列表IMEI ,在IMEI Query页面，查询IMEI，信息是否正确")
    @allure.severity("normal")
    @pytest.mark.smoke
    @pytest.mark.usefixtures('function_imei_query_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")
        sleep(2)
        imei_query = IMEIQueryPage(drivers)
        get_imei = imei_query.get_code('获取IMEI数据')
        logging.info("获取IMEI Inventory Query页面，列表的IMEI字段:{}".format(get_imei))
        imei_query.click_close_imei_inven_query()

        Base(drivers).refresh()
        user.click_gotomenu("IMEI Management", "IMEI Query")
        imei_query.click_choose_imei()
        imei_query.input_code(get_imei)

        """获取列表查询后的数据，进行断言"""
        get_list_imei = imei_query.get_code('获取列表IMEI')
        ValueAssert.value_assert_equal(get_list_imei, get_imei)
        #imei_query.click_close_imei_query()

    @allure.story("导出IMEI")
    @allure.title("导出IMEI")
    @allure.description("导出IMEI")
    @allure.severity("normal")
    @pytest.mark.smoke
    @pytest.mark.usefixtures('function_imei_query_fixture')
    def test_002_002(self, drivers):
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "lhmadmin", "dcr123456")
        user1.click_gotomenu("IMEI Management", "IMEI Query")
        user = IMEIQueryPage(drivers)
        user.input_code('356209114268102')
        user.click_export()
        user.assert_export_success()

if __name__ == '__main__':
    pytest.main(['IMEIManagement_IMEIQuery.py'])
