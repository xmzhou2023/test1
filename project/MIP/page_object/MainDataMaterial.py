import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import random
import string
import re

object_name = os.path.basename(__file__).split('.')[0]
data = Element(pro_name, object_name)


class MainDataMaterial(Base):
    """主数据-物料主数据"""

    @allure.step("输入物料编码查询条件")
    def input_itemCode(self, itemL=None, itemR=None, scene=None):
        """多选功能没用"""
        if scene is None:
            self.input_text(data['物料编码文本框 左'], itemL)
            self.input_text(data['物料编码文本框 右'], itemR)
            logging.info("输入物料编码 {}到{}".format(itemL, itemR))
        elif scene == "单一物料查询":
            self.input_text(data['物料编码文本框 左'], itemL)
            logging.info("输入物料编码 {}".format(itemL))
        elif scene == "到某一物料截止":
            self.input_text(data['物料编码文本框 右'], itemR)
            logging.info("输入物料编码 0到{}".format(itemR))

    @allure.step("选择类目")
    def choice_category(self, level1=None, level2=None):
        if level1 is not None and level2 is None:
            self.is_click(data['类目下拉框 左'])
            self.is_click(data['选择下拉项'], level1)
            logging.info("选择一级类目：{}".format(level1))
        elif level1 is None:
            try:
                self.is_click(data['类目下拉框 右'])
                txt = self.element_text(data['下拉列表无数据'])
                assert txt == "无数据", logging.warning("断言失败")
                logging.info("断言成功，未选择一级类目，无二级类目可选")
            except:
                self.is_click(data['类目下拉框 右'])
        elif level1 and level2 is not None:
            self.is_click(data['类目下拉框 左'])
            self.is_click(data['选择下拉项'], level1)
            self.is_click(data['类目下拉框 右'])
            self.is_click(data['选择下拉项'], level2)
            logging.info("选择一级类目：{},二级类目{}".format(level1, level2))

    @allure.step("选择品牌")
    def choice_brand(self, brand):
        self.is_click(data['品牌下拉'])
        self.is_click(data['选择下拉项'], brand)
        logging.info("选择品牌：{}".format(brand))

    @allure.step("选择上下架状态")
    def choice_statue(self, statue):
        self.is_click(data['上下架状态下拉'])
        if statue == "已上架":
            self.is_click(data['选择下拉项'], statue)
        else:
            self.is_click(data['选择下拉项'], statue)
        logging.info("选择上下架状态：{}".format(statue))

    @allure.step("展开 高级搜索")
    def button_spread(self):
        txt = self.element_text(data['展开 按钮'])
        if txt == "展开":
            self.is_click(data['展开 按钮'])
            logging.info("展开 高级搜索")
            sleep(1)
        else:
            self.is_click(data['收起 按钮'])
            logging.info("收起 高级搜索")

    @allure.step("输入物料描述")
    def input_itemDescribe(self, itemDescribe):
        self.input_text(data['物料描述文本框'], itemDescribe)
        logging.info("输入物料描述：{}".format(itemDescribe))

    @allure.step("输入类别")
    def input_itemType(self, itemType):
        self.input_text(data['类别文本框'], itemType)
        logging.info("输入物料类别：{}".format(itemType))

    @allure.step("输入海关编码")
    def input_customsCode(self, customsCodeL, customsCodeR):
        """暂未使用"""
        self.input_text(data['海关编码 左'], customsCodeL)
        self.input_text(data['海关编码 右'], customsCodeR)
        logging.info("输入海关编码 {}到{}".format(customsCodeL, customsCodeR))

    @allure.step("输入旧物料编码")
    def input_oldItemCode(self, oldItemCodeL=None, oldItemCodeR=None, scene=None):
        if scene is None:
            self.input_text(data['旧物料编码 左'], oldItemCodeL)
            self.input_text(data['旧物料编码 右'], oldItemCodeR)
            logging.info("输入旧物料编码 {}到{}".format(oldItemCodeL, oldItemCodeR))
        elif scene == "单一物料查询":
            self.input_text(data['旧物料编码 左'], oldItemCodeL)
            logging.info("输入旧物料编码 {}".format(oldItemCodeL))
        elif scene == "到某一物料截止":
            self.input_text(data['旧物料编码 右'], oldItemCodeR)
            logging.info("输入旧物料编码 0 到{}".format(oldItemCodeR))

    @allure.step("输入型号")
    def input_itemModel(self, itemModel):
        self.input_text(data['型号文本框'], itemModel)
        logging.info("输入物料型号：{}".format(itemModel))

    @allure.step("选择年")
    def choice_year(self, year):
        self.is_click(data['header年'])
        sleep(1)
        fristyear = self.element_text(data['年列表 第一年'])
        lastyear = self.element_text(data['年列表 最后一年'])
        if year < fristyear:
            for i in  range(3):
                fristyear1 = self.element_text(data['年列表 第一年'])
                lastyear1 = self.element_text(data['年列表 最后一年'])
                if fristyear1 <= year <= lastyear1:
                    self.is_click(data['选择年'], year)
                    logging.info("选择年{}".format(year))
                    break
                else:
                    self.is_click(data['选择 前一年'])
        elif year > lastyear:
            for i in  range(3):
                fristyear1 = self.element_text(data['年列表 第一年'])
                lastyear1 = self.element_text(data['年列表 最后一年'])
                if fristyear1 <= year <= lastyear1:
                    self.is_click(data['选择年'], year)
                    logging.info("选择年{}".format(year))
                else:
                    self.is_click(data['选择 后一年'])
        elif fristyear <= year <= lastyear:
            self.is_click(data['选择年'], year)

    @allure.step("输入创建时间")
    def input_createTime(self, createTimeL=None, createTimeR=None, scene=None):
        if scene is None:
            self.is_click(data['创建时间 左'])
            time1 = createTimeL.split("-")
            time2 = createTimeR.split("-")
            self.choice_year(time1[0])
            self.is_click(data['选择月'], time1[1])
            self.is_click(data['选择 日期'], time1[2])

            self.is_click(data['创建时间 右'])
            self.choice_year(time2[0])
            self.is_click(data['选择月'], time2[1])
            self.is_click(data['选择 日期'], time2[2])
            logging.info("选择创建日期：{}到{}".format(createTimeL, createTimeR))
        if scene == "单一日期查询":
            self.is_click(data['创建时间 左'])
            time1 = createTimeL.split("-")
            self.choice_year(time1[0])
            self.is_click(data['选择月'], time1[1])
            self.is_click(data['选择 日期'], time1[2])
            logging.info("选择创建时间：{}".format(createTimeL))
        if scene == "到某一日期截止":
            time2 = createTimeR.split("-")
            self.is_click(data['创建时间 右'])
            self.choice_year(time2[0])
            self.is_click(data['选择月'], time2[1])
            self.is_click(data['选择 日期'], time2[2])
            logging.info("选择创建日期：截止到{}".format(createTimeR))

    @allure.step("点击查询按钮")
    def button_query(self):
        self.is_click(data['查询 按钮'])
        logging.info("点击查询按钮")
        sleep(1)

    @allure.step("点击清空按钮 清空查询条件")
    def button_empty(self):
        self.is_click(data['清空 按钮'])
        logging.info("点击清空按钮")
        sleep(1)

    @allure.step("获取列表数据数量，用做断言")
    def get_listNum(self):
        txt = self.element_text(data['获取列表数量'])
        num = re.findall(" (.*?) ", txt)[0]
        logging.info("列表数据数量：{}".format(num))
        return int(num)

    @allure.step("查询数据库 用做断言")
    def get_sqlResult(self, sql):
        user = SQL("MIP", "test")
        num = user.query_db(sql)
        num1 = [item[key] for item in num for key in item]
        logging.info("查询数据库数量：{}".format(num1[0]))
        return num1[0]

    @allure.step("返回列表无数据文本 用做断言")
    def return_txt(self):
        txt = self.element_text(data['暂无数据'])
        return txt

    @allure.step("点击编辑物料编码")
    def click_itemCode(self,itemcode):
        Npath = data['物料编码(第一行)'][1]
        Npath1 = Npath.replace('variable', str(itemcode), 1)
        print(Npath1)
        self.force_click(Npath1, xpath_js=True)
        logging.info("点击物料编码")
        sleep(1)

    @allure.step("返回物料主数据页面")
    def return_itemPage(self):
        self.is_click(data['主数据页面'])
        logging.info("返回物料主数据页面")

    @allure.step("点击编辑按钮")
    def button_edit(self):
        self.is_click(data['编辑按钮(第一行)'])
        logging.info("点击编辑按钮")

    @allure.step("点击预览按钮")
    def button_preview(self):
        self.is_click(data['预览按钮(第一行)'])
        logging.info("点击预览按钮")

    @allure.step("切换新窗口")
    def checkout_newWindow(self):
        windows = self.driver.window_handles  # 获取该会话所有的句柄
        self.driver.switch_to.window(windows[-1])  # 跳转到最新的句柄
        logging.info("切换至新窗口")

    @allure.step("关闭新窗口")
    def close_newWindow(self):
        windows = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(windows[0])  # 切换回百度首页
        logging.info("关闭新窗口")

    @allure.step("勾选主数据")
    def select_itemData(self,selectorMode=None):
        if selectorMode is None:
            self.is_click(data['复选框(第一行)'])
            logging.info("勾选主数据")
        else:
            self.is_click(data['全选'])
            logging.info("全选主数据")

    @allure.step("上/下架")
    def on_off_Shelves(self):
        self.DivRolling(data['横向滚动条div'])
        txt = self.element_text(data['获取上/下架状态'])
        if txt == "已上架":
            self.is_click(data['下架 按钮'])
            result = self.element_text(data['获取上/下架状态'])
            assert result == "已下架",logging.warning("断言失败，主数据下架失败")
            logging.info("断言成功，主数据下架成功")
        else:
            self.is_click(data['上架 按钮'])
            result = self.element_text(data['获取上/下架状态'])
            assert result == "已上架", logging.warning("断言失败，主数据上架失败")
            logging.info("断言成功，主数据上架成功")




if __name__ == '__main__':
    pass
