import allure
import pytest

from project.TBM.page_object.KeyComponent_KeyComponentSearch import KeyComponentsSearch

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""


@allure.feature("关键器件-关键器件查询") # 模块名称
class TestCreateProcess:
    @allure.story("创建流程")  # 场景名称
    @allure.title("进入关键器件修订发起页面,查看关键器件-业务审核-维护关键器件显示是否正确")  # 用例名称
    @allure.description("进入关键器件修订发起页面，查看业务审核中维护关键器件部分的内容是否正确（例如摄像头+闪光灯，硬件电子料-基带）")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage_click_menu()
        user.click_operate('50A710U', '修订')
        user.click_key('摄像头+闪光灯')
        user.click_revise_comfirm()
        user.assert_review('摄像头+闪光灯')
        user.assert_review('硬件电子料-基带', False)
        user.refresh_webpage_click_menu()
        user.click_operate('50A710U', '修订')
        user.click_key('硬件电子料-基带')
        user.click_revise_comfirm()
        user.assert_review('摄像头+闪光灯', False)
        user.assert_review('硬件电子料-基带')
        user.refresh_webpage_click_menu()
        user.click_operate('50A710U', '修订')
        user.click_key('摄像头+闪光灯')
        user.click_key('硬件电子料-基带')
        user.click_revise_comfirm()
        user.assert_review('摄像头+闪光灯')
        user.assert_review('硬件电子料-基带')


@allure.feature("关键器件-关键器件查询")
class TestCreateProcessExceptionScenario:
    @allure.story("创建流程异常场景")
    @allure.title("请勿重复维护关键器件角色！")  # 用例名称
    @allure.description("进入关键器件修订发起页面，选择业务审核中维护关键器件部分的人员为同一个人，点击提交，提示请勿重复维护关键器件角色！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_001(self, drivers):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage_click_menu()
        user.click_operate('50A710U', '修订')
        user.click_key('摄像头+闪光灯')
        user.click_key('硬件电子料-基带')
        user.click_revise_comfirm()
        user.click_add_submit()
        user.assert_toast('请勿重复维护关键器件角色！')
if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
