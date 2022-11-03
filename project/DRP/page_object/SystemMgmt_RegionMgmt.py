import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import logging
from ..test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)



class AreaPage(Base):
    """区域管理"""

    @allure.step("前往树")
    def goto_tree(self, *content):
        for i in range(len(content)):
            if i == 0:
                self.is_click(user['tab区域总菜单'], choice=content[0])
                sleep(1)
                self.is_click(user['tab区域菜单一级菜单'], choice=content[0])
                sleep(1)
            elif i == 1:
                self.is_click(user['tab区域菜单二级菜单'], choice=content[1])
                sleep(1)
            elif i == 2:
                self.is_click(user['tab区域菜单三级菜单'], choice=content[2])
                sleep(1)
            elif i == 3:
                self.is_click(user['tab区域菜单四级菜单'], choice=content[3])
                sleep(1)
            elif i == 4:
                self.is_click(user['tab区域菜单五级菜单'], choice=content[4])
                sleep(1)

    @allure.step("区域导出")
    def download_area(self, content):
        self.check_download(user['区域导出'], content)

    def check_tree(self, text, allist):
        """判断树"""
        try:
            count = 0
            for i in range(len(allist)):
                if text in allist[i]:
                    logging.info("{} is in {}".format(text, allist[i]))
                    for j in range(1, len(allist[i])):
                        if text in allist[i][j]:
                            count = count + 1
                    return count
                else:
                    logging.info("{}is not in {}".format(text, allist[i]))
        except Exception as e:
            print(str(e))

    @allure.step("区域层级断言")
    def assert_area(self,value1=None, value2=None,value3=None):
        tier = self.element_text(user['区域层级断言'])
        org = self.element_text(user['名称断言'])
        if value3 is not None:
            tier1 = self.element_text(user['区域子层级断言'])
            assert tier1 == value3,logging.warning("区域子层级断言失败 {}!={}".format(value3,tier1))
            logging.info("区域子层级断言成功 {}={}".format(value3,tier1))
        assert tier == value1,logging.warning("区域层级断言失败 {}!={}".format(value1,tier))
        logging.info("区域层级断言成功 {}={}".format(value1,tier))
        assert org == value2,logging.warning("组织名称断言失败 {}!={}".format(value2,org))
        logging.info("组织名称断言成功 {}={}".format(value2,org))


    @allure.step("查询区域")
    def search_area(self, content):
        """查询区域"""
        self.input_text(user["区域搜索框"], content)
        logging.info("输入框键入{}".format(content))
        sleep(1)

    @allure.step("产品信息页-区域搜索框断言")
    def search_data(self):
        searchData = self.element_text(user['区域搜索框'])
        return searchData


    @allure.step("点击新增按钮")
    def add_button(self):
        self.is_click(user['新增'])
        sleep(1)

    @allure.step("点击保存按钮")
    def save_button(self):
        txt = self.element_text(user['区域层级断言'])
        if txt == "大区":
            self.is_click(user['保存'],str(7))
        elif txt == "国家":
            self.is_click(user['保存'],str(8))
        else:
            self.is_click(user['保存'],str(6))
        sleep(1)

    @allure.step("重复新增断言")
    def assert_add(self):
        txt = self.element_text(user['区域层级断言'])
        txt_hite = self.element_text(user['错误提示'])
        if txt_hite == "失败，数据已存在":
            logging.info("重复新增失败")
            if txt == "大区":
                self.is_click(user['取消'], str(7))
            elif txt == "国家":
                self.is_click(user['取消'], str(8))
            else:
                self.is_click(user['取消'], str(6))
            logging.info("取消新增")

    @allure.step("选择下拉选项")
    def chooseOption(self,value):
        option = self.find_elements(user['下拉列表'])
        lis = []
        for i in range(len(option)):
            lis.append(option[i].text)
        if value in lis:
            num = lis.index(value) + 1
            self.is_click(user['下拉选项'],str(num))
            logging.info("选择：{}".format(value))
        else:
            self.is_click(user['可输入下拉框'])
            logging.info("下拉列表无{}此选项，请重新选择".format(value))

    @allure.step("新增区域")
    def add_area(self, value, type=None):
        """新增区域"""
        txt = self.element_text(user['区域层级断言'])
        if txt != "国家" and txt != "大区":
            self.is_click(user['中文名称下拉框'])
            self.scroll_into_view(user['中文名称下拉选项'],value)
            self.is_click(user['中文名称下拉选项'],value)
        elif txt == "大区":
            self.is_click(user['中文名称下拉框(大区)'])
            self.scroll_into_view(user['中文名称下拉选项'],value)
            self.is_click(user['中文名称下拉选项'],value)
        else:
            self.is_click(user['可输入下拉框'],type)
            self.input_text(user['可输入下拉框'],value,choice=type)
            self.is_click(user['中文名称下拉选项'],value)

    @allure.step("指定行删除按钮")
    def del_list(self, num, area_name):
        """删除列表指定行数据"""
        a = self.find_elements(user['列表第n列'], str(num))
        b = []  # 取出列表第二列的所有文本
        for i in range(len(a)):
            b.append(a[i].text)
        if area_name in b:
            c = b.index(area_name) + 1  # 取到所传参数所在行号
            self.find_element(user['删除'],str(c)).click()  # 将行号c替换到xpath中进行相关操作
        sleep(1)

    @allure.step("删除断言")
    def del_assert(self):
        txt = self.element_text(user['错误提示'])
        assert txt == "失败，数据已被使用",logging.warning("删除断言失败")
        logging.info("删除断言成功")

    @allure.step("前置条件-新增指定区域")
    def precondition(self,drivers,tier):
        user = AreaPage(drivers)
        if tier == 2:
            user.goto_tree('Infinix事业部')
            user.add_button()  # 点击新增按钮
            user.add_area('其他')  # 输入地区中英文名称
            user.save_button()  # 点击保存按钮
        elif tier == 3:
            user.goto_tree('Infinix事业部')
            user.add_button()  # 点击新增按钮
            user.add_area('其他')  # 输入地区中英文名称
            user.save_button()  # 点击保存按钮
            user.goto_tree('Infinix事业部','其他')
            user.add_button()  # 点击新增按钮
            user.add_area('其他')  # 输入地区中英文名称
            user.save_button()  # 点击保存按钮
        elif tier == 4:
            user.goto_tree('Infinix事业部')
            user.add_button()  # 点击新增按钮
            user.add_area('其他')  # 输入地区中英文名称
            user.save_button()  # 点击保存按钮
            user.goto_tree('Infinix事业部','其他')
            user.add_button()  # 点击新增按钮
            user.add_area('其他')  # 输入地区中英文名称
            user.save_button()  # 点击保存按钮
            user.goto_tree('Infinix事业部','其他','其他')
            user.add_button()  # 点击新增按钮
            user.add_area('迪拜')  # 输入地区中英文名称
            user.save_button()  # 点击保存按钮
        elif tier == 5:
            user.goto_tree('Infinix事业部')
            user.add_button()  # 点击新增按钮
            user.add_area('其他')  # 输入地区中英文名称
            user.save_button()  # 点击保存按钮
            user.goto_tree('Infinix事业部','其他')
            user.add_button()  # 点击新增按钮
            user.add_area('其他')  # 输入地区中英文名称
            user.save_button()  # 点击保存按钮
            user.goto_tree('Infinix事业部','其他','其他')
            user.add_button()  # 点击新增按钮
            user.add_area('迪拜')  # 输入地区中英文名称
            user.save_button()  # 点击保存按钮
            user.goto_tree('Infinix事业部','其他','其他','迪拜')
            user.add_button()  # 点击新增按钮
            user.add_area('贝宁')  # 输入地区中英文名称
            user.save_button()  # 点击保存按钮

    @allure.step("前置条件-新增目标区域")
    def precondition1(self,drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.add_button()  # 点击新增按钮
        user.add_area('新市场')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        user.goto_tree('Infinix事业部','新市场')
        user.add_button()  # 点击新增按钮
        user.add_area('东非地区')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        user.goto_tree('Infinix事业部', '新市场','东非地区')
        user.add_button()  # 点击新增按钮
        user.add_area('东非一区')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮

    @allure.step("前置条件-新增目标区域")
    def precondition2(self,drivers):
        user = AreaPage(drivers)
        user.add_button()  # 点击新增按钮
        user.add_area('孟加拉')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮

    @allure.step("清空测试数据")
    def clear_testdata(self):
        user = SQL("DRP", "test")
        user.delete_db(
            "DELETE from cd_dimension_area where creator_name = '隆江'")
        logging.info("清空测试数据")

    @allure.step("前置条件-编辑国家信息")
    def precondition_contry(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部','其他','其他', '迪拜','贝宁')
        user.add_button()  # 点击新增按钮
        user.add_area('Infinix','品牌')  # 选择品牌
        user.add_area('公开市场','市场分类')  # 选择市场分类
        user.add_area('Infinix事业部','组织')  # 选择组织
        user.add_area('Infinix事业部','部门')  # 选择部门
        user.add_area('Infinix事业部','事业部')  # 选择事业部
        user.save_button()  # 点击保存按钮

    @allure.step("指定行编辑按钮")
    def edit_list(self, num, area_name):
        """编辑列表指定行数据"""
        a = self.find_elements(user['列表第n列'], str(num))
        b = []  # 取出列表第二列的所有文本
        for i in range(len(a)):
            b.append(a[i].text)
        if area_name in b:
            c = b.index(area_name) + 1  # 取到所传参数所在行号
            self.find_element(user['编辑'],str(c)).click()  # 将行号c替换到xpath中进行相关操作
        sleep(1)

    @allure.step("编辑后断言")
    def edit_assert(self, num, area_name):
        """编辑列表指定行数据"""
        a = self.find_elements(user['列表第n列'], str(num))
        b = []  # 取出列表第二列的所有文本
        for i in range(len(a)):
            b.append(a[i].text)
        assert area_name in b,logging.warning("编辑断言失败")
        logging.info("编辑断言成功")
        return b

    @allure.step("移动国家")
    def move_button(self,num,area_name):
        """点击移动到按钮，打开弹窗"""
        sleep(2)
        a = self.find_elements(user['列表第n列'], str(num))
        b = []  # 取出列表第二列的所有文本
        for i in range(len(a)):
            b.append(a[i].text)
        if area_name in b:
            c = b.index(area_name) + 1  # 取到所传参数所在行号
            self.find_element(user['移动到'],str(c)).click()  # 将行号c替换到xpath中进行相关操作
        sleep(1)
        txt = self.element_text(user['弹窗断言'])
        assert txt == "移动到",logging.warning("打开移动弹窗失败")
        logging.info("打开{} 移动弹窗".format(area_name))

    @allure.step("移动国家")
    def choice_target(self,value1,value2,value3):
        self.is_click(user['移动到 复选框'])
        self.is_click(user['市场划分下拉选项'], value1)
        try:
            txt = self.element_text(user['暂无数据 断言'])
            assert txt == "暂无数据",logging.warning("区域有数据")
            logging.info("区域无数据，断言成功")
            self.is_click(user['关闭弹窗'])
            logging.info("关闭移动弹窗")
        except:
            self.is_click(user['区域下拉选项'], value2)
            self.is_click(user['大区下拉选项'], value3)
            logging.info("选择移动国家完成，{}/{}/{}".format(value1,value2,value3))

    @allure.step("确认移动")
    def move_affirm(self,num, area_name):
        self.is_click(user['确定 按钮'])
        try:
            txt = self.element_text(user['列表 无数据 断言'])
            assert txt == '暂无数据',logging.warning("xx")
            logging.info("国家移动成功")
        except:
            txt1 = self.edit_assert(num, area_name)
            assert area_name not in txt1,logging.warning("断言失败，国家未完成移动")
            logging.info("断言成功，原大区没有{}国家".format(area_name))


    @allure.step("选择移动国家 多选")
    def choice_country(self,num,area_name):
        a = self.find_elements(user['列表第n列'], str(num))
        b = []  # 取出列表第二列的所有文本
        for i in range(len(a)):
            b.append(a[i].text)
        if area_name in b:
            c = b.index(area_name) + 1  # 取到所传参数所在行号
            self.find_element(user['复选框'],str(c)).click()  # 将行号c替换到xpath中进行相关操作
        logging.info("勾选国家{}".format(area_name))

    @allure.step("批量操作-移动")
    def bulk_operation(self):
        self.is_click(user['批量操作 按钮'])
        sleep(1)
        self.is_click(user['批量移动 按钮'])
        sleep(1)
        txt = self.element_text(user['弹窗断言'])
        assert txt == "移动到",logging.warning("打开移动弹窗失败")
        logging.info("打开移动弹窗")

    @allure.step("选择移动国家 全选")
    def choice_all(self):
        self.is_click(user['全选'])
        logging.info("全选完成")





if __name__ == '__main__':
    pass

