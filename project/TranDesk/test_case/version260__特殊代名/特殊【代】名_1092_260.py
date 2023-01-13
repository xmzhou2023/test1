import allure
import pytest
from project.TranDesk.page_object.Center_Component import UserPage
@allure.feature("特殊【代】名_1092")  # 迭代名称
class Teststory_4443:
    @allure.story("'特'殊'字'符'3'3'3'")  # 用户故事名称
    @allure.title("测试2")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31008(self, drivers):
        user = UserPage(drivers)


    @allure.story("'特'殊'字'符'3'3'3'")  # 用户故事名称
    @allure.title("用例444")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31013(self, drivers):
        user = UserPage(drivers)


if __name__ == '__main__':
    pass
