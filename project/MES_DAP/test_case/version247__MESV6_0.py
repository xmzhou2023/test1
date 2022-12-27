import allure
import pytest
@allure.feature("MESV6_0")  # 迭代名称
class Teststory_4131:
    @allure.story("工具上传软件离线升级记录接口")  # 用户故事名称
    @allure.title("工具上传软件离线升级记录接口参数正确，上传成功，数据正确存储，接口返回正确")  # 用例名称
    @allure.description("SN	SNChipID	ChipID如10b04aab16fe14d79018cf0d03b02c76versionInfo	升级后软件版本如V4.1810.09.18result	升级结果，默认0PASS，1FAILToolVersion	工具版本号subStation	升级电脑名称==所有参数必填SN	SNChipID	ChipID如10b04aab16fe14d79018cf0d03b02c76versionInfo	升级后软件版本如V4.1810.09.18result	升级结果，默认0PASS，1FAILToolVersion	工具版本号subStation	升级电脑名称")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28247(self, drivers):
        pass


if __name__ == '__main__':
      pass
