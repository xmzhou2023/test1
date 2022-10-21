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
user = Element(pro_name, object_name)


class DimensionManage(Base):
    """维度管理"""

    @allure.step("前往标签页")
    def goto_labelPage(self,labelPage):
        self.is_click(user['标签页'],labelPage)
        logging.info("前往标签页：{}".format(labelPage))
        sleep(1)
        listNum = self.return_listNum()
        sql = SQLAssert("DRP", "test")
        sql.assert_sql_count(listNum,"select count(*) from dc_meta_item where meta_code in (SELECT meta_code FROM dc_meta where name_zh = '{}')".format(labelPage))


    @allure.step("获取列表是数据条数")
    def return_listNum(self):
        sleep(1)
        txt = self.element_text(user['列表数据数量'])
        b = re.findall(" (.*?) ", txt)[0]
        logging.info("列表数据量:{}条".format(b))
        return int(b)

    @allure.step("搜索功能")
    def query_value(self,value):
        self.readonly_input_text(user['查询搜索框'],value)
        self.is_click(user['列表数据数量'])
        listNum = self.return_listNum()
        if listNum == 0:
            txt = self.element_text(user['暂无数据 断言'])
            assert txt == "暂无数据",logging.warning("断言失败，列表有数据")
            logging.info("查询:{},结果为空".format(listNum))
        else:
            logging.info("查询到数据{}条".format(listNum))

    @allure.step("新增按钮")
    def add_button(self):
        self.is_click(user['新增按钮'])
        logging.info("点击新增按钮")

    @allure.step("返回 数据所在行号")
    def return_rowNum(self,ID=None):
        txt = self.find_elements(user['列表某列数据'],str(2))
        b = []
        for i in range(len(txt)):
            b.append(txt[i].text)
        if ID in b:
            rowNum = b.index(ID) +1
            logging.info("{}所在行：{}行".format(ID,rowNum))
            return str(rowNum)
        elif ID is None:
            logging.info("返回行号：1 ")
            return str(1)

    @allure.step("输入文本")
    def input_testdata(self, coding=None,name_Zh=None,name_En=None):
        rowNum = self.return_rowNum()
        self.readonly_input_text(user['编码输入'], coding, str(rowNum))
        self.readonly_input_text(user['名称（Zh）输入'], name_Zh, str(rowNum))
        self.readonly_input_text(user['名称（En）输入'], name_En, str(rowNum))
        logging.info("输入 编码：{}，名称（Zh）：{}，名称（En）：{}".format(coding,name_Zh,name_En))

    @allure.step("编辑保存")
    def update_save(self):
        Nxpath = user['编辑保存'][1]
        self.force_click(Nxpath, xpath_js=True)
        logging.info("编辑保存成功")
        sleep(2)

    @allure.step("保存按钮")
    def save_button(self):
        Nxpath = user['列表 保存按钮'][1]
        self.force_click(Nxpath, xpath_js=True)
        sleep(1)
        txt = self.element_text(user['错误提示'])
        if txt == "参数错误" or txt[0:2] == "失败":
            Nxpath1 = user['列表 取消按钮'][1]
            self.force_click(Nxpath1, xpath_js=True)
            logging.info("保存失败，失败原因：{},取消新增".format(txt))
        else:
            logging.info("保存成功")

    @allure.step("清空测试数据")
    def clear_testdata(self, dimensionality,name_zh):
        user = SQL("DRP", "test")
        user.delete_db(
            "DELETE from dc_meta_item where meta_code in (SELECT meta_code FROM dc_meta where name_zh = '{}') and name_zh ='{}';".format(dimensionality,name_zh))
        logging.info("清空测试数据")

    @allure.step("数据库断言")
    def assert_sql(self, dimensionality, name_zh, type = None):
        sql = SQLAssert("DRP", "test")
        listNum = self.return_listNum()
        if type != "反例":
            sql.assert_sql_count(listNum,
                "select count(name_zh) from dc_meta_item where meta_code in (SELECT meta_code FROM dc_meta where name_zh = '{}') and name_zh ='{}' or name_en ='{}';".format(dimensionality,name_zh,name_zh))
        else:
            sql.assert_sql_count(0,
                "select count(name_zh) from dc_meta_item where meta_code in (SELECT meta_code FROM dc_meta where name_zh = '{}') and name_zh ='{}' or name_en ='{}';".format(dimensionality,name_zh,name_zh))













if __name__ == '__main__':
    pass