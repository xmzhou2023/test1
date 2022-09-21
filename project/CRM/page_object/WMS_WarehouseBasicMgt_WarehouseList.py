from selenium.webdriver.support import expected_conditions as EC
import allure, os

from libs.config.conf import DOWNLOAD_PATH
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class WarehouseList(Base):
    """仓库列表"""

    @allure.step("查询仓库")
    def search_warehousetype(self, type):
        self.is_click(user["Warehouse Type"])
        self.input_text(user['Warehouse Type'],type)
        sleep(0.5)
        self.is_click_tbm(user["下拉筛选第一条数据"])
        sleep(0.5)
        self.is_click(user['Search'])

    def get_total1(self):
        sleep(0.5)
        total = self.element_text(user["total数量"])
        logging.info("获取total文本{}".format(total))
        num = total.split(" ",1)
        number = num[1]
        return number

    @allure.step("查询仓库")
    def search_warehousecode(self,code):
        self.is_click(user["Warehouse Code"])
        self.input_text(user["Warehouse Code"],code)
        sleep(0.5)
        self.is_click(user['Search'])

    def get_total2(self):
        sleep(0.5)
        total1 = self.element_text(user["total数量2"])
        logging.info("huoqu total文本{}".format(total1))
        num = total1.split(" ",1)
        number1 = num[1]
        return number1



    @allure.step("编辑仓库数据")
    def edit_warehouse(self,wcode):
        self.is_click_tbm(user["Edit"])
        self.input_text(user["code输入框"],wcode)
        sleep(0.5)
        self.is_click(user["save"])



    @allure.step("下载仓库模板")
    def check_warehousetemplate(self, content):
        """下载模板"""
        # self.clear_download(DOWNLOAD_PATH)
        self.is_click_tbm(user["Import"])
        self.is_click_tbm(user["Download Template"])
        self.is_click_tbm(user["关闭下载框"])
        assert self.download_file(filename=content, load=3), logging.warning("断言失败: 下载该附件失败 | {} ".format(content))
        logging.info("断言成功: 下载该附件成功 | {} ".format(content))




    # @allure.step("新增仓库")
    # def add_warehouse(self,code,name,type,parent,Assignment,contacts,no,address1,keeper):
    #     self.is_click(user["Add"])
    #     self.input_text(user["新增code输入框"],code)
    #     self.input_text(user["新增name输入框"],name)
    #     self.input_text(user["新增type下拉框"],type)
    #     sleep(0.3)
    #     self.is_click_tbm(user["type下拉第一条数据"])
    #     self.input_text(user["新增parent下拉框"],parent)
    #     sleep(1)
    #     self.hover(user["parent下拉第一条数据"])
    #     self.is_click(user["parent下拉第一条数据"])
    #     sleep(1)
    #     self.hover(user["新增company搜索框"])
    #     self.is_click_tbm(user["新增company搜索框"])
    #     sleep(0.3)
    #     self.hover(user["company搜索第一条数据"])
    #     self.is_click_tbm(user["company搜索第一条数据"])
    #
    #     self.input_text(user["新增Assignment搜索框"],Assignment)
    #     sleep(0.3)
    #     self.is_click_tbm(user["Assignment下拉第五条数据"])
    #
    #     self.input_text(user["新增contacts搜索框"],contacts)
    #     sleep(0.3)
    #     self.is_click_tbm(user["contacts搜索第一条数据"])
    #     self.input_text(user["新增contacts no输入框"],no)
    #     self.is_click_tbm(user["新增address下拉框"])
    #     sleep(0.3)
    #     self.is_click_tbm(user["address下拉第一条数据"])
    #     self.input_text(user["address详情"],address1)
    #     self.input_text(user["新增keeper搜索框"],keeper)
    #     sleep(0.3)
    #     self.is_click_tbm(user["keeper搜索第一条数据"])
    #     self.is_click(user["新增保存"])
    #     wan = self.wait.until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Happy_Thur')]".format(code)))).text
    #     assert code in wan, logging.warning("断言失败：页面不存在该标识 | 当前页面关键字: {}".format(wan.replace("\n", "|")))
    #     logging.info("断言成功：页面存在该标识 | 当前页面关键字: {}".format(wan.replace("\n", "|")))








if __name__ == '__main__':
    pass
