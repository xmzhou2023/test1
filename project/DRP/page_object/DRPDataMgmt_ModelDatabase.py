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
        logging.info("前往菜单{}", format(tab))
        sleep(1)

    @allure.step("点击新增按钮")
    def append_button(self):
        self.is_click(user['新增按钮'])
        logging.info("打开新增弹窗")
        sleep(1)

    @allure.step("点击变更日志按钮")
    def changelog_button(self):
        self.is_click(user['变更日志按钮'])
        logging.info("前往变更日志页签")

    @allure.step("点击筛选按钮")
    def screen_button(self):
        self.is_click(user['筛选按钮'])
        logging.info("打开筛选框")
        sleep(1)

    @allure.step("关闭筛选弹窗")
    def close_screen(self):
        self.is_click(user['关闭筛选'])
        sleep(1)

    @allure.step("新增弹窗取消")
    def append_cancel(self):
        self.is_click(user['新增_取消'])
        logging.info("取消新增")
        sleep(1)

    @allure.step("新增_关闭弹窗")
    def appendClose_button(self):
        self.is_click(user['新增_关闭弹窗'])
        logging.info("关闭新增弹窗")
        sleep(1)

    @allure.step("新增弹窗 来源选项（必填）")
    def source_option(self, source=None):
        self.is_click(user['新增_来源'])
        try:
            if source == "数仓":
                self.is_click(user['新增_下拉选项'], "1")
            elif source == "自建":
                self.is_click(user['新增_下拉选项'], "2")
            logging.info("新增机型来源：{}", format(source))
        except:
            self.is_click(user['新增_来源'])
        sleep(1)
        return source

    @allure.step("新增弹窗 供应类型选项（必填）")
    def supplyType_option(self, supplyType=None):
        self.is_click(user['新增_供应类型'])
        try:
            if supplyType == "自研":
                self.is_click(user['新增_下拉选项'], "1")
            elif supplyType == "外购":
                self.is_click(user['新增_下拉选项'], "2")
            logging.info("供应商类型：{}", format(supplyType))
        except:
            self.is_click(user['新增_供应类型'])
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
            logging.info("品牌：{}", format(brand))
        except:
            self.is_click(user['新增_品牌'])
        sleep(1)

    @allure.step("新增弹窗 大类粗选项（必填）")
    def broadCoarse_option(self, broadCoarse=None):
        self.is_click(user['新增_大类粗'])
        try:
            if broadCoarse == "功能机":
                self.is_click(user['新增_下拉选项'], "1")
            elif broadCoarse == "智能机":
                self.is_click(user['新增_下拉选项'], "2")
            logging.info("大类粗：{}", format(broadCoarse))
        except:
            self.is_click(user['新增_大类粗'])
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
            logging.info("大类细：{}", format(broadFine))
        except:
            self.is_click(user['新增_大类细'])
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
                c = b.index(series) + 1  # 取到所传参数所在行号
                self.find_element(user['新增_下拉选项'], str(c)).click()  # 将行号c替换到xpath中进行相关操作
                logging.info("系列：{}", format(series))
        else:
            self.is_click(user['新增_系列'])
        sleep(1)

    @allure.step("新增弹窗 项目名_自建输入（必填）")
    def projectName_input(self, projectName=None):
        self.readonly_input_text(user['新增_项目名_自建'], projectName)
        logging.info("来源=自建，项目名为文本框，输入项目：{}", format(projectName))
        sleep(1)

    @allure.step("新增弹窗 项目名_数仓选项（必填）")
    def projectName_option(self, projectName=None):
        self.is_click(user['新增_项目名_数仓'])
        sleep(2)
        a = self.find_elements(user['新增_下拉选项集'])
        b = []
        for i in range(len(a)):
            b.append(a[i].text)
        if projectName in b:
            c = b.index(projectName) + 1  # 取到所传参数所在行号
            self.find_element(user['新增_下拉选项'], str(c)).click()
            logging.info("来源=数仓，项目名为下拉选项，选择项目：{}", format(projectName))
            sleep(1)

    @allure.step("新增弹窗 内存版本输入（必填）")
    def memoryVersion(self, memoryVersion=None):
        self.readonly_input_text(user['新增_内存版本'], memoryVersion)
        logging.info("内存版本：{}", format(memoryVersion))
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
            logging.info("网络制式：{}", format(network))
        except:
            self.is_click(user['新增_网络制式'])
        sleep(1)

    @allure.step("新增弹窗 市场名输入（必填）")
    def marketName(self, marketName=None):
        self.readonly_input_text(user['新增_市场名'], marketName)
        logging.info("市场名：{}", format(marketName))
        sleep(1)

    @allure.step("新增弹窗 打开颜色弹窗")
    def color_window(self):
        self.is_click(user['新增_颜色'])
        logging.info("打开颜色弹窗")
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
            logging.info("颜色：{}", format(color))

    @allure.step("新增弹窗 保存颜色")
    def save_color(self):
        self.is_click(user['新增_颜色（保存）'])
        logging.info("点击颜色保存按钮")

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
            logging.info("状态：{}", format(state))
        except:
            self.is_click(user['新增_状态'])

    @allure.step("新增弹窗 FOB HK选择日期")
    def fob_hk(self, date):
        self.is_click(user['新增_FOB HK'])
        self.is_click(user['新增_FOB HK日期'], date)
        logging.info("选择FOB HK日期：{}", format(date))

    @allure.step("新增弹窗 LT输入")
    def lt_input(self, LT):
        self.readonly_input_text(user['新增_LT'], LT)
        logging.info("LT：",format(LT))


    @allure.step("新增弹窗 选择上市时间")
    def listing_date(self, years, month):
        self.is_click(user['新增_上市时间'])
        self.is_click(user['新增_年'])
        self.is_click(user['新增_选择年'], years)
        self.is_click(user['新增_上市/清尾时间'], month)

    @allure.step("新增弹窗 选择清尾时间")
    def cleaning_date(self, years, month):
        self.is_click(user['新增_清尾时间'])
        self.is_click(user['新增_年'])
        self.is_click(user['新增_选择年'], years)
        self.is_click(user['新增_上市/清尾时间'], month)

    @allure.step("新增弹窗 输入备注")
    def remark_input(self, remark):
        self.readonly_input_text(user['新增_备注'], remark)

    @allure.step("新增弹窗 新增保存")
    def save_button(self,t):
        self.is_click(user['新增_确定'])
        if t == "反例":
            a = self.element_text(user['新增 必填项'])
            if a == '不能为空':
                logging.info("有必填项未维护,新增失败")
                self.appendClose_button()
            # else:
            #     assert False
        else:
            # TODO
            ...

    @allure.step("导入弹窗-下载导入模板")
    def downloadTemplate_button(self, content):
        self.check_download(user['下载导入模板'], content)
        sleep()

    @allure.step("导入弹窗-选择文件")
    def selectFile_button(self):
        self.find_element(user['选择文件']).send_keys("project/DRP/excel_drive/TestCase.xlsx")
        sleep()

    @allure.step("导入弹窗-选择文件")
    def import_button(self):
        self.is_click(user['导入按钮'])
        sleep()

    @allure.step("导入弹窗-关闭")
    def importClose_button(self, button):
        self.is_click(user['关闭导入弹窗'], button)
        sleep()


    @allure.step("导出按钮")
    def export(self, content):
        self.check_download(user['导出按钮'], content)
        sleep()

if __name__ == '__main__':
    pass