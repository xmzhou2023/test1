import pytest
from public.base.assert_ui import *
from project.TBM.page_object.BOMCooperation_BareMobilePhoneBomCooperation import BareMobilePhoneBomCooperation

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""


@allure.feature("BOM协作-单机头BOM协作")
class TestCreateProcess:

    @allure.story("创建流程")
    @allure.title("创建流程成功")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，"
                        "在产出品选择一个物料编码，用量填写为1000，点击提交，能提交成功“创建流程成功”")
    @allure.severity("blocker")  # blocker\\normal\\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011067')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_exact_att('创建流程成功')
        user.refresh()
        user.assert_bare_mobile_phone_bom_cooperation_add_result('单机头BOM制作', 'X572-1', 'itel', '埃塞本地', '试产阶段', '审批中',
                                                                 '未同步')
        process_code = user.get_bare_mobile_phone_bom_cooperation_info()[2]
        user.delete_flow(process_code)

    @allure.story("创建流程")
    @allure.title("创建流程成功")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，正确填入产成品数据，在指纹模组中新增两颗物料，添加替代组都为A1，份额为一个20，一个80，其他内容正确填写，点击提交，能提交成功并且提示“创建流程成功”")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011331')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('指纹模组', '物料编码', '17600563')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('指纹模组', '用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('指纹模组', '替代组', 'A1')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('指纹模组', '份额', '20')
        user.click_bare_mobile_phone_bom_cooperation_optional_material()
        user.move_to_add_material('17600563')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('17600563', '物料编码', '17600606')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('17600563', '用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('17600563', '替代组', 'A1')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('17600563', '份额', '80')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('创建流程成功')
        user.refresh()
        user.assert_bare_mobile_phone_bom_cooperation_add_result('单机头BOM制作', 'X572-1', 'itel', '埃塞本地', '试产阶段', '审批中',
                                                                 '未同步')
        process_code = user.get_bare_mobile_phone_bom_cooperation_info()[2]
        user.delete_flow(process_code)

    @allure.story("创建流程")
    @allure.title("正确选择物料编码，点击一键填写，填写内容保存正确")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，在单机头中和PCBA中正确选择物料编码，选中两颗物料，点击一键填写，填写用量和1000点击确认，页面上显示两颗物料用量都为1000")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_003(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '物料编码', '25001649')
        user.click_bare_mobile_phone_bom_cooperation_checkbox()
        user.input_bare_mobile_phone_bom_cooperation_one_press('用量', '1000')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('单机头')[7]
        ValueAssert.value_assert_equal(amount, '1000')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('电池')[7]
        ValueAssert.value_assert_equal(amount, '1000')

    @allure.story("创建流程")
    @allure.title("BOM tree中不选择物料，页面上不存在删除按钮")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不选择物料，页面上不存在删除按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_004(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.assert_bare_mobile_phone_bom_cooperation_batch_delete(False)

    @allure.story("创建流程")
    @allure.title("选择物料，页面上存在删除按钮")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择物料，页面上存在删除按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_005(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_checkbox()
        user.assert_bare_mobile_phone_bom_cooperation_batch_delete(True)

    @allure.story("创建流程")
    @allure.title("选中父节点物料后点击删除，删除页面数据")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_006(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_bomtree_delete('单机头')
        user.click_bare_mobile_phone_bom_cooperation_batch_confirm()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("创建流程")
    @allure.title("选中子节点物料后点击删除，清子节点内容")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_007(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '物料编码', '25001649')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '替代组', 'A1')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '份额', '20')
        user.click_bare_mobile_phone_bom_cooperation_bomtree_delete('电池')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('电池')[4]
        ValueAssert.value_assert_equal(amount, '')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('电池')[7]
        ValueAssert.value_assert_equal(amount, '')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('电池')[8]
        ValueAssert.value_assert_equal(amount, '')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('电池')[9]
        ValueAssert.value_assert_equal(amount, '')

    # @allure.story("创建流程")
    # @allure.title("选中子节点物料后点击删除，清子节点内容")
    # @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，"
    #                     "选择导入BOM选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")
    # @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.UT
    # def test_001_008(self, drivers):
    #     user = BareMobilePhoneBomCooperation(drivers)
    #     user.refresh_webpage_click_menu()
    #     user.bare_mobile_phone_bom_cooperation_add_bom_info()
    #     user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
    #     user.click_bare_mobile_phone_bom_cooperation_bom_import()
    #     user.upload_bare_mobile_phone_bom_cooperation_true_file()


@allure.feature("BOM协作-单机头BOM协作")
class TestCreateProcessExceptionScenario:

    @allure.story("创建流程异常场景")
    @allure.title("导入Bom之前需要选中模板")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个不存在模板的品牌，其他内容正确填写，"
                        "查看BOM Tree，无新增BOM按钮；点击导入提示'导入Bom之前需要选中模板'")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_001(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'aaaaa')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.assert_bare_mobile_phone_bom_cooperation_add_bomtree_exist(False)
        user.click_bare_mobile_phone_bom_cooperation_bom_import()
        DomAssert(drivers).assert_att('导入Bom之前需要选中模板')

    @allure.story("创建流程异常场景")
    @allure.title("不添加BOM内容，提示BOM状态不能为空")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOM tree中点击新增BOM，不添加BOM内容，"
                        "其他内容正确填写，点击提交，提示BOM状态不能为空")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_002(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('BOM状态不能为空')

    @allure.story("创建流程异常场景")
    @allure.title("不选择BOM状态，提示BOM状态不能为空")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOM tree中点击新增BOM，不选择BOM状态，"
                        "其他内容正确填写，点击提交，提示BOM状态不能为空")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_003(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('BOM状态不能为空')

    @allure.story("创建流程异常场景")
    @allure.title("BOM编码[null]的物料组在对应的模板中未设置！")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOM tree中点击新增BOM，不填写物料编码，"
                        "其他内容正确填写，点击提交，提示BOM编码[null]的物料组在对应的模板中未设置！")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_004(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('BOM编码[null]的物料组在对应的模板中未设置！')

    @allure.story("创建流程异常场景")
    @allure.title("xxxxxxxx的数量为空")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，"
                        "在产出品选择一个物料编码，用量不进行填写，点击提交，不能提交成功并给出提示“xxxxxxxx的数量为空!”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_005(self, drivers):
        """
        回归测试用例：005
        用例：进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，
            用量不进行填写，点击提交，不能提交成功并给出提示“xxxxxxxx的数量为空!”
        """
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('[12011336]的数量为空!')

    @allure.story("创建流程异常场景")
    @allure.title("父阶BOM料号xxxxxxxx用量不为1000")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，"
                        "在产出品选择一个物料编码，用量填写为1，点击提交，不能提交成功并给出提示“父阶BOM料号xxxxxxxx用量不为1000”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_006(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('父阶BOM料号12011336用量不为1000')

    @allure.story("创建流程异常场景")
    @allure.title("用量只能填写非0数字(最多3位小数)")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，"
                        "在产出品选择一个物料编码，用量填写为非数字类型，点击提交，不能提交成功并给出提示“用量只能填写非0数字(最多3位小数)”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_007(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', 'a')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('用量只能填写非0数字(最多3位小数)')

    @allure.story("创建流程异常场景")
    @allure.title("父阶BOM料号XXXXXXXX下的子阶BOM料号XXXXXXXX用量不为1000")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，"
                        "选择单机头的物料编码，输入PCBA用量为1，点击提示，不能提交成功并给出提示“父阶BOM料号XXXXXXXX下的子阶BOM"
                        "料号XXXXXXXX用量不为1000”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_008(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('PCBA', '物料编码', '12101691')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('PCBA', '用量', '1')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('父阶BOM料号12011336下的子阶BOM料号12101691用量不为1000')

    @allure.story("创建流程异常场景")
    @allure.title("业务评审MPM不能为空！")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示“业务评审MPM不能为空！”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_009(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('业务评审MPM不能为空！')

    @allure.story("创建流程异常场景")
    @allure.title("业务评审MPM不能为空！")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确填入产成品数据，"
                        "业务评审MPM不选择评审人员，其他选择审批人员，点击提交，不能提交成功，并给出提示“业务评审MPM不能为空！”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_010(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素', '项目经理')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('业务评审MPM不能为空！')

    @allure.story("创建流程异常场景")
    @allure.title("[XXXXXX] 替代组[XX]的份额总和不为100")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，正确填入产成品数据，在充电器中新增两颗物料，添加替代组都为A1，份额为一个20，一个20"
                        "，其他内容正确填写，点击提交，不能提交成功并且提示替代组&份额相加不为100")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_011(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '物料编码', '25001649')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '替代组', 'A1')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '份额', '20')
        user.click_bare_mobile_phone_bom_cooperation_optional_material()
        user.move_to_add_material('25001649')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('25001649', '物料编码', '25001643')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('25001649', '用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('25001649', '替代组', 'A1')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('25001649', '份额', '20')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('[12011336] 替代组[A1]的份额总和不为100')

    @allure.story("创建流程异常场景")
    @allure.title("填入产成品数据，不选择物料，一键填写用量，页面上没有填写上任何数据")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，正确填入产成品数据，不选择物料，点击一键填写，填写用量为1000，点击确定，页面上没有填写上任何数据")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_012(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_one_press('用量', '1000')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('单机头')[7]
        ValueAssert.value_assert_equal(amount, '')

    @allure.story("创建流程异常场景")
    @allure.title("不填写产成品数据，全选一键填写用量，页面上没有填写上任何数据")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，在产成品中不选择物料编码，全选选中物料，点击一键填写，一键填写时选择用量和1000，点击确定，页面上不会新增用量数量")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_013(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_checkbox()
        user.input_bare_mobile_phone_bom_cooperation_one_press('用量', '1000')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('单机头')[7]
        ValueAssert.value_assert_equal(amount, '')

    @allure.story("创建流程异常场景")
    @allure.title("文件类型非excel!")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示“文件类型非excel!”")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_014(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_bom_import()
        user.upload_bare_mobile_phone_bom_cooperation_wrong_file()
        DomAssert(drivers).assert_att('文件类型非excel!')

    @allure.story("创建流程异常场景")
    @allure.title("模板正确内容错误的文件导入失败，并在校验结果给出相应错误提示，导出校验可点击")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_015(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_bom_import()
        user.upload_bare_mobile_phone_bom_cooperation_wrongcontent_file()
        user.assert_bare_mobile_phone_bom_cooperation_wrongcontent_upload_result()


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
        user.enter_bare_mobile_phone_bom_cooperation_onework_check(BarePhone_API[0])
        sleep(2)
        info1 = user.get_bare_mobile_phone_bom_cooperation_onework_bominfo('制作类型')
        info2 = user.get_bare_mobile_phone_bom_cooperation_onework_bominfo('品牌')
        info3 = user.get_bare_mobile_phone_bom_cooperation_onework_bominfo('机型')
        info4 = user.get_bare_mobile_phone_bom_cooperation_onework_bominfo('阶段')
        info5 = user.get_bare_mobile_phone_bom_cooperation_onework_bominfo('市场')
        ValueAssert.value_assert_equal(info1, '单机头BOM制作')
        ValueAssert.value_assert_equal(info2, 'itel')
        ValueAssert.value_assert_equal(info3, 'X572-1')
        ValueAssert.value_assert_equal(info4, '试产阶段')
        ValueAssert.value_assert_equal(info5, '埃塞本地')
        user.assert_bare_mobile_phone_bom_cooperation_oneworks_bomtree_result(
            ('1', '单机头', '12012025', '单机头_itel_it2173_G1812_B_深蓝_RU_4+4', '可选', '1000'), )
        user.quit_oneworks()

    @allure.story("流程审批")
    @allure.title("补充工厂页面，审批成功")
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示“处理成功”，并且页面成功跳转;"
                        "成功处理了补充工厂审核点，我的待办中不存在该条单据在补充工厂审核节点（建议：校验单据号和当前节点）")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_002(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.input_bare_mobile_phone_bom_cooperation_oneworks_plant_info('国内组包工厂', '1051')
        user.click_bare_mobile_phone_bom_cooperation_oneworks_slash()
        user.click_bare_mobile_phone_bom_cooperation_oneworks_plant_check('贴片工厂正确')
        user.click_bare_mobile_phone_bom_cooperation_oneworks_agree()
        user.click_bare_mobile_phone_bom_cooperation_oneworks_confirm()
        DomAssert(drivers).assert_att('处理成功，审核通过')
        user.quit_oneworks()
        user.assert_my_todo_node(BarePhone_API[0], '补充工厂')

    # @allure.story("流程审批")
    # @allure.title("结构工程师审核页面，审批成功")
    # @allure.description("结构工程师审核页面中，所有数据都正确，点击同意，可以提交成功并给出提示“处理成功，审核通过”，页面成功跳转;"
    #                     "成功处理了结构工程师审核点，我的待办中不存在该条单机在BOM工程师审核节点（建议：校验单据号和当前节点）")
    # @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.UT
    # def test_003_003(self, drivers, BarePhone_API):
    #     user = BareMobilePhoneBomCooperation(drivers)
    #     user.refresh_webpage()
    #     user.bare_mobile_phone_bom_cooperation_supplementary_factory_flow(BarePhone_API[0])
    #     user.enter_bare_mobile_phone_bom_cooperation_onework_edit(BarePhone_API[0])
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_agree()
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_confirm()
    #     DomAssert(drivers).assert_att('处理成功，审核通过')
    #     user.quit_oneworks()
    #     user.assert_my_todo_node(BarePhone_API[0], 'BOM工程师审核')

    # @allure.story("流程审批")
    # @allure.title("补充工厂页面中，导出的xlsx表的数据和页面的数据是一致")
    # @allure.description("在补充工厂页面中，点击导出，导出的xlsx表的数据和页面的数据是一致的")
    # @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.UT
    # def test_003_003(self, drivers, BarePhone_API):
    #     user = BareMobilePhoneBomCooperation(drivers)
    #     user.refresh_webpage()
    #     user.enter_bare_mobile_phone_bom_cooperation_onework_edit(BarePhone_API[0])
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_checkbox()
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_approval_export()
    #     user.assert_bare_mobile_phone_bom_cooperation_oneworks_factoryinfo()
    #     user.quit_oneworks()
    #
    # @allure.story("流程审批")
    # @allure.title("BOM工程师页面，Bom Tree导出数据一致")
    # @allure.description("在结构工程师审批页面中，在Bom Tree中点导出，导出的数据和Bom Tree的数据是一致的")
    # @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.UT
    # def test_003_004(self, drivers, BarePhone_API):
    #     user = BareMobilePhoneBomCooperation(drivers)
    #     user.refresh_webpage()
    #     user.enter_bare_mobile_phone_bom_cooperation_onework_edit(BarePhone_API[0])
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_checkbox()
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_approval_export()
    #     user.assert_bare_mobile_phone_bom_cooperation_oneworks_approval_bominfo()
    #     user.quit_oneworks()



@allure.feature("BOM协作-单机头BOM协作")
class TestProcessApprovalExceptionScenario:
    @allure.story("流程审批异常场景")
    @allure.title("【生产工厂信息】物料xxxxxx的组包工厂不能为空")
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示“【生产工厂信息】物料xxxxxx的组包工厂不能为空”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_001(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.click_bare_mobile_phone_bom_cooperation_oneworks_agree()
        user.click_bare_mobile_phone_bom_cooperation_oneworks_confirm()
        user.enter_oneworks_iframe()
        DomAssert(drivers).assert_att('【生产工厂信息】物料12012025的组包工厂不能为空')
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
        user.assert_bare_mobile_phone_bom_cooperation_oneworks_onepress_write()
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("请选择工厂分类")
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，不进行工厂分类，点击确认，不能进行确认并给出必填提示“请选择工厂分类”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_003(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.click_bare_mobile_phone_bom_cooperation_oneworks_checkbox()
        user.click_bare_mobile_phone_bom_cooperation_oneworks_onepress_write()
        user.click_bare_mobile_phone_bom_cooperation_oneworks_onepress_write_confirm()
        DomAssert(drivers).assert_att('请选择工厂分类')
        user.quit_oneworks()

    @allure.story("流程审批异常场景")
    @allure.title("请选择工厂")
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，不进行选择工厂，点击确认，不能进行确认并给出必填提示“请选择工厂”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_004_004(self, drivers, BarePhone_API):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(BarePhone_API[0])
        user.click_bare_mobile_phone_bom_cooperation_oneworks_checkbox()
        user.click_bare_mobile_phone_bom_cooperation_oneworks_onepress_write()
        user.click_bare_mobile_phone_bom_cooperation_oneworks_onepress_write_confirm()
        DomAssert(drivers).assert_att('请选择工厂')
        user.quit_oneworks()

    # @allure.story("流程审批异常场景")
    # @allure.title("检查贴片工厂不能为空！")
    # @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示“检查贴片工厂不能为空！”")
    # @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.UT
    # def test_004_005(self, drivers, BarePhone_API):
    #     user = BareMobilePhoneBomCooperation(drivers)
    #     user.refresh_webpage()
    #     user.enter_bare_mobile_phone_bom_cooperation_onework_edit(BarePhone_API[0])
    #     user.input_bare_mobile_phone_bom_cooperation_oneworks_plant_info('国内组包工厂', '1051')
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_slash()
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_agree()
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_confirm()
    #     user.enter_onework_iframe()
    #     DomAssert(drivers).assert_att('检查贴片工厂不能为空！')
    #     user.quit_oneworks)
    #
    # @allure.story("流程审批异常场景")
    # @allure.title("父阶BOM料号xxxxxxxx用量不为1000")
    # @allure.description("在结构工程师审批页面中，在Bom Tree中点编辑，将用量编辑为“1”，"
    #                     "点击同意，不能提交成功页面给出提示“父阶BOM料号xxxxxxxx用量不为1000”")
    # @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.UT
    # def test_004_006(self, drivers, BarePhone_API):
    #     user = BareMobilePhoneBomCooperation(drivers)
    #     user.refresh_webpage()
    #     user.bare_mobile_phone_bom_cooperation_supplementary_factory_flow(BarePhone_API[0])
    #     user.enter_bare_mobile_phone_bom_cooperation_onework_edit(BarePhone_API[0])
    #     user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('产成品', '用量', '1')
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_agree()
    #     user.click_bare_mobile_phone_bom_cooperation_oneworks_confirm()
    #     user.enter_oneworks_iframe()
    #     DomAssert(drivers).assert_att('父阶BOM料号12012025用量不为1000')
    #     user.quit_oneworks()


if __name__ == '__main__':
    pytest.main(['BOMCooperation_BareMobilePhoneBomCooperation.py'])
