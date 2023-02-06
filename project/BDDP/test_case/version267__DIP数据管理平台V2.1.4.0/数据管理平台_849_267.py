import allure
import pytest
@allure.feature("数据管理平台_849")  # 迭代名称
class Teststory_4526:
    @allure.story("授权用户组件更新")  # 用户故事名称
    @allure.title("单个用户授权验证")  # 用例名称
    @allure.description("步骤1:登录数据管理平台后台;步骤2:点击角色管理;步骤3:点击新增角色，填写相关资料;步骤4:输入工号检索单个用户进行授权;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_32006(self, drivers):
        pass


    @allure.story("授权用户组件更新")  # 用户故事名称
    @allure.title("批量用户授权验证")  # 用例名称
    @allure.description("步骤1:登录数据管理平台后台;步骤2:点击角色管理;步骤3:点击新增角色，填写相关资料;步骤4:模糊工号检索多个用户进行批量授权;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_32007(self, drivers):
        pass


    @allure.story("授权用户组件更新")  # 用户故事名称
    @allure.title("单个用户授权成功后，供应链移动端平台登录验证")  # 用例名称
    @allure.description("步骤1:登录数据管理平台后台;步骤2:点击角色管理;步骤3:点击新增角色，填写相关资料;步骤4:输入工号检索单个用户进行授权;步骤5:用此授权用户工号登录供应链移动端平台;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_32009(self, drivers):
        pass


    @allure.story("授权用户组件更新")  # 用户故事名称
    @allure.title("单个用户授权成功后，绩效看板平台登录验证")  # 用例名称
    @allure.description("步骤1:登录数据管理平台后台;步骤2:点击角色管理;步骤3:点击新增角色，填写相关资料;步骤4:输入工号检索单个用户进行授权;步骤5:用此授权用户工号登录绩效看板平台;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_32010(self, drivers):
        pass


    @allure.story("授权用户组件更新")  # 用户故事名称
    @allure.title("单个用户授权成功后，营销移动端平台登录验证")  # 用例名称
    @allure.description("步骤1:登录数据管理平台后台;步骤2:点击角色管理;步骤3:点击新增角色，填写相关资料;步骤4:输入工号检索单个用户进行授权;步骤5:用此授权用户工号登录营销移动端平台;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_32011(self, drivers):
        pass


    @allure.story("授权用户组件更新")  # 用户故事名称
    @allure.title("同一用户多次授权验证")  # 用例名称
    @allure.description("步骤1:登录数据管理平台后台;步骤2:点击角色管理;步骤3:点击新增角色，填写相关资料;步骤4:输入工号检索单个用户进行授权;步骤5:再次输入此工号检索单个用户进行授权，;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_32013(self, drivers):
        pass


    @allure.story("授权用户组件更新")  # 用户故事名称
    @allure.title("ui界面验证")  # 用例名称
    @allure.description("步骤1:登录数据管理平台后台;步骤2:点击角色管理;步骤3:点击新增角色，填写相关资料;步骤4:输入工号检索单个用户进行授权;步骤5:查看相关界面是否与需求一致;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_32015(self, drivers):
        pass


    @allure.story("授权用户组件更新")  # 用户故事名称
    @allure.title("易用性验证")  # 用例名称
    @allure.description("步骤1:登录数据管理平台后台;步骤2:点击角色管理;步骤3:点击新增角色，填写相关资料;步骤4:输入工号检索单个用户进行授权;步骤5:检验其易用性;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_32052(self, drivers):
        pass


if __name__ == '__main__':
      pass
