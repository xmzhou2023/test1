import allure
import pytest
@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2905:
    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护菜单权限校验")  # 用例名称
    @allure.description("登录账号为配置该模块权限时==配置权限后")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18186(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护查询条件检查")  # 用例名称
    @allure.description("检查查询条件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18187(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护列表字段检查")  # 用例名称
    @allure.description("检查列表字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18189(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护列表内容检查")  # 用例名称
    @allure.description("检查列表内容")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18190(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护操作按钮检查")  # 用例名称
    @allure.description("检查页面操作按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18191(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护查询后正确返回查询结果")  # 用例名称
    @allure.description("按编码查询==按名称查询==按状态为空查询==按状态=启用查询==按状态=禁用查询==条件组合查询")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18193(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护新增弹窗字段检查")  # 用例名称
    @allure.description("title==弹窗字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18194(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护字段为空时新增失败")  # 用例名称
    @allure.description("点击新增按钮，部分字段为空时保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18214(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护所有字段正确填写，新增成功")  # 用例名称
    @allure.description("点击新增按钮，全部字段正确填写后保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18215(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护新增弹窗字段长度不限制")  # 用例名称
    @allure.description("点击新增按钮，编码、名称输入超长文本、选择状态后保存")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18216(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护重置后，查询条件清空")  # 用例名称
    @allure.description("输入/选择查询条件后查询==点击重置按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18217(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护查询、翻页组合场景检查")  # 用例名称
    @allure.description("查询后翻页==重置、翻页后查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18219(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护选择每页展示条数，数量正确")  # 用例名称
    @allure.description("切换每页展示条数")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18220(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护编辑弹窗字段检查")  # 用例名称
    @allure.description("title==弹窗字段")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18222(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护编辑后保存成功")  # 用例名称
    @allure.description("点击列表后编辑按钮==检查弹窗字段内容==修改各字段后保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18223(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护新增、编辑时关闭/退出，数据未保存")  # 用例名称
    @allure.description("新增，填写内容后关闭/退出==修改页面内容后关闭/退出")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18253(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护新增编码、名称重复数据失败")  # 用例名称
    @allure.description("新增编码、名称重复数据，保存")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18254(self, drivers):
        pass


    @allure.story("总部端物料分类维护")  # 用户故事名称
    @allure.title("全流程报表物料分类维护列表按创建时间倒序排序")  # 用例名称
    @allure.description("检查列表排序")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18605(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2913:
    @allure.story("OTP烧录数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT烧录数据供应商上传请求参数检查")  # 用例名称
    @allure.description("检查请求参数")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18435(self, drivers):
        pass


    @allure.story("OTP烧录数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT烧录数据供应商上传部分参数缺失/为空，上传失败返回对应提示")  # 用例名称
    @allure.description("请求时，各个参数依次为空/缺失")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18436(self, drivers):
        pass


    @allure.story("OTP烧录数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT烧录数据供应商上传参数正确，上传成功")  # 用例名称
    @allure.description("参数正确==·")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18440(self, drivers):
        pass


    @allure.story("OTP烧录数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT烧录数据供应商上传MD51错误时，上传失败，并返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18595(self, drivers):
        pass


    @allure.story("OTP烧录数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT烧录数据供应商上传料号错误时，上传失败，并返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18596(self, drivers):
        pass


    @allure.story("OTP烧录数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT烧录数据供应商上传sensorIdproduceTime重复时，上传失败，并返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18597(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2917:
    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询菜单权限校验")  # 用例名称
    @allure.description("登录账号为配置该模块权限时==配置权限后")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18601(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询查询条件检查")  # 用例名称
    @allure.description("检查查询条件==检查查询条件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18603(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询列表字段检查")  # 用例名称
    @allure.description("检查列表字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18604(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询列表内容检查")  # 用例名称
    @allure.description("检查列表内容")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18606(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询操作按钮检查")  # 用例名称
    @allure.description("检查页面操作按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18609(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询列表按更新时间倒序排序")  # 用例名称
    @allure.description("检查列表排序")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18610(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询查询后正确返回查询结果")  # 用例名称
    @allure.description("按物料类别查询==按物料编码查询==按物料描述（中）查询==按物料描述（英）查询==按更新时间查询==条件组合查询")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18611(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询重置后，查询条件清空")  # 用例名称
    @allure.description("输入/选择查询条件后查询==点击重置按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18612(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询查询、翻页组合场景检查")  # 用例名称
    @allure.description("查询后翻页==重置、翻页后查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18613(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询选择每页展示条数，数量正确")  # 用例名称
    @allure.description("切换每页展示条数")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18614(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询获取SAP物料弹窗字段检查")  # 用例名称
    @allure.description("title==弹窗字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18618(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询获取SAP物料成功")  # 用例名称
    @allure.description("点击【获取SAP物料】==选择物料分类，点击获取")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18619(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询获取不存在的物料分类失败")  # 用例名称
    @allure.description("点击【获取SAP物料】==选择物料分类，点击获取不存在的物料分类==点击【获取SAP物料】==选择物料分类，点击获取不存在的物料分类")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18637(self, drivers):
        pass


    @allure.story("物料信息查询、同步")  # 用户故事名称
    @allure.title("全流程报表物料信息查询获取物料信息定时任务校验")  # 用例名称
    @allure.description("校验物料信息获取定时任务")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18638(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2885:
    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息查询条件检查")  # 用例名称
    @allure.description("检查查询条件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18762(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息列表字段检查")  # 用例名称
    @allure.description("检查列表字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18765(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息列表按创建时间倒序排序")  # 用例名称
    @allure.description("检查列表排序")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18767(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息列表内容检查")  # 用例名称
    @allure.description("检查列表内容")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18769(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息操作按钮检查")  # 用例名称
    @allure.description("检查页面操作按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18770(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息查询后正确返回查询结果")  # 用例名称
    @allure.description("按供应商编码查询==按供应商名称查询==按状态为空查询==按状态=启用查询==按状态=禁用查询==条件组合查询")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18771(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息重置后，查询条件清空")  # 用例名称
    @allure.description("输入/选择查询条件后查询==点击重置按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18773(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息查询、翻页组合场景检查")  # 用例名称
    @allure.description("查询后翻页==重置、翻页后查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18775(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息选择每页展示条数，数量正确")  # 用例名称
    @allure.description("切换每页展示条数")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18776(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息新增弹窗字段检查")  # 用例名称
    @allure.description("title==弹窗字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19052(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息字段为空时新增失败")  # 用例名称
    @allure.description("点击新增按钮，部分字段为空时保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19053(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息所有字段正确填写，新增成功")  # 用例名称
    @allure.description("点击新增按钮，全部字段正确填写后保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19054(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息新增供应商编码、供应商名称重复数据失败")  # 用例名称
    @allure.description("新增供应商编码、供应商名称重复数据，保存")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19055(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息编辑弹窗字段检查")  # 用例名称
    @allure.description("title==弹窗字段")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19056(self, drivers):
        pass


    @allure.story("供应商管理")  # 用户故事名称
    @allure.title("供应商信息编辑后保存成功")  # 用例名称
    @allure.description("点击列表后编辑按钮==检查弹窗字段内容==修改各字段后保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19069(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2914:
    @allure.story("OTP出货数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT出货数据供应商上传请求参数检查")  # 用例名称
    @allure.description("检查请求参数")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20688(self, drivers):
        pass


    @allure.story("OTP出货数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT出货数据供应商上传部分参数缺失/为空，上传失败返回对应提示")  # 用例名称
    @allure.description("请求时，各个参数依次为空/缺失")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20697(self, drivers):
        pass


    @allure.story("OTP出货数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT出货数据供应商上传参数正确，上传成功，后台形成批次号")  # 用例名称
    @allure.description("参数正确==·==参数正确==·")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20698(self, drivers):
        pass


    @allure.story("OTP出货数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT烧录数据供应商上传传音供应商编码、传音供应商名称错误时，上传失败并返回对应提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20699(self, drivers):
        pass


    @allure.story("OTP出货数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT出货数据供应商上传箱号不存在时，上传失败并返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20700(self, drivers):
        pass


    @allure.story("OTP出货数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT出货数据供应商上传sensorid已上传，上传失败并返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20701(self, drivers):
        pass


    @allure.story("OTP出货数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT出货数据供应商上传箱号物料编码不唯一，上传失败并返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20702(self, drivers):
        pass


    @allure.story("OTP出货数据供应商上传接口")  # 用户故事名称
    @allure.title("OPT出货数据供应商上传materialCodesensorid与烧录数据表的materialCodesensorid不一致，上传失败并返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20703(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2909:
    @allure.story("总部sensorid及moduledata查询")  # 用户故事名称
    @allure.title("烧录数据查询查询条件检查")  # 用例名称
    @allure.description("检查查询条件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20717(self, drivers):
        pass


    @allure.story("总部sensorid及moduledata查询")  # 用户故事名称
    @allure.title("烧录数据查询查询结果字段检查")  # 用例名称
    @allure.description("检查查询结果字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20735(self, drivers):
        pass


    @allure.story("总部sensorid及moduledata查询")  # 用户故事名称
    @allure.title("烧录数据查询查询结果为空时，显示无数据")  # 用例名称
    @allure.description("输入不存在的sensorid查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20736(self, drivers):
        pass


    @allure.story("总部sensorid及moduledata查询")  # 用户故事名称
    @allure.title("烧录数据查询查询结果内容检查")  # 用例名称
    @allure.description("输入正确sensorid查询")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20737(self, drivers):
        pass


    @allure.story("总部sensorid及moduledata查询")  # 用户故事名称
    @allure.title("烧录数据查询重置后，查询条件及结果清空")  # 用例名称
    @allure.description("输入正确sensorid查询==点击重置按钮")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20739(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2916:
    @allure.story("总部端模组批次烧录数据查询")  # 用户故事名称
    @allure.title("模组批次数据查询查询条件检查")  # 用例名称
    @allure.description("检查查询条件")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20740(self, drivers):
        pass


    @allure.story("总部端模组批次烧录数据查询")  # 用户故事名称
    @allure.title("模组批次数据查询列表字段检查")  # 用例名称
    @allure.description("检查列表字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20741(self, drivers):
        pass


    @allure.story("总部端模组批次烧录数据查询")  # 用户故事名称
    @allure.title("模组批次数据查询列表按创建时间倒序排序")  # 用例名称
    @allure.description("检查列表排序")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20742(self, drivers):
        pass


    @allure.story("总部端模组批次烧录数据查询")  # 用户故事名称
    @allure.title("模组批次数据查询列表内容检查")  # 用例名称
    @allure.description("检查列表内容")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20792(self, drivers):
        pass


    @allure.story("总部端模组批次烧录数据查询")  # 用户故事名称
    @allure.title("模组批次数据查询操作按钮检查")  # 用例名称
    @allure.description("检查页面操作按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20793(self, drivers):
        pass


    @allure.story("总部端模组批次烧录数据查询")  # 用户故事名称
    @allure.title("模组批次数据查询查询后正确返回查询结果")  # 用例名称
    @allure.description("按物料编码查询==按sensorid查询==按模组单体SN查询==按箱号查询==按创建时间查询==按供应商生产时间查询==按供应商名称查询==按客户生产工厂查询==条件组合查询")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20795(self, drivers):
        pass


    @allure.story("总部端模组批次烧录数据查询")  # 用户故事名称
    @allure.title("模组批次数据查询重置后，查询条件清空")  # 用例名称
    @allure.description("输入/选择查询条件后查询==点击重置按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20796(self, drivers):
        pass


    @allure.story("总部端模组批次烧录数据查询")  # 用户故事名称
    @allure.title("模组批次数据查询查询、翻页组合场景检查")  # 用例名称
    @allure.description("查询后翻页==重置、翻页后查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20797(self, drivers):
        pass


    @allure.story("总部端模组批次烧录数据查询")  # 用户故事名称
    @allure.title("模组批次数据查询英文版翻译检查")  # 用例名称
    @allure.description("英文版翻译检查")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20798(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2977:
    @allure.story("工厂TPS在线烧录接口")  # 用户故事名称
    @allure.title("工厂TPS在线烧录接口请求参数检查")  # 用例名称
    @allure.description("检查请求参数")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21724(self, drivers):
        pass


    @allure.story("工厂TPS在线烧录接口")  # 用户故事名称
    @allure.title("工厂TPS在线烧录接口参数缺失/为空，上传失败返回对应提示")  # 用例名称
    @allure.description("请求时参数为空/缺失")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21725(self, drivers):
        pass


    @allure.story("工厂TPS在线烧录接口")  # 用户故事名称
    @allure.title("工厂TPS在线烧录接口参数正确，成功获取OTP烧录数据")  # 用例名称
    @allure.description("参数正确==·")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21726(self, drivers):
        pass


    @allure.story("工厂TPS在线烧录接口")  # 用户故事名称
    @allure.title("工厂TPS在线烧录接口获取10个sensorid的烧录数据成功")  # 用例名称
    @allure.description("参数正确，参数包含10个sensorid==·")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21727(self, drivers):
        pass


    @allure.story("工厂TPS在线烧录接口")  # 用户故事名称
    @allure.title("工厂TPS在线烧录接口获取11个sensorid的烧录数据失败")  # 用例名称
    @allure.description("参数正确，参数包含11个sensorid==·")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21728(self, drivers):
        pass


    @allure.story("工厂TPS在线烧录接口")  # 用户故事名称
    @allure.title("工厂TPS在线烧录接口工厂本地库存在对应OTP烧录数据时，则从工厂本地库获取")  # 用例名称
    @allure.description("使用工厂本地库已有对应烧录数据的sensorid请求==·")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21729(self, drivers):
        pass


    @allure.story("工厂TPS在线烧录接口")  # 用户故事名称
    @allure.title("工厂TPS在线烧录接口工厂本地库无对应OTP烧录数据时，则从总部获取")  # 用例名称
    @allure.description("使用工厂本地库没有的烧录数据发送请求==·")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21730(self, drivers):
        pass


    @allure.story("工厂TPS在线烧录接口")  # 用户故事名称
    @allure.title("工厂TPS在线烧录接口获取不存在的sensorid，返回错误提示")  # 用例名称
    @allure.description("获取本地库及总部均不存在的烧录数据==·")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21731(self, drivers):
        pass


    @allure.story("工厂TPS在线烧录接口")  # 用户故事名称
    @allure.title("工厂TPS在线烧录接口从工厂获取烧录数据，同一sensorid存在多行数据时，取供应商生产时间最新的数据")  # 用例名称
    @allure.description("·")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21732(self, drivers):
        pass


    @allure.story("工厂TPS在线烧录接口")  # 用户故事名称
    @allure.title("工厂TPS在线烧录接口从总部获取烧录数据，同一sensorid存在多行数据时，取供应商生产时间最新的数据")  # 用例名称
    @allure.description("·")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21733(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2978:
    @allure.story("售后售后工具烧录接口")  # 用户故事名称
    @allure.title("售后工具烧录接口请求参数检查")  # 用例名称
    @allure.description("检查请求参数")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22201(self, drivers):
        pass


    @allure.story("售后售后工具烧录接口")  # 用户故事名称
    @allure.title("售后工具烧录接口参数缺失/为空，上传失败返回对应提示")  # 用例名称
    @allure.description("请求时参数为空/缺失")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22202(self, drivers):
        pass


    @allure.story("售后售后工具烧录接口")  # 用户故事名称
    @allure.title("售后工具烧录接口参数正确，成功获取OTP烧录数据")  # 用例名称
    @allure.description("参数正确==·")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22203(self, drivers):
        pass


    @allure.story("售后售后工具烧录接口")  # 用户故事名称
    @allure.title("售后工具烧录接口获取10个sensorid的烧录数据成功")  # 用例名称
    @allure.description("参数正确，参数包含10个sensorid==·")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22204(self, drivers):
        pass


    @allure.story("售后售后工具烧录接口")  # 用户故事名称
    @allure.title("售后工具烧录接口获取11个sensorid的烧录数据失败")  # 用例名称
    @allure.description("参数正确，参数包含11个sensorid==·")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22205(self, drivers):
        pass


    @allure.story("售后售后工具烧录接口")  # 用户故事名称
    @allure.title("售后工具烧录接口同一sensorid存在多行数据时，取供应商生产时间最新的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22206(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2982:
    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息菜单权限校验")  # 用例名称
    @allure.description("登录账号为配置该模块权限时==配置权限后")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22207(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息查询条件检查")  # 用例名称
    @allure.description("检查查询条件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22208(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息列表字段检查")  # 用例名称
    @allure.description("检查列表字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22209(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息列表按创建时间倒序排序")  # 用例名称
    @allure.description("检查列表排序")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22210(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息列表内容检查")  # 用例名称
    @allure.description("检查列表内容")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22211(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息操作按钮检查")  # 用例名称
    @allure.description("检查页面操作按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22212(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息查询后正确返回查询结果")  # 用例名称
    @allure.description("按物料类别查询==按物料编码查询==按物料描述（中）查询==按物料描述（英）查询==条件组合查询")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22213(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息重置后，查询条件清空")  # 用例名称
    @allure.description("输入/选择查询条件后查询==点击重置按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22214(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息查询、翻页组合场景检查")  # 用例名称
    @allure.description("查询后翻页==重置、翻页后查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22215(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息选择每页展示条数，数量正确")  # 用例名称
    @allure.description("切换每页展示条数")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22216(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息获取总部物料弹窗字段检查")  # 用例名称
    @allure.description("title==弹窗字段==title==弹窗字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22217(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息起止物料编码为空时，获取总部物料成功")  # 用例名称
    @allure.description("点击【获取总部物料】==起止物料编码为空，点击获取")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22218(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息根据起止物料编码获取总部物料成功")  # 用例名称
    @allure.description("点击【获取总部物料】==填写起止物料编码，点击获取")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22219(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息获取不存在的物料编码失败")  # 用例名称
    @allure.description("点击【获取总部物料】==输入不存在的起止物料编码")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22220(self, drivers):
        pass


    @allure.story("工厂物料信息同步及拉取")  # 用户故事名称
    @allure.title("看板物料信息页面翻译检查")  # 用例名称
    @allure.description("切换英文版，检查页面翻译")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22225(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2981:
    @allure.story("工厂sensorid及moduledata查询")  # 用户故事名称
    @allure.title("看板烧录数据查询查询条件检查")  # 用例名称
    @allure.description("检查查询条件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22307(self, drivers):
        pass


    @allure.story("工厂sensorid及moduledata查询")  # 用户故事名称
    @allure.title("看板烧录数据查询查询结果字段检查")  # 用例名称
    @allure.description("检查查询结果字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22308(self, drivers):
        pass


    @allure.story("工厂sensorid及moduledata查询")  # 用户故事名称
    @allure.title("看板烧录数据查询查询结果为空时，显示无数据")  # 用例名称
    @allure.description("输入不存在的sensorid查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22309(self, drivers):
        pass


    @allure.story("工厂sensorid及moduledata查询")  # 用户故事名称
    @allure.title("看板烧录数据查询查询结果内容检查")  # 用例名称
    @allure.description("输入正确sensorid查询")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22310(self, drivers):
        pass


    @allure.story("工厂sensorid及moduledata查询")  # 用户故事名称
    @allure.title("看板烧录数据查询重置后，查询条件及结果清空")  # 用例名称
    @allure.description("输入正确sensorid查询==点击重置按钮")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22311(self, drivers):
        pass


@allure.feature("MES_OTP")  # 迭代名称
class Teststory_2979:
    @allure.story("工厂端模组批次数据查询、拉取")  # 用户故事名称
    @allure.title("看板模组批次数据查询查询条件检查")  # 用例名称
    @allure.description("检查查询条件")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22377(self, drivers):
        pass


    @allure.story("工厂端模组批次数据查询、拉取")  # 用户故事名称
    @allure.title("看板模组批次数据查询列表字段检查")  # 用例名称
    @allure.description("检查列表字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22378(self, drivers):
        pass


    @allure.story("工厂端模组批次数据查询、拉取")  # 用户故事名称
    @allure.title("看板模组批次数据查询列表按创建时间倒序排序")  # 用例名称
    @allure.description("检查列表排序")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22379(self, drivers):
        pass


    @allure.story("工厂端模组批次数据查询、拉取")  # 用户故事名称
    @allure.title("看板模组批次数据查询列表内容检查")  # 用例名称
    @allure.description("检查列表内容==检查列表内容")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22431(self, drivers):
        pass


    @allure.story("工厂端模组批次数据查询、拉取")  # 用户故事名称
    @allure.title("看板模组批次数据查询操作按钮检查")  # 用例名称
    @allure.description("检查页面操作按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22445(self, drivers):
        pass


    @allure.story("工厂端模组批次数据查询、拉取")  # 用户故事名称
    @allure.title("看板模组批次数据查询查询后正确返回查询结果")  # 用例名称
    @allure.description("按物料编码查询==按sensorid查询==按模组单体SN查询==按箱号查询==按供应商生产时间查询==按供应商名称查询==按客户生产工厂查询==条件组合查询")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22490(self, drivers):
        pass


    @allure.story("工厂端模组批次数据查询、拉取")  # 用户故事名称
    @allure.title("看板模组批次数据查询重置后，查询条件清空")  # 用例名称
    @allure.description("输入/选择查询条件后查询==点击重置按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22491(self, drivers):
        pass


    @allure.story("工厂端模组批次数据查询、拉取")  # 用户故事名称
    @allure.title("看板模组批次数据查询英文版翻译检查")  # 用例名称
    @allure.description("英文版翻译检查")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22492(self, drivers):
        pass


    @allure.story("工厂端模组批次数据查询、拉取")  # 用户故事名称
    @allure.title("看板模组批次数据查询拉取总部数据弹窗字段检查")  # 用例名称
    @allure.description("英文版翻译检查==检查拉取总部数据弹窗字段==检查拉取总部数据弹窗字段==物料编码选择弹窗")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22493(self, drivers):
        pass


    @allure.story("工厂端模组批次数据查询、拉取")  # 用户故事名称
    @allure.title("看板模组批次数据查询拉取总部数据成功")  # 用例名称
    @allure.description("【拉取总部数据】，填写物料编码后拉取")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22565(self, drivers):
        pass


if __name__ == '__main__':
      pass
