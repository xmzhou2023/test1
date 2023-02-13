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
        repeatbatch = self.get_columnValue(choice="3")[2]
        end = self.get_date()[0]
        self.is_click(user["add按钮"])
        self.wait.until(EC.presence_of_element_located(user["batchNo"]),message="新增弹窗打开失败")
        if batch == repeatbatch:
            logging.info("输入重复的batch号")
            self.input_text(user["batchNo"],batch)
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

        elif startdate == end:
            logging.info("输入结束时间大于开始时间")
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
        logging.info("点击新增弹窗上的save")

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
        date = str(datetime.datetime(year=2021, month=9, day=22))
        enddate = date.split(" ", 1)
        return enddate


    @allure.step("获取11位长度文本")
    def get_Numbersletters(self):
        num = string.ascii_letters+string.digits
        Numbersletters = "".join(random.sample(num , 11))
        return Numbersletters

    def sunkingedit(self, batch, startdate, enddate):
        repeatbatch = self.get_columnValue(choice="3")[2]
        self.is_click_tbm(user["第一行edit按钮"])
        self.wait.until(EC.presence_of_element_located(user["batchNo"]), message="编辑框打开失败")
        end = self.get_date()[0]
        if batch == repeatbatch:
            self.input_text(user["batchNo"], batch)

        elif startdate == end:
            logging.info("已打开编辑框")
            self.is_click(user["date"], "startTime")  # 点击warrantystartdate
            sleep(1)
            self.input_text(user["selectdate"], startdate, choice="Select date")  # 输入日期
            self.is_click(user["selectdate"], choice="Select time")
            self.is_click(user["date"], choice="endTime")  # 点击warrantyenddate
            sleep(1)
            self.input_text(user["selectdate"], enddate, choice="Select date")
            self.is_click(user["selectdate"], choice="Select time")
            self.is_click(user["日期选择框上的OK"])

        else:
            logging.info("进入编辑页输入batch No 值")
            self.input_text(user["batchNo"], batch)
        self.is_click_tbm(user["save"])


    def FG_export(self, country):

        if country is not None:
            self.is_click(user["筛选框"], choice="countryCode")
            self.input_text(user["筛选框"], country,choice="countryCode")
            logging.info("国家筛选框输入{}".format(country))
            sleep(0.5)
            self.is_click(user["下拉筛选框_第一条数据"])
            logging.info("对指定国家进行下载")
            self.is_click(user["export"])
            self.wait.until(EC.presence_of_element_located(user["tasktips的ok按钮"]),message="异步下载提示框没有显示")
            self.is_click(user["tasktips的ok按钮"])
        else:
            logging.info("对所有数据进行下载")
            self.is_click(user["export"])
            self.wait.until(EC.presence_of_element_located(user["tasktips的ok按钮"]),message="异步下载提示框没有显示")
            self.is_click(user["tasktips的ok按钮"])




    def task_download(self, name, content):
        self.is_click(user["取消全选按钮"])
        self.input_text(user["MenuName"], name)
        sleep(3)
        self.is_click(user["搜索按钮"])
        task_status = self.element_text(user['Task_Status'])
        if task_status == '100-Finished':
            logging.info("当前状态是100，可以直接下载")
            self.check_download(user['Download_Task'], content)
        elif task_status != '100-Finished':
            logging.info("再次点击search，直到100状态")
            while task_status != '100-Finished':
                sleep(3)
                self.is_click(user["搜索按钮"])
                task_status = self.element_text(user['Task_Status'])
            self.check_download(user['Download_Task'], content)
        else:
            self.is_click(user["搜索按钮"])
            self.wait.until(EC.presence_of_element_located(user["Download_Task"]), message='进度不是100')
            task_status = self.element_text(user['Task_Status'])
            logging.info("当前状态是{}".format(task_status))
            self.check_download(user['Download_Task'], content)

if __name__ == '__main__':
    pass
