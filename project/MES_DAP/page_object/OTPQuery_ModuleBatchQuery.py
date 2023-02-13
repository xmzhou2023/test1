import os.path
import allure
from ..test_case.conftest import *
from libs.common.read_element import Element
from public.base.basics import Base

object_name = os.path.basename(__file__).split('.')[0]
otpData = Element(pro_name, object_name)


class ModuleBatchQuery(Base):
    """OTP批次数据查询"""

    @allure.step("输入物料编码")
    def input_matcode(self, matcode):
        self.input_text(otpData["物料编码输入框"], matcode)

    @allure.step("输入sensorID")
    def input_sensorID(self, sensorID):
        self.input_text(otpData["sensorID输入框"], sensorID)

    @allure.step("输入模组单体SN")
    def input_sn(self, sn):
        self.input_text(otpData["模组单体SN输入框"], sn)

    @allure.step("输入箱号")
    def input_cartonNo(self, cartonNo):
        self.input_text(otpData["箱号输入框"], cartonNo)

    @allure.step("输入供应商名称")
    def input_supplierName(self, supplierName):
        self.input_text(otpData["供应商名称输入框"], supplierName)

    @allure.step("输入客户生产工厂")
    def input_factoryName(self, factoryName):
        self.input_text(otpData["客户生产工厂输入框"], factoryName)

    @allure.step("输入供应商生产时间")
    def input_ProduceTime(self, starProduceTime, endProduceTime):
        self.input_text(otpData["供应商生产开始日期选择框"], starProduceTime)
        self.input_text(otpData["供应商生产结束日期选择框"], endProduceTime)

    @allure.step("点击查询按钮")
    def click_querry(self):
        self.is_click(otpData["查询按钮"])

    @allure.step("点击重置按钮")
    def click_reset(self):
        self.is_click(otpData["重置按钮"])

    @allure.step("点击拉取总部数据按钮")
    def click_pull(self):
        self.is_click(otpData["拉取总部数据按钮"])

    @allure.step("获取列表title")
    def get_titles(self):
        return self.element_text(otpData["表格title"]).split()


    @allure.step("根据列名获取列数据")
    def get_cols_values(self, *title):
        values = {}
        titles = self.get_titles()
        for i in list(title):
            if i:
                try:
                    col_elements = self.find_elements(otpData["表格第n列"], str(titles.index(i)+1))
                    col_texts = []
                    for j in range(len(col_elements)):
                        col_texts.append(col_elements[j].text)
                    values[i] = col_texts
                except:
                    logging.info("列名(%s)不存在" % i)
        return values