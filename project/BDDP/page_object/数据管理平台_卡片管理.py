import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


# ---卡片管理----

class kapianguanli(Base):
    """用户类"""

    @allure.step("查找工号")
    def search_user(self, jobnum=None, name=None):
        if jobnum is not None:
            self.readonly_input_text(user['用户管理-工号输入框'], txt=jobnum)
            sleep(2)
            self.is_click(user['用户管理-工号下拉列表'], jobnum)
        if name is not None:
            self.readonly_input_text(user['用户管理-姓名输入框'], txt=name)
            sleep(2)
            self.is_click(user['用户管理-姓名下拉列表'], name)
        self.is_click(user['用户管理-查询'])
        sleep()

    @allure.step("查找工号")
    def click_primary(self):
        self.is_click_tbm(user['主题域'])

    @allure.step("点击卡片名称")
    def click_card(self):
        self.is_click_tbm(user['卡片名称'])

    @allure.step("断言输入框内容")
    def assert_input(self, header, content):
        if header == '主题域' or header == '业务组织':
            ac_content = self.element_text(user['输入框内容2'], header)
            ValueAssert.value_assert_equal(ac_content, content)
        elif header == '新建说明':
            ac_content = self.element_input_text(user['输入框内容3'], header)
            ValueAssert.value_assert_equal(ac_content, content)
        elif header == '英文属性说明':
            ac_content = self.element_input_text(user['输入框内容4'], header)
            ValueAssert.value_assert_equal(ac_content, content)
        else:
            ac_content = self.element_input_text(user['输入框内容'], header)
            ValueAssert.value_assert_equal(ac_content, content)

    @allure.step("点击菜单")
    def click_menu(self, menu):
        self.is_click_tbm(user['菜单'], menu)

    @allure.step("点击新建")
    def click_add(self, ):
        self.is_click_tbm(user['新建'])

    @allure.step("点击新建")
    def input_content(self, header, content):
        textarea_list = ['说明']
        fuzzySelect_list = ['需求提出人', '业务负责人', 'IT负责人', 'Supplier']
        exactSelect_list = ['应用类型', '卡片名称']
        exactSelect_list1 = ['报表名称']
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in textarea_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框3'], content, header)
            elif header in exactSelect_list:
                self.is_click_tbm(user['输入框内容'], header)
                self.readonly_input_text(user['输入框内容'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in fuzzySelect_list:
                self.is_click_tbm(user['输入框内容'], header)
                self.input_text(user['输入框内容'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
            elif header in exactSelect_list1:
                self.is_click_tbm(user['输入框内容'], header)
                self.input_text(user['输入框内容'], content, header)
            else:
                logging.error('请输入正确的查询条件')
                raise ValueError('请输入正确的查询条件')

    @allure.step("主题域")
    def click_theme(self):
        self.is_click(user['主题域'])

    @allure.step("营销")
    def click_theme1(self):
        self.is_click(user['营销'])

    @allure.step("经营分析")
    def click_theme2(self):
        self.is_click(user['经营分析'])

    @allure.step("业务组织")
    def click_group(self):
        self.is_click(user['业务组织'])

    @allure.step("深圳传音控股")
    def click_group1(self):
        self.is_click(user['深圳传音控股'])

    @allure.step("是否公开")
    def click_open(self):
        self.is_click(user['是否公开'])

    @allure.step("有首页卡片池")
    def click_homepage(self):
        self.is_click(user['有首页卡片池'])

    @allure.step("下钻报表")
    def click_report(self):
        self.is_click(user['下钻报表'])

    @allure.step("销售月报")
    def click_report1(self):
        self.is_click(user['销售月报'])

    @allure.step("报表2")
    def click_report01(self):
        self.is_click(user['报表2'])

    @allure.step("确定报表")
    def click_report2(self):
        self.is_click(user['确定报表'])

    @allure.step("卡片组件")
    def click_card(self):
        self.is_click(user['卡片组件'])

    @allure.step("分享")
    def click_share(self):
        self.is_click(user['分享'])

    @allure.step("分析指标")
    def click_targer(self):
        self.is_click(user['分析指标'])

    @allure.step("选择分析指标")
    def click_targer1(self):
        self.is_click(user['选择分析指标'])

    @allure.step("选择分析指标1")
    def click_targer2(self):
        self.is_click(user['选择分析指标1'])

    @allure.step("指标确定")
    def click_targersure(self):
        self.is_click(user['指标确定'])

    @allure.step("说明")
    def click_explain(self):
        self.is_click(user['说明'])

    @allure.step("说明")
    def click_explain1(self):
        self.input_text(user['输入说明'], '销售情况')

    @allure.step("配置卡片名称")
    def click_card_explain(self):
        self.is_click(user['配置卡片名称'])

    @allure.step("配置卡片名称1")
    def click_card_explain01(self):
        self.is_click(user['配置卡片名称1'])

    @allure.step("输入卡片名称")
    def click_card_explain1(self):
        self.input_text(user['输入卡片名称'], 'test')

    @allure.step("输入卡片名称1")
    def click_card_explain01(self):
        self.input_text(user['输入卡片名称1'], 'test')

    @allure.step("名称说明")
    def click_card_name(self):
        self.is_click(user['名称说明'])

    @allure.step("名称说明")
    def click_card_name1(self):
        self.input_text(user['输入名称说明'], 'test')

    @allure.step("新建确定")
    def click_created(self):
        self.is_click(user['新建确定'])

    @allure.step("编辑")
    def click_editor(self):
        self.is_click(user['编辑'])

    @allure.step("保存编辑")
    def click_save_editor(self):
        self.is_click(user['保存编辑'])

    @allure.step("查看")
    def click_check(self):
        self.is_click(user['查看'])

    @allure.step("退出查看")
    def click_check_quit(self):
        self.is_click(user['退出查看'])

    @allure.step("启用")
    def click_start(self):
        self.is_click(user['启用'])

    @allure.step("确定启用")
    def click_start1(self):
        self.is_click(user['确定启用'])

    @allure.step("停用")
    def click_stop(self):
        self.is_click(user['停用'])

    @allure.step("确定停用")
    def click_stop1(self):
        self.is_click(user['确定停用'])

    @allure.step("删除卡片")
    def click_delete(self):
        self.is_click(user['删除卡片'])

    @allure.step("确定删除")
    def click_yes(self):
        self.is_click(user['确定删除'])

    @allure.step("全部")
    def click_all_code(self):
        self.is_click(user['全部'])

    @allure.step("已启用")
    def click_initiate_code(self):
        self.is_click(user['已启用'])

    @allure.step("已停用")
    def click_stop_code(self):
        self.is_click(user['已停用'])

    @allure.step("卡片类型搜索")
    def click_card_code_search(self):
        self.is_click(user['卡片类型搜索'])

    @allure.step("pc端")
    def click_card_code_search1(self):
        self.is_click(user['pc端'])

    @allure.step("重置")
    def click_reset(self):
        self.is_click(user['重置'])

    @allure.step("类型输入")
    def click_input_code(self):
        self.is_click(user['类型输入'])

    @allure.step("移动端")
    def click_input_code1(self):
        self.input_text(user['输入卡片类型'], '移动端')

    @allure.step("查询")
    def click_search(self):
        self.is_click(user['查询'])

    @allure.step("初始化1")
    def click_close_card(self):
        self.is_click(user['关闭卡片管理'])

    @allure.step("初始化3")
    def click_close(self):
        self.is_click(user['关闭维度管理'])

    # ----角色管理----------------------------------------------------

    @allure.step("点击系统管理")
    def click_system(self):
        self.is_click(user['点击系统管理'])

    @allure.step("点击角色管理")
    def click_role(self):
        self.is_click(user['点击角色管理'])

    @allure.step("角色名称")
    def click_rolename(self):
        self.input_text(user['角色名称'], 'SMR001')

    @allure.step("角色说明")
    def click_describe(self):
        self.input_text(user['角色说明'], '经理')

    @allure.step("菜单报表授权")
    def click_menubar(self):
        self.is_click(user['菜单报表授权'])

    @allure.step("授权报表")
    def click_menubar1(self):
        self.is_click(user['授权报表'])

    @allure.step("保存报表")
    def click_savereport(self):
        self.is_click(user['保存报表'])

    @allure.step("关联用户")
    def click_user(self):
        self.is_click(user['关联用户'])

    @allure.step("关联用户1")
    def click_user01(self):
        self.is_click(user['关联用户1'])

    @allure.step("输入用户")
    def click_user1(self):
        self.input_text(user['输入用户'], '18653759')

    @allure.step("增加用户")
    def click_user02(self):
        self.input_text(user['增加用户'], '18646861')

    @allure.step("授权用户")
    def click_user2(self):
        self.is_click(user['授权用户'])

    @allure.step("确定授权")
    def click_user3(self):
        self.is_click(user['确定授权'])

    @allure.step("授权首页")
    def click_home_card(self):
        self.is_click(user['授权首页'])

    @allure.step("选择")
    def click_home_card1(self):
        self.is_click(user['选择'])

    @allure.step("选择卡片")
    def click_select(self):
        self.is_click(user['选择卡片'])

    @allure.step("保存授权")
    def click_home_card2(self):
        self.is_click(user['保存授权'])

    @allure.step("粘贴工号")
    def click_paste(self):
        self.is_click(user['粘贴工号'])

    @allure.step("粘贴")
    def click_paste1(self):
        self.input_text(user['粘贴'], '18601002,18649492,18653759,18645046,18647281')

    @allure.step("确定粘贴")
    def click_paste2(self):
        self.is_click(user['确定粘贴'])

    @allure.step("保存")
    def click_save(self):
        self.is_click(user['保存'])

    @allure.step("编辑角色")
    def click_edit_role(self):
        self.is_click(user['编辑角色'])

    @allure.step("搜索角色")
    def click_search_role(self):
        self.input_text(user['搜索角色'], '移动端')

    @allure.step("查询角色")
    def click_search_role1(self):
        self.is_click(user['查询角色'])

    @allure.step("角色初始化")
    def click_rolereset(self):
        self.is_click(user['角色初始化'])

    @allure.step("删除角色")
    def click_deleterole(self):
        self.is_click(user['删除角色'])

    @allure.step("关闭角色")
    def click_close_role(self):
        self.is_click(user['关闭角色'])

    @allure.step("关闭维度")
    def click_close_tables(self):
        self.is_click(user['关闭维度'])

    # -------报表管理 ---------------------------------------------

    @allure.step("报表管理")
    def click_menu1(self):
        self.is_click(user['报表管理'])

    @allure.step("我的报表")
    def click_menu2(self):
        self.is_click(user['我的报表'])

    @allure.step("卡片来源")
    def click_card_source(self):
        self.is_click(user['卡片来源'])

    @allure.step("移动驾驶舱测试1")
    def click_card_source1(self):
        self.is_click(user['移动驾驶舱测试1'])

    @allure.step("确定卡片")
    def click_card_source2(self):
        self.is_click(user['确定卡片'])

    @allure.step("选择指标")
    def click_tg(self):
        self.is_click(user['选择指标'])

    @allure.step("昨日激活SO")
    def click_tg1(self):
        self.is_click(user['昨日激活SO'])

    @allure.step("报表指标确定")
    def click_tg2(self):
        self.is_click(user['报表指标确定'])

    @allure.step("报表名称1")
    def click_report_name1(self):
        self.input_text(user['报表名称1'], 'test')

    @allure.step("报表说明")
    def click_report_name2(self):
        self.input_text(user['报表说明'], 'test')

    @allure.step("保存报表1")
    def click_save_reprot(self):
        self.is_click(user['保存报表1'])




if __name__ == '__main__':
    pass
