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
    sleep(1)
    logging.info("前置条件:进入序列化工单列表页")
    user = NavPage(drivers)
    user.refresh()
    sleep(1)
    user.click_gotonav("Repair Mgt", "WO Serialized Mgt", 'WO Serialized List')
    user = DomAssert(drivers)
    user.assert_url("/maintenanceMgt/workorderSerializedMgt/workorderSerializedList")
    yield
    logging.info("后置条件:合起菜单")
    user = NavPage(drivers)
    user.click_gotonav("Repair Mgt")



@allure.feature("WO Serialized Mgt-assignWorkorderToTechnician")
class TestWOSerializedAssignToTech:
    @allure.story("工单状态允许分派技术员时，可分派成功") # 场景名称
    @allure.title("从工单列表页复制一个10状态的工单，操作assign select可成功")  # 用例名称
    @allure.description("从工单列表页复制一个10状态的工单，到分派技术员页面查询后勾选，选择对应技术人员后点击assign selected可成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignToTech(drivers)
        word= num.getworkorderno(row=1, column=3, status="Created")
        num = NavPage(drivers)
        num.click_gotonav("Assign WO To Technician")
        num = WOSerializedAssignToTech(drivers)
        num.woassigntotech(workorder=word, row=1, column=2, status="Created")
        num = DomAssert(drivers)
        num.assert_att("Success")

    @allure.story("工单状态不允许分派技术员时，无法操作分派技术员")  # 场景名称
    @allure.title("非10状态的工单无法操作assign select 成功，页面不可找到该工单")  # 用例名称
    @allure.description("从工单列表页复制一个非10状态的工单，到分派技术员页面查询不到")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke # 用例标记
    @pytest.mark.parametrize("status", ["Assigned To Technician", "Repair Completed", "Non Repairable", "Damage"])
    def test_001_002(self, drivers, status):   # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignToTech(drivers)
        word = num.getworkorderno(row=1, column=3, status=status)
        num = NavPage(drivers)
        num.click_gotonav("Assign WO To Technician")
        num = WOSerializedAssignToTech(drivers)
        num1 = num.woassigntotech(workorder=word, row=1, column=2, status=status)
        ValueAssert.value_assert_equal(num1, 0)




if __name__ == '__main__':
    pass

