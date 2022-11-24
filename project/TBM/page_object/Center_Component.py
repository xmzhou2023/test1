from selenium.webdriver import ActionChains, Keys
from libs.common.read_element import Element
from libs.config.conf import BASE_DIR
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)


class CenterComponent(Base, APIRequest):
    """用户类"""
    # 审核人
    review = '李小素'

    def hover(self, locator, *choice):
        """鼠标悬停"""
        sleep(1)
        element = self.find_element(locator, *choice)
        # 创建Action对象
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(1)

    def input_text(self, locator, txt, *choice):
        """输入文本"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        ele.clear()
        ele.send_keys(txt)
        logging.info("输入文本：{}".format(txt))

    def click_logout(self):
        """点击退出登录"""
        self.is_click(user['头像'])
        self.is_click_tbm(user['退出登录'])

    def click_accountlogin(self):
        """点击帐号密码登录"""
        self.is_click(user['账号密码登录'])

    def input_account(self, content):
        """输入工号"""
        self.input_text(user['工号输入框'], txt=content)
        sleep()

    def input_passwd(self, content):
        """输入密码"""
        self.input_text(user['密码输入框'], txt=content)
        sleep()

    def check_box(self):
        """判断是否被选中"""
        return self.select_state(user['隐私保护勾选框'])

    def click_proxy_checkbox(self):
        """点击复选框"""
        if not self.check_box():
            self.is_click(user['隐私保护勾选框'])

    def click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(user['登录'])
        sleep(6)

    def relogin(self, username):
        """统一登录֤"""
        self.click_logout() # 退出登录
        self.click_accountlogin() # 点击帐户密码登录
        self.input_account(username) # 输入帐户名
        self.input_passwd('xLily6x') # 输入密码
        self.click_loginsubmit()

    @allure.step("点击菜单")
    def click_menu(self, metatitle, nestmenu):
        """点击菜单"""
        ele = self.element_text(user['当前菜单']).strip()
        if ele != nestmenu:
            try:
                self.is_click_tbm(user['meta-title'], metatitle)
                logging.info(f'点击一级菜单:{metatitle}')
                self.is_click_tbm(user['nest-menu'], nestmenu)
                logging.info(f'点击二级菜单:{nestmenu}')
                sleep(1)
                self.refresh()
                self.click_menu(metatitle, nestmenu)
            except Exception as e:
                self.base_get_img()
                self.refresh()
                self.is_click_tbm(user['meta-title'], metatitle)
                logging.info(f'点击一级菜单:{metatitle}')
                self.is_click_tbm(user['nest-menu'], nestmenu)
                logging.info(f'点击二级菜单:{nestmenu}')
                sleep(1)
                self.refresh()
                self.click_menu(metatitle, nestmenu)

    @allure.step("初始化浏览器")
    def refresh_webpage(self):
        logging.info("初始化浏览器")
        self.refresh()
        self.driver.switch_to.default_content()
        handles = self.driver.window_handles
        logging.info('当前窗口：{}'.format(handles))
        if len(handles) != 1:
            for i in range(1, len(handles)):
                self.close_switch(1)
        else:
            self.switch_window(0)
        text = self.element_text(user['所有文本']).replace("\n", "|")
        if '扫码快捷登录' in text:
            """使用统一登录"""
            logging.info("前置条件：传音统一登录开始")
            self.get_url('http://bom-sit.transsion.com/#/process/home-page')  # 跳转到指定网页
            DomAssert(self.driver).assert_exact_att('首页')
            logging.info("前置条件：传音统一登录成功")

    @allure.step("输入BOM信息")
    def input_bom_info(self, type, content):
        """
        单机头BOM协作新增页面-输入BOM信息
        :param type: 选择要输入的信息
        :param content: 选择信息内容
        """
        if type == '机型':
            self.input_text(user['BOM信息输入框'], content, type)
            sleep(1)
            self.is_click_tbm(user['BOM信息输入框机型选择'], content)
        elif type == '检查关键器件' or type == '制作虚拟贴片/套片':
            self.is_click_tbm(user['BOM信息选择框'], type)
            self.is_click_tbm(user['BOM信息输入框选择'], content)
        else:
            self.is_click_tbm(user['BOM信息输入框'], type)
            self.scroll_into_view(user['BOM信息输入框选择'], content)
            self.is_click_tbm(user['BOM信息输入框选择'], content)
        logging.info('输入BOM信息 : 字段{}， 内容：{}'.format(type, content))

    @allure.step("BomTree信息根据Tree在指定列输入内容")
    def input_bomtree(self, tree, header, content):
        """
        BomTree信息根据Tree在指定列表输入内容
        @param tree:输入选择
        @param header: BomTree要输入的表头；【BOM类型， BOM状态， 物料编码， 用量， 替代组， 份额】
        @param content:输入的内容
        """
        header_list = ['用量', '替代组', '份额', '物料编码', 'BOM状态', 'BOM类型', '数量', '位号']
        input_list = ['用量', '替代组', '份额', '数量', '位号']
        select_list = ['物料编码']
        click_list = ['BOM状态', 'BOM类型']
        if header in header_list:
            col = self.get_table_info(user['BOMTree表格'], header)
            if header in select_list:
                self.is_click_tbm(user['BOMTree编辑'], tree)
                self.readonly_input_text(user['BOMTree'], content, tree, col)
                sleep(1)
                self.is_click_tbm(user['物料编码选择'], content)
                self.is_click_tbm(user['BOMTree确定'], tree)
            elif header in click_list:
                self.is_click_tbm(user['BOMTree'], tree, col)
                self.is_click_tbm(user['BOMTree输入框选择'], content)
            elif header in input_list:
                self.is_click_tbm(user['BOMTree编辑'], tree)
                self.readonly_input_text(user['BOMTree'], content, tree, col)
                self.is_click_tbm(user['BOMTree确定'], tree)
            logging.info('输入BomTree内容， 字段： {} ， 选择： {}'.format(header, content))
        else:
            logging.error('请输入正确的表头字段')
            raise ValueError('请输入正确的表头字段')

    @allure.step("新增物料输入内容")
    def input_add_material(self, tree, header, content):
        """
        新增物料后，模版信息根据条件在新增的物料输入内容并且点击
        @param tree:上级物料编码
        @param content:输入的内容
        @param header: BomTree要输入的表头；{'BOM类型':'2','BOM状态':'3','物料编码':'6','用量':'9','替代组':'10','份额':'11',}
        上级物料已输入编码'17600563'，根据编码填写新增的物料编码，输入的数据是'17600606'
        user.input_add_material('17600563', '物料编码', '17600606')
        """
        input_list = ['用量', '替代组', '份额', '数量']
        select_list = ['物料编码']
        col = self.get_table_info(user['BOMTree表格'], header)
        if header in select_list:
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料'], content, tree, col)
            sleep(1)
            self.is_click_tbm(user['物料编码选择'], content)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        elif header in input_list:
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料'], content, tree, col)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        else:
            logging.error("输入正确需要操作的表头")
            raise ValueError('输入正确需要操作的表头')

    def assert_bomtree(self, header, content):
        col = self.get_table_info(user['BOMTree表格'], header)
        DomAssert(self.driver).assert_control(user['BOMTree新增物料行'], content, col, result=False)

    def inner_text(self, locator, *args):
        """获取元素的文本"""
        ele = self.find_element(locator, *args)
        _text = ele.get_attribute('innerText').replace("\n", "|")
        logging.info("获取文本：{}".format(_text))
        return _text

    @allure.step("获取BOMTREE指定列内容")
    def get_bomtree_info(self, material, header, type=None):
        """
        获取单机头BOM协作-BOMTREE指定列内容
        @param material: 物料名
        @param header: 指定字段文本
        @param type:如果第一个参数是物料编码， 需要给参数type传 code
        example: get_bomtree_info('单机头', '用量') 获取BomTree表格中Tree为单机头的用量文本
        """
        column = self.get_table_info(user['表格字段'], header)
        if type == "code":
            info = self.inner_text(user['BomTree指定物料编码内容'], material, column)
        else:
            info = self.inner_text(user['BomTree内容'], material, column)

        return info

    @allure.step("断言：BomTree指定行的指定数据")
    def assert_BomTree_OnepressResult(self, material, header, content, type=None):
        """
        获取单机头BOM协作-BOMTREE指定列内容
        @param material: 物料名
        @param header: 指定字段
        @param content: 需要比对的内容
        @param type:如果第一个参数是物料编码， 需要给参数type传 code
        example: get_bomtree_info('单机头', '用量') 获取BomTree表格中Tree为单机头的用量文本
        """
        ac_content = self.get_bomtree_info(material, header, type)
        try:
            assert content in ac_content
            logging.info("断言成功，结果:{}包含指定内容:{}".format(ac_content, content))
        except:
            logging.error("断言失败，结果不包含指定内容")
            raise

    @allure.step("第一列内容")
    def get_info(self, metatitle, nestmenu):
        """
        获取整机BOM协作第一列内容 @return:返回文本及索引位置分别是'No.'：0; '流程编码':1; '制作类型':2; '机型'：3; '品牌':4; '市场':5; '阶段':6; '单据状态':7;
        '同步状态':8; '申请人':9; '创建时间':10; '操作':11
        :param metatitle: 一级菜单
        :param nestmenu: 二级菜单
        """
        self.click_menu(metatitle, nestmenu)
        self.refresh()
        sleep(1)
        info = self.find_elements_tbm(user['表格内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    @allure.step("断言整机BOM协作新增成功后，页面表格内容是否正确")
    def assert_add_result(self, metatitle, nestmenu, *content):
        """
        断言整机BOM协作新增成功后，页面表格内容是否正确
        :param metatitle: 一级菜单
        :param nestmenu: 二级菜单
        :param content: 需要，可以一次传入多个
        """
        try:
            contents = self.get_info(metatitle, nestmenu)
            assert set(content) <= set(contents)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("进入框架")
    def enter_oneworks_iframe(self):
        self.frame_enter(user['待办列表-iframe'])

    @allure.step("退出oneworks查看流程页面")
    def quit_oneworks(self):
        self.frame_exit()
        logging.info("退出oneworks查看流程页面")
        self.close_switch(1)
        logging.info("关闭窗口")
        self.refresh_webpage()

    @allure.step("进入待办列表框架")
    def refresh_todo_list(self):
        self.refresh()
        self.frame_enter(user['待办列表-iframe'])
        self.is_click_tbm(user['待办列表-刷新'])

    @allure.step("点击提交")
    def click_add_submit(self):
        self.scroll_into_view(user['提交'])
        sleep(0.5)
        self.is_click_tbm(user['提交'])

    @allure.step("待办列表 根据单据号 筛选")
    def screening_code(self, code):
        """
        @param code:流程编码
        """
        self.is_click_tbm(user['待办列表-筛选框'])
        self.input_text(user['待办列表-筛选框-单据号'], code)
        self.is_click_tbm(user['待办列表-筛选框-筛选'])
        for i in range(20):
            text = self.element_text(user['所有文本']).replace("\n", "|")
            if code not in text:
                self.is_click_tbm(user['待办列表-刷新'])
                sleep(1)
            else:
                break
        self.base_get_img()

    @allure.step("进入 我的待办 页面")
    def enter_my_todo(self):
        ele = self.element_text(user['当前菜单']).strip()
        if ele == '我的待办':
            self.refresh_todo_list()
        else:
            self.click_menu('待办列表', '我的待办')
            sleep(1)
            try:
                self.refresh_todo_list()
            except:
                self.refresh_todo_list()

    @allure.step("进入 我申请的 页面")
    def enter_my_application(self):
        ele = self.element_text(user['当前菜单']).strip()
        if ele == '我申请的':
            self.refresh_todo_list()
        else:
            self.click_menu('待办列表', '我申请的')
            try:
                self.refresh_todo_list()
            except:
                self.refresh_todo_list()

    @allure.step("点击 查看详情 进入 oneworks 页面")
    def loginUser_judge(self, code, node=None):
        """
        判断节点审批人与当前登录人是否一致
        @param code:流程编码
        @param node:节点名称
        """
        assignee = self.API_getHistoric(code, node)
        if assignee.find('[') != -1:
            assignee = assignee[:assignee.index('[')]
        logging.info('节点：{} 当前审批人是：{}'.format(node, assignee))
        User = self.find_element(user['登录人']).get_attribute('innerText')
        User = User[:User.index('，')]
        logging.info('当前登录人是：{}'.format(User))
        if assignee != User:
            Employee_Number = self.API_queryDeptAndEmployee(assignee)['data'][0]['employeeNo']
            self.relogin(Employee_Number)

    @allure.step("点击 查看详情 进入 oneworks 页面")
    def enter_oneworks_edit(self, code, node=None):
        """
        点击 查看详情 进入 oneworks 页面
        输入流程编码过滤后，根据当前节点名称点击查看详情进入详情页面
        @param code:流程编码
        @param node:节点名称
        """
        self.loginUser_judge(code, node)
        self.enter_my_todo()
        self.screening_code(code)
        if node is not None:
            self.is_click_tbm(user['待办列表-我申请的-查看详情(节点名称)'], node)
        else:
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], code)
        logging.info('点击查看详情')
        self.frame_exit()
        logging.info('跳出框架')
        self.switch_window(1)
        logging.info('切换窗口')
        try:
            sleep(2)
            logging.info('强制等待')
            self.frame_enter(user['待办列表-iframe'])
            logging.info('进入框架')
            DomAssert(self.driver).assert_att('基本信息')
        except:
            self.refresh()
            sleep(2)
            logging.info('强制等待')
            self.frame_enter(user['待办列表-iframe'])
            logging.info('进入框架')
            DomAssert(self.driver).assert_att('基本信息')

    @allure.step("点击 查看详情 进入 oneworks 页面")
    def enter_oneworks_application(self, code, node=None):
        """
        点击 查看详情 进入 oneworks 页面
        输入流程编码过滤后，根据当前节点名称点击查看详情进入详情页面
        @param code:流程编码
        @param node:节点名称
        """
        self.enter_my_application()
        self.screening_code(code)
        if node is not None:
            self.is_click_tbm(user['待办列表-我申请的-查看详情(节点名称)'], node)
        else:
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], code)
        logging.info('点击查看详情')
        self.frame_exit()
        logging.info('跳出框架')
        self.switch_window(1)
        logging.info('切换窗口')
        try:
            sleep(2)
            logging.info('强制等待')
            self.frame_enter(user['待办列表-iframe'])
            logging.info('进入框架')
            DomAssert(self.driver).assert_att('基本信息')
        except:
            self.refresh()
            sleep(2)
            logging.info('强制等待')
            self.frame_enter(user['待办列表-iframe'])
            logging.info('进入框架')
            DomAssert(self.driver).assert_att('基本信息')

    @allure.step("断言")
    def assert_toast(self, content=None):
        # att = self.element_text(user['toast提示'])
        try:
            att = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']/p"))).text
            self.base_get_img()
            logging.info('获取toast提示语：{}'.format(att))
            try:
                if content is None:
                    assert '请求成功' in att or '审核通过' in att or '操作成功' in att or '处理成功' in att
                    logging.info('断言成功，toast提示为：{}'.format(att))
                else:
                    assert content in att
                    logging.info('断言成功，toast提示为：{}'.format(att))
            except:
                logging.error('断言失败，实际提示为：{}'.format(att))
                raise
        except:
            logging.error('断言失败，未获取到toast提示语/toast提示语错误')
            raise

    @allure.step("我的待办页面-断言：我的待办中存在/不存在该条单据在指定审核节点")
    def assert_my_todo_node(self, code, node, exist=False):
        """
        我的待办页面-断言：成功处理了流程后，我的待办中存在/不存在该条单据在指定审核节点
        @param code:流程编码
        @param node:节点名称
        @param exist:断言存在或者不存在
        """
        self.enter_my_todo()
        self.screening_code(code)
        actual_node = self.element_text(user['待办列表-我的待办-当前节点'], code)
        if exist is False:
            try:
                assert actual_node != node
                logging.info('断言成功，我的待办中该条单据不存在:{}节点，实际在:{}节点'.format(node, actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我的待办中存在该条单据在:{}审核节点'.format(actual_node))
                raise
            finally:
                self.frame_exit()
        else:
            try:
                assert actual_node == node
                logging.info('断言成功，我的待办中存在该条单据在:{}审核节点'.format(actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我的待办中该条单据不存在:{}节点，实际在:{}节点'.format(node, actual_node))
                raise
            finally:
                self.frame_exit()

    @allure.step("我申请的页面-断言：我的待办中存在/不存在该条单据在指定审核节点")
    def assert_my_application_node(self, code, node, exist=False):
        """
        我申请的页面-断言：成功处理了流程后，我申请的中存在/不存在该条单据在指定审核节点
        @param code:流程编码
        @param node:节点名称
        @param exist:断言存在或者不存在
        """
        self.enter_my_application()
        self.screening_code(code)
        actual_node = self.element_text(user['待办列表-我申请的-当前节点'], code)
        if exist is False:
            try:
                assert actual_node != node
                logging.info('断言成功，我申请的中该条单据不存在:{}节点，实际在:{}节点'.format(node, actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中存在该条单据在:{}节点'.format(actual_node))
                raise
            finally:
                self.frame_exit()
        else:
            try:
                assert actual_node == node
                logging.info('断言成功，我申请的中存在该条单据在:{}审核节点'.format(actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中不存在该条单据在:{}审核节点'.format(actual_node))
                raise
            finally:
                self.frame_exit()

    @allure.step("我申请的页面-断言：我的待办中存在/不存在该条单据在指定流程")
    def assert_my_application_flow(self, code, flow, exist=True):
        """
        我申请的页面-断言：成功处理了流程后，我申请的中存在/不存在该条单据在指定流程中
        @param code:流程编码
        @param flow:流程名称
        @param exist:断言存在或者不存在
        """
        self.enter_my_application()
        self.screening_code(code)
        actual_flow = self.element_text(user['待办列表-我申请的-当前流程'], code)
        if exist is True:
            try:
                assert actual_flow == flow
                logging.info('断言成功，我申请的中该条单据在:{}流程'.format(actual_flow))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中该条单据不在:{}流程，实际在:{}流程'.format(flow, actual_flow))
                raise
            finally:
                self.frame_exit()
        elif exist is False:
            try:
                assert actual_flow != flow
                logging.info('断言成功，我申请的中该条单据不在:{}流程，实际在:{}流程'.format(flow, actual_flow))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中该条单据在:{}流程'.format(actual_flow))
                raise
            finally:
                self.frame_exit()

    @allure.step("在待办列表-我申请的 根据流程编码对流程进行撤回操作")
    def recall_process(self, code):
        """
        提交流程申请后，在待办列表-我申请的 根据流程编码对流程进行撤回操作
        @param code:流程编码
        """
        self.enter_my_application()
        try:
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], code)
        except:
            self.refresh()
            self.frame_enter(user['待办列表-iframe'])
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], code)
        self.switch_window(1)
        try:
            self.is_click_tbm(user['oneworks-撤回'])
            self.is_click_tbm(user['提示确定'])
        except:
            self.base_get_img()
            self.refresh()
            self.is_click_tbm(user['oneworks-撤回'])
            self.is_click_tbm(user['提示确定'])
        self.frame_exit()
        DomAssert(self.driver).assert_att('操作成功')
        self.close_switch(1)
        self.frame_exit()

    @allure.step("断言：校验转交流程在转交人")
    def assert_flow_deliver(self, code, name):
        """
        断言：BOM工程师审批页面 确认转交后，校验流程移交到转交人上
        @param code:流程编码
        @param name:审批人名称
        """
        self.enter_my_application()
        self.screening_code(code)
        approver = self.element_text(user['待办列表-我申请的-审批人'], code)
        try:
            assert name in approver
            logging.info('断言成功，审批人为:{}'.format(approver))
        except:
            self.base_get_img()
            logging.error('断言失败，审批人为:{}'.format(approver))
            raise
        finally:
            self.frame_exit()

    @allure.step("点击同意按钮")
    def click_agree(self):
        self.frame_exit()
        self.is_click_tbm(user['同意'])
        logging.info('点击同意')

    @allure.step("提示框点击确定")
    def click_dialog_confirm(self):
        self.is_click_tbm(user['提示确定'])
        logging.info('提示框点击确定')

    @allure.step("提示框点击取消")
    def click_dialog_cancel(self):
        self.is_click_tbm(user['提示取消'])
        logging.info('提示框点击取消')

    @allure.step("oneworks点击取消")
    def click_oneworks_cancel(self):
        self.is_click_tbm(user['提示取消'])
        logging.info('点击取消')

    @allure.step("oneworks点击同意-确定按钮")
    def click_oneworks_agree(self):
        self.click_agree()
        self.click_dialog_confirm()

    @allure.step("断言OneWorks同意成功流程")
    def assert_OneWorks_AgreeFlow(self):
        self.click_oneworks_agree()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("oneworks点击转交")
    def click_oneworks_refer(self):
        self.frame_exit()
        self.is_click_tbm(user['oneworks-转交'])
        logging.info('点击转交')

    @allure.step("oneworks转交 点击确认")
    def click_oneworks_refer_comfirm(self):
        self.is_click_tbm(user['oneworks-转交-确定'])
        logging.info('点击转交确定')

    @allure.step("断言：是否存在确定转交按钮")
    def assert_oneworks_comfirmrefer_exist(self, result):
        DomAssert(self.driver).assert_control(user['oneworks-确定转交'], result=result)

    @allure.step("转交 输入转交人")
    def input_oneworks_refer(self, referrer):
        """
        转交 输入转交人
        @param referrer:转交人
        """
        self.input_text(user['oneworks-转交-转交人输入'], referrer)
        logging.info('输入转交人：{}'.format(referrer))
        self.is_click_tbm(user['oneworks-转交-查询'])
        logging.info('点击查询')
        sleep(1)

    @allure.step("转交 选择转交人")
    def select_oneworks_refer(self, referrer):
        """
        BOM工程师审批页面 转交 选择转交人
        @param referrer:转交人
        """
        self.is_click_tbm(user['oneworks-转交-转交人选择'], referrer)
        logging.info('点击转交人')

    @allure.step("选择转交后 点击取消")
    def click_oneworks_refer_cancel(self):
        self.is_click_tbm(user['oneworks-转交取消'])
        logging.info('点击转交取消')

    @allure.step("选择转交后 点击确认转交")
    def click_oneworks_refer_comfirmrefer(self):
        self.is_click_tbm(user['oneworks-确定转交'])
        logging.info('点击确认转交')

    @allure.step("断言： 是否存在转交，回退按钮")
    def assert_oneworks_rollback_refer_exist(self, result):
        DomAssert(self.driver).assert_control(user['oneworks-回退'], result=result)
        DomAssert(self.driver).assert_control(user['oneworks-转交'], result=result)

    @allure.step("断言： 是否存在转交按钮")
    def assert_oneworks_refer_exist(self, result):
        DomAssert(self.driver).assert_control(user['oneworks-转交'], result=result)

    @allure.step("点击拒绝")
    def click_oneworks_refuse(self):
        self.frame_exit()
        self.is_click_tbm(user['oneworks-拒绝'])
        logging.info('点击拒绝')
        self.is_click_tbm(user['提示确定'])
        logging.info('点击确定')

    @allure.step("点击回退，根据node选择回退节点")
    def click_oneworks_rollback(self, node):
        """
        @param node:节点
        """
        self.frame_exit()
        self.is_click_tbm(user['oneworks-回退'])
        logging.info('点击回退')
        self.is_click_tbm(user['oneworks-回退到'])
        node_dict = {'申请人': '申请人[Applicant]', node: node}
        self.is_click_tbm(user['oneworks-回退选择'], node_dict[node])
        logging.info('回退到：{}'.format(node))

    @allure.step("点击回退确定")
    def click_oneworks_rollback_confirm(self):
        self.is_click_tbm(user['oneworks-回退确定'])
        logging.info('点击回退确定')

    @allure.step("点击新增")
    def click_add(self):
        self.is_click_tbm(user['新增'])
        if self.element_exist(user['基本信息']) is False:
            self.is_click_tbm(user['新增'])
            sleep(1)
        DomAssert(self.driver).assert_att('基本信息')

    @allure.step("点击查看")
    def click_check(self, code):
        """
        根据流程编码点击查看 进行查看操作
        @param code:流程编码
        """
        self.is_click_tbm(user['查看'], code)

    @allure.step("进入oneworks查看流程页面")
    def enter_onework_check(self, code):
        sleep(1)
        self.click_check(code)
        self.switch_window(1)
        sleep(1)
        self.frame_enter(user['待办列表-iframe'])
        sleep(2)
        DomAssert(self.driver).assert_att('基本信息')

    @allure.step("获取oneworks页面的Bom信息")
    def get_onework_bominfo(self, select):
        """
        获取oneworks页面的Bom信息
        @param select:需要获取的信息类型： 制作类型， 品牌， 机型， 阶段， 市场， 模板， 自研/外研
        """
        self.scroll_into_view(user['BomTree'])
        DomAssert(self.driver).assert_control(user['BomTreeTitle'])
        if select == '机型':
            BomInfo = self.element_text(user['OneworksBom信息-机型'])
            logging.info('获取Bom信息：{}'.format(BomInfo))
            return BomInfo
        BomInfo = self.element_input_text(user['BOM信息输入框'], select)
        logging.info('获取Bom信息：{}'.format(BomInfo))
        return BomInfo

    @allure.step("补充工厂页面输入生产工厂信息")
    def input_oneworks_plant_info(self, plant, content):
        """
        补充工厂页面输入生产工厂信息
        :param plant: 选择工厂：国内组包工厂、 国内贴片工厂、 海外组包工厂、 海外贴片工厂
        :param content: 需要输入的工厂编号
        """
        if plant in ('国内组包工厂', '国内贴片工厂', '海外组包工厂', '海外贴片工厂'):
            self.readonly_input_text(user['生产工厂信息输入框'], content, plant)
            self.is_click_tbm(user['生产工厂信息输入框选择'], content)
        else:
            logging.error('请输入正确的工厂')
            raise

    @allure.step("补充工厂页面点击’一键/‘")
    def click_oneworks_slash(self):
        self.is_click_tbm(user['补充工厂一键/'])

    @allure.step("补充工厂页面点击 一键填写按钮")
    def click_oneworks_onepress_write(self):
        self.is_click_tbm(user['补充工厂一键填写'])

    @allure.step("补充工厂页面点击 一键填写-确定按钮")
    def click_oneworks_onepress_write_confirm(self):
        self.is_click_tbm(user['补充工厂一键填写确定'])

    @allure.step("补充工厂页面点击检查贴片工厂，选择贴片工厂正确/不正确")
    def click_oneworks_plant_check(self, select):
        """
        补充工厂页面点击检查贴片工厂，选择贴片工厂正确/不正确
        :param select: 输入’贴片工厂不正确‘ 或者 ’贴片工厂正确‘
        """
        if select in ('贴片工厂不正确', '贴片工厂正确'):
            self.is_click_tbm(user['补充工厂检查贴片工厂'])
            self.is_click_tbm(user['补充工厂检查贴片工厂选择'], select)
        else:
            logging.error('请输入 贴片工厂不正确 或者 贴片工厂正确')
            raise ValueError('请输入 贴片工厂不正确 或者 贴片工厂正确')

    @allure.step("断言: 在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")
    def assert_oneworks_onepress_write(self):
        try:
            sleep(5)
            write = self.find_element(user['补充工厂一键填写'])
            assert 'is-disabled' in write.get_attribute('class')
            logging.info('断言成功，一键填写按钮不可点击')
        except:
            self.base_get_img()
            logging.error('断言失败，请检查按钮状态')
            raise

    @allure.step("审核人设置")
    def select_business_review(self, audit, type='all'):
        """
        审核人设置-业务评审-：选择用户
        @param type:选择的类别
        @param audit:输入的用户名
        """
        self.scroll_into_view(user['审核人设置'])
        if type == 'all':
            AuditGroup_list = self.find_elements(user['审核类别'])
            for i in AuditGroup_list:
                logging.info('审核组：{}'.format(i.text.strip()))
                AuditGroup = self.find_elements(user['业务审核名单'], i.text.strip())
                infolist = []
                for i in AuditGroup:
                    infolist.append(i.text)
                    self.is_click_tbm(user['审核人类别'], i.text)
                    self.input_text(user['成员列表多选输入框'], audit)
                    sleep(1)
                    self.is_click_tbm(user['成员选择'], audit)
                    self.is_click_tbm(user['成员多选确定'])
                self.base_get_img()
                logging.info('获取审核人名单:{}'.format(infolist))
        else:
            self.is_click_tbm(user['审核人类别'], type)
            self.input_text(user['成员列表多选输入框'], audit)
            sleep(1)
            self.is_click_tbm(user['成员选择'], audit)
            self.is_click_tbm(user['成员多选确定'])
            self.base_get_img()
        logging.info('审核人填写:字段：{}， 审核人：{}'.format(type, audit))

    @allure.step("断言：多次点击BomTree数据，该列数据是不能再进行编辑")
    def assert_oneworks_bomtree_edit(self, tree, header):
        column_class = self.get_table_info(user['编辑验证表头'], header)
        self.mouse_double_click(user['编辑验证'], tree, column_class)
        sleep(0.5)
        DomAssert(self.driver).assert_control(user['编辑验证'], tree, column_class)

    @allure.step("业务审核页面 点击 自检清单")
    def click_self_inspection(self, box, option):
        """
        业务审核页面 点击 自检清单
        @param box:输入框
        @param option:选项
        """
        self.is_click_tbm(user['业务审核-自检清单-业务类型'], box)
        self.is_click_tbm(user['业务审核-自检清单-检查角色'], option)

    @allure.step("业务审核页面 滑动到 自检清单")
    def scroll_self_inspection(self):
        self.scroll_into_view(user['业务审核-自检清单'])

    @allure.step("业务审核页面 自检清单 点击输入检查结果")
    def input_self_inspection_result(self, rule='all', result='通过'):
        if rule == 'all':
            num = self.elements_num(user['业务审核-自检清单-检查结果-规则数量'])
            for i in range(1, num + 1):
                try:
                    self.is_click_tbm(user['业务审核-自检清单-检查结果-选择'], str(i), result)
                except:
                    self.scroll_into_view(user['业务审核-自检清单-检查结果-选择'], str(i), result)
                    self.is_click_tbm(user['业务审核-自检清单-检查结果-选择'], str(i), result)
        else:
            try:
                self.is_click_tbm(user['业务审核-自检清单-指定规则-检查结果-选择'], rule, result)
            except:
                self.scroll_into_view(user['业务审核-自检清单-指定规则-检查结果-选择'], rule, result)
                self.is_click_tbm(user['业务审核-自检清单-指定规则-检查结果-选择'], rule, result)

    @allure.step("产品定义信息-点击确定")
    def click_product_definition_confirm(self):
        self.is_click_tbm(user['产品定义信息确定'])

    @allure.step("产品定义信息-点击编辑")
    def click_product_definition_edit(self, item=None):
        sleep(2)
        if item is None:
            self.is_click_tbm(user['产品定义信息编辑'])
        else:
            self.is_click_tbm(user['指定产品定义信息编辑'], item)

    @allure.step("产品定义信息-点击复制")
    def click_product_definition_copy(self):
        self.is_click_tbm(user['产品定义信息复制'])

    @allure.step("产品定义信息-点击删除")
    def click_product_definition_delete(self):
        self.is_click_tbm(user['产品定义信息删除'])

    @allure.step("出货国家流程新增页面 - 新增产品定义信息")
    def input_product_definition_info(self, header, content):
        """
        出货国家流程新增页面 - 新增产品定义信息
        :param header: 选择要输入的信息
        :param content: 选择信息内容
        """
        definition_dict = ['全球版本', '市场名称', '项目名称', 'MEMORY', 'BAND STRATEGY', '产品经理', '项目经理', 'aaa', 'bbb', '再增', '配色', '尺寸']
        select_list = ['全球版本', 'MEMORY', 'BAND STRATEGY', 'aaa', 'bbb', '再增', '配色', '尺寸']
        input_list = ['市场名称', '项目名称', '摄像头', '型号', '新增', '首单量产时间']
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
            logging.error(f'请输入正确选项：{definition_dict}')
            raise

    @allure.step("输入查询条件")
    def input_search_info(self, type, info):
        """
        :param type: 查询字段
        :param info: 查询内容
        """
        input_type = ['标题', '流程编码', 'BOM编码']
        select_type = ['制作类型', '品牌', '阶段', '市场', '单据状态', '同步状态']
        if type in input_type:
            self.readonly_input_text(user['查询条件'], info, type)
        elif type in select_type:
            self.is_click_tbm(user['查询条件'], type)
            self.is_click_tbm(user['查询选择'], info)
        logging.info('输入框：{}，输入内容：{}'.format(type, info))

    @allure.step("点击查询")
    def click_search(self):
        self.is_click_tbm(user['查询'])
        logging.info('点击查询')
        self.base_get_img('result')

    @allure.step("点击重置")
    def click_reset(self):
        self.is_click_tbm(user['重置'])
        logging.info('点击重置')
        self.base_get_img('result')

    @allure.step("断言：表格内容行数")
    def assert_search_row(self, row):
        search_row = self.elements_num(user['表格内容行'])
        ValueAssert.value_assert_equal(search_row, row)

    @allure.step("断言：查询结果")
    def assert_search_result(self, header, content):
        """
        :param header: 需要断言的字段
        :param content: 需要断言的内容
        """
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格指定列内容'], header, content, sc_element=user['滚动条'])

    @allure.step("获得BOM列表指定内容")
    def get_bom_info(self, menu, info, header, attr='class', index='0'):
        """
        :param menu: 需要进入的BOM协作菜单
        :param info: 输入指定内容查找 如：传入流程编码
        :param header: 需要获取的指定字段
        :param attr: 需要获取的属性 默认class属性
        :param index: 属性索引位置 默认0
        """
        self.click_menu("BOM协作", menu)
        sleep(1)
        column = self.get_table_info(user['表格字段'], header, attr=attr, index=index)
        content = self.element_text(user['BOM列表指定内容'], info, column)
        return content

    @allure.step("获得关键器件流程列表指定内容")
    def get_Device_info(self, info, header, attr='class', index='0'):
        """
        :param info: 输入指定内容查找 如：传入流程编码
        :param header: 需要获取的指定字段
        :param attr: 需要获取的属性 默认class属性
        :param index: 属性索引位置 默认0
        """
        self.click_menu("关键器件", "关键器件流程")
        sleep(1)
        column = self.get_table_info(user['表格字段'], header, attr=attr, index=index)
        content = self.inner_text(user['关键器件列表指定内容'], info, column)
        return content


    @allure.step("新增页面-输入基本信息")
    def input_basic_info(self, header, info):
        """
        :param header: 基本信息字段
        :param info: 输入内容
        """
        input_list = ['标题']
        select_list = ['申请人']
        if header in input_list:
            sleep(2)
            self.input_text(user['基本信息内容'], info, header)
            logging.info('输入Bom信息 {}:{}'.format(header, info))
        elif header in select_list:
            self.is_click_tbm(user['基本信息内容'], header)
            self.input_text(user['产品定义信息成员列表输入框'], info)
            sleep(1)
            self.is_click_tbm(user['成员选择'], info)
            self.is_click_tbm(user['产品定义信息成员确定'])

    @allure.step("点击编辑")
    def click_edit(self, code):
        self.is_click_tbm(user['编辑'], code)
        logging.info('点击编辑')
        sleep(2)

    @allure.step("点击保存")
    def click_add_save(self):
        self.scroll_into_view(user['保存'])
        sleep(0.5)
        self.is_click_tbm(user['保存'])
        logging.info('点击保存')

    @allure.step("点击刷新")
    def click_refresh(self):
        self.scroll_into_view(user['刷新'])
        self.is_click_tbm(user['刷新'])
        logging.info('点击刷新')

    def click_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)

    @allure.step("获取行内容")
    def get_col_content(self, locator):
        info = self.find_elements_tbm(locator)
        infolist = []
        for i in info:
            infolist.append(i.text)
        logging.info('获取结果{}'.format(infolist))
        return infolist

    @allure.step("获取整个元素内容")
    def get_table_content(self, locator):
        info = self.find_elements(locator)
        infolist = []
        for i in info:
            content_list = i.get_attribute('innerText').replace("\t","").split('\n')
            infolist += content_list
        while "" in infolist:
            infolist.remove("")
        logging.info('获取结果{}'.format(infolist))
        return infolist

    @allure.step("断言：出货国家选择全球版本，汇签人员会自动获取人员")
    def assert_version_get_member(self, ver):
        ver_dict = {'版本1': 'ver1', '版本2': 'ver2', '版本3': 'ver3'}
        Employee_list = []
        ServiceDictData = self.API_TBM_ServiceDictData('GLOBAL_VERB')
        for i in ServiceDictData['data'][0]['values']:
            if i['key'] == ver_dict[ver]:
                member_list = i['chValue'].split(',')
                logging.info('获取字典服务汇签人员工号：{}'.format(member_list))
                for j in member_list:
                    Employee_Name = self.API_queryDeptAndEmployee(j)['data'][0]['employeeName']
                    Employee_list.append(Employee_Name)
                logging.info('获取字典服务汇签人员名字：{}'.format(Employee_list))
        self.assert_member('汇签人员', Employee_list)

    @allure.step("断言：出货国家选择全球版本，汇签人员会自动获取人员")
    def assert_member(self, type, member):
        signatory_List = self.element_input_text(user['汇签/抄送人员选择框'], type).split(';')
        try:
            assert set(member) <= set(signatory_List)
            logging.info('断言成功，{}：{} 包含人员：{}'.format(type, signatory_List, member))
        except:
            logging.error('断言失败，{}：{} 不包含人员：{}'.format(type, signatory_List, member))
            raise

    @allure.step("断言变更国家增加已变更产品成功")
    def assert_change_success(self, content):
        ac_content = self.get_table_content(user['产品定义信息内容'])
        try:
            assert content in ac_content
            logging.info('断言成功，结果包含内容')
        except:
            logging.info('断言失败，结果不包含内容')
            raise

    @allure.step("断言产品定义信息复制成功")
    def assert_copy_success(self, content):
        ac_content = self.get_table_content(user['产品定义信息内容'])
        content_num = ac_content.count(content)
        try:
            assert content_num == 2
            logging.info('断言成功，{} 存在{}条数据'.format(content, content_num))
        except:
            logging.info('断言失败，{} 存在{}条数据'.format(content, content_num))
            raise

    @allure.step("点击变更已有产品")
    def click_products(self):
        self.is_click_tbm(user['变更已有产品'])
        logging.info('点击变更已有产品')

    @allure.step("输入已有产品")
    def search_products(self, header, txt):
        self.input_text(user['变更已有产品输入框'], txt, header)
        self.is_click_tbm(user['查询'])

    @allure.step("选择已有产品")
    def select_products(self, name):
        self.is_click_tbm(user['变更已有产品选择'], name)
        logging.info('选择已有产品:{}'.format(name))

    @allure.step("上传文件")
    def upload_file_tbm(self, locator, file):
        file_path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', file)
        logging.info("文件地址：{}".format(file_path))
        self.upload_file(locator, file_path)

    @allure.step("清空汇签/抄送人员")
    def clear_member(self, type):
        self.hover(user['汇签/抄送人员选择框'], type)
        self.is_click_tbm(user['汇签/抄送人员清空'], type)

    @allure.step("创建页面上传附件")
    def add_upload_file(self, name):
        self.upload_file_tbm(user['附件'], name)

    @allure.step("创建页面导入")
    def add_import_file(self, name):
        self.upload_file_tbm(user['导入'], name)

    @allure.step("断言：导入成功状态")
    def assert_import_success(self):
        DomAssert(self.driver).assert_control(user['导入成功状态'])

    @allure.step("断言：导入失败状态")
    def assert_import_fail(self):
        DomAssert(self.driver).assert_control(user['导入失败状态'])

    @allure.step("删除上传附件")
    def delete_upload_file(self, name):
        self.hover(user['指定附件'], name)
        self.is_click_tbm(user['附件删除'], name)
        sleep(2)

    @allure.step("断言：是否存在指定附件")
    def assert_upload(self, name, result=True):
        DomAssert(self.driver).assert_control(user['指定附件'], name, result=result)

    @allure.step("断言：判断是否存在批量删除")
    def assert_batch_delete(self, result):
        DomAssert(self.driver).assert_control(user['批量删除'], result=result)

    @allure.step("点击批量删除")
    def click_batch_delete(self):
        self.is_click_tbm(user['批量删除'])
        logging.info('点击批量删除')

    @allure.step("点击确定")
    def click_batch_confirm(self):
        self.is_click_tbm(user['确定'])
        logging.info('确定')
        sleep(0.5)

    @allure.step("断言导入错误内容后，页面状态是否正确")
    def assert_wrongcontent_upload_result(self):
        try:
            apply = self.find_element(user['导入应用状态'])
            check = self.find_element(user['导入导出校验状态'])
            assert 'is-disabled' in apply.get_attribute('class')
            assert 'is-disabled' not in check.get_attribute('class')
            logging.info('断言成功，导出校验可点击，应用不可点击')
        except:
            self.base_get_img()
            logging.error('断言失败，请检查按钮状态')
            raise

    @allure.step("点击应用")
    def click_apply(self):
        for i in range(10):
            apply = self.find_element(user['导入应用状态'])
            if 'is-disabled' not in apply.get_attribute('class'):
                self.is_click_tbm(user['应用'])
                logging.info('点击应用')
                break
            else:
                sleep(1)

    @allure.step("点击展开+图标")
    def click_tree(self, tree):
        """
        点击展开+图标
        :param tree: 物料名称
        """
        self.is_click_tbm(user['展开'], tree)
        logging.info('点击展开')

    @allure.step("新增物料对焦")
    def material_focus(self, tree):
        """
        新增物料后，根据上级物料 点击新增加的物料列进行对焦
        """
        self.is_click_tbm(user['BOMTree物料对焦'], tree)

    @allure.step("点击新增物料")
    def click_add_material(self):
        self.is_click_tbm(user['新增物料'])
        logging.info('点击新增物料')

    @allure.step("点击一键填写")
    def click_one_press(self):
        self.is_click_tbm(user['一键填写'])
        logging.info('点击一键填写')

    @allure.step("点击一键填写-确定")
    def click_OnePress_confirm(self):
        self.is_click_tbm(user['一键填写确定'])
        sleep(0.5)
        logging.info('点击一键填写确定')

    @allure.step("点击一键填写-取消")
    def click_OnePress_cancel(self):
        self.is_click_tbm(user['一键填写取消'])
        sleep(0.5)
        logging.info('点击一键填写取消')

    @allure.step("BOM信息一键填写")
    def input_OnePress(self, key, value):
        """
        一键填写-根据key选择字段名称，根据value输入字段值
        @param key:字段名称
        @param value:字段值
        """
        self.click_one_press()
        self.is_click_tbm(user['一键填写-字段名称'])
        self.is_click_tbm(user['一键填写-字段名称选择'], key)
        if value == '':
            self.find_element(user['一键填写-字段值']).send_keys(Keys.CONTROL + 'a')
            self.find_element(user['一键填写-字段值']).send_keys(Keys.BACKSPACE)
        else:
            self.input_text(user['一键填写-字段值'], value)
        self.click_OnePress_confirm()

    @allure.step("关键器件-输入一键填写内容")
    def input_KeyDevice_OnePress(self, field, name):
        """
        oneworks-节点：维护关键器件-查看详情页面
        输入一键填写内容
        """
        self.is_click_tbm(user['一键填写-字段名称'])
        self.is_click_tbm(user['一键填写-字段名称选择'], field)
        self.is_click_tbm(user['一键填写-字段值'])
        self.input_text(user['成员列表输入框'], name)
        sleep(1)
        self.is_click_tbm(user['成员选择'], name)
        self.is_click_tbm(user['成员确定'])

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

    @allure.step("点击新增bom")
    def click_add_bomtree(self):
        self.is_click_tbm(user['新增BomTree'])
        logging.info('点击新增Bom')
        sleep(0.5)

    @allure.step("断言：存在新增bom按钮")
    def assert_add_bomtree_exist(self, result):
        """点击新增bom"""
        DomAssert(self.driver).assert_control(user['新增BomTree'], result=result)

    @allure.step("根据Tree点击删除按钮")
    def click_bomtree_delete(self, tree, type=None):
        """
        BOM Tree根据 物料编码 点击删除按钮
        @param tree:物料编码，传入BomTree的物料名称
        @param type:如果第一个参数是物料编码， 需要给参数type传 code
        """
        if type == 'code':
            self.is_click_tbm(user['BOMTree删除'], tree)
        else:
            self.is_click_tbm(user['BOMTree指定Tree删除'], tree)

    def get_bomtree_tree_info(self):
        """
        获取BOMTree所有内容
        """
        info = self.find_elements(user['BomTree全部内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取BOMTree所有内容{}'.format(infolist))
        return infolist

    @allure.step("断言导入BOM-导入后，页面表格内容是否正确")
    def assert_tree_result(self, *content):
        """
        断言导入BOM-导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_bomtree_tree_info()
            content_list = []
            for i in contents:
                content_list.append(tuple(i))
            assert set(content) <= set(content_list)
            logging.info(content_list)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            self.base_get_img()
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("点击导入BOM按钮")
    def click_bom_import(self):
        self.is_click_tbm(user['导入BOM'])
        logging.info('点击导入BOM')

    @allure.step("获取导入BOM-结果内容")
    def get_bomtree_upload_info(self):
        info = self.find_elements_tbm(user['导入BOM内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取BOM导入结果{}'.format(infolist))
        return infolist

    @allure.step("断言导入后，页面表格内容是否正确")
    def assert_upload_result(self, *content):
        """
        断言导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_bomtree_upload_info()
            content_list = []
            for i in contents:
                content_list.append(tuple(i))
            logging.info(content_list)
            assert set(content) <= set(content_list)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            self.base_get_img()
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("点击BOM Tree复选框")
    def click_BOMTree_checkbox(self, code='all', type=None):
        """
        BOM Tree根据 物料编码 点击指定复选框，默认全选
        @param code:物料名/Tree，传入BomTree的物料名称；默认‘all’表示点击全选复选框
        @param type:如果是Tree， 需要给参数type传 Tree
        """
        DomAssert(self.driver).assert_control(user['BomTreeTitle'])
        if code == 'all':
            self.is_click_tbm(user['BomTree复选框全选'])
        else:
            if type == 'Tree':
                self.is_click_tbm(user['BomTree复选框Tree单选'], code)
            else:
                self.is_click_tbm(user['BomTree复选框单选'], code)
        logging.info('点击BOM Tree复选框')

    @allure.step("点击生产工厂信息复选框")
    def click_Factory_checkbox(self, code='all'):
        """
        生产工厂信息根据 物料编码 点击指定复选框，默认全选
        @param code:物料名，传入生产工厂信息的物料名称；默认‘all’表示点击全选复选框
        """
        DomAssert(self.driver).assert_control(user['生产工厂信息Title'])
        if code == 'all':
            self.is_click_tbm(user['生产工厂信息复选框全选'])
        else:
            self.is_click_tbm(user['生产工厂信息复选框单选'], code)
        logging.info('点击生产工厂信息复选框')

    @allure.step("点击关键器件复选框")
    def click_Device_checkbox(self, code='all'):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击复选框
        @param code:物料编码，传入物料编码；默认‘all’表示点击全选复选框
        """
        DomAssert(self.driver).assert_control(user['关键器件Title'])
        if code == 'all':
            self.is_click_tbm(user['关键器件复选框全选'])
        else:
            self.is_click_tbm(user['关键器件复选框单选'], code)
        logging.info('点击关键器件复选框')

    @allure.step("断言：审批页面BomTree数据是否一致")
    def assert_oneworks_bomtree_result(self, tree, *content):
        """
        断言：审批页面BomTree数据是否一致
        :param tree: 需要点击Tree展开BomTree表格
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            self.click_tree(tree)
            contents = self.get_bomtree_tree_info()
            content_list = []
            for i in contents:
                content_list.append(tuple(i))
            assert set(content) <= set(content_list)
            logging.info(content_list)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            self.base_get_img()
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("点击衍生BOM制作需求-新增")
    def click_Derived_add(self):
        self.is_click_tbm(user['衍生BOM制作需求-新增'])
        logging.info('点击衍生BOM制作需求-新增')
        sleep(0.5)

    @allure.step("输入衍生BOM制作需求信息")
    def input_Derived_info(self, header, info, serial=1):
        select_list = ['操作']
        input_list = ['用量', '替代组', '份额', '数量', '位号']
        if header in select_list:
            column = self.get_table_info(user['衍生BOM制作需求-操作'])
            self.is_click_tbm(user['衍生BOM制作需求-输入框'], serial, column)
            self.is_click_tbm(user['衍生BOM制作需求-操作选择'], info)
        elif header in input_list:
            column = self.get_table_info(user['衍生BOM制作需求-字段'], header)
            self.input_text(user['衍生BOM制作需求-输入框'], info, serial, column)
        else:
            column = self.get_table_info(user['衍生BOM制作需求-字段'], header)
            self.is_click_tbm(user['衍生BOM制作需求-输入框'], serial, column)
            self.input_text(user['衍生BOM制作需求-输入框'], info, serial, column)
            self.is_click_tbm(user['衍生BOM制作需求-选择'], info)

    @allure.step("删除衍生BOM制作需求信息")
    def delete_Derived_info(self):
        column = self.get_table_info(user['衍生BOM制作需求-操作删除框'])
        self.is_click_tbm(user['衍生BOM制作需求-删除'], column)

    @allure.step("断言：衍生BOM制作需求-暂无数据")
    def assert_Derived_None(self):
        DomAssert(self.driver).assert_control(user['衍生BOM制作需求-暂无数据'])

    @allure.step("断言：生产工厂信息-暂无数据")
    def assert_Factory_None(self):
        DomAssert(self.driver).assert_control(user['生产工厂信息-暂无数据'])

    @allure.step("点击衍生差异")
    def click_Derived_differ(self):
        self.is_click_tbm(user['衍生差异'])
        logging.info('点击衍生差异')
        sleep(0.5)

    @allure.step("点击生成BOM")
    def click_Creat_BOM(self):
        self.is_click_tbm(user['生成BOM'])
        logging.info('点击生成BOM')
        sleep(2)

    @allure.step("点击衍生需求导入")
    def click_Derived_import(self):
        self.is_click_tbm(user['衍生BOM制作需求-导入'])
        logging.info('点击衍生BOM制作需求-导入')

    @allure.step("点击生产工厂信息导入")
    def click_Factory_import(self):
        self.is_click_tbm(user['生产工厂信息-导入'])
        logging.info('点击生产工厂信息-导入')

    @allure.step("关键器件流程-输入评估内容")
    def input_KeyDevice_Evaluation_content(self, node, choice, content):
        """
        oneworks-节点：资源商务评估-查看详情页面
        物料详情-采购评估
        @param node:评估节点
        @param choice:内容
        @param content:参数名称
        """
        input_list = ['供应商选择原因', '份额', 'NUDD说明', 'NUDD管理方案', '原因及修改建议', 'CG颜色', '接口类型', '物料属性', 'L/T(天)',
                      '最小下单量(pcs)', '此项目峰值需求(K/M)', '供应商总产能(K/M)', '分配传音产能(K/M)', '供应弹性(%)', '共用项目需求合计(K/M)',
                      '此项目产能分配(K/M)', '共用项目名', '备料建议']
        select_list = ['供应商名称', '是否新供应商', '国产化属性', '供应商选择原因类别', '是否客供物料', '价格趋势（6个月）', '是否NUDD',
                       '评审结论', '技术类型', '连接方式', '产能评审结论', '认证状态']
        if choice in input_list:
            if node == '标准化评估':
                self.readonly_input_text(user['标准化评估文本框'], content, choice)
            elif node == '参数':
                self.readonly_input_text(user['参数输入框'], content, choice)
            else:
                self.readonly_input_text(user['关键器件评估输入框'], content, node, choice)
        elif choice in select_list:
            if node == '标准化评估':
                self.is_click_tbm(user['标准化评估输入框'], choice)
            elif node == '参数':
                self.is_click_tbm(user['参数输入框'], choice)
            else:
                self.is_click_tbm(user['关键器件评估输入框'], node, choice)
            self.is_click_tbm(user['关键器件评估输入框选择'], content)
        else:
            logging.error('请输入正确的字段')
            raise ValueError('请输入正确的字段')

    @allure.step("点击指定关键器件左侧三角按钮展开")
    def click_Device_unfold(self, key):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击指定关键器件左侧三角按钮展开
        @param key:关键器件
        """
        self.is_click_tbm(user['维护关键器件-物料模块-展开'], key)


    @allure.step("维护关键器件-点击指定物料模块")
    def click_Device_module(self, module):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击指定物料模块
        @param module:物料模块
        """
        self.is_click_tbm(user['维护关键器件-物料模块'], module)

    @allure.step("维护关键器件-点击物料编码右侧的加号")
    def click_Device_code_add(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击物料编码右侧的加号
        """
        self.is_click_tbm(user['维护关键器件-物料模块-物料编码加号'])

    @allure.step("维护关键器件-鼠标悬停在物料右侧，点击加号")
    def click_Device_material_add(self, code):
        """
        oneworks-节点：维护关键器件-查看详情页面
        鼠标悬停在物料右侧，点击加号
        @param code:物料模块
        """
        self.hover(user['维护关键器件-物料模块-物料编码按钮组'], code)
        self.is_click_tbm(user['维护关键器件-物料模块-物料编码按钮组-加号'], code)

    @allure.step("维护关键器件-点击待申请编码，打开物料详情（参数）")
    def click_Device_pending_code(self, code):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击待申请编码，打开物料详情（参数）
        @param code:待申请编码
        """
        self.is_click_tbm(user['维护关键器件-物料模块-物料编码-待申请编码'], code)

    @allure.step("维护关键器件-物料详情-滚动显示")
    def scroll_Device_material_details(self, param):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-滚动显示
        """
        self.scroll_into_view(user['维护关键器件-物料模块-物料编码-物料详情'], param)

if __name__ == '__main__':
    pass
