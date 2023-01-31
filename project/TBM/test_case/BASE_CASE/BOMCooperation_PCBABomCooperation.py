import pytest
from public.base.assert_ui import *
from project.TBM.page_object.BOMCooperation_PCBABomCooperation import PCBABomCooperation


@allure.feature("BOM协作-PCBA BOM协作")  # 模块名称
class TestCreateProcess:
    @allure.story("创建流程")  # 场景名称
    @allure.title("创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，能提交成功并且提示“建流程成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM制作')
        user.input_bom_info('品牌', 'Infinix')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('制作虚拟贴片/套片', '否')
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12105821')
        user.input_bomtree('PCBA', '数量', '1')
        user.select_business_review('李小素')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "PCBA BOM协作", '自动化新增用例', 'PCBA BOM制作', 'JMB-01', 'Infinix', '试产阶段', '审批中', '未同步')
        process_code = user.get_bom_info('PCBA BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("添加替代组，创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，在充电器中新增两颗物料，添加替代组都为A1，份额为一个20，一个30，其他内容正确填写，点击提交，能提交成功并且提示“创建流程成功”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM制作')
        user.input_bom_info('品牌', 'Infinix')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('制作虚拟贴片/套片', '否')
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12105698')
        user.input_bomtree('PCBA', '数量', '1')
        user.input_bomtree('CPU', '物料编码', '12105820')
        user.input_bomtree('CPU', '数量', '1')
        user.input_bomtree('CPU', '替代组', 'A1')
        user.input_bomtree('CPU', '份额', '20')
        user.click_add_material()
        user.input_add_material('12105820', '物料编码', '12105822')
        user.input_add_material('12105820', '数量', '1')
        user.input_add_material('12105820', '替代组', 'A1')
        user.input_add_material('12105820', '份额', '80')
        user.select_business_review('李小素')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "PCBA BOM协作", '自动化新增用例', 'PCBA BOM制作', 'JMB-01', 'Infinix', '试产阶段', '审批中', '未同步')
        process_code = user.get_bom_info('PCBA BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")
    @allure.title("一键填写生效")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在PCBA中和PCB中正确选择物料编码，选中两颗物料，点击一键填写，填写数量为1点击确认，页面上显示两颗物料用量都为1")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_003(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12105698')
        user.input_bomtree('CPU', '物料编码', '12105820')
        user.click_BOMTree_checkbox()
        user.input_OnePress('数量', '1')
        user.assert_BomTree_OnepressResult('12105698', '数量', '1', 'code')
        user.assert_BomTree_OnepressResult('12105820', '数量', '1', 'code')

    @allure.story("创建流程")
    @allure.title("BOM tree中不选择物料，页面上不存在删除按钮")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不选择物料，页面上不存在删除按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_004(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.assert_batch_delete(False)

    @allure.story("创建流程")
    @allure.title("BOM tree中选择物料，页面上存在删除按钮")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择物料，页面上存在删除按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_005(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_BOMTree_checkbox()
        user.assert_batch_delete(True)

    @allure.story("创建流程")
    @allure.title("选中父节点物料后点击删除，删除页面数据")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_006(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_bomtree_delete('PCBA')
        user.click_batch_confirm()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("创建流程")
    @allure.title("选中子节点物料后点击删除，清子节点内容")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_007(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('CPU', '物料编码', '25001649')
        user.input_bomtree('CPU', '数量', '1000')
        user.input_bomtree('CPU', '替代组', 'A1')
        user.input_bomtree('CPU', '份额', '20')
        user.click_bomtree_delete('CPU')
        user.assert_BomTree_OnepressResult('CPU', '物料编码', '')
        user.assert_BomTree_OnepressResult('CPU', '数量', '')
        user.assert_BomTree_OnepressResult('CPU', '替代组', '')
        user.assert_BomTree_OnepressResult('CPU', '份额', '')

    @allure.story("创建流程")
    @allure.title("选择正确的文件进行导入，并应用，显示的数据与模板的数据一致")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_008(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_bom_import()
        user.add_import_file('PCBA发起导入模板.xlsx')
        user.assert_import_success()
        user.assert_upload_result(('1', '试产', '12105866', '贴片主板_SU385_A1_32GB+2GB_V1.1_自制', '15800619',
                                   '副板PCB_H6123_SUB_PCB_1_6LPTH_V1.1_ZBX', '1'))
        user.click_apply()
        user.click_tree('PCBA')
        user.assert_tree_result(('1', 'PCBA', '12105866', '贴片主板_SU385_A1_32GB+2GB_V1.1_自制', '可选', '1', '编辑删除'),
                                ('1.1', 'PCB155/158', '15800619', '副板PCB_H6123_SUB_PCB_1_6LPTH_V1.1_ZBX', '可选', '1', '编辑删除'))

    @allure.story("创建流程")  # 场景名称
    @allure.title("PCBA BOM衍生,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息包含新增为128开头的物料，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，提示发起成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_009(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12398884')
        user.input_Derived_info('原始BOM编码', '12106993')
        user.input_Derived_info('原始BOM工厂', 'C105')
        user.click_Derived_differ()
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12398884')
        user.input_Derived_info('操作', '新增物料')
        user.input_Derived_info('处理物料编码', '12105698')
        user.input_Derived_info('数量', '1')
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '结构工程师')
        user.select_business_review('李小素', '采购部(NPS)')
        user.select_business_review('李小素', '射频&天线工程师')
        user.select_business_review('李小素', '检查人')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "PCBA BOM协作", '自动化新增用例', 'PCBA BOM衍生', 'JMB-01', 'itel', '试产阶段', '审批中')
        process_code = user.get_bom_info('PCBA BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("PCBA BOM衍生,不填写衍生差异信息，创建流程成功")  # 用例名称
    @allure.description("在PCBA BOM制作新增页面，制作类型选择PCBA BOM衍生，填写BOM信息，在衍生BOM制作需求点击新增正确填写信息，不填写衍生差异信息，点击生成BOM，填写业务评审和业务审核，点击提交，提交成功并流程发起成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_010(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12398884')
        user.input_Derived_info('原始BOM编码', '12106993')
        user.input_Derived_info('原始BOM工厂', 'C105')
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '结构工程师')
        user.select_business_review('李小素', '采购部(NPS)')
        user.select_business_review('李小素', '射频&天线工程师')
        user.select_business_review('李小素', '检查人')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "PCBA BOM协作", '自动化新增用例', 'PCBA BOM衍生', 'JMB-01', 'itel', '试产阶段', '审批中')
        process_code = user.get_bom_info('PCBA BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("PCBA BOM衍生导入模板,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，下载模板，模板内容正确填写包含新增为128开头的物料，在衍生差异点击导入，文件导入成功，点击生成BOM，点击刷新，填写业务审核，点击提交，流程发起成功并提示流程创建成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_011(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.click_Derived_import()
        user.add_import_file('PCBA衍生BOM制作需求导入模板.xlsx')
        user.click_apply()
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '结构工程师')
        user.select_business_review('李小素', '采购部(NPS)')
        user.select_business_review('李小素', '射频&天线工程师')
        user.select_business_review('李小素', '检查人')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "PCBA BOM协作", '自动化新增用例', 'PCBA BOM衍生', 'JMB-01', 'itel', '试产阶段', '审批中')
        process_code = user.get_bom_info('PCBA BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("PCBA BOM衍生,保存草稿成功")  # 用例名称
    @allure.description("在PCBA BOM制作新增页面，制作类型选择PCBA BOM衍生，填写BOM信息，在衍生BOM制作需求和衍生差异信息，点击新增正确填写信息，点击生成BOM，填写业务评审和业务审核，点击保存，提示：保存草稿成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_012(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.click_Derived_import()
        user.add_import_file('PCBA衍生BOM制作需求导入模板.xlsx')
        user.click_apply()
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '结构工程师')
        user.select_business_review('李小素', '采购部(NPS)')
        user.select_business_review('李小素', '射频&天线工程师')
        user.select_business_review('李小素', '检查人')
        user.click_add_save()
        user.assert_toast('保存草稿成功')
        user.refresh()
        user.assert_add_result("BOM协作", "PCBA BOM协作", '自动化新增用例', 'PCBA BOM衍生', 'JMB-01', 'itel', '试产阶段', '草稿')
        process_code = user.get_bom_info('PCBA BOM协作', '自动化新增用例', '流程编码')
        user.click_delete(process_code)
        user.click_dialog_confirm()
        user.assert_toast('删除成功')


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
        user.click_add()
        user.input_bom_info('制作类型', 'PCBA BOM制作')
        user.input_bom_info('品牌', '其他')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('制作虚拟贴片/套片', '否')
        user.assert_add_bomtree_exist(False)
        user.click_bom_import()
        user.assert_toast('导入Bom之前需要选中模板')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM tree不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，在BOM tree中不点击新增BOM，其他内容正确填写，点击提交，提示BOM tree不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.select_business_review('李小素')
        user.select_business_review('李小素', '射频&天线工程师')
        user.click_add_submit()
        user.assert_toast('Bom Tree不能为空！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，在BOM tree中点击新增BOM，不选择BOM状态，其他内容正确填写，点击提交，提示BOM状态不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_003(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', '物料编码', '12398884')
        user.input_bomtree('PCBA', '数量', '1')
        user.click_add_submit()
        user.assert_toast('BOM状态不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM编码[null]的物料组在对应的模板中未设置！")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，在BOM tree中点击新增BOM，不填写物料编码，其他内容正确填写，点击提交，提示BOM编码空的物料组在对应的模板中未设置！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_004(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '数量', '1')
        user.select_business_review('李小素')
        user.select_business_review('李小素', '射频&天线工程师')
        user.click_add_submit()
        user.assert_toast('BOM编码[null]的物料组在对应的模板中未设置！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("请完善Bom信息")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，选择一个不存在模板的品牌，其他内容正确填写，点击提交，不能提交成功并给出提示请完善Bom信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_005(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', 'PCBA BOM制作')
        user.input_bom_info('品牌', '其他')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('制作虚拟贴片/套片', '否')
        user.click_add_submit()
        user.assert_toast('请完善Bom信息！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不添加BOM内容，其他内容正确填写，点击提交，不能提交成功并给出提示BOM状态不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_006(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_add_submit()
        user.assert_toast('BOM状态不能为空')

    @allure.story("创建流程异常场景")
    @allure.title("xxxxxxxx的数量为空")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，数量不进行填写，点击提交，不能提交成功并给出提示xxxxxxxx的数量为空!")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_007(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12398884')
        user.select_business_review('李小素')
        user.click_add_submit()
        user.assert_toast('[12398884]的数量为空!')

    @allure.story("创建流程异常场景")
    @allure.title("数量长度超3字符")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，数量填写为1000，点击提交，不能提交成功并给出提示数量长度超3字符")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_008(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12398884')
        user.input_bomtree('PCBA', '数量', '1000')
        user.select_business_review('李小素')
        user.click_add_submit()
        user.assert_toast('数量长度超3字符')

    @allure.story("创建流程异常场景")
    @allure.title("数量只能填写1-8位正整数")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，数量填写为非数字类型，点击提交，不能提交成功并给出提示数量只能填写1-8位正整数")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_009(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12105866')
        user.input_bomtree('PCBA', '数量', 'aaa')
        user.select_business_review('李小素')
        user.click_add_submit()
        user.assert_toast('数量只能填写1-8位正整数')

    @allure.story("创建流程异常场景")
    @allure.title("父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx数量不为1")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，选择单机头的物料编码，输入单机头用量为2，点击提示，不能提交成功并给出提示父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx数量不为1")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_010(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12398884')
        user.input_bomtree('PCBA', '数量', '1')
        user.input_bomtree('CPU', '物料编码', '12105820')
        user.input_bomtree('CPU', '数量', '2')
        user.select_business_review('李小素')
        user.click_add_submit()
        user.assert_toast('父阶BOM料号12398884下的子阶BOM料号12105820数量不为1')

    @allure.story("创建流程异常场景")
    @allure.title("业务评审必填项需填写完整")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示业务评审必填项需填写完整！")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_011(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12105866')
        user.input_bomtree('PCBA', '数量', '1')
        user.click_add_submit()
        user.assert_toast('业务评审必填项需填写完整！')

    @allure.story("创建流程异常场景")
    @allure.title("不选择物料，一键填写不生效")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入PCBA数据，不选择物料，点击一键填写，填写数量为1，点击确定，页面上没有填写上任何数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_012(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12105866')
        user.input_OnePress('数量', '1')
        user.assert_BomTree_OnepressResult('12105866', '数量',  '', 'code')

    @allure.story("创建流程异常场景")
    @allure.title("不填写产成品数据，选择物料一键填写不生效")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在PCBA中不选择物料编码，全选选中物料，点击一键填写，一键填写时选择数量为1，点击确定，页面上不会新增用量数量")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_013(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_BOMTree_checkbox()
        user.input_OnePress('数量', '1')
        user.assert_BomTree_OnepressResult('PCBA', '数量', '')

    @allure.story("创建流程异常场景")
    @allure.title("不能为空")
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产成品中和单机头中正确选择物料编码，选中两颗物料，点击一键填写，选择用量，并且不填写字段值，点击确认，给出必填提示，提示为“不能为空”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_014(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_BOMTree_checkbox()
        user.input_OnePress('数量', '')
        DomAssert(drivers).assert_att('不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("一键填写无内容提示内容不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示“文件类型非excel!”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_015(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_bom_import()
        user.add_import_file('worng_file_text.txt')
        user.assert_toast('文件类型非excel!')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("模板正确内容错误的文件进行导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_016(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_bom_import()
        user.add_import_file('PCBA发起导入模板错误内容.xlsx')
        user.assert_import_fail()
        user.assert_wrongcontent_upload_result()

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("[XXXXX] 替代组[XX]只有一颗物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，新增物料，添加替代组为A1，份额为20，其他内容正确填写，点击提交，不能提交成功并且提示“替代组只有一颗物料”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_017(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12105698')
        user.input_bomtree('PCBA', '数量', '1')
        user.input_bomtree('CPU', '物料编码', '12105820')
        user.input_bomtree('CPU', '数量', '1')
        user.input_bomtree('CPU', '替代组', 'A1')
        user.input_bomtree('CPU', '份额', '20')
        user.click_add_submit()
        user.assert_toast('[12105698] 替代组[A1]只有一颗物料')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("输入位号U1001,U1002,U1003,U1004,U1005，数量自动变为5")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，输入正确的PCBA物料用量为1，在IC144输入物料编码为14400003，输入位号U1001,U1002,U1003,U1004,U1005，数量自动变为5")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_018(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12105698')
        user.input_bomtree('PCBA', '数量', '1')
        user.input_bomtree('IC144', '物料编码', '14400003')
        user.input_bomtree('IC144', '位号', 'U1001,U1002,U1003,U1004,U1005')
        user.assert_BomTree_OnepressResult('14400003', '数量', '5', 'code')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM衍生，Bom Tree不能为空！")  # 用例名称
    @allure.description("在PCBA BOM制作新增页面，制作类型选择PCBA BOM衍生，填写BOM信息，衍生BOM制作需求不点击新增，填写业务评审和业务审核，点击提交，提示：Bom Tree不能为空！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_019(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.click_add_submit()
        user.assert_toast('Bom Tree不能为空！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM衍生，请完善Bom信息！")  # 用例名称
    @allure.description("在PCBA BOM制作新增页面，制作类型选择PCBA BOM衍生，不填写BOM信息，在衍生制作需求点击新增，提示：请完善Bom信息！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_020(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.click_add_submit()
        user.assert_toast('请完善Bom信息！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM衍生，不生成BOM提示Bom Tree不能为空！")  # 用例名称
    @allure.description("在PCBA BOM制作新增页面，制作类型选择PCBA BOM衍生，填写BOM信息，在衍生BOM制作需求和衍生差异信息，点击新增正确填写信息，不点击生成BOM，填写业务评审和业务审核，点击提交，提示：Bom Tree不能为空！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_021(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12398884')
        user.input_Derived_info('原始BOM编码', '12106993')
        user.input_Derived_info('原始BOM工厂', 'C105')
        user.click_Derived_differ()
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12398884')
        user.input_Derived_info('操作', '新增物料')
        user.input_Derived_info('处理物料编码', '12105698')
        user.input_Derived_info('数量', '1')
        user.click_add_submit()
        user.assert_toast('Bom Tree不能为空！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM衍生，原始bom工厂不能为空！;")  # 用例名称
    @allure.description("在PCBA BOM制作新增页面，制作类型选择PCBA BOM衍生，填写BOM信息，在衍生BOM制作需求点击新增不填写原始BOM工厂，点击生成BOM，提示：原始bom工厂不能为空！;")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_022(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12398884')
        user.input_Derived_info('原始BOM编码', '12106993')
        user.click_Creat_BOM()
        user.assert_toast('原始bom工厂不能为空！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("PCBA BOM衍生,数量长度超3字符")  # 用例名称
    @allure.description("在PCBA BOM制作新增页面，制作类型选择PCBA BOM衍生，填写BOM信息，在衍生BOM制作需求点击新增正确填写信息，衍生差异信息数量填1000，点击生成BOM，填写业务评审和业务审核，点击提交，提示：数量长度超3字符;")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_023(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12398884')
        user.input_Derived_info('原始BOM编码', '12106993')
        user.input_Derived_info('原始BOM工厂', 'C105')
        user.click_Derived_differ()
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12398884')
        user.input_Derived_info('操作', '新增物料')
        user.input_Derived_info('处理物料编码', '12105698')
        user.input_Derived_info('数量', '1000')
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '结构工程师')
        user.select_business_review('李小素', '采购部(NPS)')
        user.select_business_review('李小素', '射频&天线工程师')
        user.select_business_review('李小素', '检查人')
        user.click_add_submit()
        user.assert_toast('数量长度超3字符')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("PCBA BOM衍生,业务评审必填项需填写完整！")  # 用例名称
    @allure.description("在PCBA BOM制作新增页面，制作类型选择PCBA BOM衍生，填写BOM信息，在衍生BOM制作需求和衍生差异信息，点击新增正确填写信息，点击生成BOM，不填写业务评审和业务审核，点击提交，提示：业务评审必填项需填写完整！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_024(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12398884')
        user.input_Derived_info('原始BOM编码', '12106993')
        user.input_Derived_info('原始BOM工厂', 'C105')
        user.click_Derived_differ()
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12398884')
        user.input_Derived_info('操作', '新增物料')
        user.input_Derived_info('处理物料编码', '12105698')
        user.input_Derived_info('数量', '1')
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.click_add_submit()
        user.assert_toast('业务评审必填项需填写完整！')


@allure.feature("BOM协作-PCBA BOM协作")
class TestTheProcessOfExaminationAndApproval:
    @allure.story("流程审批")
    @allure.title("发起流程，审批页面的数据和发起的数据是一致的")
    @allure.description("发起一个PCBA BOM协作，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_001(self, drivers, PCBA_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.enter_onework_check(PCBA_API[0])
        sleep(2)
        info1 = user.get_onework_bominfo('制作类型')
        info2 = user.get_onework_bominfo('品牌')
        info3 = user.get_onework_bominfo('机型')
        info4 = user.get_onework_bominfo('阶段')
        ValueAssert.value_assert_equal(info1, 'PCBA BOM制作')
        ValueAssert.value_assert_equal(info2, 'Infinix')
        ValueAssert.value_assert_equal(info3, 'JMB-01')
        ValueAssert.value_assert_equal(info4, '试产阶段')
        user.assert_oneworks_bomtree_result('PCBA', ('1', 'PCBA', '12100001', 'PCBA_Mainboard_NL01_128MB+64MB_T630S', '可选', '1'), ('1.7', 'IC144', '14400003', 'IC-Gsensor,2axis,8bit,WLCSP6,H1.015', '可选', '5', 'U1001,U1002,U1003,U1004,U1005'))
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("补充工厂页面，审批成功")
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示“处理成功”，并且页面成功跳转，成功处理了补充工厂审核点，我的待办中不存在该条单据在补充工厂审核节点（建议：校验单据号和当前节点）")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_002(self, drivers, PCBA_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_API[0], '补充工厂', True)
        user.enter_oneworks_edit(PCBA_API[0])
        user.input_oneworks_plant_info('国内贴片工厂', '1001')
        user.click_oneworks_slash()
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(PCBA_API[0], '补充工厂')
        user.assert_my_todo_node(PCBA_API[0], '基带工程师审批', True)

    @allure.story("流程审批")
    @allure.title("基带工程师审批，审批成功")
    @allure.description("基带工程师审批页面中，所有数据都正确，点击同意，可以提交成功并给出提示“处理成功，审核通过”，页面成功跳转;成功处理了基带工程师审批节点，我的待办中不存在该条数据在基带工程师审批节点（建议：校验单据号和当前节点）")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_003(self, drivers, PCBA_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Factory_API[0])
        user.select_business_review('李小素', 'all')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(PCBA_Factory_API[0], '基带工程师审批')
        user.assert_my_todo_node(PCBA_Factory_API[0], '采购审核（NPS）', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("基带工程师审批回退到业务审核成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验：单据号和节点）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_004(self, drivers, PCBA_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Factory_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(PCBA_Factory_API[0], '补充工厂', True)

    @allure.story("流程审批")
    @allure.title("在基带工程师审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.description("在基带工程师审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_005(self, drivers, PCBA_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Factory_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("在基带工程师审批页面中，选择转交人转交，存在确定转交按钮")
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_006(self, drivers, PCBA_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("在基带工程师审批页面中，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_007(self, drivers, PCBA_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在基带工程师审批页面中，转交单据成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_008(self, drivers, PCBA_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(PCBA_Factory_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("在基带工程师审批页面中，拒绝成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击拒绝，会显示处理成功，并且页面跳转")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_009(self, drivers, PCBA_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Factory_API[0])
        user.click_oneworks_refuse()
        user.assert_toast('处理成功，审核拒绝')
        user.quit_oneworks()
        user.assert_my_application_flow(PCBA_Factory_API[0], '审批拒绝')
        process_status = user.get_bom_info('PCBA BOM协作', PCBA_Factory_API[0], '单据状态')
        ValueAssert.value_assert_In(process_status, '审批拒绝')

    @allure.story("流程审批")
    @allure.title("采购审核（NPS）页面中，审批成功")
    @allure.description("在采购审核（NPS）页面中，点击同意，可以提交成功并给出提示“处理成功，审核通过”，页面成功跳转;成功处理了采购审核（NPS）节点，我的待办中不存在该条数据在采购审核（NPS）节点（建议：校验单据号和当前节点）")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_010(self, drivers, PCBA_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Structure_API[0])
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(PCBA_Structure_API[0], '采购审核（NPS）')
        user.assert_my_todo_node(PCBA_Structure_API[0], '业务审核', True)

    @allure.story("流程审批")
    @allure.title("采购审核（NPS）页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.description("采购审核（NPS）页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_011(self, drivers, PCBA_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Structure_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("采购审核（NPS）页面中，选择转交人转交，存在确定转交按钮")
    @allure.description("采购审核（NPS）页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_012(self, drivers, PCBA_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Structure_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("采购审核（NPS）页面中，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("采购审核（NPS）页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_013(self, drivers, PCBA_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Structure_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("采购审核（NPS）页面中，转交单据成功")  # 用例名称
    @allure.description("采购审核（NPS）页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_014(self, drivers, PCBA_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Structure_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(PCBA_Structure_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("采购审核（NPS）页面中，拒绝成功")  # 用例名称
    @allure.description("采购审核（NPS）页面中，点击拒绝，会显示处理成功，并且页面跳转")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_015(self, drivers, PCBA_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Structure_API[0])
        user.click_oneworks_refuse()
        user.assert_toast('处理成功，审核拒绝')
        user.quit_oneworks()
        user.assert_my_application_flow(PCBA_Structure_API[0], '审批拒绝')
        process_status = user.get_bom_info('PCBA BOM协作', PCBA_Structure_API[0], '单据状态')
        ValueAssert.value_assert_In(process_status, '审批拒绝')

    @allure.story("流程审批")
    @allure.title("业务审核页面，产成品数据不能编辑")
    @allure.description("在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_016(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.assert_oneworks_bomtree_edit('PCBA', '物料编码')
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核成功")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择通过，添加名字为检查结果的附件，点击同意按钮，给出提示，并且页面跳转成功，跳转成功后，我的待办中不存在该条业务审核单据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_017(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.scroll_self_inspection()
        user.input_self_inspection_result()
        user.click_Accessory()
        user.add_upload_file('检查结果.PNG')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_application_node(PCBA_Purchase_API[0], '数据组审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核页面，回退到补充工厂再审核，还是业务审核节点")  # 用例名称
    @allure.description("在我的待办中审批从业务审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是业务审核节点，而不是BOM工程师节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_018(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(PCBA_Purchase_API[0], '补充工厂', True)
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(PCBA_Purchase_API[0], '业务审核', True)

    @allure.story("流程审批")
    @allure.title("在业务页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.description("在业务页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_019(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("在业务页面中，选择转交人转交，存在确定转交按钮")
    @allure.description("在业务页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_020(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("在业务页面中，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在业务页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_021(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在业务页面中，转交单据成功")  # 用例名称
    @allure.description("在业务页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_022(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(PCBA_Purchase_API[0], '陈月')

    @allure.story("流程审批")
    @allure.title("在数据组审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.description("在数据组审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_023(self, drivers, PCBA_Business_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Business_API[0], '数据组审批', True)
        user.enter_oneworks_edit(PCBA_Business_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("在数据组审核页面中，选择转交人转交，存在确定转交按钮")
    @allure.description("在数据组审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_024(self, drivers, PCBA_Business_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Business_API[0], '数据组审批', True)
        user.enter_oneworks_edit(PCBA_Business_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("在数据组审核页面中，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在数据组审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_025(self, drivers, PCBA_Business_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Business_API[0], '数据组审批', True)
        user.enter_oneworks_edit(PCBA_Business_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在数据组审核页面中，转交单据成功")  # 用例名称
    @allure.description("在数据组审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_026(self, drivers, PCBA_Business_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Business_API[0], '数据组审批', True)
        user.enter_oneworks_edit(PCBA_Business_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(PCBA_Business_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("发起PCBA BOM衍生流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个PCBA BOM衍生，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_027(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '试产阶段')
        user.click_Derived_import()
        user.add_import_file('PCBA衍生BOM制作需求导入模板.xlsx')
        user.click_apply()
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '结构工程师')
        user.select_business_review('李小素', '采购部(NPS)')
        user.select_business_review('李小素', '射频&天线工程师')
        user.select_business_review('李小素', '检查人')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        process_code = user.get_bom_info('PCBA BOM协作', '自动化新增用例', '流程编码')
        user.enter_onework_check(process_code)
        info1 = user.get_onework_bominfo('制作类型')
        info2 = user.get_onework_bominfo('品牌')
        info3 = user.get_onework_bominfo('机型')
        info4 = user.get_onework_bominfo('阶段')
        ValueAssert.value_assert_equal(info1, 'PCBA BOM衍生')
        ValueAssert.value_assert_equal(info2, 'itel')
        ValueAssert.value_assert_equal(info3, 'JMB-01')
        ValueAssert.value_assert_equal(info4, '试产阶段')
        user.assert_oneworks_bomtree_result('PCBA', ('1', 'PCBA', '12398884', 'PCBA_itel_it1655S_M30B_4+512_单卡_SKU4', '1'))
        user.quit_oneworks()
        user.delete_flow(process_code)

    @allure.story("流程审批")
    @allure.title("BOM衍生，补充工厂页面，审批成功")
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示“处理成功”，并且页面成功跳转，成功处理了补充工厂审核点，我的待办中不存在该条单据在补充工厂审核节点（建议：校验单据号和当前节点）")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_028(self, drivers, PCBA_Derived_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_API[0], '补充工厂', True)
        user.enter_oneworks_edit(PCBA_Derived_API[0])
        user.input_oneworks_plant_info('国内贴片工厂', '1001')
        user.click_oneworks_slash()
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(PCBA_Derived_API[0], '补充工厂')
        user.assert_my_todo_node(PCBA_Derived_API[0], '基带工程师审批', True)

    @allure.story("流程审批")
    @allure.title("BOM衍生，在基带工程师审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.description("在基带工程师审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_029(self, drivers, PCBA_Derived_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Factory_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("BOM衍生，在基带工程师审批页面中，选择转交人转交，存在确定转交按钮")
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_030(self, drivers, PCBA_Derived_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("BOM衍生，在基带工程师审批页面中，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_031(self, drivers, PCBA_Derived_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM衍生，在基带工程师审批页面中，转交单据成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_032(self, drivers, PCBA_Derived_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(PCBA_Derived_Factory_API[0], '陈月')

    @allure.story("流程审批")
    @allure.title("BOM衍生，基带工程师审批，审批成功")
    @allure.description("基带工程师审批页面中，所有数据都正确，点击同意，可以提交成功并给出提示“处理成功，审核通过”，页面成功跳转;成功处理了基带工程师审批节点，我的待办中不存在该条数据在基带工程师审批节点（建议：校验单据号和当前节点）")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_033(self, drivers, PCBA_Derived_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Factory_API[0])
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '基带工程师审批')
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '采购审核（NPS）', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM衍生，基带工程师审批回退到业务审核成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验：单据号和节点）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_034(self, drivers, PCBA_Derived_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Factory_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '补充工厂', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM衍生，在基带工程师审批页面中，拒绝成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击拒绝，会显示处理成功，并且页面跳转")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_035(self, drivers, PCBA_Derived_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Factory_API[0])
        user.click_oneworks_refuse()
        user.assert_toast('处理成功，审核拒绝')
        user.quit_oneworks()
        user.assert_my_application_flow(PCBA_Derived_Factory_API[0], '审批拒绝')
        process_status = user.get_bom_info('PCBA BOM协作', PCBA_Derived_Factory_API[0], '单据状态')
        ValueAssert.value_assert_In(process_status, '审批拒绝')

    @allure.story("流程审批")
    @allure.title("BOM衍生，在采购审核（NPS）页面中，审批成功")
    @allure.description("在采购审核（NPS）页面中，点击同意，可以提交成功并给出提示“处理成功，审核通过”，页面成功跳转;成功处理了采购审核（NPS）节点，我的待办中不存在该条数据在采购审核（NPS）节点（建议：校验单据号和当前节点）")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_036(self, drivers, PCBA_Derived_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Derived_Structure_API[0])
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(PCBA_Derived_Structure_API[0], '采购审核（NPS）')
        user.assert_my_todo_node(PCBA_Derived_Structure_API[0], '业务审核', True)

    @allure.story("流程审批")
    @allure.title("BOM衍生，在采购审核（NPS）页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.description("在采购审核（NPS）页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_037(self, drivers, PCBA_Derived_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Derived_Structure_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("BOM衍生，在采购审核（NPS）页面中，选择转交人转交，存在确定转交按钮")
    @allure.description("在采购审核（NPS）页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_038(self, drivers, PCBA_Derived_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Derived_Structure_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("BOM衍生，在采购审核（NPS）页面中，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在采购审核（NPS）页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_039(self, drivers, PCBA_Derived_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Derived_Structure_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM衍生，在采购审核（NPS）页面中，转交单据成功")  # 用例名称
    @allure.description("在采购审核（NPS）页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_040(self, drivers, PCBA_Derived_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Derived_Structure_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(PCBA_Derived_Structure_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM衍生，在采购审核（NPS）页面中，拒绝成功")  # 用例名称
    @allure.description("在采购审核（NPS）页面中，点击拒绝，会显示处理成功，并且页面跳转")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_041(self, drivers, PCBA_Derived_Structure_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Structure_API[0], '采购审核（NPS）', True)
        user.enter_oneworks_edit(PCBA_Derived_Structure_API[0])
        user.click_oneworks_refuse()
        user.assert_toast('处理成功，审核拒绝')
        user.quit_oneworks()
        user.assert_my_application_flow(PCBA_Derived_Structure_API[0], '审批拒绝')
        process_status = user.get_bom_info('PCBA BOM协作', PCBA_Derived_Structure_API[0], '单据状态')
        ValueAssert.value_assert_In(process_status, '审批拒绝')

    @allure.story("流程审批")
    @allure.title("BOM衍生，业务审核页面，产成品数据不能编辑")
    @allure.description("在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_042(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.assert_oneworks_bomtree_edit('PCBA', '物料编码')
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM衍生，业务审核成功")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择通过，添加名字为检查结果的附件，点击同意按钮，给出提示，并且页面跳转成功，跳转成功后，我的待办中不存在该条业务审核单据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_043(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.scroll_self_inspection()
        user.input_self_inspection_result()
        user.click_Accessory()
        user.add_upload_file('检查结果.PNG')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_application_node(PCBA_Derived_Purchase_API[0], '数据组审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM衍生，业务审核页面，回退到补充工厂再审核，还是业务审核节点")  # 用例名称
    @allure.description("在我的待办中审批从业务审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是业务审核节点，而不是BOM工程师节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_044(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(PCBA_Derived_Purchase_API[0], '补充工厂', True)
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(PCBA_Derived_Purchase_API[0], '业务审核', True)

    @allure.story("流程审批")
    @allure.title("BOM衍生，在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.description("在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_045(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("BOM衍生，在业务审核页面中，选择转交人转交，存在确定转交按钮")
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_046(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("BOM衍生，在业务审核页面中，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_047(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM衍生，在业务审核页面中，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_048(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(PCBA_Derived_Purchase_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM衍生，在数据组审批页面中，回退到补充工厂再审核，还是业务审核节点")  # 用例名称
    @allure.description("在我的待办中审批从数据组审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是数据组审核节点，而不是基带工程师审批节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_049(self, drivers, PCBA_Derived_Business_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Business_API[0], '数据组审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Business_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(PCBA_Derived_Business_API[0], '补充工厂', True)
        user.enter_oneworks_edit(PCBA_Derived_Business_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(PCBA_Derived_Business_API[0], '数据组审批', True)

    @allure.story("流程审批")
    @allure.title("BOM衍生，在数据组审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.description("在数据组审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_050(self, drivers, PCBA_Derived_Business_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Business_API[0], '数据组审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Business_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("BOM衍生，在数据组审批页面中，选择转交人转交，存在确定转交按钮")
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_051(self, drivers, PCBA_Derived_Business_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Business_API[0], '数据组审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Business_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("BOM衍生，在数据组审批页面中，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在数据组审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_052(self, drivers, PCBA_Derived_Business_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Business_API[0], '数据组审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Business_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM衍生，在数据组审批页面中，转交单据成功")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_053(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Purchase_API[0], '业务审核', True)
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(PCBA_Derived_Purchase_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查为成功，点击同意，能提交成功，并且给出提交成功的提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip  # 如果需要执行，手动将@pytest.mark.skip注释
    def test_003_054(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        # 数据组审批需要将SAP数据删除，手动删除后，需要填写相关bom信息（品牌，机型，阶段，市场）
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', 'PCBA BOM制作')
        user.input_bom_info('品牌', 'Infinix')
        user.input_bom_info('机型', 'JMB-02')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('制作虚拟贴片/套片', '否')
        user.click_add_bomtree()
        # 填写相关bomTree（BOM状态，物料编码，用量），需要在数据组审批子阶检查通过
        user.input_bomtree('PCBA', 'BOM状态', '试产')
        user.input_bomtree('PCBA', '物料编码', '12100001')
        user.input_bomtree('PCBA', '数量', '1')
        user.input_bomtree('IC144', '物料编码', '14400003')
        user.input_bomtree('IC144', '数量', '1')
        user.input_bomtree('IC144', '位号', 'U1001')
        user.select_business_review('李小素')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        process_code = user.get_bom_info('PCBA BOM协作', '自动化新增用例', '流程编码')
        user.supplement_bom_flow(process_code)
        user.supplementary_factory_flow(process_code)
        user.Structure_flow(process_code)
        user.Purchase_flow(process_code)
        user.business_approve_flow(process_code)
        user.enter_oneworks_edit(process_code)
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_application_node(process_code, '审批通知', True)
        sleep(60)
        user.assert_my_application_flow(process_code, '审批完成')
        process_status = user.get_bom_info('外研BOM协作', '自动化新增用例', '单据状态')
        ValueAssert.value_assert_equal(process_status, '审批通过')

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM，数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查为成功，点击同意，能提交成功，并且给出提交成功的提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip  # 如果需要执行，手动将@pytest.mark.skip注释
    def test_003_055(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        # 数据组审批需要将SAP数据删除，手动删除后，需要填写相关bom信息（品牌，机型，阶段，市场）
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', '客供BOM衍生')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'JMB-01')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.input_bom_info('模式', '零价值客供')
        # 填写相关衍生信息，需要在数据组审批子阶检查通过
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12000003')
        user.input_Derived_info('原始BOM编码', '12014351')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.click_Derived_differ()
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12000003')
        user.input_Derived_info('操作', '新增物料')
        user.input_Derived_info('处理物料编码', '12800001')
        user.input_Derived_info('用量', '1000')
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.click_refresh()
        user.select_business_review(user.review, 'PPM')
        user.select_business_review(user.review, 'QPM')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        process_code = user.get_bom_info('外研BOM协作', '自动化新增用例', '流程编码')
        user.business_approve_flow(process_code)
        user.enter_oneworks_edit(process_code)
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_application_node(process_code, '审批通知', True)
        sleep(60)
        user.assert_my_application_flow(process_code, '审批完成')
        process_status = user.get_bom_info('外研BOM协作', '自动化新增用例', '单据状态')
        ValueAssert.value_assert_equal(process_status, '审批通过')


@allure.feature("BOM协作-PCBA BOM协作")
class TestProcessApprovalExceptionScenario:
    @allure.story("流程审批异常场景")
    @allure.title("【生产工厂信息】物料xxxxxx的组包工厂不能为空")
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示【生产工厂信息】物料xxxxxx的贴片工厂不能为空")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_001(self, drivers, PCBA_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_API[0])
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('【生产工厂信息】物料12100001的贴片工厂不能为空')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("未选择BOM,一键填写按钮无法被点击")
    @allure.description("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_002(self, drivers, PCBA_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_API[0])
        user.assert_oneworks_onepress_write()
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("请选择工厂分类/请选择工厂")
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，直接点击确认，不能进行确认并给出必填提示“请选择工厂分类”、“请选择工厂”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_003(self, drivers, PCBA_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_API[0])
        user.click_Factory_checkbox()
        user.click_oneworks_onepress_write()
        user.click_oneworks_onepress_write_confirm()
        DomAssert(drivers).assert_att('请选择工厂分类')
        DomAssert(drivers).assert_att('请选择工厂')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("检查贴片工厂不能为空！")
    @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示检查贴片工厂不能为空！")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_004(self, drivers, PCBA_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_API[0])
        user.input_oneworks_plant_info('国内贴片工厂', '1001')
        user.click_oneworks_slash()
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('检查贴片工厂不能为空！')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("检查贴片工厂不能为空！")
    @allure.description("在补充工厂页面中，不填写贴片工厂直接点击一键/，给出提示XXX物料必填一个贴片工厂")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_005(self, drivers, PCBA_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_API[0])
        user.click_oneworks_slash()
        user.assert_toast('121物料必填一个贴片工厂')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("14400003的数量和位号个数不一致")
    @allure.description("在基带工程师审批页面中，点击编辑，将14400003数量改为1，点击同意，提示“14400003的数量和位号个数不一致”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_006(self, drivers, PCBA_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Factory_API[0])
        user.click_tree('PCBA')
        user.input_bomtree('IC144', '数量', '1')
        user.select_business_review('李小素', 'all')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('14400003的数量和位号个数不一致')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("业务审核的必填项需填写完整！")
    @allure.description("在基带工程师审批页面中，业务审核不选择人，点击同意，提示“业务审核的必填项需填写完整！”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_007(self, drivers, PCBA_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Factory_API[0])
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('业务审核的必填项需填写完整！')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单检查角色未选择")  # 用例名称
    @allure.description("在业务审核页面中，不填写任何内容，点击同意，不能提交成功，并给出提示“自检清单检查角色未选择”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_008(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        DomAssert(drivers).assert_att('自检清单检查角色未选择')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单第【1】行检查结果未选择")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，选择后直接点击同意，不能提交成功，并给出提示“自检清单第【1】行检查结果未选择”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_009(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.click_Accessory()
        user.add_upload_file('检查结果.PNG')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果未选择')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择不通过，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不通过需填写原因及修改建议")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_010(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.scroll_self_inspection()
        user.input_self_inspection_result(result='不通过')
        user.click_Accessory()
        user.add_upload_file('检查结果.PNG')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果为不通过需填写原因及修改建议')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择不涉及，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不涉及需填写原因及修改建议")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_011(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.scroll_self_inspection()
        user.input_self_inspection_result(result='不涉及')
        user.click_Accessory()
        user.add_upload_file('检查结果.PNG')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果为不涉及需填写原因及修改建议')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自请上传检查结果")  # 用例名称
    @allure.description("在业务审核页面中，正确填写自检清单，不添加附件，点击同意，提示“请上传检查结果”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_012(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.scroll_self_inspection()
        user.input_self_inspection_result()
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('请上传检查结果')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("只能上传文件名为‘检查结果’的文件")  # 用例名称
    @allure.description("在业务审核页面中，正确填写自检清单，添加名字不为检查结果的附件，提示“只能上传文件名为‘检查结果’的文件”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_013(self, drivers, PCBA_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.scroll_self_inspection()
        user.input_self_inspection_result()
        user.click_Accessory()
        user.add_upload_file('worng_file_text.txt')
        user.assert_toast('只能上传文件名为‘检查结果’的文件')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("数据组审批页面，检查失败项不为0，提交失败")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查有失败项，点击同意，不能提交成功，并且给出提交失败的提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_014(self, drivers, PCBA_Business_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Business_API[0])
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('bom检查失败，无法同步')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("BOM衍生，【生产工厂信息】物料xxxxxx的贴片工厂不能为空")
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示“【生产工厂信息】物料xxxxxxxx的贴片工厂不能为空”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_015(self, drivers, PCBA_Derived_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_API[0], '补充工厂', True)
        user.enter_oneworks_edit(PCBA_Derived_API[0])
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('【生产工厂信息】物料12198883的贴片工厂不能为空')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("BOM衍生，未选择BOM,一键填写按钮无法被点击")
    @allure.description("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_016(self, drivers, PCBA_Derived_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_API[0])
        user.assert_oneworks_onepress_write()
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("BOM衍生，请选择工厂分类/请选择工厂")
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，直接点击确认，不能进行确认并给出必填提示“请选择工厂分类”、“请选择工厂”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_017(self, drivers, PCBA_Derived_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_API[0])
        user.click_Factory_checkbox()
        user.click_oneworks_onepress_write()
        user.click_oneworks_onepress_write_confirm()
        DomAssert(drivers).assert_att('请选择工厂分类')
        DomAssert(drivers).assert_att('请选择工厂')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("BOM衍生，检查贴片工厂不能为空！")
    @allure.description("在补充工厂页面中，不填写贴片工厂直接点击一键/，给出提示XXX物料必填一个贴片工厂")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_018(self, drivers, PCBA_Derived_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_API[0])
        user.click_oneworks_slash()
        user.assert_toast('121物料必填一个贴片工厂')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("BOM衍生，检查贴片工厂不能为空！")
    @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示检查贴片工厂不能为空！")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_019(self, drivers, PCBA_Derived_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_API[0])
        user.input_oneworks_plant_info('国内贴片工厂', '1001')
        user.click_oneworks_slash()
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('检查贴片工厂不能为空！')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("BOM衍生，BOM[XXXXXXX]中的物料[XXXXXXX]位号个数与数量不一致，请检查后提交")  # 用例名称
    @allure.description("在基带工程师审批页面中，衍生差异信息中位号填多个，将BOM数量改为1，点击生成BOM，提示“BOM[XXXXXXX]中的物料[XXXXXXX]位号个数与数量不一致，请检查后提交”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_020(self, drivers, PCBA_Derived_Factory_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(PCBA_Derived_Factory_API[0], '基带工程师审批', True)
        user.enter_oneworks_edit(PCBA_Derived_Factory_API[0])
        user.click_Derived_differ()
        user.input_Derived_info('位号', 'C1,C2')
        user.click_Creat_BOM()
        user.assert_toast('BOM[12198883]中的物料[12105695]位号个数与数量不一致，请检查后提交')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("BOM衍生，自检清单检查角色未选择")  # 用例名称
    @allure.description("在业务审核页面中，不填写任何内容，点击同意，不能提交成功，并给出提示“自检清单检查角色未选择”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_021(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        DomAssert(drivers).assert_att('自检清单检查角色未选择')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("BOM衍生，自检清单第【1】行检查结果未选择")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，选择后直接点击同意，不能提交成功，并给出提示“自检清单第【1】行检查结果未选择”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_022(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.click_Accessory()
        user.add_upload_file('检查结果.PNG')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果未选择')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("BOM衍生，自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择不通过，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不通过需填写原因及修改建议")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_023(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.scroll_self_inspection()
        user.input_self_inspection_result(result='不通过')
        user.click_Accessory()
        user.add_upload_file('检查结果.PNG')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果为不通过需填写原因及修改建议')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("BOM衍生，自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择不涉及，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不涉及需填写原因及修改建议")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_024(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.scroll_self_inspection()
        user.input_self_inspection_result(result='不涉及')
        user.click_Accessory()
        user.add_upload_file('检查结果.PNG')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果为不涉及需填写原因及修改建议')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("BOM衍生，自请上传检查结果")  # 用例名称
    @allure.description("在业务审核页面中，正确填写自检清单，不添加附件，点击同意，提示“请上传检查结果”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_025(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.scroll_self_inspection()
        user.input_self_inspection_result()
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('请上传检查结果')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("BOM衍生，只能上传文件名为‘检查结果’的文件")  # 用例名称
    @allure.description("在业务审核页面中，正确填写自检清单，添加名字不为检查结果的附件，提示“只能上传文件名为‘检查结果’的文件”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_026(self, drivers, PCBA_Derived_Purchase_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_Purchase_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '检查人')
        user.scroll_self_inspection()
        user.input_self_inspection_result()
        user.click_Accessory()
        user.add_upload_file('worng_file_text.txt')
        user.assert_toast('只能上传文件名为‘检查结果’的文件')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("BOM衍生，数据组审批页面，检查失败项不为0，提交失败")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查有失败项，点击同意，不能提交成功，并且给出提交失败的提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_027(self, drivers, PCBA_Derived_Business_API):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(PCBA_Derived_Business_API[0])
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('bom检查失败，无法同步')
        user.quit_oneworks()


@allure.feature("BOM协作-PCBA BOM协作")  # 模块名称
class TestProcessSearch:

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，标题查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入“李小素”，点击查询，查询结果为所有标题包含“李小素”的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_001(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '李小素')
        user.click_search()
        user.assert_search_result('标题', '李小素')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，查询不存在标题，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的标题，点击查询，查询结果为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_002(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', 'sfdasdfwefw')
        user.click_search()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，流程编码查询结果正确")  # 用例名称
    @allure.description("在查询页面，流程编码输入框输入“1”，点击查询，查询结果为所有流程编码包含“1”的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_003(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('流程编码', '1')
        user.click_search()
        user.assert_search_result('流程编码', '1')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，查询不存在流程编码，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的流程编码，点击查询，查询结果为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_004(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('流程编码', 'sfdasdfwefw')
        user.click_search()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，PCBA BOM衍生查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为客供BOM衍生，点击查询，查询结果为所有制作类型为PCBA BOM衍生的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_005(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', 'PCBA BOM衍生')
        user.click_search()
        user.assert_search_result('制作类型', 'PCBA BOM衍生')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，PCBA BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为PCBA BOM制作，点击查询，查询结果为所有制作类型为PCBA BOM制作的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_006(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', 'PCBA BOM制作')
        user.click_search()
        user.assert_search_result('制作类型', 'PCBA BOM制作')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，组合查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入“李小素”，流程编码输入框输入“1”，BOM编码输入“2”，下拉框选择为PCBA BOM制作，点击查询，查询结果为所有标题包含“李小素”、流程编码包含“1”、物料编码包含“2”、制作类型为PCBA BOM制作的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_007(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '李小素')
        user.input_search_info('流程编码', '1')
        user.input_search_info('制作类型', 'PCBA BOM制作')
        user.click_search()
        user.assert_search_result('制作类型', 'PCBA BOM制作')
        user.assert_search_result('流程编码', '1')
        user.assert_search_result('标题', '李小素')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，编辑正常")  # 用例名称
    @allure.description("在查询页面，点击编辑，跳转至oneworks编辑页面，可以编辑页面信息、提交、保存")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记

    def test_005_008(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '自动化查询用例')
        user.click_search()
        user.click_edit('自动化查询用例')
        user.select_business_review('李小素', 'all')
        user.click_add_save()
        DomAssert(drivers).assert_att('保存草稿成功')
        user.click_edit('自动化查询用例')
        user.select_business_review('李小素', 'all')
        user.click_add_submit()
        DomAssert(drivers).assert_att('创建流程成功')
        user.input_search_info('标题', '自动化查询用例')
        user.click_search()
        code = user.get_bom_info('PCBA BOM协作', '自动化查询用例', '流程编码')
        user.recall_process(code)

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，删除取消无变动")  # 用例名称
    @allure.description("在查询页面，点击删除，提示是否确认删除，点击取消，取消成功，页面无变动")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_009(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '自动化查询用例')
        user.click_search()
        user.click_delete('自动化查询用例')
        user.click_dialog_cancel()
        DomAssert(drivers).assert_att('自动化查询用例')


if __name__ == '__main__':
    pytest.main(['BOMCooperation_PCBABomCooperation.py'])
