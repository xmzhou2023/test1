import logging

from libs.common.read_element import Element
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)


class CenterComponent(Base, APIRequest):
    """用户类"""

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
    def enter_oneworks_edit(self, code, node=None):
        """
        点击 查看详情 进入 oneworks 页面
        输入流程编码过滤后，根据当前节点名称点击查看详情进入详情页面
        @param code:流程编码
        @param node:节点名称
        """
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
            self.is_click_tbm(user['oneworks-撤回确定'])
        except:
            self.base_get_img()
            self.refresh()
            self.is_click_tbm(user['oneworks-撤回'])
            self.is_click_tbm(user['oneworks-撤回确定'])
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

    @allure.step("oneworks点击同意")
    def click_oneworks_agree(self):
        self.frame_exit()
        self.is_click_tbm(user['oneworks-同意'])
        logging.info('点击同意')

    @allure.step("oneworks点击确定")
    def click_oneworks_confirm(self):
        self.is_click_tbm(user['同意确定'])
        logging.info('点击确定')

    @allure.step("oneworks点击取消")
    def click_oneworks_cancel(self):
        self.is_click_tbm(user['同意取消'])
        logging.info('点击取消')

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
    def assert_oneworks_rollback_refer(self, result):
        DomAssert(self.driver).assert_control(user['oneworks-转交'], result=result)

    @allure.step("点击拒绝")
    def click_oneworks_refuse(self):
        self.frame_exit()
        self.is_click_tbm(user['oneworks-拒绝'])
        logging.info('点击拒绝')
        self.is_click_tbm(user['oneworks-拒绝-确定'])
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
        self.base_get_img()
        DomAssert(self.driver).assert_att('基本信息')

    @allure.step("断言：区域配置数据按照时间降序排序")
    def assert_search_time_desc(self):
        times = self.find_elements(user['创建时间'])
        timelist = []
        for i in times:
            timelist.append(i.text)
        try:
            for i in range(len(timelist) - 1):
                try:
                    assert timelist[i] >= timelist[i + 1]
                except:
                    logging.error('未按降序排序,修改时间分别为：{}，{}'.format(timelist[i], timelist[i + 1]))
                    raise
            logging.info('查询按照按修改时间的降序排序')
        except Exception as e:
            logging.error(e)
            raise

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
        self.frame_enter(user['待办列表-我申请的-iframe'])
        sleep(2)
        DomAssert(self.driver).assert_att('基本信息')

    @allure.step("获取oneworks页面的Bom信息")
    def get_onework_bominfo(self, select):
        """
        获取oneworks页面的Bom信息
        @param select:需要获取的信息类型： 制作类型， 品牌， 机型， 阶段， 市场， 模板， 自研/外研
        """
        self.scroll_into_view(user['BOM工程师-BomTree'])
        DomAssert(self.driver).assert_control(user['BOM工程师-BomTreeTitle'])
        if select == '机型':
            BomInfo = self.element_text(user['OneworksBom信息-机型'])
            logging.info('获取Bom信息：{}'.format(BomInfo))
            return BomInfo
        BomInfo = self.element_input_text(user['BOM信息输入框'], select)
        logging.info('获取Bom信息：{}'.format(BomInfo))
        return BomInfo

    @allure.step("获取BOMTree所有内容")
    def get_oneworks_bomtree_info(self):
        info = self.find_elements_tbm(user['OneworksBomTree全部内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取Oneworks-BOMTree所有内容{}'.format(infolist))
        return infolist

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
            print('请输入’贴片工厂不正确‘ 或者 ’贴片工厂正确‘')

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

    @allure.step("补充工厂页面 根据material点击指定复选框")
    def click_oneworks_checkbox(self, code='all'):
        """
        补充工厂页面 根据material点击指定复选框，默认全选
        @param code:物料编码，传入物料编码；默认‘all’表示点击全选复选框
        """
        DomAssert(self.driver).assert_control(user['生产工厂信息Title'])
        if code == 'all':
            self.is_click_tbm(user['生产工厂信息复选框全选'])
        else:
            self.is_click_tbm(user['生产工厂信息复选框单选'], code)
        logging.info('点击复选框')

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
                    self.input_text(user['成员列表输入框'], audit)
                    sleep(1)
                    self.is_click_tbm(user['成员选择'], audit)
                    self.is_click_tbm(user['成员确定'])
                self.base_get_img()
                logging.info('获取审核人名单:{}'.format(infolist))
        else:
            self.is_click_tbm(user['审核人类别'], type)
            self.input_text(user['成员列表输入框'], audit)
            sleep(1)
            self.is_click_tbm(user['成员选择'], audit)
            self.is_click_tbm(user['成员确定'])
            self.base_get_img()
        logging.info('审核人填写:字段：{}， 审核人：{}'.format(type, audit))

    @allure.step("断言：在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")
    def assert_oneworks_bomtree_edit(self, tree, header):
        """
        在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑
        """
        column_class = self.get_table_info(user['编辑验证表头'], header)
        self.mouse_double_click(user['编辑验证'], tree, column_class)
        sleep(0.5)
        DomAssert(self.driver).assert_control(user['编辑验证'], tree, column_class)

    @allure.step("业务审核页面 点击 自检清单")
    def click_oneworks_businessapprove_self_inspection(self, box, option):
        """
        业务审核页面 点击 自检清单
        @param box:输入框
        @param option:选项
        """
        self.is_click_tbm(user['业务审核-自检清单-业务类型'], box)
        self.is_click_tbm(user['业务审核-自检清单-检查角色'], option)

    @allure.step("业务审核页面 滑动到 自检清单")
    def scroll_oneworks_businessapprove_self_inspection(self):
        self.scroll_into_view(user['业务审核-自检清单'])

    @allure.step("业务审核页面 自检清单 点击输入检查结果")
    def input_oneworks_businessapprove_inspection_result(self, rule='all', result='通过'):
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

    @allure.step("产品定义信息-点击确定")
    def click_product_definition_edit(self):
        sleep(2)
        self.is_click_tbm(user['产品定义信息编辑'])

    @allure.step("出货国家流程新增页面 - 新增产品定义信息")
    def input_product_definition_info(self, header, content):
        """
        出货国家流程新增页面 - 新增产品定义信息
        :param header: 选择要输入的信息
        :param content: 选择信息内容
        """
        definition_dict = ['全球版本', '市场名称', '项目名称', 'MEMORY', 'BAND STRATEGY', '产品经理', '项目经理', 'aaa', 'bbb', '再增', '配色', '尺寸']
        select_list = ['全球版本', 'MEMORY', 'BAND STRATEGY', 'aaa', 'bbb', '再增', '配色', '尺寸']
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

    def click_delete_confirm(self):
        self.is_click_tbm(user['同意确定'])
        logging.info('点击确定')

    def click_delete_cancel(self):
        self.is_click_tbm(user['同意取消'])
        logging.info('点击取消')


if __name__ == '__main__':
    pass
