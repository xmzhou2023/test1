import allure
import pytest
@allure.feature("项目管理")  # 迭代名称
class Teststory_3259:
    @allure.story("创建项目")  # 用户故事名称
    @allure.title("新增项目成功")  # 用例名称
    @allure.description("点击新增==输入项目信息==保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20708(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3275:
    @allure.story("基本信息")  # 用户故事名称
    @allure.title("必填项填写完成保存成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20711(self, drivers):
        pass


if __name__ == '__main__':
      pass
