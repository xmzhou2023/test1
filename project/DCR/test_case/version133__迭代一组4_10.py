import allure
import pytest
@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_2097:
    @allure.story("接口优化/api/rest/v1/authorization/employeeShop/dseList")  # 用户故事名称
    @allure.title("使用授权门店较多的账号，添加巡店计划，门店查询列表加载时长，3000左右的门店查询30s内")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11350(self, drivers):
        pass


@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_2096:
    @allure.story("接口优化/api/rest/v1/authorization/employeeShop/enterpriseList")  # 用户故事名称
    @allure.title("使用授权门店较多的账号，添加巡店计划，门店查询列表加载时长，3000左右的门店查询30s内")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11353(self, drivers):
        pass


@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_2086:
    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("国家价格管理数据权限调整，当前登录人员的授权销售区域对应国家品牌权限quot")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11371(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("国家价格管理数据权限调整，没有授权区域的用户查看国家价格数据没数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11372(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("国家价格管理数据权限调整，编辑更新人员授权的销售区域查看国家价格数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11373(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("国家价格管理数据权限调整，查看超管权限的国家价格管理数据权限，品牌管理员根据品牌限制数据权限")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11374(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，初始数据获取列表原有价格数据，以更新时间精确到天为开始日期，生成价格纪录")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11375(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入模板字段（Item、国家、开始日期必填）Item、DealerPrice、RetailerPrice、RecommendRetailPrice、Country、Start_Date")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11376(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入必填项校验")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11377(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入日期不符合YYYYMMDD格式，导入报错提示Dateformaterror，formatYYYYMMDD")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11378(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入数据同一国家机型存在相同开始日期，提示Countrymodelexistssamestartdate")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11379(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入数据同一国家机型存在与价格纪录相同开始日期，提示Countrymodelexistssamepricerecord")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11380(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入一组某国家机型的价格，一个开始日期，生成新的价格纪录，开始日期是导入的开始日期，结束日期是新的开始日期1")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11381(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入某国家机型的价格，多个开始日期，倒序创建价格纪录，开始日期是导入的开始日期，结束日期是新的开始日期1")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11382(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入某国家机型，两个连续的开始日期，生成一条只有一天生效的价格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11383(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入不同开始日期，国家机型价格相同的数据，生成新的价格纪录")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11384(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入日期成功，系统当前日期在新的价格纪录时间段中，更新当前国家机型价格信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11385(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入日期成功，系统当前日期不在新的价格纪录时间段中，不更新当前国家机型价格信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11386(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导入国家机型价格为空时，导入成功该时间段价格为0")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11387(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，定时任务更新当前日期国家机型价格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11388(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("批量导入修改各时间段价格，导出国家机型价格是否同步更新")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11389(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("编辑列表销售价格，当前系统日期与价格纪录的开始日期一致，该时间段的价格纪录更新为编辑成功的价格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11390(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("编辑列表销售价格，当前系统日期与价格纪录的开始日期不一致，以当前系统日期为新的开始日期，创建价格纪录")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11391(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	列表新增固定操作列，按钮价格纪录")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11392(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	点击弹窗展示价格纪录数据title机型、市场名、国家，字段生效日期、经销商价格、零售商价格、建议价格、操作（删除按钮）多语言检查")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11393(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	根据开始时间倒序排列展示，每页15条数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11394(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	价格纪录只有一条隐藏删除按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11395(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	价格纪录多条选择某一条记录点击删除，弹出二次确认弹窗提示删除价格纪录，系统将根据已有价格纪录开始日期重新生成价格纪录，请谨慎操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11396(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	确认删除价格纪录，关闭确认弹窗，现有开始日期重新生成价格纪录")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11397(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	删除当前日期在该时间段中的记录，更新列表国家机型价格信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11398(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	删除当前日期不在该时间段中的记录，不更新列表国家机型价格信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11399(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	删除结束日期为空的价格纪录，上一个价格纪录的结束日期更新1，并生成新的结束日期为空的价格纪录")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11400(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	一次删除多条价格纪录，查看列表国家机型价格更新")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11401(self, drivers):
        pass


    @allure.story("国家价格管理，数据权限与修改价格逻辑调整")  # 用户故事名称
    @allure.title("价格纪录弹窗	删除所有价格纪录剩余一条，查看删除按钮是否隐藏")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11402(self, drivers):
        pass


@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_2084:
    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("测试路径BasicDataManagementMultilingual")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11546(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11549(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("筛选项_1、【端侧】下拉选择框，多选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11551(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("筛选项_11、选项内容Web、Appios、Appandroid、System")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11553(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("筛选项_12、筛选【端侧】，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11554(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("筛选项_2、【模块】文本输入框，根据输入内容，模糊匹配业务系统对应模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11555(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("筛选项_21、筛选【模块】，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11556(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("筛选项_3、【字段】文本选择框，根据输入内容，模糊匹配业务系统对应字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11557(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("筛选项_31、筛选【字段】，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11558(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【搜索】按钮_1、点击【搜索】按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11559(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【搜索】按钮_11、单个筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11560(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【搜索】按钮_12、组合筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11561(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【重置】按钮_1、点击【重置】按钮，重置筛选项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11562(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【新增】按钮_1、点击【新增】按钮，弹出'新增字段'弹窗，可进行新增字段操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11563(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【拓展新语言】按钮_1、点击【拓展新语言】按钮，弹出'拓展新语言'弹窗，可进行拓展新语言操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11564(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【下载导入模板】按钮_1、点击【下载导入模板】按钮，可下载模板")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11565(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【新增导入】按钮_1、点击【新增导入】按钮，可进行新增导入操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11566(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【编辑导入】按钮_1、点击【编辑导入】按钮，可进行编辑导入操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11567(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【导出Excel】按钮_1、点击【导出Excel】按钮，导出当前列表筛选出的全部数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11568(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【导出资源文件】按钮_1、点击【导出资源文件】按钮，弹出'导出资源文件'弹窗，可进行导出资源文件操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11569(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【编辑】按钮_1、编辑按钮为在语种字段右侧的铅笔图标。点击编辑按钮，对应语种列为可编辑状态（出现输入框）。再点击一次编辑按钮，对应语种又变为不可编辑状态（输入框消失）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11570(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【编辑】按钮_11、编辑翻译内容选择任一字段进行编辑，鼠标点击输入框外的区域，关闭当前输入框，根据业务系统、端侧、模块、字段、语种修改原字段语种内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11571(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【编辑】按钮_12、支持批量编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11572(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("【编辑】按钮_13、编辑成功时，离开选框提示'Editsucceeded'/'编辑成功'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11573(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表按端侧、模块进行分组。按照创建时间倒序进行排序")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11574(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表中【中文】、【英语】为固定列。其余语种根据业务系统拓展语言做动态列处理（如果用户手动拓展新语言，列表会增加一列展示）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11575(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表字段_1、【字段】字段名称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11576(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表字段_2、【端侧】字段归属的端侧。Web/App/System")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11577(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表字段_3、【模块】字段归属的模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11578(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表字段_4、【中文】字段的中文翻译（固定列）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11579(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表字段_5、【英语】字段的英语翻译（固定列）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11580(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表字段_51、如果操作了拓展新语种，在【英语】后面会增加展示拓展的新语种列（动态列）。例如【法语】/【西班牙语】/【葡萄牙语】/【泰语】/【越南语】/【土耳其语】/【阿拉伯语】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11581(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表字段_6、【更新时间】字段最后一次的更新时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11582(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表字段_7、【更新人员】字段最后一次的更新人员")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11583(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表字段_8、【创建时间】字段的创建时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11584(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("列表字段_9、【创建人员】字段的创建人员")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11585(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("翻页_1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11586(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("翻页_2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11587(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("翻页_3、页面右下角totalrecords统计正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11588(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("翻页_4、页面右下角每页显示记录可设置（20，50，100，500，1000），如果选择20，则每页显示1至20条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11589(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_1、点击【取消】按钮或者【X】按钮，关闭当前弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11625(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_2、字段名称必填（红色标识）。如果未填写，点击【确定】按钮时，输入框标红并提示'Thisfieldisrequired'/'有必填项未填写'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11626(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_21、仅支持英文、数字、符号输入。填写非法内容时，点击【确定】按钮，提示仅支持英文、数字和符号现在时输入框直接限制输入格式")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11627(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_22、填入的字段在所选端侧、模块已有相同字段时，点击【确定】按钮，提示XX已在XX端侧XX模块有相同字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11628(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_3、所属端侧必填（红色标识），下拉单选，框内默认提示'Pleaseselect'。如果未填写，点击【确定】按钮时，选择框标红并提示'Thisfieldisrequired'/'有必填项未填写'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11629(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_31、选项内容Web、Appios、Appandroid、System")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11630(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_4、所属模块必填（红色标识）。如果未填写，点击【确定】按钮时，输入框标红并提示'Thisfieldisrequired'/'有必填项未填写'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11631(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_41、仅支持英文、数字、符号输入。填写非法内容时，点击【确定】按钮，提示仅支持英文、数字和符号现在时输入框直接限制输入格式")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11632(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_5、中文翻译必填（红色标识）。如果未填写，点击【确定】按钮时，输入框标红并提示'Thisfieldisrequired'/'有必填项未填写'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11633(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_51、格式不做限制，最大长度为1000，超过提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11634(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_6、英语翻译必填（红色标识）。如果未填写，点击【确定】按钮时，输入框标红并提示'Thisfieldisrequired'/'有必填项未填写'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11635(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_61、格式不做限制，最大长度为1000，超过提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11637(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'新增字段'弹窗_7、点击【确定】按钮，未存在以上异常在所选端侧的选中模块下新增字段，以英文翻译为基准，调用API接口，根据业务系统已有语种对字段进行自动翻译。列表展示新增的字段内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11639(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_1、点击【取消】按钮或者【X】按钮，关闭当前弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11644(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_2、语种必填（红色标识），下拉单选，框内默认提示'Pleaseselect'。如果未填写，点击【确定】按钮时，选择框标红并提示'Thisfieldisrequired'/'有必填项未填写'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11645(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_21、选项内容业务系统后台维护的语种，显示全称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11646(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_3、自动翻译必填（红色标识），单选。选项内容是、否，默认选中是")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11647(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_4、提示红色字体显示提示部分的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11648(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_41、提示内容1为'1、选择自动翻译系统将根据选择的语种，对业务系统全端侧、模块的所有字段进行自动翻译'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11649(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_42、提示内容2为'2、不选择自动翻译用户根据实际需求，按端侧、模块导出字段表，翻译完成后再通过编辑导入把翻译好的字段表导入系统'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11650(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_5、点击【确定】按钮，校验所选语种在业务系统是否已存在，如果已存在，提示XX语种已存在")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11651(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_6、点击【确定】按钮，未存在以上异常，判断自动翻译选项内容为")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11652(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_61、否业务系统全端侧、模块的所有字段，增加新增语种。新增语种内容为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11653(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_62、是业务系统全端侧、模块的所有字段，增加新增语种。新增语种以英文为参照，调用API接口完成自动翻译并进行保存，并展示在列表")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11654(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_7、拓展新语言成功后自动关闭弹窗，列表增加新语言列，自动刷新并显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11655(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_8、导入模板自动拓展新语言列")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11656(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("下载导入模板_1、下载模板的文件名为quotTranslationTemplatequot")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11657(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("下载导入模板_2、中文、英文为固定列。其余语种根据业务系统拓展语言做动态列处理")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11658(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("下载导入模板_3、报表字段从左到右依次为【字段】、【端侧】、【模块】、【中文】、【英语】。标红色（必填）在用户刚开始使用多语言组件时还没操作拓展新语言，下载的导入模板是只有这几个字段的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11659(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("下载导入模板_31、【端侧】是下拉单选的，选项内容Appandroid、Appios、Web、System")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11660(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("下载导入模板_32、如果操作了拓展新语种，在【英语】后面会增加展示拓展的新语种列（动态列）。例如【法语】/【西班牙语】/【葡萄牙语】/【泰语】/【越南语】/【土耳其语】/【阿拉伯语】等。标紫色（非必填）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11661(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入_1、上载的字段和模板中字段一致，内容正确且符合格式要求，即可成功上载")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11668(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入_2、上载成功后列表展示导入的数据，且数据内容/数据条数与导入的内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11669(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入_3、新增导入的上传记录会写入【导入记录】页面DCR系统的ImportRecord页面（MKT列表）/BatchImport页面（MKT列表）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11670(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入_4、新增导入成功后，在所选端侧的选中模块下新增字段，以英文翻译为基准，调用API接口，根据业务系统已有语种对字段进行自动翻译。列表展示新增的字段内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11671(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入_5、新增导入时，Appandroid若模块下有相同字段，保存相同字段不同的内容值（根据字段、端侧、模块，更新语种内容）首次导入才支持，再次新增导入时提示'XX已在XX端侧XX模块有相同字段'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11672(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_1、【字段】为必填字段在所选端侧、模块是唯一的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11673(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_11、导入字段为空时，失败原因未填写字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11674(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_12、导入字段在所选端侧、模块已有相同字段时，失败原因XX已在XX端侧XX模块有相同字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11675(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_13、导入字段仅支持英文、数字、符号输入。填写非法内容时，提示仅支持英文、数字和符号")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11676(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_14、若端侧为Appandroid，字段在导入文件有相同字段，但服务器没有相同字段，则视为校验通过")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11677(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_2、【端侧】为必填字段。下拉单选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11678(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_21、选项内容Web、Appios、Appandroid、System")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11679(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_22、导入端侧为空或非法内容时，失败原因端侧只能选择Web、Appios、Appandroid、System其中一项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11680(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_3、【模块】为必填字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11681(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_31、导入模块为空时，失败原因未填写模块名称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11682(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_32、导入模块仅支持英文、数字、符号输入。填写非法内容时，提示仅支持英文、数字和符号")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11683(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_4、【中文】为必填字段（固定列）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11684(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_41、导入字段为空时，失败原因未填写中文")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11685(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_42、格式不做限制，最大长度为1000，超过提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11686(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_5、【英语】为必填字段（固定列）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11687(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_51、导入字段为空时，失败原因未填写英语")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11688(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_52、格式不做限制，最大长度为1000，超过提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11689(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_53、如果操作了拓展新语种，在【英语】后面会增加展示拓展的新语种列（动态列）。例如【法语】/【西班牙语】/【葡萄牙语】/【泰语】/【越南语】/【土耳其语】/【阿拉伯语】等。为非必填字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11690(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("新增导入校验_6、新增导入时，导入excel的语言列与业务系统多语言列表语言列不一致，导入失败，不出现错误提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11691(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入_1、编辑导入成功后列表展示更新的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11692(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入_2、编辑导入的上传记录会写入【导入记录】页面DCR系统的ImportRecord页面（MKT列表）/BatchImport页面（MKT列表）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11693(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入_3、编辑导入成功后，列表展示编辑的字段内容（这边是不会触发自动翻译的，编辑的内容直接覆盖原来的数据内容）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11694(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入_4、编辑导入时，Web、Appios、System根据字段、端侧、模块，更新语种内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11695(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入_5、编辑导入时，Appandroid若模块下有相同字段，保存相同字段不同的内容值（根据字段、端侧、模块，更新语种内容）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11696(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入_6、编辑导入时，Appandroid导出来有多个词条的值时，假设原来这个词条有两个，现在词条删除一个只保留一个，导入进去的话它就只剩下一个了")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11697(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_1、【字段】为必填字段在所选端侧、模块是唯一的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11698(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_11、导入字段为空时，失败原因未填写字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11699(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_12、导入字段在所选端侧、模块查询结果为空时，失败原因XX端的XX模块没有当前字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11700(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_13、导入字段仅支持英文、数字、符号输入。填写非法内容时，提示仅支持英文、数字和符号")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11701(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_2、【端侧】为必填字段。下拉单选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11702(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_21、选项内容Web、Appios、Appandroid、System")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11703(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_22、导入端侧为空或非法内容时，失败原因端侧只能选择Web、Appios、Appandroid、System其中一项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11704(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_3、【模块】为必填字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11705(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_31、导入模块为空时，失败原因未填写模块名称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11706(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_32、导入模块仅支持英文、数字、符号输入。填写非法内容时，提示仅支持英文、数字和符号")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11707(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_4、【中文】为必填字段（固定列）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11708(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_41、导入字段为空时，失败原因未填写中文")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11709(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_42、格式不做限制，最大长度为1000，超过提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11710(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_5、【英语】为必填字段（固定列）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11711(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_51、导入字段为空时，失败原因未填写英语")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11712(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_52、格式不做限制，最大长度为1000，超过提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11713(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_53、如果操作了拓展新语种，在【英语】后面会增加展示拓展的新语种列（动态列）。例如【法语】/【西班牙语】/【葡萄牙语】/【泰语】/【越南语】/【土耳其语】/【阿拉伯语】等。为非必填字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11714(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("编辑导入校验_6、编辑导入时，导入excel的语言列与业务系统多语言列表语言列不一致，导入失败，不出现错误提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11715(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("点击导出按钮，根据查询结果将数据导出到本地，导出格式为xlsx，导出内容字段、端侧、翻译语种")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11716(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_1、导出文件名为菜单名流水号")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11717(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_2、导出的报表字段名、字段顺序、数据内容和列表一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11718(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_3、导出excel文件的样式行宽固定（20，excel中的列宽单位）。未超出则自动调整列宽，超出收缩。居左对齐。表头加粗。单元格格式常规")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11719(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_4、导出数量限制单个文档最多100w")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11720(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_5、筛选后导出的报表数据和筛选的数据保持一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11721(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_51、单个筛选，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11722(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_511、筛选【端侧】，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11723(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_512、筛选【模块】，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11724(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_513、筛选【字段】，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11725(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_52、组合筛选，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11726(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("导出Excel_6、导出的记录会写入【导出记录】页面DCR系统的ExportRecord页面（MKT列表）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11727(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'导出资源文件'弹窗_1、点击【取消】按钮或者【X】按钮，关闭当前弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11728(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'导出资源文件'弹窗_2、资源文件类型必填（红色标识），下拉单选。如果未选择，点击【确定】按钮时，选择框标红并提示'Thisfieldisrequired'/'有必填项未填写'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11729(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'导出资源文件'弹窗_21、选项内容WEBJSON（对应端侧Web）、iOSProperties（对应端侧Appios）、后台Properties（对应端侧System）、AndroidXML（对应端侧Appandroid）、AndroidJSON（对应端侧Appandroid）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11730(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'导出资源文件'弹窗_3、模块必填（红色标识）。如果未填写，点击【确定】按钮时，输入框标红并提示'Thisfieldisrequired'/'有必填项未填写'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11731(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'导出资源文件'弹窗_31、点击【确定】按钮时，填写模块名称不包含在所选模块对应端侧，提示XX端没有XX模块，请检查确认")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11732(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'导出资源文件'弹窗_4、语种必填（红色标识），下拉单选，框内默认提示'Pleaseselect'。如果未填写，点击【确定】按钮时，选择框标红并提示'Thisfieldisrequired'/'有必填项未填写'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11733(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'导出资源文件'弹窗_5、点击【确定】按钮，未存在以上异常，执行导出操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11734(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'导出资源文件'弹窗_6、生成AndroidXML、AndroidJSON时，需兼容以下场景")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11735(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'导出资源文件'弹窗_61、一个字段对应多个内容值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11736(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'导出资源文件'弹窗_62、字段内容值为对象")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11737(self, drivers):
        pass


    @allure.story("多国语言组件平台化P3导出资源文件")  # 用户故事名称
    @allure.title("'拓展新语言'弹窗_9、如果在列表完全没有数据的情况下操作扩展新语言，点击【确定】按钮会提示'Noentrieshavebeenaddedtothisproject,pleaseaddthemfirst'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11740(self, drivers):
        pass


@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_1888:
    @allure.story("人员管理列表的门店数量显示优化")  # 用户故事名称
    @allure.title("根据当前登录人品牌过滤门店数量展示，人员关联多品牌门店，登录人查看人员管理")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12067(self, drivers):
        pass


    @allure.story("人员管理列表的门店数量显示优化")  # 用户故事名称
    @allure.title("根据当前登录人品牌过滤门店数量展示，人员关联多品牌门店，门店数量展示根据登录人授权品牌过滤")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12068(self, drivers):
        pass


    @allure.story("人员管理列表的门店数量显示优化")  # 用户故事名称
    @allure.title("根据当前登录人品牌过滤门店数量展示，人员关联多品牌门店，导出数据也同步根据品牌过滤")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12069(self, drivers):
        pass


@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_2119:
    @allure.story("串码查询支持非DCR的IMEI")  # 用户故事名称
    @allure.title("1、查询IMEI时，如果IMEI没在DCR的IMEIQUERY表里，则查询大数据的IMEI信息表；")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12129(self, drivers):
        pass


    @allure.story("串码查询支持非DCR的IMEI")  # 用户故事名称
    @allure.title("11、imei查询的信息包括IMEI、IMEIList、Brand、Product、Model、DeliveryCountry、FactoryDeliveryDate、ActivatedOrNot、ActivatedCountry、ActivatedDate")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12130(self, drivers):
        pass


    @allure.story("串码查询支持非DCR的IMEI")  # 用户故事名称
    @allure.title("12、IMEI没在DCR的IMEIQUERY表里，则查询大数据的IMEI信息表，查询后数据导出也一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12131(self, drivers):
        pass


    @allure.story("串码查询支持非DCR的IMEI")  # 用户故事名称
    @allure.title("2、显示IMEI的状态字段；（以前有这个字段，应该只需要前端显示出来）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12132(self, drivers):
        pass


    @allure.story("串码查询支持非DCR的IMEI")  # 用户故事名称
    @allure.title("21、导出报表也显示IMEI的状态字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12133(self, drivers):
        pass


@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_2099:
    @allure.story("印度门店管理表单添加国包字段")  # 用户故事名称
    @allure.title("ShopManagement（India）添加字段	添加位置RetailCustomerID之前")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12211(self, drivers):
        pass


    @allure.story("印度门店管理表单添加国包字段")  # 用户故事名称
    @allure.title("ShopManagement（India）添加字段	名称DistributeCustomerID、DistributeCustomerName")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12212(self, drivers):
        pass


    @allure.story("印度门店管理表单添加国包字段")  # 用户故事名称
    @allure.title("ShopManagement（India）添加字段	取值直接取门店关联的零售商上游客户")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12213(self, drivers):
        pass


    @allure.story("印度门店管理表单添加国包字段")  # 用户故事名称
    @allure.title("ShopManagement（India）添加字段	取值为空时，该字段值为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12214(self, drivers):
        pass


    @allure.story("印度门店管理表单添加国包字段")  # 用户故事名称
    @allure.title("ShopManagement（India）添加字段	校验用户所属代理是否为国包，非国包取值则为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12215(self, drivers):
        pass


    @allure.story("印度门店管理表单添加国包字段")  # 用户故事名称
    @allure.title("ShopManagement（India）添加字段	查询门店被授权的国包代理有多个，则取值也为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12216(self, drivers):
        pass


    @allure.story("印度门店管理表单添加国包字段")  # 用户故事名称
    @allure.title("ShopManagement（India）添加字段	导出文件同步新增字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12217(self, drivers):
        pass


@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_1140:
    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("门店，有效销量（销量上报且激活了）销量返利，重选时间后，返利计算正确，条件选择总达成时ValidSalesTotalQuantityUnitRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12279(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("1、门店，有效销量（销量上报且激活了）销量返利，条件选择总达成时，可以选择过去的单月份，不能选中连续2个月的跨月时段。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12280(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("2、政策可以重选时间重选时间的机型可以相同，即2个不同时段，相同机型执行不同返利单价。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12281(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("21、预览页，同步显示所有新增项。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12282(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("4、返利政策组合ShopSchemeWiseSchemeTypeCaculateWise条件（TotalAch）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12283(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("41、ShopActivationTotalQuantityTotalRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12284(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("42、ShopActivationTotalQuantityUnitRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12285(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("43、ShopActivationItemQuantityUnitRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12286(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("44、ShopActivationItemQuantityTotalRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12287(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("45、ShopValidSalesItemQuantityUnitRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12288(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("46、ShopValidSalesItemQuantityTotalRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12289(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("47、ShopValidSalesItemQuantityRebateTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12290(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("48、ShopValidSalesTotalQuantityTotalRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12291(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("49、ShopValidSalesTotalQuantityRebateTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12292(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("410、ShopValidSalesTotalQuantityUnitRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12293(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("411、ShopSalesItemQuantityUnitRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12294(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("412、ShopSalesItemQuantityTotalRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12295(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("413、ShopSalesItemQuantityRebateTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12296(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("414、ShopSalesTotalQuantityTotalRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12297(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("415、ShopSalesTotalQuantityRebateTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12298(self, drivers):
        pass


    @allure.story("门店销量返利，增加条件可重选时间，政策也能重选时间")  # 用户故事名称
    @allure.title("416、ShopSalesTotalQuantityUnitRebateAmountTotalAch")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12299(self, drivers):
        pass


@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_2094:
    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试路径SystemManagementFunctionSetting")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12328(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_1、新增SpecialPriceAchievement配置项。value设置为1时，发布范围的国包客户计算渠道采购达成时，取经销商价格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12329(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_11、这个只作用于国包客户")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12330(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试路径RebateAchievementCustomerAchievement")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12359(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_0、新增20个字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12360(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_1、PurchaseAmountTarget（采购总金额目标）导入采购总金额目标（位置在PurchaseAch后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12361(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_11、点击后为可编辑状态。点击输入框外的区域，保存编辑内容并重新计算对应的达成值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12362(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_12、输入框支持正数，整数位最大10位，小数位最大2位这边是做成那种直接输入框就限制格式的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12363(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_2、TotalPurchaseAmount（采购总金额）客户品牌目标月份全机型结果集中，所有机型的机型目标月份采购金额之和（客户品牌目标月份全机型所有采购数量不等于0的机型）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12364(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_21、全机型以客户ID、当前记录品牌、目标月份（精确到天）作为查询条件，查询CustomerPSI页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12365(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_22、机型目标月份采购金额以客户所在国家、当前机型作为查询条件，查询机型在客户所在国家且价格记录时间范围包含在目标月份的所有价格记录（CountryPriceManagement）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12366(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_221、查询结果为空，机型在当前月份取0进行计算")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12367(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_222、价格记录生效日期在当月内可能存在分段情况，则在做统计时需要做特殊处理。例A机型的价格记录在10月份的生效日期有10.1~10.10、10.11~10.20、10.21~10.31，计算10月达成时，采购总金额=10.01~10.10的采购数量价格10.11~10.20的采购数量价格10.21~10.31的采购数量价格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12368(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_223、机型单个价格记录采购金额生效日期时间段内采购数量采购金额生效日期时间段内退货金额之和")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12369(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_2231、价格记录时间段采购数量以客户ID、价格记录生效日期、当前机型为条件，查询CustomerPSI获取客户机型在该时间段内的采购数量")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12370(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_2232、采购金额根据客户类型（卖家类型），获取机型价格记录对应金额")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12371(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_22321、国包判断客户国家品牌关联SpecialAmountAchievementvalue为1的配置项。如果关联了，取经销商价格（DP）。如果未关联，取SAP价格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12372(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_22322、二代经销商价格（DP）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12373(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_22323、零售商零售商价格（RP）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12374(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_2233、生效日期时间段内退货金额之和退货IMEI结果集中所有IMEI退货金额之和")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12375(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_22331、退货IMEI结果集以客户ID（作为买家ID）、价格生效日期、当前机型、退货状态等于已审核为条件，查询数据表dwd_chal_dcr_return_imei_d")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12376(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_22332、单个IMEI退货金额退货IMEI结果集中，IMEI关联出库单取得出库日期，以客户所在国家、IMEI机型、出库日期取得价格记录，根据客户类型获取退货金额（客户类型及价格关系与采购金额一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12377(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_224、机型目标月份采购金额=机型单个价格记录采购金额之和")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12378(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_23、印度环境增加中英文提示语印度暂不支持金额统计（Indiadoesnotsupportmonetarystatisticsatthistime）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12379(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_3、PurchaseAmountAch（采购总金额达成）采购总金额/采购总金额目标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12380(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_31、若分母为空，则显示为空值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12381(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_4、SalesAmountTarget（销售总金额目标）导入销售总金额目标（位置在SalesAch后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12382(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_41、点击后为可编辑状态。点击输入框外的区域，保存编辑内容并重新计算对应的达成值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12383(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_42、输入框支持正数，整数位最大10位，小数位最大2位这边是做成那种直接输入框就限制格式的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12384(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_5、TotalSalesAmount（销售总金额）客户品牌目标月份全机型结果集中，所有机型的机型目标月份销售金额之和（客户品牌目标月份全机型所有销售数量不等于0的机型）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12385(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_51、全机型以客户ID、当前记录品牌、目标月份（精确到天）作为查询条件，查询CustomerSalesReport页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12386(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_52、机型目标月份销售金额以客户所在国家、当前机型作为查询条件，查询机型在客户所在国家且价格记录时间范围包含在目标月份的所有价格记录（CountryPriceManagement）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12387(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_521、查询结果为空，机型在当前月份取0进行计算")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12388(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_522、价格记录生效日期在当月内可能存在分段情况，则在做统计时需要做特殊处理。例A机型的价格记录在10月份的生效日期有10.1~10.10、10.11~10.20、10.21~10.31，计算10月达成时，销售总金额=10.01~10.10的销售数量价格10.11~10.20的销售数量价格10.21~10.31的销售数量价格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12389(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_523、机型单个价格记录销售金额生效日期时间段内经销商销售金额零售商销售金额生效日期时间段内退货金额之和")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12390(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_5231、价格记录时间段销售数量以客户ID、价格记录生效日期、当前机型、买家类型为条件，查询CustomerSalesReport获取客户机型在该时间段内的已售IMEI")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12391(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_5232、销售金额根据IMEI的买家类型，取对应的价格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12392(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_52321、二代经销商价格（DP）经销商销售金额经销商销售数量DP")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12393(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_52322、零售商零售商价格（RP）零售商销售金额零售商销售数量RP")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12394(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_5233、生效日期时间段内退货金额之和退货IMEI结果集中所有IMEI退货金额之和")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12395(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_52331、退货IMEI结果集以客户ID（作为卖家ID）、价格生效日期、当前机型、退货状态等于已审核为条件，查询数据表dwd_chal_dcr_return_imei_d")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12396(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_52332、单个IMEI退货金额退货IMEI结果集中，IMEI关联出库单取得出库日期，以客户所在国家、IMEI机型、出库日期取得价格记录，根据买家客户类型取退货金额")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12397(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_524、机型目标月份销售金额=机型单个价格记录销售金额之和")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12398(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_53、印度环境增加中英文提示语印度暂不支持金额统计（Indiadoesnotsupportmonetarystatisticsatthistime）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12399(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_6、SalesAmountAch（销售总金额达成）销售总金额/销售总金额目标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12400(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_61、若分母为空，则显示为空值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12401(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_7、SPPurchaseAmountTarget（SP采购金额目标）导入SP采购金额目标（位置在SPPurchaseAch后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12402(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_71、点击后为可编辑状态。点击输入框外的区域，保存编辑内容并重新计算对应的达成值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12403(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_72、输入框支持正数，整数位最大10位，小数位最大2位这边是做成那种直接输入框就限制格式的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12404(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_8、SPPurchaseAmount（SP采购金额）客户品牌目标月份SP结果集中，所有机型的机型目标月份采购金额之和（客户品牌目标月份SP所有采购数量不等于0且类型为SP的所有机型）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12405(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_81、印度环境增加中英文提示语印度暂不支持金额统计（Indiadoesnotsupportmonetarystatisticsatthistime）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12406(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_9、SPPurchaseAmountAch（SP采购金额达成）SP采购金额/SP采购金额目标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12407(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_91、若分母为空，则显示为空值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12408(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_10、SPSalesAmountTarget（SP销售金额目标）导入SP销售金额目标（位置在SPSalesAch后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12409(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_101、点击后为可编辑状态。点击输入框外的区域，保存编辑内容并重新计算对应的达成值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12410(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_102、输入框支持正数，整数位最大10位，小数位最大2位这边是做成那种直接输入框就限制格式的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12411(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_11、SPSalesAmount（SP销售金额）客户品牌目标月份SP结果集中，所有机型的机型目标月份销售金额之和（客户品牌目标月份SP所有销售数量不等于0且类型为SP的所有机型）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12412(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_111、印度环境增加中英文提示语印度暂不支持金额统计（Indiadoesnotsupportmonetarystatisticsatthistime）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12413(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_12、SPSalesAmountAch（SP销售金额达成）SP销售金额/SP销售金额目标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12414(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_121、若分母为空，则显示为空值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12415(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_13、FPPurchaseTarget（FP采购目标）导入FP采购目标（位置在SPSalesAmountAch后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12416(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_131、点击后为可编辑状态。点击输入框外的区域，保存编辑内容并重新计算对应的达成值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12417(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_132、输入框支持正数，整数位最大10位，小数位最大2位这边是做成那种直接输入框就限制格式的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12418(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_14、FPPurchaseAmountTarget（FP采购金额目标）导入FP采购金额目标（位置在FPPurchaseAch后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12419(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_141、点击后为可编辑状态。点击输入框外的区域，保存编辑内容并重新计算对应的达成值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12420(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_142、输入框支持正数，整数位最大10位，小数位最大2位这边是做成那种直接输入框就限制格式的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12421(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_15、FPPurchaseAmount（FP采购金额）客户品牌目标月份FP结果集中，所有机型的机型目标月份采购金额之和（客户品牌目标月份FP所有采购数量不等于0且类型为FP的所有机型）（位置在FPPurchaseAch后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12422(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_151、印度环境增加中英文提示语印度暂不支持金额统计（Indiadoesnotsupportmonetarystatisticsatthistime）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12423(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_16、FPPurchaseAmountAch（FP采购金额达成）FP采购金额/FP采购金额目标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12424(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_161、FP采购金额目标（FPPurchaseAmountTarget）=采购总金额目标SP采购金额目标。该目标不在列表显示，只用于达成计算。若计算结果小于等于0，则保存为空值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12425(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_162、若分母为空，则显示为空值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12426(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_17、FPSalesTarget（FP销售目标）导入FP销售目标（位置在FPPurchaseAmountAch后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12430(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_171、点击后为可编辑状态。点击输入框外的区域，保存编辑内容并重新计算对应的达成值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12431(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_172、输入框支持正数，整数位最大10位，小数位最大2位这边是做成那种直接输入框就限制格式的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12432(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_18、FPSalesAmountTarget（FP销售金额目标）导入FP销售金额目标（位置在FPSalesAch后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12433(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_181、点击后为可编辑状态。点击输入框外的区域，保存编辑内容并重新计算对应的达成值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12434(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_182、输入框支持正数，整数位最大10位，小数位最大2位这边是做成那种直接输入框就限制格式的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12435(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_19、FPSalesAmount（FP销售金额）客户品牌目标月份FP结果集中，所有机型的机型目标月份销售金额之和（客户品牌目标月份FP所有销售数量不等于0且类型为FP的所有机型）（位置在FPSalesAch后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12436(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_191、印度环境增加中英文提示语印度暂不支持金额统计（Indiadoesnotsupportmonetarystatisticsatthistime）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12437(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_20、FPSalesAmountAch（FP销售金额达成）FP销售金额/FP销售金额目标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12438(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_201、FP销售金额目标（FPSalesAmountTarget）=销售总金额目标SP销售金额目标。该目标不在列表显示，只用于达成计算。若计算结果小于等于0，则保存为空值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12439(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_列表_202、若分母为空，则显示为空值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12440(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导出、导出字段字段显示与取值与列表字段一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12443(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_0、点击导入按钮，打开导入窗口，下载导入模板。新增PurchaseAmountTarget、SalesAmountTarget、SPPurchaseAmountTarget、SPSalesAmountTarget、FPPurchaseTarget、SPPurchaseAmountTarget、FPSalesTarget、SPSalesAmountTarget，新增校验逻辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12444(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_1、PurchaseAmountTarget数据体现在PurchaseAmountTarget列（位置在PurchaseTarget后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12445(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_11、非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12446(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_32、采购总金额目标仅支持正数，整数位最大10位，小数位最大2位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12447(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_321、新增字段输入非正数，提示'PurchaseAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12448(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_322、新增字段输入的小数点超过两位，提示'PurchaseAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12449(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_323、新增字段输入的整数位超过10位，提示'PurchaseAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12450(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_2、SalesAmountTarget数据体现在SPPurchaseAmountTarget列（位置在SalesTarget后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12451(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_21、非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12452(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_22、销售总金额目标仅支持正数，整数位最大10位，小数位最大2位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12453(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_221、新增字段输入非正数，提示'SalesAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12454(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_222、新增字段输入的小数点超过两位，提示'SalesAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12455(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_223、新增字段输入的整数位超过10位，提示'SalesAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12456(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_3、SPPurchaseAmountTarget数据体现在SPPurchaseAmountTarget列（位置在SPPurchaseTarget后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12457(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_31、非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12458(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_32、SP采购金额目标仅支持正数，整数位最大10位，小数位最大2位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12459(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_321、新增字段输入非正数，提示'SPPurchaseAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12460(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_322、新增字段输入的小数点超过两位，提示'SPPurchaseAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12461(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_323、新增字段输入的整数位超过10位，提示'SPPurchaseAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12462(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_4、SPSalesAmountTarget数据体现在SPSalesAmountTarget列（位置在SPSalesTarget后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12463(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_41、非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12464(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_42、SP销售金额目标仅支持正数，整数位最大10位，小数位最大2位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12465(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_421、新增字段输入非正数，提示'SPSalesAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12466(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_422、新增字段输入的小数点超过两位，提示'SPSalesAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12467(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_423、新增字段输入的整数位超过10位，提示'SPSalesAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12468(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_5、FPPurchaseTarget数据体现在FPPurchaseTarget列（位置在SPSalesAmountTarget后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12469(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_51、非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12470(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_52、FP采购目标仅支持正整数，整数位最大10位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12471(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_521、新增字段输入非正数，提示'FPPurchaseTargetOnlypositiveintegersaresupported,andthemaximumnumberofintegerbitsis10'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12472(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_522、新增字段输入小数点，提示'FPPurchaseTargetOnlypositiveintegersaresupported,andthemaximumnumberofintegerbitsis10'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12473(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_523、新增字段输入的整数位超过10位，提示'FPPurchaseTargetOnlypositiveintegersaresupported,andthemaximumnumberofintegerbitsis10'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12474(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_6、FPPurchaseAmountTarget数据体现在FPPurchaseAmountTarget列（位置在FPPurchaseTarget后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12475(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_61、非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12476(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_62、FP采购金额目标仅支持正数，整数位最大10位，小数位最大2位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12477(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_621、新增字段输入非正数，提示'FPPurchaseAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12478(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_622、新增字段输入的小数点超过两位，提示'FPPurchaseAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12479(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_623、新增字段输入的整数位超过10位，提示'FPPurchaseAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12480(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_7、FPSalesTarget数据体现在FPSalesTarget列（位置在FPPurchasePriceTarget后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12481(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_71、非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12482(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_72、FP销售目标仅支持正整数，整数位最大10位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12483(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_721、新增字段输入非正数，提示'FPSalesTargetOnlypositiveintegersaresupported,andthemaximumnumberofintegerbitsis10'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12484(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_722、新增字段输入小数点，提示'FPSalesTargetOnlypositiveintegersaresupported,andthemaximumnumberofintegerbitsis10'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12485(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_723、新增字段输入的整数位超过10位，提示'FPSalesTargetOnlypositiveintegersaresupported,andthemaximumnumberofintegerbitsis10'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12486(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_8、FPSalesAmountTarget数据体现在FPSalesAmountTarget列（位置在FPSalesTarget后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12487(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_81、非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12488(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_82、FP销售金额目标仅支持正数，整数位最大10位，小数位最大2位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12489(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_821、新增字段输入非正数，提示'FPSalesAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12490(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_822、新增字段输入的小数点超过两位，提示'FPSalesAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12491(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("测试点_导入_823、新增字段输入的整数位超过10位，提示'FPSalesAmountTargetOnlypositivenumbersaresupported.Themaximumnumberofintegerdigitsis10,andthemaximumnumberofdecimaldigitsis2'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12492(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("回归_1、TotalPurchase按照原有逻辑计算")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12499(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("回归_2、TotalSales、按照原有逻辑计算")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12500(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("回归_3、SPPurchase按照原有逻辑计算")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12501(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("回归_4、SPSales按照原有逻辑计算")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12502(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("回归_5、FPPurchase按照原有逻辑计算")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12503(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("回归_6、FPSales按照原有逻辑计算")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12504(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("回归_7、APP按照原有逻辑计算")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12505(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_1、设置客户品牌的FP采购/销售目标、达成值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12506(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_11、FP采购目标采购总目标SP采购目标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12507(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_12、FP销售目标销售总目标SP销售目标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12508(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_13、根据FP采购/销售目标重新计算达成值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12509(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_2、以下情况，对应记录的FP采购/销售目标保存为空且不计算达成")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12510(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_21、采购总目标、SP采购目标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12511(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_211、其中一项为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12512(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_212、采购总目标SP采购目标结果为负")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12513(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_22、销售总目标、SP销售目标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12514(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_221、其中一项为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12515(self, drivers):
        pass


    @allure.story("客户达成，新增销售额达成计算")  # 用户故事名称
    @allure.title("上线后历史数据需进行处理_222、销售总目标SP销售目标结果为负")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12516(self, drivers):
        pass


@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_1887:
    @allure.story("销售区域自动授权的创建人改为system")  # 用户故事名称
    @allure.title("授权销售区域的人员，区域内有新增门店、客户、仓库，自动授权该区域新增的门店、客户、仓库，授权的Operator是System")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12357(self, drivers):
        pass


    @allure.story("销售区域自动授权的创建人改为system")  # 用户故事名称
    @allure.title("授权销售区域的人员，区域内有新增门店、客户、仓库，导出授权记录操作者也是system")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12358(self, drivers):
        pass


@allure.feature("迭代一组4_10")  # 迭代名称
class Teststory_1141:
    @allure.story("客户采购返利，多等级增加时间重选")  # 用户故事名称
    @allure.title("1、返利对象customer，选择SetSchemeTypeByGrade，选择totalquantity，Unitrebateamount，条件选择TotalQuantity（分等级设置条件），增加起止时间列，对所选机型所选时间内的IMEI进行返利计算")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16389(self, drivers):
        pass


    @allure.story("客户采购返利，多等级增加时间重选")  # 用户故事名称
    @allure.title("2、多等级，增加条件时，条件的设置也要是多等级方式")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16390(self, drivers):
        pass


    @allure.story("客户采购返利，多等级增加时间重选")  # 用户故事名称
    @allure.title("3、条件要增加起止时间选择，可以超过第一页的时间范围。比如，9月1日9月30日的返利，可以设置7月1日7月31日和8月1日8月31日的条件时间。（不能跨月）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16391(self, drivers):
        pass


    @allure.story("客户采购返利，多等级增加时间重选")  # 用户故事名称
    @allure.title("4、操作列，增加ADD按钮，可以叠加机型。之前隐藏了。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16392(self, drivers):
        pass


    @allure.story("客户采购返利，多等级增加时间重选")  # 用户故事名称
    @allure.title("5、客户多等级的列表顺序为在统一按AZ首字母排序")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16393(self, drivers):
        pass


if __name__ == '__main__':
      pass
