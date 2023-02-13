import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
import logging
from ..test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)
from project.POP.page_object.Center_Component import *

class QueryShop(Page_Operation, General_button):
    """按条件查询门店"""
    select_list1 = {"门店列表-门店框": "门店列表-门店", "门店列表-组织框": "门店列表-组织", "门店列表-国家框": "门店列表-国家","门店列表-门店等级框":"门店列表-门店等级"}
    select_list2 = {"门店列表-销量等级框": "门店列表-销量等级", "门店列表-状态框": "门店列表-状态","门店列表-区域框":"门店列表-区域"}

    def queryhop(self, select, content, ele2=None, enddate=None):
        if select in self.select_list1:
            self.single_condition_input_boxquery(select, self.select_list1[select], content)
            sleep()
            self.query()
        elif select in self.select_list2:
            self.more()
            sleep()
            self.single_condition_input_boxquery(select, self.select_list2[select], content)
            sleep()
            self.more_query()
        elif select == "开始日期框":
            self.date_range(select, ele2, content, enddate)
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")


class AddShop(Base):
    """门店新增类"""

    @allure.step("点击门店新增")
    def click_add(self):
        self.is_click_tbm(user['新增门店按钮'])

    @allure.step("输入门店名称")
    def input_shopname(self,shopname):
        self.input_text(user['新增门店名称'],shopname)

    @allure.step("选择组织")
    def switch_organization(self,organization):
        self.is_click_tbm(user['组织下拉框'])
        self.input_text(user['组织下拉框'],organization)
        sleep(1)
        self.is_click_tbm(user['选择组织'],organization)

    @allure.step("选择国家")
    def switch_country(self,country):
        self.is_click_tbm(user['国家下拉框'])
        self.input_text(user['国家下拉框'],country)
        sleep(1)
        self.is_click_tbm(user['选择国家'],country)

    @allure.step("选择省")
    def switch_province(self,province):
        self.is_click_tbm(user['省下拉框'])
        self.input_text(user['省下拉框'],province)
        sleep(1)
        self.is_click_tbm(user['选择省'],province)

    @allure.step("选择城市")
    def switch_city(self,city):
        self.is_click_tbm(user['城市下拉框'])
        self.input_text(user['城市下拉框'],city)
        sleep(1)
        self.is_click_tbm(user['选择城市'],city)

    @allure.step("输入详细地址")
    def input_address(self,address):
        self.input_text(user['详细地址'],address)

    @allure.step("选择城市等级")
    def switch_city_level(self,citylevel):
        self.is_click_tbm(user['城市等级下拉框'])
        self.input_text(user['城市等级下拉框'],citylevel)
        sleep(1)
        self.is_click_tbm(user['选择城市等级'],citylevel)

    @allure.step("选择区域")
    def switch_region(self,region):
        self.is_click_tbm(user['区域下拉框'])
        self.input_text(user['区域下拉框'],region)
        sleep(1)
        self.is_click_tbm(user['选择区域'],region)

    @allure.step("输入建店联系人")
    def input_linkman(self,linkman):
        self.input_text(user['建店联系人'],linkman)

    @allure.step("输入手机")
    def input_phone(self,phone):
        self.input_text(user['手机'],phone)

    @allure.step("选择门店等级")
    def switch_shop_level(self,shoplevel):
        self.is_click_tbm(user['门店等级下拉框'])
        self.input_text(user['门店等级下拉框'],shoplevel)
        sleep(1)
        self.is_click_tbm(user['选择门店等级'],shoplevel)

    @allure.step("选择形象等级")
    def switch_image_level(self,imagelevel):
        self.is_click_tbm(user['形象等级下拉框'])
        self.input_text(user['形象等级下拉框'],imagelevel)
        sleep(1)
        self.is_click_tbm(user['选择形象等级'],imagelevel)

    @allure.step("选择销量等级")
    def switch_sales_volume_level(self,saleslevel):
        self.is_click_tbm(user['销量等级下拉框'])
        self.input_text(user['销量等级下拉框'],saleslevel)
        sleep(3)
        self.is_click_tbm(user['选择销量等级'],saleslevel)

    @allure.step("选择所有权")
    def switch_ownership(self,ownership):
        self.is_click_tbm(user['所有权下拉框'])
        self.input_text(user['所有权下拉框'],ownership)
        sleep(1)
        self.is_click_tbm(user['选择所有权'],ownership)

    @allure.step("输入门店面积")
    def input_shop_square_measure(self,square):
        self.input_text(user['门店面积'],square)

    @allure.step("输入门店层高")
    def input_shop_storey_height(self,height):
        self.input_text(user['门店层高'],height)

    @allure.step("上传原型尺寸图纸、照片、视频")
    def upload_drawing_video(self,drawing,video):
        sleep(2)
        # 滑动页面定位原型尺寸图纸上传图片按钮
        self.scroll_into_view(user['原型尺寸图纸'])
        self.upload_file(user['原型尺寸图纸上传'],drawing)
        self.upload_file(user['门头立面照片_远景上传'],drawing)
        self.upload_file(user['门头立面照片_近景上传'],drawing)
        self.upload_file(user['店内正视图上传'],drawing)
        self.upload_file(user['店铺实景图片上传'],drawing)
        self.upload_file(user['视频上传'],video)
        # 滑动页面定位其他上传图片按钮
        self.scroll_into_view(user['其他'])
        self.upload_file(user['其他上传'],drawing)
        sleep(3)

    @allure.step("增加人员信息")
    def add_userinformation(self,username):
        self.is_click_tbm(user['人员信息新增按钮'])
        self.is_click_tbm(user['人员信息员工ID输入框'])
        self.input_text(user['人员信息员工ID输入框'],username)
        sleep(1)
        self.is_click_tbm(user['选择人员信息员工ID输入框'],username)

    @allure.step("输入门店预估月销量")
    def input_shop_monthlysales(self,sales):
        self.input_text(user['门店预估月销量'],sales)

    @allure.step("点击提交按钮")
    def click_submit(self):
        self.is_click_tbm(user['提交按钮'])






if __name__ == '__main__':
    pass
