import allure
import pytest
@allure.feature("MESv5_4")  # 迭代名称
class Teststory_446:
    @allure.story("包装工单项目配置增加清单打印份数、箱标打印份数配置")  # 用户故事名称
    @allure.title("总部辅助数据新增单值手动录入项M1038打印份数/清单M1039打印份数/箱标.")  # 用例名称
    @allure.description("检查辅助数据单值手动录项")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1807(self, drivers):
        pass


    @allure.story("包装工单项目配置增加清单打印份数、箱标打印份数配置")  # 用户故事名称
    @allure.title("总部辅助数据'M1038打印份数/清单M1039打印份数/箱标.'推送到工厂成功")  # 用例名称
    @allure.description("推送新增的辅助数据'M1038打印份数/清单M1039打印份数/箱标.'到工厂")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1808(self, drivers):
        pass


    @allure.story("包装工单项目配置增加清单打印份数、箱标打印份数配置")  # 用户故事名称
    @allure.title("工厂拉取辅助数据'M1038打印份数/清单M1039打印份数/箱标.'成功")  # 用例名称
    @allure.description("工厂拉取新增辅助数据'M1038打印份数/清单M1039打印份数/箱标.'")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1809(self, drivers):
        pass


    @allure.story("包装工单项目配置增加清单打印份数、箱标打印份数配置")  # 用户故事名称
    @allure.title("工厂物料编码_物料配置，配置'打印份数/清单、打印份数箱标/箱标'成功")  # 用例名称
    @allure.description("选择物料编码进行物料配置，配置'打印份数/清单、打印份数箱标/箱标'并保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1825(self, drivers):
        pass


    @allure.story("包装工单项目配置增加清单打印份数、箱标打印份数配置")  # 用户故事名称
    @allure.title("物料编码未配置'打打印份数/清单、打印份数箱标/箱标'时，默认打印份数为1")  # 用例名称
    @allure.description("卡通箱装箱称重配置工单==卡通箱装箱称重==卡通箱装箱==卡通箱称重")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1826(self, drivers):
        pass


    @allure.story("包装工单项目配置增加清单打印份数、箱标打印份数配置")  # 用户故事名称
    @allure.title("物料编码已配置'打打印份数/清单、打印份数箱标/箱标'时，正确展示配置的打印份数")  # 用例名称
    @allure.description("卡通箱装箱称重配置工单==卡通箱装箱称重配置工单==卡通箱装箱==卡通箱称重")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1827(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_463:
    @allure.story("组装_关键料绑定增加管控解绑时间配置")  # 用户故事名称
    @allure.title("组装管理_关键料绑定新增操作权限管控解绑时间（ID1001）")  # 用例名称
    @allure.description("检查组装管理_关键料绑定操作权限")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2029(self, drivers):
        pass


    @allure.story("组装_关键料绑定增加管控解绑时间配置")  # 用户故事名称
    @allure.title("无'管控解绑时间'操作权限时，无法操作勾选框")  # 用例名称
    @allure.description("检查组装关键料绑定页面中的'管控解绑时间'勾选框==检查组装关键料绑定页面中的'管控解绑时间'勾选框")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2115(self, drivers):
        pass


    @allure.story("组装_关键料绑定增加管控解绑时间配置")  # 用户故事名称
    @allure.title("'管控解绑时间'默认勾选")  # 用例名称
    @allure.description("检查'管控解绑时间'默认勾选状态==检查'管控解绑时间'默认勾选状态")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2116(self, drivers):
        pass


    @allure.story("组装_关键料绑定增加管控解绑时间配置")  # 用户故事名称
    @allure.title("有'管控解绑时间'操作权限时，可操作勾选框")  # 用例名称
    @allure.description("检查组装关键料绑定页面中的'管控解绑时间'勾选框==检查组装关键料绑定页面中的'管控解绑时间'勾选框")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2117(self, drivers):
        pass


    @allure.story("组装_关键料绑定增加管控解绑时间配置")  # 用户故事名称
    @allure.title("扫入关键料SN的类型=管控解绑时间物料类型，无解绑记录，可成功绑定关键料")  # 用例名称
    @allure.description("扫入类型=管控解绑时间物料类型的关键料SN")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2179(self, drivers):
        pass


    @allure.story("组装_关键料绑定增加管控解绑时间配置")  # 用户故事名称
    @allure.title("扫入关键料SN的类型≠管控解绑时间物料类型时，可成功绑定关键料")  # 用例名称
    @allure.description("	扫入类型≠管控解绑时间物料类型的关键料SN")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2183(self, drivers):
        pass


    @allure.story("组装_关键料绑定增加管控解绑时间配置")  # 用户故事名称
    @allure.title("勾选'管控解绑时间'，扫入关键料SN的类型=管控解绑时间物料类型，有lt4h的解绑记录，绑定关键料失败")  # 用例名称
    @allure.description("扫入类型=管控解绑时间物料类型的关键料SN")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2186(self, drivers):
        pass


    @allure.story("组装_关键料绑定增加管控解绑时间配置")  # 用户故事名称
    @allure.title("不勾选'管控解绑时间'，扫入关键料SN的类型=管控解绑时间物料类型，有lt4h的解绑记录，绑定关键料成功")  # 用例名称
    @allure.description("扫入类型=管控解绑时间物料类型的关键料SN")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2187(self, drivers):
        pass


    @allure.story("组装_关键料绑定增加管控解绑时间配置")  # 用户故事名称
    @allure.title("关键料绑定方案中的关键料类型不存在于'管控解绑时间物料类型'时，不展示'管控解绑时间'，且不做解绑时间管控")  # 用例名称
    @allure.description("选择关键料绑定方案中的关键料类型不存在于'管控解绑时间物料类型'的工单==绑定4h内解绑的关键料")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2188(self, drivers):
        pass


    @allure.story("组装_关键料绑定增加管控解绑时间配置")  # 用户故事名称
    @allure.title("取消勾选'管控解绑时间'时，操作日志记录正确记录该操作")  # 用例名称
    @allure.description("取消勾选'管控解绑时间'==操作日志按'方式二'查询该工单操作记录")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2189(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_562:
    @allure.story("包装工单增加quot样机下达quot按钮，单机头样机下达时调整工单校验逻辑")  # 用户故事名称
    @allure.title("用户权限维护包装工单模块增加'样机下达'按钮权限")  # 用例名称
    @allure.description("检查用户权限维护包装工单模块==登录用户无'样机下达'按钮权限时，右键包装工单列表中未下达的工单==登录用户已配置'样机下达'按钮权限时，右键包装工单列表中未下达的工单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2232(self, drivers):
        pass


    @allure.story("包装工单增加quot样机下达quot按钮，单机头样机下达时调整工单校验逻辑")  # 用户故事名称
    @allure.title("通过'样机下达'工单，部分字段不校验")  # 用例名称
    @allure.description("新建工单，不配置以下信息（其他必填信息正确填写）彩盒标、彩盒标模板2、装箱清单模板、箱标、箱标模板2、返利标、彩盒MRP标、箱MRP标；工单料号的整机装箱数量、整机理论重量、盒箱误差、装箱理论重量、箱重误差、盒标内存配置、箱标内存配置。==右键该工单，选择'样机下达'")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2242(self, drivers):
        pass


    @allure.story("包装工单增加quot样机下达quot按钮，单机头样机下达时调整工单校验逻辑")  # 用户故事名称
    @allure.title("物料组不为120时，无法通过'样机下达'按钮下达工单")  # 用例名称
    @allure.description("新建物料组不为120的工单，右键该工单，选择'样机下达'")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2243(self, drivers):
        pass


    @allure.story("包装工单增加quot样机下达quot按钮，单机头样机下达时调整工单校验逻辑")  # 用户故事名称
    @allure.title("包装工单页面新增字段'样机下达'翻译检查")  # 用例名称
    @allure.description("登录英文版系统，检查包装工单页面新增字段'样机下达'翻译")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2674(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_556:
    @allure.story("组装工单新增'未完成数'字段")  # 用户故事名称
    @allure.title("组装工单列表增加字段未完成数字段，翻译为incompletenumber")  # 用例名称
    @allure.description("中文版检查列表==英文版检查列表")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2249(self, drivers):
        pass


    @allure.story("组装工单新增'未完成数'字段")  # 用户故事名称
    @allure.title("组装工单未完成数计算规则校验")  # 用例名称
    @allure.description("校验未完成数计算规则==校验未完成数计算规则")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2250(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_571:
    @allure.story("包装工单新增'未完成数'字段")  # 用户故事名称
    @allure.title("包装工单未完成数计算规则校验")  # 用例名称
    @allure.description("校验未完成数计算规则==校验未完成数计算规则")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2251(self, drivers):
        pass


    @allure.story("包装工单新增'未完成数'字段")  # 用户故事名称
    @allure.title("包装工单列表增加字段未完成数字段，翻译为incompletenumber")  # 用例名称
    @allure.description("中文版检查列表==英文版检查列表")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2252(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_570:
    @allure.story("巴基斯坦TTE新增工单信息查询接口（看板实现）")  # 用户故事名称
    @allure.title("所有参数正确填写查询组装工段工单信息，返回满足条件，且工艺路线包含RQC站点的工单信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3007(self, drivers):
        pass


    @allure.story("巴基斯坦TTE新增工单信息查询接口（看板实现）")  # 用户故事名称
    @allure.title("所有参数正确填写查询包装工段工单信息，返回正确内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3008(self, drivers):
        pass


    @allure.story("巴基斯坦TTE新增工单信息查询接口（看板实现）")  # 用户故事名称
    @allure.title("非必填参数为空，正确填写必填参数（工段、日期）查询组装工段工单信息，返回满足条件，且工艺路线包含RQC站点的工单信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3009(self, drivers):
        pass


    @allure.story("巴基斯坦TTE新增工单信息查询接口（看板实现）")  # 用户故事名称
    @allure.title("非必填参数为空，正确填写必填参数（工段、日期）查询包装工段工单信息，返回正确内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3010(self, drivers):
        pass


    @allure.story("巴基斯坦TTE新增工单信息查询接口（看板实现）")  # 用户故事名称
    @allure.title("必填参数为空，返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3011(self, drivers):
        pass


    @allure.story("巴基斯坦TTE新增工单信息查询接口（看板实现）")  # 用户故事名称
    @allure.title("参数'工段'不为BE或DC，返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3012(self, drivers):
        pass


    @allure.story("巴基斯坦TTE新增工单信息查询接口（看板实现）")  # 用户故事名称
    @allure.title("参数'产线'与MES命名规范不一致，返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3013(self, drivers):
        pass


    @allure.story("巴基斯坦TTE新增工单信息查询接口（看板实现）")  # 用户故事名称
    @allure.title("参数'工单'不存在时，返回错误提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3014(self, drivers):
        pass


    @allure.story("巴基斯坦TTE新增工单信息查询接口（看板实现）")  # 用户故事名称
    @allure.title("查询组装工段时，工单字段传入工艺路线不包含RQC站点的工单号，返回空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3015(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_759:
    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("总部单行数据禁用/启用成功")  # 用例名称
    @allure.description("勾选单行状态为启用的数据禁用==勾选单行状态为禁用的数据启用")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3543(self, drivers):
        pass


    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("总部禁用/启用数据后，正确推送到工厂")  # 用例名称
    @allure.description("禁用/启用数据后，推送到工厂")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3544(self, drivers):
        pass


    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("总部检查新增查询条件'状态'")  # 用例名称
    @allure.description("检查查询条件==检查该查询条件下拉枚举==筛选各状态数据==检查查询条件==检查该查询条件下拉枚举==筛选各状态数据")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3545(self, drivers):
        pass


    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("总部列表新增字段'状态'")  # 用例名称
    @allure.description("检查列表字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3546(self, drivers):
        pass


    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("总部新增数据默认状态为'启用'")  # 用例名称
    @allure.description("新增数据成功==新增数据成功")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3547(self, drivers):
        pass


    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("工厂列表新增字段'状态'")  # 用例名称
    @allure.description("检查列表字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3548(self, drivers):
        pass


    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("工厂检查新增查询条件'状态'")  # 用例名称
    @allure.description("检查查询条件==检查该查询条件下拉枚举==筛选各状态数据")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3549(self, drivers):
        pass


    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("工厂拉取总部数据后，状态正确")  # 用例名称
    @allure.description("工厂拉取总部数据")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3550(self, drivers):
        pass


    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("总部多行相同状态数据禁用/启用成功")  # 用例名称
    @allure.description("勾选多行状态为启用的数据禁用==勾选多行状态为禁用的数据启用")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3551(self, drivers):
        pass


    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("总部多行不同状态数据禁用/启用失败")  # 用例名称
    @allure.description("勾选多行状态不同的数据禁用/启用")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3552(self, drivers):
        pass


    @allure.story("sorting文件管理增加禁用、启用功能")  # 用户故事名称
    @allure.title("工具接口无法获取已禁用的sorting文件")  # 用例名称
    @allure.description("工具接口获取已禁用sorting文件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3553(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_763:
    @allure.story("CKD\SKD工单自动填充箱重上限15（按工厂辅助数据维护值填充）")  # 用户故事名称
    @allure.title("总部检查增加工厂辅助数据'CKD箱重上限（13080042）'")  # 用例名称
    @allure.description("检查辅助数据==检查字典工厂辅助数据")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3554(self, drivers):
        pass


    @allure.story("CKD\SKD工单自动填充箱重上限15（按工厂辅助数据维护值填充）")  # 用户故事名称
    @allure.title("工厂拉取新增字典值辅助数据CKD箱重上限（13080042）成功")  # 用例名称
    @allure.description("工厂拉取总部辅助数据==工厂拉取总部字典数据工厂辅助数据")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3555(self, drivers):
        pass


    @allure.story("CKD\SKD工单自动填充箱重上限15（按工厂辅助数据维护值填充）")  # 用户故事名称
    @allure.title("未配置辅助数据'箱重上限'时，CKD/SKD工单箱重上限需手动维护")  # 用例名称
    @allure.description("新建工单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4487(self, drivers):
        pass


    @allure.story("CKD\SKD工单自动填充箱重上限15（按工厂辅助数据维护值填充）")  # 用户故事名称
    @allure.title("已配置辅助数据'箱重上限'时，CKD/SKD工单箱重上限自动带出")  # 用例名称
    @allure.description("新建CKD/SKD工单==正确填写其他内容并保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4488(self, drivers):
        pass


    @allure.story("CKD\SKD工单自动填充箱重上限15（按工厂辅助数据维护值填充）")  # 用户故事名称
    @allure.title("CKD/SKD工单自动带出的箱重上限修改成功")  # 用例名称
    @allure.description("新建CKD/SKD工单==修改自动带出的箱重上限==正确填写其他内容并保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4489(self, drivers):
        pass


    @allure.story("CKD\SKD工单自动填充箱重上限15（按工厂辅助数据维护值填充）")  # 用户故事名称
    @allure.title("修改CKD/SKD工单时，若箱重上限为空，则根据辅助数据匹配并自动带出")  # 用例名称
    @allure.description("选择前置条件中新增的箱重上限为空的工单，点击修改==保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4519(self, drivers):
        pass


    @allure.story("CKD\SKD工单自动填充箱重上限15（按工厂辅助数据维护值填充）")  # 用户故事名称
    @allure.title("工厂配置工厂辅助数据'CKD箱重上限'成功")  # 用例名称
    @allure.description("新增类型为'CKD箱重上限'的数据")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7342(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_788:
    @allure.story("上卡板增加'打印箱单'按钮")  # 用户故事名称
    @allure.title("未完成'上板完成打标'时打印清单，报错提示请先进行上板完成打标")  # 用例名称
    @allure.description("未完成'上板完成打标'时打印清单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4523(self, drivers):
        pass


    @allure.story("上卡板增加'打印箱单'按钮")  # 用户故事名称
    @allure.title("已完成'上板完成打标'时打印箱单，箱单打印成功")  # 用例名称
    @allure.description("已完成'上板完成打标'时打印箱单==已完成'上板完成打标'时打印箱单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4524(self, drivers):
        pass


    @allure.story("上卡板增加'打印箱单'按钮")  # 用户故事名称
    @allure.title("上卡板模块UI检查")  # 用例名称
    @allure.description("检查新增字段==切换英文版检查新增字段翻译")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4551(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_800:
    @allure.story("物料配置匹配查询条件不生效")  # 用户故事名称
    @allure.title("工厂物料配置按'品牌'正确过滤")  # 用例名称
    @allure.description("选择'品牌'后查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4552(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_688:
    @allure.story("包装卡通箱装箱尾箱增加权限控制")  # 用户故事名称
    @allure.title("包装卡通箱装箱称重勾选'尾箱'时，需校验账号密码")  # 用例名称
    @allure.description("点击勾选'尾箱'==输入错误密码==输入正确密码")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4636(self, drivers):
        pass


    @allure.story("包装卡通箱装箱尾箱增加权限控制")  # 用户故事名称
    @allure.title("包装卡通箱装箱称重装尾箱后，功能正确")  # 用例名称
    @allure.description("点击勾选'尾箱'==输入错误密码==输入正确密码==配置工单，点击勾选'尾箱'，并输入正确密码==装箱==配置工单，点击勾选'尾箱'，并输入正确密码==装箱")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4637(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_964:
    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("包装生产进度查询页面检查")  # 用例名称
    @allure.description("进入包装生产进度查询页面，检查UI")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4719(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("权限检查")  # 用例名称
    @allure.description("1、登录账号无权限；==2、登录账号已配置权限；")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4720(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("查询条件检查")  # 用例名称
    @allure.description("1、检查查询条件；==1、检查查询条件；")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4721(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("必选/填条件检查")  # 用例名称
    @allure.description("1、检查必填条件；")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4722(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("产线下拉选项检查")  # 用例名称
    @allure.description("检查产线下拉枚举")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4723(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("机型下拉选项检查")  # 用例名称
    @allure.description("未选择产线时，检查机型下拉枚举==选择产线后，检查机型下拉枚举")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4735(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("起止日期跨度限制检查")  # 用例名称
    @allure.description("检查起止日期跨度限制")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4810(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("选择条件，正确返回查询结果")  # 用例名称
    @allure.description("选择日期，产线、机型为空，查询==选择日期。产线、机型，查询")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4811(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("重置按钮功能校验")  # 用例名称
    @allure.description("1、选择条件后点击【重置】；")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4812(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("导出按钮功能校验")  # 用例名称
    @allure.description("未查询时导出；==查询后导出；==查询后导出；")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4813(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("列表字段检查")  # 用例名称
    @allure.description("检查列表字段==检查列表字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4814(self, drivers):
        pass


    @allure.story("数据查询新增包装生产进度查询")  # 用户故事名称
    @allure.title("列表内容检查")  # 用例名称
    @allure.description("检查列表内容")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4815(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_760:
    @allure.story("生产效率报表增加工段=预加工查询")  # 用户故事名称
    @allure.title("工段下拉枚举增加'预加工'")  # 用例名称
    @allure.description("检查工段下拉枚举")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4824(self, drivers):
        pass


    @allure.story("生产效率报表增加工段=预加工查询")  # 用户故事名称
    @allure.title("查询'预加工'工段生产效率报表")  # 用例名称
    @allure.description("工段选择'预加工'，其他条件并查询")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4834(self, drivers):
        pass


    @allure.story("生产效率报表增加工段=预加工查询")  # 用户故事名称
    @allure.title("导出'预加工'工段生产效率报表成功")  # 用例名称
    @allure.description("工段选择'预加工'，其他条件，查询并导出")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4835(self, drivers):
        pass


    @allure.story("生产效率报表增加工段=预加工查询")  # 用户故事名称
    @allure.title("预加工工段生产效率报表数据检查")  # 用例名称
    @allure.description("预加工工段选择工单；==预加工工段不选择工单；==查询预加工工段生产效率报表")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5009(self, drivers):
        pass


    @allure.story("生产效率报表增加工段=预加工查询")  # 用户故事名称
    @allure.title("未导入日计划时正确展示错误提示")  # 用例名称
    @allure.description("工段选择预加工，选择时间、工单等查询条件，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7416(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1312:
    @allure.story("装箱界面标签模板锁死工单带出")  # 用户故事名称
    @allure.title("最小包装小包装标签不可手动修改")  # 用例名称
    @allure.description("配置工单==点击修改标签==打印标签")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7481(self, drivers):
        pass


    @allure.story("装箱界面标签模板锁死工单带出")  # 用户故事名称
    @allure.title("装中箱小中箱标、电池标、三层包装中箱标、SRO箱标不可手动修改")  # 用例名称
    @allure.description("配置工单==点击修改小中箱标、电池标、三层包装中箱标、SRO箱标==打印标签")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7482(self, drivers):
        pass


    @allure.story("装箱界面标签模板锁死工单带出")  # 用户故事名称
    @allure.title("装大箱大箱标、SRO箱标不可手动修改")  # 用例名称
    @allure.description("配置工单==点击修改大箱标、SRO箱标==打印标签")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7483(self, drivers):
        pass


    @allure.story("装箱界面标签模板锁死工单带出")  # 用户故事名称
    @allure.title("上卡板卡板标、电池卡板标不可手动修改")  # 用例名称
    @allure.description("配置工单==点击修改卡板标、电池卡板标==打印标签")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7484(self, drivers):
        pass


    @allure.story("装箱界面标签模板锁死工单带出")  # 用户故事名称
    @allure.title("最小包装包装工单下达后，修改工单中的小包装标签，刷新最小包装页面后，标签正确更新")  # 用例名称
    @allure.description("配置工单==在包装工单页面选择该工单，通过项目配置修改小包装标签模板并保存==重新进入最小包装页面并配置该工单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7485(self, drivers):
        pass


    @allure.story("装箱界面标签模板锁死工单带出")  # 用户故事名称
    @allure.title("装中箱包装工单下达后，修改工单中的'中箱标、电池标、三层包装中箱标、SRO箱标'标签模板，刷新装中箱页面后，标签正确更新")  # 用例名称
    @allure.description("配置工单==在包装工单页面选择该工单，通过项目配置修改中箱标、电池标、三层包装中箱标、SRO箱标签模板并保存==重新进入装中箱页面并配置该工单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7486(self, drivers):
        pass


    @allure.story("装箱界面标签模板锁死工单带出")  # 用户故事名称
    @allure.title("装大箱包装工单下达后，修改工单中的'大箱标、SRO箱标'标签模板，刷新装大箱页面后，标签正确更新")  # 用例名称
    @allure.description("配置工单==在包装工单页面选择该工单，通过项目配置修改大箱标、SRO箱标签模板并保存==重新进入装大箱页面并配置该工单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7487(self, drivers):
        pass


    @allure.story("装箱界面标签模板锁死工单带出")  # 用户故事名称
    @allure.title("上卡板包装工单下达后，修改工单中的'卡板标、电池卡板标'标签模板，刷新上卡板页面后，标签正确更新")  # 用例名称
    @allure.description("配置工单==在包装工单页面选择该工单，通过项目配置修改卡板标、电池卡板标标签模板并保存==重新进入上卡板页面并配置该工单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7488(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1311:
    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("模块权限检查")  # 用例名称
    @allure.description("当前登录用户无权限==当前登录用户已配置权限")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7510(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("QC核箱页面UI检查")  # 用例名称
    @allure.description("检查页面UI")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7513(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("产线下拉枚举检查")  # 用例名称
    @allure.description("检查产线下拉枚举")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7514(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("配置工单号后，正确带出工单信息")  # 用例名称
    @allure.description("选择产线、点击工单配置按钮==选择工单并确认==选择产线、点击工单配置按钮==选择工单并确认")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7515(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("扫入错误中箱号拦截并提示")  # 用例名称
    @allure.description("扫入错误中箱号")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7516(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("扫入不属于当前工单的中箱号拦截并提示")  # 用例名称
    @allure.description("扫入不属于当前工单的中箱号")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7517(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("扫入的中箱号装箱方式为物料装中箱或单体装中箱，拦截并提示")  # 用例名称
    @allure.description("扫入的中箱号装箱方式为物料装中箱或单体装中箱")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7518(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("扫入正确中箱号，自动带出中箱号、中箱净重、中箱毛重")  # 用例名称
    @allure.description("扫入正确的中箱号（箱号正确、属于当前工单、装箱方式为最小箱装箱）==扫入正确的中箱号（状态为生效/已核箱、箱号正确、属于当前工单、装箱方式为最小箱装箱）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7631(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("扫入状态为'已核箱'的中箱号，可重复核箱")  # 用例名称
    @allure.description("扫入正确的中箱号（状态为已核箱、箱号正确、属于当前工单、装箱方式为最小箱装箱）==扫入正确的中箱号（状态为已核箱、箱号正确、属于当前工单、装箱方式为最小箱装箱）==继续扫入正确小箱号==扫入正确的中箱号（状态为已核箱、箱号正确、属于当前工单、装箱方式为最小箱装箱）==继续扫入正确小箱号")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7666(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("QC核箱成功")  # 用例名称
    @allure.description("选择产线、点击工单配置按钮==选择工单并确认==扫入正确中箱号==正确扫入该中箱的全部小箱号")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7714(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("扫入不存在小箱号，拦截并提示")  # 用例名称
    @allure.description("扫入错误小箱号")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7715(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("扫入不属于该中箱的小箱号，拦截并提示")  # 用例名称
    @allure.description("扫入不属于该中箱的小箱号")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7716(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("扫入正确小箱号，校验通过")  # 用例名称
    @allure.description("扫入正确小箱号")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7717(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("重复扫入正确小箱号，拦截并提示")  # 用例名称
    @allure.description("重复扫入正确小箱号")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7718(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("连续扫入中箱号，正确带出中箱信息")  # 用例名称
    @allure.description("扫入正确中箱号A后，再扫入正确中箱号B==扫入正确中箱号A后，再扫入正确中箱号B")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7719(self, drivers):
        pass


    @allure.story("新增QC核箱功能")  # 用户故事名称
    @allure.title("QC核箱，连续扫入中箱号，正确带出中箱信息")  # 用例名称
    @allure.description("选择产线、点击工单配置按钮==选择工单并确认==扫入正确中箱号A==再次扫入中箱号B")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10139(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1310:
    @allure.story("SKD最小包装投产需要限制投产数量")  # 用户故事名称
    @allure.title("SKD最小包装投产数量限制规则校验")  # 用例名称
    @allure.description("配置工单==输入数量并回车==配置工单==输入数量，使同一工单同一料号中下,已投产数量最小包装输入的数量大于工单中投料明细该料号对应的数量，并回车==输入数量，使同一工单同一料号中下,已投产数量最小包装输入的数量小于或等于工单中投料明细该料号对应的数量，并回车")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7855(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1309:
    @allure.story("SKD上卡板自动计算卡板毛重")  # 用户故事名称
    @allure.title("字典工厂辅助数据增加类型卡板补偿重量，编码为13080043")  # 用例名称
    @allure.description("总部选择字典工厂辅助数据，新增数据'卡板补偿重量'，编码为13080043==总部推送==工厂拉取")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7858(self, drivers):
        pass


    @allure.story("SKD上卡板自动计算卡板毛重")  # 用户故事名称
    @allure.title("上卡板新增字段'卡板补偿重量'")  # 用例名称
    @allure.description("进入工厂SDK/CKD包装上卡板页面==切换英文版")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7859(self, drivers):
        pass


    @allure.story("SKD上卡板自动计算卡板毛重")  # 用户故事名称
    @allure.title("未维护'工厂辅助数据卡板补偿重量'时，卡板补偿重量下拉枚举为空")  # 用例名称
    @allure.description("进入工厂SDK/CKD包装上卡板页面，检查卡板补偿重量下拉枚举")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7860(self, drivers):
        pass


    @allure.story("SKD上卡板自动计算卡板毛重")  # 用户故事名称
    @allure.title("已维护'工厂辅助数据卡板补偿重量'时，'卡板补偿重量'默认带出创建时间最早的维护值，且可修改成功")  # 用例名称
    @allure.description("	进入工厂SDK/CKD包装上卡板页面，检查卡板补偿重量默认值==修改卡板补偿重量默认值")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7861(self, drivers):
        pass


    @allure.story("SKD上卡板自动计算卡板毛重")  # 用户故事名称
    @allure.title("已维护'工厂辅助数据卡板补偿重量'时，'卡板补偿重量'默认带出创建时间最早的维护值，且可修改成功")  # 用例名称
    @allure.description("	进入工厂SDK/CKD包装上卡板页面，检查卡板补偿重量默认值==修改卡板补偿重量默认值（选择其他值）")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7862(self, drivers):
        pass


    @allure.story("SKD上卡板自动计算卡板毛重")  # 用户故事名称
    @allure.title("卡板实际重量修改为自动计算")  # 用例名称
    @allure.description("	进入工厂SDK/CKD包装上卡板页面，检查卡板补偿重量默认值==检查卡板实际重量值==修改卡板补偿重量默认值（选择其他值）==检查卡板实际重量值==点击【上板完成打标】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7863(self, drivers):
        pass


    @allure.story("SKD上卡板自动计算卡板毛重")  # 用户故事名称
    @allure.title("卡板补偿重量为空时，无法上板完成打标")  # 用例名称
    @allure.description("进入工厂SDK/CKD包装上卡板页面，检查卡板补偿重量默认值==点击【上板完成打标】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7864(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1307:
    @allure.story("SKD最小包装标签增加'湿敏等级'变量")  # 用户故事名称
    @allure.title("最小包装标签正确打印'湿敏等级'")  # 用例名称
    @allure.description("最小包装模块打印最小包装标签==补打最小包装标签==最小包装模块打印最小包装标签==补打最小包装标签")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7865(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1294:
    @allure.story("上卡板在线打印箱单增加一列'客户料号'")  # 用户故事名称
    @allure.title("上卡板在线打印箱单时，列表增加'客户料号（customercode）'")  # 用例名称
    @allure.description("上卡板在线打印箱单==上卡板在线打印箱单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7866(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1402:
    @allure.story("入库单同步SAP逻辑优化")  # 用户故事名称
    @allure.title("入库单同步SAP失败后，可再次同步")  # 用例名称
    @allure.description("已过账I段入库单重新同步==已过账II段入库单重新同步==已过账PCBA入库单重新同步==已过账整机入库单重新同步==已过账预加工入库单重新同步==已过账CKD/SKD入库单重新同步")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7867(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1526:
    @allure.story("物料编码根据机型自动带出品牌")  # 用户故事名称
    @allure.title("总部物料编码拉取SAP数据，匹配品牌机型表，自动填充品牌信息")  # 用例名称
    @allure.description("在品牌机型表配置一行该机型品牌数据==在总部物料编码拉取SAP数据")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9606(self, drivers):
        pass


    @allure.story("物料编码根据机型自动带出品牌")  # 用户故事名称
    @allure.title("总部物料编码拉取SAP数据，品牌机型表无匹配数据时不更新品牌信息")  # 用例名称
    @allure.description("在品牌机型表配置删除需要拉取的机型品牌数据==在总部物料编码拉取SAP数据")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9607(self, drivers):
        pass


    @allure.story("物料编码根据机型自动带出品牌")  # 用户故事名称
    @allure.title("总部物料编码拉取SAP数据，品牌机型表匹配多行数据时不更新品牌信息")  # 用例名称
    @allure.description("在品牌机型表配置多行需要拉取的机型品牌数据==在总部物料编码拉取SAP数据")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9608(self, drivers):
        pass


    @allure.story("物料编码根据机型自动带出品牌")  # 用户故事名称
    @allure.title("总部物料编码拉取SAP数据，匹配品牌机型表，自动填充品牌信息后可修改")  # 用例名称
    @allure.description("在品牌机型表配置一行该机型品牌数据==在总部物料编码拉取SAP数据==修改品牌信息")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9609(self, drivers):
        pass


    @allure.story("物料编码根据机型自动带出品牌")  # 用户故事名称
    @allure.title("总部推送物料编码数据成功")  # 用例名称
    @allure.description("总部推送已拉取的物料信息（含品牌信息）")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9617(self, drivers):
        pass


    @allure.story("物料编码根据机型自动带出品牌")  # 用户故事名称
    @allure.title("工厂拉取物料编码数据成功")  # 用例名称
    @allure.description("工厂拉取物料信息（含品牌信息）")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9618(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1560:
    @allure.story("组装工单下达时校验工单机型项目名与组装项目表是否一致")  # 用户故事名称
    @allure.title("组装工单下达时增加校验条件工单机型项目名与组装项目表是否一直")  # 用例名称
    @allure.description("新建工单，填写配置信息，使工单机型amp项目名与组装项目表不一致，下达工单==修改工单机型amp项目名，使其余组装项目表保持一致，下达工单==新建工单，填写配置信息，使工单机型amp项目名与组装项目表不一致，下达工单==修改工单机型amp项目名，使其余组装项目表保持一致，下达工单")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10193(self, drivers):
        pass


    @allure.story("组装工单下达时校验工单机型项目名与组装项目表是否一致")  # 用户故事名称
    @allure.title("组装工单机型项目名与组装项目表不一致时，检查英文提示")  # 用例名称
    @allure.description("切换至英文版新建工单，填写配置信息，使工单机型amp项目名与组装项目表不一致，下达工单==切换至英文版新建工单，填写配置信息，使工单机型amp项目名与组装项目表不一致，下达工单==切换至英文版新建工单，填写配置信息，使工单机型amp项目名与组装项目表不一致，下达工单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10194(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1561:
    @allure.story("包装工单下达时校验工单机型项目名与组装项目表是否一致")  # 用户故事名称
    @allure.title("包装工单下达时增加校验条件工单机型项目名与组装项目表是否一直")  # 用例名称
    @allure.description("新建包装工单，填写配置信息，使工单机型amp项目名与组装项目表不一致，下达工单==修改工单机型amp项目名，使其余组装项目表保持一致，下达工单==新建包装工单，填写配置信息，使工单机型amp项目名与组装项目表不一致，下达工单==修改工单机型amp项目名，使其余组装项目表保持一致，下达工单")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10195(self, drivers):
        pass


    @allure.story("包装工单下达时校验工单机型项目名与组装项目表是否一致")  # 用户故事名称
    @allure.title("包装工单机型项目名与组装项目表不一致时，检查英文提示")  # 用例名称
    @allure.description("切换至英文版新建工单，填写配置信息，使工单机型amp项目名与组装项目表不一致，下达工单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10196(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1678:
    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料模块权限检查")  # 用例名称
    @allure.description("登录无KD特殊物料模块权限账号==登录有该模块权限账号")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10230(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料模块UI检查")  # 用例名称
    @allure.description("检查页面字段、按钮、布局等")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10235(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料模块菜单位置检查")  # 用例名称
    @allure.description("检查KD特殊物料模块菜单位置")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10236(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料查询条件全部非必填")  # 用例名称
    @allure.description("检查KD特殊物料模块查询条件必填校验==条件为空查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10533(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料各条件查询，返回查询结果")  # 用例名称
    @allure.description("按物料编码模糊查询==按传音物料描述（英）模糊查询==按KD物料描述（英）模糊查询")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10543(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料多条件组合查询，正确返回查询结果")  # 用例名称
    @allure.description("三个查询条件均输入内容后查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10544(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料新增弹窗字段检查")  # 用例名称
    @allure.description("点击新增按钮，检查新增弹窗字段==点击新增按钮，检查新增弹窗字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10545(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料新增弹窗必填字段校验")  # 用例名称
    @allure.description("点击新增按钮，检查新增弹窗必填字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10546(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料新增弹窗必填字段为空，保存失败")  # 用例名称
    @allure.description("所有字段为空保存==部分必填字段为空")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10547(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料新增数据成功")  # 用例名称
    @allure.description("点击新增按钮，正确选择/填写各字段物料分类、物料编码、KD物料描述（英），保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10548(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料修改弹窗字段检查")  # 用例名称
    @allure.description("选中某行数据后点击修改按钮，检查修改弹窗字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10549(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料修改弹窗必填字段校验")  # 用例名称
    @allure.description("选中某行后点击修改按钮，检查修改弹窗必填字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10550(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料修改数据成功")  # 用例名称
    @allure.description("选中某行后点击修改按钮==修改'KD物料描述（英）'后保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10551(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料修改弹窗切换数据并修改保存成功")  # 用例名称
    @allure.description("选中某行后点击修改按钮==点击上一笔==修改后保存==重复步骤1，点击下一笔==修改后保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10552(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料新增时退出/关闭，数据不保存")  # 用例名称
    @allure.description("选中某行后点击修改按钮==修改后点击右上角关闭按钮==重复步骤1，点击【退出】按钮==点击新增按钮==编辑后点击右上角关闭按钮==重复步骤1，点击【退出】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10553(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料修改时退出/关闭，数据不保存")  # 用例名称
    @allure.description("选中某行后点击修改按钮==修改后点击右上角关闭按钮==重复步骤1，点击【退出】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10554(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料删除数据成功")  # 用例名称
    @allure.description("选中某行后点击【删除】==选中否==重复步骤1，点击是")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10555(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料导出数据成功")  # 用例名称
    @allure.description("全量数据导出==查询后导出")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10556(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料英文版检查")  # 用例名称
    @allure.description("登录英文版，进入KD特殊物料菜单，检查翻译")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10557(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料英文版导出时，导出表列名为英文")  # 用例名称
    @allure.description("登录英文版，进入KD特殊物料菜单，导出")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10558(self, drivers):
        pass


    @allure.story("工厂端基础数据新增KD特殊物料菜单")  # 用户故事名称
    @allure.title("KD特殊物料新增弹窗各字段下拉枚举检查")  # 用例名称
    @allure.description("点击新增按钮，检查'物料分类'下拉枚举==检查'物料分类'配置弹窗")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10559(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1732:
    @allure.story("包装管理增加SAP工单备注显示")  # 用户故事名称
    @allure.title("包装工单工单弹窗中的备注调整为SAP工单备注，从SAP获取")  # 用例名称
    @allure.description("检查弹窗字段==工厂新增工单==SAP获取工单==检查弹窗字段==工厂新增工单==SAP获取工单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10560(self, drivers):
        pass


    @allure.story("包装管理增加SAP工单备注显示")  # 用户故事名称
    @allure.title("包装投产DTI2工单信息增加SAP工单备注栏位显示")  # 用例名称
    @allure.description("检查包装投产DTI2页面字段==配置工单（SAP工单备注不为空）==检查包装投产DTI2页面字段==配置工单（SAP工单备注不为空）==配置工单（SAP工单备注为空）")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10561(self, drivers):
        pass


    @allure.story("包装管理增加SAP工单备注显示")  # 用户故事名称
    @allure.title("GBL工单信息增加SAP工单备注栏位显示")  # 用例名称
    @allure.description("检查GBL页面字段==配置工单（SAP工单备注不为空）==检查GBL页面字段==配置工单（SAP工单备注不为空）==配置工单（SAP工单备注为空）")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10562(self, drivers):
        pass


    @allure.story("包装管理增加SAP工单备注显示")  # 用户故事名称
    @allure.title("卡通箱装箱称重工单信息增加SAP工单备注栏位显示")  # 用例名称
    @allure.description("检查卡通箱装箱称重页面字段==配置工单（SAP工单备注不为空）==配置工单（SAP工单备注为空）")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10563(self, drivers):
        pass


    @allure.story("包装管理增加SAP工单备注显示")  # 用户故事名称
    @allure.title("卡通箱称重工单信息增加SAP工单备注栏位显示")  # 用例名称
    @allure.description("检查卡通箱称重页面字段==配置工单（SAP工单备注不为空）==配置工单（SAP工单备注为空）")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10564(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1683:
    @allure.story("打印\导出箱单增加特殊物料判断")  # 用户故事名称
    @allure.title("上卡板工单国家不为印度，打印箱单时，物料描述不变")  # 用例名称
    @allure.description("新增国家非'印度'的工单》上卡板页面打印箱单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10567(self, drivers):
        pass


    @allure.story("打印\导出箱单增加特殊物料判断")  # 用户故事名称
    @allure.title("上卡板工单国家为印度，但KD特殊物料中未维护对应内容，打印箱单时，物料描述不变")  # 用例名称
    @allure.description("新增国家为'印度'的工单》上卡板页面打印箱单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10568(self, drivers):
        pass


    @allure.story("打印\导出箱单增加特殊物料判断")  # 用户故事名称
    @allure.title("上卡板工单国家为印度，且KD特殊物料中已维护对应内容，打印箱单时，物料描述为KD特殊物料中维护的内容")  # 用例名称
    @allure.description("新增国家为'印度'的工单》上卡板页面打印箱单")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10569(self, drivers):
        pass


    @allure.story("打印\导出箱单增加特殊物料判断")  # 用户故事名称
    @allure.title("出货导出工单国家不为印度，导出卡板箱单时，物料描述不变")  # 用例名称
    @allure.description("新增国家非'印度'的工单》出货导出页面导出卡板箱单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10570(self, drivers):
        pass


    @allure.story("打印\导出箱单增加特殊物料判断")  # 用户故事名称
    @allure.title("出货导出工单国家为印度，但KD特殊物料中未维护对应内容，导出卡板箱单时，物料描述不变")  # 用例名称
    @allure.description("新增国家为'印度'的工单》出货导出页面导出卡板箱单")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10571(self, drivers):
        pass


    @allure.story("打印\导出箱单增加特殊物料判断")  # 用户故事名称
    @allure.title("出货导出工单国家为印度，且KD特殊物料中已维护对应内容，导出卡板箱单时，物料描述为KD特殊物料中维护的内容")  # 用例名称
    @allure.description("新增国家为'印度'的工单》出货导出页面导出卡板箱单")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10572(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1719:
    @allure.story("组装CS站点调整TPS工具接口反写逻辑")  # 用户故事名称
    @allure.title("组装CS站点TPS工具接口参数正确，请求成功后数据正确反写")  # 用例名称
    @allure.description("参数正确请求接口==参数正确请求接口")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10574(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1872:
    @allure.story("包装管理SIMIMEI站点优化")  # 用户故事名称
    @allure.title("SIMIMEI扫描IMEI镭雕后6位后，一并发送请求")  # 用例名称
    @allure.description("配置工单，在扫描栏扫入IMEI==在镭雕后6位栏，扫入IMEI后6位")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10576(self, drivers):
        pass


    @allure.story("包装管理SIMIMEI站点优化")  # 用户故事名称
    @allure.title("SIMIMEI仅扫入镭雕后6位，不会发送请求")  # 用例名称
    @allure.description("配置工单，在扫描栏扫入IMEI==在镭雕后6位栏，扫入IMEI后6位==配置工单，在镭雕后6位栏，扫入IMEI后6位")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10577(self, drivers):
        pass


    @allure.story("包装管理SIMIMEI站点优化")  # 用户故事名称
    @allure.title("SIMIMEI扫入错误内容，过站失败")  # 用例名称
    @allure.description("配置工单，扫入错误的IMEI、镭雕后6位")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10578(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1836:
    @allure.story("MES工厂客户端/数据分析平台生产日志查询优化")  # 用户故事名称
    @allure.title("生产日志查询解绑并重新投产其他工单后，完整记录解绑工单前后的所有过站记录")  # 用例名称
    @allure.description("投产、送修、维修完成、解绑、投产其他工单，在生产日志查询中查询该SN记录")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12184(self, drivers):
        pass


    @allure.story("MES工厂客户端/数据分析平台生产日志查询优化")  # 用户故事名称
    @allure.title("生产日志查询检查记录日志各字段内容正确性")  # 用例名称
    @allure.description("在生产日志查询中查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12185(self, drivers):
        pass


    @allure.story("MES工厂客户端/数据分析平台生产日志查询优化")  # 用户故事名称
    @allure.title("生产日志查询校验PCBA工段直通率计算是否受影响")  # 用例名称
    @allure.description("检查PCBA工段直通率计算结果")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12186(self, drivers):
        pass


    @allure.story("MES工厂客户端/数据分析平台生产日志查询优化")  # 用户故事名称
    @allure.title("生产日志查询校验组装工段直通率计算是否受影响")  # 用例名称
    @allure.description("检查组装工段直通率计算结果")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12187(self, drivers):
        pass


    @allure.story("MES工厂客户端/数据分析平台生产日志查询优化")  # 用户故事名称
    @allure.title("生产日志查询校验包装工段直通率计算是否受影响")  # 用例名称
    @allure.description("检查包装工段直通率计算结果")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12188(self, drivers):
        pass


    @allure.story("MES工厂客户端/数据分析平台生产日志查询优化")  # 用户故事名称
    @allure.title("生产日志查询校验预加工工段直通率计算是否受影响")  # 用例名称
    @allure.description("检查预加工工段直通率计算结果")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12189(self, drivers):
        pass


@allure.feature("MESv5_4")  # 迭代名称
class Teststory_1624:
    @allure.story("IMEI防伪查询接口调整")  # 用户故事名称
    @allure.title("全流程报表查询后正确返回结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14852(self, drivers):
        pass


if __name__ == '__main__':
      pass
