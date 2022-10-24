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


class ProcessQuery(Base):
    """流程配置"""

    @allure.step("选择查询下拉选选项")
    def choice_queryCondition(self, queryCondition, value):
        condition = ["节点名称","节点类型","国家","负责人","系统角色"]
        if queryCondition in condition:
            self.readonly_input_text(user['{} 输入框'.format(queryCondition)],value)
            try:
                self.is_click(user['下拉选项'],value)
                logging.info("选择{}:{}".format(queryCondition,value))
            except:
                self.move_house(200)
                logging.info("下拉列表无选项：{}".format(value))
        else:
            self.is_click(user['{} 选择框'.format(queryCondition)])
            try:
                self.is_click(user['下拉选项'],value)
                logging.info("选择{}:{}".format(queryCondition,value))
            except:
                self.move_house(200)
                logging.info("下拉列表无选项：{}".format(value))

    @allure.step("点击查询按钮")
    def query_button(self):
        self.is_click(user['查询 按钮'])
        logging.info("点击查询按钮")
        sleep(1)

    @allure.step("点击重置按钮")
    def reset_button(self):
        self.is_click(user['重置 按钮'])
        logging.info("点击重置按钮")

    @allure.step("点击导出按钮")
    def export_button(self,content):
        try:
            self.check_download(user['导出 按钮'], content)
        except Exception:
            logging.info("断言失败: 下载该附件失败")

    @allure.step("获取列表是数据条数")
    def return_listNum(self):
        sleep(1)
        txt = self.element_text(user['获取列表数据数量 用于断言'])
        b = re.findall(" (.*?) ", txt)[0]
        logging.info("列表数据量:{}条".format(b))
        return int(b)

    @allure.step("列表数据为空断言")
    def assert_listNum_Null(self):
        txt = self.element_text(user['暂无数据 断言'])
        return txt


if __name__ == '__main__':
    pass
