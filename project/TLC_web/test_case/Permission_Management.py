import pytest
from public.base.assert_ui import *
from project.TLC_web.page_object.Center_Component import NavPage
from project.TLC_web.page_object.Permission_Management import Permission

# 卡片中心-卡片属性
@allure.feature("新增角色")
class TestAddRole:
    # 新增角色
    @allure.story("角色权限")
    @allure.title("新增角色")
    @allure.description("‘新增角色’新增成功")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.smoke
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "权限管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/set")
        user = Permission(drivers)
        user.click_roletab()
        user.add_role()
        user.input_rolename(input_rolename='autozz006')
        user.save_button("角色新增正例")
        user = DomAssert(drivers)
        user.assert_exact_att("autozz006")

    @allure.story("角色权限")
    @allure.title("新增角色弹框取消按钮操作")
    @allure.description("‘新增角色’弹框取消按钮验证")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "权限管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/set")
        user = Permission(drivers)
        user.click_roletab()
        user.add_role()
        user.cancel_button()

    @allure.story("角色权限")
    @allure.title("新增角色弹框关闭按钮操作")
    @allure.description("‘新增角色’弹框关闭按钮验证")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    def test_001_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "权限管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/set")
        user = Permission(drivers)
        user.click_roletab()
        user.add_role()
        user.close_button()

    @allure.story("角色权限")
    @allure.title("新增角色弹框关闭按钮操作")
    @allure.description("‘新增角色’弹框关闭按钮验证")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    def test_001_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "权限管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/set")
        user = Permission(drivers)
        user.click_roletab()
        user.add_role()
        user.input_rolename(input_rolename='')
        user.save_button("角色新增反例")


if __name__ == '__main__':
    pytest.main(['p'])

