import allure
import pytest
@allure.feature("自动化管理_37_场景管理_259")  # 迭代名称
class Teststory_4078:
    @allure.story("用例管理迭代需求CRM试验")  # 用户故事名称
    @allure.title("TranTest自动化测试用例1")  # 用例名称
    @allure.description("步骤1:步骤一内容;步骤2:步骤二内容;步骤3:步骤三内容;")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28234(self, drivers):
        pass


    @allure.story("用例管理迭代需求CRM试验")  # 用户故事名称
    @allure.title("传测自动化测试用例2")  # 用例名称
    @allure.description("步骤1:程序执行步骤1;步骤2:程序执行步骤二;步骤3:程序执行步骤三;")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28235(self, drivers):
        pass


if __name__ == '__main__':
    pass
