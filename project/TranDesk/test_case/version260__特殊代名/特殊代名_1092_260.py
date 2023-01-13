import allure
import pytest
@allure.feature("特殊代名_1092")  # 迭代名称
class Teststory_4433:
    @allure.story("特殊字符")  # 用户故事名称
    @allure.title("测试时1")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31007(self, drivers):
        pass


@allure.feature("特殊代名_1092")  # 迭代名称
class Teststory_4443:
    @allure.story("特殊字符333")  # 用户故事名称
    @allure.title("测试2")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31008(self, drivers):
        pass


    @allure.story("特殊字符333")  # 用户故事名称
    @allure.title("用例444")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31013(self, drivers):
        pass


@allure.feature("特殊代名_1092")  # 迭代名称
class Teststory_4431:
    @allure.story("需_求_名_称_异.常处理测试")  # 用户故事名称
    @allure.title("测试1")  # 用例名称
    @allure.description("步骤1:测试1;步骤2:测试2;步骤3:测试3;")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30733(self, drivers):
        pass


if __name__ == '__main__':
    pass
