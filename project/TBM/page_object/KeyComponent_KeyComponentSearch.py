from libs.common.read_element import Element
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class KeyComponentsSearch(CenterComponent, APIRequest):
    """关键器件_关键器件查询"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("关键器件", "关键器件查询")

    @allure.step("点击操作")
    def click_operate(self, item, operate):
        """
        关键器件查询 点击操作 ： 查看/修订/封板
        @param item:项目
        @param operate:操作
        """
        self.is_click_tbm(user['项目操作'], item, operate)

    @allure.step("点击修订关键器件复选框")
    def click_key(self, key):
        """
        关键器件查询 点击修订关键器件复选框
        @param key:指定器件分类
        """
        self.is_click_tbm(user['修订关键器件-复选框'], key)

    @allure.step("点击修订关键器件确定")
    def click_revise_comfirm(self):
        self.is_click_tbm(user['修订关键器件-确定'])

    @allure.step("断言：进入关键器件修订发起页面，查看关键器件-业务审核-维护关键器件显示是否正确")
    def assert_review(self, review, result=True):
        DomAssert(self.driver).assert_control(user['修订关键器件-业务审核'], review, result=result)

    @allure.step("业务审核")
    def select_business_review(self, audit, type):
        """
        业务审核 - 选择用户
        @param type:选择的类别
        @param audit:输入的用户名
        """
        self.is_click_tbm(user['业务审核类别'], type)
        self.is_click_tbm(user['成员列表清空'])
        self.input_text(user['成员列表输入框'], audit)
        sleep(1)
        self.is_click_tbm(user['成员选择'], audit)
        self.is_click_tbm(user['成员确定'])

    def click_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("关键器件", "关键器件流程")
        self.click_delete(code)
        self.click_dialog_confirm()
        DomAssert(self.driver).assert_att('删除成功')

    @allure.step("摄像头+闪光灯节点审批")
    def KD_image(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '摄像头+闪光灯')
        self.click_Device_unfold('摄像头+闪光灯')
        self.click_Device_module('CTP')
        self.click_Device_code_add()
        self.click_Device_material_add('CTP(1供)')
        self.click_Device_pending_code('CTP(1供)')
        self.input_KeyDevice_Evaluation_content('物料详情（参数）', '物料属性', '属性test')
        self.input_KeyDevice_Evaluation_content('参数', '技术类型', 'GFF')
        self.input_KeyDevice_Evaluation_content('参数', 'CG颜色', 'CG颜色test')
        self.input_KeyDevice_Evaluation_content('参数', '接口类型', '接口类型test')
        self.input_KeyDevice_Evaluation_content('参数', '连接方式', '焊接')
        self.click_agree()
        self.click_dialog_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("硬件电子料-基带节点审批")
    def KD_hardware(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '硬件电子料-基带')
        self.click_Device_unfold('硬件电子料-基带')
        self.click_Device_module('CPU')
        self.click_Device_code_add()
        self.click_Device_material_add('CPU(1供)')
        self.click_Device_pending_code('CPU(1供)')
        self.input_KeyDevice_Evaluation_content('物料详情（参数）', '物料属性', '属性test')
        self.click_agree()
        self.click_dialog_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("标准化代表节点审批")
    def KD_standard(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '标准化代表')
        self.click_Device_checkbox()
        self.click_one_press()
        self.input_KeyDevice_OnePress('责任人', '李小素')
        self.click_OnePress_confirm()
        self.click_OnePress_cancel()
        self.click_agree()
        self.click_dialog_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("采购代表节点审批")
    def KD_purchase(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '采购代表')
        self.click_Device_checkbox()
        self.click_one_press()
        self.input_KeyDevice_OnePress('资源商务', '李小素')
        self.click_OnePress_confirm()
        self.input_KeyDevice_OnePress('采购执行', '李小素')
        self.click_OnePress_confirm()
        self.input_KeyDevice_OnePress('采购PTC', '李小素')
        self.click_OnePress_confirm()
        self.input_KeyDevice_OnePress('采购SQM', '李小素')
        self.click_OnePress_confirm()
        self.click_OnePress_cancel()
        self.click_agree()
        self.click_dialog_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("资源商务评估节点审批")
    def KD_Resources(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '资源商务评估')
        self.click_Device_unfold('摄像头+闪光灯')
        self.click_Device_module('CTP')
        self.click_Device_pending_code('CTP(1供)')
        self.input_KeyDevice_Evaluation_content('资源商务', '供应商名称', 'TEST')
        self.input_KeyDevice_Evaluation_content('资源商务', '是否新供应商', '否')
        self.input_KeyDevice_Evaluation_content('资源商务', '国产化属性', '0')
        self.input_KeyDevice_Evaluation_content('资源商务', '供应商选择原因类别', '成本因素')
        self.input_KeyDevice_Evaluation_content('资源商务', '供应商选择原因', '供应商选择原因TEST')
        self.input_KeyDevice_Evaluation_content('资源商务', '份额', '50')
        self.input_KeyDevice_Evaluation_content('资源商务', '是否客供物料', '是')
        self.input_KeyDevice_Evaluation_content('资源商务', '价格趋势（6个月）', '持平')
        self.input_KeyDevice_Evaluation_content('资源商务', '是否NUDD', '是')
        self.input_KeyDevice_Evaluation_content('资源商务', 'NUDD说明', 'NUDD说明TEST')
        self.input_KeyDevice_Evaluation_content('资源商务', 'NUDD管理方案', 'NUDD管理方案TEST')
        self.input_KeyDevice_Evaluation_content('资源商务', '评审结论', '通过')
        self.input_KeyDevice_Evaluation_content('资源商务', '原因及修改建议', '原因及修改建议TEST')
        self.click_Device_unfold('硬件电子料-基带')
        self.click_Device_module('CPU')
        self.click_Device_pending_code('CPU(1供)')
        self.input_KeyDevice_Evaluation_content('资源商务', '供应商名称', 'TEST')
        self.input_KeyDevice_Evaluation_content('资源商务', '是否新供应商', '否')
        self.input_KeyDevice_Evaluation_content('资源商务', '国产化属性', '0')
        self.input_KeyDevice_Evaluation_content('资源商务', '供应商选择原因类别', '成本因素')
        self.input_KeyDevice_Evaluation_content('资源商务', '供应商选择原因', '供应商选择原因TEST')
        self.input_KeyDevice_Evaluation_content('资源商务', '份额', '50')
        self.input_KeyDevice_Evaluation_content('资源商务', '是否客供物料', '是')
        self.input_KeyDevice_Evaluation_content('资源商务', '价格趋势（6个月）', '持平')
        self.input_KeyDevice_Evaluation_content('资源商务', '是否NUDD', '是')
        self.input_KeyDevice_Evaluation_content('资源商务', 'NUDD说明', 'NUDD说明TEST')
        self.input_KeyDevice_Evaluation_content('资源商务', 'NUDD管理方案', 'NUDD管理方案TEST')
        self.input_KeyDevice_Evaluation_content('资源商务', '评审结论', '通过')
        self.input_KeyDevice_Evaluation_content('资源商务', '原因及修改建议', '原因及修改建议TEST')
        self.click_agree()
        self.click_dialog_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("采购执行评估节点审批")
    def KD_Executive(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '采购执行评估')
        self.click_Device_unfold('摄像头+闪光灯')
        self.click_Device_module('CTP')
        self.click_Device_pending_code('CTP(1供)')
        self.scroll_Device_material_details('采购执行')
        self.input_KeyDevice_Evaluation_content('采购执行', 'L/T(天)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '最小下单量(pcs)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '此项目峰值需求(K/M)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '供应商总产能(K/M)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '分配传音产能(K/M)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '供应弹性(%)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '共用项目需求合计(K/M)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '此项目产能分配(K/M)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '共用项目名', '共用项目名test')
        self.input_KeyDevice_Evaluation_content('采购执行', '产能评审结论', '通过')
        self.input_KeyDevice_Evaluation_content('采购执行', '原因及修改建议', '原因及修改建议test')
        self.input_KeyDevice_Evaluation_content('采购执行', '备料建议', '备料建议test')
        self.click_Device_unfold('硬件电子料-基带')
        self.click_Device_module('CPU')
        self.click_Device_pending_code('CPU(1供)')
        self.scroll_Device_material_details('采购执行')
        self.input_KeyDevice_Evaluation_content('采购执行', 'L/T(天)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '最小下单量(pcs)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '此项目峰值需求(K/M)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '供应商总产能(K/M)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '分配传音产能(K/M)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '供应弹性(%)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '共用项目需求合计(K/M)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '此项目产能分配(K/M)', '1')
        self.input_KeyDevice_Evaluation_content('采购执行', '共用项目名', '共用项目名test')
        self.input_KeyDevice_Evaluation_content('采购执行', '产能评审结论', '通过')
        self.input_KeyDevice_Evaluation_content('采购执行', '原因及修改建议', '原因及修改建议test')
        self.input_KeyDevice_Evaluation_content('采购执行', '备料建议', '备料建议test')
        self.click_agree()
        self.click_dialog_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("采购PTC评估节点审批")
    def KD_PTC(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '采购PTC评估')
        self.click_Device_unfold('摄像头+闪光灯')
        self.click_Device_module('CTP')
        self.click_Device_pending_code('CTP(1供)')
        self.scroll_Device_material_details('PTC')
        self.input_KeyDevice_Evaluation_content('PTC', '评审结论', '同意')
        self.input_KeyDevice_Evaluation_content('PTC', '原因及修改建议', '原因及修改建议test')
        self.click_Device_unfold('硬件电子料-基带')
        self.click_Device_module('CPU')
        self.click_Device_pending_code('CPU(1供)')
        self.scroll_Device_material_details('PTC')
        self.input_KeyDevice_Evaluation_content('PTC', '评审结论', '同意')
        self.input_KeyDevice_Evaluation_content('PTC', '原因及修改建议', '原因及修改建议test')
        self.click_agree()
        self.click_dialog_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("采购SQM评估节点审批")
    def KD_SQM(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '采购SQM评估')
        self.click_Device_unfold('摄像头+闪光灯')
        self.click_Device_module('CTP')
        self.click_Device_pending_code('CTP(1供)')
        self.scroll_Device_material_details('SQM')
        self.input_KeyDevice_Evaluation_content('SQM', '评审结论', '同意')
        self.input_KeyDevice_Evaluation_content('SQM', '原因及修改建议', '原因及修改建议test')
        self.click_Device_unfold('硬件电子料-基带')
        self.click_Device_module('CPU')
        self.click_Device_pending_code('CPU(1供)')
        self.scroll_Device_material_details('SQM')
        self.input_KeyDevice_Evaluation_content('SQM', '评审结论', '同意')
        self.input_KeyDevice_Evaluation_content('SQM', '原因及修改建议', '原因及修改建议test')
        self.click_agree()
        self.click_dialog_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("标准化部评估节点审批")
    def KD_standard_evaluation(self, code):
        self.enter_oneworks_edit(code, '标准化部评估')
        self.click_Device_unfold('摄像头+闪光灯')
        self.click_Device_module('CTP')
        self.click_Device_pending_code('CTP(1供)')
        self.input_KeyDevice_Evaluation_content('标准化评估', '认证状态', '认证通过')
        self.input_KeyDevice_Evaluation_content('标准化评估', '原因及修改建议', '原因及修改建议test')
        self.click_Device_unfold('硬件电子料-基带')
        self.click_Device_module('CPU')
        self.click_Device_pending_code('CPU(1供)')
        self.input_KeyDevice_Evaluation_content('标准化评估', '认证状态', '认证通过')
        self.input_KeyDevice_Evaluation_content('标准化评估', '原因及修改建议', '原因及修改建议test')
        self.click_agree()
        self.click_dialog_confirm()
        self.assert_toast()
        self.quit_oneworks()


if __name__ == '__main__':
    pass
