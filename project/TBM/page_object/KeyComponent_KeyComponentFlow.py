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

    @allure.step("点击新增")
    def click_key_components_flow_add(self):
        """点击新增"""
        self.is_click_tbm(user['新增'])
        sleep(1)

    @allure.step("关键器件流程新增页面 - 输入项目信息")
    def input_key_components_flow_add_item_info(self, info, select):
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
    def key_components_flow_add_item_info(self):
        self.input_key_components_flow_add_item_info('品牌', 'itel')
        self.input_key_components_flow_add_item_info('项目', '50A712U')
        self.input_key_components_flow_add_item_info('基线名称', '基线GP2325')
        self.input_key_components_flow_add_item_info('平台', '测试平台')
        self.input_key_components_flow_add_item_info('上市时间', '2022-06-20')
        self.input_key_components_flow_add_item_info('月度需求', '1')
        self.input_key_components_flow_add_item_info('总需求', '1')
        self.input_key_components_flow_add_item_info('目标市场', '深圳')
        self.input_key_components_flow_add_item_info('生命周期', '1')

    @allure.step("业务审核")
    def select_key_components_flow_business_review(self, type, audit):
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
    def key_components_flow_add_business_review(self):
        self.select_key_components_flow_business_review('摄像头+闪光灯', '李小素')
        self.select_key_components_flow_business_review('硬件电子料-基带', '李小素')
        self.select_key_components_flow_business_review('标准化代表', '李小素')
        self.select_key_components_flow_business_review('采购代表', '李小素')

    @allure.step("点击提交")
    def click_key_components_flow_submit(self):
        """点击提交"""
        self.is_click_tbm(user['提交'])
        sleep(1)

    @allure.step("关键器件流程新增组合流程")
    def key_components_flow_add(self):
        """
        关键器件流程新增 组合流程
        """
        self.click_key_components_flow_add()
        self.key_components_flow_add_item_info()
        self.key_components_flow_add_business_review()
        self.click_key_components_flow_submit()
        DomAssert(self.driver).assert_att('请求成功')

    @allure.step("获取关键器件第一列内容")
    def get_key_components_flow_info(self):
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

    @allure.step("删除操作")
    def click_key_components_flow_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['确定'])

    @allure.step("新建流程后的后置删除处理")
    def delete_key_components_flow_flow(self, code):
        """
        新建流程后的后置删除处理
        """
        self.recall_process(code)
        self.click_menu("关键器件", "关键器件流程")
        self.click_key_components_flow_delete(code)
        DomAssert(self.driver).assert_att('删除成功')

    @allure.step("点击指定关键器件左侧三角按钮展开")
    def click_onework_key_components_flow_unfold(self, key):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击指定关键器件左侧三角按钮展开
        @param key:关键器件
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-关键器件展开'], key)

    @allure.step("维护关键器件-点击指定物料模块")
    def click_onework_key_components_flow_module(self, module):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击指定物料模块
        @param module:物料模块
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块'], module)

    @allure.step("维护关键器件-点击物料编码右侧的加号")
    def click_onework_key_components_flow_code_add(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击物料编码右侧的加号
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码加号'])

    @allure.step("维护关键器件-鼠标悬停在物料右侧，点击加号")
    def click_onework_key_components_flow_material_add(self, code):
        """
        oneworks-节点：维护关键器件-查看详情页面
        鼠标悬停在物料右侧，点击加号
        @param code:物料模块
        """
        self.hover(user['oneworks-节点-维护关键器件-物料模块-物料编码按钮组'], code)
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码按钮组-加号'], code)

    @allure.step("维护关键器件-点击待申请编码，打开物料详情（参数）")
    def click_onework_key_components_flow_material_pending_code(self, code):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击待申请编码，打开物料详情（参数）
        @param code:待申请编码
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码-待申请编码'], code)

    @allure.step("维护关键器件-物料详情-输入物料详情")
    def input_onework_key_components_flow_material_details(self, choice, details):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-输入物料详情
        @param details:详情
        @param choice:输入框名称
        """
        self.input_text(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料详情'], details, choice)

    @allure.step("维护关键器件-物料详情-滚动显示全部参数")
    def scroll_onework_key_components_flow_material_param(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-滚动显示全部参数
        """
        self.scroll_into_view(user['oneworks-节点-物料模块-物料编码-物料详情-参数'])

    @allure.step("维护关键器件-物料详情-滚动显示")
    def scroll_onework_key_components_flow_material_details(self, param):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-滚动显示
        """
        self.scroll_into_view(user['oneworks-节点-物料模块-物料编码-物料详情'], param)

    @allure.step("维护关键器件-物料详情-输入物料参数")
    def input_onework_key_components_flow_material_parameter(self, choice, details, mode=True):
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

    @allure.step("oneworks节点：摄像头+闪光灯 页面填写 组合流程")
    def onework_key_components_flow_flowone(self, code):
        self.enter_oneworks_edit(code, '摄像头+闪光灯')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_code_add()
        self.click_onework_key_components_flow_material_add('CTP(1供)')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.input_onework_key_components_flow_material_details('物料属性', '属性test')
        self.scroll_onework_key_components_flow_material_param()
        self.input_onework_key_components_flow_material_parameter('技术类型', 'GFF', False)
        self.input_onework_key_components_flow_material_parameter('CG颜色', 'CG颜色test')
        self.input_onework_key_components_flow_material_parameter('接口类型', '接口类型test')
        self.input_onework_key_components_flow_material_parameter('连接方式', '焊接', False)
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_oneworks()

    @allure.step("oneworks节点：硬件电子料-基带 页面填写 组合流程")
    def onework_key_components_flow_flowtwo(self, code):
        self.enter_oneworks_edit(code, '硬件电子料-基带')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_code_add()
        self.click_onework_key_components_flow_material_add('CPU(1供)')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.input_onework_key_components_flow_material_details('物料属性', '属性test')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_oneworks()

    @allure.step("oneworks节点：标准化代表 页面填写 组合流程")
    def onework_key_components_flow_flowthree(self, code):
        self.enter_oneworks_edit(code, '标准化代表')
        self.click_onework_key_components_flow_checkbox()
        self.click_onework_key_components_flow_onepress()
        self.input_onework_key_components_flow_onepress('责任人', '李小素')
        self.click_onework_key_components_flow_onepress_confirm()
        self.click_onework_key_components_flow_onepress_cancel()
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_oneworks()

    @allure.step("oneworks节点：采购代表 页面填写 组合流程")
    def onework_key_components_flow_flowfour(self, code):
        self.enter_oneworks_edit(code, '采购代表')
        self.click_onework_key_components_flow_checkbox()
        self.click_onework_key_components_flow_onepress()
        self.input_onework_key_components_flow_onepress('资源商务', '李小素')
        self.click_onework_key_components_flow_onepress_confirm()
        self.input_onework_key_components_flow_onepress('采购执行', '李小素')
        self.click_onework_key_components_flow_onepress_confirm()
        self.input_onework_key_components_flow_onepress('采购PTC', '李小素')
        self.click_onework_key_components_flow_onepress_confirm()
        self.input_onework_key_components_flow_onepress('采购SQM', '李小素')
        self.click_onework_key_components_flow_onepress_confirm()
        self.click_onework_key_components_flow_onepress_cancel()
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_oneworks()

    @allure.step("oneworks节点：资源商务评估 页面填写 组合流程")
    def onework_key_components_flow_flowfive(self, code):
        self.enter_oneworks_edit(code, '资源商务评估')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.input_onework_key_components_flow_procurement_evaluation('供应商名称', 'TEST', False)
        self.input_onework_key_components_flow_procurement_evaluation('是否新供应商', '否', False)
        self.input_onework_key_components_flow_procurement_evaluation('国产化属性', '0', False)
        self.input_onework_key_components_flow_procurement_evaluation('供应商选择原因类别', '成本因素', False)
        self.input_onework_key_components_flow_procurement_evaluation('供应商选择原因', '供应商选择原因TEST')
        self.input_onework_key_components_flow_procurement_evaluation('份额', '50')
        self.input_onework_key_components_flow_procurement_evaluation('是否客供物料', '是', False)
        self.input_onework_key_components_flow_procurement_evaluation('价格趋势（6个月）', '持平', False)
        self.input_onework_key_components_flow_procurement_evaluation('是否NUDD', '是', False)
        self.input_onework_key_components_flow_procurement_evaluation('NUDD说明', 'NUDD说明TEST')
        self.input_onework_key_components_flow_procurement_evaluation('NUDD管理方案', 'NUDD管理方案TEST')
        self.input_onework_key_components_flow_procurement_evaluation('评审结论', '通过', False)
        self.input_onework_key_components_flow_procurement_evaluation('原因及修改建议', '原因及修改建议TEST')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.input_onework_key_components_flow_procurement_evaluation('供应商名称', 'TEST', False)
        self.input_onework_key_components_flow_procurement_evaluation('是否新供应商', '否', False)
        self.input_onework_key_components_flow_procurement_evaluation('国产化属性', '0', False)
        self.input_onework_key_components_flow_procurement_evaluation('供应商选择原因类别', '成本因素', False)
        self.input_onework_key_components_flow_procurement_evaluation('供应商选择原因', '供应商选择原因TEST')
        self.input_onework_key_components_flow_procurement_evaluation('份额', '50')
        self.input_onework_key_components_flow_procurement_evaluation('是否客供物料', '是', False)
        self.input_onework_key_components_flow_procurement_evaluation('价格趋势（6个月）', '持平', False)
        self.input_onework_key_components_flow_procurement_evaluation('是否NUDD', '是', False)
        self.input_onework_key_components_flow_procurement_evaluation('NUDD说明', 'NUDD说明TEST')
        self.input_onework_key_components_flow_procurement_evaluation('NUDD管理方案', 'NUDD管理方案TEST')
        self.input_onework_key_components_flow_procurement_evaluation('评审结论', '通过', False)
        self.input_onework_key_components_flow_procurement_evaluation('原因及修改建议', '原因及修改建议TEST')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_oneworks()

    @allure.step("oneworks节点：采购执行评估 页面填写 组合流程")
    def onework_key_components_flow_flowsix(self, code):
        self.enter_oneworks_edit(code, '采购执行评估')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.scroll_onework_key_components_flow_material_details('采购执行')
        self.input_onework_key_components_flow_procurement_execution('L/T(天)', '1')
        self.input_onework_key_components_flow_procurement_execution('最小下单量(pcs)', '1')
        self.input_onework_key_components_flow_procurement_execution('此项目峰值需求(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('供应商总产能(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('分配传音产能(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('供应弹性(%)', '1')
        self.input_onework_key_components_flow_procurement_execution('共用项目需求合计(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('此项目产能分配(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('共用项目名', '共用项目名test')
        self.input_onework_key_components_flow_procurement_execution('产能评审结论', '通过', False)
        self.input_onework_key_components_flow_procurement_execution('原因及修改建议', '原因及修改建议test')
        self.input_onework_key_components_flow_procurement_execution('备料建议', '备料建议test')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.scroll_onework_key_components_flow_material_details('采购执行')
        self.input_onework_key_components_flow_procurement_execution('L/T(天)', '1')
        self.input_onework_key_components_flow_procurement_execution('最小下单量(pcs)', '1')
        self.input_onework_key_components_flow_procurement_execution('此项目峰值需求(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('供应商总产能(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('分配传音产能(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('供应弹性(%)', '1')
        self.input_onework_key_components_flow_procurement_execution('共用项目需求合计(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('此项目产能分配(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('共用项目名', '共用项目名test')
        self.input_onework_key_components_flow_procurement_execution('产能评审结论', '通过', False)
        self.input_onework_key_components_flow_procurement_execution('原因及修改建议', '原因及修改建议test')
        self.input_onework_key_components_flow_procurement_execution('备料建议', '备料建议test')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_oneworks()

    @allure.step("oneworks节点：采购PTC评估 页面填写 组合流程")
    def onework_key_components_flow_ptc(self, code):
        self.enter_oneworks_edit(code, '采购PTC评估')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.scroll_onework_key_components_flow_material_details('PTC')
        self.input_onework_key_components_flow_ptc('评审结论', '同意')
        self.input_onework_key_components_flow_ptc('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.scroll_onework_key_components_flow_material_details('PTC')
        self.input_onework_key_components_flow_ptc('评审结论', '同意')
        self.input_onework_key_components_flow_ptc('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_oneworks()

    @allure.step("oneworks节点：采购SQM评估 页面填写 组合流程")
    def onework_key_components_flow_sqm(self, code):
        self.enter_oneworks_edit(code, '采购SQM评估')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.scroll_onework_key_components_flow_material_details('SQM')
        self.input_onework_key_components_flow_sqm('评审结论', '同意')
        self.input_onework_key_components_flow_sqm('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.scroll_onework_key_components_flow_material_details('SQM')
        self.input_onework_key_components_flow_sqm('评审结论', '同意')
        self.input_onework_key_components_flow_sqm('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_oneworks()

    @allure.step("oneworks节点：标准化部评估 页面填写 组合流程")
    def onework_key_components_flow_standardized_evaluation(self, code):
        self.enter_oneworks_edit(code, '标准化部评估')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.input_onework_key_components_flow_standardized_evaluation('认证状态', '认证通过')
        self.input_onework_key_components_flow_standardized_evaluation('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.input_onework_key_components_flow_standardized_evaluation('认证状态', '认证通过')
        self.input_onework_key_components_flow_standardized_evaluation('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_oneworks()

    @allure.step("点击同意-确定")
    def click_onework_key_components_flow_agree(self):
        self.frame_exit()
        self.is_click_tbm(user['同意'])
        self.is_click_tbm(user['确定'])
        self.base_get_img('result')
        logging.info('点击确定')

    @allure.step("点击复选框")
    def click_onework_key_components_flow_checkbox(self, sort='all'):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击复选框
        @param sort:物料编码，传入物料编码；默认‘all’表示点击全选复选框
        """
        sleep(3)
        if sort == 'all':
            self.is_click_tbm(user['oneworks-节点-评估关键器件-复选框全选'])
        else:
            self.is_click_tbm(user['oneworks-节点-评估关键器件-复选框单选'], sort)
        logging.info('点击复选框')

    @allure.step("点击一键填写")
    def click_onework_key_components_flow_onepress(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击一键填写
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写'])

    @allure.step("点击一键填写-确定")
    def click_onework_key_components_flow_onepress_confirm(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击一键填写-确定
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-确定'])

    @allure.step("点击一键填写-取消")
    def click_onework_key_components_flow_onepress_cancel(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击一键填写-取消
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-取消'])

    @allure.step("输入一键填写内容")
    def input_onework_key_components_flow_onepress(self, field, name):
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
    def input_onework_key_components_flow_procurement_evaluation(self, choice, details, mode=True):
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
    def input_onework_key_components_flow_procurement_execution(self, choice, details, mode=True):
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
    def input_onework_key_components_flow_ptc(self, choice, details):
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
    def input_onework_key_components_flow_sqm(self, choice, details):
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
    def input_onework_key_components_flow_standardized_evaluation(self, choice, details):
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

    @staticmethod
    def delete_key_components_flow_sql(model):
        a = SQL('TBM', 'test')
        a.change_db(
            f"UPDATE kd_flow_main SET is_deleted = 1 WHERE device_bid IN ( SELECT bid FROM kd_device_info WHERE model "
            f"= '{model}')"
        )
        logging.info('调用sql脚本修改数据库数据')

    @allure.step("断言审批状态")
    def assert_add_flow(self, status):
        try:
            ValueAssert.value_assert_equal(status, '审批通过')
        except:
            ValueAssert.value_assert_equal(status, 'approved')

if __name__ == '__main__':
    pass
