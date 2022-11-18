import allure
import pytest
@allure.feature("V3_0_1计划")  # 迭代名称
class Teststory_2467:
    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台1")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18519(self, drivers):
        pass


    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台2")  # 用例名称
    @allure.description("到用户管理页面查询工号==到用户管理页面查询姓名")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18522(self, drivers):
        pass


    @allure.story("新版DRP权限调整切面部分")  # 用户故事名称
    @allure.title("测试平台3")  # 用例名称
    @allure.description("工号查询==姓名查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18540(self, drivers):
        pass


if __name__ == '__main__':
      pass
