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
if __name__ == '__main__':
    pass
