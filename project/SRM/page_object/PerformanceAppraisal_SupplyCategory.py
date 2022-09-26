import time

import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
app = Element(pro_name, object_name)




class Performance(Base):
    """供应商绩效类"""
    @allure.step("进入供应商绩效考核")
    def PerformanceAppraisal(self):
        self.is_click(app['供应商绩效'])
        # self.frame_enter(app["供应商绩效iframe"])


    def appraisal_page_title(self):
        return self.find_element(app["供应商绩效标题"]).text


    @allure.step("最小化供应商绩效考核窗口")
    def MinWindows(self):
        self.frame_exit()
        self.is_click(app["供应商绩效考核--窗口最小化"])

    def close_valuecode_page(self):
        self.hover(app["评估代码供货品类配置-页面窗口标题"])
        self.hover_click(app["评估代码供货品类配置-关闭页面"])


    def enter_SupplyCategory(self):
        self.frame_enter(app["供应商绩效iframe"])
        self.is_click(app["供应商绩效-评估代码供货品类配置"])

    def title_SupplyCategory(self):
        return self.find_element(app["评估代码供货品类配置页面标题"]).text

    def creat_SupplyCategory(self):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-新建"])

    def get_title_creat(self):
        return self.find_element(app["评估代码供货品类配置-新建弹窗标题"]).text

    def creat_SupplyCategory_close(self):
        # self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        # self.is_click(app["评估代码供货品类配置-新建"])
        # time.sleep(2)
        self.is_click(app["评估代码供货品类配置-新建弹窗-关闭"])
        self.frame_back()

    def creat_SupplyCategory_cancel(self):
        # self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        # self.is_click(app["评估代码供货品类配置-新建"])
        self.is_click(app["评估代码供货品类配置-新建-取消"])
        self.frame_back()

    def creat_select_code(self,code):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-新建"])
        self.input_text(app['评估代码供货品类配置-新建-评估代码'],txt=code)

    def creat_select_material(self):
        self.is_click(app['评估代码供货品类配置-新建-小类搜索'])
        self.frame_back()
        self.frame_enter(app["评估代码供货品类配置-新建-小类iframe"])
        self.is_click(app['评估代码供货品类配置-新建-小类选择'])
        self.is_click(app['评估代码供货品类配置-新建-小类-确定'])
        self.frame_back()

    def creat_select_rule(self):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app['评估代码供货品类配置-新建-评分规则'])
        self.frame_back()
        self.frame_enter(app["评估代码供货品类配置-新建-评分规则iframe"])
        self.is_click(app["评估代码供货品类配置-新建-评分规则-选择"])
        self.is_click(app["评估代码供货品类配置-新建-评分规则-确定"])

    def creat_SelectOK(self):
        self.frame_back()
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-新建-确定"])
        self.frame_back()
        self.is_click(app["评估代码供货品类配置-新建-确定-保存确定"])

    def create_fail_blank(self):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-新建"])
        self.is_click(app["评估代码供货品类配置-新建-确定"])
        self.frame_back()
        # self.is_click(app["评估代码供货品类配置-关闭新建失败提示"])
        # self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        # self.is_click(app["评估代码供货品类配置-新建弹窗-关闭"])
        # self.frame_back()

    def create_fail_prompt(self):
        return self.find_element(app["评估代码供货品类配置-新建失败提示"]).text

    def close_fail(self):
        self.is_click(app["评估代码供货品类配置-关闭新建失败提示"])
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-新建弹窗-关闭"])
        self.frame_back()




    @allure.step("获取新建成功弹窗提示内容")
    def get_alert_text(self):
        # 获取弹窗内容，srm使用
        return self.find_element(app["评估代码供货品类配置-新建-操作成功提示"]).text

    @allure.step("关闭新建成功弹窗提示")
    def close_alert(self):
        self.is_click(app["评估代码供货品类配置-新建-操作成功提示关闭"])


    @allure.step("通过评估代码查询")
    def search_code(self, code):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.input_text(app["评估代码供货品类配置-评估代码查询输入框"], code)
        self.is_click(app["评估代码供货品类配置-查询"])
        self.clear_input(app["评估代码供货品类配置-评估代码查询输入框"])
        self.frame_back()
        # time.sleep(3)
        # self.find_elements_choice('//button[text()=" 查询"]',1)

    @allure.step("通过评估代码查询结果")
    def search_code_number(self):
        return self.find_element(app["评估代码搜索结果"]).text


    def search_material(self, material):
        self.input_text(app["评估代码供货品类配置-物料小类查询输入框"], material)
        self.is_click(app["评估代码供货品类配置-查询"])


    @allure.step("修改数据的评分规则")
    def change_rule(self, code):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.input_text(app["评估代码供货品类配置-评估代码查询输入框"], code)
        self.is_click(app["评估代码供货品类配置-查询"])
        self.is_click(app["评估代码搜索结果第一条"])
        self.is_click(app["评估代码供货品类配置-修改"])
        self.is_click(app["评估代码供货品类配置-修改-评分规则"])
        self.frame_back()
        self.frame_enter(app["评估代码供货品类配置-新建-评分规则iframe"])
        self.is_click(app["评估代码供货品类配置-新建-评分规则-选择"])
        self.is_click(app["评估代码供货品类配置-新建-评分规则-确定"])
        self.frame_back()
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-新建-确定"])
        self.frame_back()
        self.is_click(app["评估代码供货品类配置-新建-确定-保存确定"])
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.clear_input(app["评估代码供货品类配置-评估代码查询输入框"])
        self.is_click(app["评估代码供货品类配置-查询"])
        self.frame_back()

    @allure.step("导出模板")
    def export_template(self):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-excel导出模板"])
        time.sleep(2)
        self.frame_back()


    @allure.step("跳转到列表某一页")
    def input_page(self, page):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.keyboard_backspace(app["评估代码供货品类配置-跳转到第几页"])
        self.clear_input(app["评估代码供货品类配置-跳转到第几页"])
        self.input_text(app["评估代码供货品类配置-跳转到第几页"], page)
        # self.is_click(app["评估代码供货品类配置-跳转到第几页"])
        self.keyboard_enter(app["评估代码供货品类配置-跳转到第几页"])
        self.frame_back()


    @allure.step("跳转到列表下一页")
    def next_page(self, page):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.keyboard_backspace(app["评估代码供货品类配置-跳转到第几页"])
        self.clear_input(app["评估代码供货品类配置-跳转到第几页"])
        self.input_text(app["评估代码供货品类配置-跳转到第几页"], page)
        self.keyboard_enter(app["评估代码供货品类配置-跳转到第几页"])
        self.is_click(app["评估代码供货品类配置-列表下一页"])
        self.frame_back()


    @allure.step("跳转到列表尾页")
    def end_page(self):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-跳转到尾页"])
        self.frame_back()

    @allure.step("跳转到列表上一页")
    def previous_page(self, page):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.keyboard_backspace(app["评估代码供货品类配置-跳转到第几页"])
        self.clear_input(app["评估代码供货品类配置-跳转到第几页"])
        self.input_text(app["评估代码供货品类配置-跳转到第几页"], page)
        self.keyboard_enter(app["评估代码供货品类配置-跳转到第几页"])
        self.is_click(app["评估代码供货品类配置-列表上一页"])
        self.frame_back()


    @allure.step("跳转到列表首页")
    def first_page(self, page):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.keyboard_backspace(app["评估代码供货品类配置-跳转到第几页"])
        self.clear_input(app["评估代码供货品类配置-跳转到第几页"])
        self.input_text(app["评估代码供货品类配置-跳转到第几页"], page)
        self.keyboard_enter(app["评估代码供货品类配置-跳转到第几页"])
        self.is_click(app["评估代码供货品类配置-跳转到首页"])
        self.frame_back()


    @allure.step("筛选列表中评估代码列")
    def current_page(self):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        a = self.find_element(app["评估代码供货品类配置-当前页"]).text
        print("打印当前页码%s" % a)
        return self.find_element(app["评估代码供货品类配置-当前页"]).text


    def Frameback(self):
        self.frame_back()

    @allure.step("筛选列表中评估代码列")
    def screening_valuecode(self):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-评估代码列表筛选按钮"])
        self.is_click(app["评估代码供货品类配置-评估代码筛选取消全选"])
        self.is_click(app["评估代码供货品类配置-评估代码筛选第一个"])
        self.is_click(app["评估代码供货品类配置-评估代码筛选确定"])
        self.frame_back()



    @allure.step("新建评估代码管理人员")
    def enter_PersonManage(self):
        self.frame_enter(app["供应商绩效iframe"])
        self.is_click(app["供应商绩效->评估代码管理人员配置"])
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])

    def close_PersonManage(self):
        self.frame_back()
        self.hover(app["评估代码管理人员配置-页面窗口标题"])
        self.hover_click(app["评估代码管理人员配置-关闭页面"])







    @allure.step("新建评估代码管理人员")
    def create_blank_code(self):
        self.is_click(app["评估代码管理人员配置-新建"])
        self.is_click(app["评估代码管理人员配置-新建确定"])


    def get_message(self):
        self.frame_back()
        return self.find_element(app["评估代码管理人员配置-新建无内容提示"]).text

    def get_message_close(self):
        self.is_click(app["评估代码管理人员配置-新建无内容提示关闭"])

    def enter_iframe(self):
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])

    def create_cancel(self):
        self.is_click(app["评估代码管理人员配置-新建取消"])


    @allure.step("新建评估代码管理人员")
    def create_blank_code(self):
        self.is_click(app["评估代码管理人员配置-新建"])
        self.is_click(app["评估代码管理人员配置-新建确定"])


    @allure.step("输入评估代码搜索")
    def person_search_code(self, code):
        self.input_text(app["评估代码管理人员配置-评估代码输入框"], code)
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("清空输入的评估代码")
    def clear_input_code(self):
        self.clear_input(app["评估代码管理人员配置-评估代码输入框"])

    @allure.step("业务类型选择手机查询")
    def select_type(self):
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择手机"])
        self.is_click(app["评估代码管理人员配置-查询"])


    @allure.step("业务类型选择2G查询")
    def select_type_2G(self):
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择2G"])
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("业务类型选择手机查询")
    def select_type_phone(self):
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择手机"])
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("业务类型选择新业务查询")
    def select_type_newservice(self):
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择新业务"])
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("业务类型选择配件查询")
    def select_type_accessory(self):
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择配件"])
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("业务类型选择配件查询")
    def select_type_synthesis(self):
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择综合"])
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("业务类型选择综合查询")
    def select_type_synthesis(self):
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择综合"])
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("业务类型选择外研查询")
    def select_type_foreign(self):
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择外研"])
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("业务类型选择为空")
    def select_type_blank(self):
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别请选择"])
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("业务类型选择为空")
    def get_search_count(self):

        count = self.find_element(app["评估代码管理人员配置-查询结果"]).text()
        print(count)
        # print(count.index(7))
        # num = count.index(7)
        # return num


if __name__ == '__main__':
    pass



