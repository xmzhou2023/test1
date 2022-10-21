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


class ProcessConfig(Base):
    """流程配置"""
    @allure.step("前往指定事业部页面")
    def goto_BU(self, BU):
        self.is_click(user['BU菜单'],BU)
        logging.info("前往{}菜单成功".format(BU))
        sleep(2)

    @allure.step("选择流程名称下拉项")
    def choice_process(self, processname):
        self.readonly_input_text(user['流程名称 选择框'],processname)
        self.is_click(user['流程名称 下拉选项'],processname)
        logging.info("选择流程名称{}".format(processname))

    @allure.step("返回 数据所在行号")
    def return_rowNum(self,processname):
        txt = self.find_elements(user['流程名称(Zh) 用于获取行号'])
        b = []
        for i in range(len(txt)):
            b.append(txt[i].text)
        if processname in b:
            rowNum = b.index(processname) +1
            logging.info("{}所在行：{}行".format(processname,rowNum))
            return str(rowNum)
        else:
            logging.info("返回行号：1 ")
            return str(1)

    @allure.step("点击查询按钮")
    def query_button(self):
        self.is_click(user['查询 按钮'])
        logging.info("点击查询按钮")

    @allure.step("点击重置按钮")
    def reset_button(self):
        self.is_click(user['重置 按钮'])
        logging.info("点击重置按钮")

    @allure.step("点击新增按钮")
    def add_button(self):
        self.is_click(user['新增 按钮'])
        logging.info("点击新增按钮")

    @allure.step("输入流程名称(Zh)")
    def input_processZh(self,Zh,ZhNew):
        rowNum = self.return_rowNum(Zh)
        self.readonly_input_text(user['流程名称(Zh) 输入框'], ZhNew, rowNum)
        logging.info("输入流程名称(Zh):{}".format(Zh))

    @allure.step("输入流程名称(En)")
    def input_processEn(self,Zh,En):
        rowNum = self.return_rowNum(Zh)
        self.readonly_input_text(user['流程名称(En) 输入框'], En, rowNum)
        logging.info("输入流程名称(En):{}".format(En))

    @allure.step("输入外部流程表单")
    def input_processForm(self,Zh, form):
        rowNum = self.return_rowNum(Zh)
        self.readonly_input_text(user['外部流程表单 下拉框'], form, rowNum)
        self.is_click(user['流程名称 下拉选项'],form)
        logging.info("输入外部流程表单:{}".format(form))

    @allure.step("输入备注")
    def input_remark(self,Zh, remark):
        rowNum = self.return_rowNum(Zh)
        self.readonly_input_text(user['备注 输入框'], remark, rowNum)
        logging.info("输入备注:{}".format(remark))

    @allure.step("点击保存按钮")
    def save_button(self,Zh):
        rowNum = self.return_rowNum(Zh)
        self.is_click(user['保存 按钮'],rowNum)
        sleep(1)
        txt = self.element_text(user['错误提示'])
        if txt[-4:] == '已经存在':
            self.is_click(user['取消 按钮'],rowNum)
            logging.info("保存失败，原因:{}".format(txt))
        elif txt[-4:] == '不能为空':
            self.is_click(user['取消 按钮'],rowNum)
            logging.info("保存失败，原因:{}".format(txt))
        else:
            logging.info("保存成功")

    @allure.step("新建流程名称断言")
    def assert_process(self,Zh):
        rowNum = self.return_rowNum(Zh)
        listZh = self.element_text(user['列表断言'],rowNum)
        assert listZh == Zh,logging.warning("断言失败，{} | {} 不相等".format(Zh,listZh))
        logging.info("断言成功，{} | {} 相等".format(Zh,listZh))

    @allure.step("编辑按钮")
    def edit_button(self,Zh):
        rowNum = self.return_rowNum(Zh)
        self.is_click(user['编辑 按钮'],rowNum)
        logging.info("点击编辑按钮")

    @allure.step("删除按钮")
    def del_button(self,Zh):
        rowNum = self.return_rowNum(Zh)
        self.is_click(user['删除 按钮'],rowNum)
        self.is_click(user['删除 确认'])
        logging.info("删除确认完成")

    @allure.step("删除断言")
    def del_assert(self,Zh):
        txt = self.find_elements(user['流程名称(Zh) 用于获取行号'])
        b = []
        for i in range(len(txt)):
            b.append(txt[i].text)
        assert Zh not in b,logging.warning("删除断言失败，流程名称(Zh)={}未被删除".format(Zh))
        logging.info("删除断言成功，列表中 无 流程名称(Zh)={}的数据".format(Zh))

    @allure.step("配置按钮")
    def configuration_button(self,Zh):
        rowNum = self.return_rowNum(Zh)
        self.is_click(user['管理 按钮'],rowNum)
        logging.info("点击管理按钮")
        sleep(2)

    @allure.step("节点配置按钮")
    def nodeDeployment_button(self,Zh):
        rowNum = self.return_rowNum(Zh)
        self.is_click(user['节点配置 按钮'],rowNum)
        logging.info("点击节点配置按钮")
        sleep(2)

    @allure.step("前置条件，新增测试数据")
    def preposition(self,drivers):
        process = ProcessConfig(drivers)
        process.goto_BU("东非地区部")
        process.add_button()
        process.input_processZh("测试001","测试001")
        process.input_processEn("测试001","test001")
        process.input_processForm("测试001","itel事业部北非区审批")
        process.input_remark("测试001","xxxxx")
        process.save_button("测试001")

    @allure.step("后置条件，删除测试数据")
    def postposition(self,drivers,value):
        process = ProcessConfig(drivers)
        process.del_button(value)
        process.del_assert(value)

    @allure.step("关闭标签页")
    def close_page(self,title):
        if title == "配置管理":
            self.is_click(user['关闭配置管理标签页'])
            logging.info("关闭配置管理标签页")
        else:
            self.is_click(user['关闭节点配置标签页'])
            logging.info("关闭节点配置标签页")


if __name__ == '__main__':
    pass
