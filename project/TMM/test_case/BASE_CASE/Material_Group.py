import allure
import pytest

from project.TMM.page_object.Material_Group import MaterialGroupPage

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("物料组") # 模块名称
class TestUtil:
    @allure.story("物料组页面操作") # 场景名称
    @allure.title("切入物料组")  # 用例名称
    @allure.description("进入物料组模块页面")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        project = MaterialGroupPage(drivers)
        MaterialGroupTitle = project.goto_MaterialGroup()
        assert '物料组' in MaterialGroupTitle, '进入物料组模块失败！'

    @allure.story("物料组页面操作")  # 场景名称
    @allure.title("实体名称查询")  # 用例名称
    @allure.description("根据实体名称查询到对应的物料组数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = MaterialGroupPage(drivers)
        project.EntityNameQuery('物料主数据')

    @allure.story("物料组页面操作")  # 场景名称
    @allure.title("物料组查询")  # 用例名称
    @allure.description("根据物料组查询到对应的物料组数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = MaterialGroupPage(drivers)
        project.MaterialGroupQuery('100')

    @allure.story("物料组页面操作")  # 场景名称
    @allure.title("物料组名称查询")  # 用例名称
    @allure.description("根据物料组名称查询到对应的物料组数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = MaterialGroupPage(drivers)
        project.MaterialGroupNameQuery('整机')

    @allure.story("物料组页面操作")  # 场景名称
    @allure.title("数据来源查询")  # 用例名称
    @allure.description("根据数据来源查询到对应的物料组数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = MaterialGroupPage(drivers)
        project.DataFromQuery('TMM')

    @allure.story("物料组页面操作")  # 场景名称
    @allure.title("查询重置")  # 用例名称
    @allure.description("清空所有查询条件，返回全部列表数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = MaterialGroupPage(drivers)
        project.Reset()

    @allure.story("物料组页面操作")  # 场景名称
    @allure.title("新增物料组")  # 用例名称
    @allure.description("新增一个物料组")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_007(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = MaterialGroupPage(drivers)
        AddMaterialGroupTitle = project.AddMaterialGroup('lhjce1_edit', 'lhjce1', 'lhjce1', 'lhjce1')
        assert '新增' in AddMaterialGroupTitle, '进入新增物料组弹窗失败！'



    @allure.story("物料组页面操作")  # 场景名称
    @allure.title("查看物料组")  # 用例名称
    @allure.description("选择一个物料组，点击查看按钮，查看物料组内容")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_008(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = MaterialGroupPage(drivers)
        ViewMaterialGroupTitle = project.MaterialGroupView()
        assert '查看' in ViewMaterialGroupTitle, '进入查看物料组弹窗失败！'

    @allure.story("物料组页面操作")  # 场景名称
    @allure.title("刷新SAP最新物料组")  # 用例名称
    @allure.description("点击刷新SAP最新物料组按钮，对物料组列表进行更新操作")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_009(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = MaterialGroupPage(drivers)
        project.MaterialGroupFresh()

if __name__ == '__main__':
    pytest.main(['project/TMM/testcase/Entity.py'])