import allure
import pytest
from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_ModelDatabase import ModelDatabase


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“DRP数据管理-机型库”页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP数据管理", "机型库")
    user = DomAssert(drivers)
    user.assert_url("/dataManage/modelLibrary")


@allure.feature("DRP数据管理-机型库")
class TestSwitchMenu:

    @allure.story("前往菜单")
    @allure.title("前往产品信息菜单")
    @allure.description("点击‘产品信息‘，前往‘产品信息‘菜单")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')
        title = user.goto_tab('产品信息')
        ValueAssert.value_assert_equal(title, "新 增")

    @allure.story("前往菜单")
    @allure.title("前往产品配置菜单")
    @allure.description("点击‘产品配置’，前往‘产品配置‘菜单")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品配置')
        title = user.goto_tab('产品配置')
        ValueAssert.value_assert_equal(title, "状态")

    @allure.story("前往菜单")
    @allure.title("前往产品周期菜单")
    @allure.description("点击‘产品周期‘，前往‘产品周期‘菜单")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品周期')
        title = user.goto_tab('产品周期')
        ValueAssert.value_assert_equal(title, "管理维度")


@allure.feature("DRP数据管理-机型库")
class TestButtonFunction:

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，新增按钮 功能验证")
    @allure.description("前往‘产品信息‘菜单，点击新增按钮，弹出新增窗口")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')
        user.append_button()
        title = user.append_title()
        ValueAssert.value_assert_equal(title, "新增机型")
        user.append_cancel()

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，‘变更日志’按钮 功能验证")
    @allure.description("进入机型库-产品信息页面，点击‘变更日志’按钮，自动打开并跳转到变更日志目标页")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_002(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.changelog_button()  # 点击‘变更日志’按钮
        assertURL = DomAssert(drivers)
        assertURL.assert_url("/dataManage/modelRecord")  # URL断言
        user.close_changelog()

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，‘导入’按钮 功能验证")
    @allure.description("进入机型库-产品信息页面，点击‘导入’按钮，弹出导入窗口")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_003(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.import_button()  # 点击‘导入’按钮
        title = user.import_title()
        ValueAssert.value_assert_equal(title, "请先下载模板文件,然后编辑并导入模板数据。")
        user.importClose_button()  # 关闭导入窗口

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，‘导出’按钮 功能验证")
    @allure.description("进入机型库-产品信息页面，点击‘导出’按钮，产品信息数据导出成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_004(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.export('drp_model_export_info')  # 点击‘导出’按钮，并断言文件名

    @allure.story("页面按钮功能验证")
    @allure.title("产品信息，‘筛选’按钮 功能验证")
    @allure.description("进入机型库-产品信息页面，依次点击‘筛选’按钮，展开筛选项")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_005(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.screen_button()
        title = user.screen_title()
        ValueAssert.value_assert_equal(title,"筛选")
        user.close_screen()


@allure.feature("DRP数据管理-机型库")
class TestAppendProduct:

    @allure.story("新增产品信息")
    @allure.title("新增机型，合法维护必填项 新增成功")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，依次填选必填项，新增成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.append_button()  # 点击新增按钮
        user.source_option('数仓')  # 选择来源
        user.supplyType_option('自研')  # 选择供应类型
        user.brand_option('itel')  # 选择品牌
        user.broadCoarse_option('智能机')  # 选择大类粗
        user.series_option('A')  # 选择系列
        user.projectName_option('S11')  # 填选项目名
        user.memoryVersion('64+4')  # 输入内存版本
        user.network_option('5G')  # 选择网络制式
        user.marketName('India')  # 输入市场名
        user.color('半透黑')  # 选择颜色
        user.save_color()  # 保存颜色
        user.state_option('MP')  # 选择状态
        user.save_button("正例")  # 新增保存完成
        hintAssert = user.save_hint()
        ValueAssert.value_assert_equal(hintAssert,"新增成功!")
        """清空测试数据"""
        user.delete_testData(drivers,brand='itel',broadCoarse='智能机',mobileType='S11 64+4',marketName='India',series='A',projectName='S11',state='MP',source='数仓',supplyType='自研')

    @allure.story("新增产品信息")
    @allure.title("新增机型，合法维护全部字段 新增成功")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，依次填选所有字段，新增成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.append_button()  # 点击新增按钮
        user.source_option('数仓')  # 选择来源
        user.supplyType_option('自研')  # 选择供应类型
        user.brand_option('itel')  # 选择品牌
        user.broadCoarse_option('智能机')  # 选择大类粗
        user.broadFine_option('中端SP')  # 选择大类细
        user.series_option('A')  # 选择系列
        user.projectName_option('S11')  # 选择项目名
        user.memoryVersion('64+4')  # 输入内存版本
        user.network_option('5G')  # 选择网络制式
        user.marketName('India')  # 输入市场名
        user.color('半透黑')  # 选择颜色
        user.save_color()  # 保存颜色
        user.state_option('MP')  # 选择状态
        user.fob_hk('15')  # 选择FOB HK日期
        user.lt_input('123')  # 输入LT
        user.listing_date('2022', '八月')  # 选择上市时间
        user.cleaning_date('2023', '八月')  # 选择清尾时间
        user.remark_input('123')  # 编辑备注
        user.save_button("正例")  # 新增保存完成
        hintAssert = user.save_hint()
        ValueAssert.value_assert_equal(hintAssert,"新增成功!")
        """清空测试数据"""
        user.delete_testData(drivers,brand='itel',broadCoarse='智能机',mobileType='S11 64+4',marketName='India',series='A',projectName='S11',state='MP',source='数仓',supplyType='自研')


    @allure.story("新增产品信息")
    @allure.title("新增机型，来源=自建，项目名为文本输入框，新增成功")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，来源=自建，项目名为文本输入框，新增成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_003(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.append_button()  # 点击新增按钮
        user.source_option('自建')  # 选择来源
        user.supplyType_option('自研')  # 选择供应类型
        user.brand_option('itel')  # 选择品牌
        user.broadCoarse_option('智能机')  # 选择大类粗
        user.broadFine_option('中端SP')  # 选择大类细
        user.series_option('P')  # 选择系列
        user.projectName_input('S11')  # 选择项目名
        user.memoryVersion('64+5')  # 输入内存版本
        user.network_option('5G')  # 选择网络制式
        user.marketName('India')  # 输入市场名
        user.color('半透黑')  # 选择颜色
        user.save_color()  # 保存颜色
        user.state_option('MP')  # 选择状态
        user.fob_hk('15')  # 选择FOB HK日期
        user.lt_input('123')  # 输入LT
        user.listing_date('2022', '八月')  # 选择上市时间
        user.cleaning_date('2023', '八月')  # 选择清尾时间
        user.remark_input('123')  # 编辑备注
        user.save_button("正例")  # 新增保存完成
        hintAssert = user.save_hint()
        ValueAssert.value_assert_equal(hintAssert,"新增成功!")
        """清空测试数据"""
        user.delete_testData(drivers,brand='itel',broadCoarse='智能机',mobileType='S11 64+5',marketName='India',series='P',projectName='S11',state='MP',source='自建',supplyType='自研')


    @allure.story("新增产品信息")
    @allure.title("[异常]新增机型，有必填项未维护 新增失败")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，不维护大类粗必填项，新增失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_004(self, drivers):
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
        user.color('半透黑')  # 选择颜色
        user.save_color()  # 保存颜色
        user.state_option('MP')  # 选择状态
        user.save_button("反例")  # 新增保存失败 并关闭新建窗口


@allure.feature("DRP数据管理-机型库")
class TestImportFile:

    @allure.story("导入文件")
    @allure.title("产品信息，导入文件数据正确，导入成功")
    @allure.description("前往‘产品信息‘菜单，进入导入弹窗，导入文件成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.skip
    def test_004_001(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.import_button()
        user.selectFile_button()

    @allure.story("导入文件")
    @allure.title("产品信息，‘导入-下载模板’按钮 功能验证")
    @allure.description("进入导入弹窗，下载导入模板 成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_002(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.import_button()  # 点击‘导入’按钮
        user.downloadTemplate_button('drp_model_template.xlsx')  # 下载导入模板，并断言文件名
        user.importClose_button()


@allure.feature("DRP数据管理-机型库")
class TestScreenFunction:
    """按条件筛选机型"""
    @allure.story("筛选功能")
    @allure.title("产品信息，筛选功能验证")
    @allure.description("打开筛选弹窗，输入筛选条件，筛选机型正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_001(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.insert_testData1(drivers)  # 插入测试数据
        user.screen_button()  # 点击筛选按钮，弹出筛选框
        user.screen_brand("itel")  # 选择品牌
        user.screen_broadCoarse("智能机")  # 选择大类粗
        user.screen_mobileType("S11 64+4")  # 输入机型
        user.screen_marketName("India")  # 输入市场名
        user.screen_series("A")  # 输入系列
        user.screen_projectName("S11")  # 输入项目名
        user.screen_state("MP")  # 选择状态
        user.screen_source("数仓")  # 选择来源
        user.screen_supplyType("自研")  # 选择供应类型
        user.screen_inquire()  # 点击查询按钮
        user.assert_screen_result("隆江",num=22)
        """清空测试数据"""
        user.delete_button("隆江", num=22)  # 点击指定行删除按钮

    @allure.story("筛选功能")
    @allure.title("产品信息，组合条件查询，无匹配数据")
    @allure.description("打开筛选弹窗，输入筛选条件，点击查询，页面显示’暂无数据‘字样")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_002(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.screen_button()  # 点击筛选按钮，弹出筛选框
        user.screen_brand("itel")  # 选择品牌
        user.screen_broadCoarse("功能机")  # 选择大类粗
        user.screen_broadFine("功能机")  # 选择大类细
        user.screen_mobileType("S")  # 输入机型
        user.screen_inquire()  # 点击查询按钮
        countscreen = user.screen_count()
        ValueAssert.value_assert_IsNoneNot(countscreen)
        screen_result = user.screen_result_null()
        ValueAssert.value_assert_equal(screen_result, '暂无数据')

    @allure.story("筛选功能")
    @allure.title("产品信息，点击重置，筛选条件被清空")
    @allure.description("打开筛选弹窗，先完成组合筛选，再点击重置按钮，页面刷新，筛选条件被清空，列表展示所有数据")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_003(self, drivers):
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.screen_button()  # 点击筛选按钮，弹出筛选框
        user.screen_brand("itel")  # 选择品牌
        user.screen_broadCoarse("功能机")  # 选择大类粗
        user.screen_broadFine("功能机")  # 选择大类细
        user.screen_mobileType("S")  # 输入机型
        user.screen_inquire()  # 点击查询按钮
        countScreen = user.screen_count()
        ValueAssert.value_assert_IsNoneNot(countScreen)
        user.screen_button()  # 点击筛选按钮，弹出筛选框
        user.screen_reset()  # 点击重置按钮
        countScreen = user.screen_count()
        ValueAssert.value_assert_IsNoneNot(countScreen)
        user.assert_screen_result('冯晨', num=22)


@allure.feature("DRP数据管理-机型库")
class TestUpdate:
    """编辑机型信息"""
    @allure.story("编辑功能")
    @allure.title("产品信息，编辑指定行数据")
    @allure.description("将供应类型修改为外购 保存成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_006_001(self, drivers):
        user = ModelDatabase(drivers)
        user.insert_testData(drivers)  # 插入测试数据
        user.update_button("隆江", num=22)  # 点击指定行编辑按钮
        user.update_something(2,"外购")
        user.update_save()
        user.screen_button()  # 点击筛选按钮，弹出筛选框
        user.screen_supplyType("外购")  # 选择供应类型
        user.screen_inquire()  # 点击查询按钮
        user.assert_screen_result("隆江", num=22)
        """清空测试数据"""
        user.delete_button("隆江", num=22)  # 点击指定行删除按钮

@allure.feature("DRP数据管理-机型库")
class TestDelete:
    @allure.story("删除功能")
    @allure.title("产品信息，删除指定行数据")
    @allure.description("打开筛选弹窗，输入筛选条件过滤指定数据，将xx数据删除")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_007_001(self, drivers):
        user = ModelDatabase(drivers)
        user.insert_testData(drivers)
        user.delete_button("隆江", num=22)  # 点击指定行删除按钮
        hint = user.delete_hint()
        ValueAssert.value_assert_equal(hint, "删除成功!")







if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_ModelDatabase.py'])
