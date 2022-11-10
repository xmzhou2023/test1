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

class ProjectPage(Base):
    """项目管理页"""

    # @allure.step("获取列表第4列文本")
    # def get_columnValue(self, choice):
    #     self.refresh()
    #     eles = self.find_elements(user["第4列文本"], choice)
    #     columnValue = []
    #     for n in eles:
    #         columnValue.append(n.text)
    #     return columnValue

    @allure.step("Project管理页查询")
    def project_input_criteria(self, country, brand, status):
        self.refresh()
        if country == "IN":
            logging.info("进行国家条件查询")
            self.is_click(user["筛选项输入框"],"countryCode")
            self.input_text(user["筛选项输入框"],country,"countryCode")
            sleep(1)
            self.is_click(user["下拉筛选框_第一条数据"])
        elif brand == "TECNO":
            logging.info("进行brand条件查询")
            self.is_click(user["筛选项输入框"],"brandId")
            self.input_text(user["筛选项输入框"],brand,"brandId")
            sleep(1)
            self.is_click(user["下拉筛选框_第一条数据"])
        elif status == "Enable":
            self.is_click(user["筛选项输入框"],"isEnable")
            self.is_click(user["下拉框enable按钮"])

        else:
            logging.info("进行组合条件查询")
            self.is_click(user["筛选项输入框"], "countryCode")
            self.input_text(user["筛选项输入框"], country, "countryCode")
            sleep(1)
            self.is_click(user["下拉筛选框_第一条数据"])
            sleep(1)
            self.is_click(user["筛选项输入框"], "brandId")
            self.input_text(user["筛选项输入框"], brand, "brandId")
            sleep(1)
            self.is_click(user["下拉筛选框_第一条数据"])
            sleep(1)
            self.is_click(user["筛选项输入框"], "isEnable")
            self.is_click(user["下拉框disable按钮"])

    @allure.step("Project管理页sql查询")
    def project_sql_search(self, country, brand, status):
        if country == "IN":
            logging.info("查询国家的sql")
            user = SQL("CRM", "test")  # 链接数据库
            sql_search = user.query_db('SELECT COUNT(*) FROM crm_mdm_project_mgt WHERE crm_mdm_project_mgt.country_code = "{}"'.format(country))
            sql_qty = sql_search[0].get("COUNT(*)")
        elif brand == "TECNO":
            logging.info("查询brand的sql")
            user = SQL("CRM", "test")  # 链接数据库
            sql_search = user.query_db('SELECT COUNT(*) FROM crm_mdm_project_mgt p LEFT JOIN crm_mdm_brand b ON b.brand_id = p.brand_id WHERE b.brand_name= "{}"'.format(brand))
            sql_qty = sql_search[0].get("COUNT(*)")
        elif status == "1":
            user = SQL("CRM", "test")  # 链接数据库
            sql_search = user.query_db('SELECT COUNT(*) FROM crm_mdm_project_mgt WHERE crm_mdm_project_mgt.is_enable="{}"'.format(status))
            sql_qty = sql_search[0].get("COUNT(*)")
        else:
            logging.info("查询组合sql")
            user = SQL("CRM", "test")  # 链接数据库
            sql_search = user.query_db('SELECT COUNT(*) FROM crm_mdm_project_mgt p LEFT JOIN crm_mdm_brand b ON b.brand_id = p.brand_id WHERE b.brand_name= "{}" AND p.is_enable="{}" AND p.country_code = "{}"'.format(brand,status,country))
            sql_qty = sql_search[0].get("COUNT(*)")
        return sql_qty

    @allure.step("Project点击搜索按钮")
    def project_click_search(self):
        sleep(1)
        self.is_click(user["搜索按钮"])

    @allure.step("Project管理页点击新增按钮")
    def project_add(self):
        self.refresh()
        self.is_click(user["add按钮"])
        logging.info("点击新增按钮")

    @allure.step("Project管理页点击编辑")
    def project_edit(self):
        self.refresh()
        self.is_click(user["第一行edit按钮"])
        logging.info("点击编辑按钮")

    @allure.step("Project管理页新增和编辑操作")
    def project_input(self, country,category, StartDate, EndDate, txt):
        text = self.element_text(user["新增编辑弹窗的text"])
        if text == "Add":
            self.is_click(user["新增页输入框"],"projectName")
            self.is_click(user["下拉筛选框_第一条数据"])
            sleep(1)
            self.is_click(user["新增页输入框"], "countryCode")
            self.input_text(user["新增页输入框"],country, "countryCode")
            sleep(1)
            self.is_click(user["下拉筛选框_第一条数据"])
            sleep(1)
            self.is_click(user["新增页输入框"], "categoryName")
            self.input_text(user["新增页输入框"], category, "categoryName")
            self.is_click(user["下拉筛选框_第一条数据"])
            sleep(1)
            self.is_click(user["新增页输入框"], "brandName")
            self.is_click(user["下拉筛选框_第一条数据"])
            sleep(1)
            self.is_click(user["新增页输入框"], "effectiveTime")
            self.input_text(user["新增页输入框"], StartDate, "effectiveTime")
            sleep(1)
            self.is_click(user["新增页输入框"], "expirationTime")
            self.input_text(user["新增页输入框"], EndDate, "expirationTime")
            sleep(1)
            self.input_text(user["新增页Desc输入框"], txt)
        else:
            logging.info("编辑用例执行")
            # self.clear_input(user["enddate输入框"])
            # self.input_text(user["enddate输入框"], EndDate)
            # sleep(1)
            self.clear_input(user["新增页Desc输入框"])
            self.input_text(user["新增页Desc输入框"], txt)

    def project_save(self):
        self.is_click(user["save"], choice=2)
        logging.info("点击save按钮")

    def project_editsave(self):
        self.is_click(user["编辑页的save"])
        logging.info("点击编辑页的save按钮")

    def project_editcancel(self):
        self.is_click(user["编辑页的cancel"])
        logging.info("点击编辑页的cancel按钮")

    def get_txt(self):
        att = self.element_text(user["获取返回文本"])
        return att




    def project_cancel(self):
        self.is_click(user["cancel"], choice=3)
        logging.info("点击cancel按钮")

    def project_reset(self):
        self.is_click(user["reset"], choice=1)
        logging.info("点击reset按钮")

    @allure.step("确认禁用弹框点击确定")
    def disable(self):
        self.refresh()
        self.is_click_tbm(user["第一行enable按钮"])
        self.wait.until(EC.presence_of_element_located(user["确认disable弹窗的Yes按钮"]),message="确认禁用的弹窗未出现")
        self.is_click_tbm(user["确认disable弹窗的Yes按钮"])


if __name__ == '__main__':
    pass
