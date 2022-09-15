import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import datetime
import string
import random
import logging

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class FGsunking(Base):
    """sunking页"""

    @allure.step("获取列表第4列文本")
    def get_columnValue(self, choice):
        self.refresh()
        eles = self.find_elements(user["第4列文本"], choice)
        columnValue = []
        for n in eles:
            columnValue.append(n.text)
        return columnValue


    @allure.step("sunking新增编辑操作")
    def sunkingadd(self, batch, startdate, enddate, country, code):
        if batch==batch:
            self.is_click(user["add按钮"])
            self.input_text(user["batchNo"],batch)
            logging.info("输入重复的batch号".format(batch))
            self.is_click(user["countrycode"])
            self.input_text(user["countrycode"],country)
            sleep(1)
            self.is_click_tbm(user["下拉筛选框_第一条数据"])
            self.is_click(user["materialcode"])
            self.input_text(user["materialcode"],code)
            sleep(1)
            self.is_click_tbm(user["下拉筛选框_第一条数据"])
            self.is_click(user["date"],choice="startTime")  # 点击warrantystartdate
            sleep(1)
            self.input_text(user["selectdate"], startdate, choice="Select date")
            self.is_click(user["selectdate"],choice="Select time")
            self.is_click(user["date"],choice="endTime")  # 点击warrantyenddate
            sleep(1)
            self.input_text(user["selectdate"], enddate, choice="Select date")
            self.is_click(user["selectdate"],choice="Select time")
            self.is_click(user["日期选择框上的OK"])

        elif startdate == enddate:
            self.is_click(user["add按钮"])
            self.input_text(user["batchNo"], batch)
            self.is_click(user["countrycode"])
            self.input_text(user["countrycode"], country)
            sleep(1)
            self.is_click_tbm(user["下拉筛选框_第一条数据"])
            self.is_click(user["materialcode"])
            self.input_text(user["materialcode"], code)
            sleep(1)
            self.is_click_tbm(user["下拉筛选框_第一条数据"])
            self.is_click(user["date"], choice="startTime")  # 点击warrantystartdate
            sleep(1)
            self.input_text(user["selectdate"], startdate, choice="Select date")
            logging.info("输入开始时间大于结束时间的错误数据")
            self.is_click(user["selectdate"], choice="Select time")
            self.is_click(user["date"], choice="endTime")  # 点击warrantyenddate
            sleep(1)
            self.input_text(user["selectdate"], enddate, choice="Select date")
            self.is_click(user["selectdate"], choice="Select time")
            self.is_click(user["日期选择框上的OK"])

        else:
            self.is_click(user["add按钮"])
            self.input_text(user["batchNo"], batch)
            self.is_click(user["countrycode"])
            self.input_text(user["countrycode"], country)
            sleep(1)
            self.is_click_tbm(user["下拉筛选框_第一条数据"])
            self.is_click(user["materialcode"])
            self.input_text(user["materialcode"], code)
            sleep(1)
            self.is_click_tbm(user["下拉筛选框_第一条数据"])
            self.is_click(user["date"], choice="startTime")  # 点击warrantystartdate
            sleep(1)
            self.input_text(user["selectdate"], startdate, choice="Select date")
            self.is_click(user["selectdate"], choice="Select time")
            self.is_click(user["date"], choice="endTime")  # 点击warrantyenddate
            sleep(1)
            self.input_text(user["selectdate"], enddate, choice="Select date")
            self.is_click(user["selectdate"], choice="Select time")
            self.is_click(user["日期选择框上的OK"])

        self.is_click_tbm(user["save"])
        logging.info("点击新增弹窗上的{}".format("save"))

    @allure.step("新增框点击取消按钮")
    def click_cancel(self):
        self.is_click_tbm(user["cancel"])
        logging.info("点击新增页的{}".format("cancel"))
        self.wait.until(EC.presence_of_element_located(user["关闭弹窗上的confirm"]),message="关闭弹窗未出现")
        logging.info("点击confirm弹窗上的{}".format("关闭弹窗上的confirm"))
        self.is_click_tbm(user["关闭弹窗上的confirm"])

    @allure.step("确认禁用弹框点击确定")
    def disable(self):
        self.refresh()
        self.is_click_tbm(user["第一行enable按钮"])
        self.wait.until(EC.presence_of_element_located(user["确认disable弹窗的Yes按钮"]),message="确认禁用的弹窗未出现")
        self.is_click_tbm(user["确认disable弹窗的Yes按钮"])

    def get_date(self):
        date = str(datetime.datetime(year=2019, month=9, day=22))
        enddate = date.split(" ", 1)
        return enddate
        pass

    @allure.step("获取11位长度文本")
    def get_Numbersletters(self):
        num = string.ascii_letters+string.digits
        Numbersletters = "".join(random.sample(num , 11))
        return Numbersletters

    def sunkingedit(self, batch, startdate, enddate):
        if batch == batch:
            self.refresh()
            self.is_click(user["第一行edit按钮"])
            self.wait.until(EC.presence_of_element_located(user["batchNo"]),message="编辑框打开失败")
            self.input_text(user["batchNo"], batch)

        elif startdate == enddate:
            self.refresh()
            self.is_click(user["第一行edit按钮"])
            self.wait.until(EC.presence_of_element_located(user["batchNo"]),message="编辑框打开失败")
            self.is_click(user["date"], choice="startTime")  # 点击warrantystartdate
            sleep(1)
            self.input_text(user["selectdate"], startdate, choice="Select date")  # 输入日期
            self.is_click(user["selectdate"], choice="Select time")
            self.is_click(user["date"], choice="endTime")  # 点击warrantyenddate
            sleep(1)
            self.input_text(user["selectdate"], enddate, choice="Select date")
            self.is_click(user["selectdate"], choice="Select time")
            self.is_click(user["日期选择框上的OK"])

        else:
            self.refresh()
            self.is_click(user["第一行edit按钮"])
            self.wait.until(EC.presence_of_element_located(user["batchNo"]),message="编辑框打开失败")
            self.input_text(user["batchNo"], batch)
        self.is_click_tbm(user["save"])

if __name__ == '__main__':
    pass
