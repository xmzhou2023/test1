import allure
import pytest
from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_ModelDatabase import ModelDatabase


@allure.feature("DRP数据管理-机型库")
class TestSwitchMenu:

    @allure.story("前往菜单")
    @allure.title("前往产品信息菜单123")
    @allure.description("点击‘产品信息‘，前往‘产品信息‘菜单123")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')

    @allure.story("前往菜单")
    @allure.title("前往产品配置菜单")
    @allure.description("点击‘产品配置’，前往‘产品配置‘菜单")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品配置')

    @allure.story("前往菜单")
    @allure.title("前往产品周期菜单")
    @allure.description("点击‘产品周期‘，前往‘产品周期‘菜单")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品周期')


@allure.feature("DRP数据管理-机型库")
class TestButtonFunction:

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，新增按钮 功能验证")
    @allure.description("前往‘产品信息‘菜单，点击新增按钮，弹出新增窗口")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_002_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')
        user.append_button()
        user = DomAssert(drivers)
        user.assert_att("新增机型")
        user = ModelDatabase(drivers)
        user.append_cancel()

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，‘变更日志’按钮 功能验证")
    @allure.description("进入机型库-产品信息页面，点击‘变更日志’按钮，自动打开并跳转到变更日志目标页")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_002_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.changelog_button()  # 点击‘变更日志’按钮
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelRecord")  # URL断言

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，‘导入’按钮 功能验证")
    @allure.description("进入机型库-产品信息页面，点击‘导入’按钮，弹出导入窗口")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_002_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.import_button()  # 点击‘导入’按钮
        user = DomAssert(drivers)
        user.assert_att("请先下载模板文件,然后编辑并导入模板数据。")
        user = ModelDatabase(drivers)
        user.importClose_button()  # 关闭导入窗口

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，‘导出’按钮 功能验证")
    @allure.description("进入机型库-产品信息页面，点击‘导出’按钮，产品信息数据导出成功")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_002_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.export('drp_model_export_info')  # 点击‘导出’按钮，并断言文件名

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，‘筛选’按钮 功能验证")
    @allure.description("进入机型库-产品信息页面，依次点击‘筛选’按钮，展开筛选项")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_002_005(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.screen_button()
        user = DomAssert(drivers)
        user.assert_att("重 置")
        user = ModelDatabase(drivers)
        user.close_screen()


@allure.feature("DRP数据管理-机型库")
class TestAppendProduct:

    @allure.story("新增产品信息")
    @allure.title("新增机型，合法维护必填项 新增成功")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，依次填选必填项，新增成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_003_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.append_button()  # 点击新增按钮
        user.source_option('数仓')  # 选择来源
        user.supplyType_option('自研')  # 选择供应类型
        user.brand_option('itel')  # 选择品牌
        user.broadCoarse_option('智能机')  # 选择大类粗
        user.series_option('P')  # 选择系列
        user.projectName_option('S11')  # 填选项目名
        user.memoryVersion('64+4')  # 输入内存版本
        user.network_option('5G')  # 选择网络制式
        user.marketName('India')  # 输入市场名
        user.color_window()  # 打开颜色弹窗
        user.color('半透黑')  # 选择颜色
        user.save_color()  # 保存颜色
        user.state_option('MP')  # 选择状态
        user.save_button("正例")  # 新增保存完成
        # user = SQLAssert(drivers)
        # user.assert_sql('',)

    @allure.story("新增产品信息")
    @allure.title("新增机型，合法维护全部字段 新增成功")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，依次填选所有字段，新增成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_003_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.append_button()  # 点击新增按钮
        user.source_option('数仓')  # 选择来源
        user.supplyType_option('自研')  # 选择供应类型
        user.brand_option('itel')  # 选择品牌
        user.broadCoarse_option('智能机')  # 选择大类粗
        user.broadFine_option('中端SP')  # 选择大类细
        user.series_option('P')  # 选择系列
        user.projectName_option('S11')  # 选择项目名
        user.memoryVersion('64+4')  # 输入内存版本
        user.network_option('5G')  # 选择网络制式
        user.marketName('India')  # 输入市场名
        user.color_window()  # 打开颜色弹窗
        user.color('半透黑')  # 选择颜色
        user.save_color()  # 保存颜色
        user.state_option('MP')  # 选择状态
        user.fob_hk('15')  # 选择FOB HK日期
        user.lt_input('123')  # 输入LT
        user.listing_date('2022', '八月')  # 选择上市时间
        user.cleaning_date('2023', '八月')  # 选择清尾时间
        user.remark_input('123')  # 编辑备注
        user.save_button("正例")  # 新增保存完成

    @allure.story("新增产品信息")
    @allure.title("新增机型，来源=自建，项目名为文本输入框，新增成功")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，来源=自建，项目名为文本输入框，新增成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_003_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.append_button()  # 点击新增按钮
        user.source_option('自建')  # 选择来源
        user.supplyType_option('自研')  # 选择供应类型
        user.brand_option('itel')  # 选择品牌
        user.broadCoarse_option('智能机')  # 选择大类粗
        user.broadFine_option('中端SP')  # 选择大类细
        user.series_option('P')  # 选择系列
        user.projectName_input('test')  # 选择项目名
        user.memoryVersion('64+4')  # 输入内存版本
        user.network_option('5G')  # 选择网络制式
        user.marketName('India')  # 输入市场名
        user.color_window()  # 打开颜色弹窗
        user.color('半透黑')  # 选择颜色
        user.save_color()  # 保存颜色
        user.state_option('MP')  # 选择状态
        user.fob_hk('15')  # 选择FOB HK日期
        user.lt_input('123')  # 输入LT
        user.listing_date('2022', '八月')  # 选择上市时间
        user.cleaning_date('2023', '八月')  # 选择清尾时间
        user.remark_input('123')  # 编辑备注
        user.save_button("正例")  # 新增保存完成

    @allure.story("新增产品信息")
    @allure.title("[异常]新增机型，有必填项未维护 新增失败")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，不维护大类粗必填项，新增失败")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_003_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.append_button()  # 点击新增按钮
        user.source_option('数仓')  # 选择来源
        user.supplyType_option('自研')  # 选择供应类型
        user.brand_option('itel')  # 选择品牌
        user.broadCoarse_option()  # 选择大类粗   必填项未维护
        user.series_option('A')  # 选择系列
        user.projectName_option('S11')  # 填选项目名
        user.memoryVersion('64+4')  # 输入内存版本
        user.network_option('5G')  # 选择网络制式
        user.marketName('India')  # 输入市场名
        user.color_window()  # 打开颜色弹窗
        user.color('半透黑')  # 选择颜色
        user.save_color()  # 保存颜色
        user.state_option('MP')  # 选择状态
        user.save_button("反例")  # 新增保存完成
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")


@allure.feature("DRP数据管理-机型库")
class TestImportFile:

    @allure.story("导入文件")
    @allure.title("产品信息，导入文件数据正确，导入成功")
    @allure.description("前往‘产品信息‘菜单，进入导入弹窗，导入文件成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_004_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.import_button()
        user.selectFile_button()

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，‘导入-下载模板’按钮 功能验证")
    @allure.description("进入导入弹窗，下载导入模板 成功")
    @allure.severity("minor")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_004_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.import_button()  # 点击‘导入’按钮
        user.downloadTemplate_button('drp_model_template.xlsx')  # 下载导入模板，并断言文件名
        user.importClose_button()


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_ModelDatabase.py'])
