from project.IPM.login.login import LoginView
from project.IPM.page_object.AsystemManagement_FlowConfig import *
import allure
import pytest


@allure.feature('IPM-系统管理-流程配置-节点管理')
class TestFlowLayout:
    @allure.story("用户管理-登录用户")
    @allure.title("用户管理-登录用户")
    @allure.description("用户管理-登录用户”")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001(self, drivers):
        """用户管理-登录用户"""
        user = LoginView(drivers)
        user.login(drivers)
        sleep(3)



    @allure.story("角色管理查询_正常场景")
    @allure.title("物料类型查询")
    @allure.description("手机 / 电子元器件 / 滤波器类_334，点击查询按钮，页面数据与数据库查询出的数据一致")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003(self,drivers):
        rolemanagent=RoleManagent(drivers)
        rolemanagent.get_url_f('流程配置URL')
        rolemanagent.Role_Management()
        rolemanagent.RoleManagement_Query_material_type('电子元器件', '滤波器类_334', '2.4G wifi saw')
        rolemanagent.RoleManagement_Query()
        ass= Assert_result(drivers)
        ass.db_assert_elements_equal_Assert_result('角色管理_表单数据获取','流程配置_角色管理_物料类型获取','obj_type_name')

    def test_024(self,drivers):
        rolemanagent = RoleManagent(drivers)
        rolemanagent.get_url_f('流程配置URL')
        rolemanagent.Role_Management()
















if __name__ == '__main__':
    pytest.main('test_B_AystemManagement_FlowConfig.py')

    #allure serve ./project/IPM/test_case/allure-reports
