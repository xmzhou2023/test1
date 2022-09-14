import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import random
import string

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class ColorLibrary(Base):
    """颜色库"""

    @allure.step("输入颜色")
    def input_color(self, option):
        self.input_text(user['查询条件 颜色'], option)
        logging.info("查询颜色：{}".format(option))

    @allure.step("选择可用状态")
    def choice_state(self, option):
        self.is_click(user['查询条件 可用状态'])
        if option == "启用":
            self.is_click(user['可用状态下拉选项'], "2")
        else:
            self.is_click(user['可用状态下拉选项'], "1")
        logging.info("查询可用状态：{}".format(option))

    @allure.step("点击查询按钮")
    def query_button(self):
        self.is_click(user['查询按钮'])
        logging.info("点击查询按钮")

    @allure.step("清空查询条件")
    def reset_button(self):
        self.is_click(user['重置按钮'])
        logging.info("点击重置按钮")

    @allure.step("列表数量断言")
    def listnum_assert(self):
        return self.element_text(user['列表条数（断言）'])

    @allure.step("结果断言方法")
    def assert_method(self, color, num):
        colorList = self.find_elements(user['列表断言'], num)
        resultList = []
        for i in range(len(colorList)):
            resultList.append(colorList[i].text)
        try:
            assert color in resultList, logging.warning("断言失败: a 不包含 b | a:{} b:{}".format(resultList, color))
            logging.info("断言成功: a 包含 b | a:{} b:{}".format(resultList, color))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("查询结果断言")
    def screen_assert(self, condition, color):
        if condition == "颜色编码":
            self.assert_method(color, "2")
        elif condition == "颜色名称Zh":
            self.assert_method(color, "3")
        elif condition == "颜色名称En":
            self.assert_method(color, "4")
        else:
            self.assert_method(color, "1")

    @allure.step("导出Excel")
    def export_button(self, content):
        try:
            self.check_download(user['导出按钮'], content)
        except Exception:
            logging.info("断言失败: 下载该附件失败")

    @allure.step("新增按钮")
    def append_button(self):
        self.is_click(user['新增按钮'])
        assertValue1 = self.element_text(user['列表指定列'], "2")
        assertValue2 = self.element_text(user['保存按钮'], "8")
        assert assertValue1 == "" and assertValue2 == "保存", logging.info("断言失败")
        logging.info("点击新增按钮，列表自动插入一行 可供编辑")

    @allure.step("输入颜色信息")
    def input_colorinf(self, kwargs):
        for lis, value in kwargs.items():
            if lis == "颜色名称Zh":
                self.input_text(user['颜色名称Zh'], value, "1")
            elif lis == "颜色名称En":
                self.input_text(user['颜色名称En'], value, "1")
            elif lis == "备注":
                self.input_text(user['备注'], value, "1")
            logging.info("颜色信息：新增{}={}".format(lis,value))

    @allure.step("造数据 超32位文本")
    def build_testData(self, length):
        result = ''.join(random.sample(string.ascii_letters + string.digits, length))
        return result


    @allure.step("保存按钮")
    def save_button(self):
        try:
            self.is_click(user['保存按钮'])
            hint = self.element_text(user['提示信息'])
            Nhint = hint[-4:]
            if hint == "Success":
                logging.info("断言通过 保存成功")
            elif Nhint == "不能为空":
                logging.info("断言通过 必填项未维护 保存失败")
                self.is_click(user['取消按钮'])
            elif hint == "不超过32个字符":
                logging.info("断言通过 字符超长 保存失败")
                self.is_click(user['取消按钮'])
            elif hint == "请输入正确的英文名称":
                logging.info("断言通过 字符超长 保存失败")
                self.is_click(user['取消按钮'])
        except Exception:
            self.is_click(user['取消按钮'])
            logging.info("保存失败,颜色编码或者名称已存在")

    @allure.step("返回表格指定列的列表")
    def list_retrun(self,num):
        colorlis = self.find_elements(user['列表断言'], num)
        colorCodeList = []
        for i in range(len(colorlis)):
            colorCodeList.append(colorlis[i].text)
        return colorCodeList

    @allure.step("列表数据断言")
    def list_assert(self, inputcolor, kwargs):
        try:
            self.input_color(inputcolor)
            self.query_button()
            for lis, colorcode in kwargs.items():
                if colorcode is not None:
                    s1 = self.list_retrun(lis)
                    assert colorcode in s1
                    logging.info("断言成功，颜色{}存在于列表中".format(colorcode))
                    self.reset_button()
        except Exception:
            self.reset_button()
            logging.info("断言失败")

    @allure.step("清空测试数据")
    def clear_testdata(self, name_zh, name_en, remark, creator_name):
        user = SQL("DRP", "test")
        user.delete_db(
            "DELETE from bd_color where name_zh = '{}' and name_en = '{}' and remark = '{}' and creator_name = '{}';".format(
                name_zh, name_en, remark, creator_name))
        logging.info("清空测试数据")

    @allure.step("前置条件 新增")
    def precondition_addtestdata(self, drivers):
        color = ColorLibrary(drivers)
        color.append_button()
        color.input_colorinf({"颜色名称Zh": "123","颜色名称En": "ABC","备注": "123"})
        color.save_button()
        logging.info("前置条件，新增测试数据完成")

    @allure.step("前置条件 页面查询测试数据")
    def precondition_selecttestdata(self,inputcolor=None,state=None):
        self.reset_button()
        if inputcolor is not None:
            self.input_color(inputcolor)
        if state is not None:
            self.choice_state(state)
        self.query_button()
        logging.info("前置条件，页面查询测试数据完成")



    @allure.step("根据颜色编码 获取列表行号")
    def list_rowNum(self,searchcolor):
        a = self.find_elements(user['列表断言'], str(2))
        b = []  # 取出列表第n列的所有文本
        for i in range(len(a)):
            b.append(a[i].text)
        if searchcolor in b:
            c = b.index(searchcolor) + 1
            logging.info("获取颜色{}所在行号：{}".format(searchcolor,c))
            return c

    @allure.step("点击编辑按钮")
    def edit_button(self,searchcolor):
        c = self.list_rowNum(searchcolor)
        self.is_click(user['编辑按钮'],str(c))
        logging.info("点击编辑按钮")

    @allure.step("编辑颜色")
    def edit_color(self, searchcolor,  kwargs):
        c = self.list_rowNum(searchcolor)
        for lis, value in kwargs.items():
            if lis == "颜色名称Zh":
                self.input_text(user['颜色名称Zh'], value, str(c))
            elif lis == "颜色名称En":
                self.input_text(user['颜色名称En'], value, str(c))
            elif lis == "备注":
                self.input_text(user['备注'], value, str(c))
            logging.info("颜色信息：{}改为{}".format(lis, value))


    @allure.step("点击启用/禁用按钮")
    def edit_state(self, searchcolor):
        c = self.list_rowNum(searchcolor)
        self.is_click(user['禁用/启用 按钮'], str(c))
        sleep(1)
        logging.info("点击禁用/启用按钮")


    @allure.step("禁用-》启用，前置条件")
    def edit_stateStart(self, drivers):
        color = ColorLibrary(drivers)
        color.precondition_addtestdata(drivers)
        color.precondition_selecttestdata("ABC")
        color.edit_state("ABC")
        color.screen_assert("状态","禁用")
        color.precondition_selecttestdata(state="禁用")
        logging.info("前置条件 禁用数据创建完成")










if __name__ == '__main__':
    pass
