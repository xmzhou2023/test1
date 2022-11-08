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

    @allure.step("通过物料小类查询")
    def search_cate(self, cate):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.input_text(app["评估代码供货品类配置-物料小类查询输入框"], cate)
        self.is_click(app["评估代码供货品类配置-查询"])

    @allure.step("输入内容")
    def Clear_input(self,text):
        self.clear_input(app[text])

    @allure.step("通过物料小类查询结果")
    def search_cate_number(self):
        return self.find_element(app["评估代码供货品类配置-物料小类查询结果"]).text




    @allure.step("通过物料小类和评估代码查询")
    def search_cate_code(self, code, cate):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.input_text(app["评估代码供货品类配置-评估代码查询输入框"], code)
        self.input_text(app["评估代码供货品类配置-物料小类查询输入框"], cate)
        self.is_click(app["评估代码供货品类配置-查询"])





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
        self.is_click(app["评估代码供货品类配置-修改成功提示消息关闭"])




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
        self.is_click(app["评估代码供货品类配置-评估代码筛选输入框"])
        self.input_text(app["评估代码供货品类配置-评估代码筛选输入框"],"C0001")
        self.is_click(app["评估代码供货品类配置-评估代码筛选C0001"])
        self.is_click(app["评估代码供货品类配置-评估代码筛选确定"])
        self.frame_back()


    #评估代码管理人员配置模块
    @allure.step("进入评估代码管理人员配置模块")
    def enter_PersonManage(self):
        self.frame_enter(app["供应商绩效iframe"])
        self.is_click(app["供应商绩效->评估代码管理人员配置"])
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])

    @allure.step("关闭评估代码管理人员配置模块")
    def close_PersonManage(self):
        self.frame_back()
        self.hover(app["评估代码管理人员配置-页面窗口标题"])
        self.hover_click(app["评估代码管理人员配置-关闭页面"])
        self.frame_exit()



    @allure.step("新建评估代码管理人员--不填评估代码")
    def create_blank_all(self):
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


    @allure.step("新建评估代码管理人员--不填供应商账号")
    def create_blank_elsnumber(self):
        self.is_click(app["评估代码管理人员配置-新建"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择A0101"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择确定"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建确定"])

    def get_blank_massage(self):
        self.frame_back()
        return self.find_element(app["评估代码管理人员配置-新建-只填代码提示消息"]).text


    def close_blank_mass(self):
        self.is_click(app["评估代码管理人员配置-新建只填代码提示关闭"])



    @allure.step("新建评估代码管理人员--不填评估人")
    def create_blank_evaluator(self):
        self.is_click(app["评估代码管理人员配置-新建"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择A0101"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择确定"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建-供应商选择放大镜"])
        time.sleep(2)
        self.is_click(app["评估代码管理人员配置-新建-供应商选择860001"])
        self.is_click(app["评估代码管理人员配置-新建-供应商选择确定"])
        self.is_click(app["评估代码管理人员配置-新建确定"])


    @allure.step("新建评估代码管理人员--填部分评估人01")
    def create_blank_evaluator01(self):
        self.is_click(app["评估代码管理人员配置-新建"])
        # 选择评估代码
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择A0101"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择确定"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        # 选择供应商
        self.is_click(app["评估代码管理人员配置-新建-供应商选择放大镜"])
        time.sleep(2)
        self.is_click(app["评估代码管理人员配置-新建-供应商选择860001"])
        self.is_click(app["评估代码管理人员配置-新建-供应商选择确定"])
        # 选择成本评估人
        self.is_click(app["评估代码管理人员配置-新建-成本选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.input_text(app["评估代码管理人员配置-新建-评估人搜索输入框"], "1001")
        self.is_click(app["评估代码管理人员配置-新建-评估人搜索查询"])
        self.is_click(app["评估代码管理人员配置-新建-成本选择1001"])
        self.is_click(app["评估代码管理人员配置-新建-成本选择确定"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建确定"])
        self.frame_back()
        self.is_click(app["评估代码管理人员配置-新建保存提示确定"])

    @allure.step("新建评估代码管理人员--填部分评估人提示消息01")
    def get_blank_massage01(self):
        # self.frame_back()
        return self.find_element(app["评估代码管理人员配置-新建-只填代码提示消息"]).text

    @allure.step("新建评估代码管理人员--新建取消01")
    def create_cancel01(self):
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建取消"])

    @allure.step("新建评估代码管理人员--填部分评估人02")
    def create_blank_evaluator02(self):
        self.is_click(app["评估代码管理人员配置-新建"])
        # 选择评估代码
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择A0101"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择确定"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        # 选择供应商
        self.is_click(app["评估代码管理人员配置-新建-供应商选择放大镜"])
        time.sleep(2)
        self.is_click(app["评估代码管理人员配置-新建-供应商选择860001"])
        self.is_click(app["评估代码管理人员配置-新建-供应商选择确定"])
        # 选择成本评估人
        self.is_click(app["评估代码管理人员配置-新建-成本选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.input_text(app["评估代码管理人员配置-新建-评估人搜索输入框"], "1001")
        self.is_click(app["评估代码管理人员配置-新建-评估人搜索查询"])
        self.is_click(app["评估代码管理人员配置-新建-成本选择1001"])
        self.is_click(app["评估代码管理人员配置-新建-成本选择确定"])
        self.frame_back()
        # 选择交付评估人
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建-交付选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.input_text(app["评估代码管理人员配置-新建-评估人搜索输入框"], "1001")
        self.is_click(app["评估代码管理人员配置-新建-评估人搜索查询"])
        self.is_click(app["评估代码管理人员配置-新建-交付选择1001"])
        self.is_click(app["评估代码管理人员配置-新建-交付选择确定"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建确定"])
        self.frame_back()
        self.is_click(app["评估代码管理人员配置-新建保存提示确定"])


    @allure.step("新建评估代码管理人员-创建成功")
    def create_success_code(self):
        self.is_click(app["评估代码管理人员配置-新建"])
        # 选择评估代码
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择A0101"])
        self.is_click(app["评估代码管理人员配置-新建-评估代码选择确定"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建-业务类型选择下拉框"])
        self.is_click(app["评估代码管理人员配置-新建-业务类型选择内容"], "2G")
        # 选择供应商
        self.is_click(app["评估代码管理人员配置-新建-供应商选择放大镜"])
        self.is_click(app["评估代码管理人员配置-新建-供应商选择860001"])
        self.is_click(app["评估代码管理人员配置-新建-供应商选择确定"])
        # 选择成本评估人
        self.is_click(app["评估代码管理人员配置-新建-成本选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.input_text(app["评估代码管理人员配置-新建-评估人搜索输入框"], "1001")
        self.is_click(app["评估代码管理人员配置-新建-评估人搜索查询"])
        self.is_click(app["评估代码管理人员配置-新建-成本选择1001"])
        self.is_click(app["评估代码管理人员配置-新建-成本选择确定"])
        self.frame_back()
        # 选择交付评估人
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建-交付选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.input_text(app["评估代码管理人员配置-新建-评估人搜索输入框"], "1001")
        self.is_click(app["评估代码管理人员配置-新建-评估人搜索查询"])
        self.is_click(app["评估代码管理人员配置-新建-交付选择1001"])
        self.is_click(app["评估代码管理人员配置-新建-交付选择确定"])
        self.frame_back()
        # 选择质量评估人
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建-质量选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.input_text(app["评估代码管理人员配置-新建-评估人搜索输入框"], "1001")
        self.is_click(app["评估代码管理人员配置-新建-评估人搜索查询"])
        self.is_click(app["评估代码管理人员配置-新建-质量选择1001"])
        self.is_click(app["评估代码管理人员配置-新建-质量选择确定"])
        self.frame_back()
        # 选择管理评估人
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建-管理选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.input_text(app["评估代码管理人员配置-新建-评估人搜索输入框"], "1005")
        self.is_click(app["评估代码管理人员配置-新建-评估人搜索查询"])
        self.is_click(app["评估代码管理人员配置-新建-管理选择1005"])
        self.is_click(app["评估代码管理人员配置-新建-管理选择确定"])
        self.frame_back()
        # 选择技术评估人
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建-技术选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.input_text(app["评估代码管理人员配置-新建-评估人搜索输入框"], "1005")
        self.is_click(app["评估代码管理人员配置-新建-评估人搜索查询"])
        self.is_click(app["评估代码管理人员配置-新建-技术选择1005"])
        self.is_click(app["评估代码管理人员配置-新建-技术选择确定"])
        self.frame_back()
        # 选择技术2评估人
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建-技术2选择放大镜"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置-新建-选择内容弹窗iframe"])
        self.input_text(app["评估代码管理人员配置-新建-评估人搜索输入框"], "1009")
        self.is_click(app["评估代码管理人员配置-新建-评估人搜索查询"])
        self.is_click(app["评估代码管理人员配置-新建-技术2选择1009"])
        self.is_click(app["评估代码管理人员配置-新建-技术2选择确定"])
        self.frame_back()
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])
        self.is_click(app["评估代码管理人员配置-新建确定"])
        self.frame_back()
        self.is_click(app["评估代码管理人员配置-新建保存提示确定"])
        # self.frame_enter(app["评估代码管理人员配置页面内容iframe"])

    @allure.step("新建创建成功提示")
    def create_success_mess(self):
        return self.find_element(app["评估代码管理人员配置-新建操作成功"]).text


    @allure.step("新建创建成功提示关闭")
    def create_success_mess_close(self):
        self.is_click(app["评估代码管理人员配置-新建操作成功关闭"])
        self.frame_enter(app["评估代码管理人员配置页面内容iframe"])


    @allure.step("输入评估代码搜索")
    def person_search_code(self, code):
        self.input_text(app["评估代码管理人员配置-评估代码输入框"], code)
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("清空输入的评估代码")
    def clear_input_code(self):
        self.clear_input(app["评估代码管理人员配置-评估代码输入框"])



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

    @allure.step("查询结果数量")
    def get_search_count(self):
        count = self.find_element(app["评估代码管理人员配置-查询结果"]).text()
        print(count)
        # print(count.index(7))
        # num = count.index(7)
        # return num


    @allure.step("评估代码管理人员配置-查找供应商账号")
    def search_els_number(self, els_number):
        self.is_click(app["评估代码管理人员配置-更多"])
        self.input_text(app["评估代码管理人员配置-供应商账号输入框"], els_number)
        self.is_click(app["评估代码管理人员配置-查询"])

    @allure.step("评估代码管理人员配置-查找供应商账号清除")
    def clear_search_elsnumber(self):
        self.is_click(app["评估代码管理人员配置-更多"])
        self.clear_input(app["评估代码管理人员配置-供应商账号输入框"])
        self.is_click(app["评估代码管理人员配置-查询"])


    @allure.step("评估代码管理人员配置-供应商和评估代码组合查询")
    def search_code_elsnumber(self, code, els_number):
        self.input_text(app["评估代码管理人员配置-评估代码输入框"], code)
        self.is_click(app["评估代码管理人员配置-更多"])
        self.input_text(app["评估代码管理人员配置-供应商账号输入框"], els_number)
        self.is_click(app["评估代码管理人员配置-查询"])



    @allure.step("评估代码管理人员配置-供应商和评估代码组合查询")
    def search_code_category(self, code):
        self.input_text(app["评估代码管理人员配置-评估代码输入框"], code)
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择手机"])
        self.is_click(app["评估代码管理人员配置-查询"])



    @allure.step("评估代码管理人员配置-供应商和评估代码组合查询")
    def search_elsnumber_category(self, els_number):
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择2G"])
        self.is_click(app["评估代码管理人员配置-更多"])
        self.input_text(app["评估代码管理人员配置-供应商账号输入框"], els_number)
        self.is_click(app["评估代码管理人员配置-查询"])


    @allure.step("评估代码管理人员配置-供应商和评估代码组合查询")
    def search_all_combined(self, code, els_number):
        self.input_text(app["评估代码管理人员配置-评估代码输入框"], code)
        self.is_click(app["评估代码管理人员配置-供应商类别选择框"])
        self.is_click(app["评估代码管理人员配置-供应商类别选择手机"])
        self.is_click(app["评估代码管理人员配置-更多"])
        self.input_text(app["评估代码管理人员配置-供应商账号输入框"], els_number)
        self.is_click(app["评估代码管理人员配置-查询"])


    @allure.step("评估代码管理人员配置-列表筛选评估代码")
    def pick_code(self):
        self.is_click(app["评估代码管理人员配置-评估代码筛选"])
        self.is_click(app["评估代码管理人员配置-评估代码筛选输入框"])
        self.input_text(app["评估代码管理人员配置-评估代码筛选输入框"],"C0001")
        self.is_click(app["评估代码管理人员配置-评估代码筛选C0001"])
        self.is_click(app["评估代码管理人员配置-评估代码筛选确定"])
        self.is_click(app["评估代码管理人员配置-评估代码筛选"])
        self.is_click(app["评估代码管理人员配置-评估代码筛选重置"])
        self.is_click(app["评估代码管理人员配置-评估代码筛选确定"])



    @allure.step("进入评估模板管理")
    def enter_Value_Template(self):
        self.frame_enter(app["供应商绩效iframe"])
        self.is_click(app["供应商绩效->评估模板管理"])
        self.frame_enter(app["供应商绩效->评估模板iframe"])



    @allure.step("进入评估模板管理-")
    def close_Value_Template(self):
        self.frame_back()
        self.hover(app["评估模板管理-页面窗口标题"])
        self.hover_click(app["评估模板管理-关闭页面"])

    @allure.step("评估模板管理-根据模板编号查询")
    def search_template(self,number):
        self.input_text(app["评估模板管理-模板编号查询输入"], number)
        self.is_click(app["评估模板管理-查询"])
        self.clear_input(app["评估模板管理-模板编号查询输入"])
        self.is_click(app["评估模板管理-查询"])


    @allure.step("评估模板管理-根据模板名称查询")
    def search_template_name(self, name):
        self.input_text(app["评估模板管理-模板名称查询输入"], name)
        self.is_click(app["评估模板管理-查询"])
        self.clear_input(app["评估模板管理-模板名称查询输入"])
        self.is_click(app["评估模板管理-查询"])

    @allure.step("评估模板管理-根据模板名称+编号组合查询")
    def search_template_combined(self,number,name):
        self.input_text(app["评估模板管理-模板编号查询输入"], number)
        self.input_text(app["评估模板管理-模板名称查询输入"], name)
        self.is_click(app["评估模板管理-查询"])
        self.clear_input(app["评估模板管理-模板编号查询输入"])
        self.clear_input(app["评估模板管理-模板名称查询输入"])
        self.is_click(app["评估模板管理-查询"])





if __name__ == '__main__':
    pass



