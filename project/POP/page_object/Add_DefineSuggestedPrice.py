import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *
from conftest import *
from project.POP.page_object.Center_Component import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AddDefineSuggestedPrice(Base):
    """新增定义建议价格类"""

    @allure.step("点击新增")
    def click_button(self,content):
        self.is_click(user["按钮"],content)



    @allure.step("新增页面-输入商品名称")
    def click_productname(self,content):
        sleep(1)
        self.is_click(user["商品名称输入框"])
        self.input_text(user["商品名称输入框"],content)
        sleep(2)
        self.is_click_tbm(user["输入商品"],content)

    @allure.step("商品名称筛选")
    def click_commodityname(self,content):
        self.is_click_tbm(user["商品名称筛选框"])
        self.input_text(user["商品名称筛选框"],content)
        sleep(2)
        self.is_click_tbm(user["商品"],content)

    @allure.step("产品名称筛选")
    def click_productnamechoice(self,content):
        self.is_click_tbm(user["产品名称筛选框"])
        self.input_text(user["产品名称筛选框"],content)
        sleep(1)
        self.is_click_tbm(user["产品搜索结果"],content)


    @allure.step("品牌名称筛选")
    def click_brandname(self,content):
        self.is_click_tbm(user["品牌名称筛选框"])
        # self.input_text(user['品牌名称筛选框'],content)
        sleep(2)
        self.is_click_tbm(user["选择的品牌"],content)



    @allure.step("点击查询按钮")
    def click_search(self,content):
        self.is_click_tbm(user["查询按钮"],content)


    @allure.step("点击勾选框")
    def click_tickbox(self):
        self.is_click_tbm(user["勾选框"])

    @allure.step("点击确认按钮")
    def click_confirm(self):
        # js = "document.getElementsByClassName('el-tooltip__popper is-dark')[0].style.display='block'";
        # driver.executeScript(js)
        self.is_click_tbm(user["确认按钮"])

    @allure.step("点击新增按钮")
    def click_addbutton(self,money,region):
        self.scroll_into_view(user["Add按钮"])
        self.is_click(user["Add按钮"])
        self.is_click(user["区域输入框"])
        # self.is_click(user["顶级三角按钮"])
        self.input_text(user["区域输入框"],region)
        self.is_click(user["区域"],region)
        self.is_click(user["销售币种输入框"])
        self.is_click(user["CNY"])
        self.is_click(user["建议零售价输入框"])
        self.input_text(user["建议零售价输入框"],money)
        self.scroll_into_view(user["保存按钮"])
        self.is_click(user["保存按钮"])

    @allure.step("编辑价格")
    def click_edit_price(self,money):
        self.is_click(user["建议零售价输入框"])
        self.input_text(user["建议零售价输入框"], money)
        self.scroll_into_view(user["保存按钮"])
        self.is_click(user["保存按钮"])

    @allure.step("数据库查询新增定义建议价格断言")
    def sql_priceassert(self,count,good,region):
        sql = f"SELECT count(*) FROM `goods_price` WHERE `goods_id` = {good} AND `area_id`={region} AND `enabled_flag`=1;"
        SQLAssert('POP','test').assert_sql_count(count, sql)

class ExportPrice(Base):
    """导出定义建议价格类"""

    @allure.step("品牌名称筛选")
    def click_brandname(self, content):
        self.is_click_tbm(user["品牌名称筛选框"])
        sleep(2)
        self.is_click_tbm(user["选择的品牌"], content)

    @allure.step("点击查询按钮")
    def click_search(self, content):
        self.is_click_tbm(user["查询按钮"], content)

    @allure.step("点击导出")
    def click_export(self,content):
        self.is_click_tbm(user["按钮"],content)

class QueryGoodSugPrice(Page_Operation,General_button):
    """按条件查询商品规格"""
    select_list1 = {"定义建议价格-商品名称框":"定义建议价格-商品名称","定义建议价格-品牌名称框":"定义建议价格-品牌名称","定义建议价格-产品名称框":"定义建议价格-产品名称"}
    select_list2 = {"定义建议价格-区域框":"定义建议价格-区域","定义建议价格-自采标记框":"定义建议价格-自采标记","定义建议价格-创建人框":"定义建议价格-创建人"}
    def querygoodprice(self,select,content,ele2=None,enddate=None):
        if select in self.select_list1:
            self.single_condition_input_boxquery(select,self.select_list1[select],content)
            sleep()
            self.query()
        elif select in self.select_list2:
            self.more()
            sleep()
            self.single_condition_input_boxquery(select,self.select_list2[select],content)
            sleep()
            self.more_query()
        elif select == "定义建议价格-开始日期框":
            self.date_range(select,ele2,content,enddate)
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")


if __name__ == '__main__':
    pass
