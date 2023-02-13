import allure
import pytest
from project.CRM.page_object.WMS_WarehouseBasicMgt_WarehouseList import *
from project.CRM.page_object.Center_Component import *

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@pytest.fixture(scope='module', autouse=True)  # 模块名称
def module_fixture(drivers):
    logging.info("模块前置条件，前往Warehouse List页面")
    user = NavPage(drivers)
    user.refresh_page()
    user.click_gotonav("WMS","Warehouse Basic Info Mgt","Warehouse List")  # 点击菜单
    user= DomAssert(drivers)
    user.assert_url("warehouseBasicInfoMgt/warehouseList")
    yield
    logging.info("后置条件：收起菜单")
    user = NavPage(drivers)
    user.click_gotonav("WMS")

@allure.feature('Warehouse List')  # 模块名称
class TestSearchWarehouse:
    @allure.story("查询仓库数据")
    @allure.title("查询SWH仓库")
    @allure.description("查询")
    @allure.severity("normal")
    def test_001_001(self,drivers):
        user = WarehouseList(drivers)
        user.search_warehousetype(type="SWH")
        number = user.get_total1()
        user = SQL("CRM", "test")  # 链接数据库
        tatal = user.query_db(
            'SELECT COUNT(*) FROM crm_wms_warehouse WHERE is_enable="1" and is_deleted="0" and warehouse_type_id="1250720990169497601"')
        sql_tatal = tatal[0].get("COUNT(*)")  # 执行sql后获取返回值的第一个值
        ValueAssert.value_assert_equal(sql_tatal, int(number))  # 校验获取的sql值与获取的total值相等



    @allure.story("查询仓库数据") # 场景名称
    @allure.title("查询xiao仓库") # 用例名称
    @allure.description("查询")
    @allure.severity("normal") # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self,drivers):
        user = WarehouseList(drivers)
        user.search_warehousecode(code="xiao")
        number1 = user.get_total2()
        user = SQL("CRM","test")
        tatal1 = user.query_db(
            'select COUNT(*) from crm_wms_warehouse where warehouse_code like "%xiao%"')
        sql_tatal1 = tatal1[0].get("COUNT(*)")
        ValueAssert.value_assert_equal(sql_tatal1, int(number1))



@allure.feature('Warehouse List')  # 模块名称
class TestEditWarehouse:
    @allure.story("编辑仓库")
    @allure.title("修改仓库code")
    @allure.description("编辑")
    @allure.severity("normal")
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self,drivers):
        user = WarehouseList(drivers)
        user.edit_warehouse(wcode="xiao_aa")
        DomAssert(drivers).assert_att('Success')

@allure.feature('Warehouse List')  # 模块名称
class TestDownloadTemplate:
    @allure.story("下载模板")
    @allure.title("下载仓库模板")
    @allure.description("下载")
    @allure.severity("normal")
    @pytest.mark.skip  # 跳过不执行
    def test_003_001(self, drivers):
        user = WarehouseList(drivers)
        user.check_warehousetemplate(content="Warehouse＋List")



if __name__ == '__main__':
    pytest.main(['WMS_WarehouseBasicMgt_WarehouseList.py'])
