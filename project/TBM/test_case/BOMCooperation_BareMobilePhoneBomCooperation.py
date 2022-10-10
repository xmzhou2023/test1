import pytest
from public.base.assert_ui import *
from project.TBM.page_object.BOMCooperation_BareMobilePhoneBomCooperation import BareMobilePhoneBomCooperation


@allure.feature("BOM协作-单机头BOM协作")
class TestCreateProcess:

    @allure.story("创建流程")
    @allure.title("创建流程成功")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，能提交成功创建流程成功")
    @allure.severity("blocker")  # blocker\\normal\\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_add_bom_info('制作类型', '单机头BOM制作')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'X572-1')
        user.input_add_bom_info('阶段', '试产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('同时做衍生BOM', '否')
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011067')
        user.input_bomtree('单机头', '用量', '1000')
        user.select_business_review('李小素', 'MPM')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result('自动化新增用例', '单机头BOM制作', 'X572-1', 'itel', '埃塞本地', '试产阶段', '审批中','未同步')
        process_code = user.get_bom_info('单机头BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")
    @allure.title("创建流程成功")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，在指纹模组中新增两颗物料，添加替代组都为A1，份额为一个20，一个80，其他内容正确填写，点击提交，能提交成功并且提示创建流程成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_basic_info('标题', '自动化新增用例')
        user.input_add_bom_info('制作类型', '单机头BOM制作')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'X572-1')
        user.input_add_bom_info('阶段', '试产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('同时做衍生BOM', '否')
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011331')
        user.input_bomtree('单机头', '用量', '1000')
        user.input_bomtree('指纹模组', '物料编码', '17600563')
        user.input_bomtree('指纹模组', '用量', '1000')
        user.input_bomtree('指纹模组', '替代组', 'A1')
        user.input_bomtree('指纹模组', '份额', '20')
        user.click_optional_material()
        user.move_to_add_material('17600563')
        user.input_optional_material('17600563', '物料编码', '17600606')
        user.input_optional_material('17600563', '用量', '1000')
        user.input_optional_material('17600563', '替代组', 'A1')
        user.input_optional_material('17600563', '份额', '80')
        user.select_business_review('李小素', 'MPM')
        user.click_add_submit()
        user.assert_toast('创建流程成功')
        user.refresh()
        user.assert_add_result('自动化新增用例', '单机头BOM制作', 'X572-1', 'itel', '埃塞本地', '试产阶段', '审批中', '未同步')
        # process_code = user.get_info()[2]
        process_code = user.get_bom_info('单机头BOM协作', '自动化新增用例', '流程编码')
        user.delete_flow(process_code)

    @allure.story("创建流程")
    @allure.title("正确选择物料编码，点击一键填写，填写内容保存正确")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在单机头中和PCBA中正确选择物料编码，选中两颗物料，点击一键填写，填写用量和1000点击确认，页面上显示两颗物料用量都为1000")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_003(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011336')
        user.input_bomtree('电池', '物料编码', '25001649')
        user.click_checkbox()
        user.input_one_press('用量', '1000')
        amount = user.get_bomtree_info('单机头')[7]
        ValueAssert.value_assert_equal(amount, '1000')
        amount = user.get_bomtree_info('电池')[7]
        ValueAssert.value_assert_equal(amount, '1000')

    @allure.story("创建流程")
    @allure.title("BOM tree中不选择物料，页面上不存在删除按钮")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不选择物料，页面上不存在删除按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_004(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.assert_batch_delete(False)

    @allure.story("创建流程")
    @allure.title("选择物料，页面上存在删除按钮")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择物料，页面上存在删除按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_005(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_checkbox()
        user.assert_batch_delete(True)

    @allure.story("创建流程")
    @allure.title("选中父节点物料后点击删除，删除页面数据")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_006(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_bomtree_delete('单机头')
        user.click_batch_confirm()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("创建流程")
    @allure.title("选中子节点物料后点击删除，清子节点内容")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_007(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('电池', '物料编码', '25001649')
        user.input_bomtree('电池', '用量', '1000')
        user.input_bomtree('电池', '替代组', 'A1')
        user.input_bomtree('电池', '份额', '20')
        user.click_bomtree_delete('电池')
        amount = user.get_bomtree_info('电池')[4]
        ValueAssert.value_assert_equal(amount, '')
        amount = user.get_bomtree_info('电池')[7]
        ValueAssert.value_assert_equal(amount, '')
        amount = user.get_bomtree_info('电池')[8]
        ValueAssert.value_assert_equal(amount, '')
        amount = user.get_bomtree_info('电池')[9]
        ValueAssert.value_assert_equal(amount, '')

    @allure.story("创建流程")
    @allure.title("选择正确的文件进行导入，并应用，显示的数据与模板的数据一致")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_008(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_bom_import()
        user.upload_true_file()
        user.assert_upload_result(('1','试产', '12011336', '单机头', '25001649', '电池_Infinix_BL_51BX_5100mAh_ATL_IN_BIS', '1'),)
        user.click_apply()
        user.click_tree('单机头')
        user.assert_tree_result(('1.2', '电池', '25001649', '电池_Infinix_BL_51BX_5100mAh_ATL_IN_BIS', '可选', '1000', '编辑删除'),)


@allure.feature("BOM协作-单机头BOM协作")
class TestCreateProcessExceptionScenario:
    @allure.story("创建流程异常场景")
    @allure.title("导入Bom之前需要选中模板")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个不存在模板的品牌，其他内容正确填写，查看BOM Tree，无新增BOM按钮；点击导入提示-导入Bom之前需要选中模板")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_001(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '单机头BOM制作')
        user.input_add_bom_info('品牌', 'aaaaa')
        user.input_add_bom_info('机型', 'X572-1')
        user.input_add_bom_info('阶段', '试产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('同时做衍生BOM', '否')
        user.base_get_img()
        user.assert_add_bomtree_exist(False)
        user.click_bom_import()
        user.assert_toast('导入Bom之前需要选中模板')

    @allure.story("创建流程异常场景")
    @allure.title("不添加BOM内容，提示BOM状态不能为空")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOM tree中点击新增BOM，不添加BOM内容，其他内容正确填写，点击提交，提示BOM状态不能为空")
    @allure.severity("normal")  # blocker\normal\trivial
    @pytest.mark.UT
    def test_002_002(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_add_submit()
        user.assert_toast('BOM状态不能为空')

    @allure.story("创建流程异常场景")
    @allure.title("不选择BOM状态，提示BOM状态不能为空")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOM tree中点击新增BOM，不选择BOM状态，其他内容正确填写，点击提交，提示BOM状态不能为空")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_003(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('单机头', '物料编码', '12011336')
        user.input_bomtree('单机头', '用量', '1000')
        user.click_add_submit()
        user.assert_toast('BOM状态不能为空')

    @allure.story("创建流程异常场景")
    @allure.title("BOM编码[null]的物料组在对应的模板中未设置！")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOM tree中点击新增BOM，不填写物料编码，其他内容正确填写，点击提交，提示BOM编码[null]的物料组在对应的模板中未设置！")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_004(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '用量', '1000')
        user.select_business_review('李小素', 'MPM')
        user.click_add_submit()
        user.assert_toast('BOM编码[null]的物料组在对应的模板中未设置！')

    @allure.story("创建流程异常场景")
    @allure.title("xxxxxxxx的数量为空")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量不进行填写，点击提交，不能提交成功并给出提示xxxxxxxx的数量为空!")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_005(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011336')
        user.select_business_review('李小素', 'MPM')
        user.click_add_submit()
        user.assert_toast('[12011336]的数量为空!')

    @allure.story("创建流程异常场景")
    @allure.title("父阶BOM料号xxxxxxxx用量不为1000")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1，点击提交，不能提交成功并给出提示父阶BOM料号xxxxxxxx用量不为1000")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_006(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011336')
        user.input_bomtree('单机头', '用量', '1')
        user.base_get_img()
        user.select_business_review('李小素', 'MPM')
        user.click_add_submit()
        user.assert_toast('父阶BOM料号12011336用量不为1000')

    @allure.story("创建流程异常场景")
    @allure.title("用量只能填写非0数字(最多3位小数)")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为非数字类型，点击提交，不能提交成功并给出提示用量只能填写非0数字(最多3位小数)")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_007(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011336')
        user.input_bomtree('单机头', '用量', 'a')
        user.select_business_review('李小素', 'MPM')
        user.click_add_submit()
        user.assert_toast('用量只能填写非0数字(最多3位小数)')

    @allure.story("创建流程异常场景")
    @allure.title("父阶BOM料号XXXXXXXX下的子阶BOM料号XXXXXXXX用量不为1000")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，选择单机头的物料编码，输入PCBA用量为1，点击提示，不能提交成功并给出提示父阶BOM料号XXXXXXXX下的子阶BOM料号XXXXXXXX用量不为1000")
    @allure.severity("normal")
    @pytest.mark.UT
    def test_002_008(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011336')
        user.input_bomtree('单机头', '用量', '1000')
        user.input_bomtree('PCBA', '物料编码', '12101691')
        user.input_bomtree('PCBA', '用量', '1')
        user.select_business_review('李小素', 'MPM')
        user.click_add_submit()
        user.assert_toast('父阶BOM料号12011336下的子阶BOM料号12101691用量不为1000')

    @allure.story("创建流程异常场景")
    @allure.title("业务评审MPM不能为空！")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示业务评审MPM不能为空！")
    @allure.severity("normal")
    @pytest.mark.UT
    def test_002_009(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '单机头BOM制作')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'X572-1')
        user.input_add_bom_info('阶段', '试产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('同时做衍生BOM', '否')
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011336')
        user.input_bomtree('单机头', '用量', '1000')
        user.click_add_submit()
        user.assert_toast('业务评审MPM不能为空！')

    @allure.story("创建流程异常场景")
    @allure.title("业务评审MPM不能为空！")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，业务评审MPM不选择评审人员，其他选择审批人员，点击提交，不能提交成功，并给出提示业务评审MPM不能为空！")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_010(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', '单机头BOM制作')
        user.input_add_bom_info('品牌', 'itel')
        user.input_add_bom_info('机型', 'X572-1')
        user.input_add_bom_info('阶段', '试产阶段')
        user.input_add_bom_info('市场', '埃塞本地')
        user.input_add_bom_info('同时做衍生BOM', '否')
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011336')
        user.input_bomtree('单机头', '用量', '1000')
        user.select_business_review('李小素', '项目经理')
        user.click_add_submit()
        user.assert_toast('业务评审MPM不能为空！')

    @allure.story("创建流程异常场景")
    @allure.title("[XXXXXX] 替代组[XX]的份额总和不为100")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，在充电器中新增两颗物料，添加替代组都为A1，份额为一个20，一个20，其他内容正确填写，点击提交，不能提交成功并且提示替代组&份额相加不为100")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_011(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011336')
        user.input_bomtree('单机头', '用量', '1000')
        user.input_bomtree('电池', '物料编码', '25001649')
        user.input_bomtree('电池', '用量', '1000')
        user.input_bomtree('电池', '替代组', 'A1')
        user.input_bomtree('电池', '份额', '20')
        user.click_optional_material()
        user.move_to_add_material('25001649')
        user.input_optional_material('25001649', '物料编码', '25001643')
        user.input_optional_material('25001649', '用量', '1000')
        user.input_optional_material('25001649', '替代组', 'A1')
        user.input_optional_material('25001649', '份额', '20')
        user.select_business_review('李小素', 'MPM')
        user.click_add_submit()
        user.assert_toast('[12011336] 替代组[A1]的份额总和不为100')

    @allure.story("创建流程异常场景")
    @allure.title("填入产成品数据，不选择物料，一键填写用量，页面上没有填写上任何数据")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，不选择物料，点击一键填写，填写用量为1000，点击确定，页面上没有填写上任何数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_012(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011336')
        user.input_one_press('用量', '1000')
        amount = user.get_bomtree_info('单机头')[7]
        ValueAssert.value_assert_equal(amount, '')

    @allure.story("创建流程异常场景")
    @allure.title("不填写产成品数据，全选一键填写用量，页面上没有填写上任何数据")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产成品中不选择物料编码，全选选中物料，点击一键填写，一键填写时选择用量和1000，点击确定，页面上不会新增用量数量")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_013(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_checkbox()
        user.input_one_press('用量', '1000')
        amount = user.get_bomtree_info('单机头')[7]
        ValueAssert.value_assert_equal(amount, '')

    @allure.story("创建流程异常场景")
    @allure.title("文件类型非excel!")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示文件类型非excel!")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_014(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_bom_import()
        user.upload_wrong_file()
        user.assert_toast('文件类型非excel!')

    @allure.story("创建流程异常场景")
    @allure.title("模板正确内容错误的文件导入失败，并在校验结果给出相应错误提示，导出校验可点击")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_015(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_bom_import()
        user.upload_wrongcontent_file()
        user.assert_wrongcontent_upload_result()

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("[XXXXX] 替代组[XX]只有一颗物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入数据，新增一颗物料，添加替代组为A1，份额为20，其他内容正确填写，点击提交，不能提交成功并且提示替代组只有一颗物料")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_016(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('单机头', 'BOM状态', '试产')
        user.input_bomtree('单机头', '物料编码', '12011331')
        user.input_bomtree('单机头', '用量', '1000')
        user.input_bomtree('指纹模组', '物料编码', '17600563')
        user.input_bomtree('指纹模组', '用量', '1000')
        user.input_bomtree('指纹模组', '替代组', 'A1')
        user.input_bomtree('指纹模组', '份额', '20')
        user.click_add_submit()
        user.assert_toast('[12011331] 替代组[A1]只有一颗物料')


@allure.feature("BOM协作-单机头BOM协作")
class TestTheProcessOfExaminationAndApproval:
    @allure.story("流程审批")
    @allure.title("发起流程，审批页面的数据和发起的数据是一致的")
    @allure.description("发起一个单机头BOM协作，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_001(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.enter_onework_check(BarePhone_API[0])
        sleep(2)
        info1 = user.get_onework_bominfo('制作类型')
        info2 = user.get_onework_bominfo('品牌')
        info3 = user.get_onework_bominfo('机型')
        info4 = user.get_onework_bominfo('阶段')
        info5 = user.get_onework_bominfo('市场')
        ValueAssert.value_assert_equal(info1, '单机头BOM制作')
        ValueAssert.value_assert_equal(info2, 'itel')
        ValueAssert.value_assert_equal(info3, 'X572-1')
        ValueAssert.value_assert_equal(info4, '试产阶段')
        ValueAssert.value_assert_equal(info5, '埃塞本地')
        user.assert_oneworks_bomtree_result(('1', '单机头', '12012025', '单机头_itel_it2173_G1812_B_深蓝_RU_4+4', '可选', '1000'), )
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("补充工厂页面，审批成功")
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示处理成功，并且页面成功跳转;成功处理了补充工厂审核点，我的待办中不存在该条单据在补充工厂审核节点（建议：校验单据号和当前节点）")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_002(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.input_oneworks_plant_info('国内组包工厂', '1051')
        user.click_oneworks_slash()
        user.click_oneworks_plant_check('贴片工厂正确')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_API[0], '补充工厂')

    @allure.story("流程审批")
    @allure.title("结构工程师审核页面，审批成功")
    @allure.description("结构工程师审核页面中，所有数据都正确，点击同意，可以提交成功并给出提示处理成功，审核通过，页面成功跳转;成功处理了结构工程师审核点，我的待办中不存在该条单机在BOM工程师审核节点（建议：校验单据号和当前节点）")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_003(self, drivers, BarePhone_Factory_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.select_business_review('李小素')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_Factory_API[0], '结构工程师审批')

    @allure.story("流程审批")  # 场景名称
    @allure.title("结构工程师审批页面，物料编码和物料描述不能编辑")  # 用例名称
    @allure.description("在结构工程师审批页面中，多次点击单机头列数据，该列物料编码和物料描述是不能再进行编辑")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_004(self, drivers, BarePhone_Factory_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.assert_oneworks_bomtree_edit('单机头', '物料编码')
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("结构工程师审批回退到申请人成功")  # 用例名称
    @allure.description("在结构工程师审批页面中，点击回退，选择回退到申请人，查看我的申请中有该单据，显示回退到申请人")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_005(self, drivers, BarePhone_Factory_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.click_oneworks_rollback('申请人')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_application_flow(BarePhone_Factory_API[0], '退回申请人')

    @allure.story("流程审批")  # 场景名称
    @allure.title("结构工程师审批页面，回退到补充工厂再审核，还是结构工程师审批节点")  # 用例名称
    @allure.description("在我的待办中审批从结构工程师审批页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是结构工程师审批")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_006(self, drivers, BarePhone_Factory_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_Factory_API[0], '补充工厂', True)
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_Factory_API[0], '结构工程师审批', True)

    @allure.story("流程审批")
    @allure.title("结构工程师审批页面，不选择转交人转交，不存在确定转交按钮")
    @allure.description("在结构工程师审批页面中，点击转交，不选择转交的人直接点击确认，选择框自动关闭，下面只有选择转交人和取消按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_007(self, drivers, BarePhone_Factory_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("结构工程师审批页面，选择转交人转交，存在确定转交按钮")
    @allure.description("在结构工程师审批页面中，点击转交，选择转交的人直接点击确认，转交成功，可在转交人账号看到该待办消息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_008(self, drivers, BarePhone_Factory_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("结构工程师审批页面，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在结构工程师审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_009(self, drivers, BarePhone_Factory_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("结构工程师审批页面，转交单据成功")  # 用例名称
    @allure.description("在结构工程师审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_010(self, drivers, BarePhone_Factory_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(BarePhone_Factory_API[0], '陈月')

    @allure.story("流程审批")
    @allure.title("业务审核页面，产成品数据不能编辑")
    @allure.description("在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_011(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.assert_oneworks_bomtree_edit('单机头', '物料编码')
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核成功")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择质量部，在检查结果中选择通过，点击同意按钮，给出提示，并且页面跳转成功，跳转成功后，我的待办中不存在该条业务审核单据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_012(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.click_oneworks_self_inspection('业务类型', '手机')
        user.click_oneworks_self_inspection('检查角色', '质量部(QPM)')
        user.scroll_oneworks_self_inspection()
        user.input_oneworks_inspection_result()
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_application_node(BarePhone_StructureEnginner_API[0], 'BOM工程师审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核页面，回退到补充工厂再审核，还是业务审核节点")  # 用例名称
    @allure.description("在我的待办中审批从业务审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是业务审核节点，而不是BOM工程师节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_013(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_StructureEnginner_API[0], '补充工厂', True)
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_StructureEnginner_API[0], '业务审核', True)

    @allure.story("流程审批")
    @allure.title("业务审核页面，不选择转交人转交，不存在确定转交按钮")
    @allure.description("在业务页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_014(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("业务审核页面，选择转交人转交，存在确定转交按钮")
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_015(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("业务审核页面，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_016(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("业务审核页面，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_017(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(BarePhone_StructureEnginner_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，检查失败项为0，提交成功")  # 用例名称
    @allure.description("在BOM工程师审批中，检查失败项为0时，不填写任何内容，点击同意，可以提交成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_018(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        # user.enter_oneworks_iframe()
        user.assert_toast()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师页面，检查失败项不为0，提交成功")  # 用例名称
    @allure.description("在BOM工程师审批中，检查失败项不为0时，不填写任何内容，点击同意，可以提交成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_019(self, drivers, BarePhone_Approval_Fail_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_Fail_API[0])
        user.bom_check('失败')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.enter_oneworks_iframe()
        user.assert_toast()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("更新子阶BOM，提示刷新成功")  # 用例名称
    @allure.description("在BOM工程师审批中，在BOM工程师审批中，点击更多操作-更新子阶BOM，提示刷新成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_020(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_more()
        user.click_update()
        user.assert_toast('刷新成功！')
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("在BOM工程师页面，拒绝成功")  # 用例名称
    @allure.description("在BOM工程师审批中，点击拒绝，会显示处理成功，并且页面跳转")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_021(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_refuse()
        user.assert_toast('处理成功，审核拒绝')
        user.quit_oneworks()
        user.assert_my_application_flow(BarePhone_Approval_API[0], '审批拒绝')
        process_status = user.get_bom_info('单机头BOM协作', BarePhone_Approval_API[0], '单据状态')
        ValueAssert.value_assert_In(process_status, '审批拒绝')

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师审批回退到结构工程师审批成功")  # 用例名称
    @allure.description("在BOM工程师审批中，点击回退，选择回退到结构工程师审批页面，查看我的待办中存在结构工程师审批节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_022(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_rollback('结构工程师审批')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_Approval_API[0], '结构工程师审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师审批回退到业务审核成功")  # 用例名称
    @allure.description("在BOM工程师审批中，点击回退，选择回退到业务审核页面，查看我的待办中存在业务审核节点")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_023(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_rollback('业务审核')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_Approval_API[0], '业务审核', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师审批回退到申请人成功")  # 用例名称
    @allure.description("在BOM工程师审批中，点击回退，选择回退到申请人，查看我的申请中有该单据，显示回退到申请人")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_024(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_rollback('申请人')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_application_flow(BarePhone_Approval_API[0], '退回申请人')

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师审批页面，回退到补充工厂再审核，还是BOM工程师审批节点")  # 用例名称
    @allure.description("在我的待办中审批从BOM工程师审批回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是BOM工程师审批")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_025(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_Approval_API[0], '补充工厂', True)
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_Approval_API[0], 'BOM工程师审批', True)

    @allure.story("流程审批")
    @allure.title("BOM工程师审批页面，不选择转交人转交，不存在确定转交按钮")
    @allure.description("在BOM工程师审批页面中，点击转交，不选择转交的人直接点击确认，选择框自动关闭，下面只有选择转交人和取消按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_026(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("BOM工程师审批页面，选择转交人转交，存在确定转交按钮")
    @allure.description("在BOM工程师审批页面中，点击转交，选择转交的人直接点击确认，转交成功，可在转交人账号看到该待办消息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_027(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("BOM工程师审批页面，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在BOM工程师审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_028(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("BOM工程师审批页面，转交单据成功")  # 用例名称
    @allure.description("在BOM工程师审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_029(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(BarePhone_Approval_API[0], '陈月')

    @allure.story("流程审批")  # 场景名称
    @allure.title("数据组审批页面，回退到补充工厂再审核，还是BOM工程师审批节点")  # 用例名称
    @allure.description("在我的待办中审批从数据组审批回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是数据组审批")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_030(self, drivers, BarePhone_bomEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_bomEnginner_API[0])
        user.click_oneworks_rollback('补充工厂')
        user.click_oneworks_rollback_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_bomEnginner_API[0], '补充工厂', True)
        user.enter_oneworks_edit(BarePhone_bomEnginner_API[0])
        user.click_oneworks_plant_check('贴片工厂正确')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_bomEnginner_API[0], '数据组审批', True)

    @allure.story("流程审批")
    @allure.title("数据组审批页面，不选择转交人转交，不存在确定转交按钮")
    @allure.description("在数据组审批批页面中，点击转交，不选择转交的人直接点击确认，选择框自动关闭，下面只有选择转交人和取消按钮")
    @allure.severity("normal")
    @pytest.mark.UT  # 用例标记
    def test_003_031(self, drivers, BarePhone_bomEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(False)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("数据组审批页面，选择转交人转交，存在确定转交按钮")
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，转交成功，可在转交人账号看到该待办消息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_032(self, drivers, BarePhone_bomEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.assert_oneworks_comfirmrefer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("数据组审批页面，选择转交人转交取消，存在转交，回退按钮")
    @allure.description("在数据组审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_033(self, drivers, BarePhone_bomEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('李小素')
        user.select_oneworks_refer('李小素')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_cancel()
        user.assert_oneworks_rollback_refer_exist(True)
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("数据组审批页面，转交单据成功")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_003_034(self, drivers, BarePhone_bomEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_bomEnginner_API[0])
        user.click_oneworks_refer()
        user.input_oneworks_refer('陈月')
        user.select_oneworks_refer('陈月')
        user.click_oneworks_refer_comfirm()
        user.click_oneworks_refer_comfirmrefer()
        user.assert_toast()
        user.quit_oneworks()
        user.assert_flow_deliver(BarePhone_bomEnginner_API[0], '陈月')


@allure.feature("BOM协作-单机头BOM协作")
class TestProcessApprovalExceptionScenario:
    @allure.story("流程审批异常场景")
    @allure.title("【生产工厂信息】物料xxxxxx的组包工厂不能为空")
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示【生产工厂信息】物料xxxxxx的组包工厂不能为空")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_001(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.enter_oneworks_iframe()
        user.assert_toast('【生产工厂信息】物料12012025的组包工厂不能为空')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("未选择BOM,一键填写按钮无法被点击")
    @allure.description("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_002(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.assert_oneworks_onepress_write()
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("请选择工厂分类")
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，不进行工厂分类，点击确认，不能进行确认并给出必填提示请选择工厂分类")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_003(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.click_oneworks_checkbox()
        user.click_oneworks_onepress_write()
        user.click_oneworks_onepress_write_confirm()
        DomAssert(drivers).assert_att('请选择工厂分类')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("请选择工厂")
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，不进行选择工厂，点击确认，不能进行确认并给出必填提示请选择工厂")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_004(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.click_oneworks_checkbox()
        user.click_oneworks_onepress_write()
        user.click_oneworks_onepress_write_confirm()
        DomAssert(drivers).assert_att('请选择工厂')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("检查贴片工厂不能为空！")
    @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示检查贴片工厂不能为空！")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_005(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.input_oneworks_plant_info('国内组包工厂', '1051')
        user.click_oneworks_slash()
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.enter_oneworks_iframe()
        user.assert_toast('检查贴片工厂不能为空！')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("父阶BOM料号xxxxxxxx用量不为1000")
    @allure.description("在结构工程师审批页面中，在Bom Tree中点编辑，将用量编辑为1，点击同意，不能提交成功页面给出提示父阶BOM料号xxxxxxxx用量不为1000")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_006(self, drivers, BarePhone_Factory_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.input_bomtree('单机头', '用量', '1')
        user.select_business_review('李小素')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.enter_oneworks_iframe()
        user.assert_toast('父阶BOM料号12012025用量不为1000')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单检查角色未选择")  # 用例名称
    @allure.description("在业务审核页面中，不填写任何内容，点击同意，不能提交成功，并给出提示自检清单检查角色未选择")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_007(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单检查角色未选择')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不通过，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不通过需填写原因及修改建议")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_008(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.click_oneworks_self_inspection('业务类型', '手机')
        user.click_oneworks_self_inspection('检查角色', '质量部(QPM)')
        user.scroll_oneworks_self_inspection()
        user.input_oneworks_inspection_result(result='不通过')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果为不通过需填写原因及修改建议')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不涉及，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不涉及需填写原因及修改建议")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_009(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.click_oneworks_self_inspection('业务类型', '手机')
        user.click_oneworks_self_inspection('检查角色', '质量部(QPM)')
        user.scroll_oneworks_self_inspection()
        user.input_oneworks_inspection_result(result='不涉及')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.enter_oneworks_iframe()
        user.assert_toast('自检清单第【1】行检查结果为不涉及需填写原因及修改建议')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("BOM工程师审批，点击删除BOMTree，提示不能删除BOM")  # 用例名称
    @allure.description("在BOM工程师审批中，在BOMTree中，点击删除，提示不能删除BOM")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_010(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.click_bomtree_delete('12012025')
        user.assert_toast('不能删除BOM')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("BOM工程师审批，点击删除BOMTree，提示不能删除BOM")  # 用例名称
    @allure.description("在BOM工程师审批中，在BOMTree中，点击编辑，可更改用量，将用量改为10000，点击确定，点击同意，提示父阶BOM料号xxxxxxxx用量不为1000")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_011(self, drivers, BarePhone_Approval_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_API[0])
        user.input_bomtree('12012025', '用量', '10000')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.enter_oneworks_iframe()
        user.assert_toast('父阶BOM料号12012025用量不为1000')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")  # 场景名称
    @allure.title("数据组审批页面，检查失败项不为0，提交失败")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查有失败项，点击同意，不能提交成功，并且给出提交失败的提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_004_012(self, drivers, BarePhone_bomEnginner_Fail_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_bomEnginner_Fail_API[0])
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.enter_oneworks_iframe()
        user.assert_toast('子阶bom检查失败，无法同步')
        user.quit_oneworks()


@allure.feature("BOM协作-单机头BOM协作")  # 模块名称
class TestProcessInformationExport:
    @allure.story("流程信息导出")  # 场景名称
    @allure.title("补充工厂页面中，导出的xlsx表的数据和页面的数据是一致")
    @allure.description("在补充工厂页面中，点击导出，导出的xlsx表的数据和页面的数据是一致的")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    @pytest.mark.skip
    def test_005_001(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.assert_oneworks_factoryinfo()
        user.quit_oneworks()

    @allure.story("流程信息导出")
    @allure.title("结构工程师审批页面，Bom Tree导出数据一致")
    @allure.description("在结构工程师审批页面中，在Bom Tree中点导出，导出的数据和Bom Tree的数据是一致的")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    @pytest.mark.skip
    def test_005_002(self, drivers, BarePhone_Factory_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Factory_API[0])
        user.assert_oneworks_approval_bominfo()
        user.quit_oneworks()

    @allure.story("流程信息导出")
    @allure.title("在业务审核页面中，在生产工厂信息导出的数据和页面的数据是一致的")
    @allure.description("在业务审核页面中，在生产工厂信息中点击导出，导出文件中的数据和页面的数据是一致的")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    @pytest.mark.skip
    def test_005_003(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.assert_oneworks_factoryinfo()
        user.quit_oneworks()

    @allure.story("流程信息导出")
    @allure.title("在业务审核页面中，在BOM Tree导出的数据和页面的数据是一致的")
    @allure.description("在业务审核页面中，点击BOM Tree中的导出，导出文件中的数据和页面中的数据是一致的")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    @pytest.mark.skip
    def test_005_004(self, drivers, BarePhone_StructureEnginner_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_StructureEnginner_API[0])
        user.assert_oneworks_approval_bominfo()
        user.quit_oneworks()

    @allure.story("流程信息导出")
    @allure.title("在BOM工程师审批中，子阶BOM检查内容导出和页面的数据是一致的")
    @allure.description("在BOM工程师审批中，在BOM工程师审批中，点击导出，可以导出子阶BOM检查内容")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    @pytest.mark.skip
    def test_005_005(self, drivers, BarePhone_Approval_Fail_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_Approval_Fail_API[0])
        user.assert_oneworks_approval_bomcheck()
        user.quit_oneworks()


@allure.feature("BOM协作-单机头BOM协作")  # 模块名称
class TestProcessSearch:


    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，标题查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入“李小素”，点击查询，查询结果为所有标题包含“李小素”的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_001(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '李小素')
        user.click_search()
        user.assert_search_result('标题', '李小素')


    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，查询不存在标题，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的标题，点击查询，查询结果为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_002(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', 'sfdasdfwefw')
        user.click_search()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，流程编码查询结果正确")  # 用例名称
    @allure.description("在查询页面，流程编码输入框输入“1”，点击查询，查询结果为所有流程编码包含“1”的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_003(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('流程编码', '1')
        user.click_search()
        user.assert_search_result('流程编码', '1')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，查询不存在流程编码，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的流程编码，点击查询，查询结果为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_004(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('流程编码', 'sfdasdfwefw')
        user.click_search()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，单机头BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为单机头BOM制作，点击查询，查询结果为所有制作类型为单机头BOM制作的信息息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_005(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', '单机头BOM制作')
        user.click_search()
        user.assert_search_result('制作类型', '单机头BOM制作')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，单机头BOM衍生查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为单机头BOM衍生，点击查询，查询结果为所有制作类型为单机头BOM衍生的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_006(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', '单机头BOM衍生')
        user.click_search()
        user.assert_search_result('制作类型', '单机头BOM衍生')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，二级BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为二级BOM制作，点击查询，查询结果为所有制作类型为二级BOM制作的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_007(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', '二级BOM制作')
        user.click_search()
        user.assert_search_result('制作类型', '二级BOM制作')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，预加工件/虚拟件制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为预加工件/虚拟件制作，点击查询，查询结果为所有制作类型为预加工件/虚拟件制作的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_008(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', '预加工件/虚拟件制作')
        user.click_search()
        user.assert_search_result('制作类型', '预加工件/虚拟件制作')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，预加工件/虚拟件衍生查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为预加工件/虚拟件衍生，点击查询，查询结果为所有制作类型为预加工件/虚拟件衍生的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_009(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('制作类型', '预加工件/虚拟件衍生')
        user.click_search()
        user.assert_search_result('制作类型', '预加工件/虚拟件衍生')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，组合查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入“李小素”，流程编码输入框输入“1”，下拉框选择为单机头BOM制作，点击查询，查询结果为所有标题包含“李小素”、流程编码包含“1”、制作类型为客供BOM制作的信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_010(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '李小素')
        user.input_search_info('流程编码', '1')
        user.input_search_info('制作类型', '单机头BOM制作')
        user.click_search()
        user.assert_search_result('制作类型', '单机头BOM制作')
        user.assert_search_result('流程编码', '1')
        user.assert_search_result('标题', '李小素')

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，编辑正常")  # 用例名称
    @allure.description("在查询页面，点击编辑，跳转至oneworks编辑页面，可以编辑页面信息、提交、保存")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_011(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '自动化查询用例')
        user.click_search()
        user.click_edit('自动化查询用例')
        user.select_business_review('李小素', 'MPM')
        user.click_add_save()
        DomAssert(drivers).assert_att('保存草稿成功')
        user.click_edit('自动化查询用例')
        user.click_add_submit()
        DomAssert(drivers).assert_att('创建流程成功')
        user.input_search_info('标题', '自动化查询用例')
        user.click_search()
        code = user.get_bom_info('单机头BOM协作', '自动化查询用例', '流程编码')
        user.recall_process(code)

    @allure.story("流程查询")  # 场景名称
    @allure.title("在查询页面，删除取消无变动")  # 用例名称
    @allure.description("在查询页面，点击删除，提示是否确认删除，点击取消，取消成功，页面无变动")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_006_012(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.input_search_info('标题', '自动化查询用例')
        user.click_search()
        user.click_delete('自动化查询用例')
        user.click_delete_cancel()
        user.click_search()
        user.assert_search_result('标题', '自动化查询用例')


if __name__ == '__main__':
    pytest.main(['BareMobilePhoneBomCooperation.py'])
