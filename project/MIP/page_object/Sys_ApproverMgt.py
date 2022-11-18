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
set = Element(pro_name, object_name)


class SysApproverMgt(Base):
    """系统管理-审批人管理"""

    @allure.step("选择品牌")
    def choice_brand(self, brand):
        self.is_click(set['品牌下拉'])
        self.is_click(set['下拉选项'], brand)
        logging.info("选择品牌：{}".format(brand))

    @allure.step("选择所属组织")
    def choice_organization(self, organization):
        self.is_click(set['所属组织下拉'])
        self.is_click(set['下拉选项'], organization)
        logging.info("选择组织：{}".format(organization))

    @allure.step("输入审批人")
    def input_approver(self, approver):
        self.is_click(set['审批人文本框'])
        self.input_text(set['审批人文本框'], approver)
        self.is_click(set['下拉选项'], approver)
        logging.info("选择审批人：{}".format(approver))

    @allure.step("选择审批节点")
    def choice_approveNode(self, approveNode):
        self.is_click(set['审批节点下拉'])
        self.is_click(set['下拉选项'], approveNode)
        logging.info("选择审批节点：{}".format(approveNode))

    @allure.step("选择地区")
    def choice_area(self, area):
        self.is_click(set['地区下拉'])
        self.is_click(set['下拉选项'], area)
        logging.info("选择地区：{}".format(area))

    @allure.step("点击查询按钮")
    def button_query(self):
        self.is_click(set['搜索 按钮'])
        logging.info("点击搜索按钮")

    @allure.step("点击重置按钮")
    def button_reset(self):
        self.is_click(set['重置 按钮'])
        logging.info("点击重置按钮")

    @allure.step("获取列表数据数量，用做断言")
    def get_listNum(self):
        txt = self.element_text(set['获取列表数量'])
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

    @allure.step("点击新增按钮")
    def button_Add(self):
        self.is_click(set['新增 按钮'])
        logging.info("点击新增按钮")

    @allure.step("维护审批人信息")
    def edit_approverinf(self, brand, group, area, nodeName, approver):
        dict = {"1": brand, "2": group, "3": area, "4": nodeName, "5": approver}
        for k, v in dict.items():
            if k == "5":
                if v == "":
                    pass
                else:
                    self.is_click(set['新增 列表某列数据'], k)
                    self.input_text(set['新增 审批人输入框'], v, k)
                    sleep(1)
                    self.is_click(set['下拉选项'], v)
                    sleep(1)
            elif v == "":
                pass
            else:
                self.is_click(set['新增 列表某列数据'], k)
                self.is_click(set['下拉选项'], v)
        logging.info("维护审批人信息：品牌：{}，所属组织：{}，地区：{}，审批节点：{}，审批人：{}".format(brand, group, area, nodeName, approver))

    @allure.step("点击保存按钮")
    def button_save(self):
        self.is_click(set['新增 保存按钮'])
        txt = self.element_text(set['获取提示信息 断言'])
        if txt != "新增成功":
            if txt == "编辑成功":
                logging.info("编辑保存成功")
            else:
                self.is_click(set['新增 取消按钮'])
                logging.info("新增保存失败，失败原因：{}".format(txt))
        else:
            logging.info("新增保存成功")
        sleep(1)

    @allure.step("查找测试数据")
    def query_testdata(self, drivers, brand, organization, approver, approveNode, area):
        set = SysApproverMgt(drivers)
        set.choice_brand(brand)
        set.choice_organization(organization)
        set.input_approver(approver)
        set.choice_approveNode(approveNode)
        set.choice_area(area)
        set.button_query()
        listNum = set.get_listNum()
        return listNum

    @allure.step("创建测试数据")
    def creat_testdata(self,drivers, brand, group, area, nodeName, approver):
        set = SysApproverMgt(drivers)
        set.button_Add()
        set.edit_approverinf(brand, group, area, nodeName, approver)
        set.button_save()
        logging.info("新增测试数据完成")


    @allure.step("清除测试数据")
    def clear_testData(self, nodename, approver, brand, country, group):
        user = SQL("MIP", "test")
        brandcode = ""
        countrycode = ""
        groupid = ""
        if brand == "INFINIX":
            brandcode = "02"
        if brand == "ITEL":
            brandcode = "03"
        if country == "阿富汗":
            countrycode = "AF"
        if group == "地区部":
            groupid = "1"
        user.delete_db("DELETE from process_user_manage WHERE node_name = '{}' and approve_user_name ='{}' and "
                       "brand_code ='{}' and country_code ='{}' and group_id = '{}'".format(nodename, approver,
                                                                                            brandcode, countrycode,
                                                                                            groupid))
        logging.info("清空测试数据")

    @allure.step("点击编辑按钮")
    def button_edit(self):
        self.is_click(set['编辑按钮'])
        logging.info("点击编辑按钮")
        sleep(2)
