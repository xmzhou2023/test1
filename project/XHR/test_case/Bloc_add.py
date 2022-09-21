import allure
import pytest

#from project.XHR.page_object.XHR import XHR
from public.base.assert_ui import DomAssert
from project.XHR.page_object.Bloc_add import Bloc_add

@allure.feature("新增集团方案") # 模块名称
class TestUtil:
    @allure.story("新增集团方案")  # 场景名称
    @allure.title("薪酬配置界面，新增集团方案")  # 用例名称
    @allure.description("薪酬配置界面进入集团方案，点击新增")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 新增集团方案
        user = Bloc_add(drivers)
        user.click_menu()
        user.click_Bloc()  # 点击集团方案
        user.add_Bloc()
        user.Bloc_Code('6911t')  # 输入集团方案编码
        user.Bloc_Name('123F')
        user.Bloc_Date('2022-08-05')
        user.Bloc_Status('启用')
        user.Bloc_Confirm()
        #user.Bloc_delete('123F(691t)')  # 删除集团方案，使其为一闭环
        DomAssert(drivers).assert_att('请输入4位方案编码，由数字、字母组成')

if __name__ == '__main__':
    pytest.main(['project/XHR/test_case/Bloc_add.py'])
