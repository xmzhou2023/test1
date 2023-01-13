import allure
import pytest
@allure.feature("DRP管理_28")  # 迭代名称
class Teststory_11:
    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("_DRP管理_一级菜单下新增_DRP2国家销售版DRP2NationalSalesVer._二级菜单，菜单权限控制准确")  # 用例名称
    @allure.description("步骤1:登录DRP进入DRP管理菜单导航，查看下级菜单;步骤2:统一用户中心去除用户对应菜单权限，返回DRP查看DRP管理下级菜单;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_102(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("销售版展示数据与用户数据权限保持一致")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版，查看销售版主页面展示数据;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_103(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版主页面页面信息完整，排版布局美观")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:主页面信息检查;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_104(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面查询条件下拉项与用户权限保持一致")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:查询条件提报周期品牌管理维度下拉框检查;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_105(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面各项查询，单项联合查询成功，查询结果正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:切换提报周期查询;步骤3:选择品牌进行查询;步骤4:选择管理维度进行查询;步骤5:联合查询;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_106(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面查询后进行重置，重置成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择查询条件查询后，点击重置;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_107(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面下载导入模板成功，文件格式内容正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:点击导入下载导入文件;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_108(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面导入管理维度和品牌不匹配，导入失败")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:点击导入，选择管理维度和品牌不匹配的文件进行导入;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_109(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面导入国家不在管理维度内，导入失败")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:点击导入，选择的国家不在管理维度内文件进行导入;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_110(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面导入机型市场名品牌不匹配，导入失败")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:点击导入，选择机型市场名品牌不匹配的文件进行导入;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_111(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面导入数据缺少关键字段数据，导入失败")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:点击导入，选择数据缺少关键字段数据的文件进行导入;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_112(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面导入文件内容合规的数据文件的，导入成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:点绕导入，选择文件内容合规的数据文件进行导入;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_113(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，不同数据状态的数据，按钮显隐不同")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:待发布状态数据，按钮检查;步骤3:已发布状态数据，按钮检查;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_114(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面撤回按钮单独受权限控制显隐")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:设置用户撤回按钮权限，查看已发布状态数据;步骤3:取消用户撤回按钮权限，查看已发布状态数据;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_115(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择单条待发布状态进行发布，发布成功，各状态流转正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择一条待发布状态数据，点击发布;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_116(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择多条待发布状态进行发布，发布成功，各状态流转正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择多条待发布状态数据，点击发布;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_117(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择多条含有已发布状态数据进行发布，发布失败")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择多条含有已发布状态数据进行发布;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_118(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择多条待发布数据确认删除，删除成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择多条待发布状态数据进行删除;步骤3:确认删除;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_119(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择多条含有非待发布数据确认删除，删除失败")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择多条含有非待发布数据点击批量删除;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_120(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择多条待发布数据点击删除后取消，取消成功，数据无变更")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择多条待发布数据点击删除后取消;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_121(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面确认撤回数据成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择已发布数据点击撤回;步骤3:确认撤回;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_122(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面取消撤回数据成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择已发布数据点击撤回;步骤3:取消撤回;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_123(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面撤回数据后，重新发布成功，数据记录正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择已发布数据点击撤回;步骤3:确认撤回;步骤4:再次确认发布该数据;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_124(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择数据批量导出成功，数据内容正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择多条数据，点击批量导出;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_125(self, drivers):
        pass


@allure.feature("DRP管理_28")  # 迭代名称
class Teststory_7:
    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情页面中头部信息完整")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:编辑详情title页面检查;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_126(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面精简模式和标准模式信息表单信息完整")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:明细页面标准和精简模式表单检查;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_127(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面，各项查询条件单项和联合查询成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:明细页面单项查询;步骤4:联合查询;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_128(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面，导出数据成功，导出文件数据内容正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:明细页面点击导出;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_129(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面，确认删除机型成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:明细页面选择机型进行批量单条删除;步骤4:确认删除;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_130(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面，取消删除机型成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:明细页面选择机型进行批量单条删除;步骤4:取消删除;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_131(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面，在线编辑修改数据成功，保存成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:明细页面选择机型点击编辑;步骤4:修改数据点击保存;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_132(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情总量页面，精简模式和标准模式信息表单完整")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:总量页面精简模式总量模式检查;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_133(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情总量页面，各项查询条件单项和联合查询成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:总量页面单项查询;步骤4:联合查询;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_134(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情总量页面，导出数据成功，导出文件数据内容正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:总量页面点击导出;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_135(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情页面，发布成功，数据变更正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:点击发布;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_136(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情页面，返回成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击编辑;步骤3:点击返回;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_137(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，查看详情页面，各页面元素与编辑页面保持一致")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择待发布数据点击查看;步骤3:查看详情明细页面检查;步骤4:查看详情总量页面检查;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_138(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，查看详情明细页面，各项查询条件单项和联合查询成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择已发布数据点击查看;步骤3:明细页面单项查询;步骤4:联合查询;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_139(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，查看详情总量页面，各项查询条件单项和联合查询成功")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择已发布数据点击查看;步骤3:总量页面单项查询;步骤4:联合查询;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_140(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，查看详情总量页面，导出数据成功，导出文件数据内容正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择已发布数据点击查看;步骤3:总量页面点击导出;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_141(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，查看详情明细页面，导出数据成功，导出文件数据内容正确")  # 用例名称
    @allure.description("步骤1:登录DRP，进入DRP管理DRP2国家销售版;步骤2:选择已发布数据点击查看;步骤3:明细页面点击导出;")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_142(self, drivers):
        pass


if __name__ == '__main__':
      pass
