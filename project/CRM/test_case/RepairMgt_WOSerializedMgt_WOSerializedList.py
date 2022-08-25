import allure
import pytest
from public.base.assert_ui import *
from project.CRM.page_object.Center_Component import NavPage
from project.CRM.page_object.RepairMgt_WOSerializedMgt_WOSerializedList import *
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@pytest.fixture(scope='module',autouse=True)
def class_setup_fixture(drivers):
    num = NavPage(drivers)
    num.click_gotonav("WMS", "Stock In/Out Mgt", "Initialize Inventory")
    num = DomAssert(drivers)
    num.assert_url("/wms/stockInOutMgt/initializeInventory")

    logging.info("前置条件:添加物料库存")
    num = WOSerializedListAdd(drivers)
    num.add_material()

@pytest.fixture(scope='module',autouse=True)
def module_setup_fixture(drivers):
    logging.info("前置条件:进入序列化工单列表页")
    user = NavPage(drivers)
    user.click_gotonav("Repair Mgt", "WO Serialized Mgt", 'WO Serialized List')
    user = DomAssert(drivers)
    user.assert_url("/maintenanceMgt/workorderSerializedMgt/workorderSerializedList")

@allure.feature("WO Serialized Mgt-WO Serialized List")
class TestAddWoList:
    @allure.story("新增序列化工单成功") # 场景名称
    @allure.title("序列化工单新增成功")  # 用例名称
    @allure.description("输入的imei在所选的仓库中有defective状态库存")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        sn_imei = WOSerializedListAdd.search_imei_stock(self)
        num = WOSerializedListAdd(drivers)
        num.add_woserlist(Warehouse='API_母仓', imei=sn_imei)
        num = DomAssert(drivers)
        num.assert_att(sn_imei)

    @allure.story("新增序列化工单失败")  # 场景名称
    @allure.title("序列化工单新增失败")  # 用例名称
    @allure.description("输入的imei不在当前所选仓库")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        sn_imei = WOSerializedListAdd.add_imei(self)
        num = WOSerializedListAdd(drivers)
        num.add_woserlist(Warehouse='API_母仓', imei=sn_imei)
        num = DomAssert(drivers)
        num.assert_att("IMEI/SN Does not exist or does not belong to the current location！")

@allure.feature("WO Serialized Mgt-WO Serialized List")
class TestSearchWoList:
    @allure.story("查询序列化工单所有数据")  # 场景名称
    @allure.title("查询序列化工单所有数据")  # 用例名称
    @allure.description("查询条件都设置为空,查询所有序列化工单数据")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        num = WOSerializedListSearch(drivers)
        num.search_woserlist(scope=all)
        record = num.search_stock(stock=all)
        ValueAssert.value_assert_equal(record[0], record[1],)


    @allure.story("查询序列化工单部分数据")  # 场景名称
    @allure.title("查询印度当月的序列化工单数据")  # 用例名称
    @allure.description("查询条件设置时间为当月，国家选择印度进行查询")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        num = WOSerializedListSearch(drivers)
        num.search_woserlist(scope='part')
        record = num.search_stock(stock='part')
        ValueAssert.value_assert_equal(record[0], record[1],)

if __name__ == '__main__':
    pass

