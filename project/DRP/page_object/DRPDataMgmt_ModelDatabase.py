import allure
import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class ModelDatabase(Base):
    """机型库"""

    @allure.step("前往Tab菜单")
    def goto_tab(self, tab):
        self.is_click(user['Tab菜单'], tab)
        logging.info("前往菜单{}".format(tab))
        if tab == '产品信息':
            return self.element_text(user['产品信息页面(新增按钮)'])
        elif tab == '产品配置':
            return self.element_text(user['页面断言(状态)'])
        else:
            return self.element_text(user['页面断言(管理维度)'])

    @allure.step("点击新增按钮")
    def append_button(self):
        self.is_click(user['新增按钮'])
        logging.info("打开新增弹窗")

    @allure.step("返回新增窗口title文本，用做断言")
    def append_title(self):
        return self.element_text(user['新增title'])

    @allure.step("点击变更日志按钮")
    def changelog_button(self):
        self.is_click(user['变更日志按钮'])
        logging.info("前往变更日志页签")
        sleep(1)

    @allure.step("关闭变更日志页签")
    def close_changelog(self):
        self.is_click(user['关闭变更日志页签'])
        logging.info("关闭变更日志页签")

    @allure.step("点击筛选按钮")
    def screen_button(self):
        self.is_click(user['筛选按钮'])
        logging.info("打开筛选框")
        sleep(1)

    @allure.step("返回筛选弹窗文本，用做断言")
    def screen_title(self):
        return self.element_text(user['筛选框断言'])

    @allure.step("关闭筛选弹窗")
    def close_screen(self):
        self.is_click(user['关闭筛选'])
        logging.info("关闭筛选框")

    @allure.step("新增弹窗取消")
    def append_cancel(self):
        self.is_click(user['新增_取消'])
        logging.info("取消新增，关闭新增窗口")

    @allure.step("新增_关闭弹窗")
    def appendClose_button(self):
        self.is_click(user['新增_关闭弹窗'])
        logging.info("关闭新增弹窗")

    @allure.step("新增弹窗 来源选项（必填）")
    def source_option(self, source=None):
        self.is_click(user['新增_来源'])
        if source == "数仓":
            self.is_click(user['新增_下拉选项'], "1")
        elif source == "自建":
            self.is_click(user['新增_下拉选项'], "2")
        else:
            self.is_click(user['新增_来源'])
        logging.info("新增机型来源：{}".format(source))
        return source

    @allure.step("新增弹窗 供应类型选项（必填）")
    def supplyType_option(self, supplyType=None):
        self.is_click(user['新增_供应类型'])
        if supplyType == "自研":
            self.is_click(user['新增_下拉选项'], "1")
        elif supplyType == "外购":
            self.is_click(user['新增_下拉选项'], "2")
        else:
            self.is_click(user['新增_供应类型'])
        logging.info("供应商类型：{}".format(supplyType))

    @allure.step("新增弹窗 品牌选项（必填）")
    def brand_option(self, brand=None):
        self.is_click(user['新增_品牌'])
        if brand == "Infinix":
            self.is_click(user['新增_下拉选项'], "1")
        elif brand == "itel":
            self.is_click(user['新增_下拉选项'], "2")
        elif brand == "TECNO":
            self.is_click(user['新增_下拉选项'], "3")
        else:
            self.is_click(user['新增_品牌'])
        logging.info("品牌：{}".format(brand))

    @allure.step("新增弹窗 大类粗选项（必填）")
    def broadCoarse_option(self, broadCoarse=None):
        self.is_click(user['新增_大类粗'])
        if broadCoarse == "功能机":
            self.is_click(user['新增_下拉选项'], "1")
        elif broadCoarse == "智能机":
            self.is_click(user['新增_下拉选项'], "2")
        else:
            self.is_click(user['新增_大类粗'])
        logging.info("大类粗：{}".format(broadCoarse))

    @allure.step("新增弹窗 大类细选项")
    def broadFine_option(self, broadFine=None):
        self.is_click(user['新增_大类细'])
        if broadFine == "低端SP":
            self.is_click(user['新增_下拉选项'], "1")
        elif broadFine == "中端SP":
            self.is_click(user['新增_下拉选项'], "2")
        elif broadFine == "高端SP":
            self.is_click(user['新增_下拉选项'], "3")
        else:
            self.is_click(user['新增_大类细'])
        logging.info("大类细：{}".format(broadFine))

    @allure.step("新增弹窗 系列选项（必填）")
    def series_option(self, series=None):
        self.is_click(user['新增_系列'])
        self.is_click(user['新增_下拉选项(系列&项目名)'], series)
        logging.info("系列：{}".format(series))

    @allure.step("新增弹窗 项目名_自建输入（必填）")
    def projectName_input(self, projectName=None):
        self.readonly_input_text(user['新增_项目名_自建'], projectName)
        logging.info("来源=自建，项目名为文本框，输入项目：{}".format(projectName))

    @allure.step("新增弹窗 项目名_数仓选项（必填）")
    def projectName_option(self, projectName=None):
        self.is_click(user['新增_项目名_数仓'])
        self.is_click(user['新增_下拉选项(系列&项目名)'], projectName)
        logging.info("来源=数仓，项目名为下拉选项，选择项目：{}".format(projectName))

    @allure.step("新增弹窗 内存版本输入（必填）")
    def memoryVersion(self, memoryVersion=None):
        self.readonly_input_text(user['新增_内存版本'], memoryVersion)
        logging.info("内存版本：{}".format(memoryVersion))

    @allure.step("新增弹窗 网络制式选项（必填）")
    def network_option(self, network=None):
        self.is_click(user['新增_网络制式'])
        if network == "2G":
            self.is_click(user['新增_下拉选项'], "1")
        elif network == "3G":
            self.is_click(user['新增_下拉选项'], "2")
        elif network == "4G":
            self.is_click(user['新增_下拉选项'], "3")
        elif network == "5G":
            self.is_click(user['新增_下拉选项'], "4")
        else:
            self.is_click(user['新增_网络制式'])
        logging.info("网络制式：{}".format(network))

    @allure.step("新增弹窗 市场名输入（必填）")
    def marketName(self, marketName=None):
        self.readonly_input_text(user['新增_市场名'], marketName)
        logging.info("市场名：{}".format(marketName))
        sleep(1)

    @allure.step("新增弹窗 颜色选择（必填）")
    def color(self, color=None):
        self.is_click(user['新增_颜色'])
        logging.info("打开颜色弹窗")
        sleep(2)
        self.readonly_input_text(user['新增_颜色（弹窗输入框）'], color)
        sleep(1)
        a = self.find_elements(user['新增_颜色（定位颜色所在行）'])
        b = []
        for i in range(len(a)):
            b.append(a[i].text)
        if color in b:
            c = b.index(color) + 1  # 取到所传参数所在行号
            self.find_element(user['新增_颜色（添加按钮）'], str(c)).click()  # 将行号c替换到xpath中进行相关操作
            logging.info("颜色：{}".format(color))

    @allure.step("新增弹窗 保存颜色")
    def save_color(self):
        self.is_click(user['新增_颜色（保存）'])
        logging.info("点击颜色保存按钮")

    @allure.step("新增弹窗 状态选项（必填）")
    def state_option(self, state):
        self.is_click(user['新增_状态'])
        if state == "NP":
            self.is_click(user['新增_下拉选项'], "1")
        elif state == "MP":
            self.is_click(user['新增_下拉选项'], "2")
        elif state == "EOL":
            self.is_click(user['新增_下拉选项'], "3")
        elif state == "END":
            self.is_click(user['新增_下拉选项'], "4")
        else:
            self.is_click(user['新增_状态'])
        logging.info("状态：{}".format(state))

    @allure.step("新增弹窗 FOB HK选择日期")
    def fob_hk(self, date):
        self.is_click(user['新增_FOB HK'])
        self.is_click(user['新增_FOB HK日期'], date)
        logging.info("选择FOB HK日期：{}".format(date))

    @allure.step("新增弹窗 LT输入")
    def lt_input(self, LT):
        self.readonly_input_text(user['新增_LT'], LT)
        logging.info("LT：".format(LT))

    @allure.step("新增弹窗 选择上市时间")
    def listing_date(self, years, month):
        self.is_click(user['新增_上市时间'])
        self.is_click(user['新增_年'])
        self.is_click(user['新增_选择年'], years)
        self.is_click(user['新增_上市/清尾时间'], month)
        logging.info("上市日期：{}年{}".format(years, month))
        sleep(2)

    @allure.step("新增弹窗 选择清尾时间")
    def cleaning_date(self, years, month):
        self.is_click(user['新增_清尾时间'])
        self.is_click(user['新增_年'])
        self.is_click(user['新增_选择年'], years)
        self.is_click(user['新增_上市/清尾时间'], month)
        logging.info("清尾日期：{}年{}".format(years, month))

    @allure.step("新增弹窗 输入备注")
    def remark_input(self, remark):
        self.readonly_input_text(user['新增_备注'], remark)
        logging.info("备注:{}".format(remark))

    @allure.step("新增弹窗 新增保存")
    def save_button(self, caseType):
        self.is_click(user['新增_确定'])
        if caseType == "反例":
            hint = self.element_text(user['新增 必填项'])
            if hint == "不能为空":
                self.appendClose_button()
                logging.info("有必填项未维护,新增失败,关闭新增弹窗")
        else:
            logging.info("新增保存成功")

    @allure.step("返回新增成功提示文本，用做断言")
    def save_hint(self):
        return self.element_text(user['断言（新增保存成功）'])

    @allure.step("导入弹窗-下载导入模板")
    def downloadTemplate_button(self, content):
        self.check_download(user['下载导入模板'], content)

    @allure.step("导入弹窗-选择文件")
    def selectFile_button(self):
        self.find_element(user['选择文件']).send_keys("project/DRP/excel_drive/TestCase.xlsx")
        logging.info("选择文件")

    @allure.step("导入弹窗-选择文件")
    def import_button(self):
        self.is_click(user['导入按钮'])
        logging.info("点击导入按钮，打开导入弹窗")


    @allure.step("返回导入窗口文本，用做断言")
    def import_title(self):
        return self.element_text(user['导入窗口断言'])

    @allure.step("导入弹窗-关闭")
    def importClose_button(self):
        self.is_click(user['关闭导入弹窗'])
        logging.info("关闭导入弹窗")

    @allure.step("导出按钮")
    def export(self, content):
        self.check_download(user['导出按钮'], content)

    @allure.step("筛选品牌")
    def screen_brand(self, brand):
        self.is_click(user['品牌下拉框'])
        if brand == "Infinix":
            self.is_click(user['新增_下拉选项'], "1")
        elif brand == "itel":
            self.is_click(user['新增_下拉选项'], "2")
        elif brand == "TECNO":
            self.is_click(user['新增_下拉选项'], "3")
        else:
            self.is_click(user['品牌下拉框'])
        logging.info("筛选品牌：{}".format(brand))

    @allure.step("筛选大类粗")
    def screen_broadCoarse(self, broadCoarse):
        self.is_click(user['大类粗下拉框'])
        if broadCoarse == "功能机":
            self.is_click(user['新增_下拉选项'], "1")
        elif broadCoarse == "智能机":
            self.is_click(user['新增_下拉选项'], "2")
        else:
            self.is_click(user['大类粗下拉框'])
        logging.info("筛选大类粗：{}".format(broadCoarse))

    @allure.step("筛选大类细")
    def screen_broadFine(self, broadFine=None):
        self.is_click(user['大类细下拉框'])
        if broadFine == "低端SP" or broadFine == "功能机":
            self.is_click(user['新增_下拉选项'], "1")
        elif broadFine == "中端SP":
            self.is_click(user['新增_下拉选项'], "2")
        elif broadFine == "高端SP":
            self.is_click(user['新增_下拉选项'], "3")
        else:
            self.is_click(user['大类细下拉框'])
        logging.info("筛选大类细：{}".format(broadFine))

    @allure.step("筛选机型")
    def screen_mobileType(self, mobileType=None):
        self.readonly_input_text(user['机型输入框'], mobileType)
        sleep(1)
        a = self.find_elements(user['新增_下拉选项集'])
        b = []
        for i in range(len(a)):
            b.append(a[i].text)
        if mobileType in b:
            self.is_click(user['输入框下拉'], mobileType)
        elif mobileType not in b:
            self.is_click(user['输入框下拉（模糊）'])
        else:
            self.is_click(user['筛选框断言'])
        logging.info("筛选机型：{}".format(mobileType))

    @allure.step("筛选市场名")
    def screen_marketName(self, marketName=None):
        self.readonly_input_text(user['市场名输入框'], marketName)
        sleep(1)
        self.is_click(user['输入框下拉'], marketName)
        logging.info("筛选市场名：{}".format(marketName))

    @allure.step("筛选系列")
    def screen_series(self, series=None):
        self.readonly_input_text(user['系列输入框'], series)
        self.is_click(user['输入框下拉'], series)
        logging.info("筛选系列：{}".format(series))

    @allure.step("筛选项目名")
    def screen_projectName(self, screen_projectName=None):
        self.readonly_input_text(user['项目名输入框'], screen_projectName)
        self.is_click(user['输入框下拉'], screen_projectName)
        logging.info("筛选项目名：{}".format(screen_projectName))

    @allure.step("筛选状态")
    def screen_state(self, state):
        self.is_click(user['状态下拉框'])
        if state == "NP":
            self.is_click(user['新增_下拉选项'], "1")
        elif state == "MP":
            self.is_click(user['新增_下拉选项'], "2")
        elif state == "EOL":
            self.is_click(user['新增_下拉选项'], "3")
        elif state == "END":
            self.is_click(user['新增_下拉选项'], "4")
        else:
            self.is_click(user['状态下拉框'])
        logging.info("筛选状态：{}".format(state))

    @allure.step("筛选来源")
    def screen_source(self, source=None):
        self.is_click(user['来源下拉框'])
        if source == "数仓":
            self.is_click(user['新增_下拉选项'], "1")
        elif source == "自建":
            self.is_click(user['新增_下拉选项'], "2")
        else:
            self.is_click(user['来源下拉框'])
        logging.info("筛选来源：{}".format(source))

    @allure.step("筛选供应类型")
    def screen_supplyType(self, supplyType=None):
        self.is_click(user['供应类型下拉框'])
        if supplyType == "自研":
            self.is_click(user['新增_下拉选项'], "1")
        elif supplyType == "外购":
            self.is_click(user['新增_下拉选项'], "2")
        else:
            self.is_click(user['供应类型下拉框'])
        logging.info("筛选供应类型：{}".format(supplyType))

    @allure.step("筛选--查询")
    def screen_inquire(self):
        self.is_click(user['查询按钮'])
        logging.info("筛选查询成功")

    @allure.step("返回筛选条件数量，用做断言")
    def screen_count(self):
        return self.element_text(user['筛选数量'])

    @allure.step("筛选--重置")
    def screen_reset(self):
        self.is_click(user['重置按钮'])
        logging.info("筛选重置")

    @allure.step("筛选--取消")
    def screen_cancel(self):
        self.is_click(user['取消按钮'])
        logging.info("筛选取消")

    @allure.step("获取单机头BOM协作第一列内容")
    def get_mobileTypeList(self, num):
        """
        获取机型列表
        @return:返回文本及索引位置;
        """
        info = self.find_elements(user['列表第n列'], num)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    @allure.step("断言筛选后，列表展示的结果")
    def assert_screen_result(self, *content, num):
        """
        断言筛选机型后，页面表格内容是否正确
        :param content: 需要，可以一次传入多个
        """
        self.scroll_into_view(user['筛选结果断言'], "更新人")
        try:
            contents = self.get_mobileTypeList(num)
            assert set(content) <= set(contents)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            logging.error('断言失败，选项值不包含：{}'.format(content))
            # raise

    @allure.step("筛选结果为空断言")
    def screen_result_null(self):
        return self.element_text(user['筛选结果(无数据)'])

    @allure.step("点击指定行编辑按钮")
    def update_button(self, updateOne_name, num):
        line = self.find_elements(user['列表第n列'], num)
        name = []  # 取出列表第n列的所有文本
        for i in range(len(line)):
            name.append(line[i].text)
        if updateOne_name in name:
            lineNum = name.index(updateOne_name) + 1  # 取到所传参数所在行号
            Nxpath = user['编辑'][1].replace('variable', str(lineNum))
            self.force_click(Nxpath, xpath_js=True)  # 将行号c替换到xpath中进行相关操作
            logging.info('点击指定行编辑按钮成功')
            return str(lineNum), Nxpath

    @allure.step("编辑某列内容")
    def update_something(self, line, option):
        Nxpath = user['编辑第n列'][1].replace('variable', str(line))
        self.force_click(Nxpath, xpath_js=True)  # 点击展开某列下拉选项
        sleep()
        eles = self.find_elements(user['编辑下拉选项集'])
        optionList = []
        for i in range(len(eles)):
            optionList.append(eles[i].text)
        if option in optionList:
            index = optionList.index(option) + 1
            self.is_click(user['编辑下拉选项'],str(index))
            logging.info('编辑成功，修改为{}'.format(option))
        else:
            logging.info("无此选项，退出编辑")

    @allure.step("编辑保存")
    def update_save(self):
        Nxpath = user['编辑保存'][1]
        self.force_click(Nxpath, xpath_js=True)
        logging.info("编辑保存成功")
        sleep(2)

    @allure.step("返回编辑保存成功警示文本，用做断言")
    def update_save_hint(self):
        return self.element_text(user["断言（保存成功）"])

    @allure.step("点击指定行删除按钮")
    def delete_button(self,updateOne_name,num):
        line = self.find_elements(user['列表第n列'], num)
        print("line0",line)
        name = []  # 取出列表第n列的所有文本
        for i in range(len(line)):
            name.append(line[i].text)
        if updateOne_name in name:
            lineNum = name.index(updateOne_name) + 1  # 取到所传参数所在行号
            Nxpath = user['删除'][1].replace('variable', str(lineNum))
            print('Nxpath',Nxpath)
            self.force_click(Nxpath, xpath_js=True)  # 将行号c替换到xpath中进行相关操作
            logging.info('点击指定行删除按钮成功')
            return str(lineNum), Nxpath

    @allure.step("返回删除保存成功警示文本，用做断言")
    def delete_hint(self):
        hint = self.element_text(user["断言（保存成功）"])
        print(f"删除{hint}")
        return hint

    @allure.step("删除测试数据")
    def delete_testData(self, drivers,**kwargs):
        user = ModelDatabase(drivers)
        user.screen_button()  # 点击筛选按钮，弹出筛选框
        user.screen_brand(kwargs["brand"])  # 选择品牌
        user.screen_broadCoarse(kwargs["broadCoarse"])  # 选择大类粗
        user.screen_mobileType(kwargs["mobileType"])  # 输入机型
        user.screen_marketName(kwargs["marketName"])  # 输入市场名
        user.screen_series(kwargs["series"])  # 输入系列
        user.screen_projectName(kwargs["projectName"])  # 输入项目名
        user.screen_state(kwargs["state"])  # 选择状态
        user.screen_source(kwargs["source"])  # 选择来源
        user.screen_supplyType(kwargs["supplyType"])  # 选择供应类型
        user.screen_inquire()  # 点击查询按钮
        user.assert_screen_result("隆江", num=22)
        logging.info('列表操作，前置条件过滤完成')
        user.delete_button("隆江", num=22)  # 点击指定行删除按钮

    @allure.step("造测试数据并筛选")
    def insert_testData(self, drivers):
        user = ModelDatabase(drivers)
        user.append_button()  # 点击新增按钮
        user.source_option('数仓')  # 选择来源
        user.supplyType_option('自研')  # 选择供应类型
        user.brand_option('itel')  # 选择品牌
        user.broadCoarse_option('智能机')  # 选择大类粗
        user.series_option('A')  # 选择系列
        user.projectName_option('S11')  # 填选项目名
        user.memoryVersion('64+4')  # 输入内存版本
        user.network_option('5G')  # 选择网络制式
        user.marketName('India')  # 输入市场名
        user.color('半透黑')  # 选择颜色
        user.save_color()  # 保存颜色
        user.state_option('MP')  # 选择状态
        user.save_button("正例")  # 新增保存完成
        user.screen_button()  # 点击筛选按钮，弹出筛选框
        user.screen_brand("itel")  # 选择品牌
        user.screen_broadCoarse("智能机")  # 选择大类粗
        user.screen_mobileType("S11 64+4")  # 输入机型
        user.screen_marketName("India")  # 输入市场名
        user.screen_series("A")  # 输入系列
        user.screen_projectName("S11")  # 输入项目名
        user.screen_state("MP")  # 选择状态
        user.screen_source("数仓")  # 选择来源
        user.screen_supplyType("自研")  # 选择供应类型
        user.screen_inquire()  # 点击查询按钮
        user.assert_screen_result("隆江", num=22)
        logging.info('列表操作，前置条件过滤完成')

    @allure.step("造测试数据")
    def insert_testData1(self, drivers):
        """大类细：中端SP"""
        user = ModelDatabase(drivers)
        user.goto_tab('产品信息')  # 切换到产品信息tab页
        user.append_button()  # 点击新增按钮
        user.source_option('数仓')  # 选择来源
        user.supplyType_option('自研')  # 选择供应类型
        user.brand_option('itel')  # 选择品牌
        user.broadCoarse_option('智能机')  # 选择大类粗
        user.broadFine_option('中端SP')  # 选择大类细
        user.series_option('A')  # 选择系列
        user.projectName_option('S11')  # 填选项目名
        user.memoryVersion('64+4')  # 输入内存版本
        user.network_option('5G')  # 选择网络制式
        user.marketName('India')  # 输入市场名
        user.color('半透黑')  # 选择颜色
        user.save_color()  # 保存颜色
        user.state_option('MP')  # 选择状态
        user.save_button("正例")  # 新增保存完成
        sleep(2)



if __name__ == '__main__':
    pass
