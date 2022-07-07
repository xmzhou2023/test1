import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)


class ModelDatabase(Base):
    """机型库"""

    @allure.step("前往Tab菜单")
    def goto_tab(self, tab):
        self.is_click(user['Tab菜单'], tab)
        sleep(1)

    @allure.step("点击功能按钮")
    def button(self, button):
        self.is_click(user['功能按钮'], button)
        sleep(1)

    @allure.step("新增弹窗按钮")
    def cancel(self, button):
        self.is_click(user['新增_按钮'], button)
        sleep(1)

    @allure.step("新增弹窗 来源选项（必填）")
    def source_option(self, source=None):
        self.is_click(user['新增_来源'])
        try:
            if source == "数仓":
                self.is_click(user['新增_下拉选项'], "1")
            elif source == "自建":
                self.is_click(user['新增_下拉选项'], "2")
        except:
            self.is_click(user['新增_来源'])
        sleep(1)
        return

    @allure.step("新增弹窗 供应类型选项（必填）")
    def supplyType_option(self, supplyType=None):
        self.is_click(user['新增_供应类型'])
        try:
            if supplyType == "自研":
                self.is_click(user['新增_下拉选项'], "1")
            elif supplyType == "外购":
                self.is_click(user['新增_下拉选项'], "2")
        except:
            self.is_click(user['新增_来源'])
        sleep(1)

    @allure.step("新增弹窗 品牌选项（必填）")
    def brand_option(self, brand=None):
        self.is_click(user['新增_品牌'])
        try:
            if brand == "Infinix":
                self.is_click(user['新增_下拉选项'], "1")
            elif brand == "itel":
                self.is_click(user['新增_下拉选项'], "2")
            elif brand == "TECNO":
                self.is_click(user['新增_下拉选项'], "3")
        except:
            self.is_click(user['新增_来源'])
        sleep(1)

    @allure.step("新增弹窗 大类粗选项（必填）")
    def broadCoarse_option(self, broadCoarse=None):
        self.is_click(user['新增_大类粗'])
        try:
            if broadCoarse == "功能机":
                self.is_click(user['新增_下拉选项'], "1")
            elif broadCoarse == "智能机":
                self.is_click(user['新增_下拉选项'], "2")
        except:
            self.is_click(user['新增_来源'])
        sleep(1)

    @allure.step("新增弹窗 大类细选项")
    def broadFine_option(self, broadFine=None):
        self.is_click(user['新增_大类细'])
        try:
            if broadFine == "低端SP":
                self.is_click(user['新增_下拉选项'], "1")
            elif broadFine == "中端SP":
                self.is_click(user['新增_下拉选项'], "2")
            elif broadFine == "高端SP":
                self.is_click(user['新增_下拉选项'], "3")
        except:
            self.is_click(user['新增_来源'])
        sleep(1)

    @allure.step("新增弹窗 系列选项（必填）")
    def series_option(self, series=None):
        brand = self.element_text(user['新增_品牌'])
        self.is_click(user['新增_系列'])
        if brand != "请选择":
            a = self.find_elements(user['新增_下拉选项集'])
            b = []
            for i in range(len(a)):
                b.append(a[i].text)
            if series in b:
                c = int(b.index(series)) + 1  # 取到所传参数所在行号
                self.find_element(user['新增_下拉选项'], str(c)).click()  # 将行号c替换到xpath中进行相关操作
        else:
            self.is_click(user['新增_系列'])
        sleep(1)

    @allure.step("新增弹窗 项目名_自建输入（必填）")
    def projectName_input(self, projectName=None):
        self.readonly_input_text(user['新增_项目名_自建'], projectName)
        sleep(1)

    @allure.step("新增弹窗 项目名_数仓选项（必填）")
    def projectName_option(self, projectName=None):

        self.is_click(user['新增_项目名_数仓'])
        a = self.find_elements(user['新增_下拉选项集'])
        b = []
        for i in range(len(a)):
            b.append(a[i].text)
        if projectName in b:
            c = int(b.index(projectName)) + 1  # 取到所传参数所在行号
            self.find_element(user['新增_下拉选项'], str(c)).click()
            sleep(1)

    @allure.step("新增弹窗 内存版本输入（必填）")
    def memoryVersion(self, memoryVersion=None):
        self.readonly_input_text(user['新增_内存版本'], memoryVersion)
        sleep(1)

    @allure.step("新增弹窗 网络制式选项（必填）")
    def network_option(self, network=None):
        self.is_click(user['新增_网络制式'])
        try:
            if network == "2G":
                self.is_click(user['新增_下拉选项'], "1")
            elif network == "3G":
                self.is_click(user['新增_下拉选项'], "2")
            elif network == "4G":
                self.is_click(user['新增_下拉选项'], "3")
            elif network == "5G":
                self.is_click(user['新增_下拉选项'], "4")
        except:
            self.is_click(user['新增_网络制式'])
        sleep(1)

    @allure.step("新增弹窗 市场名输入（必填）")
    def marketName(self, marketName=None):
        self.readonly_input_text(user['新增_市场名'], marketName)
        sleep(1)

    @allure.step("新增弹窗 打开颜色弹窗")
    def color_window(self):
        self.is_click(user['新增_颜色'])
        sleep(2)

    @allure.step("新增弹窗 颜色选择（必填）")
    def color(self, color=None):
        self.readonly_input_text(user['新增_颜色（弹窗输入框）'], color)
        sleep(1)
        a = self.find_elements(user['新增_颜色（定位颜色所在行）'])
        b = []
        for i in range(len(a)):
            b.append(a[i].text)
        if color in b:
            c = b.index(color) + 1  # 取到所传参数所在行号
            self.find_element(user['新增_颜色（添加按钮）'], str(c)).click()  # 将行号c替换到xpath中进行相关操作

    @allure.step("新增弹窗 保存颜色")
    def save_color(self):
        self.is_click(user['新增_颜色（保存）'])

    @allure.step("新增弹窗 状态选项（必填）")
    def state_option(self, state):
        self.is_click(user['新增_状态'])
        try:
            if state == "NP":
                self.is_click(user['新增_下拉选项'], "1")
            elif state == "MP":
                self.is_click(user['新增_下拉选项'], "2")
            elif state == "EOL":
                self.is_click(user['新增_下拉选项'], "3")
            elif state == "END":
                self.is_click(user['新增_下拉选项'], "4")
        except:
            self.is_click(user['新增_状态'])

    @allure.step("新增弹窗 FOB HK选择日期")
    def FOB_HK(self, date):
        self.is_click(user['新增_FOB HK'])
        self.is_click(user['新增_FOB HK日期'], date)

    @allure.step("新增弹窗 LT输入")
    def LT_input(self, LT):
        self.readonly_input_text(user['新增_LT'], LT)
        sleep()

    @allure.step("新增弹窗 选择上市时间")
    def listing_date(self, years, month):
        self.is_click(user['新增_上市时间'])
        sleep()
        self.is_click(user['新增_年'])
        sleep()
        self.is_click(user['新增_选择年'], years)
        sleep()
        self.is_click(user['新增_上市/清尾时间'], month)
        sleep()

    @allure.step("新增弹窗 选择清尾时间")
    def cleaning_date(self, years, month):
        self.is_click(user['新增_清尾时间'])
        sleep()
        self.is_click(user['新增_年'])
        sleep()
        self.is_click(user['新增_选择年'], years)
        sleep()
        self.is_click(user['新增_上市/清尾时间'], month)
        sleep()

    @allure.step("新增弹窗 输入备注")
    def remark_input(self, remark):
        self.readonly_input_text(user['新增_备注'], remark)

    @allure.step("新增弹窗 新增保存")
    def save_button(self, button):
        self.is_click(user['新增_按钮'], button)

    @allure.step("导入弹窗-下载导入模板")
    def downloadTemplate_button(self, button):
        self.is_click(user['下载导入模板'], button)
        sleep()

    @allure.step("导入弹窗-选择文件")
    def selectFile_button(self, button):
        self.is_click(user['选择文件'], button)
        sleep()

    @allure.step("导入弹窗-选择文件")
    def import_button(self, button):
        self.is_click(user['导入按钮'], button)
        sleep()