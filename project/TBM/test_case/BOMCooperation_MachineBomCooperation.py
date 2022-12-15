import pytest
from public.base.assert_ui import *
from project.TBM.page_object.BOMCooperation_MachineBomCooperation import MachineBOMCollaboration


@allure.feature("BOM协作-整机BOM协作")  # 模块名称
class TestCreateProcess:

    @allure.story("创建流程")  # 场景名称
    @allure.title("创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，能提交成功，创建流程成功")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', '生产BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', '10018956')
        user.input_bomtree('产成品', '用量', '1000')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', 'NPS')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "整机BOM协作", '生产BOM', 'X572-1', 'itel', '埃塞本地', '试产阶段', '审批中', '未同步')
        process_code = user.get_info("BOM协作", "整机BOM协作")[1]
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("新增物料，创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，在充电器中新增两颗物料，添加替代组都为A1，份额为一个20，一个80，其他内容正确填写，点击提交，能提交成功并且提示创建流程成功")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.add_bomtree()
        user.input_bomtree('充电器', '物料编码', '25101424')
        user.input_bomtree('充电器', '用量', '1000')
        user.input_bomtree('充电器', '替代组', 'A1')
        user.input_bomtree('充电器', '份额', '20')
        user.click_add_material()
        user.input_add_material('25101424', '物料编码', '25101448')
        user.input_add_material('25101424', '用量', '1000')
        user.input_add_material('25101424', '替代组', 'A1')
        user.input_add_material('25101424', '份额', '80')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', 'NPS')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "整机BOM协作", '生产BOM', 'X572-1', 'Infinix', '埃塞本地', '试产阶段', '审批中', '未同步')
        process_code = user.get_info("BOM协作", "整机BOM协作")[1]
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("正确选择物料编码，点击一键填写，填写内容保存正确")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产成品中和单机头中正确选择物料编码，选中两颗物料，点击一键填写，填写用量和1000点击确认，页面上显示两颗物料用量都为1000")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_001_003(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', '10000010')
        user.input_bomtree('单机头', '物料编码', '10000011')
        user.click_BOMTree_checkbox()
        user.input_OnePress('用量', '1000')
        amount1 = user.get_bomtree_info('产成品', '用量')
        amount2 = user.get_bomtree_info('产成品', '用量')
        ValueAssert.value_assert_equal(amount1, '1000')
        ValueAssert.value_assert_equal(amount2, '1000')

    @allure.story("创建流程")  # 场景名称
    @allure.title("BOM tree中不选择物料，页面上不存在删除按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不选择物料，页面上不存在删除按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_001_004(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.assert_batch_delete(False)

    @allure.story("创建流程")  # 场景名称
    @allure.title("BOM tree中选择物料，页面上存在删除按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择物料，页面上存在删除按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_001_005(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_BOMTree_checkbox()
        user.assert_batch_delete(True)

    @allure.story("创建流程")  # 场景名称
    @allure.title("选中父节点物料后点击删除，删除页面数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_001_006(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', '10000010')
        user.click_BOMTree_checkbox()
        user.click_batch_delete()
        user.click_batch_confirm()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("创建流程")  # 场景名称
    @allure.title("选中子节点物料后点击删除，清子节点内容")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_001_007(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('充电器', '物料编码', '10000011')
        user.input_bomtree('充电器', '用量', '1000')
        user.input_bomtree('充电器', '替代组', 'A1')
        user.input_bomtree('充电器', '份额', '20')
        user.click_BOMTree_checkbox('充电器', 'Tree')
        user.click_batch_delete()
        user.click_batch_confirm()
        ValueAssert.value_assert_equal(user.get_bomtree_info('充电器', '物料编码'), '')
        ValueAssert.value_assert_equal(user.get_bomtree_info('充电器', '用量'), '')
        ValueAssert.value_assert_equal(user.get_bomtree_info('充电器', '替代组'), '')
        ValueAssert.value_assert_equal(user.get_bomtree_info('充电器', '份额'), '')

    @allure.story("创建流程")  # 场景名称
    @allure.title("复制审批人成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，正确填入数据后，在审核人设置中点击复制审批人，会弹出选择单据号页面，查询结果正确显示，并且选择生效")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_001_008(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_copy_review()
        user.doc_num_search('单据号', 'ZBOM20220824071208114316')
        user.doc_num_search('机型名称', 'X572-1')
        user.click_search()
        user.assert_doc_result('ZBOM20220824071208114316', 'X572-1')
        user.click_doc_select('ZBOM20220824071208114316')
        user.assert_doc_copy('李小素', 'MPM')
        user.assert_doc_copy('李小素', 'NPS')

    @allure.story("创建流程")  # 场景名称
    @allure.title("衍生BOM,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，填写BOM信息，在衍生BOM列表点击新增并正确填写信息，填写审核人设置，点击提交，能提交成功“创建流程成功”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_009(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_add()
        user.input_Derived_info('新BOM类型', '发货BOM')
        user.input_Derived_info('新BOM编码', '11000002')
        user.input_Derived_info('原始BOM编码', '10026373')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '音频')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "整机BOM协作", '衍生BOM', 'X572-1', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_info("BOM协作", "整机BOM协作")[1]
        user.delete_flow(process_code)

    @allure.story("创建流程")
    @allure.title("衍生BOM，选择正确的文件进行导入，创建流程成功")
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，填写业务评审和业务审核，点击提交，提交成功并流程发起成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_010(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_import()
        user.add_import_file('衍生bom项目经理导入模板.xls')
        user.assert_import_success()
        user.assert_upload_result(('1', '发货BOM', '11000002', 'CKD_itel_A44_F3706_玫瑰金_IN_BCFL_8+1_P05_E', '10026373', '整机_Infinix_PR652C_F6319_B1_海洋之心32+2_欧规_Ⅰ', 'PL01'),)
        user.click_apply()
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '音频')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "整机BOM协作", '衍生BOM', 'X572-1', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_info("BOM协作", "整机BOM协作")[1]
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("导入-简易模式选择正确的文件进行导入成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入-简易模式选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_001_011(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_simple_import()
        user.add_import_file('生产BOM项目经理简易模式导入.xls')
        user.assert_import_success()
        user.assert_upload_result(('国内生产BOM', '试产', '10000010', '1单机头(无卡)1移动电源1充电器1数据线1耳机1皮套1套包材', '12000002', '单机头_TECNO_T722_E680B1_白色_4G', '2000'), ('国内生产BOM', '试产', '10000010', '1单机头(无卡)1移动电源1充电器1数据线1耳机1皮套1套包材', '12000001', '单机头_TECNO_T722_E680B1_咖啡色_4G', '1000'))
        user.click_apply()
        user.click_tree('产成品')
        user.assert_tree_result(('1', '产成品', '10000010', '1单机头(无卡)1移动电源1充电器1数据线1耳机1皮套1套包材', '可选', '1000', '编辑删除'), ('1.1.1', '12000001', '单机头_TECNO_T722_E680B1_咖啡色_4G', '可选', '1000', '编辑删除'), ('1.1.2', '12000002', '单机头_TECNO_T722_E680B1_白色_4G', '可选', '2000', '编辑删除'))

    @allure.story("创建流程")  # 场景名称
    @allure.title("导入选择正确的文件进行导入成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_001_012(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', '生产BOM')
        user.input_bom_info('品牌', 'Infinix')
        user.input_bom_info('机型', '1005G1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '孟加拉')
        user.click_bom_import()
        user.add_import_file('生产bom项目经理导入模板.xlsx')
        # user.assert_import_success()
        user.assert_upload_result(('1', '10000010', '1单机头(无卡)1移动电源1充电器1数据线1耳机1皮套1套包材', '未归档', '1', '国内生产BOM', '量产', '孟加拉', '16+1', '12000001'), )
        user.click_apply()
        user.click_tree('产成品')
        user.assert_tree_result(('1', '产成品', '10000010', '1单机头(无卡)1移动电源1充电器1数据线1耳机1皮套1套包材', '可选', '编辑删除'), )

    @allure.story("创建流程")  # 场景名称
    @allure.title("衍生BOM，导入选择正确的文件进行导入成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，点击附件中的加号，上传正确的文件，文件上传成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_001_013(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.add_upload_file('检查结果.PNG')
        user.assert_upload('检查结果.PNG')


@allure.feature("BOM协作-整机BOM协作")  # 模块名称
class TestCreateProcessExceptionScenario:

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("请完善Bom信息！")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个不存在模板的品牌，其他内容正确填写，点击提交，不能提交成功并给出提示请完善Bom信息！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', '生产BOM')
        user.input_bom_info('品牌', 'aaaaa')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_add_submit()
        user.assert_toast('请完善Bom信息！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("产成品必须有物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不添加BOM内容，其他内容正确填写，点击提交，不能提交成功并给出提示产成品必须有物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_002(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_add_submit()
        user.assert_toast('产成品必须有物料')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM类型不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不选择BOM类型，正确填写物料编码等其他内容，点击提交，不能提交成功并给出提示BOM类型不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_003(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', '10000010')
        user.input_bomtree('产成品', '用量', '1000')
        user.click_add_submit()
        user.assert_toast('BOM类型不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不选择BOM状态，正确填写物料编码等其他内容，点击提交，不能提交成功并给出提示BOM状态不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_004(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', '物料编码', '10000010')
        user.input_bomtree('产成品', '用量', '1000')
        user.click_add_submit()
        user.assert_toast('BOM状态不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("含有物料的节点，用量不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量不进行填写，点击提交，不能提交成功并给出提示含有物料的节点，用量不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_005(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', '10000010')
        user.click_add_submit()
        user.assert_toast('含有物料的节点，用量不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("父阶BOM料号XXXXXXXX用量不为1000")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1，点击提交，不能提交成功并给出提示父阶BOM料号10000001用量不为1000")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_006(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        code = '10018959'
        user.input_bomtree('产成品', '物料编码', code)
        user.input_bomtree('产成品', '用量', '1')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', 'NPS')
        user.click_add_submit()
        user.assert_toast(f'父阶BOM料号{code}用量不为1000')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("用量只能填写非数字（最多3位小数）")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为非数字类型，点击提交，不能提交成功并给出提示用量只能填写非数字（最多3位小数）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_007(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', '10000010')
        user.input_bomtree('产成品', '用量', 'acb')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', 'NPS')
        user.click_add_submit()
        user.assert_toast('用量只能填写非0数字(最多3位小数)')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx用量不为1000")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，选择单机头的物料编码，输入单机头用量为1，点击提示，不能提交成功并给出提示父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx用量不为1000")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_008(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        f_code, s_code = '10018959', '10000012'
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', f_code)
        user.input_bomtree('产成品', '用量', '1000')
        user.input_bomtree('单机头', '物料编码', s_code)
        user.input_bomtree('单机头', '用量', '1')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', 'NPS')
        user.click_add_submit()
        user.assert_toast(f'父阶BOM料号{f_code}下的子阶BOM料号{s_code}用量不为1000')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("业务评审MPM不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示业务评审MPM不能为空！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_009(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', '10000010')
        user.input_bomtree('产成品', '用量', '1')
        user.select_business_review('李小素', 'NPS')
        user.click_add_submit()
        user.assert_toast('业务评审MPM不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("业务审核至少要选中一个")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，业务审核不选择相应的审核人员，点击提交，不能提交成功，并给出提示业务审核至少要选中一个！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_010(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', '10000010')
        user.input_bomtree('产成品', '用量', '1')
        user.select_business_review('李小素', 'MPM')
        user.click_add_submit()
        user.assert_toast('业务审核至少要选中一个！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("[国内生产BOM][XXXXXXXX] 替代组[A1]的份额总和不为100")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，在充电器中新增两颗物料，添加替代组都为A1，份额为一个20，一个20，其他内容正确填写，点击提交，不能提交成功并且提示[国内生产BOM][XXXXXXXX] 替代组[A1]的份额总和不为100")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_011(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        f_code = '10000010'
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', f_code)
        user.input_bomtree('产成品', '用量', '1000')
        user.input_bomtree('充电器', '物料编码', '10000011')
        user.input_bomtree('充电器', '用量', '1000')
        user.input_bomtree('充电器', '替代组', 'A1')
        user.input_bomtree('充电器', '份额', '20')
        user.click_add_material()
        user.input_add_material('10000011', '物料编码', '10000012')
        user.input_add_material('10000011', '用量', '1000')
        user.input_add_material('10000011', '替代组', 'A1')
        user.input_add_material('10000011', '份额', '20')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', 'NPS')
        user.click_add_submit()
        user.assert_toast(f'[国内生产BOM][{f_code}] 替代组[A1]的份额总和不为100')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("填入产成品数据，不选择物料，一键填写用量，页面上没有填写上任何数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，不选择物料，点击一键填写，填写用量为1000，点击确定，页面上没有填写上任何数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_012(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', '10000010')
        user.input_OnePress('用量', '1000')
        amount = user.get_bomtree_info('产成品', '用量')
        ValueAssert.value_assert_equal(amount, '')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("不填写产成品数据，全选一键填写用量，页面上没有填写上任何数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产成品中不选择物料编码，全选选中物料，点击一键填写，一键填写时选择用量和1000，点击确定，页面上不会新增用量数量")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_013(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_BOMTree_checkbox()
        user.input_OnePress('用量', '1000')
        amount = user.get_bomtree_info('产成品', '用量')
        ValueAssert.value_assert_equal(amount, '')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("一键填写，不填写内容提示为“不能为空”")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产成品中和单机头中正确选择物料编码，选中两颗物料，点击一键填写，选择用量，并且不填写字段值，点击确认，给出必填提示，提示为不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_014(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.add_bomtree()
        user.click_BOMTree_checkbox()
        user.input_OnePress('用量', '')
        DomAssert(drivers).assert_att('不能为空')
        user.click_OnePress_cancel()

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("[XXXXX] 替代组[XX]只有一颗物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入数据，新增一颗物料，添加替代组为A1，份额为20，其他内容正确填写，点击提交，不能提交成功并且提示替代组只有一颗物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_015(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.add_bomtree()
        user.input_bomtree('充电器', '物料编码', '10018955')
        user.input_bomtree('充电器', '用量', '1000')
        user.input_bomtree('充电器', '替代组', 'A1')
        user.input_bomtree('充电器', '份额', '20')
        user.click_add_submit()
        user.assert_toast('[国内生产BOM][10018955] 替代组[A1]只有一颗物料')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("衍生BOM,请完善Bom信息！")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个不存在模板的品牌，其他内容正确填写，点击提交，不能提交成功并给出提示“请完善Bom信息！”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_016(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'aaaaa')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_add()
        user.input_Derived_info('新BOM类型', '发货BOM')
        user.input_Derived_info('新BOM编码', '11000002')
        user.input_Derived_info('原始BOM编码', '10026373')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.click_add_submit()
        user.assert_toast('请完善Bom信息！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("衍生BOM,衍生BOM列表不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，不添加BOM内容，其他内容正确填写，点击提交，不能提交成功并给出提示衍生BOM列表不能为空！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_017(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_add_submit()
        user.assert_toast('衍生BOM列表不能为空！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("衍生BOM,【衍生BOM列表】新BOM类型不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，不添加BOM内容，其他内容正确填写，点击提交，不能提交成功并给出提示【衍生BOM列表】新BOM类型不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_018(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '11000002')
        user.input_Derived_info('原始BOM编码', '10026373')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.click_add_submit()
        user.assert_toast('【衍生BOM列表】新BOM类型不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("衍生BOM,业务评审MPM不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示“业务评审MPM不能为空！”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_019(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_add()
        user.input_Derived_info('新BOM类型', '发货BOM')
        user.input_Derived_info('新BOM编码', '11000002')
        user.input_Derived_info('原始BOM编码', '10026373')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.click_add_submit()
        user.assert_toast('业务评审MPM不能为空！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("衍生BOM,业务审核至少要选中一个！")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，正确填入产成品数据，业务审核不选择相应的审核人员，点击提交，不能提交成功，并给出提示业务审核至少要选中一个！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_020(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_add()
        user.input_Derived_info('新BOM类型', '发货BOM')
        user.input_Derived_info('新BOM编码', '11000002')
        user.input_Derived_info('原始BOM编码', '10026373')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.select_business_review('李小素', 'MPM')
        user.click_add_submit()
        user.assert_toast('业务审核至少要选中一个！')

    @allure.story("创建流程异常场景")
    @allure.title("衍生BOM，文件类型非excel!")
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示“文件类型非excel!”")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_021(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_import()
        user.add_import_file('worng_file_text.txt')
        DomAssert(drivers).assert_att('文件类型非excel!')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("正确内容错误的文件进行导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_022(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_bom_import()
        user.add_import_file('生产bom项目经理导入模板错误内容.xlsx')
        user.assert_import_fail()
        user.assert_wrongcontent_upload_result()

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("导入-简易模式选择错误文件提示文件类型非excel!")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入-简易模式选择一个错误的文件格式进行导入，不能导入成功并提示文件类型非excel!")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_023(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_simple_import()
        user.add_import_file('worng_file_text.txt')
        user.assert_toast('文件类型非excel!')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("导入-简易模式选择内容错误的文件进行导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入-简易模式选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_024(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_simple_import()
        user.add_import_file('生产BOM项目经理简易模式导入错误内容.xls')
        user.assert_import_fail()
        user.assert_wrongcontent_upload_result()

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("选择错误文件导入提示文件类型非excel!")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示文件类型非excel!")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_025(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        sleep(1)
        user.click_bom_import()
        user.add_import_file('worng_file_text.txt')
        user.assert_toast('文件类型非excel!')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("衍生BOM，选择内容错误的文件进行导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_026(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_import()
        user.add_import_file('衍生bom错误模板项目经理导入模板.xls')
        user.assert_import_fail()
        user.assert_wrongcontent_upload_result()


@allure.feature("BOM协作-整机BOM协作")  # 模块名称
class TestTheProcessOfExaminationAndApproval:

    @allure.story("流程审批")  # 场景名称
    @allure.title("发起流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个整机生产BOM，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_001(self, drivers, Machine_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.enter_onework_check(Machine_API[0])
        info1 = user.get_onework_bominfo('制作类型')
        info2 = user.get_onework_bominfo('品牌')
        info3 = user.get_onework_bominfo('机型')
        info4 = user.get_onework_bominfo('阶段')
        info5 = user.get_onework_bominfo('市场')
        ValueAssert.value_assert_equal(info1, '生产BOM')
        ValueAssert.value_assert_equal(info2, 'itel')
        ValueAssert.value_assert_equal(info3, 'X572-1')
        ValueAssert.value_assert_equal(info4, '试产阶段')
        ValueAssert.value_assert_equal(info5, '埃塞本地')
        user.assert_oneworks_bomtree_result('产成品', ('1', '产成品', '10026418', '整机_Infinix_X695D_H854_N1_7度紫_PH_128+8_Ⅰ', '可选', '1000'), )
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在补充工厂页面，审批成功")  # 用例名称
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示“处理成功”，页面成功跳转，成功处理了补充工厂审核点，我的待办中不存在该条单据在补充工厂审核节点（建议：校验单据号和当前节点）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_002(self, drivers, Machine_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_API[0])
        user.input_oneworks_plant_info('国内组包工厂', '1051')
        user.click_oneworks_slash()
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(Machine_API[0], '补充工厂')

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，审批成功并给出提示“处理成功，审核通过”")  # 用例名称
    @allure.description("在BOM工程师页面中，所有数据都正确，点击同意，可以提交成功并给出提示“处理成功，审核通过”，页面成功跳转；成功处理了BOM工程师审核点，我的待办中不存在该条单机在BOM工程师审核节点（建议：校验单据号和当前节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_003(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(Machine_Factory_API[0], 'BOM工程师审批')

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，点击一键填写按钮，能弹出一键填写的页面")  # 用例名称
    @allure.description("在BOM工程师页面中，点击一键填写按钮，能弹出一键填写的页面")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_004(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_one_press()
        DomAssert(drivers).assert_exact_att('一键填写')
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，回退到补充工厂页面")  # 用例名称
    @allure.description("在BOM工程师页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验：单据号和节点）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_005(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(Machine_Factory_API[0], 'BOM工程师审批')
        user.assert_my_todo_node(Machine_Factory_API[0], '补充工厂', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，转交时不选择转交人，不存在确定转交按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_006(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_007(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，选择转交人转交后取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_008(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，转交单据成功")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_009(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(Machine_Factory_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，拒绝成功")  # 用例名称
    @allure.description("在BOM工程师页面中，点击拒绝，会显示处理成功，并且页面跳转")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_010(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_oneworks_refuse()
        user.assert_toast('处理成功，审核拒绝')
        user.quit_oneworks()
        user.assert_my_application_flow(Machine_Factory_API[0], '审批拒绝')
        # process_status = user.get_info()[7]
        process_status = user.get_bom_info('整机BOM协作', Machine_Factory_API[0], '单据状态')
        ValueAssert.value_assert_equal(process_status, '审批拒绝')

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核页面，产成品数据不能编辑")  # 用例名称
    @allure.description("在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_011(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.assert_oneworks_bomtree_edit('产成品', '物料编码')
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核成功")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择通过，点击同意按钮，给出提示，并且页面跳转成功，跳转成功后，我的待办中不存在该条业务审核单据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_012(self, drivers, Machine_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.supplementary_factory_flow(Machine_API[0])
        user.engineer_approve_flow(Machine_API[0])
        user.enter_oneworks_edit(Machine_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '音频')
        user.scroll_self_inspection()
        user.input_self_inspection_result()
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_application_node(Machine_API[0], '数据组审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核回退到补充工厂成功")  # 用例名称
    @allure.description("在业务审核页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验：单据号和节点）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_013(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(Machine_bomEnginner_API[0], '补充工厂', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核回退到补充工厂重新审核，下一节点是业务审核")  # 用例名称
    @allure.description("在我的待办中审批从业务审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是业务审核节点，而不是BOM工程师节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_014(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.quit_oneworks()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(Machine_bomEnginner_API[0], '业务审核', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("在业务审核页面，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_015(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在业务审核页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_016(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在业务审核页面，选择转交人转交后取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_017(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在业务审核页面，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_018(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.quit_oneworks()
        user.assert_flow_deliver(Machine_bomEnginner_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM/状态/物料检查为成功，点击同意，能提交成功，并且给出提交成功的提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip  # 如果需要执行，手动将@pytest.mark.skip注释
    def test_003_019(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        # 数据组审批需要将SAP数据删除，手动删除后，需要填写相关bom信息（品牌，机型，阶段，市场），修改下面方法第二个字串就好
        user.input_bom_info('制作类型', '生产BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '试产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_add_bomtree()
        # 填写相关bomTree（BOM类型，BOM状态，物料编码，用量）
        user.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        user.input_bomtree('产成品', 'BOM状态', '试产')
        user.input_bomtree('产成品', '物料编码', '10018956')
        user.input_bomtree('产成品', '用量', '1000')
        user.input_bomtree('充电器', '物料编码', '25101424')
        user.input_bomtree('充电器', '用量', '1000')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', 'NPS')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        process_code = user.get_info("BOM协作", "整机BOM协作")[1]
        user.supplementary_factory_flow(process_code)
        user.engineer_approve_flow(process_code)
        user.business_approve_flow(process_code)
        user.enter_oneworks_edit(process_code)
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_application_node(process_code, '审批通知', True)
        sleep(60)
        user.assert_my_application_flow(process_code, '审批完成')
        document_status = user.get_assigned_info(process_code)[7]
        ValueAssert.value_assert_equal(document_status, '审批通过')

    @allure.story("流程审批")  # 场景名称
    @allure.title("数据组审批页面，回退到补充工厂")  # 用例名称
    @allure.description("在数据组审批页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验：单据号和节点）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_020(self, drivers, Machine_Approval_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Approval_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(Machine_Approval_API[0], '补充工厂', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("数据组审批页面，回退到补充工厂再审核，还是数据组审核节点")  # 用例名称
    @allure.description("在我的待办中审批从数据组审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是数据组审核节点，而不是BOM工程师节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_021(self, drivers, Machine_Approval_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Approval_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.enter_oneworks_edit(Machine_Approval_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(Machine_Approval_API[0], '数据组审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("数据组审批页面，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_022(self, drivers, Machine_Approval_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Approval_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("数据组审批页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_023(self, drivers, Machine_Approval_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Approval_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("数据组审批页面，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_024(self, drivers, Machine_Approval_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Approval_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，选BOMTree中点击设置市场/配置按钮，保存成功")  # 用例名称
    @allure.description("在BOM工程师中，BOMTree中点击设置市场/配置按钮，弹出相应页面，在设置市场/配置页面中，填入组号和销售市场和机型配置，点击确认，能保存成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_025(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_config()
        user.modify_config('10026418', '组号', '5')
        user.modify_config('10026418', '销售市场', '尼泊尔')
        user.modify_config('10026418', '机型配置', '64+3')
        user.click_config_confirm()
        user.assert_toast('已成功更新BOM的市场及配置')
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在BOM工程师中，BOMTree新增物料成功")  # 用例名称
    @allure.description("在BOM工程师中，BOM Tree上点击新增物料，会出现新的物料节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_026(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_tree('产成品')
        user.input_bomtree('充电器', '物料编码', '25001673')
        user.click_add_material()
        user.input_add_material('25001673', '物料编码', '25001674')
        user.assert_oneworks_add_material(['1.2.1.2', '25001674', '电池_TECNO_BL_49FT_4900mAh_FH_IN_W10', '外研', '编辑删除'])
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("补充工厂页面中，导出的xlsx表的数据和页面的数据是一致的")  # 用例名称
    @allure.description("在补充工厂页面中，点击导出，导出的xlsx表的数据和页面的数据是一致的")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip
    def test_003_027(self, drivers, Machine_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_API[0])
        user.assert_oneworks_factoryinfo()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，Bom Tree导出数据一致")  # 用例名称
    @allure.description("在BOM工程师页面中，在Bom Tree中点导出，导出的数据和Bom Tree的数据是一致的")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip
    def test_003_028(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_BOMTree_checkbox()
        user.click_oneworks_approval_export()
        user.assert_oneworks_approval_bominfo()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核页面，生产工厂信息导出数据和页面数据一致")  # 用例名称
    @allure.description("在业务审核页面中，在生产工厂信息中点击导出，导出文件中的数据和页面的数据是一致的")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip
    def test_003_029(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.assert_oneworks_factoryinfo()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核页面，BOM Tree导出数据和页面中数据一致")  # 用例名称
    @allure.description("在业务审核页面中，点击BOM Tree中的导出，导出文件中的数据和页面中的数据是一致的")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip
    def test_003_030(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_BOMTree_checkbox()
        user.click_oneworks_approval_export()
        user.assert_oneworks_approval_bominfo()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在数据组审批页面，生产工厂信息导出数据和页面数据一致")  # 用例名称
    @allure.description("在数据组审批页面中，在生产工厂信息中点击导出，导出的文件中的数据和页面中的数据是一致的")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip
    def test_003_031(self, drivers, Machine_Approval_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Approval_API[0])
        user.click_Factory_checkbox()
        user.click_oneworks_factory_export()
        user.assert_oneworks_factoryinfo()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM，发起流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个整机生产BOM，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_032(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_add()
        user.input_Derived_info('新BOM类型', '发货BOM')
        user.input_Derived_info('新BOM编码', '11000002')
        user.input_Derived_info('原始BOM编码', '10026373')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '音频')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "整机BOM协作", '衍生BOM', 'X572-1', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_info("BOM协作", "整机BOM协作")[1]
        user.enter_onework_check(process_code)
        info1 = user.get_onework_bominfo('制作类型')
        info2 = user.get_onework_bominfo('品牌')
        info3 = user.get_onework_bominfo('机型')
        info4 = user.get_onework_bominfo('阶段')
        info5 = user.get_onework_bominfo('市场')
        ValueAssert.value_assert_equal(info1, '衍生BOM')
        ValueAssert.value_assert_equal(info2, 'itel')
        ValueAssert.value_assert_equal(info3, 'X572-1')
        ValueAssert.value_assert_equal(info4, '量产阶段')
        ValueAssert.value_assert_equal(info5, '埃塞本地')
        user.assert_oneworks_bomtree_result('产成品', ('1', '产成品', '11000002', 'CKD_itel_A44_F3706_玫瑰金_IN_BCFL_8+1_P05_E', '可选'))
        user.quit_oneworks()
        user.delete_flow(process_code)

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM，在补充工厂页面，审批成功")  # 用例名称
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示“处理成功”，并且页面成功跳转")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_033(self, drivers, Machine_Derive_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_API[0], '补充工厂', True)
        user.enter_oneworks_edit(Machine_Derive_API[0])
        user.input_oneworks_plant_info('国内组包工厂', '1051')
        user.click_oneworks_slash()
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(Machine_Derive_API[0], 'BOM工程师审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM，BOM工程师页面，审批成功并给出提示“处理成功，审核通过”")  # 用例名称
    @allure.description("在BOM工程师页面中，所有数据都正确，点击同意，可以提交成功并给出提示“处理成功，审核通过”，页面成功跳转；成功处理了BOM工程师审核点，我的待办中不存在该条单机在BOM工程师审核节点（建议：校验单据号和当前节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_034(self, drivers, Machine_Derive_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Factory_API[0], 'BOM工程师审批', True)
        user.enter_oneworks_edit(Machine_Derive_Factory_API[0])
        user.click_handle_bom()
        user.assert_toast('处理成功，请检查！')
        user.click_oneworks_agree()
        DomAssert(drivers).assert_att('处理成功，审核通过')
        user.quit_oneworks()
        user.assert_my_todo_node(Machine_Derive_Factory_API[0], 'BOM工程师审批')
        user.assert_my_todo_node(Machine_Derive_Factory_API[0], '业务审核', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM，BOM工程师页面，转交时不选择转交人，不存在确定转交按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_035(self, drivers, Machine_Derive_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Factory_API[0], 'BOM工程师审批', True)
        user.enter_oneworks_edit(Machine_Derive_Factory_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM，BOM工程师页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_036(self, drivers, Machine_Derive_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Factory_API[0], 'BOM工程师审批', True)
        user.enter_oneworks_edit(Machine_Derive_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM，BOM工程师页面，选择转交人转交后取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_037(self, drivers, Machine_Derive_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Factory_API[0], 'BOM工程师审批', True)
        user.enter_oneworks_edit(Machine_Derive_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM，BOM工程师页面，转交单据成功")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_038(self, drivers, Machine_Derive_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Factory_API[0], 'BOM工程师审批', True)
        user.enter_oneworks_edit(Machine_Derive_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(Machine_Derive_Factory_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM，BOM工程师页面，拒绝成功")  # 用例名称
    @allure.description("在BOM工程师页面中，点击拒绝，会显示处理成功，并且页面跳转")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_039(self, drivers, Machine_Derive_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Factory_API[0], 'BOM工程师审批', True)
        user.enter_oneworks_edit(Machine_Derive_Factory_API[0])
        user.click_oneworks_refuse()
        user.assert_toast('处理成功，审核拒绝')
        user.quit_oneworks()
        user.assert_my_application_flow(Machine_Derive_Factory_API[0], '审批拒绝')
        # process_status = user.get_info()[7]
        process_status = user.get_bom_info('整机BOM协作', Machine_Derive_Factory_API[0], '单据状态')
        ValueAssert.value_assert_equal(process_status, '审批拒绝')

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,BOM工程师中，新增物料成功")  # 用例名称
    @allure.description("在BOM工程师中，衍生BOM处理信息中点击新增物料，会出现新的物料节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_040(self, drivers, Machine_Derive_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Factory_API[0], 'BOM工程师审批', True)
        user.enter_oneworks_edit(Machine_Derive_Factory_API[0])
        user.click_OneworksDerived_add()
        user.input_OneworksDerived_info('BOM类型', '发货BOM')
        user.input_OneworksDerived_info('新BOM编码', '11000002')
        user.input_OneworksDerived_info('原始BOM编码', '10026373')
        user.input_OneworksDerived_info('父阶物料编码', '10026373')
        user.input_OneworksDerived_info('操作', '新增物料')
        user.input_OneworksDerived_info('子阶物料编码', '11000007')
        user.input_OneworksDerived_info('用量', '1')
        user.click_handle_bom()
        user.assert_toast('处理成功，请检查！')
        sleep(2)
        user.click_tree('产成品')
        user.assert_tree_result(('1.4.1', '11000007', 'CKD_Infinix_X604_H633_J_柏林灰_IN_32+3_E', '可选', '1'))
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,业务审核成功")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择通过，点击同意按钮，给出提示，并且页面跳转成功，跳转成功后，我的待办中不存在该条业务审核单据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_041(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_add()
        user.input_Derived_info('新BOM类型', '发货BOM')
        user.input_Derived_info('新BOM编码', '11000002')
        user.input_Derived_info('原始BOM编码', '10026373')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '音频')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "整机BOM协作", '衍生BOM', 'X572-1', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_info("BOM协作", "整机BOM协作")[1]
        user.supplementary_factory_flow(process_code)
        user.engineer_Derivedapprove_flow(process_code)
        user.enter_oneworks_edit(process_code)
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '音频')
        user.scroll_self_inspection()
        user.input_self_inspection_result()
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_application_node(process_code, '数据组审批', True)
        user.delete_flow(process_code)

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,业务审核回退到补充工厂成功")  # 用例名称
    @allure.description("在业务审核页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验：单据号和节点）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_042(self, drivers, Machine_Derive_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_bomEnginner_API[0], '业务审核', True)
        user.enter_oneworks_edit(Machine_Derive_bomEnginner_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(Machine_Derive_bomEnginner_API[0], '补充工厂', True)
        user.enter_oneworks_edit(Machine_Derive_bomEnginner_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(Machine_Derive_bomEnginner_API[0], '业务审核', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,在业务审核页面中，转交时不选择转交人，不存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_043(self, drivers, Machine_Derive_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_bomEnginner_API[0], '业务审核', True)
        user.enter_oneworks_edit(Machine_Derive_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,在业务审核页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_044(self, drivers, Machine_Derive_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_bomEnginner_API[0], '业务审核', True)
        user.enter_oneworks_edit(Machine_Derive_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,在业务审核页面中，选择转交人转交后取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_045(self, drivers, Machine_Derive_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_bomEnginner_API[0], '业务审核', True)
        user.enter_oneworks_edit(Machine_Derive_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,在业务审核页面中，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_046(self, drivers, Machine_Derive_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_bomEnginner_API[0], '业务审核', True)
        user.enter_oneworks_edit(Machine_Derive_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(Machine_Derive_bomEnginner_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM/状态/物料检查为成功，点击同意，能提交成功，并且给出提交成功的提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    @pytest.mark.skip  # 如果需要执行，手动将@pytest.mark.skip注释
    def test_003_047(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_bom_info('制作类型', '衍生BOM')
        user.input_bom_info('品牌', 'itel')
        user.input_bom_info('机型', 'X572-1')
        user.input_bom_info('阶段', '量产阶段')
        user.input_bom_info('市场', '埃塞本地')
        user.click_Derived_add()
        user.input_Derived_info('新BOM类型', '发货BOM')
        user.input_Derived_info('新BOM编码', '11000002')
        user.input_Derived_info('原始BOM编码', '10026373')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.select_business_review('李小素', 'MPM')
        user.select_business_review('李小素', '音频')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result("BOM协作", "整机BOM协作", '衍生BOM', 'X572-1', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_info("BOM协作", "整机BOM协作")[1]
        user.supplementary_factory_flow(process_code)
        user.engineer_Derivedapprove_flow(process_code)
        user.business_approve_flow(process_code)
        user.enter_oneworks_edit(process_code)
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_application_node(process_code, '审批通知', True)
        sleep(60)
        user.assert_my_application_flow(process_code, '审批完成')
        document_status = user.get_assigned_info(process_code)[7]
        ValueAssert.value_assert_equal(document_status, '审批通过')

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,在数据组审批页面中回退到补充工厂成功")  # 用例名称
    @allure.description("在数据组审批页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验：单据号和节点）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_048(self, drivers, Machine_Derive_Approval_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Approval_API[0], '数据组审批', True)
        user.enter_oneworks_edit(Machine_Derive_Approval_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(Machine_Derive_Approval_API[0], '补充工厂', True)
        user.enter_oneworks_edit(Machine_Derive_Approval_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(Machine_Derive_Approval_API[0], '数据组审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,在数据组审批页面中，转交时不选择转交人，不存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_049(self, drivers, Machine_Derive_Approval_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Approval_API[0], '数据组审批', True)
        user.enter_oneworks_edit(Machine_Derive_Approval_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,在数据组审批页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_050(self, drivers, Machine_Derive_Approval_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Approval_API[0], '数据组审批', True)
        user.enter_oneworks_edit(Machine_Derive_Approval_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("衍生BOM,在数据组审批页面中，选择转交人转交后取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_051(self, drivers, Machine_Derive_Approval_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Machine_Derive_Approval_API[0], '数据组审批', True)
        user.enter_oneworks_edit(Machine_Derive_Approval_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

@allure.feature("BOM协作-整机BOM协作")  # 模块名称
class TestProcessApprovalExceptionScenario:

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("【生产工厂信息】物料XXXXXXXX的组包工厂不能为空")  # 用例名称
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示【生产工厂信息】物料xxxxxx的组包工厂不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_001(self, drivers, Machine_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_API[0])
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('【生产工厂信息】物料10026418的组包工厂不能为空')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("未选择BOM，无法点击一键填写按钮")  # 用例名称
    @allure.description("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_002(self, drivers, Machine_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_API[0])
        user.assert_oneworks_onepress_write()
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("请选择工厂分类")  # 用例名称
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，不进行工厂分类，不进行选择工厂，点击确认，不能进行确认并给出必填提示请选择工厂分类，请选择工厂")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_003(self, drivers, Machine_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_API[0])
        user.click_Factory_checkbox()
        user.click_oneworks_onepress_write()
        user.click_oneworks_onepress_write_confirm()
        DomAssert(drivers).assert_att('请选择工厂分类')
        DomAssert(drivers).assert_att('请选择工厂')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("检查贴片工厂不能为空！")  # 用例名称
    @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示检查贴片工厂不能为空！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_004(self, drivers, Machine_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_API[0])
        user.input_oneworks_plant_info('国内组包工厂', '1051')
        user.click_oneworks_slash()
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('检查贴片工厂不能为空！')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("父阶BOM料号xxxxxxxx用量不为1000！")  # 用例名称
    @allure.description("在BOM工程师页面中，在Bom Tree中点编辑，将用量编辑为“1”，点击同意，不能提交成功页面给出提示父阶BOM料号xxxxxxxx用量不为1000")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_005(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.input_bomtree('产成品', '用量', '1')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('父阶BOM料号10026418用量不为1000')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("不能删除BOM！")  # 用例名称
    @allure.description("在BOM工程师页面中，在产成品中点击删除按钮，不能进行删除，并且给出提示不能删除BOM！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_006(self, drivers, Machine_Factory_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Factory_API[0])
        user.click_bomtree_delete('产成品')
        user.assert_toast('不能删除BOM！')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单检查角色未选择")  # 用例名称
    @allure.description("在业务审核页面中，不填写任何内容，点击同意，不能提交成功，并给出提示自检清单检查角色未选择")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_007(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单检查角色未选择')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单第【1】行检查结果未选择")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，选择后直接点击同意，不能提交成功，并给出提示自检清单第【1】行检查结果未选择")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_008(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '音频')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果未选择')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不通过，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不通过需填写原因及修改建议")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_009(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '音频')
        user.scroll_self_inspection()
        user.input_self_inspection_result(result='不通过')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果为不通过需填写原因及修改建议')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不涉及，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不涉及需填写原因及修改建议")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_010(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '音频')
        user.scroll_self_inspection()
        user.input_self_inspection_result(result='不涉及')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果为不涉及需填写原因及修改建议')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("[手机_itel_预研组_整机BOM]未配置自检清单！&自检清单不能为空")  # 用例名称
    @allure.description("在业务审核页面中，选择检查角色没有配置的自检清单的检查角色，会提示[手机_itel_预研组_整机BOM]未配置自检清单！，直接点击同意，会提示自检清单不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_011(self, drivers, Machine_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_bomEnginner_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', 'MPM')
        user.assert_toast('[手机_itel_MPM_整机BOM]未配置自检清单！')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        DomAssert(drivers).assert_att('自检清单不能为空')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("衍生BOM，【生产工厂信息】物料XXXXXXXX的组包工厂不能为空")  # 用例名称
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示【生产工厂信息】物料xxxxxx的组包工厂不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_012(self, drivers, Machine_Derive_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Derive_API[0])
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('【生产工厂信息】物料11000002的组包工厂不能为空')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("衍生BOM，未选择BOM，无法点击一键填写按钮")  # 用例名称
    @allure.description("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_013(self, drivers, Machine_Derive_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Derive_API[0])
        user.assert_oneworks_onepress_write()
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("衍生BOM，请选择工厂分类，请选择工厂")  # 用例名称
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，不进行工厂分类，不进行选择工厂，点击确认，不能进行确认并给出必填提示请选择工厂分类，请选择工厂")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_014(self, drivers, Machine_Derive_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Derive_API[0])
        user.click_Factory_checkbox()
        user.click_oneworks_onepress_write()
        user.click_oneworks_onepress_write_confirm()
        DomAssert(drivers).assert_att('请选择工厂分类')
        DomAssert(drivers).assert_att('请选择工厂')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("衍生BOM，检查贴片工厂不能为空！")  # 用例名称
    @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示检查贴片工厂不能为空！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_015(self, drivers, Machine_Derive_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Derive_API[0])
        user.input_oneworks_plant_info('国内组包工厂', '1051')
        user.click_oneworks_slash()
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('检查贴片工厂不能为空！')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("衍生BOM，自检清单第【1】行检查结果未选择")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，选择后直接点击同意，不能提交成功，并给出提示自检清单第【1】行检查结果未选择")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_016(self, drivers, Machine_Derive_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Derive_bomEnginner_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '音频')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果未选择')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("衍生BOM，自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不通过，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不通过需填写原因及修改建议")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_017(self, drivers, Machine_Derive_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Derive_bomEnginner_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '音频')
        user.scroll_self_inspection()
        user.input_self_inspection_result(result='不通过')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果为不通过需填写原因及修改建议')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("衍生BOM，自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不涉及，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不涉及需填写原因及修改建议")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_018(self, drivers, Machine_Derive_bomEnginner_API):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Machine_Derive_bomEnginner_API[0])
        user.click_self_inspection('业务类型', '手机')
        user.click_self_inspection('检查角色', '音频')
        user.scroll_self_inspection()
        user.input_self_inspection_result(result='不涉及')
        user.click_oneworks_agree()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果为不涉及需填写原因及修改建议')
        user.quit_oneworks()


@allure.feature("BOM协作-整机BOM协作")  # 模块名称
class TestProcessSearch:

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，制作类型和流程编码查询结果正确")  # 用例名称
    @allure.description("进入整机BOM协作页面，输入存在的制作类型和流程编码，点击查询，下方会显示相应的数据（建议：校验制作类型和流程编码）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_001(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', '衍生BOM')
        user.input_search_info('流程编码', 'ZBOM20220516083131304353')
        user.click_search()
        user.assert_search_result('制作类型', '衍生BOM')
        user.assert_search_result('流程编码', 'ZBOM20220516083131304353')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，查询后点击重置，下方会显示所有的数据")  # 用例名称
    @allure.description("进入整机BOM协作页面，输入存在的流程编码和BOM编码，点击查询，查询后点击重置，下方会显示所有的数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_002(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', '衍生BOM')
        user.input_search_info('流程编码', 'ZBOM20220516083131304353')
        user.click_search()
        user.assert_search_result('制作类型', '衍生BOM')
        user.assert_search_result('流程编码', 'ZBOM20220516083131304353')
        user.click_reset()
        user.assert_search_row(10)

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，查询不存在流程编码，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的流程编码，点击查询，查询结果为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_003(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('流程编码', 'sfdasdfwefw')
        user.click_search()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，单机头BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为单机头BOM制作，点击查询，查询结果为所有制作类型为单机头BOM制作的信息息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_004(self, drivers):
        user = MachineBOMCollaboration(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', 'CKD/SKD BOM（国内整机已归档）')
        user.click_search()
        user.assert_search_result('制作类型', 'CKD/SKD BOM（国内整机已归档）')


if __name__ == '__main__':
    pytest.main(['BOMCooperation_MachineBomCooperation.py'])
