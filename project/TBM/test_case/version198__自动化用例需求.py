import allure
import pytest
@allure.feature("自动化用例需求")  # 迭代名称
class Teststory_3247:
    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=创建流程成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20149(self, drivers):
        pass


if __name__ == '__main__':
      pass
