import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import re
import random
import string

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class Optim(Base):
    """集成数据管理"""


    @allure.step("菜单搜索框")
    def input_menu(self, type, menu):
        try:
            if type == "精确搜索":
                self.input_text(user['菜单查询输入框'], menu)
                result = self.element_text(user['菜单列表'])
                assert menu == result, logging.warning("断言失败,查询结果{} != {}".format(result,menu))
                logging.info("断言成功,查询结果{} = {}".format(result,menu))
            elif type == "模糊搜索":
                before = self.find_elements(user['菜单列表'])
                self.input_text(user['菜单查询输入框'], menu)
                after = self.find_elements(user['菜单列表'])
                assert len(before) > len(after),logging.warning("断言失败")
                logging.info("断言成功")
        except:
            self.input_text(user['菜单查询输入框'], menu)
            result = self.element_text(user['菜单列表 无数据'])
            assert result == "暂无数据...",logging.warning("断言失败")
            logging.info("断言成功")

    @allure.step("清空菜单搜索框")
    def clear_menuInputBox(self):
        self.is_click(user['菜单查询输入框'])
        self.is_click(user['菜单输入框 清除按钮'])
        logging.info("菜单输入框 清空完成")


    @allure.step("返回列表行号")
    def retrun_listRowNum(self,locator,value):
        lis = self.find_elements(locator)
        Nlis = []
        for i in range(len(lis)):
            Nlis.append(lis[i].text)
        if value in Nlis:
            rowNum = Nlis.index(value) + 1  # 取到所传参数所在行号
            return rowNum

    @allure.step("前往指定菜单页")
    def goto_menu(self, menu):
        rowNum = self.retrun_listRowNum(user['菜单列表'],menu)
        self.is_click(user['菜单列表 进入菜单'],str(rowNum))
        txt = self.element_text(user['数据名称 用做断言'])
        assert txt == menu, logging.warning("断言失败，数据名称'{}'与菜单'{}'不一致".format(txt,menu))
        logging.info("断言成功，数据名称'{}'与菜单'{}'一致".format(txt, menu))

    @allure.step("选择品牌")
    def choose_brand(self, brand):
        self.is_click(user['品牌下拉'])
        if brand == "Infinix":
            self.is_click(user['下拉选项'],"1")
        elif brand == "itel":
            self.is_click(user['下拉选项'],"2")
        elif brand == "TECNO":
            self.is_click(user['下拉选项'],"3")
        else:
            logging.info("品牌输入有误")
        logging.info("选择品牌：{}".format(brand))

    @allure.step("选择汇总期间")
    def choose_monthOrWeek(self, value):
        txt = self.element_text(user['时段'])
        if txt != value:
            self.is_click(user['汇总期间'])
            txt1 = self.element_text(user['时段'])
            assert txt1 == value, logging.warning("断言失败")
            logging.info("断言成功，选择汇总期间 = {}".format(value))
        else:
            logging.info("选择汇总期间 完成")

    @allure.step("选择汇总期间 时段")
    def choose_timeFrame(self, star, end):
        txt = self.element_text(user['时段'])
        starLis = star.split('-')
        endLis = end.split('-')
        if txt == "月时段":
            self.is_click(user['选择时段'])  # 展开日期选项
            starYear = self.element_text(user['获取月时段左年 文本'])
            starYearLis = starYear.split(' ')
            endYear = self.element_text(user['获取月时段右年 文本'])
            endYearLis = endYear.split(' ')
            if starLis[0] < starYearLis[0] or endYearLis[0] < endLis[0]:
                year = self.element_text(user['获取月时段左年 文本'])
                yserLis = year.split(' ')
                year1 = self.element_text(user['获取月时段右年 文本'])
                yserLis1 = year1.split(' ')
                if yserLis[0] == starLis[0]:
                    self.is_click(user['月时段选项 左月'],starLis[1])
                    logging.info("开始年：{} 月:{}".format(starLis[0],starLis[1]))
                else:
                    for i in range(1,10):
                        self.is_click(user['月时段选项 左年'])
                        year = self.element_text(user['获取月时段左年 文本'])
                        yserLis = year.split(' ')
                        if yserLis[0] == starLis[0]:
                            logging.info("开始年:{}".format(yserLis[0]))
                            break
                    self.is_click(user['月时段选项 左月'],starLis[1])
                    logging.info("开始月:{}".format(starLis[1]))
                if yserLis1[0] == endLis[0]:
                    self.is_click(user['月时段选项 右月'],str(endLis[1]))
                    logging.info("开始年：{} 月:{}".format(endLis[0],endLis[1]))
                else:
                    for i in range(1,10):
                        self.is_click(user['月时段选项 右年'])
                        year1 = self.element_text(user['获取月时段右年 文本'])
                        yserLis1 = year1.split(' ')
                        if yserLis1[0] == endLis[0]:
                            logging.info("结束年:{}".format(yserLis1[0]))
                            break
                    self.is_click(user['月时段选项 右月'],str(endLis[1]))
                    logging.info("结束月:{}".format(endLis[1]))
            elif starLis[0] == endLis[0]:
                if starLis[0] == starYearLis[0]:
                    self.is_click(user['月时段选项 左月'], str(starLis[1]))
                    self.is_click(user['月时段选项 左月'], str(endLis[1]))
                    logging.info("选择开始年：{} 月：{}，结束年：{} 月：{}".format(starLis[0],starLis[1],starLis[0],endLis[1]))
                elif endLis[0] == endYearLis[0]:
                    self.is_click(user['月时段选项 右月'], str(starLis[1]))
                    self.is_click(user['月时段选项 右月'], str(endLis[1]))
                    logging.info("选择开始年：{} 月：{}，结束年：{} 月：{}".format(starLis[0],starLis[1],starLis[0],endLis[1]))
        elif txt == "周时段":
            self.is_click(user['周时段 左周'])
            year = self.element_text(user['获取周时段 title年文本'])
            self.is_click(user['周时段 title年'],str(year))
            self.is_click(user['周时段 年选项'],starLis[0])
            self.is_click(user['周时段 月选项'],starLis[1])
            self.is_click(user['周时段 周选项'],starLis[2])
            logging.info("开始 年：{}，月：{}，日{}".format(starLis[0],starLis[1], starLis[2]))
            self.is_click(user['周时段 右周'])
            endyear = self.element_text(user['获取周时段 title年文本'])
            self.is_click(user['周时段 title年'],str(endyear))
            self.is_click(user['周时段 年选项'],endLis[0])
            self.is_click(user['周时段 月选项'],endLis[1])
            self.is_click(user['周时段 周选项'],endLis[2])
            logging.info("结束 年：{}，月：{}，日{}".format(endLis[0],endLis[1], endLis[2]))

    @allure.step("选择区域")
    def choose_area(self,level=None,area=None):
        self.is_click(user['区域输入框'])
        self.input_text(user['区域输入框'], area)
        try:
            if area == "全部区域":
                self.is_click(user['区域树-全部区域'])
            elif level == "地区部":
                self.is_click(user['区域树-全部区域'],area)
            elif level == "大区":
                self.is_click(user['区域树-大区层级'],area)
            elif level == "国家":
                self.is_click(user['区域树-国家层级'],area)
            logging.info("选择{} : {}".format(level, area))
        except:
            self.move_house(user['数据名称 用做断言'])
            logging.info("输入国家有误")

    @allure.step("选择匹配状态")
    def choose_matchState(self,state):
        self.is_click(user['匹配状态'])
        if state == "成功":
            self.is_click(user['下拉选项'],"1")
        elif state == "失败":
            self.is_click(user['下拉选项'],"2")
        else:
            logging.info("匹配状态输入有误")
        logging.info("选择匹配状态：{}".format(state))

    @allure.step("输入机型")
    def choose_inputMobleType(self,mobileType):
        self.is_click(user['机型输入框'])
        self.input_text(user['机型输入框'],mobileType)
        a = self.find_elements(user['下拉选项集'])
        b = []
        for i in range(len(a)):
            b.append(a[i].text)
        if mobileType in b:
            self.is_click(user['输入框下拉'], mobileType)
        elif mobileType not in b:
            self.is_click(user['下拉选项'],str(1))
        else:
            self.is_click(user['机型输入框'])
        logging.info("输入机型：{}".format(mobileType))

    @allure.step("输入市场名")
    def choose_markName(self,markname):
        self.is_click(user['市场名输入框'])
        self.input_text(user['市场名输入框'],markname)
        a = self.find_elements(user['下拉选项集'])
        b = []
        for i in range(len(a)):
            b.append(a[i].text)
        if markname in b:
            self.is_click(user['输入框下拉'], markname)
        elif markname not in b:
            self.is_click(user['下拉选项'],str(1))
        else:
            self.is_click(user['市场名输入框'])
        logging.info("输入市场名：{}".format(markname))

    @allure.step("选择状态")
    def choose_state(self, all= None, option= None):
        self.is_click(user['状态下拉'])
        if all is not None:
            self.hover(user['下拉选项'],str(1))
            self.is_click(user['全选'])
            logging.info("状态全选")
        else:
            if option == "NP":
                self.is_click(user['下拉选项'],str(2))
                logging.info("状态选择{}".format(option))
            elif option == "MP":
                self.is_click(user['下拉选项'],str(3))
                logging.info("状态选择{}".format(option))
            elif option == "EOL":
                self.is_click(user['下拉选项'],str(4))
                logging.info("状态选择{}".format(option))
            elif option == "END":
                self.is_click(user['下拉选项'],str(5))
                logging.info("状态选择{}".format(option))
            else:
                logging.info("状态输入有误")
            logging.info("选择状态：{}".format(option))

    @allure.step("点击查询按钮")
    def query_button(self):
        self.is_click(user['查询按钮'])
        logging.info("点击查询按钮")
        sleep(5)



    @allure.step("查询数据库 用做断言")
    def SQL_assert(self, timeFrame=None, country=None, time1=None, time2=None, brand=None, modle=None, mark=None):
        user = SQL("DRP", "test")
        if timeFrame is None and country is not None:
            num = user.query_db("select count(item) from ed_period_data_stat where brand_code = '{}' and model_code "
                                "= '{}' and item = '{}' and period BETWEEN '{}' and '{}' and period "
                                "not like '%W%' and data_type = '1' and country_code in (SELECT code from bd_country "
                                "where name_zh = '{}')".format(brand, modle, mark, time1, time2, country))
            for item in num:
                for k, v in item.items():
                    logging.info("获取数据库 数据数量:{}".format(v))
                    return str(v)
        elif timeFrame is not None and country is not None:
            num = user.query_db("select count(item) from ed_period_data_stat where brand_code = '{}' and model_code "
                                "= '{}' and item = '{}' and period BETWEEN '{}' and '{}' and period "
                                "like '%W%' and data_type = '1' and country_code in (SELECT code from bd_country "
                                "where name_zh = '{}')".format(brand, modle, mark, time1, time2, country))
            for item in num:
                for k, v in item.items():
                    logging.info("获取数据库 数据数量:{}".format(v))
                    return str(v)
        elif timeFrame is None and country is None:
            num = user.query_db("select count(item) from ed_period_data_stat where brand_code = '{}' and model_code "
                                "= '{}' and item = '{}' and period BETWEEN '{}' and '{}' and period "
                                "like '%W%' and data_type = '1'".format(brand, modle, mark, time1, time2))
            for item in num:
                for k, v in item.items():
                    logging.info("获取数据库 数据数量:{}".format(v))
                    return str(v)

    @allure.step("返回页面列表数据数量")
    def retrun_listNum(self):
        a = self.element_text(user['列表数据统计'])
        b = re.findall(" (.*?) ", a)[0]
        return b

    @allure.step("点击重置按钮")
    def reset_button(self):
        self.is_click(user['重置按钮'])
        logging.info("点击重置按钮")
        sleep(2)

    @allure.step("点击手动拉取按钮")
    def pull_button(self):
        self.is_click(user['手动拉取按钮'])
        logging.info("点击手动拉取按钮")
        sleep(2)

    @allure.step("手动拉取表单 更新期间")
    def choice_period(self, value):
        txt = self.element_text(user['拉取表单 获取时段'])
        if txt != value:
            self.is_click(user['拉取表单 更新期间'])
            txt1 = self.element_text(user['value'])
            assert txt1 == value, logging.warning("断言失败")
            logging.info("断言成功，选择更新期间 = {}".format(value))
        else:
            logging.info("选择更新期间 完成")

    @allure.step("拉取表单选择更新期间 时段")
    def chooseForm_timeFrame(self, star, end):
        txt = self.element_text(user['拉取表单 获取时段'])
        starLis = star.split('-')
        endLis = end.split('-')
        if txt == "月时段":
            self.is_click(user['拉取表单 选择时段'])  # 展开日期选项
            starYear = self.element_text(user['获取月时段左年 文本'])
            starYearLis = starYear.split(' ')
            endYear = self.element_text(user['获取月时段右年 文本'])
            endYearLis = endYear.split(' ')
            if starLis[0] < starYearLis[0] or endYearLis[0] < endLis[0]:
                year = self.element_text(user['获取月时段左年 文本'])
                yserLis = year.split(' ')
                year1 = self.element_text(user['获取月时段右年 文本'])
                yserLis1 = year1.split(' ')
                if yserLis[0] == starLis[0]:
                    self.is_click(user['月时段选项 左月'],starLis[1])
                    logging.info("开始年：{} 月:{}".format(starLis[0],starLis[1]))
                else:
                    for i in range(1,10):
                        self.is_click(user['月时段选项 左年'])
                        year = self.element_text(user['获取月时段左年 文本'])
                        yserLis = year.split(' ')
                        if yserLis[0] == starLis[0]:
                            logging.info("开始年:{}".format(yserLis[0]))
                            break
                    self.is_click(user['月时段选项 左月'],starLis[1])
                    logging.info("开始月:{}".format(starLis[1]))
                if yserLis1[0] == endLis[0]:
                    self.is_click(user['月时段选项 右月'],str(endLis[1]))
                    logging.info("开始年：{} 月:{}".format(endLis[0],endLis[1]))
                else:
                    for i in range(1,10):
                        self.is_click(user['月时段选项 右年'])
                        year1 = self.element_text(user['获取月时段右年 文本'])
                        yserLis1 = year1.split(' ')
                        if yserLis1[0] == endLis[0]:
                            logging.info("结束年:{}".format(yserLis1[0]))
                            break
                    self.is_click(user['月时段选项 右月'],str(endLis[1]))
                    logging.info("结束月:{}".format(endLis[1]))
            elif starLis[0] == endLis[0]:
                if starLis[0] == starYearLis[0]:
                    self.is_click(user['月时段选项 左月'], str(starLis[1]))
                    self.is_click(user['月时段选项 左月'], str(endLis[1]))
                    logging.info("选择开始年：{} 月：{}，结束年：{} 月：{}".format(starLis[0],starLis[1],starLis[0],endLis[1]))
                elif endLis[0] == endYearLis[0]:
                    self.is_click(user['月时段选项 右月'], str(starLis[1]))
                    self.is_click(user['月时段选项 右月'], str(endLis[1]))
                    logging.info("选择开始年：{} 月：{}，结束年：{} 月：{}".format(starLis[0],starLis[1],starLis[0],endLis[1]))
        elif txt == "周时段":
            self.is_click(user['周时段 左周'])
            year = self.element_text(user['获取周时段 title年文本'])
            self.is_click(user['周时段 title年'],str(year))
            self.is_click(user['周时段 年选项'],starLis[0])
            self.is_click(user['周时段 月选项'],starLis[1])
            self.is_click(user['周时段 周选项'],starLis[2])
            logging.info("开始 年：{}，月：{}，日{}".format(starLis[0],starLis[1], starLis[2]))
            self.is_click(user['周时段 右周'])
            endyear = self.element_text(user['获取周时段 title年文本'])
            self.is_click(user['周时段 title年'],str(endyear))
            self.is_click(user['周时段 年选项'],endLis[0])
            self.is_click(user['周时段 月选项'],endLis[1])
            self.is_click(user['周时段 周选项'],endLis[2])
            logging.info("结束 年：{}，月：{}，日{}".format(endLis[0],endLis[1], endLis[2]))

    @allure.step("手动拉取表单 确认按钮")
    def notarize_button(self):
        self.is_click(user['拉取表单 确认按钮'])
        logging.info("点击拉取表单 确认按钮")

    @allure.step("点击下载按钮")
    def download_button(self):
        self.is_click(user['下载按钮'])
        logging.info("点击下载按钮")

if __name__ == '__main__':
    pass