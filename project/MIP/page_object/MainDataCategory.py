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
category = Element(pro_name, object_name)


class MainDataCategory(Base):
    """主数据-类目管理"""

    @allure.step("输入类目名称查询条件")
    def input_categoryName(self, categoryName):
        self.input_text(category['物料描述文本框'], categoryName)
        logging.info("输入类目名称：{}".format(categoryName))
        self.button_query()
        txt = self.element_text(category['列表数据断言'], 1, 3)
        if txt != categoryName:
            self.is_click(category['展开/收起 某行一级类目'], str(1))
            logging.info("展开二级类目")
        rowNum = self.get_rowNum(categoryName)
        value = self.element_text(category['列表数据断言'], rowNum, 3)
        return value

    @allure.step("点击查询按钮")
    def button_query(self):
        self.is_click(category['查询 按钮'])
        logging.info("点击查询按钮")
        sleep(1)

    @allure.step("点击重置按钮")
    def button_reset(self):
        self.is_click(category['重置 按钮'])
        logging.info("点击重置按钮")
        sleep(1)

    @allure.step("点击新增按钮")
    def button_add(self):
        self.is_click(category['新增 按钮'])
        sleep(1)
        txt = self.element_text(category['获取弹出窗 文本'])
        assert txt == "新增", logging.warning("打开新增窗口失败")
        logging.info("点击新增按钮，弹出新增窗口")

    @allure.step("选择上级类目")
    def choice_superiorCategory(self, superiorCategory):
        if superiorCategory is not None and superiorCategory != '':
            self.is_click(category['新增 上级类目下拉框'])
            self.scroll_into_view(category['下拉选项'], superiorCategory)
            self.is_click(category['下拉选项'], superiorCategory)
            logging.info("选择上级类目：{}".format(superiorCategory))
        else:
            logging.info("无需选择上级类目")

    @allure.step("维护类目-并保存")
    def maintain_category(self, superiorCategory, name_zh, name_en, type=None):
        self.choice_superiorCategory(superiorCategory)
        self.input_text(category['类目名称(中文)文本框'], name_zh)
        self.input_text(category['类目名称(英文)文本框'], name_en)
        self.is_click(category['保存按钮'])
        """场景及断言"""
        if type == "正例":
            txt = self.element_text(category['断言 保存提示信息'])
            assert txt == "Success",logging.warning("断言失败，新增失败")
            logging.info("新增保存成功，选择上级类目:{},类目名称(中文):{},类目名称(英文):{}".format(superiorCategory, name_zh, name_en))
        elif type == "反例 必填验证":
            if name_zh is None:
                txt = self.element_text(category['断言 中文类目名称为必填'])
                assert txt == "中文类目名称为必填", logging.warning("断言失败")
                logging.info("断言成功，中文类目名称为必填")
            if name_en is None:
                txt = self.element_text(category['断言 英文类目名称为必填'])
                assert txt == "英文类目名称为必填", logging.warning("断言失败")
                logging.info("断言成功，英文类目名称为必填")
            self.is_click(category['关闭弹窗'])  # 必填项未维护，关闭新增窗口
            logging.info("存在必填项未维护，关闭新增窗口")
        elif type == "反例 重复新增":
            txt = self.element_text(category['断言 保存提示信息'])
            result = re.findall('"message": "(.*?)" }', txt)[0]
            assert result == "编辑或新增失败，当前类目已存在！",logging.warning("断言失败，提示信息与预期不符")
            logging.info("断言成功，提示信息为：‘编辑或新增失败，当前类目已存在！’")

    @allure.step("点击编辑按钮")
    def button_edit(self,name_zh):
        rowNum = self.get_rowNum(name_zh)
        Npath = category['某行 编辑按钮'][1]
        Npath1 = Npath.replace('variable', str(rowNum))
        self.force_click(Npath1, xpath_js=True)
        sleep(1)
        txt = self.element_text(category['获取弹出窗 文本'])
        assert txt == "编辑", logging.warning("打开编辑窗口失败")
        logging.info("点击{}对应的编辑按钮，弹出编辑窗口".format(name_zh))

    @allure.step("编辑类目信息")
    def edit_categoryInf(self, name_zh=None,name_en=None, type=None):
        if type == "反例 必填校验":
            if name_zh is None:
                self.is_click(category['类目名称(中文)文本框'])
                self.is_click(category['清空 类目名称文本框'])
                self.is_click(category['弹窗空白处'])
                txt = self.element_text(category['断言 中文类目名称为必填'])
                assert txt == "中文类目名称为必填", logging.warning("断言失败")
                logging.info("断言成功，中文类目名称为必填")
            if name_en is None:
                self.is_click(category['类目名称(英文)文本框'])
                self.is_click(category['清空 类目名称文本框'])
                self.is_click(category['弹窗空白处'])
                txt = self.element_text(category['断言 英文类目名称为必填'])
                assert txt == "英文类目名称为必填", logging.warning("断言失败")
                logging.info("断言成功，英文类目名称为必填")
            self.is_click(category['关闭弹窗'])  # 必填项未维护，关闭窗口
        else:
            self.input_text(category['类目名称(中文)文本框'], name_zh)
            self.input_text(category['类目名称(英文)文本框'], name_en)
            self.is_click(category['保存按钮'])
            txt = self.element_text(category['断言 保存提示信息'])
            if type == "反例 重复":
                result = re.findall('"message": "(.*?)" }', txt)[0]
                assert result == "编辑失败，当前类目名称已存在！",logging.warning("断言失败")
                logging.info("编辑失败，当前类目已存在！")
            else:
                assert txt == "Success",logging.warning("断言失败")
                logging.info("编辑保存成功")
        self.refresh()

    @allure.step("获取类目名称所在行")
    def get_rowNum(self, name_zh):
        ele = self.find_elements(category['获取行号'])
        lis =[]
        for i in range(len(ele)):
            lis.append(ele[i].text)
        if name_zh in lis:
            rowNum = lis.index(name_zh) + 1  # 取到所传参数所在行号
            logging.info("获取类目名称{}所在行：{}".format(name_zh,rowNum))
            return rowNum

    @allure.step("操作类目状态窗口")
    def window_status(self,status):
        txt = self.element_text(category['获取 失效/启用 窗口文本'])
        if status == "失效":
            assert txt == "你确定要禁用该类目吗?", logging.warning("断言失败，打开窗口失败")
            logging.info("断言成功，打开状态修改窗口")
        else:
            assert txt == "你确定要启用该类目吗?", logging.warning("断言失败，打开窗口失败")
            logging.info("断言成功，打开状态修改窗口")
        self.is_click(category['状态窗口 确定按钮'])
        sleep(1)

    @allure.step("操作类目状态按钮")
    def button_status(self, name_zh):
        txt = self.element_text(category['列表数据断言'], 1, 3)
        if txt != name_zh:
            self.is_click(category['展开/收起 某行一级类目'], str(1))
            logging.info("展开二级类目")
        num = self.get_rowNum(name_zh)
        self.is_click(category['某行 编辑按钮'],str(num))
        txt1 = self.element_text(category['列表数据断言'],str(num),5)
        self.is_click(category['某行 失效/启用按钮'], str(num))
        if txt1 == "失效":
            self.window_status("启用")
            result = self.element_text(category['列表数据断言'], str(num), 5)
            assert result == "启用",logging.warning("断言失败，状态为 失效")
            logging.info("断言成功，操作类目启用成功")
        else:
            self.window_status("失效")
            result = self.element_text(category['列表数据断言'], str(num), 5)
            assert result == "失效",logging.warning("断言失败，状态为 启用")
            logging.info("断言成功，操作类目失效成功")

    @allure.step("查询数据库 用做断言")
    def get_sqlResult(self, sql):
        user = SQL("MIP", "test")
        value = user.query_db(sql)
        result = [item[key] for item in value for key in item]
        logging.info("查询数据库结果：{}".format(result))
        return result[0]

    @allure.step("清空测试数据")
    def clear_testData(self, name_zh):
        user = SQL("MIP", "test")
        user.delete_db("DELETE a from bb_category a ,(select category_id  from bb_category where category_name='{}') b "
                       "WHERE a.category_id = b.category_id".format(name_zh))
        logging.info("清空测试数据")

    @allure.step("前置条件，创建测试数据")
    def creat_testData(self, drivers, superiorCategory, name_zh,name_en):
        category = MainDataCategory(drivers)
        category.button_add()
        category.maintain_category(superiorCategory, name_zh, name_en,'正例')



if __name__ == '__main__':
    pass
