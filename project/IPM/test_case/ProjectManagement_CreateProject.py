import allure
import pytest
from project.IPM.page_object.ProjectManagement_CreateProject import *
from project.IPM.page_base.assert_pubic import *

@allure.feature("项目管理")  # 迭代名称
class Teststory_p:
    @allure.story("初始化页面")  # 用户故事名称
    @allure.title("")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001(self,drivers):
        # now_times = strftime('%Y-%m-%d%H:%M:%S')
        # test=CreateProject(drivers)
        # test.get_url_project()
        # test.Create_project('保存','IT项目模板',f'IPM自动化编辑测试{now_times}',f'IPM自动化项目描述{now_times}')
        # test.project_entrance(f'IPM自动化编辑测试{now_times}',now_times)
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        test=CreateProject(drivers)
        test.get_url_project()
        test.Create_project('保存','IT项目模板',f'IPM自动化编辑测试{now_times}',f'IPM自动化项目描述{now_times}')
        test.enter_the_project(f'IPM自动化编辑测试{now_times}')
        test.click_edit()
        test.Start_project()
        ass=Assert_result(drivers)
        ass.assert_toast('断言项目启动成功','启动成功!')
        test.close_switch(-1)

if __name__ == '__main__':
    pytest.main(['ProjectManagement_CreateProject.py'])

