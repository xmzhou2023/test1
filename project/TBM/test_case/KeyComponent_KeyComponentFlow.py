import pytest
from public.base.assert_ui import *
from project.TBM.page_object.KeyComponent_KeyComponentFlow import KeyComponentsFlow


@allure.feature("关键器件-关键器件流程")  # 模块名称
class TestCreateProcess:
    @allure.story("创建流程")  # 场景名称
    @allure.title("创建流程成功")  # 用例名称
    @allure.description("进入新增页面，输入项目信息（项目输入未存在的项目，其他随便填），填写业务审核，点击提交，提示操作成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers, KeyDevice_SQL_50A712U):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.add_item_info()
        user.add_business_review()
        user.click_add_submit()
        user.assert_toast()
        process_code = user.get_info("关键器件", "关键器件流程")[1]
        user.delete_flow(process_code)


@allure.feature("关键器件-关键器件流程")  # 模块名称
class TestTheProcessOfExaminationAndApproval:
    @allure.story("流程审批")  # 场景名称
    @allure.title("摄像头+闪光灯节点，审批成功")  # 用例名称
    @allure.description("摄像头+闪光灯节点，关键器件中的摄像头+闪光灯节点，点击左侧三角，点击下面的模块，点击物料编码右侧的加号，物料编码下面出现一行，点击新出现这行的加号，填写代申请编码信息，点击其他模块保存成功（像这样随便填几个模块），点击同意，提示操作成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_001(self, drivers, KeyDevice_API):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_API[0], '摄像头+闪光灯')
        user.click_Device_unfold('摄像头+闪光灯')
        user.click_Device_module('CTP')
        user.click_Device_code_add()
        user.click_Device_material_add('CTP(1供)')
        user.click_Device_pending_code('CTP(1供)')
        user.input_KeyDevice_Evaluation_content('物料详情（参数）', '物料属性', '属性test')
        user.input_KeyDevice_Evaluation_content('参数', '技术类型', 'GFF')
        user.input_KeyDevice_Evaluation_content('参数', 'CG颜色', 'CG颜色test')
        user.input_KeyDevice_Evaluation_content('参数', '接口类型', '接口类型test')
        user.input_KeyDevice_Evaluation_content('参数', '连接方式', '焊接')
        user.assert_OneWorks_AgreeFlow()

    @allure.story("流程审批")  # 场景名称
    @allure.title("硬件电子料-基带节点，审批成功")  # 用例名称
    @allure.description("硬件电子料-基带节点，关键器件中的硬件电子料-基带节点，点击左侧三角，点击下面的模块，点击物料编码右侧的加号，物料编码下面出现一行，点击新出现这行的加号，填写代申请编码信息，点击其他模块保存成功（像这样随便填几个模块），点击同意，提示操作成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_002(self, drivers, KeyDevice_API):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_API[0], '硬件电子料-基带')
        user.click_Device_unfold('硬件电子料-基带')
        user.click_Device_module('CPU')
        user.click_Device_code_add()
        user.click_Device_material_add('CPU(1供)')
        user.click_Device_pending_code('CPU(1供)')
        user.input_KeyDevice_Evaluation_content('物料详情（参数）', '物料属性', '属性test')
        user.assert_OneWorks_AgreeFlow()

    @allure.story("流程审批")  # 场景名称
    @allure.title("标准化代表节点，审批成功")  # 用例名称
    @allure.description("标准化代表节点，找到标准化评估责任人，点击左侧全选，点击右侧一键填写，弹出一键填写框，字段名称选择责任人，责任人选择xxx，点击确定，提示已选分类的审批人设置成功，点击关闭按钮，弹框关闭，点击同意，提示操作成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_003(self, drivers, KeyDevice_nodeMat_API):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_nodeMat_API[0], '标准化代表')
        user.click_Device_checkbox()
        user.click_one_press()
        user.input_KeyDevice_OnePress('责任人', '李小素')
        user.click_OnePress_confirm()
        user.click_OnePress_cancel()
        user.assert_OneWorks_AgreeFlow()

    @allure.story("流程审批")  # 场景名称
    @allure.title("采购代表节点，审批成功")  # 用例名称
    @allure.description("采购代表节点，找到采购评估责任人，点击左侧全选，点击右侧一键填写，弹出一键填写框，字段名称选择资源商务，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购执行，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购PTC，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购SQM，责任人选择xxx，点击确定。提示已选分类的审批人设置成功，点击关闭按钮，弹框关闭，点击同意，提示操作成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_004(self, drivers, KeyDevice_nodeMat_API):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_nodeMat_API[0], '采购代表')
        user.click_Device_checkbox()
        user.click_one_press()
        user.input_KeyDevice_OnePress('资源商务', '李小素')
        user.click_OnePress_confirm()
        DomAssert(drivers).assert_att('已选分类的审批人设置成功')
        user.input_KeyDevice_OnePress('采购执行', '李小素')
        user.click_OnePress_confirm()
        DomAssert(drivers).assert_att('已选分类的审批人设置成功')
        user.input_KeyDevice_OnePress('采购PTC', '李小素')
        user.click_OnePress_confirm()
        DomAssert(drivers).assert_att('已选分类的审批人设置成功')
        user.input_KeyDevice_OnePress('采购SQM', '李小素')
        user.click_OnePress_confirm()
        DomAssert(drivers).assert_att('已选分类的审批人设置成功')
        user.click_OnePress_cancel()
        user.assert_OneWorks_AgreeFlow()

    @allure.story("流程审批")  # 场景名称
    @allure.title("资源商务评估节点，审批成功")  # 用例名称
    @allure.description("资源商务评估节点，（所有前面填过信息的这里都可以填采购评估-资源商务）勾选是否新供应商、国产化属性、供应商选择原因类别、是否客供物料、价格趋势（6个月）、是否NUDD、评审结论（选通过或者选建议修改，填原因及修改建议），填写供应商选择原因、份额（只能输数字1-100）、关联物料（只能填物料）、NUDD说明、NUDD管理方案、原因及修改建议；点击同意，有必填不填时有提示，点击确定")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_005(self, drivers, KeyDevice_Approver_API):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Approver_API[0], '资源商务评估')
        user.click_Device_unfold('摄像头+闪光灯')
        user.click_Device_module('CTP')
        user.click_Device_pending_code('CTP(1供)')
        user.input_KeyDevice_Evaluation_content('资源商务', '供应商名称', 'TEST')
        user.input_KeyDevice_Evaluation_content('资源商务', '是否新供应商', '否')
        user.input_KeyDevice_Evaluation_content('资源商务', '国产化属性', '0')
        user.input_KeyDevice_Evaluation_content('资源商务', '供应商选择原因类别', '成本因素')
        user.input_KeyDevice_Evaluation_content('资源商务', '供应商选择原因', '供应商选择原因TEST')
        user.input_KeyDevice_Evaluation_content('资源商务', '份额', '50')
        user.input_KeyDevice_Evaluation_content('资源商务', '是否客供物料', '是')
        user.input_KeyDevice_Evaluation_content('资源商务', '价格趋势（6个月）', '持平')
        user.input_KeyDevice_Evaluation_content('资源商务', '是否NUDD', '是')
        user.input_KeyDevice_Evaluation_content('资源商务', 'NUDD说明', 'NUDD说明TEST')
        user.input_KeyDevice_Evaluation_content('资源商务', 'NUDD管理方案', 'NUDD管理方案TEST')
        user.input_KeyDevice_Evaluation_content('资源商务', '评审结论', '通过')
        user.input_KeyDevice_Evaluation_content('资源商务', '原因及修改建议', '原因及修改建议TEST')
        user.click_Device_unfold('硬件电子料-基带')
        user.click_Device_module('CPU')
        user.click_Device_pending_code('CPU(1供)')
        user.input_KeyDevice_Evaluation_content('资源商务', '供应商名称', 'TEST')
        user.input_KeyDevice_Evaluation_content('资源商务', '是否新供应商', '否')
        user.input_KeyDevice_Evaluation_content('资源商务', '国产化属性', '0')
        user.input_KeyDevice_Evaluation_content('资源商务', '供应商选择原因类别', '成本因素')
        user.input_KeyDevice_Evaluation_content('资源商务', '供应商选择原因', '供应商选择原因TEST')
        user.input_KeyDevice_Evaluation_content('资源商务', '份额', '50')
        user.input_KeyDevice_Evaluation_content('资源商务', '是否客供物料', '是')
        user.input_KeyDevice_Evaluation_content('资源商务', '价格趋势（6个月）', '持平')
        user.input_KeyDevice_Evaluation_content('资源商务', '是否NUDD', '是')
        user.input_KeyDevice_Evaluation_content('资源商务', 'NUDD说明', 'NUDD说明TEST')
        user.input_KeyDevice_Evaluation_content('资源商务', 'NUDD管理方案', 'NUDD管理方案TEST')
        user.input_KeyDevice_Evaluation_content('资源商务', '评审结论', '通过')
        user.input_KeyDevice_Evaluation_content('资源商务', '原因及修改建议', '原因及修改建议TEST')
        user.assert_OneWorks_AgreeFlow()

    @allure.story("流程审批")  # 场景名称
    @allure.title("采购执行评估节点，审批成功")  # 用例名称
    @allure.description("采购执行评估节点，（所有前面填过信息的这里都可以填采购评估-采购执行）勾选产能评审结论（选通过或者选建议修改，填原因及修改建议），填写L/T(天)、最小下单量(pcs)、此项目峰值需求(K/M)、供应商总产能(K/M)、分配传音产能(K/M)、供应弹性(%)、共用项目需求合计(K/M)、此项目产能分配(""K/M)、共用项目名、原因及修改建议、备料建议，点击同意，有必填不填时有提示，点击确定")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_006(self, drivers, KeyDevice_Approver_API):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Approver_API[0], '采购执行评估')
        user.click_Device_unfold('摄像头+闪光灯')
        user.click_Device_module('CTP')
        user.click_Device_pending_code('CTP(1供)')
        user.scroll_Device_material_details('采购执行')
        user.input_KeyDevice_Evaluation_content('采购执行', 'L/T(天)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '最小下单量(pcs)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '此项目峰值需求(K/M)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '供应商总产能(K/M)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '分配传音产能(K/M)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '供应弹性(%)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '共用项目需求合计(K/M)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '此项目产能分配(K/M)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '共用项目名', '共用项目名test')
        user.input_KeyDevice_Evaluation_content('采购执行', '产能评审结论', '通过')
        user.input_KeyDevice_Evaluation_content('采购执行', '原因及修改建议', '原因及修改建议test')
        user.input_KeyDevice_Evaluation_content('采购执行', '备料建议', '备料建议test')
        user.click_Device_unfold('硬件电子料-基带')
        user.click_Device_module('CPU')
        user.click_Device_pending_code('CPU(1供)')
        user.scroll_Device_material_details('采购执行')
        user.input_KeyDevice_Evaluation_content('采购执行', 'L/T(天)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '最小下单量(pcs)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '此项目峰值需求(K/M)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '供应商总产能(K/M)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '分配传音产能(K/M)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '供应弹性(%)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '共用项目需求合计(K/M)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '此项目产能分配(K/M)', '1')
        user.input_KeyDevice_Evaluation_content('采购执行', '共用项目名', '共用项目名test')
        user.input_KeyDevice_Evaluation_content('采购执行', '产能评审结论', '通过')
        user.input_KeyDevice_Evaluation_content('采购执行', '原因及修改建议', '原因及修改建议test')
        user.input_KeyDevice_Evaluation_content('采购执行', '备料建议', '备料建议test')
        user.assert_OneWorks_AgreeFlow()

    @allure.story("流程审批")  # 场景名称
    @allure.title("采购PTC评估节点，审批成功")  # 用例名称
    @allure.description("采购PTC评估节点，（所有前面填过信息的这里都可以填采购评估-PTC）勾选评审结论（选通过或者选不同意，填原因及修改建议），填写原因及修改建议，，点击同意，有必填不填时有提示，点击确定")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_007(self, drivers, KeyDevice_Approver_API):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Approver_API[0], '采购PTC评估')
        user.click_Device_unfold('摄像头+闪光灯')
        user.click_Device_module('CTP')
        user.click_Device_pending_code('CTP(1供)')
        user.scroll_Device_material_details('PTC')
        user.input_KeyDevice_Evaluation_content('PTC', '评审结论', '同意')
        user.input_KeyDevice_Evaluation_content('PTC', '原因及修改建议', '原因及修改建议test')
        user.click_Device_unfold('硬件电子料-基带')
        user.click_Device_module('CPU')
        user.click_Device_pending_code('CPU(1供)')
        user.scroll_Device_material_details('PTC')
        user.input_KeyDevice_Evaluation_content('PTC', '评审结论', '同意')
        user.input_KeyDevice_Evaluation_content('PTC', '原因及修改建议', '原因及修改建议test')
        user.assert_OneWorks_AgreeFlow()

    @allure.story("流程审批")  # 场景名称
    @allure.title("采购SQM评估节点，审批成功")  # 用例名称
    @allure.description("采购SQM评估节点，（所有前面填过信息的这里都可以填采购评估-SQM）勾选评审结论（选通过或者选不同意，填原因及修改建议），填写原因及修改建议，点击同意，有必填不填时有提示，点击确定")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_008(self, drivers, KeyDevice_Approver_API):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Approver_API[0], '采购SQM评估')
        user.click_Device_unfold('摄像头+闪光灯')
        user.click_Device_module('CTP')
        user.click_Device_pending_code('CTP(1供)')
        user.scroll_Device_material_details('SQM')
        user.input_KeyDevice_Evaluation_content('SQM', '评审结论', '同意')
        user.input_KeyDevice_Evaluation_content('SQM', '原因及修改建议', '原因及修改建议test')
        user.click_Device_unfold('硬件电子料-基带')
        user.click_Device_module('CPU')
        user.click_Device_pending_code('CPU(1供)')
        user.scroll_Device_material_details('SQM')
        user.input_KeyDevice_Evaluation_content('SQM', '评审结论', '同意')
        user.input_KeyDevice_Evaluation_content('SQM', '原因及修改建议', '原因及修改建议test')
        user.assert_OneWorks_AgreeFlow()

    @allure.story("流程审批")  # 场景名称
    @allure.title("标准化部评估节点，审批成功")  # 用例名称
    @allure.description("关键器件-关键器件流程，查看单据状态已变为审批通过")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_009(self, drivers, KeyDevice_SQL):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'itel')
        user.input_add_item_info('项目', '50A1S')
        user.input_add_item_info('基线名称', '基线GP2325')
        user.input_add_item_info('平台', '测试平台')
        user.input_add_item_info('上市时间', '2022-06-20')
        user.input_add_item_info('月度需求', '1')
        user.input_add_item_info('总需求', '1')
        user.input_add_item_info('目标市场', '深圳')
        user.input_add_item_info('生命周期', '1')
        user.select_business_review('李小素', '摄像头+闪光灯')
        user.select_business_review('李小素', '硬件电子料-基带')
        user.select_business_review('李小素', '标准化代表')
        user.select_business_review('李小素', '采购代表')
        user.click_add_submit()
        user.assert_toast()
        process_code = user.get_info("关键器件", "关键器件流程")[1]
        user.KD_image(process_code)
        user.KD_hardware(process_code)
        user.KD_standard(process_code)
        user.KD_purchase(process_code)
        user.KD_Resources(process_code)
        user.KD_Executive(process_code)
        user.KD_PTC(process_code)
        user.KD_SQM(process_code)
        user.KD_standard_evaluation(process_code)
        user.assert_my_application_node(process_code, '审批抄送', True)
        sleep(60)
        user.assert_my_application_flow(process_code, '审批完成')
        document_status = user.get_Device_info(process_code, "单据状态")
        ValueAssert.value_assert_equal(document_status, '审批通过')


@allure.feature("关键器件-关键器件流程")  # 模块名称
class TestCreateProcessExceptionScenario:
    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("请完善项目信息！")  # 用例名称
    @allure.description("进入关键器件新增页面，不输入项目，其他的内容正确填写，点击提交，提示请完善项目信息！")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_001(self, drivers):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'itel')
        user.input_add_item_info('基线名称', '基线GP2325')
        user.input_add_item_info('平台', '测试平台')
        user.input_add_item_info('上市时间', '2022-06-20')
        user.input_add_item_info('月度需求', '1')
        user.input_add_item_info('总需求', '1')
        user.input_add_item_info('目标市场', '深圳')
        user.input_add_item_info('生命周期', '1')
        user.add_business_review()
        user.click_add_submit()
        user.assert_toast("请完善项目信息！")

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("不完全填写维护关键器件，提示请完善业务审核信息！")  # 用例名称
    @allure.description("进入关键器件新增页面，项目信息和评估关键器件信息完全填写，不完全填写维护关键器件，直接点击提示，提示请完善业务审核信息！")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_002(self, drivers):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'itel')
        user.input_add_item_info('项目', '50A712U')
        user.input_add_item_info('基线名称', '基线GP2325')
        user.input_add_item_info('平台', '测试平台')
        user.input_add_item_info('上市时间', '2022-06-20')
        user.input_add_item_info('月度需求', '1')
        user.input_add_item_info('总需求', '1')
        user.input_add_item_info('目标市场', '深圳')
        user.input_add_item_info('生命周期', '1')
        user.select_business_review('李小素', '摄像头+闪光灯')
        user.select_business_review('李小素', '硬件电子料-基带')
        user.select_business_review('李小素', '标准化代表')
        user.click_add_submit()
        user.assert_toast("请完善业务审核信息！")

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("不输入评估关键器件信息，提示请完善业务审核信息！")  # 用例名称
    @allure.description("进入关键器件新增页面，项目基本信息都完全填写，不输入评估关键器件信息，直接点击提交，提示请完善业务审核信息！")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_003(self, drivers):
        user = KeyComponentsFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'itel')
        user.input_add_item_info('项目', '50A712U')
        user.input_add_item_info('基线名称', '基线GP2325')
        user.input_add_item_info('平台', '测试平台')
        user.input_add_item_info('上市时间', '2022-06-20')
        user.input_add_item_info('月度需求', '1')
        user.input_add_item_info('总需求', '1')
        user.input_add_item_info('目标市场', '深圳')
        user.input_add_item_info('生命周期', '1')
        user.select_business_review('李小素', '摄像头+闪光灯')
        user.select_business_review('李小素', '硬件电子料-基带')
        user.click_add_submit()
        user.assert_toast("请完善业务审核信息！")


if __name__ == '__main__':
    pytest.main(['Test_module.py'])
