import allure
import pytest
@allure.feature("自_27_246")  # 迭代名称
class Teststory_4209:


    @allure.story("平台整体功能联调与维稳")  # 用户故事名称
    @allure.title("测测测444")  # 用例名称
    @allure.description("步骤1:步骤1;步骤2:步骤2;步骤3:步骤3;")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17(self, drivers):
        print('123')

    @allure.story("平台整体功能联调与维稳")  # 用户故事名称
    @allure.title("测测测3")  # 用例名称
    @allure.description("步骤1:步骤1;步骤2:步骤2;步骤3:步骤3;")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18(self, drivers):
        print('123')


if __name__ == '__main__':
      pass
