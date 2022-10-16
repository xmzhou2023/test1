import allure
import pytest

from libs.common.time_ui import sleep
from project.TBM.page_object.BOMCooperation_ForeignBom import ForeignBom
from public.base.assert_ui import DomAssert, ValueAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("BOM协作-外研BOM协作")  # 模块名称
class TestCreateProcess:
    @allure.story("创建流程")  # 场景名称
    @allure.title("创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，在生产工厂信息点击刷新按钮，点击提交，能提交成功创建流程成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_add_bom_info('制作类型', '客供BOM制作')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
        user.click_add_bomtree()
        user.input_bomtree('客供BOM','BOM状态', '量产')
        user.input_bomtree('客供BOM','物料编码', '12004871')
        user.input_bomtree('客供BOM','用量', '1000')
        user.click_optional_material()
        user.input_optional_material('12004871', '物料编码', '12800002')
        user.input_optional_material('12004871', '用量', '1000')
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.click_search()
        user.assert_add_result('自动化新增用例', '客供BOM制作', 'JMB-01', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_bom_info('外研BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("新增同组物料两颗，份额合计100,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据；新增两颗物料，添加替代组都为A1，份额为一个20，一个80，其他内容正确填写，点击提交，能提交成功并且提示“创建流程成功”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_add_bom_info('制作类型', '客供BOM制作')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
        user.click_add_bomtree()
        user.input_bomtree('客供BOM','BOM状态', '量产')
        user.input_bomtree('客供BOM','物料编码', '12004871')
        user.input_bomtree('客供BOM','用量', '1000')
        user.click_optional_material()
        user.input_optional_material('12004871', '物料编码', '12800002')
        user.input_optional_material('12004871', '用量', '1000')
        user.input_optional_material('12004871', '替代组', 'A1')
        user.input_optional_material('12004871', '份额', '20')
        user.material_focus('12004871')
        user.click_optional_material()
        user.input_optional_material('12800002', '物料编码', '12800003')
        user.input_optional_material('12800002', '用量', '1000')
        user.input_optional_material('12800002', '替代组', 'A1')
        user.input_optional_material('12800002', '份额', '80')
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result('自动化新增用例', '客供BOM制作', 'JMB-01', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_bom_info('外研BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("选择物料编码，点击一键填写，填写内容保存正确")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选中两颗物料，点击一键填写，填写用量和1000点击确认，页面上显示两颗物料用量都为1000")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM', 'BOM状态', '量产')
        user.input_bomtree('客供BOM', '物料编码', '12004871')
        user.click_optional_material()
        user.input_optional_material('12004871', '物料编码', '12800002')
        user.click_checkbox()
        user.input_one_press('用量', '1000')
        amount = user.get_bomtree_info('客供BOM')[7]
        ValueAssert.value_assert_equal(amount, '1000')
        amount = user.get_bomtree_info('12800002')[1]
        user.assert_value_in('1000', amount)

    @allure.story("创建流程")
    @allure.title("BOM tree中不选择物料，页面上不存在删除按钮")
    @allure.description("进入新增页面制作类型选择客供BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不选择物料，页面上不存在删除按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_004(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.assert_batch_delete(False)

    @allure.story("创建流程")
    @allure.title("选择物料，页面上存在删除按钮")
    @allure.description("进入新增页面制作类型选择客供BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择物料，页面上存在删除按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_005(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_checkbox()
        user.assert_batch_delete(True)

    @allure.story("创建流程")
    @allure.title("选中父节点物料后点击删除，删除页面数据")
    @allure.description("进入新增页面制作类型选择客供BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_006(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_bomtree_delete('客供BOM')
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("创建流程")
    @allure.title("选中子节点物料后点击删除，清子节点内容")
    @allure.description("进入新增页面制作类型选择客供BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_007(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM', 'BOM状态', '量产')
        user.input_bomtree('客供BOM', '物料编码', '12004871')
        user.input_bomtree('客供BOM', '用量', '1000')
        user.click_optional_material()
        user.input_optional_material('12004871', '物料编码', '12800002')
        user.input_optional_material('12004871', '用量', '1000')
        user.input_optional_material('12004871', '替代组', 'A1')
        user.input_optional_material('12004871', '份额', '20')
        user.click_bomtree_delete('12800002')
        user.assert_bomtree('12800002')

    @allure.story("创建流程")
    @allure.title("选择正确的文件进行导入，并应用，显示的数据与模板的数据一致")
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_008(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_bom_import()
        user.upload_true_file()
        user.assert_upload_result(('1','量产', '12004871', '外购单机头_TECNO_W1_B40030_埃塞_新客供', '12800002', '整机外包料Infinix_X5010_AW878_黑_A欧_P02_Ⅰ', '1000'),)
        user.click_apply()
        user.click_tree('客供BOM')
        user.assert_tree_result(('1', '客供BOM', '12004871', '外购单机头_TECNO_W1_B40030_埃塞_新客供', '外研', '1000', '编辑删除'), ('1.1', '12800002', '整机外包料Infinix_X5010_AW878_黑_A欧_P02_Ⅰ', '外研', '1000', '编辑删除'))

    @allure.story("创建流程")  # 场景名称
    @allure.title("客供BOM衍生,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息包含新增为128开头的物料，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，提示发起成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_009(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
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
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result('自动化新增用例', '客供BOM衍生', 'JMB-01', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_bom_info('外研BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("客供BOM衍生,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息包含新增为128开头的物料，再新增1颗物料，添加替代组都为A1，份额为一个20，一个80，其他内容正确填写，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，能提交成功并且提示“创建流程成功”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_010(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
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
        user.input_Derived_info('替代组', 'A1')
        user.input_Derived_info('份额', '30')
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12000003', 2)
        user.input_Derived_info('操作', '新增物料', 2)
        user.input_Derived_info('处理物料编码', '12800002', 2)
        user.input_Derived_info('用量', '1000', 2)
        user.input_Derived_info('替代组', 'A1', 2)
        user.input_Derived_info('份额', '70', 2)
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result('自动化新增用例', '客供BOM衍生', 'JMB-01', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_bom_info('外研BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("客供BOM衍生导入模板,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，下载模板，模板内容正确填写包含新增为128开头的物料，在衍生差异点击导入，文件导入成功，点击生成BOM，点击刷新，填写业务审核，点击提交，流程发起成功并提示流程创建成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_011(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
        user.click_Derived_import()
        user.upload_Derived_file('外研BOM衍生需求导入模板.xlsx')
        user.click_apply()
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result('自动化新增用例', '客供BOM衍生', 'JMB-01', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_bom_info('外研BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("客供BOM衍生,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中新增物料后，点击删除按钮，物料信息删除成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_012(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12000003')
        user.input_Derived_info('原始BOM编码', '12014351')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.delete_Derived_info()
        user.assert_Derived_None()
        user.click_Derived_differ()
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12000003')
        user.input_Derived_info('操作', '新增物料')
        user.input_Derived_info('处理物料编码', '12800001')
        user.input_Derived_info('用量', '1000')
        user.input_Derived_info('替代组', 'A1')
        user.input_Derived_info('份额', '20')
        user.delete_Derived_info()
        user.assert_Derived_None()

@allure.feature("BOM协作-外研BOM协作")
class TestCreateProcessExceptionScenario:
    @allure.story("创建流程异常场景")
    @allure.title("生产工厂信息不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，提示生产工厂信息不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_001(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.add_bomtree_info()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('生产工厂信息不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不选择BOM状态，正确填写物料编码等其他内容，点击提交，不能提交成功并给出提示BOM状态不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_002(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM','物料编码', '12004871')
        user.input_bomtree('客供BOM','用量', '1000')
        user.click_add_submit()
        user.assert_toast('BOM状态不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("[XXXXX]下必须存在物料组为128的子阶物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，只加一个BOM，不在下面添加子BOM，点击提交，不能成功并给出提示[12010003]下必须存在物料组为128的子阶物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_003(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM', 'BOM状态', '量产')
        user.input_bomtree('客供BOM','物料编码', '12004871')
        user.input_bomtree('客供BOM','用量', '1000')
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('[12004871]下必须存在物料组为128的子阶物料')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("xxxxxxx用量不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量不进行填写，点击提交，不能提交成功并给出提示xxxxxx用量不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_004(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM', 'BOM状态', '量产')
        user.input_bomtree('客供BOM','物料编码', '12004871')
        user.click_add_submit()
        user.assert_toast('12004871用量不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("父阶BOM料号xxxxxxxx用量不为1000")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1，点击提交，不能提交成功并给出提示父阶BOM料号10000001用量不为1000")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_005(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM', 'BOM状态', '量产')
        user.input_bomtree('客供BOM','物料编码', '12004871')
        user.input_bomtree('客供BOM','用量', '1')
        user.click_optional_material()
        user.input_optional_material('12004871', '物料编码', '12800002')
        user.input_optional_material('12004871', '用量', '1')
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('父阶BOM料号12004871用量不为1000')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("用量只能填写非0数字(最多3位小数)")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为非数字类型，点击提交，不能提交成功并给出提示用量只能填写非0数字(最多3位小数)")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_006(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM', 'BOM状态', '量产')
        user.input_bomtree('客供BOM','物料编码', '12004871')
        user.input_bomtree('客供BOM','用量', 'a')
        user.click_add_submit()
        user.assert_toast('用量只能填写非0数字(最多3位小数)')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("业务审核必填项需填写完整！")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示业务审核必填项需填写完整！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_007(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM', 'BOM状态', '量产')
        user.input_bomtree('客供BOM','物料编码', '12004871')
        user.input_bomtree('客供BOM','用量', '1000')
        user.click_refresh()
        user.click_add_submit()
        DomAssert(drivers).assert_att('业务审核必填项需填写完整！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("只填写一个业务审核，提示业务审核必填项需填写完整！")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，其中一个业务审核不选择相应的审核人员，点击提交，不能提交成功，并给出提示业务审核必填项需填写完整！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_008(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.add_bomtree_info()
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.click_add_submit()
        user.assert_toast('业务审核必填项需填写完整！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("[XXXXX] 替代组[XX]只有一颗物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入数据，新增一颗物料，添加替代组为A1，份额为20，其他内容正确填写，点击提交，不能提交成功并且提示替代组只有一颗物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_009(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.add_bomtree_info()
        user.input_optional_material('12004871', '替代组', 'A1')
        user.input_optional_material('12004871', '份额', '20')
        user.click_add_submit()
        user.assert_toast('[12004871] 替代组[A1]只有一颗物料')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("不选择物料，点击一键填写不生效")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，不选择物料，点击一键填写，填写用量为1000，点击确定，页面上没有填写上任何数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_010(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_checkbox()
        user.input_one_press('用量', '1000')
        amount = user.get_bomtree_info('客供BOM')[7]
        ValueAssert.value_assert_equal(amount, '')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("一键填写无内容提示内容不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选中两颗物料，点击一键填写，选择用量，并且不填写字段值，点击确认，给出必填提示，提示为不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_011(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_checkbox()
        user.input_one_press('用量', '')
        DomAssert(drivers).assert_att('不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("文件类型非excel")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示文件类型非excel!")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_012(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_bom_import()
        user.upload_wrong_file()
        user.assert_toast('文件类型非excel!')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("正确内容错误的文件进行导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_013(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_bom_import()
        user.upload_wrongcontent_file()
        user.assert_wrongcontent_upload_result()

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("[xxxxxxxx]下必须存在物料组为128的子阶物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM、新增物料，输入客供BOM的物料编码、用量，新增物料时输入物料编码不为128的料，点击刷新，点击提交，xxxxxxxx下必须存在物料组为128的子阶物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_014(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM', 'BOM状态', '量产')
        user.input_bomtree('客供BOM','物料编码', '12004871')
        user.input_bomtree('客供BOM','用量', '1000')
        user.click_optional_material()
        user.input_optional_material('12004871', '物料编码', '12700002')
        user.input_optional_material('12004871', '用量', '1000')
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('[12004871]下必须存在物料组为128的子阶物料')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BomTree与生产工厂信息数据不一致，请点击刷新按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中输入客供BOM的物料编码、用量，点刷新；修改客供BOM的物料编码，不点刷新，点击提交，提示BomTree与生产工厂信息数据不一致，请点击刷新按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_015(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM', 'BOM状态', '量产')
        user.input_bomtree('客供BOM','物料编码', '12004872')
        user.input_bomtree('客供BOM','用量', '1000')
        user.click_refresh()
        user.input_bomtree('客供BOM', '物料编码', '12004873')
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('BomTree与生产工厂信息数据不一致，请点击刷新按钮')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("请先选择制作类型")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，不选择制作类型，点击新增BOM，提示请先选择制作类型!")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_016(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.click_add_bomtree()
        user.assert_toast('请先选择制作类型!')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("[xxxxx]下必须存在物料组为128的子阶物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，选择一个存在模板的品牌，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息不包含新增为128开头的物料，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，提示[xxxxxx]下必须存在物料组为128的子阶物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_017(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12000003')
        user.input_Derived_info('原始BOM编码', '12014351')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.click_Derived_differ()
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12000003')
        user.input_Derived_info('操作', '新增物料')
        user.input_Derived_info('处理物料编码', '12700001')
        user.input_Derived_info('用量', '1000')
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('[12000003]下必须存在物料组为128的子阶物料')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("请完善Bom信息！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息不填写完整，输入业务审核必填项，点击提交，提示请完善Bom信息！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_018(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.click_add_submit()
        user.assert_toast('请完善Bom信息！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("Bom Tree不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，不填写BOM Tree点击提交，提示Bom Tree不能为空！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_019(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
        user.click_add_submit()
        user.assert_toast('Bom Tree不能为空！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("不点击生成BOM，Bom Tree不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，不点击生成BOM，点击提交，提示Bom Tree不能为空！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_020(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
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
        user.click_add_submit()
        user.assert_toast('Bom Tree不能为空！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("生产工厂信息不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，不点击生成BOM，点击提交，提示Bom Tree不能为空！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_021(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
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
        user.click_add_submit()
        DomAssert(drivers).assert_att('生产工厂信息不能为空！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("业务审核必填项需填写完整！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，点击生成BOM，不填写业务审核，点击刷新，点击提交，提示业务审核必填项需填写完整！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_022(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
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
        user.click_add_submit()
        DomAssert(drivers).assert_att('业务审核必填项需填写完整！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("衍生差异【第1行】用量只能填写非0数字(最多3位小数)")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，衍生差异的用量填0，点击生成BOM，提示衍生差异【第1行】用量只能填写非0数字(最多3位小数)")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_023(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12000003')
        user.input_Derived_info('原始BOM编码', '12014351')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.click_Derived_differ()
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12000003')
        user.input_Derived_info('操作', '新增物料')
        user.input_Derived_info('处理物料编码', '12800001')
        user.input_Derived_info('用量', '0')
        user.click_Creat_BOM()
        user.assert_toast('衍生差异【第1行】用量只能填写非0数字(最多3位小数)')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx用量不为1000")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，衍生差异的用量填10，点击生成BOM，提示“父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx用量不为1000”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_024(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
        user.click_Derived_add()
        user.input_Derived_info('新BOM编码', '12000003')
        user.input_Derived_info('原始BOM编码', '12014351')
        user.input_Derived_info('原始BOM工厂', 'PL01')
        user.click_Derived_differ()
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12000003')
        user.input_Derived_info('操作', '新增物料')
        user.input_Derived_info('处理物料编码', '12800001')
        user.input_Derived_info('用量', '10')
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12000003', 2)
        user.input_Derived_info('操作', '新增物料', 2)
        user.input_Derived_info('处理物料编码', '12100001', 2)
        user.input_Derived_info('用量', '10', 2)
        user.click_Creat_BOM()
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('父阶BOM料号12000003下的子阶BOM料号12100001用量不为1000')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("业务审核必填项需填写完整！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，点击生成BOM，业务审核有一个必填项不填，点击刷新，点击提交，提示业务审核必填项需填写完整！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_025(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
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
        user.select_business_review('李小素', 'PPM')
        user.click_add_submit()
        user.assert_toast('业务审核必填项需填写完整！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("xxxxxxxx替代组[xx]只有一颗物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息包含新增为128开头的物料添加替代组为A1，份额为20，其他内容正确填写，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，不能提交成功并且提示“xxxxxxxx替代组[xx]只有一颗物料”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_026(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
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
        user.input_Derived_info('替代组', 'A1')
        user.input_Derived_info('份额', '20')
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('[12000003] 替代组[A1]只有一颗物料')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("xxxxxxxx替代组[xx]的份额总和不为100")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息包含新增为128开头的物料添加替代组为A2，份额为20，再新增1颗物料添加替代组为A2，份额为20，其他内容正确填写，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，不能提交成功并且提示“xxxxxxxx替代组[xx]的份额总和不为100”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_027(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_add_bom_info('制作类型', '客供BOM衍生')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '量产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('模式', '零价值客供')
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
        user.input_Derived_info('替代组', 'A1')
        user.input_Derived_info('份额', '20')
        user.click_Derived_add()
        user.input_Derived_info('BOM编码', '12000003', 2)
        user.input_Derived_info('操作', '新增物料', 2)
        user.input_Derived_info('处理物料编码', '12800002', 2)
        user.input_Derived_info('用量', '1000', 2)
        user.input_Derived_info('替代组', 'A1', 2)
        user.input_Derived_info('份额', '79', 2)
        user.click_Creat_BOM()
        user.assert_toast('生成衍生BOM成功')
        user.click_refresh()
        user.select_business_review('李小素', 'PPM')
        user.select_business_review('李小素', 'QPM')
        user.click_add_submit()
        user.assert_toast('[12000003] 替代组[A1]的份额总和不为100')
@allure.feature("BOM协作-外研BOM协作")  # 模块名称
class TestTheProcessOfExaminationAndApproval:

    @allure.story("流程审批")  # 场景名称
    @allure.title("发起流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个整机生产BOM，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_001(self, drivers, Foreign_API):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.enter_onework_check(Foreign_API[0])
        info1 = user.get_onework_bominfo('制作类型')
        info2 = user.get_onework_bominfo('品牌')
        info3 = user.get_onework_bominfo('机型')
        info4 = user.get_onework_bominfo('阶段')
        info5 = user.get_onework_bominfo('市场')
        info6 = user.get_onework_bominfo('模式')
        ValueAssert.value_assert_equal(info1, '客供BOM制作')
        ValueAssert.value_assert_equal(info2, 'itel')
        ValueAssert.value_assert_equal(info3, 'JMB-01')
        ValueAssert.value_assert_equal(info4, '量产阶段')
        ValueAssert.value_assert_equal(info5, '埃塞本地')
        ValueAssert.value_assert_equal(info6, '零价值客供')
        user.assert_oneworks_bomtree_result(('1', '客供BOM', '12004875', '单机头_Spice_Z301_G282Z2_蓝色_无卡_IN', '可选', '1000'), ('1.1', '12800002', '整机外包料Infinix_X5010_AW878_黑_A欧_P02_Ⅰ', '外研', '1000'))
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核页面，审核成功")  # 用例名称
    @allure.description("在业务审核页面，所有数据正确填写，点击同意，能成功提交，并给出提示处理成功，并且页面成功跳转")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_002(self, drivers, Foreign_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Foreign_API[0])
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(Foreign_API[0], '数据组审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核页面，审核成功")  # 用例名称
    @allure.description("在业务审核页面，所有数据正确填写，点击同意，弹出弹框确认同意？，点击取消，取消成功，页面无变化")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_003(self, drivers, Foreign_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Foreign_API[0])
        user.click_oneworks_agree()
        user.click_oneworks_cancel()
        user.enter_oneworks_iframe()
        user.quit_oneworks()
        user.assert_my_todo_node(Foreign_API[0], '业务审核', True)

    @allure.story("流程审批")
    @allure.title("在业务审核页面中，选择转交人转交，存在确定转交按钮")
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_004(self, drivers, Foreign_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Foreign_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("在业务审核页面中，不选择转交人转交，不存在确定转交按钮")
    @allure.description("在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_005(self, drivers, Foreign_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Foreign_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("在业务审核页面中，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_006(self, drivers, Foreign_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Foreign_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在业务审核页面中，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_007(self, drivers, Foreign_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(Foreign_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(Foreign_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("在数据组审批页面中，回退到业务审核再审核，还是数据组审批节点")  # 用例名称
    @allure.description("在数据组审批页面中，点击回退，选择回退到业务审核页面，查看我的待办中存在业务审核节点，在业务审核同意并审核成功，下个节点是数据组审核节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_008(self, drivers, Foreign_Approval_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Foreign_Approval_API[0], '数据组审批', True)
        user.enter_oneworks_edit(Foreign_Approval_API[0])
        user.click_oneworks_rollback('业务审核')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(Foreign_Approval_API[0], '业务审核', True)
        user.enter_oneworks_edit(Foreign_Approval_API[0])
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(Foreign_Approval_API[0], '数据组审批', True)

    @allure.story("流程审批")
    @allure.title("在业务审核页面中，选择转交人转交，存在确定转交按钮")
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_009(self, drivers, Foreign_Approval_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Foreign_Approval_API[0], '数据组审批', True)
        user.enter_oneworks_edit(Foreign_Approval_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("在业务审核页面中，不选择转交人转交，不存在确定转交按钮")
    @allure.description("在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_010(self, drivers, Foreign_Approval_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Foreign_Approval_API[0], '数据组审批', True)
        user.enter_oneworks_edit(Foreign_Approval_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("在业务审核页面中，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_011(self, drivers, Foreign_Approval_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Foreign_Approval_API[0], '数据组审批', True)
        user.enter_oneworks_edit(Foreign_Approval_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在业务审核页面中，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_012(self, drivers, Foreign_Approval_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Foreign_Approval_API[0], '数据组审批', True)
        user.enter_oneworks_edit(Foreign_Approval_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(Foreign_Approval_API[0], '陈月')

@allure.feature("BOM协作-外研BOM协作")
class TestProcessApprovalExceptionScenario:
    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("数据组审批页面，检查失败项不为0，提交失败")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM/状态/物料检查为失败，点击同意，不能提交成功，并且给出提交失败的提示子阶bom检查失败，无法同步")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_001(self, drivers, Foreign_Failed_API):
        user = ForeignBom(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(Foreign_Failed_API[0], '数据组审批', True)
        user.enter_oneworks_edit(Foreign_Failed_API[0])
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.enter_oneworks_iframe()
        user.assert_toast('子阶bom检查失败，无法同步')
        user.quit_oneworks()


@allure.feature("BOM协作-外研BOM协作")  # 模块名称
class TestProcessSearch:

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，标题查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入“李小素”，点击查询，查询结果为所有标题包含“李小素”的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_001(self, drivers):
        user = ForeignBom(drivers)
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
        user = ForeignBom(drivers)
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
        user = ForeignBom(drivers)
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
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('流程编码', 'sfdasdfwefw')
        user.click_search()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，客供BOM衍生查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为客供BOM衍生，点击查询，查询结果为所有制作类型为客供BOM衍生的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_005(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', '客供BOM衍生')
        user.click_search()
        user.assert_search_result('制作类型', '客供BOM衍生')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，客供BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为客供BOM制作，点击查询，查询结果为所有制作类型为客供BOM制作的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_006(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', '客供BOM制作')
        user.click_search()
        user.assert_search_result('制作类型', '客供BOM制作')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，客供BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入“李小素”，流程编码输入框输入“1”，BOM编码输入“2”，下拉框选择为客供BOM制作，点击查询，查询结果为所有标题包含“李小素”、流程编码包含“1”、物料编码包含“2”、制作类型为客供BOM制作的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_007(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '李小素')
        user.input_search_info('流程编码', '1')
        user.input_search_info('制作类型', '客供BOM制作')
        user.click_search()
        user.assert_search_result('制作类型', '客供BOM制作')
        user.assert_search_result('流程编码', '1')
        user.assert_search_result('标题', '李小素')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，编辑正常")  # 用例名称
    @allure.description("在查询页面，点击编辑，跳转至oneworks编辑页面，可以编辑页面信息、提交、保存")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_008(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '自动化查询用例test')
        user.click_search()
        user.click_edit('自动化查询用例test')
        user.click_add_save()
        DomAssert(drivers).assert_att('保存草稿成功')
        user.click_edit('自动化查询用例test')
        user.click_add_submit()
        DomAssert(drivers).assert_att('创建流程成功')
        user.input_search_info('标题', '自动化查询用例test')
        user.click_search()
        code = user.get_bom_info('外研BOM协作', '自动化查询用例test', '流程编码')
        user.recall_process(code)

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，删除取消无变动")  # 用例名称
    @allure.description("在查询页面，点击删除，提示是否确认删除，点击取消，取消成功，页面无变动")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_005_009(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '自动化查询用例test')
        user.click_search()
        user.click_delete('自动化查询用例test')
        user.click_delete_cancel()
        user.assert_search_result('标题', '自动化查询用例test')
if __name__ == '__main__':
    pytest.main(['BOMCooperation_ForeignBom.py'])
