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

    @allure.step("删除操作")
    def click_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['确定'])

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("关键器件", "关键器件流程")
        self.click_delete(code)
        DomAssert(self.driver).assert_att('删除成功')

    @allure.step("获取关键器件第一列内容")
    def get_info(self):
        """
        获取关键器件第一列内容
        @return:返回文本及索引位置分别是'No.'==0; '流程编码'==1; '流程类型'==2; '项目'==3; '品牌'==4; '单据状态'==5; '申请人'==6; '申请时间'==7; '操作'==8;
        """
        self.click_menu("关键器件", "关键器件流程")
        sleep(1)
        info = self.find_elements_tbm(user['表格内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    @allure.step("点击指定关键器件左侧三角按钮展开")
    def click_onework_unfold(self, key):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击指定关键器件左侧三角按钮展开
        @param key:关键器件
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-关键器件展开'], key)

    @allure.step("维护关键器件-点击指定物料模块")
    def click_onework_module(self, module):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击指定物料模块
        @param module:物料模块
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块'], module)

    @allure.step("维护关键器件-点击物料编码右侧的加号")
    def click_onework_code_add(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击物料编码右侧的加号
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码加号'])

    @allure.step("维护关键器件-鼠标悬停在物料右侧，点击加号")
    def click_onework_material_add(self, code):
        """
        oneworks-节点：维护关键器件-查看详情页面
        鼠标悬停在物料右侧，点击加号
        @param code:物料模块
        """
        self.hover(user['oneworks-节点-维护关键器件-物料模块-物料编码按钮组'], code)
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码按钮组-加号'], code)

    @allure.step("维护关键器件-点击待申请编码，打开物料详情（参数）")
    def click_onework_material_pending_code(self, code):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击待申请编码，打开物料详情（参数）
        @param code:待申请编码
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码-待申请编码'], code)

    @allure.step("维护关键器件-物料详情-输入物料详情")
    def input_onework_material_details(self, choice, details):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-输入物料详情
        @param details:详情
        @param choice:输入框名称
        """
        self.input_text(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料详情'], details, choice)

    @allure.step("维护关键器件-物料详情-滚动显示全部参数")
    def scroll_onework_material_param(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-滚动显示全部参数
        """
        self.scroll_into_view(user['oneworks-节点-物料模块-物料编码-物料详情-参数'])

    @allure.step("维护关键器件-物料详情-滚动显示")
    def scroll_onework_material_details(self, param):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-滚动显示
        """
        self.scroll_into_view(user['oneworks-节点-物料模块-物料编码-物料详情'], param)

    @allure.step("维护关键器件-物料详情-输入物料参数")
    def input_onework_material_parameter(self, choice, details, mode=True):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-输入物料参数
        @param details:内容
        @param choice:参数名称
        @param mode:默认True为输入框，如果是选择框则输入False
        """
        if mode is True:
            self.input_text(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料参数'], details, choice)
        else:
            self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料参数'], choice)
            self.scroll_into_view(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料参数选择'], details)
            self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料参数选择'], details)

    @allure.step("点击复选框")
    def click_onework_checkbox(self, sort='all'):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击复选框
        @param sort:物料编码，传入物料编码；默认‘all’表示点击全选复选框
        """
        # sleep(5)
        DomAssert(self.driver).assert_control(user['oneworks-节点-评估关键器件-Title'])
        if sort == 'all':
            self.is_click_tbm(user['oneworks-节点-评估关键器件-复选框全选'])
        else:
            self.is_click_tbm(user['oneworks-节点-评估关键器件-复选框单选'], sort)
        logging.info('点击复选框')

    @allure.step("点击一键填写")
    def click_onework_onepress(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击一键填写
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写'])

    @allure.step("点击一键填写-确定")
    def click_onework_onepress_confirm(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击一键填写-确定
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-确定'])

    @allure.step("点击一键填写-取消")
    def click_onework_onepress_cancel(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击一键填写-取消
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-取消'])

    @allure.step("输入一键填写内容")
    def input_onework_onepress(self, field, name):
        """
        oneworks-节点：维护关键器件-查看详情页面
        输入一键填写内容
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-字段名称'])
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-字段名称选择'], field)
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-责任人'])
        self.input_text(user['成员列表输入框'], name)
        sleep(1)
        self.is_click_tbm(user['成员选择'], name)
        self.is_click_tbm(user['成员确定'])

    @allure.step("资源商务评估-输入资源商务内容")
    def input_onework_procurement_evaluation(self, choice, details, mode=True):
        """
        oneworks-节点：资源商务评估-查看详情页面
        物料详情-采购评估
        @param details:内容
        @param choice:参数名称
        @param mode:默认True为输入框，如果是选择框则输入False
        """
        if mode is True:
            self.readonly_input_text(user['oneworks-节点-资源商务评估-采购评估-资源商务-输入框'], details, choice)
        else:
            self.is_click_tbm(user['oneworks-节点-资源商务评估-采购评估-资源商务-输入框'], choice)
            try:
                self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)
            except:
                self.scroll_into_view(user['oneworks-节点-下拉框-选择'], details)
                self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)

    @allure.step("资源商务评估-输入采购执行内容")
    def input_onework_procurement_execution(self, choice, details, mode=True):
        """
        oneworks-节点：采购执行评估-查看详情页面
        物料详情-采购执行
        @param details:内容
        @param choice:参数名称
        @param mode:默认True为输入框，如果是选择框则输入False
        """
        if mode is True:
            self.readonly_input_text(user['oneworks-节点-资源商务评估-采购评估-采购执行-输入框'], details, choice)
        else:
            self.is_click_tbm(user['oneworks-节点-资源商务评估-采购评估-采购执行-输入框'], choice)
            try:
                self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)
            except:
                self.scroll_into_view(user['oneworks-节点-下拉框-选择'], details)
                self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)

    @allure.step("采购PTC评估-输入PTC内容")
    def input_onework_ptc(self, choice, details):
        """
        oneworks-节点：采购PTC评估-查看详情页面
        物料详情-采购PTC评估
        @param details:内容
        @param choice:参数名称
        """
        if choice == '原因及修改建议':
            self.readonly_input_text(user['oneworks-节点-采购PTC评估-采购评估-PTC-输入框'], details, choice)
        elif choice == '评审结论':
            self.is_click_tbm(user['oneworks-节点-采购PTC评估-采购评估-PTC-输入框'], choice)
            self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)

    @allure.step("采购PTC评估-输入SQM内容")
    def input_onework_sqm(self, choice, details):
        """
        oneworks-节点：采购SQM评估-查看详情页面
        物料详情-采购SQM评估
        @param details:内容
        @param choice:参数名称
        """
        if choice == '原因及修改建议':
            self.readonly_input_text(user['oneworks-节点-采购PTC评估-采购评估-SQM-输入框'], details, choice)
        elif choice == '评审结论':
            self.is_click_tbm(user['oneworks-节点-采购PTC评估-采购评估-SQM-输入框'], choice)
            self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)

    @allure.step("标准化评估-输入标准化评估内容")
    def input_onework_standardized_evaluation(self, choice, details):
        """
        oneworks-节点：标准化评估-查看详情页面
        物料详情-标准化评估
        @param details:内容
        @param choice:参数名称
        """
        if choice == '原因及修改建议':
            self.readonly_input_text(user['oneworks-节点-标准化部评估-标准化评估-文本框'], details, choice)
        elif choice == '认证状态' or '评审结论':
            self.is_click_tbm(user['oneworks-节点-标准化部评估-标准化评估-输入框'], choice)
            self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)

    @allure.step("摄像头+闪光灯节点审批")
    def KD_image(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '摄像头+闪光灯')
        self.click_onework_unfold('摄像头+闪光灯')
        self.click_onework_module('CTP')
        self.click_onework_code_add()
        self.click_onework_material_add('CTP(1供)')
        self.click_onework_material_pending_code('CTP(1供)')
        self.input_onework_material_details('物料属性', '属性test')
        self.scroll_onework_material_param()
        self.input_onework_material_parameter('技术类型', 'GFF', False)
        self.input_onework_material_parameter('CG颜色', 'CG颜色test')
        self.input_onework_material_parameter('接口类型', '接口类型test')
        self.input_onework_material_parameter('连接方式', '焊接', False)
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("硬件电子料-基带节点审批")
    def KD_hardware(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '硬件电子料-基带')
        self.click_onework_unfold('硬件电子料-基带')
        self.click_onework_module('CPU')
        self.click_onework_code_add()
        self.click_onework_material_add('CPU(1供)')
        self.click_onework_material_pending_code('CPU(1供)')
        self.input_onework_material_details('物料属性', '属性test')
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("标准化代表节点审批")
    def KD_standard(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '标准化代表')
        self.click_onework_checkbox()
        self.click_onework_onepress()
        self.input_onework_onepress('责任人', '李小素')
        self.click_onework_onepress_confirm()
        self.click_onework_onepress_cancel()
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("采购代表节点审批")
    def KD_purchase(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '采购代表')
        self.click_onework_checkbox()
        self.click_onework_onepress()
        self.input_onework_onepress('资源商务', '李小素')
        self.click_onework_onepress_confirm()
        DomAssert(self.driver).assert_att('已选分类的审批人设置成功')
        self.input_onework_onepress('采购执行', '李小素')
        self.click_onework_onepress_confirm()
        DomAssert(self.driver).assert_att('已选分类的审批人设置成功')
        self.input_onework_onepress('采购PTC', '李小素')
        self.click_onework_onepress_confirm()
        DomAssert(self.driver).assert_att('已选分类的审批人设置成功')
        self.input_onework_onepress('采购SQM', '李小素')
        self.click_onework_onepress_confirm()
        DomAssert(self.driver).assert_att('已选分类的审批人设置成功')
        self.click_onework_onepress_cancel()
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("资源商务评估节点审批")
    def KD_Resources(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '资源商务评估')
        self.click_onework_unfold('摄像头+闪光灯')
        self.click_onework_module('CTP')
        self.click_onework_material_pending_code('CTP(1供)')
        self.input_onework_procurement_evaluation('供应商名称', 'TEST', False)
        self.input_onework_procurement_evaluation('是否新供应商', '否', False)
        self.input_onework_procurement_evaluation('国产化属性', '0', False)
        self.input_onework_procurement_evaluation('供应商选择原因类别', '成本因素', False)
        self.input_onework_procurement_evaluation('供应商选择原因', '供应商选择原因TEST')
        self.input_onework_procurement_evaluation('份额', '50')
        self.input_onework_procurement_evaluation('是否客供物料', '是', False)
        self.input_onework_procurement_evaluation('价格趋势（6个月）', '持平', False)
        self.input_onework_procurement_evaluation('是否NUDD', '是', False)
        self.input_onework_procurement_evaluation('NUDD说明', 'NUDD说明TEST')
        self.input_onework_procurement_evaluation('NUDD管理方案', 'NUDD管理方案TEST')
        self.input_onework_procurement_evaluation('评审结论', '通过', False)
        self.input_onework_procurement_evaluation('原因及修改建议', '原因及修改建议TEST')
        self.click_onework_unfold('硬件电子料-基带')
        self.click_onework_module('CPU')
        self.click_onework_material_pending_code('CPU(1供)')
        self.input_onework_procurement_evaluation('供应商名称', 'TEST', False)
        self.input_onework_procurement_evaluation('是否新供应商', '否', False)
        self.input_onework_procurement_evaluation('国产化属性', '0', False)
        self.input_onework_procurement_evaluation('供应商选择原因类别', '成本因素', False)
        self.input_onework_procurement_evaluation('供应商选择原因', '供应商选择原因TEST')
        self.input_onework_procurement_evaluation('份额', '50')
        self.input_onework_procurement_evaluation('是否客供物料', '是', False)
        self.input_onework_procurement_evaluation('价格趋势（6个月）', '持平', False)
        self.input_onework_procurement_evaluation('是否NUDD', '是', False)
        self.input_onework_procurement_evaluation('NUDD说明', 'NUDD说明TEST')
        self.input_onework_procurement_evaluation('NUDD管理方案', 'NUDD管理方案TEST')
        self.input_onework_procurement_evaluation('评审结论', '通过', False)
        self.input_onework_procurement_evaluation('原因及修改建议', '原因及修改建议TEST')
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("采购执行评估节点审批")
    def KD_Executive(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '采购执行评估')
        self.click_onework_unfold('摄像头+闪光灯')
        self.click_onework_module('CTP')
        self.click_onework_material_pending_code('CTP(1供)')
        self.scroll_onework_material_details('采购执行')
        self.input_onework_procurement_execution('L/T(天)', '1')
        self.input_onework_procurement_execution('最小下单量(pcs)', '1')
        self.input_onework_procurement_execution('此项目峰值需求(K/M)', '1')
        self.input_onework_procurement_execution('供应商总产能(K/M)', '1')
        self.input_onework_procurement_execution('分配传音产能(K/M)', '1')
        self.input_onework_procurement_execution('供应弹性(%)', '1')
        self.input_onework_procurement_execution('共用项目需求合计(K/M)', '1')
        self.input_onework_procurement_execution('此项目产能分配(K/M)', '1')
        self.input_onework_procurement_execution('共用项目名', '共用项目名test')
        self.input_onework_procurement_execution('产能评审结论', '通过', False)
        self.input_onework_procurement_execution('原因及修改建议', '原因及修改建议test')
        self.input_onework_procurement_execution('备料建议', '备料建议test')
        self.click_onework_unfold('硬件电子料-基带')
        self.click_onework_module('CPU')
        self.click_onework_material_pending_code('CPU(1供)')
        self.scroll_onework_material_details('采购执行')
        self.input_onework_procurement_execution('L/T(天)', '1')
        self.input_onework_procurement_execution('最小下单量(pcs)', '1')
        self.input_onework_procurement_execution('此项目峰值需求(K/M)', '1')
        self.input_onework_procurement_execution('供应商总产能(K/M)', '1')
        self.input_onework_procurement_execution('分配传音产能(K/M)', '1')
        self.input_onework_procurement_execution('供应弹性(%)', '1')
        self.input_onework_procurement_execution('共用项目需求合计(K/M)', '1')
        self.input_onework_procurement_execution('此项目产能分配(K/M)', '1')
        self.input_onework_procurement_execution('共用项目名', '共用项目名test')
        self.input_onework_procurement_execution('产能评审结论', '通过', False)
        self.input_onework_procurement_execution('原因及修改建议', '原因及修改建议test')
        self.input_onework_procurement_execution('备料建议', '备料建议test')
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("采购PTC评估节点审批")
    def KD_PTC(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '采购PTC评估')
        self.click_onework_unfold('摄像头+闪光灯')
        self.click_onework_module('CTP')
        self.click_onework_material_pending_code('CTP(1供)')
        self.scroll_onework_material_details('PTC')
        self.input_onework_ptc('评审结论', '同意')
        self.input_onework_ptc('原因及修改建议', '原因及修改建议test')
        self.click_onework_unfold('硬件电子料-基带')
        self.click_onework_module('CPU')
        self.click_onework_material_pending_code('CPU(1供)')
        self.scroll_onework_material_details('PTC')
        self.input_onework_ptc('评审结论', '同意')
        self.input_onework_ptc('原因及修改建议', '原因及修改建议test')
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("采购SQM评估节点审批")
    def KD_SQM(self, code):
        self.refresh_webpage()
        self.enter_oneworks_edit(code, '采购SQM评估')
        self.click_onework_unfold('摄像头+闪光灯')
        self.click_onework_module('CTP')
        self.click_onework_material_pending_code('CTP(1供)')
        self.scroll_onework_material_details('SQM')
        self.input_onework_sqm('评审结论', '同意')
        self.input_onework_sqm('原因及修改建议', '原因及修改建议test')
        self.click_onework_unfold('硬件电子料-基带')
        self.click_onework_module('CPU')
        self.click_onework_material_pending_code('CPU(1供)')
        self.scroll_onework_material_details('SQM')
        self.input_onework_sqm('评审结论', '同意')
        self.input_onework_sqm('原因及修改建议', '原因及修改建议test')
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("标准化部评估节点审批")
    def KD_standard_evaluation(self, code):
        self.enter_oneworks_edit(code, '标准化部评估')
        self.click_onework_unfold('摄像头+闪光灯')
        self.click_onework_module('CTP')
        self.click_onework_material_pending_code('CTP(1供)')
        self.input_onework_standardized_evaluation('认证状态', '认证通过')
        self.input_onework_standardized_evaluation('原因及修改建议', '原因及修改建议test')
        self.click_onework_unfold('硬件电子料-基带')
        self.click_onework_module('CPU')
        self.click_onework_material_pending_code('CPU(1供)')
        self.input_onework_standardized_evaluation('认证状态', '认证通过')
        self.input_onework_standardized_evaluation('原因及修改建议', '原因及修改建议test')
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()
if __name__ == '__main__':
    pass
