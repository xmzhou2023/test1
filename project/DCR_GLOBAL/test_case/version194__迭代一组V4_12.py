import allure
import pytest
@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_2888:
    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR同步用户状态为禁用，不清除该账号授权")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20823(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR状态为在职，但用户中心状态为离职的外部员工	更新员工离职状态、Updater、UpdaterDate、OffServiceUpdater、OffServiceDate")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20824(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR状态为在职，但用户中心状态为离职的外部员工	不解除员工客户、品牌、仓库、门店关系（记录日志）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20825(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR状态是离职，用户中心在职状态的外部员工	不更新DCR外部账号的状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20826(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR同步用护中心禁用状态	用户限制登录，不重置密码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20827(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR同步用护中心禁用状态	再次启用后重置密码可以登录，用户授权依然在")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20828(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("批量选择用户点击重置密码，如果有内部账号，提示Transsionaccountcan039tberesetpasswordintheDCR,plscontactITservice，重置失败")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20829(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("批量选择用户点击重置密码，如果有已禁用的账号，提示Disableaccountcan039tberesetpassword,plsenableitfirst，重置失败")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20830(self, drivers):
        pass


@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_3125:
    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("1、返利对象customer中SchemeWise增加激活维度Activation不考虑多等级及时间重选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21139(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("2、SchemeWise选择了Activation，SchemeType下拉内容仅有TotalQuantity，默认选中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21140(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("3、SchemeWise选择了Activation，SchemeType下拉内容仅有UnitRebateAmount、UnitRebateAmount，默认选中UnitRebateAmount")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21141(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("4、SchemeWise选择了Activation，返利条件包括TotalQuantity、MaxRebateAmount、Amount、Quantity、MidHighTotalQuantity")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21142(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("5、取数页面CustomeractivitionPSI国包或者二代ActivationSales，注意需要国包和二代收货，只看激活。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21143(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("6、组合各种维度条件跑数，客户类型需覆盖国包、二代、零售商")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21144(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("61、一个二代向多个国包拿货，SchemeReportItem表需要根据国包数量及item拆分返利")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21145(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("62、其他情况，SchemeReportItem正常根据item拆分")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21146(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("7、返利对象customerSchemeWiseActivationSchemeTypeCaculateWise条件,组合跑返利政策")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21147(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("71、冒烟customerActivationTotalQuantityUnitRebateAmountTotalQuantity（条件），跑出的结果正确，落表正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21148(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("72、customerActivationRebateTotalQuantity（条件），跑出的结果正确，落表正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21149(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("73、customerActivationUnitRebateAmountMaxRebateAmount，跑出的结果正确，落表正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21150(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("73、customerActivationUnitRebateAmountAmount，跑出的结果正确，落表正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21151(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("73、customerActivationUnitRebateAmountQuantity，跑出的结果正确，落表正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21152(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("73、customerActivationUnitRebateAmountMidHighTotalQuantity条件，跑出的结果正确，落表正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21153(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("74、customerActivationUnitRebateAmount多条件组合，跑出的结果正确，落表正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21154(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("8、推送FOL二代返利的金额，要按拿货情况，拆分国包商进行FOL推送。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21155(self, drivers):
        pass


if __name__ == '__main__':
      pass
