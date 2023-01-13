import allure
import pytest
from public.base.assert_ui import *
from project.CRM.page_object.Center_Component import NavPage
from project.CRM.page_object.RepairMgt_WOSerializedMgt_AssignSpareToWO import *
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
    yield
    logging.info("后置条件:合起菜单")
    user = NavPage(drivers)
    user.click_gotonav("Repair Mgt")



@allure.feature("WOSerializedMgt-AssignSpareToWO")
class TestWOSerializedAssignToWO:
    @allure.story("工单状态非20时，操作派料失败")  # 场景名称
    @allure.title("从工单列表页复制非20状态的工单，进行派料时提示报错")  # 用例名称
    @allure.description("从工单列表页复制一个非20状态的工单，点击add或者直接从操作区输入工单号，确认后提示报错")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.parametrize("status", ["Created", "Repair Completed", "Non Repairable", "Damage"])
    def test_001_001(self, drivers, status):  # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignSpareToWO(drivers)
        word = num.getworkorderno(row=1, column=3, status=status)
        num = NavPage(drivers)
        num.click_gotonav("Assign Spare To WO")
        num = WOSerializedAssignSpareToWO(drivers)
        num.woassigntowo(workorder=word,  status=status)
        num = DomAssert(drivers)
        num.assert_att("not allowed in the current status of Serialize workorder")

    @allure.story("成功进入派料新增页")  # 场景名称
    @allure.title("从工单列表页复制20状态的工单，进行派料时可正常跳转")  # 用例名称
    @allure.description("从工单列表页复制一个20状态的工单，点击add或者直接从操作区输入工单号，确认可跳转到派料页")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    # @pytest.mark.parametrize("status", ["Created", "Repair Completed", "Non Repairable", "Damage"])
    def test_001_002(self, drivers, status):  # 用例名称取名规范'test+场景编号+用例编号'
        num = NavPage(drivers)
        num.click_gotonav("WO Serialized List")
        num = WOSerializedAssignSpareToWO(drivers)
        word = num.getworkorderno(row=1, column=3, status="Assigned To Technician")
        num = NavPage(drivers)
        num.click_gotonav("Assign Spare To WO")
        num = WOSerializedAssignSpareToWO(drivers)
        num.woassigntowo(workorder=word)
        # num.woassigntowo(workorder=word, status="Assigned To Technician")
        num = DomAssert(drivers)
        num.assert_att("Spare Parts")








if __name__ == '__main__':
    pass

