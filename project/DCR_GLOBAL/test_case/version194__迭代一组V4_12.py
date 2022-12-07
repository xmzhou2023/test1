import allure
import pytest
@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_2888:
    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR同步用户状态为禁用，不清除该账号授权")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20823(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR状态为在职，但用户中心状态为离职的外部员工	更新员工离职状态、Updater、UpdaterDate、OffServiceUpdater、OffServiceDate")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20824(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR状态为在职，但用户中心状态为离职的外部员工	不解除员工客户、品牌、仓库、门店关系（记录日志）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20825(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR状态是离职，用户中心在职状态的外部员工	不更新DCR外部账号的状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20826(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR同步用护中心禁用状态	用户限制登录，不重置密码")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20827(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("DCR同步用护中心禁用状态	再次启用后重置密码可以登录，用户授权依然在")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20828(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("批量选择用户点击重置密码，如果有内部账号，提示Transsionaccountcan039tberesetpasswordintheDCR,plscontactITservice，重置失败")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20829(self, drivers):
        pass


    @allure.story("用户中心禁用外部账号更新DCR账号状态")  # 用户故事名称
    @allure.title("批量选择用户点击重置密码，如果有已禁用的账号，提示Disableaccountcan039tberesetpassword,plsenableitfirst，重置失败")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20830(self, drivers):
        pass


@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_3125:
    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("1、返利对象customer中SchemeWise增加激活维度Activation不考虑多等级及时间重选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21139(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("2、SchemeWise选择了Activation，SchemeType下拉内容仅有TotalQuantity，默认选中")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21140(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("3、SchemeWise选择了Activation，SchemeType下拉内容仅有UnitRebateAmount、UnitRebateAmount，默认选中UnitRebateAmount")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21141(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("4、SchemeWise选择了Activation，返利条件包括TotalQuantity、MaxRebateAmount、Amount、Quantity、MidHighTotalQuantity")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21142(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("5、取数页面CustomeractivitionPSI国包或者二代ActivationSales，注意需要国包和二代收货，只看激活。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21143(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("6、组合各种维度条件跑数，客户类型需覆盖国包、二代、零售商")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21144(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("61、一个二代向多个国包拿货，SchemeReportItem表需要根据国包数量及item拆分返利")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21145(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("62、其他情况，SchemeReportItem正常根据item拆分")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21146(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("7、返利对象customerSchemeWiseActivationSchemeTypeCaculateWise条件,组合跑返利政策")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21147(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("71、冒烟customerActivationTotalQuantityUnitRebateAmountTotalQuantity（条件），跑出的结果正确，落表正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21148(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("72、customerActivationRebateTotalQuantity（条件），跑出的结果正确，落表正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21149(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("73、customerActivationUnitRebateAmountMaxRebateAmount，跑出的结果正确，落表正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21150(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("73、customerActivationUnitRebateAmountAmount，跑出的结果正确，落表正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21151(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("73、customerActivationUnitRebateAmountQuantity，跑出的结果正确，落表正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21152(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("73、customerActivationUnitRebateAmountMidHighTotalQuantity条件，跑出的结果正确，落表正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21153(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("74、customerActivationUnitRebateAmount多条件组合，跑出的结果正确，落表正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21154(self, drivers):
        pass


    @allure.story("返利新场景渠道激活返利")  # 用户故事名称
    @allure.title("8、推送FOL二代返利的金额，要按拿货情况，拆分国包商进行FOL推送。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21155(self, drivers):
        pass


@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_3194:
    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("新增功能配置项，支持国家品牌、客户类型、客户ID三种方式配置生效")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21156(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("新增功能配置项，remark调拨单是否可以选择上月的日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21157(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("新增功能配置项，配置0不可以")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21158(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("新增功能配置项，配置gt=1当前日期在配置日期之前时，可以选择上月日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21159(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("新增功能配置项，配置1只能选择昨天的日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21160(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("新增功能配置项，优先级同出库单出入日期限制的功能配置")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21161(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("页面创建调拨单，新增调拨日期字段，TransferDate，必填项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21162(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("页面创建调拨单，新增调拨日期字段，默认选择当前日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21163(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("页面创建调拨单，新增调拨日期字段，根据Transferfrom客户，可以选择当月和上月日期创建调拨单")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21164(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("页面创建调拨单，新增调拨日期字段，更新Transferfrom客户，联动更新调拨可选日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21165(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("页面创建调拨单，新增调拨日期字段，验证同客户仓库间调拨场景")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21166(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("页面创建调拨单，新增调拨日期字段，列表Operation之前新增TransferDate字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21167(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("页面创建调拨单，新增调拨日期字段，导出列表同步新增字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21168(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("批导新增调拨字段，非必填项，紫色显示该字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21169(self, drivers):
        pass


    @allure.story("渠道调拨单新增调拨日期")  # 用户故事名称
    @allure.title("批导新增调拨字段，导入不支持的日期，导入失败提示调拨单日期不再可选范围/TransferDateisnotoption")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21170(self, drivers):
        pass


@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_3195:
    @allure.story("返利机型前端显示优化")  # 用户故事名称
    @allure.title("返利第二页的机型重选区域，显示机型总数量，点击数量进入重选机型页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21171(self, drivers):
        pass


    @allure.story("返利机型前端显示优化")  # 用户故事名称
    @allure.title("返利对象user、shop、customer分别创建返利政策，第二页机型重选，显示为总数量，点击数量，进入重选机型页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21545(self, drivers):
        pass


    @allure.story("返利机型前端显示优化")  # 用户故事名称
    @allure.title("通过新增、编辑、copy路径创建返利，第二页机型重选，显示为总数量，点击数量，进入重选机型页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21546(self, drivers):
        pass


@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_3124:
    @allure.story("返利对象无效的原因显示")  # 用户故事名称
    @allure.title("登录账号没有客户/门店权限，查询后显示ID没有授权，提示以下ID没有授权，请授权后再设置（中英文）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21172(self, drivers):
        pass


    @allure.story("返利对象无效的原因显示")  # 用户故事名称
    @allure.title("显示输入框下方，不算在有效门店数量里")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21173(self, drivers):
        pass


    @allure.story("返利对象无效的原因显示")  # 用户故事名称
    @allure.title("测试路径RebateAchievementSchemeManagement中点击【Add】按钮进入的SchemeAdd页面中SchemeObject")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22155(self, drivers):
        pass


    @allure.story("返利对象无效的原因显示")  # 用户故事名称
    @allure.title("测试点_1、黏贴的ID，登录账户没有授权。需要显示具体哪个ID没有授权。验证维度有三个User、Customer、Shop")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22156(self, drivers):
        pass


    @allure.story("返利对象无效的原因显示")  # 用户故事名称
    @allure.title("测试点_11、中文提示语以下ID没有授权，请授权后再设置'PK11111，PK22222，PK33333'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22157(self, drivers):
        pass


    @allure.story("返利对象无效的原因显示")  # 用户故事名称
    @allure.title("测试点_12、英文提示语ThefollowingIDsarenotauthorized,pleaseaddauthorizationandsetagain'PK11111，PK22222，PK33333'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22158(self, drivers):
        pass


@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_3123:
    @allure.story("返利对象兼容大小写")  # 用户故事名称
    @allure.title("返利对象粘贴user、Customer、Shop的ID存在大小写与正确的不一致时，check需检测正确的匹配显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21174(self, drivers):
        pass


    @allure.story("返利对象兼容大小写")  # 用户故事名称
    @allure.title("第二页重选对象粘贴也要兼容大小写，匹配到正确的ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21175(self, drivers):
        pass


    @allure.story("返利对象兼容大小写")  # 用户故事名称
    @allure.title("第一页和第二页粘贴对象，输入无效的ID，需优化显示DCR查无此ID，请重新入quotPK1111''PK112'（中英文）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21176(self, drivers):
        pass


    @allure.story("返利对象兼容大小写")  # 用户故事名称
    @allure.title("返利对象手动输入user、Customer、Shop的ID存在大小写与正确的不一致时，check需检测正确的匹配显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21722(self, drivers):
        pass


    @allure.story("返利对象兼容大小写")  # 用户故事名称
    @allure.title("第二页重选对象手动输入也要兼容大小写，匹配到正确的ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21723(self, drivers):
        pass


@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_3184:
    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("Web右上角消息通知左侧新增时区选择器，展示当前时区国家和与零时区的时差")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21177(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("点击弹出时区选择弹窗，title展示时区，展示用户时区和提示文案切换时区后，系统所有数据时间将根据选择时区进行转换")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21178(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("点击弹出时区选择弹窗，时区选项区域滑动展示74国家时区")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21179(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("点击弹出时区选择弹窗，第一个固定展示零时区，每行默认展示三个时区，按照时区维度GMT0~GMT24排序显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21180(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("点击弹出时区选择弹窗，默认选中用户当前时区")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21181(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("点击弹出时区选择弹窗，取消和确认按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21182(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("点击弹出时区选择弹窗，点击右上角关闭按钮，关闭弹窗")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21183(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("点击弹出时区选择弹窗，点击取消，关闭弹窗")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21184(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("点击弹出时区选择弹窗，时区切换后点击确定，关闭弹窗，刷新模块数据时间，更新系统右上角用户切换的时区入口")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21185(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("验证考勤和巡店模块的时间	AttendanceRules验证CreatedDate和UpdateDate时间转义，其他业务时间不随时区转换")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21186(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("验证考勤和巡店模块的时间	Attendancerecords目前所有时间都不随时区转换")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21187(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("验证考勤和巡店模块的时间	AttendancePhoto目前所有时间不随时区转换")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21188(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("验证考勤和巡店模块的时间	AttendanceStatistics目前所有时间都不随时区转换")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21189(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("验证考勤和巡店模块的时间	LeaveApplicationRecords验证请假StartDate、StartTime、EndDate、EndTime时区转换垮天、月、年时的显示，SubmitDate、ApproverDate时间转换")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21190(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("验证考勤和巡店模块的时间	VisitingTemplate验证CreatedDate时间转换")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21191(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("验证考勤和巡店模块的时间	VisitPlan验证CreatedDate、PlanDate、CompletedDate时间转换，注意垮天、月、年的显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21192(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("验证考勤和巡店模块的时间	VisitRecords时间转换，PlanDate同Visitplan转义后的时间，VisitDate、VisitTime、SubmitDate、SubmitTime随时区转换")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21193(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("验证考勤和巡店模块的时间	VisitPhoto属性时间是否转换待定")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21194(self, drivers):
        pass


    @allure.story("DCR时区改造")  # 用户故事名称
    @allure.title("新用户登录默认展示用户资料国家的时区展示，用户资料国家不在系统时区范围内，默认取零时区")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21195(self, drivers):
        pass


@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_2702:
    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_1、根据用户关联角色的菜单权限用户数据权限")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21547(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_2、菜单权限StaffAuthorizationRoleDefinition里面配置")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21548(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_3、数据权限品牌、客户、门店、员工")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21549(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_4、权限控制逻辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21550(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_41、根据选中模块查询图片取得模块结果集")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21551(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_42、模块图片结果集根据用户授权品牌查询，取得模块品牌结果集")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21552(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_43、模块品牌结果集中图片的业务属性（客户、门店、员工）匹配用户授权的客户、门店、员工其中一项，则用户可以查看该图片")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21553(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("测试路径BasicDataManagement文档库页面展示的语言需要实现根据系统语言适配")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21554(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21555(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("根据业务系统，获取文档中心对应业务系统的资源文件。可根据文档、图片进行切换显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21556(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("业务系统提交资源文件后，文档中心保存资源文件，生成资源文件地址")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21557(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("业务系统提交编辑操作，根据编辑内容对原资源文件进行删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21558(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_1、Module（模块）文档归属的业务模块。下拉选择框，单选，支持模糊查询。按用户菜单权限顺序做默认选中")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21559(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_11、DCR选项内容（知识库）、CustomerManagement（客户管理）、（返利政策）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21560(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_12、筛选Module，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21561(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_2、SalesRegion（销售区域）下拉选择框，多选，支持下拉搜索输入模糊匹配。根据图片关联的业务数据进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21562(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_21、DCR选项内容根据销售区域表，显示SR3的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21563(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_22、图片关联业务模块的销售区域，按以下对象取值")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21564(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_221、（知识库）创建人所属的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21565(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_222、CustomerManagement（客户管理）客户所属的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21566(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_223、（返利政策）返利政策所属的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21567(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_23、筛选SalesRegion，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21568(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_3、Country（国家）下拉选择框，多选，支持下拉搜索输入模糊匹配。根据图片关联的业务数据进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21569(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_31、DCR选项内容国家资料表的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21570(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_32、图片关联业务模块的国家，按以下对象取值")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21571(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_221、（知识库）创建人所属的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21572(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_222、CustomerManagement（客户管理）客户所属的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21573(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_223、（返利政策）返利政策所属的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21574(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_33、筛选Country，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21575(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_4、Date（日期）日历选择器，根据选择日期范围，查询创建时间包含在选择范围")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21576(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_41、筛选Date，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21577(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("Search（搜索）按钮_1、点击Search按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21578(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("Search（搜索）按钮_11、单个筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21579(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("Search（搜索）按钮_12、组合筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21580(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("Reset（重置）按钮_1、点击Reset按钮，重置筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21581(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("列表按照创建时间倒序进行排序")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21582(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("列表字段_1、Module（模块）资源文件对应的业务模块。DCR涉及上传文档类型模块如下")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21583(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("列表字段_11、知识库新增/编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21584(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("列表字段_12、客户管理新增/编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21585(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("列表字段_13、返利政策新增/编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21586(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("列表字段_2、DocumentName（文件名称）资源文件名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21587(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("列表字段_21、文件名称可点击，点击后打开新页面查看文档内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21588(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("列表字段_3、Uploader（上传用户）上传资源文件的用户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21589(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("列表字段_4、UploadTime（上传时间）上传资源文件的时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21590(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("翻页_1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21591(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("翻页_2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21592(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("翻页_3、页面右下角totalrecords统计正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21593(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("翻页_4、页面右下角每页显示记录可设置（20，50，100，500，1000），如果选择20，则每页显示1至20条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21594(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("测试路径BasicDataManagement文档库页面展示的语言需要实现根据系统语言适配")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21595(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21596(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("根据业务系统，获取文档中心对应业务系统的资源文件。可根据文档、图片进行切换显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21597(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("业务系统提交资源文件后，调用大数据图片服务接口，校验图片")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21598(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("可正常调用大数据服务校验图片，并标记校验结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21599(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("纯色图片（黑色、白色等）等不符合业务场景图片识别。校验失败提示语''/'图片内容错误'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21600(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("业务系统提交编辑操作，根据编辑内容对原资源文件进行删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21601(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_1、Module（模块）图片归属的业务模块。下拉选择框，单选，支持模糊查询。按用户菜单权限顺序做默认选中")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21602(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_11、DCR选项内容AttendanceRecords/AttendancePhoto（考勤）、VisitRecord（巡店）、CustomerManagement（客户管理）、ShopManagement（门店管理）、UserManagement（员工管理）、ShopAsset/AssetMaintenanceHistory（资产管理）、DemoPhoneQuery（样机管理）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21603(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_12、筛选Module，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21604(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_2、SalesRegion（销售区域）图片关联业务模块的销售区域。下拉选择框，多选，支持下拉搜索输入模糊匹配。根据图片关联的业务数据进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21605(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_21、DCR选项内容根据销售区域表，显示SR3的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21606(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_22、图片关联业务模块的销售区域，按以下对象取值")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21607(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_221、AttendanceRecords/AttendancePhoto（考勤）员工所属的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21608(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_222、VisitRecord（巡店）门店所属的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21609(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_223、CustomerManagement（客户管理）客户所属的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21610(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_224、ShopManagement（门店管理）门店所属的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21611(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_225、UserManagement（员工管理）员工所属的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21612(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_226、ShopAsset/AssetMaintenanceHistory（资产管理）门店所属的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21613(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_227、DemoPhoneQuery（样机管理）门店所属的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21614(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_23、筛选SalesRegion，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21615(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_3、Country（国家）图片关联业务模块的国家。下拉选择框，多选，支持下拉搜索输入模糊匹配。根据图片关联的业务数据进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21616(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_31、DCR选项内容国家资料表的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21617(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_32、图片关联业务模块的国家，按以下对象取值")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21618(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_321、AttendanceRecords/AttendancePhoto（考勤）员工所属的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21619(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_322、VisitRecord（巡店）门店所属的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21620(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_323、CustomerManagement（客户管理）客户所属的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21621(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_324、ShopManagement（门店管理）门店所属的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21622(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_325、UserManagement（员工管理）员工所属的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21623(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_326、ShopAsset/AssetMaintenanceHistory（资产管理）门店所属的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21624(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_327、DemoPhoneQuery（样机管理）门店所属的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21625(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_33、筛选Country，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21626(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_4、Date（日期）日历选择器，根据选择日期范围，查询创建时间包含在选择范围")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21627(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_41、筛选Date，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21628(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_5、Status（检验状态）下拉选择框，单选？输入模糊匹配")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21629(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_51、选项内容All（全部）、（失败）、（成功）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21630(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("筛选项_52、筛选Status，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21631(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("Search（搜索）按钮_1、点击Search按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21632(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("Search（搜索）按钮_11、单个筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21633(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("Search（搜索）按钮_12、组合筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21634(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("Reset（重置）按钮_1、点击Reset按钮，重置筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21635(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_1、显示图片缩略图，分页加载方式为下滑加载，点击图片可查看大图")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21636(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_2、图片业务属性")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21637(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_21、除校验状态外，其他业务属性由业务系统定义")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21638(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_22、校验状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21639(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_221、成功文案显示''/'校验成功'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21640(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_222、失败文案显示''/'校验失败。原因当前图片校验失败原因呢'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21641(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3、业务数据取数从大数据获取，具体业务数据可查看")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21642(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_31、AttendanceRecords/AttendancePhoto（考勤）StandardPhoto、CheckinPhoto、CheckoutPhoto")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21643(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_311、业务图片1打卡人脸识别（人脸识别失败。校验失败提示语''/'图片内容错误'）这块大数据目前没法实现校验为哪种类型的图片，大数据只能判断纯色图片为错误图片")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21644(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_312、业务图片2请假请假条（校验规则为通用规则）这块大数据目前没法实现校验为哪种类型的图片，大数据只能判断纯色图片为错误图片")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21645(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_313、图片业务属性")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21646(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3131、员工名称工号")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21647(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3132、品牌（员工的品牌）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21648(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3133、职位（员工的职位）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21649(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3134、打卡时间（考勤图片的打卡时间）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21650(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3135、校验状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21651(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_32、VisitRecord（巡店）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21652(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_321、业务图片货柜陈列、督导在店、样机陈列、店内环境这块大数据目前没法实现校验为哪种类型的图片，大数据只能判断纯色图片为错误图片")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21653(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_322、图片业务属性")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21654(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3221、员工名称工号")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21655(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3222、品牌（门店的品牌）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21656(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3223、图片字段名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21657(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3224、巡店时间（巡店图片的巡店时间）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21658(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3225、校验状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21659(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_33、CustomerManagement（客户管理）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21660(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_321、业务图片公司门头照、内部照新建客户时编辑的这块大数据目前没法实现校验为哪种类型的图片，大数据只能判断纯色图片为错误图片")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21661(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_322、图片业务属性")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21662(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3321、客户名称客户ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21663(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3322、客户类型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21664(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3323、图片字段名称。例FaceImage、InnerImage、OtherImage")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21665(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3324、上传时间（图片上传到服务器的时间。若资源文件上传没有记录时间，则取资源文件对应业务记录的最后修改时间）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21666(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3325、校验状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21667(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_34、ShopManagement（门店管理）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21668(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_341、业务图片门头照、店内照新建门店时编辑的这块大数据目前没法实现校验为哪种类型的图片，大数据只能判断纯色图片为错误图片")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21669(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_342、图片业务属性")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21670(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3421、门店名称门店ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21671(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3422、图片字段名称。例全球版FaceImage、InnerImage、OtherImage、OtherImage。印度版FaceImage、InnerImage、CopyofBankAccountDetails、OtherImage")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21672(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3423、上传时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21673(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3424、校验状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21674(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_35、UserManagementindia（员工管理印度版）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21675(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_351、业务图片员工银行卡复印件新建员工时编辑的这块大数据目前没法实现校验为哪种类型的图片，大数据只能判断纯色图片为错误图片")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21676(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_352、图片业务属性")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21677(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3521、员工名称员工ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21678(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3522、职位（员工的职位）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21679(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3523、图片字段名称。例CopyofPANcardattachment、CopyofAadhaarcardattachment、CopyofBankPassbook/CancelChequeAttachment")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21680(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3524、上传日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21681(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3525、校验状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21682(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_36、ShopAsset/AssetMaintenanceHistory（资产管理）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21683(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_361、业务图片门店资产物件，如柜台、灯具这块大数据目前没法实现校验为哪种类型的图片，大数据只能判断纯色图片为错误图片")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21684(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_362、图片业务属性")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21685(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3621、门店名称门店ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21686(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3622、资产名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21687(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3623、图片字段名称。例Overall、Side、Back、Others")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21688(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3624、上传日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21689(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3625、校验状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21690(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_37、DemoPhoneQuery（样机管理）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21691(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_371、业务图片手机、包装盒图片这块大数据目前没法实现校验为哪种类型的图片，大数据只能判断纯色图片为错误图片")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21692(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_372、图片业务属性")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21693(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3721、门店名称门店ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21694(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3722、ModelIMEI。例X671B（358132470520007）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21695(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3723、图片字段名称。例SampleDeviceWithExperienceTable、Overallreviewofshop、IMEI/SNstickerofSampleDevice、Demodeviceshowingsamplevedio")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21696(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3724、上传日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21697(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("图片展示_3725、校验状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21698(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_431、【图片】AttendanceRecords/AttendancePhoto（考勤）品牌门店员工")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21749(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_432、【图片】VisitRecord（巡店）品牌门店员工")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21750(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_433、【图片】CustomerManagement（客户管理）品牌客户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21751(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_434、【图片】ShopManagement（门店管理）品牌门店")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21752(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_435、【图片】UserManagement（员工管理）品牌员工")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21753(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_436、【图片】ShopAsset/AssetMaintenanceHistory（资产管理）品牌门店员工")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21754(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_437、【图片】DemoPhoneQuery（样机管理）品牌门店员工")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21755(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_438、【文档】（知识库）职位组为ManagementGroup、DivisionManagerGroup的员工")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21756(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_439、【文档】CustomerManagement（客户管理）品牌客户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21757(self, drivers):
        pass


    @allure.story("文档库")  # 用户故事名称
    @allure.title("数据权限控制_4310、【文档】（返利政策）员工（授权用户包含创建人、更新人）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21758(self, drivers):
        pass


@allure.feature("迭代一组V4_12")  # 迭代名称
class Teststory_3185:
    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("测试路径FeedBackSystemModule")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21759(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21760(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_1、InsertorNot（是否接入）下拉单选，选项内容是（Yes）、否（No）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21761(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_11、筛选InsertorNot，筛选出的数据正确查询接入状态等于选中内容的模块")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21762(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Search按钮、点击【Search】按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21763(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Reset按钮、点击【Reset】按钮，重置筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21764(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Add按钮、点击【Add】按钮，弹出新增弹窗（Add），可新增模块")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21765(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Delete按钮_1、点击【Delete】按钮，支持批量删除未关联规则的模块没有选中数据，点击按钮提示'Pleaseselectarecord'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21766(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Delete按钮_11、如果选中的都是未关联规则的模块，打开二次确认弹窗'Tips'，内容quotConfirmtodelete?quot/'确定删除？'。点击确定【Confirm】删除当前模块；点击取消【Cancel】/【X】关闭二次确认弹窗。删除成功提示'Deletedsuccessfully'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21767(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Delete按钮_12、如果选中的有已关联规则的模块，弹窗'Tips'报错提示'Therulehasbeenassociatedandcannotbedeleted.'/'模块XX已关联规则，不能删除'，并且下面列出对应的Module")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21768(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21769(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21770(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表排序规则按创建时间倒序排列")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21771(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_1、Key（Key）业务系统模块Key")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21772(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21773(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_2、Module（模块）业务系统模块名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21774(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21775(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_3、Rules（接入规则）业务系统模块接入规则")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21776(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21777(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_4、InsertorNot（是否接入）业务系统模块接入状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21778(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_41、若模块接入状态为已接入，页面按钮为已接入样式（按钮样式，按钮呈打开状态）。反之为未接入样式（按钮样式，按钮呈关闭状态）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21779(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_42、点击接入状态按钮，将模块的状态设置为另一个状态（接入→未接入、未接入→接入），接入状态修改成功提示'Editsucceeded'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21780(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_43、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21781(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_5、Operation（操作栏）操作栏展示【Delete】按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21782(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_51、点击【Delete】按钮，单个删除这行模块只支持删除未关联规则的模块")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21783(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_511、如果选择的是未关联规则的模块，打开二次确认弹窗'Tips'，内容quotConfirmtodelete?quot/'确定删除？'。点击确定【Confirm】删除当前模块；点击取消【Cancel】/【X】关闭二次确认弹窗。删除成功提示'Deletedsuccessfully'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21784(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_512、如果选中的是已关联规则的模块，弹窗'Tips'报错提示'Therulehasbeenassociatedandcannotbedeleted.'/'模块XX已关联规则，不能删除'，并且下面列出对应的Module")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21785(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21786(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21787(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21788(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页4、页面右下角每页显示记录可设置（20，50，100，500，1000），如果选择20，则每页显示1至20条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21789(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_1、Module（模块）支持中文、英文、数字输入，必填（红色标识）现在也不限制其他格式的输入最多输入50位")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21790(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_2、Key（Key）支持英文、数字输入，最多输入8位，必填（红色标识）现在也不限制其他格式的输入")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21791(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_3、InsertorNot（是否接入）下拉选择项，选项内容是、否。默认选中否，非必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21792(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_4、Rules（接入规则）最多输入200，非必填现在也不限制其他格式的输入")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21793(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_5、【Confirm】按钮有必填项未填写时，确定按钮置灰现在是没有做这个置灰的功能的，现在是必填项提示'Thisfieldisrequired'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21794(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_51、业务系统已存在相同的模块/Key时，提示'Failedtoadd,Keyornameexisting'/'XX模块已存在'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21795(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_52、未存在以上异常，将业务系统的模块内容保存到中台。弹窗关闭，提示'Addedsuccessfully'，新增的模块写入列表")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21796(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_6、新增弹窗点击【Cancel】按钮或者【X】按钮，关闭当前弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21797(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("测试路径FeedBackReason")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21798(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21799(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_1、Reason（不满意原因）文本输入框，支持模糊查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21800(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_11、筛选Reason，筛选出的数据正确根据输入关键字查询业务系统的不满意原因筛选列表中Reason（不满意原因）、EN（英语）、FR（法语）、POR（葡萄牙语）、ES（西班牙语）、THA（泰语）的内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21801(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Search按钮_1、点击【Search】按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21802(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Reset按钮、点击【Reset】按钮，重置筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21803(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Add按钮、点击【Add】按钮，弹出新增弹窗（Add），可新增不满意原因")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21804(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Delete按钮_1、点击【Delete】按钮，支持批量删除未关联规则的不满意原因没有选中数据，点击按钮提示'Pleaseselectarecord'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21805(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Delete按钮_11、如果选中的都是未关联规则的不满意原因，打开二次确认弹窗'Tips'，内容'Confirmtodelete?'/'确定删除？'。点击确定【Confirm】删除当前不满意原因；点击取消【Cancel】/【X】关闭二次确认弹窗。删除成功提示'Deletedsuccessfully'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21806(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Delete按钮_12、如果选中的有已关联规则的不满意原因，弹窗'Tips'报错提示'Therulehasbeenassociatedandcannotbedeleted.'/'不满意原因XX已关联规则，不能删除'，并且下面列出对应语言的Reason")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21807(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21808(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21809(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表排序规则列表以模块、分类进行分组，按创建时间倒序排列")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21810(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_1、Reason（不满意原因）回显不满意原因的中文")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21811(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21812(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_2、Classify（分类）不满意原因归属的分类")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21813(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21814(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_3、EN（英语）不满意原因的英语翻译")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21815(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21816(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_4、FR（法语）不满意原因的法语翻译")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21817(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_41、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21818(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_5、POR（葡萄牙语）不满意原因的葡萄牙翻译")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21819(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21820(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_6、ES（西班牙语）不满意原因的西班牙语翻译")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21821(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_61、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21822(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_7、THA（泰语）不满意原因的泰语翻译")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21823(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_71、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21824(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_8、Creator（创建人）不满意原因的创建人")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21825(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_81、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21826(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_9、CreateTime（创建时间）不满意原因的创建时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21827(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_91、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21828(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_11、Opration（操作栏）操作栏有两个按钮，【Edit】按钮和【Delete】按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21829(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_111、点击【Edit】按钮，弹出编辑弹窗（Edit），可编辑不满意原因")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21830(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_1111、编辑弹窗，回显不满意原因")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21831(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_1112、编辑后点击确定，根据内容更新当前规则。编辑成功提示'Editsucceeded'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21832(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_112、点击【Delete】按钮，单个删除这行不满意原因只支持删除未关联规则的不满意原因")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21833(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_1121、如果选择的是未关联规则的不满意原因，打开二次确认弹窗'Tips'，内容'Confirmtodelete?'/'确定删除？'。点击确定【Confirm】删除当前不满意原因；点击取消【Cancel】/【X】关闭二次确认弹窗。删除成功提示'Deletedsuccessfully'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21834(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_1122、如果选中的是已关联规则的不满意原因，弹窗'Tips'报错提示'Therulehasbeenassociatedandcannotbedeleted.'/'不满意原因XX已关联规则，不能删除'，并且下面列出对应语言的Reason")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21835(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21836(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21837(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21838(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页4、页面右下角每页显示记录可设置（20，50，100，500，1000），如果选择20，则每页显示1至20条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21839(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_1、Reason（不满意原因）必填（红色标识），内容最多8位")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21840(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_2、Translate（翻译）这边填入EN（英语）、FR（法语）、POR（葡萄牙语）、ES（西班牙语）、THA（泰语）。英文必填（红色标识），内容最多50位")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21841(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_3、Classify（分类）显示业务系统已有的分类。非必选，单选，单选框内提示'PleaseSelect'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21842(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_31、点击单选框右侧的维护分类按钮【MaintainClassify】，打开维护分类弹窗（MaintainClassify）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21843(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_311、维护分类弹窗上部分是AddClassify（新增分类）栏")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21844(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_3111、未填写分类名称，添加按钮【Add】置灰")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21845(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_3112、在ClassifyName（分类名称）后面的输入框中填入分类名称后点击添加按钮【Add】，将分类与业务系统绑定并保存到中台，添加的分类会展示在下方的（已有分类）栏，添加成功提示语'Addedsuccessfully'分类名称最多12位")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21846(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_312、维护分类弹窗下部分是ExistingClassify（已有分类）栏这一栏只有已有分类时才会展现下面的分类内容，还没有分类时只会展示栏目名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21847(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_3121、已有分类按创建时间进行排序，已添加的分类标签右上角出现删除按钮，点击删除按钮，将分类从业务系统中删除。删除成功提示语'Deletedsuccessfully'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21898(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_31211、点击删除分类时，如果该分类有关联的原因，弹窗提示XX已关联原因，移除后对应原因会取消与当前分类的关系，确认删除？（XXhasbeenassociatedreason.Afterremoval,thecorrespondingreasonwillcancelrelationshipwiththisclassify.Suretodelete?）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21899(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_313、维护分类弹窗点击【Close】/【X】按钮，关闭当前弹窗")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21900(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_314、分类翻译由机器自动翻译")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21901(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_4、【Confirm】按钮有必填项未填写时，确定按钮置灰")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21902(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_41、业务系统已存在相同的不满意原因时，提示'reasonalreadyexists'/'XX原因已存在'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21903(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_42、未存在以上异常，保存当前不满意原因。弹窗关闭，提示'Addedsuccessfully'，新增的不满意原因写入列表")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21904(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_43、不满意原因默认作用于系统所有模块")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21905(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_5、新增弹窗点击【Cancel】按钮或者【X】按钮，关闭当前弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21906(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("测试路径FeedBackFeedBackRule")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21912(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21913(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_1、Module（模块）下拉多选，查询业务系统包含选中模块的规则如果点击AddAll，可选择全部")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21914(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_11、选项内容模块接入表状态为已接入的模块因为这边只在进入页面的时候请求一次，要CtrlR刷新页面/重新进入页面才会请求模块接入表那边最新的已接入的模块")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21915(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_12、筛选Module，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21916(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_2、Country（国家）下拉多选，模糊匹配，查询业务系统包含选中国家的规则如果点击AddAll，可选择全部")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21917(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_21、选项内容业务系统国家表")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21918(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_22、业务系统已配置列表'国家'显示，该查询条件显示，否则不显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21919(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_23、筛选Country，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21920(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_3、Status（状态）下拉单选，查询业务系统包含选中状态的规则")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21921(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_31、选项内容Pending（待开始）、Processing（进行中）、Closed（已结束）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21922(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_32、筛选Status，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21923(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Search按钮_1、点击Search按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21924(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Search按钮_2、单个筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21925(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Search按钮_3、组合筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21926(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Reset按钮、点击Reset按钮，重置筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21927(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Add按钮、点击【Add】按钮，弹出新增弹窗（Add），可新增用户反馈规则")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21928(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Disable按钮_1、点击【Disable】按钮，支持批量停止用户反馈规则没有选中数据，点击按钮提示'Pleaseselectarecord'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21929(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Disable按钮_11、点击【Disable】按钮，出现二次确认弹窗，内容'Confirmdisabledcurrentrule?'/'确定停用当前规则？'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21930(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Disable按钮_111、点击【Confirm】按钮，将选中规则状态变更为已结束并关闭二次确认弹窗。提示'Disabledsuccessfully'，这条数据的状态变更为Closed可成功对状态为Processing的规则进行操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21931(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Disable按钮_112、点击【X】按钮，关闭二次确认弹窗，选中规则不做任何修改")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21932(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Disable按钮_12、如果批量选中的数据中包含状态为Pending/Closed的规则，点击【Disable】按钮，出现'Tips'弹窗，内容'Thefollowingrulescannotoperate'，并且下面列出对应的规则ID。点击【Confirm】/【X】按钮，关闭'Tips'弹窗，选中规则不做任何修改")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21933(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Enable按钮_1、点击【Enable】按钮，支持批量启用用户反馈规则没有选中数据，点击按钮提示'Pleaseselectarecord'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21934(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Enable按钮_11、打开设置收集时间弹窗（SelectCollectionTime）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21935(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Enable按钮_111、CollectionTime（收集时间）必填（红色标识），日期具体到天。开始时间只能选择当天及以后日期，结束时间不能小于开始日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21936(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Enable按钮_112、点击【Confirm】按钮，更新选中规则的收集时间，提示'Enabledsuccessfully'可成功对状态为Closed和Pending的规则进行操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21937(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Enable按钮_1121、判断开始时间等于当天，规则状态为Processing（进行中），规则时间大于当天，规则状态为Pending（待开始）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21938(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Enable按钮_113、点击【Cancel】按钮或者【X】按钮，关闭设置收集时间弹窗，选中规则不做任何修改")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21939(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Enable按钮_12、如果批量选中的数据中包含状态为Processing的规则，点击【Enable】按钮，出现'Tips'弹窗，内容'Thefollowingrulescannotoperate'，并且下面列出对应的规则ID。点击【Confirm】/【X】按钮，关闭'Tips'弹窗，选中规则不做任何修改")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21940(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21941(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21942(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表排序规则列表以模块分组，创建时间倒序排列")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21943(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_1、ID（规则ID）用户反馈规则ID。规则ID格式为FB年月日4位编码")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21944(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21945(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_2、Module（模块）用户反馈规则关联的模块")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21946(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21947(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_3、Country（国家）用户反馈规则关联的国家数量合计")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21948(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_31、可点击，点击后出现国家浮窗显示所关联的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21949(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_32、该字段根据业务系统需求，可配置是否显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21950(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_33、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21951(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_4、CollectionTime（收集时间）用户反馈规则设定的收集时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21952(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_41、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21953(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_5、Status（状态）用户反馈规则状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21954(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21955(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_6、Creator（创建人）用户反馈规则创建人。显示为用户名称用户ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21956(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_61、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21957(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_7、CreateTime（创建时间）用户反馈规则创建时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21958(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_71、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21959(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_8、Opration（操作栏）操作栏根据规则的状态显示对应按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21960(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_81、Pending（待开始）【View】、【Edit】、【Enable】")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21961(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_82、Processing（进行中）【View】、【Disable】")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21962(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_83、Closed（已结束）【View】、【Enable】")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21963(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_84、点击【View】按钮，打开查看弹窗'View'，将规则内容回显并置灰，隐藏【Confirm】、【Cancel】按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21964(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_841、点击【X】按钮，关闭查看弹窗")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21965(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_85、点击【Edit】按钮，打开编辑弹窗（Edit），根据规则回显内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21966(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_851、编辑后点击【Confirm】按钮，根据内容更新当前规则，提示'Success'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21967(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_8511、收集时间的开始时间大于当天，规则状态变更为Pending（待开始）。开始时间等于当天，规则状态变更为进行中Processing（进行中）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21968(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_852、点击【Cancel】按钮或者【X】按钮，关闭编辑弹窗，选中规则不做任何修改")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21969(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_86、点击【Enable】按钮，打开设置收集时间弹窗（SelectCollectionTime）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21970(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_861、CollectionTime（收集时间）必填（红色标识），日期具体到天。开始时间只能选择当天及以后日期，结束时间不能小于开始日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21971(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_862、点击【Confirm】按钮，更新选中规则的收集时间，提示'Enabledsuccessfully'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21972(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_8621、判断开始时间等于当天，规则状态为Processing（进行中），规则时间大于当天，规则状态为Pending（待开始）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21973(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_863、点击【Cancel】按钮或者【X】按钮，关闭设置收集时间弹窗，选中规则不做任何修改")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21974(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_87、点击【Disable】按钮，出现二次确认弹窗，内容'Confirmdisabledcurrentrule?'/'确定停用当前规则？'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21975(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_871、点击【Confirm】按钮，将选中规则状态变更为已结束并关闭二次确认弹窗。提示'Disabledsuccessfully'，这条数据的状态变更为Closed")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21976(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_872、点击【X】按钮，关闭二次确认弹窗，选中规则不做任何修改")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21977(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21978(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21979(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21980(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页4、页面右下角每页显示记录可设置（20，50，100，500，1000），如果选择20，则每页显示1至20条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21981(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_1、CollectionTime（收集时间）必填（红色标识），日期具体到天。开始时间只能选择当天及以后日期，结束时间不能小于开始日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21982(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_2、EvaluationMethod（评价方式）必填（红色标识），默认选中评分制（星级）'Ratingsystemstar'，不可取消")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21983(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_3、Country（收集国家）必填（红色标识），下拉多选输入框默认提示'Pleaseselect'如果选中后又取消选中，选项框变红色")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21984(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_31、选项内容从系统国家表获取")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21985(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_4、Module（模块）必填（红色标识），多选。若只有一个模块，该模块为选中状态且不可取消现在我看是置灰状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21986(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_41、选项内容模块接入表状态为已接入的模块如果选中后又取消选中，提示'Thisisrequired'这边是实时获取模块接入表那边已接入的模块的")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21987(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_42、业务系统的模块接入表没有状态为已接入的模块，红色字体提示'Thesystemhasnomoduleaccessservice'/'系统暂无任何模块接入服务'。【Confirm】按钮置灰")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21988(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_5、Reason（不满意原因）必填（红色标识），多选如果选中后又取消选中，提示'Thisisrequired'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21989(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_51、选项内容业务系统的不满意原因列表中添加的不满意原因。按原因序号进行排序现在是最新增加的不满意原因在最前面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21990(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_52、业务系统的不满意原因列表没有数据，红色字体提示'Nodissatisfactionreasonisset'/'未设置不满意原因'。【Confirm】按钮置灰")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21991(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_6、PopupRules（弹窗规则）必填（红色标识），单选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21992(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_61、Whenusercompletestheevaluation，popupruleis（用户完成评价，弹窗）可选择'Nolongerpopup'/'不再弹出'，或者编辑'daypopup'/'天弹出'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21993(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_611、编辑天弹出时天数只能输入正整数不能为0")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21994(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_62、Whenuserclosed，popupruleis（用户直接关闭，弹窗）可选择'Nolongerpopup'/'不再弹出'，或者编辑'daypopup'/'天弹出'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21995(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_621、编辑天弹出时天数只能输入正整数不能为0")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21996(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_7、【Confirm】按钮有必填项未填写时，确定按钮置灰")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21997(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_71、判断已选国家在选中模块已生成规则，提示'XXModuleisconfiguredXXcountryrule'/'XX模块已配置XX国家规则'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21998(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_72、根据选中模块与国家保存规则新增成功提示'Success'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21999(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_73、判断开始时间等于当天，规则状态为Processing（进行中）。规则时间大于当天，规则状态为Pending（待开始）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22000(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("新增弹窗_8、新增弹窗点击【Confirm】按钮或者【X】按钮，关闭当前弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22001(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("测试路径FeedBackFeedBack")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22002(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22003(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_1、Module（模块）下拉多选，支持模糊查询，查询业务系统模块字段包含输入关键字的评价内容如果点击AddAll，可选择全部")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22004(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_11、选项内容模块接入表状态为已接入的模块因为这边只在进入页面的时候请求一次，要CtrlR刷新页面/重新进入页面才会请求模块接入表那边最新的已接入的模块")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22005(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_12、筛选Module，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22006(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_2、Position（职位）文本输入框，支持模糊查询，查询业务系统职位字段包含输入关键字的评价内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22007(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_21、该查询条件与列表字段关联显示业务系统已配置列表'职位'显示，该查询条件显示，否则不显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22008(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_22、筛选Position，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22009(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_3、Role（角色）文本输入框，支持模糊查询，查询业务系统角色字段包含输入关键字的评价内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22010(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_31、该查询条件与列表字段关联显示业务系统已配置列表'角色'显示，该查询条件显示，否则不显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22011(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_32、筛选Role，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22012(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_4、Country（国家）下拉多选，模糊匹配，查询业务系统国家字段包含选中内容的评价内容如果点击AddAll，可选择全部")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22013(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_41、选项内容业务系统国家表")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22014(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_42、业务系统已配置列表'国家'显示，该查询条件显示，否则不显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22015(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_43、筛选Country，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22016(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_5、FeedbackTime（评价日期）日期选择器，查询业务系统评价时间在选中时间段范围内的评价内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22017(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_51、筛选FeedbackTime，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22018(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_6、Evaluate（评价等级），下拉多选。根据选中等级，查询对应的评价记录如果点击AddAll，可选择全部")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22019(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_61、选项内容1~5、未评价（NotEvaluated）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22020(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("筛选项_62、筛选Evaluate，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22021(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Search按钮_1、点击Search按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22022(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Search按钮_2、单个筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22023(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Search按钮_3、组合筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22024(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Reset按钮、点击Reset按钮，重置筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22025(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Export按钮、点击Export按钮，导出当前筛选出的全部数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22026(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Export导出_1、导出文件名为菜单名流水号")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22027(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Export导出_2、导出的报表字段名、字段顺序、数据内容和列表一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22028(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Export导出_3、导出的报表表头需要12号字紫色，不做自适应。导出的报表字段宽度为16个字符宽度现在列宽很随机")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22029(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Export导出_4、筛选后导出的报表数据和筛选的数据保持一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22030(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Export导出_41、单个筛选，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22031(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Export导出_411、筛选Module，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22032(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Export导出_412、筛选Country，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22033(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Export导出_413、筛选FeedbackTime，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22034(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("Export导出_42、组合筛选，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22035(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22036(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22037(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表排序规则显示APP用户提交的反馈内容，按评价时间倒序进行显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22038(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_1、Module（模块）用户反馈来源的模块")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22039(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22040(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_2、Evaluate（评价等级）用户评价等级。评价等级有1~5、未评价（NotEvaluated）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22041(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_21、用户关闭APP反馈弹窗，生成评价记录并记录用户评价等级为未评价")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22042(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_22、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22043(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_3、Reason（不满意原因）用户选择13星时，选择的不满意原因列表和导出都取Reason（Reason页面的Reason），不用取多语言")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22044(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22045(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_4、Feedback（反馈意见）用户填写的反馈意见")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22046(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_41、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22047(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_5、UserID（用户编码）用户ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22048(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22049(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_6、UserName（用户名称）用户名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22050(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_61、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22051(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_7、Position（职位）用户职位")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22052(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_71、该字段根据业务系统需求，可配置是否显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22053(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_72、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22054(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_8、Role（角色）用户角色")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22055(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_81、该字段根据业务系统需求，可配置是否显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22056(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_82、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22057(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_9、Country（国家）用户资料的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22058(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_91、该字段根据业务系统需求，可配置是否显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22059(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_92、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22060(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_10、FeedbackTime（评价时间）用户提交反馈的时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22061(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("列表字段_101、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22062(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22063(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22064(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22065(self, drivers):
        pass


    @allure.story("用户反馈迭代需求")  # 用户故事名称
    @allure.title("翻页4、页面右下角每页显示记录可设置（20，50，100，500，1000），如果选择20，则每页显示1至20条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22066(self, drivers):
        pass


if __name__ == '__main__':
    pass
