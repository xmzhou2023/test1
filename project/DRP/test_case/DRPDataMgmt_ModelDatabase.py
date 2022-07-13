import allure
import pytest
from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_ModelDatabase import ModelDatabase


@allure.feature("DRP数据管理-机型库")
class TestSwitchMenu:

    @allure.story("切换菜单")
    @allure.title("前往产品信息菜单")
    @allure.description("前往‘产品信息‘菜单")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab(tab='产品信息')

    @allure.story("切换菜单")
    @allure.title("前往产品配置菜单")
    @allure.description("前往‘产品配置‘菜单")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab(tab='产品配置')

    @allure.story("切换菜单")
    @allure.title("前往产品周期菜单")
    @allure.description("前往‘产品周期‘菜单")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab(tab='产品周期')


@allure.feature("DRP数据管理-机型库")
class TestAppendProduct:

    @allure.story("新增产品信息")
    @allure.title("产品信息 新增/取消按钮功能检查")
    @allure.description("前往‘产品信息‘菜单，依次点击新增/取消按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab(tab='产品信息')
        user.button(button='新 增')
        user.cancel(button='取消')

    @allure.story("新增产品信息")
    @allure.title("产品信息 合法维护必填项新增成功")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，依次填选必填项，新增成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab(tab='产品信息')                             # 切换到产品信息tab页
        user.button(button='新 增')                              # 点击新增按钮
        user.source_option(source='数仓')                        # 选择来源
        user.supplyType_option(supplyType='自研')                # 选择供应类型
        user.brand_option(brand='itel')                         # 选择品牌
        user.broadCoarse_option(broadCoarse='智能机')            # 选择大类粗
        user.series_option(series='P')                          # 选择系列
        user.projectName_option(projectName='S11')              # 选择项目名
        user.memoryVersion(memoryVersion='64+4')                # 输入内存版本
        user.network_option(network='5G')                       # 选择网络制式
        user.marketName(marketName='India')                     # 输入市场名
        user.color_window()                                     # 打开颜色弹窗
        user.color(color='半透黑')                               # 选择颜色
        user.save_color()                                       # 保存颜色
        user.state_option(state='MP')                           # 选择状态
        user.save_button(save='确定')                            # 新增保存完成

    @allure.story("新增产品信息")
    @allure.title("产品信息 合法维护所有字段 新增成功")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，依次填选所有字段，新增成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab(tab='产品信息')                             # 切换到产品信息tab页
        user.button(button='新 增')                              # 点击新增按钮
        user.source_option(source='数仓')                        # 选择来源
        user.supplyType_option(supplyType='自研')                # 选择供应类型
        user.brand_option(brand='itel')                         # 选择品牌
        user.broadCoarse_option(broadCoarse='智能机')            # 选择大类粗
        user.broadFine_option(broadFine='中端SP')                # 选择大类细
        user.series_option(series='P')                          # 选择系列
        user.projectName_option(projectName='S11')              # 选择项目名
        user.memoryVersion(memoryVersion='64+4')                # 输入内存版本
        user.network_option(network='5G')                       # 选择网络制式
        user.marketName(marketName='India')                     # 输入市场名
        user.color_window()                                     # 打开颜色弹窗
        user.color(color='半透黑')                               # 选择颜色
        user.save_color()                                       # 保存颜色
        user.state_option(state='MP')                           # 选择状态
        user.FOB_HK(date='15')                                  # 选择FOB HK日期
        user.LT_input(LT='123')                                 # 输入LT
        user.listing_date(years='2022', month='八月')            # 选择上市时间
        user.cleaning_date(years='2023', month='八月')           # 选择清尾时间
        user.remark_input(remark='123')                         # 编辑备注
        user.save_button(save='确定')                            # 新增保存完成

    @allure.story("新增产品信息")
    @allure.title("新增机型，来源=自建，项目名为文本输入框，新增成功")
    @allure.description("前往‘产品信息‘菜单，打开新增窗口，来源=自建，项目名为文本输入框，新增成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab(tab='产品信息')                             # 切换到产品信息tab页
        user.button(button='新 增')                              # 点击新增按钮
        user.source_option(source='自建')                        # 选择来源
        user.supplyType_option(supplyType='自研')                # 选择供应类型
        user.brand_option(brand='itel')                         # 选择品牌
        user.broadCoarse_option(broadCoarse='智能机')            # 选择大类粗
        user.broadFine_option(broadFine='中端SP')                # 选择大类细
        user.series_option(series='P')                          # 选择系列
        user.projectName_input(projectName='test')              # 选择项目名
        user.memoryVersion(memoryVersion='64+4')                # 输入内存版本
        user.network_option(network='5G')                       # 选择网络制式
        user.marketName(marketName='India')                     # 输入市场名
        user.color_window()                                     # 打开颜色弹窗
        user.color(color='半透黑')                               # 选择颜色
        user.save_color()                                       # 保存颜色
        user.state_option(state='MP')                           # 选择状态
        user.FOB_HK(date='15')                                  # 选择FOB HK日期
        user.LT_input(LT='123')                                 # 输入LT
        user.listing_date(years='2022', month='八月')            # 选择上市时间
        user.cleaning_date(years='2023', month='八月')           # 选择清尾时间
        user.remark_input(remark='123')                         # 编辑备注
        user.save_button(button='确定')                          # 新增保存完成


@allure.feature("DRP数据管理-机型库")
class TestChangeLog:

    @allure.story("变更日志按钮")
    @allure.title("‘变更日志’按钮 功能验证")
    @allure.description("进入机型库-产品信息页面，点击‘变更日志’按钮，自动打开并跳转到变更日志目标页")
    @allure.severity("minor")  # blocker\critical\normal\minor\trivial
    # # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab(tab='产品信息')                             # 切换到产品信息tab页
        user.button(button='变更日志')                            # 点击‘变更日志’按钮
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelRecord")              # URL断言


@allure.feature("DRP数据管理-机型库")
class TestImport:

    @allure.story("导入")
    @allure.title("‘导入’按钮 功能验证")
    @allure.description("进入机型库-产品信息页面，点击‘导入’按钮，弹出导入窗口")
    @allure.severity("minor")  # blocker\critical\normal\minor\trivial
    # # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab(tab='产品信息')                             # 切换到产品信息tab页
        user.button(button='导入')                               # 点击‘导入’按钮

    @allure.story("导入-下载模板")
    @allure.title("‘导入-下载模板’按钮 功能验证")
    @allure.description("进入导入弹窗，下载导入模板")
    @allure.severity("minor")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("DRP数据管理", "机型库")
        user = DomAssert(drivers)
        user.assert_url("/dataManage/modelLibrary")
        user = ModelDatabase(drivers)
        user.goto_tab(tab='产品信息')                             # 切换到产品信息tab页
        user.button(button='导入')                               # 点击‘导入’按钮


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_ModelDatabase.py'])
