import logging
import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from ..test_case.conftest import *
import random
import string
import re
import time

object_name = os.path.basename(__file__).split('.')[0]
requestCap = Element(pro_name, object_name)


class MainDataRequestCap(Base):
    """主数据-请购上限管理"""

    @allure.step("输入并选择物料编码")
    def input_itemCode(self, itemCode):
        self.is_click(requestCap['物料编码文本框'])
        self.input_text(requestCap['物料编码文本框'], itemCode)
        self.is_click(requestCap['下拉选项'], itemCode)
        logging.info("输入并选择物料编码：{}".format(itemCode))

    @allure.step("选择品牌")
    def choice_brand(self, brand):
        self.is_click(requestCap['品牌下拉'])
        self.is_click(requestCap['下拉选项'], brand)
        logging.info("选择品牌：{}".format(brand))

    @allure.step("选择状态")
    def choice_status(self, status):
        self.is_click(requestCap['状态下拉'])
        self.is_click(requestCap['下拉选项'], status)
        logging.info("选择状态：{}".format(status))

    @allure.step("点击查询按钮")
    def button_query(self):
        self.is_click(requestCap['查询 按钮'])
        logging.info("点击查询按钮")

    @allure.step("点击重置按钮")
    def button_reset(self):
        self.is_click(requestCap['重置 按钮'])
        logging.info("点击重置按钮")

    @allure.step("点击新增按钮")
    def button_newly(self):
        self.is_click(requestCap['新增 按钮'])
        sleep(1)
        txt = self.element_text(requestCap['弹出窗 断言'])
        assert txt == "新增", logging.warning("断言失败，新增窗口打开失败")
        logging.info("点击新增按钮，弹出新增窗口")

    @allure.step("维护新增物料信息")
    def add_info(self, itemcode=None, upperLimit=None, type=None):
        if itemcode != '':
            self.is_click(requestCap['弹出窗 物料编码文本框'])
            self.input_text(requestCap['弹出窗 物料编码文本框'], itemcode)
            self.is_click(requestCap['下拉选项'], itemcode)
        self.is_click(requestCap['弹出窗 申请上限(箱)文本框'])
        self.input_text(requestCap['弹出窗 申请上限(箱)文本框'], upperLimit)
        self.is_click(requestCap['弹出窗 保存按钮'])
        sleep(2)
        if type is None:
            txt = self.element_text(requestCap['断言 保存提示信息'])
            if txt == 'Success':
                logging.info("保存成功")
            else:
                result = re.findall('"message": "(.*?)" }', txt)[0]
                assert result == "当前物料已存在该记录!", logging.warning("断言失败")
                logging.info("保存失败，当前类目已存在！")
        else:
            if itemcode == '':
                txt = self.element_text(requestCap['断言 物料编码不为空'])
                assert txt == '物料编码不为空', logging.warning("断言失败")
                logging.info("断言成功，物料编码提示信息正确")
            if upperLimit == '':
                txt = self.element_text(requestCap['断言 申请上限数量(PCS)不为空'])
                assert txt == '申请上限数量(PCS)不为空', logging.warning("断言失败")
                logging.info("断言成功，申请上限提示信息正确")
            self.is_click(requestCap['弹出窗 关闭按钮'])
            logging.info("有必填项未维护，关闭弹窗")

    @allure.step("获取列表数据数量，用做断言")
    def get_listNum(self):
        txt = self.element_text(requestCap['获取列表数量'])
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

    @allure.step("清空测试数据")
    def clear_testData(self, itemcode,status):
        user = SQL("MIP", "test")
        if status is None:
            user.delete_db("DELETE from mm_req_list_limit where mat_code = '{}' and enable_flag ='1'".format(itemcode))
        else:
            user.delete_db("DELETE from mm_req_list_limit where mat_code = '{}' and enable_flag ='0'".format(itemcode))
        logging.info("清空测试数据")

    @allure.step("获取置灰文本")
    def get_hiddenText(self, ClassName, index):
        """获取置灰文本(用js)"""
        txt = self.driver.execute_script("document.getElementsByClassName('{}')[{}].value".format(ClassName, index))
        logging.info("获取隐藏文本：{}".format(txt))
        return txt

    @allure.step("前置条件，新增测试数据")
    def create_testData(self, drivers, itemcode, num):
        user = MainDataRequestCap(drivers)
        user.button_newly()
        user.add_info(itemcode, num)
        logging.info("新增测试数据，物料编码：{}，请购上限：{}；".format(itemcode, num))

    @allure.step("前置条件，查询测试数据")
    def query_testData(self, drivers, itemcode, brand, status):
        user = MainDataRequestCap(drivers)
        user.input_itemCode(itemcode)
        user.choice_brand(brand)
        user.choice_status(status)
        user.button_query()

    @allure.step("获取系统日期")
    def get_system_time(self):
        sys_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 格式化时间，按照 2022-04-15 13:46:32的格式打印出来
        new_time = sys_time.split(" ")
        return new_time[0]

    @allure.step("获取物料所在行")
    def assert_editdate(self):
        systime = self.get_system_time()
        a = self.find_element(requestCap['获取行号'], 8)
        b = a.get_attribute("innerHTML")
        c = re.findall(" (.*?) ", b)
        print(c)

    @allure.step("打开编辑弹窗")
    def button_edit(self):
        self.is_click(requestCap['列表 编辑按钮'], 1)
        sleep(1)
        txt = self.element_text(requestCap['弹出窗 断言'])
        assert txt == "编辑", logging.warning("断言失败，打开编辑弹窗失败")
        logging.info("断言成功，打开编辑弹窗成功")


    @allure.step("编辑物料信息")
    def edit_info(self, upperLimit=None, type=None):
        if type is None:
            self.is_click(requestCap['弹出窗 申请上限(箱)文本框'])
            self.input_text(requestCap['弹出窗 申请上限(箱)文本框'], upperLimit)
            self.is_click(requestCap['编辑 保存按钮'])
            sleep(1)
            txt = self.element_text(requestCap['断言 保存提示信息'])
            if txt == 'Success':
                logging.info("保存成功")
            else:
                result = re.findall('"message": "(.*?)" }', txt)[0]
                assert result == "当前申请上限数量(箱)已存在！", logging.warning("断言失败")
                logging.info("保存失败，当前申请上限数量(箱)已存在！")
        else:
            if upperLimit == '':
                self.is_click(requestCap['弹出窗 申请上限(箱)文本框'])
                self.is_click(requestCap['弹出窗 清空文本框'])
                self.is_click(requestCap['编辑 保存按钮'])
                txt = self.element_text(requestCap['断言 申请上限数量(PCS)不为空'])
                assert txt == '申请上限数量(PCS)不为空', logging.warning("断言失败")
                logging.info("断言成功，申请上限提示信息正确")
            self.is_click(requestCap['编辑弹窗 关闭按钮'])
            logging.info("有必填项未维护，关闭弹窗")

    @allure.step("点击启用/删除按钮")
    def button_changeStatus(self):
        self.is_click(requestCap['列表 删除/启用按钮'], 1)
        sleep(1)
        txt = self.element_text(requestCap['获取 删除 窗口文本'])
        assert txt == "确定要删除该物料的申请上限限制吗?", logging.warning("断言失败，打开窗口失败")
        logging.info("断言成功，打开状态修改窗口")
        self.is_click(requestCap['删除 窗口 确认按钮'])





