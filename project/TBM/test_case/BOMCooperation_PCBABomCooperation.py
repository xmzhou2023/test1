import pytest
from public.base.assert_ui import *
from project.TBM.page_object.BOMCooperation_PCBABomCooperation import PCBABomCooperation


@allure.feature("BOM协作-PCBA BOM协作")  # 模块名称
class TestCreateProcess:
    @allure.story("创建流程")  # 场景名称
    @allure.title("创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，能提交成功“创建流程成功”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_pcba_bom_cooperation_add()
        user.input_pcba_bom_cooperation_add_bom_info('制作类型', 'PCBA BOM制作')
        user.input_pcba_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_pcba_bom_cooperation_add_bom_info('机型', 'JMB-01')
        user.input_pcba_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_pcba_bom_cooperation_add_bom_info('制作虚拟贴片/套片', '否')
        user.click_pcba_bom_cooperation_add_bomtree()
        user.input_pcba_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_pcba_bom_cooperation_bomtree('物料编码', '12105821')
        user.input_pcba_bom_cooperation_bomtree('用量', '1')
        user.select_pcba_bom_cooperation_business_review('李小素')
        user.select_pcba_bom_cooperation_business_review('李小素', '射频&天线工程师')
        user.click_pcba_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('创建流程成功')
        user.refresh()
        user.assert_pcba_bom_cooperation_add_result('PCBA BOM制作', 'JMB-01', 'itel', '试产阶段', '审批中', '未同步')
        process_code = user.get_pcba_bom_cooperation_info()[2]
        user.delete_pcba_bom_cooperation_flow(process_code)


@allure.feature("BOM协作-PCBA BOM协作")  # 模块名称
class TestCreateProcessExceptionScenario:
    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("导入Bom之前需要选中模板")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，选择一个不存在模板的品牌，其他内容正确填写，查看BOM Tree，无新增BOM按钮；点击导入提示-导入Bom之前需要选中模板")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_pcba_bom_cooperation_add()
        user.input_pcba_bom_cooperation_add_bom_info('制作类型', 'PCBA BOM制作')
        user.input_pcba_bom_cooperation_add_bom_info('品牌', 'aaaaa')
        user.input_pcba_bom_cooperation_add_bom_info('机型', 'JMB-01')
        user.input_pcba_bom_cooperation_add_bom_info('阶段', '量产阶段')
        user.input_pcba_bom_cooperation_add_bom_info('制作虚拟贴片/套片', '否')
        user.assert_pcba_bom_cooperation_add_bomtree_exist(False)
        user.click_pcba_bom_cooperation_bom_import()
        DomAssert(drivers).assert_att('导入Bom之前需要选中模板')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM tree不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，在BOM tree中不点击新增BOM，其他内容正确填写，点击提交，提示BOM tree不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.pcba_bom_cooperation_add_bom_info()
        user.select_pcba_bom_cooperation_business_review('李小素')
        user.select_pcba_bom_cooperation_business_review('李小素', '射频&天线工程师')
        user.click_pcba_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('Bom Tree不能为空！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，在BOM tree中点击新增BOM，不选择BOM状态，其他内容正确填写，点击提交，提示BOM状态不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_003(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.pcba_bom_cooperation_add_bom_info()
        user.click_pcba_bom_cooperation_add_bomtree()
        user.input_pcba_bom_cooperation_bomtree('物料编码', '12105866')
        user.input_pcba_bom_cooperation_bomtree('用量', '1')
        user.click_pcba_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('BOM状态不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM编码[null]的物料组在对应的模板中未设置！")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，在BOM tree中点击新增BOM，不填写物料编码，其他内容正确填写，点击提交，提示BOM编码[null]的物料组在对应的模板中未设置！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_004(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.pcba_bom_cooperation_add_bom_info()
        user.click_pcba_bom_cooperation_add_bomtree()
        user.input_pcba_bom_cooperation_bomtree('BOM状态', '量产')
        user.input_pcba_bom_cooperation_bomtree('用量', '1')
        user.select_pcba_bom_cooperation_business_review('李小素')
        user.select_pcba_bom_cooperation_business_review('李小素', '射频&天线工程师')
        user.click_pcba_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('BOM编码[null]的物料组在对应的模板中未设置！')


if __name__ == '__main__':
    pytest.main(['BOMCooperation_PCBABomCooperation.py'])
