import allure
from public.base.basics import Base
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import logging
from project.TLC_web.test_case.conftest import *
pro_env = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, pro_env)
class label(Base):
    """卡片属性"""

# 新增标签
    @allure.step("点击新增按钮")
    def append_button(self):
        self.is_click(user['添加标签按钮'])
        # WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_clickable(user['添加标签按钮'])).click()
        logging.info("打开新增标签弹窗")
        sleep(1)

    @allure.step("新增弹窗 名称描述输入")
    def add_label(self, input_labelName=None, input_Description=None):
        self.readonly_input_text(user['标签名称输入框'], input_labelName)
        self.readonly_input_text(user['标签描述输入框'], input_Description)
        sleep(1)

    @allure.step("新增弹窗 新增保存")
    def add_save(self, t):
        self.is_click(user['确定按钮'])
        if t == "标签名称为空":
            a = self.element_text(user['名称新增必填项'])
            if a == '请输入分类名称':
                self.is_click(user['新增弹框关闭按钮'])
                logging.info("名称为必填项,新增失败")
        else:
            # TODO
            ...


    @allure.step("关闭新建弹窗")
    def close_screen(self):
        self.is_click(user['新增弹框关闭按钮'])
        logging.info("取消新增")
        sleep(2)

    @allure.step("新建弹框取消")
    def append_cancel(self):
        self.is_click(user['取消按钮'])
        logging.info("取消新增")
        sleep(2)

    @allure.step("卡片属性页面点击")
    def page_click(self):
        self.is_click(user['卡片属性页面点击'])
        logging.info("卡片属性页面点击成功")
        sleep(2)


# 编辑标签
    @allure.step("点击编辑按钮")
    def edit_button(self):
        self.is_click(user['标签编辑'])
        logging.info("打开编辑标签弹窗")
        sleep(2)


    @allure.step("编辑弹窗 名称描述输入")
    def edit_label(self, edit_labelName=None, edit_Description=None):
        self.is_click(user['标签名称编辑框'])
        self.is_click(user['标签名称清除'])
        self.readonly_input_text(user['标签名称编辑框'], edit_labelName)
        self.readonly_input_text(user['标签描述编辑框'], edit_Description)
        sleep(2)

    @allure.step("编辑弹窗 确定保存")
    def edit_save(self, t):
        self.is_click(user['编辑确定'])
        if t == "编辑标签名称为空":
            a = self.element_text(user['名称编辑必填项'])
            if a == '请输入分类名称':
                self.is_click(user['编辑取消'])
                logging.info("名称为必填项,新增失败")
        else:
            # TODO
            ...

    @allure.step("关闭编辑弹窗")
    def edit_close(self):
        self.is_click(user['编辑弹框关闭按钮'])
        logging.info("编辑弹框关闭")
        sleep(1)

    @allure.step("编辑弹框取消")
    def edit_cancel(self):
        self.is_click(user['编辑取消'])
        logging.info("取消编辑")
        sleep(2)

# 删除标签
    @allure.step("点击删除按钮")
    def del_button(self):
        self.is_click(user['标签删除'])
        logging.info("打开标签删除弹窗")
        sleep(2)

    @allure.step("确定删除")
    def del_save(self):
        self.is_click(user['删除确定'])
        logging.info("标签删除")
        sleep(2)

    @allure.step("关闭删除弹窗")
    def del_close(self):
        self.is_click(user['删除弹框关闭按钮'])
        logging.info("删除弹框关闭")
        sleep(1)

    @allure.step("编辑弹框取消")
    def del_cancel(self):
        self.is_click(user['删除取消'])
        logging.info("取消删除")
        sleep(1)

# 标签状态
    @allure.step("启用标签")
    def enable_label(self):
        self.is_click(user['启用/禁用切换按钮'])
        logging.info("标签被启用")
        sleep(1)

    @allure.step("禁用标签")
    def disable_label(self):
        self.is_click(user['启用/禁用切换按钮'])
        self.is_click(user['禁用确定'])
        logging.info("标签被禁用")
        sleep(2)

    @allure.step("禁用标签取消")
    def disable_cancel(self):
        self.is_click(user['启用/禁用切换按钮'])
        self.is_click(user['禁用取消'])
        logging.info("禁用标签弹框关闭，标签为启用")
        sleep(2)

    @allure.step("禁用标签弹框关闭")
    def disable_close(self):
        self.is_click(user['启用/禁用切换按钮'])
        self.is_click(user['禁用弹框关键按钮'])
        logging.info("禁用标签弹框关闭，标签为启用")
        sleep(2)

# 标签查询
    @allure.step("打开标签查询弹框")
    def query_label(self):
        self.is_click(user['查询按钮'])
        logging.info("标签查询框打开")
        sleep(2)

    @allure.step("输入名称查询")
    def query_labelName(self, query_labelName=None):
        self.readonly_input_text(user['名称查询'], query_labelName)
        sleep(1)

    @allure.step("下拉选择标签状态")
    def query_labelState(self, query_labelState=None):
        self.is_click(user['启用状态下拉框'])
        try:
            if query_labelState == "启用":
                self.is_click(user['启用/禁用查询选择'], "1")
            elif query_labelState == "禁用":
                self.is_click(user['启用/禁用查询选择'], "2")
            logging.info("标签状态：{}", format(query_labelState))
        except:
            self.is_click(user['查询确定'])
        sleep(2)

    @allure.step("标签查询框确认按钮")
    def query_save(self):
        self.is_click(user['查询确定'])
        logging.info("查询完成")
        sleep(1)

    @allure.step("标签查询框重置按钮")
    def query_reset(self):
        self.is_click(user['重置查询'])
        self.is_click(user['查询确定'])
        logging.info("查询条件重置完成")
        sleep(1)

    @allure.step("标签查询框取消按钮")
    def query_cancel(self):
        self.is_click(user['取消查询'])
        logging.info("查询条件取消完成")
        sleep(1)

    @allure.step("标签查询框关闭按钮")
    def query_close(self):
        self.is_click(user['查询框关闭'])
        logging.info("标签查询框关闭完成")
        sleep(1)



if __name__ == '__main__':
        pass