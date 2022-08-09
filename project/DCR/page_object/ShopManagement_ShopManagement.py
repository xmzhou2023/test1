from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
import random
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopManagementPage(Base):
    """ShopManagementPage 页面元素类"""

    @allure.step("点击Add新建门店按钮")
    def click_add(self):
        Base.presence_sleep_dcr(self, user['Add'])
        self.is_click(user['Add'])
        sleep(3)

    @allure.step("新建门店，输入门店名称")
    def input_shop_name(self, content):
        self.input_text(user['Shop Name'], txt=content)

    @allure.step("新建门店，输入联系人")
    def input_contact_name(self, content):
        self.input_text(user['Contact Name'], txt=content)

    @allure.step("新建门店，输入联系人电话")
    def input_contact_no(self, content):
        self.input_text(user['Contact No'], txt=content)

    @allure.step("新建门店时，输入国家城市")
    def input_country_city(self, content):
        self.is_click(user['Country City'])
        self.input_text(user['Country City'], txt=content)
        sleep(1)
        self.is_click(user['Country City value'])

    @allure.step("新建门店时，输入地址")
    def input_address(self, content):
        self.input_text(user['Address'], txt=content)

    @allure.step("新建门店时，选择品牌")
    def click_brand(self):
        self.is_click(user['Brand'])
        sleep(1)
        self.is_click(user['TECNO'], "TECNO")

    @allure.step("新建门店时，输入销售区域")
    def input_sales_region(self, content):
        self.scroll_into_view(user['Sales Region'])
        self.is_click(user['Sales Region'])
        self.input_text(user['Sales Region'], txt=content)
        sleep(1)
        self.is_click(user['Sales Region value'], "Barisal itel")
        sleep(1)

    @allure.step("新建门店时，选择门店等级")
    def click_shop_grade(self):
        self.is_click(user['Shop Grade'])
        sleep(2)
        self.is_click(user['Shop Grade Value'], "B 0-50 ")

    @allure.step("新建门店时，选择门店类型")
    def click_shop_type(self):
        self.is_click(user['Shop Type'])
        sleep(1)
        self.is_click(user['Shop Type GRT value'], "GRT")

    @allure.step("新建门店时，选择门店形象类型")
    def click_image_type(self):
        self.scroll_into_view(user['Image Type'])
        self.is_click(user['Image Type'])
        sleep(1)
        self.is_click(user['Zone Shop Value'], "Zone Shop")

    @allure.step("新建门店时，选择上传方式")
    def click_upload_mode(self):
        self.is_click(user['Inventory Upload mode'])
        sleep(1)
        self.is_click(user['Freedom value'], "Freedom")

    @allure.step("新建门店时，选择NO，输入门店关联的零售商ID")
    def input_retailer_account(self, content):
        self.is_click(user['点击No'])
        sleep(1)
        self.is_click(user['输入零售商'])
        self.input_text(user['输入零售商'], txt=content)
        sleep(2)
        self.is_click(user['选中零售商'], "SN455338 lhmRetailer005 ")

    @allure.step("新建门店时，选择商业区域")
    def click_commercial_area_tag(self):
        self.is_click(user['Commercial Area Tag'])
        sleep(1)
        self.is_click(user['Commercial Area value'], "IR")

    @allure.step("新建或者编辑门店时，点击提交")
    def click_submit(self):
        self.is_click_dcr(user['Submit'], "Submit")
        sleep(5)

    @allure.step("新建门店时，门店名称后缀随机生成")
    def shop_random(self):
        num = str(random.randint(100, 999))
        return num

    @allure.step("根据门店名称查询，最近新建的门店ID")
    def input_query_shop_name(self, content, content1):
        Base.presence_sleep_dcr(self, user['点击门店输入框'])
        self.is_click_dcr(user['点击门店输入框'])
        self.input_text(user['门店输入框输入'], txt=content)
        sleep(3)
        self.is_click(user['选中门店值1'], content1)

    @allure.step("根据门店名称查询，最近扩展门店品牌的的门店ID")
    def extend_query_shop_name(self, content, content1):
        self.is_click(user['点击门店输入框'])
        self.input_text_dcr(user['点击门店输入框'], txt=content)
        sleep(2.5)
        self.is_click(user['选中门店值2'], content1)

    @allure.step("点击Search查询门店信息")
    def click_query_search(self):
        self.is_click(user['Search'])
        sleep(6)

    @allure.step("筛选最近新建的门店ID后，勾线第一个复选框")
    def click_first_checkbox(self):
        Base.presence_sleep_dcr(self, user['勾选第一个复选框'])
        self.is_click(user['勾选第一个复选框'])

    @allure.step("勾选第二个复选框")
    def click_second_checkbox(self):
        self.is_click(user['勾选第二个复选框'])

    @allure.step("点击More Option更多操作按钮")
    def click_more_option(self):
        self.is_click(user['More Option'])
        sleep(2)

    @allure.step("点击delete 删除按钮")
    def click_delete(self):
        Base.presence_sleep_dcr(self, user['Delete'])
        self.is_click(user['Delete'])
        sleep(1)

    @allure.step("点击Confirm 确认删除按钮")
    def click_confirm_delete(self):
        self.is_click(user['Delete Confirm'])
        sleep(1)

    @allure.step("删除门店成功后，获取列表 successfully文本内容")
    def get_text_edit_success(self):
        success = self.element_text(user['Edited Successfully'])
        return success

    @allure.step("删除门店成功后，获取列表 successfully文本内容")
    def get_text_del_success(self):
        success = self.element_text(user['delete successfully'])
        return success

    @allure.step("删除门店成功后，获取列表 No Data文本内容")
    def get_text_nodata(self):
        nodata = self.element_text(user['No Data'])
        return nodata

    @allure.step("获取列表Shop ID文本")
    def get_shop_id_text(self):
        sleep(5)
        Base.presence_sleep_dcr(self, user['获取ShopID文本'])
        get_shop_id = self.element_text(user['获取ShopID文本'])
        return get_shop_id

    @allure.step("获取列表Shop ID文本")
    def get_extend_shop_id_text(self):
        Base.presence_sleep_dcr(self, user['获取ShopID文本'])
        get_shop_id = self.element_text(user['获取ShopID文本'])
        return get_shop_id

    @allure.step("获取列表Shop Name文本")
    def get_shop_name_text(self):
        Base.presence_sleep_dcr(self, user['获取ShopName文本'])
        get_shop_name = self.element_text(user['获取ShopName文本'])
        return get_shop_name

    @allure.step("获取列表brand文本")
    def get_shop_brand_text(self):
        get_brand = self.element_text(user['获取Brand文本'])
        return get_brand

    @allure.step("获取列表Status文本")
    def get_shop_status_text(self):
        get_status = self.element_text(user['获取Status文本'])
        return get_status

    @allure.step("点击Reset重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(5)

    # def query_sql_shopid(self):
    #     """查询最近新建的门店ID"""
    #     shop_data = connect_sql.query_db("select public_code,shop_name from  t_retail_shop_base where creator=99940 order by creation_time desc limit 1")
    #     shop_id = shop_data[0].get("public_code")
    #     shop_name = shop_data[0].get("shop_name")
    #     return shop_id, shop_name

    """门店扩展品牌"""
    @allure.step("点击More Option->Extend Brand扩展品牌按钮")
    def click_extend_brand(self):
        Base.presence_sleep_dcr(self, user['Extend Brand'])
        self.is_click(user['Extend Brand'])
        sleep(1)

    @allure.step("点击选择扩展品牌的输入框，然后选择扩展的品牌itel")
    def select_extend_brand(self, content):
        self.is_click(user['下拉选择扩展品牌'])
        self.input_text(user['下拉选择扩展品牌'], txt=content)
        sleep(2)
        self.is_click(user['选中扩展的品牌'])

    @allure.step("点击增加扩展品牌时，弹出窗口选择品牌后，点击Save")
    def extend_brand_save(self):
        self.is_click(user['Extend Brand Save'])
        sleep(4.5)

    @allure.step("编辑门店，增加扩展品牌时，输入销售区域并选择销售区域")
    def input_extend_sales_region(self, content):
        self.scroll_into_view(user['Extend Sales Region'])
        sleep(3)
        self.is_click(user['Extend Sales Region'])
        self.input_text(user['Extend Sales Region'], txt=content)
        sleep(2)
        self.is_click(user['Extend Sales Region Value'], content)

    @allure.step("扩展门店等级属性")
    def click_extend_shop_grade(self):
        self.scroll_into_view(user['Extend Shop Grade'])
        self.is_click(user['Extend Shop Grade'])
        sleep(2)
        self.is_click(user['Extend Shop Grade Value'], "A 10-20 ")

    @allure.step("扩展门店类型属性")
    def click_extend_shop_type(self):
        self.is_click(user['Extend Shop Type'])
        sleep(1.5)
        self.is_click(user['Extend Shop Type Value'], "CHIN")

    @allure.step("扩展门店形象属性")
    def click_extend_image_type(self):
        self.is_click(user['Extend Image Type'])
        sleep(1.5)
        self.is_click_dcr(user['Extend Zone Shop Value'], "Zone Shop")

    @allure.step("扩展零售商客户属性")
    def extend_retail_customer(self, content):
        self.is_click(user['扩展品牌输入零售商'])
        self.input_text(user['扩展品牌输入零售商'], txt=content)
        sleep(3)
        self.is_click_dcr(user['扩展品牌选中零售商'], content)

    @allure.step("扩展商业区域属性")
    def extend_commercial_area(self):
        self.is_click(user['Extend Commercial Area'])
        sleep(1.5)
        self.is_click_dcr(user['Extend Commercial Value'], "KA")

    #禁用门店
    @allure.step("点击禁用门店操作")
    def click_disable_confirm(self):
        Base.presence_sleep_dcr(self, user['Disable'])
        self.is_click(user['Disable'])
        sleep(2)
        Base.presence_sleep_dcr(self, user['Disable Confirm'])
        self.is_click(user['Disable Confirm'])

    @allure.step("关闭门店管理菜单")
    def click_close_shop_management(self):
        self.is_click(user['关闭门店管理菜单'])
        sleep(2)



if __name__ == '__main__':
    pass