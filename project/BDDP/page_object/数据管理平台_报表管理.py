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

class baobiaoguanli(Base):
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
        fuzzySelect_list1 = ['主题域', 'Supplier']
        fuzzySelect_list2 = ['业务组织', 'Supplier']
        exactSelect_list = ['应用类型', '卡片名称']
        exactSelect_list1 = ['报表名称']
        exactSelect_list2 = ['报表类型']
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in textarea_list:
                self.is_click_tbm(user['输入框内容'], header)
                self.input_text(user['输入框内容'], content, header)
            elif header in exactSelect_list:
                self.is_click_tbm(user['输入框内容'], header)
                self.readonly_input_text(user['输入框内容'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in fuzzySelect_list:
                self.is_click_tbm(user['输入框内容'], header)
                self.input_text(user['输入框内容'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
            elif header in fuzzySelect_list1:
                self.is_click_tbm(user['输入框内容'], header)
                self.input_text(user['输入框内容'], content, header)
                self.is_click(user['经营分析'])
            elif header in fuzzySelect_list2:
                self.is_click_tbm(user['输入框内容'], header)
                self.input_text(user['输入框内容'], content, header)
                self.is_click(user['深圳传音控股'])
            elif header in exactSelect_list1:
                self.is_click_tbm(user['输入框内容'], header)
                self.input_text(user['输入框内容'], content, header)
            elif header in exactSelect_list2:
                self.is_click_tbm(user['输入框内容'], header)
                self.readonly_input_text(user['输入框内容'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            else:
                logging.error('请输入正确的查询条件')
                raise ValueError('请输入正确的查询条件')
        # -------报表管理 ---------------------------------------------

    @allure.step("报表管理")
    def click_menu1(self):
        self.is_click(user['报表管理'])

    @allure.step("我的报表")
    def click_menu2(self):
        self.is_click(user['我的报表'])

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

    @allure.step("首页差异化")
    def click_home(self):
        self.is_click(user['首页差异化'])

    @allure.step("报表类型选择")
    def click_home1(self):
        self.is_click(user['报表类型选择'])

    @allure.step("地区部")
    def click_CE(self):
        self.is_click(user['地区部'])


    @allure.step("事业部")
    def click_BU(self):
        self.is_click(user['事业部'])


    @allure.step("卡片来源")
    def click_card_source(self):
        self.is_click(user['卡片来源'])

    @allure.step("移动驾驶舱测试1")
    def click_card_source1(self):
        self.is_click(user['移动驾驶舱测试1'])

    @allure.step("确定卡片")
    def click_card_source2(self):
        self.is_click(user['确定卡片'])

    @allure.step("外部引入")
    def click_external(self):
        self.is_click(user['外部引入'])

    @allure.step("定制化")
    def click_customized(self):
        self.is_click(user['定制化'])

    @allure.step("访问地址")
    def click_address(self):
        self.input_text(user['访问地址'], 'https://cockpitnew.transsion.com/dip/')

    @allure.step("访问地址1")
    def click_address1(self):
        self.input_text(user['访问地址1'], 'https://cockpitnew.transsion.com/dip/')

    @allure.step("选择指标")
    def click_tg(self):
        self.is_click(user['选择指标'])

    @allure.step("昨日激活SO")
    def click_tg1(self):
        self.is_click(user['昨日激活SO'])

    @allure.step("报表指标确定")
    def click_tg2(self):
        self.is_click(user['报表指标确定'])

    @allure.step("说明")
    def click_explain1(self, content):
        self.input_text(user['说明'], content)

    @allure.step("报表名称1")
    def click_report_name1(self, content):
        self.input_text(user['报表名称1'], content)

    @allure.step("报表名称2")
    def click_report_name01(self, content):
        self.input_text(user['报表名称2'], content)

    @allure.step("报表名称3")
    def click_report_name02(self, content):
        self.input_text(user['报表名称3'], content)

    @allure.step("报表名称4")
    def click_report_name03(self, content):
        self.input_text(user['报表名称4'], content)

    @allure.step("报表说明")
    def click_report_name2(self, content):
        self.input_text(user['报表说明'], content)

    @allure.step("保存报表1")
    def click_save_reprot(self):
        self.is_click(user['保存报表1'])

    @allure.step("编辑")
    def click_edit(self):
        self.is_click(user['编辑'])

    @allure.step("启用")
    def click_start(self):
        self.is_click(user['启用'])

    @allure.step("停用")
    def click_stop(self):
        self.is_click(user['停用'])

    @allure.step("保存")
    def click_save(self):
        self.is_click(user['保存'])

    @allure.step("类型搜索")
    def click_code_search(self):
        self.is_click(user['类型搜索'])

    @allure.step("移动端")
    def click_code_search1(self):
        self.is_click(user['移动端'])

    @allure.step("重置")
    def click_reset(self):
        self.is_click(user['重置'])


    @allure.step("移动端")
    def click_input_code(self):
        self.input_text(user['输入类型'], '移动端')

    @allure.step("查询")
    def click_search(self):
        self.is_click(user['查询'])


    @allure.step("删除卡片")
    def click_delete(self):
        self.is_click(user['删除卡片'])

    @allure.step("确定删除")
    def click_yes(self):
        self.is_click(user['确定删除'])

    @allure.step("初始化1")
    def click_close_report(self):
        self.is_click(user['关闭报表管理'])

    @allure.step("初始化3")
    def click_close(self):
        self.is_click(user['关闭维度管理'])


if __name__ == '__main__':
    pass
