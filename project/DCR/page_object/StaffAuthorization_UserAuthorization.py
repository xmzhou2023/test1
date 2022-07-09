from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserAuthorizationPage(Base):
    """ User Authorization 菜单定位元素类"""
    """ 根据代理用户筛选用户关联的数据 """
    def input_dealer_user_query(self, content):
        """进入用户授权页面，根据User 筛选品牌、客户等数据"""
        self.is_click_dcr(user['Input User'])
        self.input_text_dcr(user['Input User'], txt=content)
        sleep(3)
        self.is_click(user['Click Dealer User Value'])

    """ 根据传音用户筛选用户关联的数据 """
    def input_trans_user_query(self, content):
        """进入用户授权页面，根据User 筛选品牌、客户等数据"""
        self.is_click_dcr(user['Input User'])
        self.input_text_dcr(user['Input User'], txt=content)
        sleep(3)
        self.is_click(user['Click Trans User Value'])

    def click_search(self):
        """ 点击user对应的Search按钮 """
        self.is_click_dcr(user['User Search'])
        sleep(2)

    """删除与添加品牌定位方法"""
    def get_list_infinix_text(self):
        """ 获取列表Infinix品牌文本 """
        infinix = self.element_text(user['获取列表Infinix文本'])
        return infinix

    def click_cancel_association(self):
        """点击Cancel Association 删除品牌按钮 """
        self.is_click(user['infinix Cancel Association'])
        sleep(1)

    def click_delete_brand(self):
        """点击Delete 确认删除品牌按钮 """
        self.is_click(user['确认删除品牌按钮'])
        sleep(0.5)

    def get_delete_brand_success(self):
        """获取删除品牌成功 Successfully 提示语"""
        success = self.element_text(user['获取删除品牌成功提示'])
        return success

    def click_add_brand(self):
        """点击Add Association添加品牌按钮"""
        self.is_click_dcr(user['Add Association Brand'])
        sleep(2)

    def get_add_infinix_text(self):
        """Add Association页面，获取infinix品牌文本 """
        add_infinix = self.element_text(user['获取添加页面Infinix文本'])
        return add_infinix

    def click_add_brand_checkbox(self):
        """点击添加 infinix 品牌前面的复选框"""
        self.is_click(user['点击添加品牌的复选框'])

    def click_save_brand(self):
        """点击Save 保存品牌按钮"""
        self.is_click(user['保存品牌'])

    def get_add_brand_success(self):
        """ 获取添加品牌成功 Successfully 提示语"""
        success = self.element_text(user['获取添加品牌成功提示'])
        return success


    """添加客户Customer定位方法"""
    def click_customer_tab(self):
        """ 点击Customer页签 """
        self.is_click_dcr(user['切换客户页签'])
        sleep(3)

    def click_add_customer(self):
        """ 在客户页签，点击Add Association按钮 """
        self.is_click(user['Add Association Customer'])
        sleep(2)

    def click_input_customer(self, content):
        """ 添加客户页面，输入Customer ID筛选需要添加的客户 """
        self.is_click(user['Add Click Input Query Cust'])
        self.input_text_dcr(user['Add Input Query Cust'], txt=content)
        EC.visibility_of_element_located((By.XPATH, "//*[@id='userAuthCustomer']/div[3]/div/div[2]/form/div/div/div/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/ul/li/span"))
        self.is_click(user['Add Input Query Cust Value'])


    def click_add_customer_search(self):
        """ 在添加客户页面，点击Search按钮 """
        self.is_click(user['Add Customer Search'])
        sleep(4)

    def get_customer_id_text(self):
        """ 在添加客户页面，获取Customer ID文本 """
        get_customer = self.element_text(user['Add 获取CustomerID文本'])
        return get_customer

    def click_add_customer_checkbox(self):
        """ 添加客户页面，勾选第一个客户的复选框，进行添加客户操作 """
        self.is_click(user['添加客户勾选复选框'])

    def click_cust_authoriz_select(self):
        """ 添加客户页面，点击Authorized Selected授权选中按钮 """
        self.is_click(user['Add Cust Authorized Selected'])
        sleep(0.5)

    def get_add_cust_success_text(self):
        """ 在添加客户页面，获取添加客户成功提示语 """
        get_success = self.element_text(user['获取添加客户成功提示'])
        return get_success

    #删除客户Customer定位方法
    def input_list_customer(self, content):
        """ 在客户页签，输入Customer ID进行筛选需要删除的客户 """
        self.is_click_dcr(user['客户列表点击客户输入框'])
        self.input_text_dcr(user['客户列表输入客户'], txt=content)
        sleep(2)
        self.is_click(user['客户列表选中输入的客户'])

    def click_customer_search(self):
        """ 在客户页签，点击Search按钮 """
        self.is_click(user['Customer list Search'])
        sleep(4)

    def get_list_customer_id(self):
        """ 在客户页签，获取客户列表的Customer ID """
        get_list_cust = self.element_text(user['获取客户列表CustomerID'])
        return get_list_cust

    def click_list_cust_checkbox(self):
        """ 在客户页签，筛选Customer ID后，点击勾选客户的复选框 """
        self.is_click(user['客户列表勾选客户复选框'])

    def click_cust_more_option(self):
        """ 在客户页签，筛选Customer ID后，点击More Option按钮 """
        self.is_click(user['Customer More Option'])
        sleep(2)

    def click_cust_cancel_association(self):
        """ 在客户页签，点击Batch Cancel Association按钮 """
        self.is_click(user['Cust Batch Cancel Association'])
        sleep(1)

    def click_cust_delete(self):
        """ 在客户页签，点击delete确认删除按钮 """
        self.is_click(user['Customer Delete'])

    def get_cust_delete_success(self):
        """ 在客户页签，获取客户列表 删除客户成功提示语 """
        get_dele_success = self.element_text(user['获取删除客户成功提示'])
        return get_dele_success
        sleep(1)

    def get_cust_dele_no_data(self):
        """ 在客户页签，获取客户列表 删除成功后，No Data文本 """
        get_dele_nodata = self.element_text(user['获取客户无数据文本'])
        return get_dele_nodata

    def click_brand_tab(self):
        self.is_click(user['点击品牌页签'])
        sleep(1)


    """删除仓库Warehouse定位方法"""
    def click_warehouse_tab(self):
        """ 在仓库页签，点击Warehouse 切换仓库页签 """
        self.is_click_dcr(user['切换仓库页签'])
        sleep(3)

    def input_list_query_ware(self, content):
        """ 在仓库页签，输入Warehouse ID进行筛选需要删除的仓库 """
        self.is_click(user['仓库列表点击仓库输入框'])
        self.input_text_dcr(user['仓库列表点击仓库输入框'], txt=content)
        sleep(2)
        self.is_click(user['仓库列表选中输入的仓库'])

    def click_warehouse_list_search(self):
        """ 在仓库页签，点击Search 查询按钮 """
        self.is_click(user['Warehouse list Search'])
        sleep(4)

    def get_list_warehouseID_text(self):
        """ 在仓库页签，筛选Warehouse ID后，获取筛选到的Warehouse ID文本 """
        get_list_ware = self.element_text(user['list 获取Warehouse文本'])
        return get_list_ware

    def click_list_ware_checkbox(self):
        """ 在仓库页签，筛选Warehouse ID后，点击勾选仓库ID对应的复选框 """
        self.is_click(user['仓库列表勾选仓库复选框'])

    def click_ware_more_option(self):
        """ 在仓库页签，筛选Warehouse ID后，点击More Option按钮 """
        self.is_click(user['Warehouse More Option'])
        sleep(1)

    def click_ware_cancel_association(self):
        """ 在仓库页签，点击Batch Cancel Association 按钮 """
        self.is_click(user['Ware Batch Cancel Association'])
        sleep(1)

    def click_ware_delete(self):
        """ 在仓库页签，点击delete确认删除仓库按钮 """
        self.is_click(user['Warehouse Delete'])

    def get_ware_delete_success(self):
        """ 在仓库页签，获取仓库列表 删除仓库成功提示语 """
        ware_del_success = self.element_text(user['获取成功提示语'])
        return ware_del_success
        sleep(1)

    def get_ware_dele_no_data(self):
        """ 在仓库页签，获取删除仓库成功后的 No Data文本 """
        get_ware_nodata = self.element_text(user['获取仓库无数据文本'])
        return get_ware_nodata


    """添加仓库Warehouse定位方法"""
    def click_add_association_ware(self):
        """ 在仓库页签，点击Add Association 添加仓库按钮 """
        self.is_click_dcr(user['Add Association Warehouse'])
        sleep(3)

    def input_add_query_ware(self, content):
        """ 在新增仓库页面，Warehouse输入框输入需要筛选的仓库 """
        self.is_click(user['Add Click Input Query Ware'])
        self.input_text(user['Add Click Input Query Ware'], txt=content)
        sleep(3)
        self.is_click_dcr(user['Add Input Query Ware Value'])

    def click_add_ware_search(self):
        """ 新增仓库页面，点击仓库Search按钮 """
        self.is_click(user['Add Warehouse Search'])
        sleep(4)

    def get_add_warehouseid_text(self):
        """ 新增仓库页面，获取warehouseID文本 """
        get_add_ware = self.element_text(user['Add 获取WarehouseID文本'])
        return get_add_ware

    def click_add_ware_checkbox(self):
        """ 新增仓库页面，点击添加需要添加仓库的 复选框 """
        self.is_click(user['添加仓库勾选复选框'])

    def click_add_ware_save(self):
        """ 新增仓库页面，点击Save保存按钮 """
        self.is_click_dcr(user['Add Warehouse Save'])

    def get_add_ware_success(self):
        """ 新增仓库页面，点击Save后，获取新增仓库成功Successfully文本 """
        add_ware_success = self.element_text(user['获取成功提示语'])
        return add_ware_success
        sleep(2)


    """删除门店Shop 定位方法"""
    def click_shop_tab(self):
        """ 在门店页签，点击Shop 切换门店页签 """
        self.is_click_dcr(user['切换门店页签'])
        sleep(3)

    def input_list_query_shop(self, context):
        """ 在门店页签，输入Shop ID进行筛选需要删除的门店 """
        self.is_click(user['门店列表点击门店输入框'])
        self.input_text_dcr(user['门店列表点击门店输入框'], txt=context)
        sleep(2)
        self.is_click(user['门店列表选中输入的门店'])

    def click_shop_list_search(self):
        """ 在门店页签，点击Search 查询按钮 """
        self.is_click(user['Shop list Search'])
        sleep(2)

    def get_list_shop_text(self):
        """ 在门店页签，筛选Shop ID后，获取筛选到的Shop ID文本 """
        get_list_shopid = self.element_text(user['list 获取ShopID文本'])
        return get_list_shopid

    def click_list_shop_checkbox(self):
        """ 在门店页签，筛选Shop ID后，点击勾选Shop ID对应的复选框 """
        self.is_click(user['门店列表勾选门店复选框'])

    def click_shop_more_option(self):
        """ 在门店页签，筛选Shop ID后，点击More Option按钮 """
        self.is_click(user['Shop More Option'])
        sleep(1)

    def click_shop_cancel_association(self):
        """ 在门店页签，点击 Batch Cancel Association取消关联按钮 """
        self.is_click(user['Shop Batch Cancel Association'])
        sleep(1)

    def click_shop_delete(self):
        """ 在门店页签，点击确认删除Delete按钮 """
        self.is_click(user['Shop Delete'])

    def get_shop_delete_success(self):
        """ 在门店页签，获取仓库列表 删除仓库成功提示语 """
        shop_del_success = self.element_text(user['获取成功提示语'])
        return shop_del_success
        sleep(1)

    def get_shop_delete_no_data(self):
        """ 在门店页签，获取删除仓库成功后的 No Data文本 """
        get_shop_nodata = self.element_text(user['获取门店无数据文本'])
        return get_shop_nodata


    """新增门店Shop定位方法"""
    def click_add_association_shop(self):
        self.is_click_dcr(user['Add Association Shop'])
        sleep(2)

    def input_add_query_shop(self, content):
        """ 在新增门店页面，Shop输入框输入需要筛选的门店 """
        self.is_click(user['Add Click Input Query Shop'])
        self.input_text(user['Add Input Query Shop'], txt=content)
        sleep(3)
        self.is_click_dcr(user['Add Input Query Shop Value'])

    def click_add_shop_search(self):
        """ 新增门店页面，点击门店Search按钮 """
        self.is_click(user['Add Shop Search'])
        sleep(3)

    def get_add_shop_id_text(self):
        """ 新增门店页面，获取Shop ID文本 """
        get_add_shop_id = self.element_text(user['add 获取ShopID文本'])
        return get_add_shop_id

    def click_add_shop_checkbox(self):
        """ 在门店页签，筛选Shop ID后，点击勾选Shop ID对应的复选框 """
        self.is_click(user['添加门店勾选复选框'])

    def click_add_shop_author_select(self):
        """ 新增门店页面，点击Authorized Selected 选中授权按钮 """
        self.is_click(user['Add Shop Authorized Selected'])


    def get_shop_add_success(self):
        """ 新增门店页面，获取新增门店成功提示语 """
        shop_add_success = self.element_text(user['获取成功提示语'])
        return shop_add_success
        sleep(1)

    def get_list_shop_id_text(self):
        """ 门店页签，获取门店列表 Shop ID文本 """
        get_list_shop = self.element_text(user['门店列表获取ShopID文本'])
        return get_list_shop


    """ 添加销售区域Sales Region定位方法"""
    def click_sales_region_tab(self):
        """ 在销售页签，点击Sales Region 切换销售区域页签 """
        self.is_click_dcr(user['切换销售区域页签'])
        sleep(4)

    def click_east_africa_checkbox(self):
        """ 在销售页签，勾选East Africa I 销售区域复选框 """
        self.is_click(user['Select East AfricaI Checkbox'])

    def get_sale_checkbox_status(self):
        """ 在销售页签，勾选User 复选框 """
        sale_checkbox_status = self.select_state(user['Select East AfricaI Checkbox'])
        return sale_checkbox_status

    def click_score_user_checkbox(self):
        """ 在销售页签，勾选User 复选框 """
        self.is_click(user['Select Scope user Checkbox'])

    def click_save_sales_region(self):
        """ 在销售页签，点击Save按钮，保存销售区域 """
        self.is_click_dcr(user['Sales Region Save'])

    def get_not_auto_score_text(self):
        """ 在销售页签，未勾选销售范围时，点击Save按钮，提示：请先勾选销售范围 """
        get_not_score_text = self.element_text(user['获取未授权范围提示语'])
        return get_not_score_text

    def get_sale_region_success(self):
        """ 在销售页签，点击Save成功后，获取销售区域成功提示语 """
        get_sale_sucess = self.element_text(user['获取销售区域成功提示'])
        return get_sale_sucess
        sleep(1.5)



if __name__ == '__main__':
    pass