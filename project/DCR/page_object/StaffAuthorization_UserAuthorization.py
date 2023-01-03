from libs.common.read_element import Element
from libs.config.conf import BASE_DIR
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
        self.is_click_dcr(user['infinix Cancel Association'])
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
        sleep(2)
        self.is_click_dcr(user['Add Input Query Cust Value'], content)

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
    def get_list_customer_id(self, context):
        self.presence_sleep_dcr(user['获取客户列表CustomerID'], context)
        get_list_cust = self.element_text(user['获取客户列表CustomerID'], context)
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
        #sleep(2)

    @allure.step("点击标签页")
    def click_tab(self, select):
        self.is_click(user['tab标签'], select)
        logging.info(f'点击标签页： {select}')

    @allure.step("输入查询条件")
    def input_search(self, header, content):
        click_list = ['Customer Type']
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if header == 'User ID':
            self.is_click_tbm(user['输入框'], header)
            self.input_text(user['输入框3'], content, header)
        elif header == 'User Name':
            self.is_click_tbm(user['输入框'], header)
            self.input_text(user['输入框2'], content, header)
            self.is_click_tbm(user['输入结果模糊选择'], content)
        elif header in click_list:
            self.is_click(user['输入框'], header)
            self.is_click(user['点击选择'], content)
        else:
            logging.error('请输入正确的查询条件')
            raise ValueError('请输入正确的查询条件')

    @allure.step("点击功能按钮")
    def click_function_button(self, function):
        """
        @function： 需要点击的功能按钮，具体如下：
        Add Association, Import, Export Filtered, More Option,
        Batch Cancel Association, Empty All Association
        """
        MoreOptionList = ['Batch Cancel Association', 'Empty All Association']
        if function in MoreOptionList:
            self.is_click(user['功能按钮'], 'More Option')
            self.is_click(user['功能按钮2'], function)
        else:
            self.is_click(user['功能按钮'], function)
            # if function == 'Import':
                # self.click_upload()
        logging.info(f'点击功能按钮： {function}')

    @allure.step("输入查询条件")
    def input_AddAssociation_search(self, header, content):
        logging.info(f'AddAssociation弹框输入查询条件： {header} ，内容： {content}')
        select_list = ['Customer', 'Shop']
        click_list = ['Customer Type']
        title = self.element_text(user['AddAssociationTitle'])
        if 'Customer' in title or 'Shop' in title:
            if header in select_list:
                self.is_click(user['AddAssociation输入框'], header)
                self.input_text(user['AddAssociation输入框2'], content, header)
                self.is_click(user['输入选择'], content)
            elif header in click_list:
                self.is_click(user['AddAssociation输入框'], header)
                self.is_click(user['点击选择'], content)
        elif 'Warehouse' in title:
            if header in select_list:
                self.is_click(user['AddAssociation输入框'], header)
                self.input_text(user['AddAssociation输入框'], content, header)
                self.is_click(user['输入选择'], content)
            elif header in click_list:
                self.is_click(user['AddAssociation输入框'], header)
                self.is_click(user['点击选择'], content)
        else:
            logging.error('请输入正确的查询条件')
            raise ValueError('请输入正确的查询条件')

    @allure.step("AddAssociation弹框点击搜索")
    def click_AddAssociation_search(self):
        self.is_click(user['AddAssociationSearch'])
        logging.info('AddAssociation弹框 点击搜索')

    @allure.step("点击指定复选框")
    def click_CheckBox(self, Cid):
        self.is_click(user['指定复选框'], Cid)
        logging.info(f'点击 {Cid} 复选框')

    @allure.step("点击指定复选框")
    def click_Authorized_All_Filtered_Records(self):
        self.is_click(user['AuthorizedAllFilteredRecords'])

    @allure.step("AddAssociation弹框点击保存")
    def click_Authorized_Selected(self):
        title = self.element_text(user['AddAssociationTitle'])
        if 'Customer' in title or 'Shop' in title:
            self.is_click(user['AuthorizedSelected'])
        elif 'Warehouse' in title:
            self.is_click(user['Save'])
        else:
            logging.error('无对应保存按钮')
            raise ValueError('无对应保存按钮')
        logging.info('AddAssociation弹框 点击保存')

    @allure.step("断言：用户授权页面查询结果")
    def assert_Query_containsresult(self, header, content):
        """
        :param header: 需要获取的指定字段
        :param content: 需要断言的值
        :param num: 包含的数量
        """
        logging.info('开始断言：用户授权页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['menu表格字段'], user['表格内容'], header, content, sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("点击确定删除按钮")
    def click_Delete(self):
        self.is_click(user['确定删除'])
        logging.info('点击确定删除按钮')

    @allure.step("断言：用户授权页面存在NoData")
    def assert_NoData(self):
        logging.info('开始断言：用户授权页面存在NoData')
        DomAssert(self.driver).assert_control(user['NoData'])

    @allure.step("前置：移除所有授权")
    def reset_Association(self):
        logging.info('开始：移除所有授权')
        self.click_function_button('Empty All Association')
        self.click_Delete()
        DomAssert(self.driver).assert_att('Successfully')
        self.assert_NoData()

    @allure.step("组合方法：添加授权")
    def Association_Method(self, Cid, header='Customer'):
        """
        添加授权
        :param Cid: 默认输入客户id，如需要其他筛选方式输入对应数据即可
        :param header: 默认Customer，其他筛选方式：Customer Type，Country/City，Warehouse
        """
        logging.info('开始使用组合方法：添加授权')
        self.click_function_button('Add Association')
        self.input_AddAssociation_search(header, Cid)
        self.click_AddAssociation_search()
        self.click_CheckBox(Cid)
        self.click_Authorized_Selected()
        DomAssert(self.driver).assert_att('Successfully')

    @allure.step("查找菜单")
    def click_menu(self, *content):
        self.is_click_tbm(user['菜单栏'])
        self.refresh()
        for i in range(len(content)):
            self.is_click_tbm(user['菜单'], content[i])
            logging.info('点击菜单：{}'.format(content[i]))
        self.refresh()
        self.element_exist(user['Loading'])

    @allure.step("点击Upload按钮")
    def click_upload(self):
        self.is_click(user['Upload'])
        logging.info('点击upload按钮')
        # k = PyKeyboard()
        # k.tap_key(k.escape_key)

    @allure.step("导入门店")
    def import_file(self, name):
        file_path = os.path.join(BASE_DIR, 'project', 'DCR', 'data', name)
        logging.info("文件地址：{}".format(file_path))
        self.upload_file(user['导入'], file_path)
        self.assert_import_success()

    @allure.step("点击Save按钮")
    def click_save(self):
        self.is_click(user['ImportSave'])
        logging.info('点击Save按钮')

    @allure.step("点击Confirm按钮")
    def click_confirm(self):
        self.is_click(user['Confirm'])
        logging.info('点击Confirm按钮')
        sleep(2)
        self.refresh()

    @allure.step("断言：导入成功状态")
    def assert_import_success(self):
        DomAssert(self.driver).assert_control(user['导入成功状态'])

    @allure.step("获得Record指定内容")
    def get_Record_info(self, menu, name, header):
        """
        :param menu: 菜单名
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        """
        for i in range(20):
            ac_menu = self.element_text(user['当前菜单'])
            if ac_menu != menu:
                self.click_menu('Basic Data Management', menu)
            column = self.get_table_info(user['表格字段'], header, h_element=user['表头文本'])
            content = self.element_text(user['表格指定列内容'], name, column)
            logging.info(f'获得 {menu} 页面 {name} 文件 {header} 字段内容 {content}')
            return content

    @allure.step("断言：导入导出Record结果")
    def assert_Record_result(self, menu, name, header, result=None):
        """
        :param menu: 菜单
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        :param result: 需要断言的值 比如状态，数量，时间
        """
        ac_result = self.get_Record_info(menu, name, header)
        if header == 'File Size':
            ValueAssert.value_assert_IsNot(ac_result, '0B')
        else:
            ValueAssert.value_assert_In(result, ac_result)




if __name__ == '__main__':
    pass