import allure
import pytest
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

@allure.feature("BOM协作-外研协作")  # 模块名称
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
        user.refresh()
        user.assert_add_result('客供BOM制作', 'JMB-01', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_info()[2]
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
        user.assert_add_result('客供BOM制作', 'JMB-01', 'itel', '量产阶段', '审批中', '埃塞本地')
        process_code = user.get_info()[2]
        user.delete_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("选择物料编码，点击一键填写，填写内容保存正确")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产成品中和单机头中正确选择物料编码，选中两颗物料，点击一键填写，填写用量和1000点击确认，页面上显示两颗物料用量都为1000")
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
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不选择物料，页面上不存在删除按钮")
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
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择物料，页面上存在删除按钮")
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
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_006(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.click_bomtree_delete('客供BOM')
        user.click_batch_confirm()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("创建流程")
    @allure.title("选中子节点物料后点击删除，清子节点内容")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_001_007(self, drivers):
        user = ForeignBom(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('客供BOM','BOM状态', '量产')
        user.input_bomtree('客供BOM','物料编码', '12004871')
        user.input_bomtree('客供BOM','用量', '1000')
        user.click_optional_material()
        user.input_optional_material('12004871', '物料编码', '12800002')
        user.input_optional_material('12004871', '用量', '1000')
        user.input_optional_material('12004871', '替代组', 'A1')
        user.input_optional_material('12004871', '份额', '20')
        user.click_bomtree_delete('12004871')
        amount = user.get_bomtree_info('电池')[4]
        ValueAssert.value_assert_equal(amount, '')
        amount = user.get_bomtree_info('电池')[7]
        ValueAssert.value_assert_equal(amount, '')
        amount = user.get_bomtree_info('电池')[8]
        ValueAssert.value_assert_equal(amount, '')
        amount = user.get_bomtree_info('电池')[9]
        ValueAssert.value_assert_equal(amount, '')

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
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产成品中和单机头中正确选择物料编码，选中两颗物料，点击一键填写，选择用量，并且不填写字段值，点击确认，给出必填提示，提示为不能为空")
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

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
