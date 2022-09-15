import datetime
import logging
from time import sleep
from libs.common.read_element import Element
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class ShippingCountryFlow(CenterComponent, APIRequest):
    """出货国家_出货国家流程"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("出货国家", "出货国家流程")

    @allure.step("删除操作")
    def click_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['确定'])

    @allure.step("新建流程后的后置删除处理")
    def delete_shipping_country_flow(self, code):
        logging.info(f'开始撤回流程：{code}')
        self.recall_process(code)
        self.click_menu("出货国家", "出货国家流程")
        self.click_delete(code)
        self.assert_toast()
        logging.info('撤回删除流程成功')

    @allure.step("出货国家流程新增页面 - 输入项目信息")
    def input_add_item_info(self, info, select):
        """
        出货国家流程新增页面 - 输入项目信息
        :param info: 选择要输入的信息
        :param select: 选择信息内容
        """
        if info == '品牌':
            self.is_click_tbm(user['项目信息输入框'], info)
            logging.info('点击项目信息输入框:{}'.format(info))
            self.scroll_into_view(user['项目信息输入框选择'], select)
            sleep(1)
            self.is_click_tbm(user['项目信息输入框选择'], select)
            logging.info('选择项目信息 品牌:{}'.format(select))

        elif info == '项目':
            self.input_text(user['项目信息输入框'], select, info)
            logging.info('输入项目信息 项目:{}'.format(select))
        elif info == '描述':
            self.input_text(user['项目信息文本框'], select, info)
            logging.info('输入项目信息 描述:{}'.format(select))
        else:
            print('请选择正确的项目信息输入：品牌 or 项目 or 描述')

    @allure.step("出货国家流程新增页面 - 新增产品定义信息")
    def input_add_product_definition_info(self, header, content):
        """
        出货国家流程新增页面 - 新增产品定义信息
        :param header: 选择要输入的信息
        :param content: 选择信息内容
        """
        definition_dict = {'全球版本': '4', '市场名称': '5', '项目名称': '6', 'MEMORY': '7', 'BANDSTRATEGY': '8',
                           '产品经理': '9', '项目经理': '10', 'aaa': '12', 'bbb': '13'}
        select_list = ['全球版本', 'MEMORY', 'BAND STRATEGY', 'aaa', 'bbb', '再增']

        input_list = ['市场名称', '项目名称', '摄像头', '型号', '新增']
        member_list = ['产品经理', '项目经理']
        column = self.get_table_info(user['产品定义信息字段'], header)
        if header in select_list:
            self.is_click_tbm(user['产品定义信息输入'], column)
            self.is_click_tbm(user['产品定义信息选择'], content)
        elif header in input_list:
            self.input_text(user['产品定义信息输入'], content, column)
        elif header in member_list:
            self.is_click_tbm(user['产品定义信息输入'], column)
            self.input_text(user['产品定义信息成员列表输入框'], content)
            sleep(1)
            self.is_click_tbm(user['成员选择'], content)
            self.is_click_tbm(user['产品定义信息成员确定'])
        else:
            print(f'请输入正确选项：{definition_dict}')

    @allure.step("产品定义信息-点击确定")
    def click_product_definition_confirm(self):
        self.is_click_tbm(user['产品定义信息确定'])

    @allure.step("选择汇签/抄送人员")
    def select_signatory(self, choice, name):
        """
        出货国家流程新增页面 - 选择汇签/抄送人员
        :param choice: 汇签/抄送人员选择框
        :param name: 人员名字
        """
        self.is_click_tbm(user['汇签/抄送人员选择框'], choice)
        self.is_click_tbm(user['成员列表清空'], choice)
        self.input_text(user['成员列表输入框'], name)
        sleep(1)
        self.is_click_tbm(user['成员选择'], name)
        self.is_click_tbm(user['成员确定'])

    @allure.step("点击提交")
    def click_add_submit(self):
        """点击提交"""
        self.scroll_into_view(user['提交'])
        sleep(0.5)
        self.is_click_tbm(user['提交'])

    @allure.step("获取出货国家流程第一列内容")
    def get_info(self, item):
        """
        获取出货国家流程第一列内容
        @parma item:项目名称
        @return:返回文本及索引位置分别是'No.'==0; '标题'==1; '流程编码'==2; '业务类型'==3; '项目'==4; '品牌'==5; '单据状态'==6; '申请人'==7; '申请时间'==8; '操作'==9;
        """
        self.click_menu("出货国家", "出货国家流程")
        sleep(1)
        self.refresh()
        info = self.find_elements_tbm(user['表格指定行内容'], item)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    @allure.step("出货国家流程新增页面 - 项目信息组合")
    def add_item_info(self, item):
        self.input_add_item_info('品牌', 'Infinix')
        self.input_add_item_info('项目', item)
        self.input_add_item_info('描述', '出货国家流程新增描述test')

    @allure.step("出货国家流程新增页面 - 产品定义信息组合")
    def add_product_definition_info(self, item):
        self.click_add()
        self.input_add_product_definition_info('全球版本', '版本1')
        self.input_add_product_definition_info('市场名称', f'市场名称{item}')
        self.input_add_product_definition_info('项目名称', item)
        self.input_add_product_definition_info('MEMORY', '128+8')
        self.input_add_product_definition_info('BANDSTRATEGY', '拉美市场')
        self.input_add_product_definition_info('项目经理', '李小素')
        self.input_add_product_definition_info('aaa', '2G')
        self.input_add_product_definition_info('bbb', 'MT6761')
        self.click_product_definition_confirm()

    @allure.step("出货国家流程新增流程 组合")
    def add_flow(self, item):
        self.click_add()
        self.add_item_info(item)
        self.add_product_definition_info(item)
        self.select_signatory('汇签人员', '李小素')
        self.click_add_submit()
        self.assert_toast()

    @allure.step("出货国家流程 新增流程 产品部管理员审核 组合")
    def product_department_administrator_review(self, code):
        self.assert_my_todo_node(code, '产品部管理员审核', True)
        self.enter_oneworks_edit(code)
        self.click_onework_agree()
        self.assert_toast()
        self.quit_oneworks()
        self.assert_my_todo_node(code, '产品部汇签', True)

    @allure.step("出货国家流程 新增流程 产品部汇签 组合")
    def product_department_sign(self, code):
        self.enter_oneworks_edit(code)
        self.click_onework_agree()
        self.assert_toast()
        self.quit_oneworks()
        self.assert_my_todo_node(code, '产品经理修改', True)

    @allure.step("出货国家流程 新增流程 产品经理修改 组合")
    def product_manager_modification(self, code):
        self.enter_oneworks_edit(code)
        querytime = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        self.input_oneworks_product_definition_info('全球版本', '版本2')
        self.input_oneworks_product_definition_info('市场名称', f'市场名称test{querytime}')
        self.input_oneworks_product_definition_info('项目名称', f'项目名称test{querytime}')
        self.input_oneworks_product_definition_info('MEMORY', '64+8')
        self.input_oneworks_product_definition_info('BANDSTRATEGY', '公开市场')
        self.input_oneworks_product_definition_info('项目经理', '李小素')
        self.input_oneworks_product_definition_info('aaa', '1G')
        self.input_oneworks_product_definition_info('bbb', 'G70')
        self.click_onework_agree()
        self.assert_toast()
        self.quit_oneworks()
        self.assert_my_todo_node(code, '产品部管理员复核', True)

    @allure.step("出货国家流程 新增流程 产品经理修改 组合")
    def product_department_administrator_re_review(self, code):
        self.enter_oneworks_edit(code)
        self.click_onework_agree()
        self.assert_toast()
        self.quit_oneworks()
        self.assert_my_todo_node(code, '项目经理审批', True)

    @allure.step("点击同意-确定")
    def click_onework_agree(self):
        self.frame_exit()
        self.is_click_tbm(user['同意'])
        self.is_click_tbm(user['确定'])
        logging.info('点击同意-确定')

    @allure.step("oneworks-产品经理修改-编辑产品定义信息")
    def input_oneworks_product_definition_info(self, header, content):
        """
        oneworks-节点：产品经理修改-查看详情页面
        编辑产品定义信息
        :param header: 选择要输入的信息
        :param content: 选择信息内容
        """
        definition_dict = {'全球版本': '4', '市场名称': '5', '项目名称': '6', 'MEMORY': '7', 'BANDSTRATEGY': '8',
                           '产品经理': '9', '项目经理': '10', 'aaa': '12', 'bbb': '13'}
        select_list = ['全球版本', 'MEMORY', 'BANDSTRATEGY']
        select1_list = ['aaa', 'bbb']
        input_list = ['市场名称', '项目名称']
        member_list = ['产品经理', '项目经理']
        if header in select_list:
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-编辑'])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-输入框'], definition_dict[header])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-选择'], content)
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-确定'])
        elif header in select1_list:
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-编辑'])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-输入框2'], definition_dict[header])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-选择'], content)
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-确定'])
        elif header in input_list:
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-编辑'])
            self.input_text(user['oneworks-节点-产品经理修改-产品定义信息-输入框'], content, definition_dict[header])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-确定'])
        elif header in member_list:
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-编辑'])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-输入框2'], definition_dict[header])
            self.input_text(user['产品定义信息成员列表输入框'], content)
            sleep(1)
            self.is_click_tbm(user['成员选择'], content)
            self.is_click_tbm(user['产品定义信息成员确定'])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-确定'])
        else:
            print(f'请输入正确选项：{definition_dict}')


if __name__ == '__main__':
    pass
