import allure
import pytest
@allure.feature("自动化管理_37")  # 迭代名称
class Teststory_4206:
    @allure.story("平台整体功能联调与维稳")  # 用户故事名称
    @allure.title("测测测1")  # 用例名称
    @allure.description("步骤1:步骤1;步骤2:步骤2;步骤3:步骤3;")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30739(self, drivers):
        pass


if __name__ == '__main__':
    pass
