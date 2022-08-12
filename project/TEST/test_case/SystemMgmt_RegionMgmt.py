import allure
import pytest
from project.DRP.page_object.Center_Component import NavPage
from project.TEST.page_object.SystemMgmt_RegionMgmt import AreaPage
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

# @allure.feature("脚本名称") # 模块名称
# class TestUtil:
#     @allure.story("二级标题") # 场景名称
#     @allure.title("三级标题")  # 用例名称
#     @allure.description("用例描述")
#     @allure.severity("normal")  # 用例等级
#     @pytest.mark.smoke # 用例标记
#     def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
#         pass
@allure.feature("系统管理-区域管理")
class TestExportArea:

    # @allure.story("新增区域子层级")
    # @allure.title("新增区域子层级")
    # @allure.description("新增区域子层级")
    # @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.FT
    # def test_001_001(self, drivers):
    #     user = NavPage(drivers)
    #     user.click_gotonav("系统管理", "区域管理")
    #     user = AreaPage(drivers)
    #     user.goto_tree('itel事业部', 'itel事业部', 'itel事业部')
    #     user.create_area()
    #     ##新增区域
    #     user.add_country_area()
    #     # 查询区域
    #     user.input_search_name("索马里兰")
    #     # 删除区域
    #     user.del_area()
    #     user.sure_del_area()

    @allure.story("新增区域配置")
    @allure.title("新增区域配置")
    @allure.description("新增区域配置")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部', 'itel事业部')
        user.create_area()
        ##新增区域配置
        user.input_Zh_name("自动化test")
        user.input_En_name("autotest")
        user.save_area()
        # 删除区域配置
        user.del_area()
        user.sure_del_area()

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
