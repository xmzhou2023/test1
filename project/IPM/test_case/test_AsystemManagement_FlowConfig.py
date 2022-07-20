from project.IPM.login.login import LoginView
from project.IPM.page_object.AsystemManagement_FlowConfig import *
import allure
import pytest

@allure.feature('IPM-系统管理-流程配置-节点管理')
class TestFlowLayout:
    @allure.story("用户管理-登录用户")
    @allure.title("用户管理-登录用户")
    @allure.description("用户管理-登录用户”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_001(self, drivers):
        """用户管理-登录用户"""
        user = LoginView(drivers)
        user.login(drivers)
        sleep(3)



    @allure.story("新增异常场景")
    @allure.title("说明/节点角色与节点名称不匹配")
    @allure.description("属性说明/节点角色与节点名称不匹配，点击提交提示：”")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_002(self,drivers):
        home=FlowLayout()
        home.click_home(drivers)
        sleep(2)
        add = RoleManagement(drivers)
        add.db_updata(databases=db_ipm_config_uat,sql='更改手机物料发起节点为删除状态')

        add.add_RoleManagent()
        add.NodeName_RoleManagent('1','发起节点')
        add.sort_RoleManagent('1','0')
        add.NodeRole_RoleManagent('1','项目经理')
        add.Preservation_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='节点与节点角色不匹配实际结果',
                                 expected_results='节点与节点角色不匹配预期结果')
    @allure.story("新增正常场景")
    @allure.title("新增成功")
    @allure.description("属性说明/节点管理新增成功”")
    @allure.severity("critical")
    @pytest.mark.smoke
    def test_003(self,drivers):
        add = RoleManagement(drivers)
        add.db_updata(databases=db_ipm_config_uat,sql='更改手机物料发起节点为删除状态')
        add.url_RoleManagent()
        sleep(2)
        add.add_RoleManagent()
        add.NodeName_RoleManagent('1','发起节点')
        add.sort_RoleManagent('1','0')
        add.Preservation_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='新增成功实际结果',
                                 expected_results='节点新增成功预期结果')

    @allure.story("新增节点异常场景")
    @allure.title("点击删除，提示，是否删除该数据")
    @allure.description("删除按钮，未启用的数据可见；点击删除，提示，是否删除该数据”")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_004(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.delete_RoleManagent('1')
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='删除节点提示语',
                                 expected_results='删除节点提示语')


    @allure.story("新增节点异常场景")
    @allure.title("在删除提示窗口点击取消")
    @allure.description("删除按钮，未启用的数据可见；点击删除，提示，是否删除该数据，点击取消数据不丢失”")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_005(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.delete_RoleManagent('1')
        add.cancek_RoleManagent()
        sleep(2)
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='获取NO1的节点名称',
                                 expected_results='NO1的节点名称')

    @allure.story("新增节点异常场景")
    @allure.title("点击确认角色管理不显示发起节点")
    @allure.description("删除按钮，未启用的数据可见；点击删除，提示，是否删除该数据，点击确认角色管理不显示发起节点”")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_006(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.delete_RoleManagent('1')
        add.cinfirm_RoleManagent()
        add.url_RoleManagent()
        sleep(2)
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='获取NO1的节点名称',
                                 expected_results='test_007NO1的节点名称')


    @allure.story("新增节点正常场景")
    @allure.title("表格中新增一条数据")
    @allure.description("新增：点击“新增”按钮，表格中新增一条数据（显示在第一行）")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_007(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.add_RoleManagent()
        add.NodeName_RoleManagent('1','发起节点')
        add.sort_RoleManagent('1', '0')
        add.Preservation_RoleManagent()
        sleep(2)
        add.add_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='span', choice='保存', expected_results='保存')


    @allure.story("新增节点异常场景")
    @allure.title("不可同时新增或者编辑多条数据")
    @allure.description("节点设置/新增：不可同时新增或者编辑多条数据")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_008(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.add_RoleManagent()
        add.add_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='未保存新增节点再节点新增按钮实际结果',
                                 expected_results='未保存新增节点再点击新增按钮预期结果')
        sleep(3)
        add.rop_down_box('编辑','2')
        ass.assert_element_equal(actual_results='未保存新增节点实际结果',
                                 expected_results='未保存新增节点预期结果')

    @allure.story("新增节点异常场景")
    @allure.title("新增必填项未填，提示")
    @allure.description("属性说明/节点名称：未填，提示")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_09(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.add_RoleManagent()
        add.sort_RoleManagent('1', '0')
        add.Preservation_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='节点名称未填写实际结果',
                                 expected_results='节点名称未填写预期结果')


    @allure.story("新增节点异常场景")
    @allure.title("节点名称：下拉，单选，必填")
    @allure.description("属性说明/节点名称：下拉，单选，必填")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_010(self,drivers):
            add = RoleManagement(drivers)
            add.url_RoleManagent()
            sleep(2)
            add.add_RoleManagent()
            add.NodeName_RoleManagent('1','发起节点')
            ass = Assert_result(drivers)
            ass.assert_element_equal(actual_results='节点名称',
                                     choice='1',
                                     get_attribute='value',
                                     expected_results='节点名称选择预期结果')


    @allure.story("新增节点异常场景")
    @allure.title("排序未填写")
    @allure.description("属性说明/排序：排序未填写")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_011(self,drivers):
            add = RoleManagement(drivers)
            add.url_RoleManagent()
            sleep(2)
            add.add_RoleManagent()
            add.NodeName_RoleManagent('1','发起节点')
            add.Preservation_RoleManagent()
            ass = Assert_result(drivers)
            ass.assert_element_equal(actual_results='排序未填写实际结果',
                                     expected_results='排序未填写预期结果')


    @allure.story("新增节点异常场景")
    @allure.title("排序：特殊字符校验")
    @allure.description("属性说明/排序：特殊字符校验，double数字类型如非 ‘1.1、1.2等")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_012(self,drivers):
            add = RoleManagement(drivers)
            add.url_RoleManagent()
            sleep(2)
            add.add_RoleManagent()
            add.NodeName_RoleManagent('1','发起节点')
            add.input_texts(elements='排序', choice='1', text='项目经理')
            ass = Assert_result(drivers)
            ass.assert_element_equal(actual_results='排序',
                                     choice='1',
                                     get_attribute='value',
                                     expected_results='排序特殊字符预期结果')

    @allure.story("新增节点异常场景")
    @allure.title("新增节点已存在")
    @allure.description("属性说明/节点名称重复提示：当前流程配置已存在该物料类型的配置")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_013(self, drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.add_RoleManagent()
        add.NodeName_RoleManagent('1','发起节点')
        add.sort_RoleManagent('1','0')
        add.Preservation_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='节点名称重复实际结果',
                                 expected_results='节点名称重复预期结果')


    @allure.story("新增节点异常场景")
    @allure.title("新增节点状态默认")
    @allure.description("新增节点配置默认为未启用")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_014(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='状态默认实际结果',
                                 expected_results='状态默认预期结果')


    @allure.story("新增节点异常场景")
    @allure.title("未启用可删除可编辑操作")
    @allure.description("未启用：当状态未启用，此节点可启用可删除可编辑操作")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_015(self,drivers):
        ass = Assert_result(drivers)
        ass.assert_elements_equal(actual_results='未启用节点编辑/删除按钮',
                                 expected_results='未启用节点显示编辑/删除按钮预期结果')


    @allure.story("新增节点正常场景")
    @allure.title("启用节点时弹窗询问")
    @allure.description("启用一个节点时，提示：该操作将不可逆,启用后将无法恢复，是否继续?")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_016(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.state_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='节点启用提示',
                                 expected_results='节点启用预期结果')



    @allure.story("新增节点正常场景")
    @allure.title("启用节点窗口中点击取消")
    @allure.description("启用一个节点时，提示：该操作将不可逆,启用后将无法恢复，是否继续?后点击取消?")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_017(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.state_RoleManagent()
        add.cancek_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='状态默认实际结果',
                                 expected_results='状态默认预期结果')
    @allure.story("新增节点正常场景")
    @allure.title("启用节点窗口中点击确认")
    @allure.description("启用一个节点时，提示：该操作将不可逆,启用后将无法恢复，是否继续?后点击确认提示：状态成功修改为启用")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_018(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.state_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='节点启用提示',
                                 expected_results='节点启用预期结果')
        add.cinfirm_RoleManagent()
        ass.assert_element_equal(actual_results='状态启用提示',
                                 expected_results='状态启用提示')


    @allure.story("状态修改")
    @allure.title("状态修改为禁用")
    @allure.description("禁用一个节点时，提示：状态成功修改为禁用")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_019(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.state_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='状态禁用提示',
                                 expected_results='状态禁用提示')


    @allure.story("编辑")
    @allure.title("点击编辑")
    @allure.description("点击编辑按钮打开编辑功能")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_020(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.Edit_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='span', choice='保存', expected_results='保存')




    @allure.story("编辑")
    @allure.title("编辑状态中更改状态")
    @allure.description("在编辑状态中更改状态，更改成功")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_021(self,drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.Edit_RoleManagent()
        add.state_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='状态启用提示',
                                 expected_results='状态启用提示')

    @allure.story("编辑")
    @allure.title("修改状态为禁用")
    @allure.description("节点名称为发起节点的状态为禁用，在角色管理表头不显示发起节点")
    @allure.severity("critical")
    @pytest.mark.smoke
    def test_022(self, drivers):
        add = RoleManagement(drivers)
        add_two=RoleManagent(drivers)
        sleep(2)
        add.db_updata(databases=db_ipm_config_uat,sql='修改状态为禁用')
        sleep(3)
        add.url_RoleManagent()
        sleep(1)
        add_two.Role_Management()
        ass = Assert_result(drivers)
        ass.many_db_assert_element_equal(actual_results='角色管理表头获取',
                                         databases_one=db_ipm_config_uat,
                                         sql_one='流程配置_角色管理获取状态为启用的手机物料',
                                         listname_one='node_bid',
                                         databases_two=hulk_workflow_transfer_uat,
                                         sql_two='流程配置_角色管理_将启用手机物料的key转为中文名',
                                         listname_two='field_name',
                                         choice=None,
                                         default='流程配置_角色管理表头默认'
                                         )



    @allure.story("编辑")
    @allure.title("修改状态为启用")
    @allure.description("编辑状态为启用后点击保存，提示：编辑成功")
    @allure.severity("critical")
    @pytest.mark.smoke
    def test_023(self, drivers):
        add = RoleManagement(drivers)
        add.url_RoleManagent()
        sleep(2)
        add.Edit_RoleManagent()
        add.state_RoleManagent()
        add.Preservation_RoleManagent()
        ass = Assert_result(drivers)
        ass.assert_element_equal(actual_results='编辑成功',
                                 expected_results='编辑成功')






#角色管理



if __name__ == '__main__':
    pytest.main('test_AystemManagement_FlowConfig.py')
# blocker\critical\normal\minor\trivial

    #allure serve ./project/IPM/test_case/allure-reports
