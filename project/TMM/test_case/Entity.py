import allure
import pytest

from project.TMM.page_object.Entity import EntityPage

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("实体") # 模块名称
class TestUtil:
    @allure.story("实体页面操作") # 场景名称
    @allure.title("切入实体")  # 用例名称
    @allure.description("进入实体模块页面")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        project = EntityPage(drivers)
        EntityTitle = project.GotoEntity()
        assert '实体' in EntityTitle, '进入实体模块失败！'


    @allure.story("实体页面操作")  # 场景名称
    @allure.title("实体名称查询")  # 用例名称
    @allure.description("查询想要查看的实体信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = EntityPage(drivers)
        project.EntityQuery('123')



    @allure.story("实体页面操作")  # 场景名称
    @allure.title("实体名称重置")  # 用例名称
    @allure.description("清除实体名称查询框的内容")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = EntityPage(drivers)
        project.EntityReset()

    @allure.story("实体页面操作")  # 场景名称
    @allure.title("新增实体")  # 用例名称
    @allure.description("新增一条新的实体")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = EntityPage(drivers)
        AddEntityTitle = project.AddEntity('lhjce1', 'lhjce1')
        assert '保存' in AddEntityTitle, '进入实体新增弹窗失败！'


    @allure.story("实体页面操作")  # 场景名称
    @allure.title("编辑实体")  # 用例名称
    @allure.description("编辑一条历史实体")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = EntityPage(drivers)
        EditEntityTitle = project.EditEntity('lhjce1_edit', 'lhjce1_edit')
        assert '实体名称' in EditEntityTitle, '进入实体编辑弹窗失败！'

    @allure.story("实体页面操作")  # 场景名称
    @allure.title("查看实体")  # 用例名称
    @allure.description("查看一条历史实体")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = EntityPage(drivers)
        ViewEntityTitle = project.ViewEntity()
        assert '返回' in ViewEntityTitle, '进入实体查看弹窗失败！'

if __name__ == '__main__':
    pytest.main(['project/TMM/testcase/Entity.py'])
