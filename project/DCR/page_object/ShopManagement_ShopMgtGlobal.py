from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
import random
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopManagementPage(Base):
    """ShopManagementPage 页面元素类"""
    def click_add(self):
        """点击Add新建门店按钮"""
        Base.presence_sleep_dcr(self, user['Add'])
        self.is_click(user['Add'])
        sleep(3)

    def input_shop_name(self, content):
        """新建门店，输入门店名称"""
        self.input_text(user['Shop Name'], txt=content)

    def input_contact_name(self, content):
        """新建门店，输入联系人"""
        self.input_text(user['Contact Name'], txt=content)

    def input_contact_no(self, content):
        """新建门店，输入联系人电话"""
        self.input_text(user['Contact No'], txt=content)

    def input_country_city(self, content):
        """新建门店时，输入国家城市"""
        self.is_click(user['Country City'])
        self.input_text(user['Country City'], txt=content)
        sleep(1)
        self.is_click(user['Country City value'])

    def input_address(self, content):
        """新建门店时，输入地址"""
        self.input_text(user['Address'], txt=content)

    def click_brand(self):
        """新建门店时，选择品牌"""
        self.is_click(user['Brand'])
        sleep(1)
        self.is_click(user['TECNO'], "TECNO")

    def input_sales_region(self, content):
        """新建门店时，输入销售区域"""
        self.is_click(user['Sales Region'])
        self.input_text(user['Sales Region'], txt=content)
        sleep(1)
        self.is_click(user['Sales Region value'])

    def click_shop_grade(self):
        """新建门店时，选择门店等级"""
        self.is_click(user['Shop Grade'])
        sleep(2)
        self.is_click(user['Shop Grade Value'], "B 0-50 ")

    def click_shop_type(self):
        """新建门店时，选择门店类型"""
        self.is_click(user['Shop Type'])
        sleep(1)
        self.is_click(user['Shop Type GRT value'], "GRT")

    def click_image_type(self):
        """新建门店时，选择门店形象类型"""
        self.scroll_into_view(user['Image Type'])
        self.is_click(user['Image Type'])
        sleep(1)
        self.is_click(user['Zone Shop Value'], "Zone Shop")

    def click_upload_mode(self):
        """新建门店时，选择上传方式"""
        self.is_click(user['Inventory Upload mode'])
        sleep(1)
        self.is_click(user['Freedom value'], "Freedom")

    def input_retailer_account(self, content):
        """新建门店时，选择NO，输入门店关联的零售商ID"""
        self.is_click(user['点击No'])
        self.is_click(user['输入零售商'])
        self.input_text(user['输入零售商'], txt=content)
        sleep(2)
        self.is_click(user['选中零售商'])

    def click_commercial_area_tag(self):
        """新建门店时，选择商业区域"""
        self.is_click(user['Commercial Area Tag'])
        sleep(1)
        self.is_click(user['Commercial Area value'], "IR")

    def click_submit(self):
        """新建或者编辑门店时，点击提交"""
        self.is_click_dcr(user['Submit'])


    def shop_random(self):
        """新建门店时，门店名称后缀随机生成"""
        num = str(random.randint(100, 999))
        return num

    def input_query_shop_name(self, content, content1):
        """根据门店名称查询，最近新建的门店ID"""
        #Base.presence_sleep_dcr(self, user['点击门店输入框'])
        self.is_click_dcr(user['点击门店输入框'])
        self.input_text(user['门店输入框输入'], txt=content)
        sleep(3)
        self.is_click(user['选中门店值1'], content1)

    def extend_query_shop_name(self, content, content1):
        """根据门店名称查询，最近扩展门店品牌的的门店ID"""
        self.is_click(user['点击门店输入框'])
        self.input_text_dcr(user['点击门店输入框'], txt=content)
        sleep(2.5)
        self.is_click(user['选中门店值2'], content1)

    def click_query_search(self):
        """点击Search查询门店信息"""
        self.is_click(user['Search'])
        sleep(4)

    def click_first_checkbox(self):
        """筛选最近新建的门店ID后，勾线第一个复选框"""
        self.is_click(user['勾选第一个复选框'])

    def click_more_option(self):
        """点击More Option更多操作按钮"""
        self.is_click(user['More Option'])
        sleep(1)

    def click_delete(self):
        """点击delete 删除按钮"""
        self.is_click(user['Delete'])
        sleep(1)

    def click_confirm_delete(self):
        """点击Confirm 确认删除按钮"""
        self.is_click(user['Delete Confirm'])

    def get_text_edit_success(self):
        """删除门店成功后，获取列表 successfully文本内容"""
        success = self.element_text(user['Edited Successfully'])
        return success

    def get_text_del_success(self):
        """删除门店成功后，获取列表 successfully文本内容"""
        success = self.element_text(user['delete successfully'])
        return success

    def get_text_nodata(self):
        """删除门店成功后，获取列表 No Data文本内容"""
        nodata = self.element_text(user['No Data'])
        return nodata

    def get_shop_id_text(self):
        """获取列表Shop ID文本"""
        Base.presence_sleep_dcr(self, user['获取ShopID文本'])
        get_shop_id = self.element_text(user['获取ShopID文本'])
        return get_shop_id

    def get_extend_shop_id_text(self):
        """获取列表Shop ID文本"""
        get_shop_id = self.element_text(user['获取ShopID文本'])
        return get_shop_id

    def get_shop_name_text(self):
        """获取列表Shop Name文本"""
        Base.presence_sleep_dcr(self, user['获取ShopName文本'])
        get_shop_name = self.element_text(user['获取ShopName文本'])
        return get_shop_name

    def get_shop_brand_text(self):
        """获取列表brand文本"""
        get_brand = self.element_text(user['获取Brand文本'])
        return get_brand

    def get_shop_status_text(self):
        """获取列表Status文本"""
        get_status = self.element_text(user['获取Status文本'])
        return get_status

    def click_reset(self):
        """点击Reset重置按钮"""
        self.is_click(user['Reset'])
        sleep(5)

    # def query_sql_shopid(self):
    #     """查询最近新建的门店ID"""
    #     shop_data = connect_sql.query_db("select public_code,shop_name from  t_retail_shop_base where creator=99940 order by creation_time desc limit 1")
    #     shop_id = shop_data[0].get("public_code")
    #     shop_name = shop_data[0].get("shop_name")
    #     return shop_id, shop_name

    """门店扩展品牌"""
    def iframe_shop_edit(self):
        """进入门店扩展品牌页面iframe"""
        self.frame_enter(user['iframe shop edit'])
        sleep(1)

    def click_extend_brand(self):
        """点击More Option->Extend Brand扩展品牌按钮"""
        self.is_click(user['Extend Brand'])
        sleep(1)

    def select_extend_brand(self, content):
        """点击选择扩展品牌的输入框，然后选择扩展的品牌itel"""
        self.is_click(user['下拉选择扩展品牌'])
        self.input_text(user['下拉选择扩展品牌'], txt=content)
        sleep(2)
        self.is_click(user['选中扩展的品牌'])

    def extend_brand_save(self):
        """点击增加扩展品牌时，弹出窗口选择品牌后，点击Save"""
        self.is_click(user['Extend Brand Save'])
        sleep(4.5)

    def input_extend_sales_region(self, content):
        """编辑门店，增加扩展品牌时，输入销售区域并选择销售区域"""
        self.scroll_into_view(user['Extend Sales Region'])
        sleep(1.5)
        self.is_click(user['Extend Sales Region'])
        self.input_text(user['Extend Sales Region'], txt=content)
        sleep(2)
        self.is_click(user['Extend Sales Region Value'])

    def click_extend_shop_grade(self):
        """扩展门店等级属性"""
        self.is_click(user['Extend Shop Grade'])
        sleep(1)
        self.is_click(user['Extend Shop Grade Value'], "A 10-20 ")

    def click_extend_shop_type(self):
        """扩展门店类型属性"""
        self.is_click(user['Extend Shop Type'])
        sleep(1)
        self.is_click(user['Extend Shop Type Value'], "CHIN")

    def click_extend_image_type(self):
        """扩展门店形象属性"""
        self.is_click(user['Extend Image Type'])
        sleep(1)
        self.is_click_dcr(user['Extend Zone Shop Value'], "Zone Shop")

    def extend_retail_customer(self, content):
        """扩展零售商客户属性"""
        self.scroll_into_view(user['扩展品牌输入零售商'])
        self.is_click(user['扩展品牌输入零售商'])
        self.input_text(user['扩展品牌输入零售商'], txt=content)
        sleep(3)
        self.is_click_dcr(user['扩展品牌选中零售商'])

    def extend_commercial_area(self):
        """扩展商业区域属性"""
        self.is_click(user['Extend Commercial Area'])
        sleep(1)
        self.is_click_dcr(user['Extend Commercial Value'], "KA")


if __name__ == '__main__':
    pass