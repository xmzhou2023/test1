import allure
import pytest
from project.XHR.page_object.filter import Filter
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""


@allure.feature("组织人事/职员管理")  # 模块名称
class TestUtil:
    @allure.story("筛选导出数据")  # 场景名称
    @allure.title("导出")  # 用例名称
    @allure.description(
        "在当前页面，任意选择一位职员，点击员工档案图标，页面跳转到此员工详细页面。操作导出档案，数据导出与员工详细页面显示一致")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = Filter(drivers)
        user.click_menu('组织人事')
        user.click_filter()
        user.input_filter_info('向往', '员工')
        user.click_search('查询')
        user.click_error()
        user.click_more('导出')
        user.click_reset('重置')
        # DomAssert.assert_filename()
