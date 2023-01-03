import allure
import pytest
@allure.feature("B001R001V002SP008")  # 迭代名称
class Teststory_4078:
    @allure.story("用例管理迭代需求CRM试验")  # 用户故事名称
    @allure.title("TranTest自动化测试用例1")  # 用例名称
    @allure.description("123==123==123==步骤1==步骤2==步骤3==步骤一内容==步骤二内容==步骤三内容==步骤一内容==步骤二内容==步骤三内容")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28234(self, drivers):
        pass


    @allure.story("用例管理迭代需求CRM试验")  # 用户故事名称
    @allure.title("传测自动化测试用例2")  # 用例名称
    @allure.description("123==123==123==程序执行步骤一==程序执行步骤二==程序执行步骤三")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28235(self, drivers):
        pass


if __name__ == '__main__':
      pass
