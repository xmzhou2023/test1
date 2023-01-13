import allure
import pytest
@allure.feature("巡店管理_908")  # 迭代名称
class Teststory_4184:
    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("原删除内容X按钮变更为扫描按钮，点击扫描按钮转跳至门店扫描页")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30492(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("当搜索框内容不为空，扫描按钮变更为删除内容按钮点击后可清空搜索内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30493(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("手动输入点击键盘Search按钮，根据输入内容进行模糊精确查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30494(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("扫描门店二维码成功自动填充根据填充的门店ID进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30495(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("扫描的门店二维码为授权的门店数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30496(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("当扫描的门店二维码与登录人无授权关系时扫描填充搜索无结果显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30497(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("扫描成功的门店ID填充至门店搜索框，并根据门店ID进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30498(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("扫描成功查询出门店可进行操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30499(self, drivers):
        pass


if __name__ == '__main__':
      pass
