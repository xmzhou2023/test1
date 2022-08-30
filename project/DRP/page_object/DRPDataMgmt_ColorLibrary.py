import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class ColorLibrary(Base):
    """颜色库"""

    @allure.step("输入颜色")
    def input_color(self, option):
        self.input_text(user['查询条件 颜色'],option)
        logging.info("查询颜色：{}".format(option))

    @allure.step("选择可用状态")
    def choice_state(self, option):
        self.is_click(user['查询条件 可用状态'])
        if option == "启用":
            self.is_click(user['可用状态下拉选项'],"2")
        else:
            self.is_click(user['可用状态下拉选项'],"1")
        logging.info("查询可用状态：{}".format(option))

    @allure.step("点击查询按钮")
    def query_button(self):
        self.is_click(user['查询按钮'])
        logging.info("点击查询按钮")

    @allure.step("清空查询条件")
    def reset_button(self):
        self.is_click(user['重置按钮'])
        logging.info("点击重置按钮")

    @allure.step("列表数量断言")
    def listnum_assert(self):
        return self.element_text(user['列表条数（断言）'])



    @allure.step("结果断言方法")
    def assert_method(self, color, num):
        colorList = self.find_elements(user['获取列表指定列所有文本'],num)
        print(colorList)
        resultList = []
        for i in range(len(colorList)):
            resultList.append(colorList[i].text)
        try:
            assert color in resultList, logging.warning("断言失败: a 不包含 b | a:{} b:{}".format(resultList, color))
            logging.info("断言成功: a 包含 b | a:{} b:{}".format(resultList, color))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("查询结果断言")
    def screen_assert(self, condition, color):
        if condition == "颜色编码":
            self.assert_method(color,"2")
        elif condition == "颜色名称Zh":
            self.assert_method(color, "3")
        elif condition == "颜色名称Eh":
            self.assert_method(color, "4")
        else:
            self.assert_method(color, "1")

    @allure.step("导出Excel")
    def export_button(self,content):
        try:
            self.check_download(user['导出按钮'], content)
        except Exception:
            logging.info("断言失败: 下载该附件失败")



if __name__ == '__main__':
    pass
