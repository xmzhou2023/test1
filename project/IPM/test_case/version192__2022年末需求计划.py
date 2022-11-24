import allure
import pytest
@allure.feature("2022年末需求计划")  # 迭代名称
class Teststory_2760:
    @allure.story("高级搜索优化")  # 用户故事名称
    @allure.title("自动化测试跑流程")  # 用例名称
    @allure.description("登录==创建项目")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18778(self, drivers):
        pass


    @allure.story("高级搜索优化")  # 用户故事名称
    @allure.title("IPM流程测试")  # 用例名称
    @allure.description("发起==流程审批==断言")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19625(self, drivers):
        pass


if __name__ == '__main__':
      pass
