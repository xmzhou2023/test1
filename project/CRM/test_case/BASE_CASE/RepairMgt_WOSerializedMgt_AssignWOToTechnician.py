import allure
import pytest
from public.base.assert_ui import *
from project.CRM.page_object.Center_Component import NavPage
from project.CRM.page_object.RepairMgt_WOSerializedMgt_AssignWOToTechnician import *
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@pytest.fixture(scope='module',autouse=True)
def module_fixture(drivers):
    logging.info("前置条件:进入序列化工单列表页")
    user = NavPage(drivers)
    user.refresh_page()
    user.list_search(content='WO Serialized List')
    # user.click_gotonav("Repair Mgt", "WO Serialized Mgt", 'WO Serialized List')
    # sleep(1)
    # user = DomAssert(drivers)
    # user.assert_url("/maintenanceMgt/workorderSerializedMgt/workorderSerializedList")
    yield
    logging.info("后置条件:合起菜单")
    user = NavPage(drivers)
    user.click_gotonav("Repair Mgt")



@allure.feature("WO Serialized Mgt-assignWorkorderToTechnician")
class TestWOSerializedAssignToTech:
    @allure.story("分派技术员") # 场景名称
    @allure.title("从工单列表页复制一个10状态的工单，操作assign select可成功")  # 用例名称
    @allure.description("从工单列表页复制一个10状态的工单，到分派技术员页面查询后勾选，选择对应技术人员后点击assign selected可成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignToTech(drivers)
        word = num.getworkorderno(row=1, column=3, status="Created")
        num = NavPage(drivers)
        num.click_gotonav("Assign WO To Technician")
        num = WOSerializedAssignToTech(drivers)
        num.woassigntotech(workorder=word, row=1, column=2, status="Created")
        num = DomAssert(drivers)
        num.assert_att("Success")

    @allure.story("分派技术员") # 场景名称
    @allure.title("从工单列表页复制一个10状态的工单，操作assign All可成功")  # 用例名称
    @allure.description("从工单列表页复制一个10状态的工单，到分派技术员页面查询单号，选择分派技术员，直接点击assign All可成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignToTech(drivers)
        word= num.getworkorderno(row=1, column=3, status="Created")
        num = NavPage(drivers)
        num.click_gotonav("Assign WO To Technician")
        num = WOSerializedAssignToTech(drivers)
        num.woassigntotech(workorder=word, row=1, column=2, status="Created", scope="All")
        num = DomAssert(drivers)
        num.assert_att("Success")

    @allure.story("分派技术员")  # 场景名称
    @allure.title("非10状态的工单无法操作assign select成功，页面不可找到该工单")  # 用例名称
    @allure.description("从工单列表页复制一个非10状态的工单，到分派技术员页面查询不到")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke # 用例标记
    @pytest.mark.parametrize("status", ["Assigned To Technician", "Repair Completed", "Non Repairable", "Damage"])
    def test_001_003(self, drivers, status):   # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignToTech(drivers)
        word = num.getworkorderno(row=1, column=3, status=status)
        num = NavPage(drivers)
        num.click_gotonav("Assign WO To Technician")
        num = WOSerializedAssignToTech(drivers)
        num1 = num.woassigntotech(workorder=word, row=1, column=2, status=status)
        ValueAssert.value_assert_equal(num1, 0)

    @allure.story("分派技术员")  # 场景名称
    @allure.title("从工单列表页复制一个10状态的工单，操作Assign By Scan以及其弹框页可成功")  # 用例名称
    @allure.description("从工单列表页复制一个10状态的工单，到分派技术员页面查询单号，直接点击Assign By Scan跳转到其弹框页数据填写完整后可操作成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignToTech(drivers)
        word = num.getworkorderno(row=1, column=3, status="Created")
        num = NavPage(drivers)
        num.click_gotonav("Assign WO To Technician")
        num = WOSerializedAssignToTech(drivers)
        num.woassigntotech(workorder=word, row=1, column=2, status="Created", scope="Scan")
        num = DomAssert(drivers)
        num.assert_att("Success")

    @allure.story("分派技术员")  # 场景名称
    @allure.title("从工单列表页复制一个非10状态的工单，操作Assign By Scan以及其弹框页提示报错")  # 用例名称
    @allure.description("从工单列表页复制一个非10状态的工单，到分派技术员页面查询单号，直接点击Assign By Scan跳转到其弹框页数据填写完整后可提示报错")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.parametrize("status", ["Assigned To Technician", "Repair Completed", "Non Repairable", "Damage"])
    def test_001_005(self, drivers, status):  # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignToTech(drivers)
        word = num.getworkorderno(row=1, column=3, status=status)
        num = NavPage(drivers)
        num.click_gotonav("Assign WO To Technician")
        num = WOSerializedAssignToTech(drivers)
        num.woassigntotech(workorder=word, row=1, column=2, status=status, scope="Scan")
        num = DomAssert(drivers)
        num.assert_att("The serialized work order has been assigned")

    @allure.story("分派技术员")  # 场景名称
    @allure.title("从工单列表页复制一个非20状态的工单，操作Re-Assigned不可成功")  # 用例名称
    @allure.description("从工单列表页复制一个非20状态的工单，到分派技术员页Re-Assigned跳转到弹框页输入对应单号后，提示报错")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.parametrize("status", ["Created", "Repair Completed", "Non Repairable", "Damage"])
    def test_002_001(self, drivers, status):  # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignToTech(drivers)
        word = num.getworkorderno(row=1, column=3, status="Created")
        num = NavPage(drivers)
        num.click_gotonav("Assign WO To Technician")
        num = WOSerializedAssignToTech(drivers)
        num.woreassigntotech(workorder=word, status=status)
        num = DomAssert(drivers)
        num.assert_att("cannot be re-assign to technician")

    @allure.story("分派技术员")  # 场景名称
    @allure.title("从工单列表页复制一个20状态的工单，操作Re-Assigned可成功")  # 用例名称
    @allure.description("从工单列表页复制一个20状态的工单，到分派技术员页Re-Assigned跳转到弹框页输入对应单号后填写完整，保存可成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignToTech(drivers)
        word = num.getworkorderno(row=1, column=3, status="Assigned To Technician")
        num = NavPage(drivers)
        num.click_gotonav("Assign WO To Technician")
        num = WOSerializedAssignToTech(drivers)
        num.woreassigntotech(workorder=word, status="Assigned To Technician" )
        num = DomAssert(drivers)
        num.assert_att("Success")


if __name__ == '__main__':
    pass

