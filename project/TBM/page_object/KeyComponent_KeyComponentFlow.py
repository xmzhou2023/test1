from time import sleep
from libs.common.read_element import Element
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class KeyComponentsFlow(CenterComponent, APIRequest):
    """关键器件_关键器件流程"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("关键器件", "关键器件流程")

    @allure.step("关键器件流程新增页面 - 输入项目信息")
    def input_add_item_info(self, info, select):
        """
        关键器件流程新增页面 - 输入项目信息
        :param info: 选择要输入的信息
        :param select: 选择信息内容
        """
        if info == '品牌' or info == '基线名称':
            self.is_click_tbm(user['项目信息输入框'], info)
            logging.info('点击项目信息输入框:{}'.format(info))
            self.scroll_into_view(user['项目信息输入框选择'], select)
            sleep(1)
            self.is_click_tbm(user['项目信息输入框选择'], select)
            logging.info('选择项目信息:{}'.format(select))

        elif info == '项目':
            self.readonly_input_text(user['项目信息输入框'], select, info)
            sleep(1)
            self.is_click_tbm(user['项目信息输入框选择'], select)
            logging.info('选择点击项目信息:{}'.format(select))

        else:
            self.input_text(user['项目信息输入框'], select, info)

    @allure.step("关键器件流程新增页面-项目信息组合")
    def add_item_info(self):
        self.input_add_item_info('品牌', 'itel')
        self.input_add_item_info('项目', '50A712U')
        self.input_add_item_info('平台', '测试平台')
        self.input_add_item_info('上市时间', '2022-06-20')
        self.input_add_item_info('月度需求', '1')
        self.input_add_item_info('总需求', '1')
        self.input_add_item_info('目标市场', '深圳')
        self.input_add_item_info('生命周期', '1')

    @allure.step("业务审核")
    def select_business_review(self, audit, type):
        """
        业务审核 - 选择用户
        @param type:选择的类别
        @param audit:输入的用户名
        """
        self.is_click_tbm(user['业务审核类别'], type)
        self.input_text(user['成员列表输入框'], audit)
        sleep(1)
        self.is_click_tbm(user['成员选择'], audit)
        self.is_click_tbm(user['成员确定'])

    @allure.step("关键器件流程新增页面-业务审核组合")
    def add_business_review(self):
        self.select_business_review('李小素', '摄像头+闪光灯')
        self.select_business_review('李小素', '硬件电子料-基带')
        self.select_business_review('李小素', '标准化代表')
        self.select_business_review('李小素', '采购代表')

    @allure.step("关键器件流程新增组合流程")
    def add(self):
        self.click_add()
        self.add_item_info()
        self.add_business_review()
        self.click_add_submit()
        DomAssert(self.driver).assert_att('请求成功')

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

    @allure.step("oneworks节点：摄像头+闪光灯 页面填写 组合流程")
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
        self.assert_OneWorks_AgreeFlow()

    @allure.step("oneworks节点：硬件电子料-基带 页面填写 组合流程")
    def KD_hardware(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '硬件电子料-基带')
        self.click_Device_unfold('硬件电子料-基带')
        self.click_Device_module('CPU')
        self.click_Device_code_add()
        self.click_Device_material_add('CPU(1供)')
        self.click_Device_pending_code('CPU(1供)')
        self.input_KeyDevice_Evaluation_content('物料详情（参数）', '物料属性', '属性test')
        self.assert_OneWorks_AgreeFlow()

    @allure.step("oneworks节点：标准化代表 页面填写 组合流程")
    def KD_standard(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '标准化代表')
        self.click_Device_checkbox()
        self.click_one_press()
        self.input_KeyDevice_OnePress('责任人', '李小素')
        self.click_OnePress_confirm()
        self.click_OnePress_cancel()
        self.assert_OneWorks_AgreeFlow()

    @allure.step("oneworks节点：采购代表 页面填写 组合流程")
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
        self.assert_OneWorks_AgreeFlow()

    @allure.step("oneworks节点：资源商务评估 页面填写 组合流程")
    def KD_Resources(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '资源商务评估')
        self.click_Device_unfold('摄像头+闪光灯')
        self.click_Device_module('CTP')
        self.click_Device_pending_code('CTP(1供)')
        self.input_KeyDevice_Evaluation_content('资源商务', '供应商名称', 'TEST')
        self.input_KeyDevice_Evaluation_content('资源商务', '是否新供应商', '否')
        self.input_KeyDevice_Evaluation_content('资源商务', '国产化属性', '不涉及')
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
        self.input_KeyDevice_Evaluation_content('资源商务', '国产化属性', '不涉及')
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
        self.assert_OneWorks_AgreeFlow()

    @allure.step("oneworks节点：采购执行评估 页面填写 组合流程")
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
        self.assert_OneWorks_AgreeFlow()

    @allure.step("oneworks节点：采购PTC评估 页面填写 组合流程")
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
        self.assert_OneWorks_AgreeFlow()

    @allure.step("oneworks节点：采购SQM评估 页面填写 组合流程")
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
        self.assert_OneWorks_AgreeFlow()

    @allure.step("oneworks节点：标准化部评估 页面填写 组合流程")
    def KD_standard_evaluation(self, code):
        self.refresh_webpage()
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
        self.assert_OneWorks_AgreeFlow()


if __name__ == '__main__':
    pass
