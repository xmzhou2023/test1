from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserAuthorizationPage(Base):
    """ 根据代理用户筛选用户关联的数据 """

    @allure.step("进入用户授权页面，根据User 筛选品牌、客户等数据")
    def input_dealer_user_query(self, content):
        self.presence_sleep_dcr(user['Input User'])
        self.is_click_dcr(user['Input User'])
        self.input_text_dcr(user['Input User'], txt=content)
        sleep(3)
        self.presence_sleep_dcr(user['Click Dealer User Value'], content)
        self.is_click(user['Click Dealer User Value'], content)

    @allure.step("根据传音用户筛选用户关联的数据")
    def input_trans_user_query(self, content):
        """进入用户授权页面，根据User 筛选品牌、客户等数据"""
        self.is_click_dcr(user['Input User'])
        self.input_text_dcr(user['Input User'], txt=content)
        sleep(3.5)
        self.presence_sleep_dcr(user['Click Trans User Value'], content)
        self.is_click(user['Click Trans User Value'], content)

    @allure.step("点击user对应的Search按钮")
    def click_search(self):
        self.is_click_dcr(user['User Search'])
        sleep(2.5)


    """删除与添加品牌定位方法"""
    @allure.step("获取列表Infinix品牌文本")
    def get_list_infinix_text(self):
        self.presence_sleep_dcr(user['获取列表Infinix文本'])
        infinix = self.element_text(user['获取列表Infinix文本'])
        return infinix

    @allure.step("点击Cancel Association 删除品牌按钮")
    def click_cancel_association(self):
        self.is_click(user['infinix Cancel Association'])
        sleep(1.5)

    @allure.step("点击Delete 确认删除品牌按钮")
    def click_delete_brand(self):
        self.is_click(user['确认删除品牌按钮'])


    @allure.step("获取删除品牌成功 Successfully提示语")
    def get_delete_brand_success(self):
        success = self.element_text(user['获取删除品牌成功提示'])
        return success

    @allure.step("点击Add Association添加品牌按钮")
    def click_add_brand(self):
        self.is_click_dcr(user['Add Association Brand'])
        sleep(2)

    @allure.step("Add Association页面，获取infinix品牌文本")
    def get_add_infinix_text(self):
        self.presence_sleep_dcr(user['获取添加页面Infinix文本'])
        add_infinix = self.element_text(user['获取添加页面Infinix文本'])
        return add_infinix

    @allure.step("点击添加 infinix 品牌前面的复选框")
    def click_add_brand_checkbox(self):
        self.is_click(user['点击添加品牌的复选框'])

    @allure.step("点击Save 保存品牌按钮")
    def click_save_brand(self):
        self.is_click(user['保存品牌'])

    @allure.step("获取添加品牌成功 Successfully 提示语")
    def get_add_brand_success(self):
        success = self.element_text(user['获取添加品牌成功提示'])
        return success


    """添加客户Customer定位方法"""
    @allure.step("点击Customer页签")
    def click_customer_tab(self):
        self.is_click_dcr(user['切换客户页签'])
        sleep(2)

    @allure.step("在客户页签，点击Add Association按钮")
    def click_add_customer(self):
        self.is_click(user['Add Association Customer'])
        sleep(2)

    @allure.step("添加客户页面，输入Customer ID筛选需要添加的客户")
    def click_input_customer(self, content):
        self.presence_sleep_dcr(user['Add Click Input Query Cust'])
        self.is_click(user['Add Click Input Query Cust'])
        self.input_text_dcr(user['Add Input Query Cust'], txt=content)
        self.presence_sleep_dcr(user['Add Input Query Cust Value'])
        self.is_click(user['Add Input Query Cust Value'])

    @allure.step("在添加客户页面，点击Search按钮")
    def click_add_customer_search(self):
        self.is_click(user['Add Customer Search'])
        sleep(2)

    @allure.step("在添加客户页面，获取Customer ID文本")
    def get_customer_id_text(self):
        self.presence_sleep_dcr(user['Add 获取CustomerID文本'], 'CN20009')
        get_customer = self.element_text(user['Add 获取CustomerID文本'], 'CN20009')
        return get_customer

    @allure.step("添加客户页面，勾选第一个客户的复选框，进行添加客户操作")
    def click_add_customer_checkbox(self):
        self.is_click(user['添加客户勾选复选框'])

    @allure.step("添加客户页面，点击Authorized Selected授权选中按钮")
    def click_cust_authoriz_select(self):
        self.is_click(user['Add Cust Authorized Selected'])
        sleep(0.5)

    @allure.step("在添加客户页面，获取添加客户成功提示语")
    def get_add_cust_success_text(self):
        get_success = self.element_text(user['获取添加客户成功提示'])
        return get_success

    #删除客户Customer定位方法
    @allure.step("在客户页签，输入Customer ID进行筛选需要删除的客户")
    def input_list_customer(self, content):
        self.presence_sleep_dcr(user['客户列表点击客户输入框'])
        self.is_click_dcr(user['客户列表点击客户输入框'])
        self.input_text_dcr(user['客户列表输入客户'], txt=content)
        sleep(2.5)
        self.presence_sleep_dcr(user['客户列表选中输入的客户'], content)
        self.is_click(user['客户列表选中输入的客户'], content)

    @allure.step("在客户页签，点击Search按钮")
    def click_customer_search(self):
        self.is_click(user['Customer list Search'])
        sleep(2)

    @allure.step("在客户页签，获取客户列表的Customer ID")
    def get_list_customer_id(self):
        self.presence_sleep_dcr(user['获取客户列表CustomerID'], 'CN20009')
        get_list_cust = self.element_text(user['获取客户列表CustomerID'], 'CN20009')
        return get_list_cust

    @allure.step("在客户页签，筛选Customer ID后，点击勾选客户的复选框")
    def click_list_cust_checkbox(self):
        self.is_click(user['客户列表勾选客户复选框'])

    @allure.step("在客户页签，筛选Customer ID后，点击More Option按钮")
    def click_cust_more_option(self):
        self.is_click(user['Customer More Option'])
        sleep(2)

    @allure.step("在客户页签，点击Batch Cancel Association按钮")
    def click_cust_cancel_association(self):
        self.is_click(user['Cust Batch Cancel Association'])
        sleep(1)

    @allure.step("在客户页签，点击delete确认删除按钮")
    def click_cust_delete(self):
        self.is_click(user['Customer Delete'])

    @allure.step("在客户页签，获取客户列表 删除客户成功提示语")
    def get_cust_delete_success(self):
        get_dele_success = self.element_text(user['获取删除客户成功提示'])
        return get_dele_success
        sleep(1)

    @allure.step("在客户页签，获取客户列表 删除成功后，No Data文本")
    def get_cust_dele_no_data(self):
        get_dele_nodata = self.element_text(user['获取客户无数据文本'])
        return get_dele_nodata

    @allure.step("点击品牌页签")
    def click_brand_tab(self):
        self.is_click(user['点击品牌页签'])
        sleep(1)


    """删除仓库Warehouse定位方法"""

    @allure.step("在仓库页签，点击Warehouse 切换仓库页签")
    def click_warehouse_tab(self):
        self.is_click_dcr(user['切换仓库页签'])
        sleep(2)

    @allure.step("在仓库页签，输入Warehouse ID进行筛选需要删除的仓库")
    def input_list_query_ware(self, content):
        self.presence_sleep_dcr(user['仓库列表点击仓库输入框'])
        self.is_click(user['仓库列表点击仓库输入框'])
        self.input_text_dcr(user['仓库列表点击仓库输入框'], txt=content)
        sleep(2)
        self.is_click_dcr(user['仓库列表选中输入的仓库'], 'WNG2061304 NG2061303')

    @allure.step("在仓库页签，点击Search 查询按钮")
    def click_warehouse_list_search(self):
        self.is_click(user['Warehouse list Search'])
        sleep(4)

    @allure.step("在仓库页签，筛选Warehouse ID后，获取筛选到的Warehouse ID文本")
    def get_list_warehouseID_text(self):
        get_list_ware = self.element_text(user['list 获取Warehouse文本'], 'WNG2061304')
        return get_list_ware

    @allure.step("在仓库页签，筛选Warehouse ID后，点击勾选仓库ID对应的复选框")
    def click_list_ware_checkbox(self):
        self.is_click(user['仓库列表勾选仓库复选框'])

    @allure.step("在仓库页签，筛选Warehouse ID后，点击More Option按钮")
    def click_ware_more_option(self):
        self.is_click(user['Warehouse More Option'])
        sleep(1)

    @allure.step("在仓库页签，点击Batch Cancel Association 按钮")
    def click_ware_cancel_association(self):
        self.presence_sleep_dcr(user['Ware Batch Cancel Association'])
        self.is_click(user['Ware Batch Cancel Association'])
        sleep(1)

    @allure.step("在仓库页签，点击delete确认删除仓库按钮")
    def click_ware_delete(self):
        self.is_click(user['Warehouse Delete'])

    @allure.step("在仓库页签，获取仓库列表 删除仓库成功提示语")
    def get_ware_delete_success(self):
        ware_del_success = self.element_text(user['获取成功提示语'])
        return ware_del_success
        sleep(1)

    @allure.step("在仓库页签，获取删除仓库成功后的 No Data文本")
    def get_ware_dele_no_data(self):
        self.presence_sleep_dcr(user['获取仓库无数据文本'])
        get_ware_nodata = self.element_text(user['获取仓库无数据文本'])
        return get_ware_nodata


    """添加仓库Warehouse定位方法"""
    @allure.step("在仓库页签，点击Add Association 添加仓库按钮")
    def click_add_association_ware(self):
        self.is_click_dcr(user['Add Association Warehouse'])
        sleep(2)

    @allure.step("在新增仓库页面，Warehouse输入框输入需要筛选的仓库")
    def input_add_query_ware(self, content):
        self.presence_sleep_dcr(user['Add Click Input Query Ware'])
        self.is_click(user['Add Click Input Query Ware'])
        self.input_text(user['Add Click Input Query Ware'], txt=content)
        sleep(3)
        self.is_click_dcr(user['Add Input Query Ware Value'], 'WNG2061304 NG2061303')

    @allure.step("新增仓库页面，点击仓库Search按钮")
    def click_add_ware_search(self):
        self.is_click(user['Add Warehouse Search'])
        sleep(2.5)

    @allure.step("新增仓库页面，获取warehouseID文本")
    def get_add_warehouseid_text(self):
        self.presence_sleep_dcr(user['Add 获取WarehouseID文本'], 'WNG2061304')
        get_add_ware = self.element_text(user['Add 获取WarehouseID文本'], 'WNG2061304')
        return get_add_ware

    @allure.step("新增仓库页面，点击添加需要添加仓库的 复选框")
    def click_add_ware_checkbox(self):
        self.is_click(user['添加仓库勾选复选框'])

    @allure.step("新增仓库页面，点击Save保存按钮")
    def click_add_ware_save(self):
        self.is_click_dcr(user['Add Warehouse Save'])

    @allure.step("新增仓库页面，点击Save后，获取新增仓库成功Successfully文本")
    def get_add_ware_success(self):
        add_ware_success = self.element_text(user['获取成功提示语'])
        return add_ware_success
        sleep(2)


    """删除门店Shop 定位方法"""
    @allure.step("在门店页签，点击Shop 切换门店页签")
    def click_shop_tab(self):
        self.presence_sleep_dcr(user['切换门店页签'])
        self.is_click_dcr(user['切换门店页签'])
        sleep(2)

    @allure.step("在门店页签，输入Shop ID进行筛选需要删除的门店")
    def input_list_query_shop(self, context):
        self.is_click_dcr(user['门店列表点击门店输入框'])
        self.input_text_dcr(user['门店列表点击门店输入框'], txt=context)
        sleep(3.7)
        self.presence_sleep_dcr(user['门店列表选中输入的门店'], context)
        self.is_click(user['门店列表选中输入的门店'], context)

    @allure.step("在门店页签，点击Search 查询按钮")
    def click_shop_list_search(self):
        self.is_click(user['Shop list Search'])
        sleep(2.5)

    @allure.step("在门店页签，筛选Shop ID后，获取筛选到的Shop ID文本")
    def get_list_shop_text(self, shop):
        self.presence_sleep_dcr(user['list 获取ShopID文本'], shop)
        get_list_shopid = self.element_text(user['list 获取ShopID文本'], shop)
        return get_list_shopid

    @allure.step("在门店页签，筛选Shop ID后，点击勾选Shop ID对应的复选框")
    def click_list_shop_checkbox(self):
        self.is_click(user['门店列表勾选门店复选框'])

    @allure.step("在门店页签，筛选Shop ID后，点击More Option按钮")
    def click_shop_more_option(self):
        self.is_click(user['Shop More Option'])
        sleep(2)

    @allure.step("在门店页签，点击 Batch Cancel Association取消关联按钮")
    def click_shop_cancel_association(self):
        self.presence_sleep_dcr(user['Shop Batch Cancel Association'])
        self.is_click(user['Shop Batch Cancel Association'])
        sleep(2)

    @allure.step("在门店页签，点击确认删除Delete按钮")
    def click_shop_delete(self):
        self.is_click(user['Shop Delete'])

    @allure.step("在门店页签，获取仓库列表 删除仓库成功提示语")
    def get_shop_delete_success(self):
        shop_del_success = self.element_text(user['获取成功提示语'])
        return shop_del_success
        sleep(1)

    @allure.step("在门店页签，获取删除仓库成功后的 No Data文本")
    def get_shop_delete_no_data(self):
        self.presence_sleep_dcr(user['获取门店无数据文本'])
        get_shop_nodata = self.element_text(user['获取门店无数据文本'])
        return get_shop_nodata


    """新增门店Shop定位方法"""
    @allure.step("点击新增门店按钮 Add Association Shop")
    def click_add_association_shop(self):
        self.is_click_dcr(user['Add Association Shop'])
        sleep(2)

    @allure.step("在新增门店页面，Shop输入框输入需要筛选的门店")
    def input_add_query_shop(self, content):
        self.presence_sleep_dcr(user['Add Click Input Query Shop'])
        self.is_click(user['Add Click Input Query Shop'])
        self.input_text(user['Add Input Query Shop'], txt=content)
        sleep(3)
        self.is_click_dcr(user['Add Input Query Shop Value'], content)

    @allure.step("新增门店页面，点击门店Search按钮")
    def click_add_shop_search(self):
        self.is_click(user['Add Shop Search'])
        sleep(3)

    @allure.step("新增门店页面，获取Shop ID文本")
    def get_add_shop_id_text(self, shop):
        self.presence_sleep_dcr(user['add获取ShopID文本'], shop)
        get_add_shop_id = self.element_text(user['add获取ShopID文本'], shop)
        return get_add_shop_id

    @allure.step("在门店页签，筛选Shop ID后，点击勾选Shop ID对应的复选框")
    def click_add_shop_checkbox(self):
        self.is_click(user['添加门店勾选复选框'])
        sleep(0.5)

    @allure.step("新增门店页面，点击Authorized Selected 选中授权按钮")
    def click_add_shop_author_select(self):
        self.is_click(user['Add Shop Authorized Selected'])

    @allure.step("新增门店页面，获取新增门店成功提示语")
    def get_shop_add_success(self):
        shop_add_success = self.element_text(user['获取成功提示语'])
        return shop_add_success
        sleep(1)

    @allure.step("门店页签，获取门店列表 Shop ID文本")
    def get_list_shop_id_text(self, shop):
        self.presence_sleep_dcr(user['门店列表获取ShopID文本'], shop)
        get_list_shop = self.element_text(user['门店列表获取ShopID文本'], shop)
        return get_list_shop


    """ 添加销售区域Sales Region定位方法"""
    @allure.step("在销售页签，点击Sales Region 切换销售区域页签")
    def click_sales_region_tab(self):
        self.presence_sleep_dcr(user['切换销售区域页签'])
        self.is_click_dcr(user['切换销售区域页签'])
        sleep(2)

    @allure.step("在销售页签，勾选East Africa I 销售区域复选框")
    def click_east_africa_checkbox(self):
        self.presence_sleep_dcr(user['Select East AfricaI Checkbox'])
        self.is_click(user['Select East AfricaI Checkbox'])

    @allure.step("在销售页签，勾选User 复选框")
    def get_sale_checkbox_status(self):
        sale_checkbox_status = self.select_state(user['Select East AfricaI Checkbox'])
        return sale_checkbox_status

    @allure.step("在销售页签，勾选User 复选框")
    def click_score_user_checkbox(self):
        self.is_click(user['Select Scope user Checkbox'])

    @allure.step("在销售页签，点击Save按钮，保存销售区域")
    def click_save_sales_region(self):
        self.is_click_dcr(user['Sales Region Save'])

    @allure.step("在销售页签，未勾选销售范围时，点击Save按钮，提示：请先勾选销售范围")
    def get_not_auto_score_text(self):
        get_not_score_text = self.element_text(user['获取未授权范围提示语'])
        return get_not_score_text

    @allure.step("在销售页签，点击Save成功后，获取销售区域成功提示语")
    def get_sale_region_success(self):
        get_sale_sucess = self.element_text(user['获取销售区域成功提示'])
        return get_sale_sucess
        sleep(1.5)

    @allure.step("关闭用户授权菜单")
    def click_close_user_authorization(self):
        self.is_click(user['关闭用户授权菜单'])
        sleep(2)


if __name__ == '__main__':
    pass