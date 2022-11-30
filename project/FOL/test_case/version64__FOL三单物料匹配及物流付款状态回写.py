import allure
import pytest
@allure.feature("FOL三单物料匹配及物流付款状态回写")  # 迭代名称
class Teststory_321:
    @allure.story("【应付】三单匹配物流编码分组逻辑修改")  # 用户故事名称
    @allure.title("物料编码首尾为7，三单匹配物料编码的前11位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1751(self, drivers):
        pass


    @allure.story("【应付】三单匹配物流编码分组逻辑修改")  # 用户故事名称
    @allure.title("物料编码首位不为7，三单匹配物料编码的前8位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1752(self, drivers):
        pass


if __name__ == '__main__':
      pass
