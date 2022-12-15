from libs.common.read_element import Element
import logging
from libs.common.connect_sql import *
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class SalesOrderPage(Base):
    """SalesOrderPage销售订单页面定位方法"""

    @allure.step("Sales Order页面，点击Add新增销售单按钮")
    def click_add_sales(self):
        self.is_click(user['Add'])
        sleep(1.5)

    @allure.step("Add新增销售单页面，输入Sales Buyer属性")
    def input_sales_buyer(self, content):
        self.presence_sleep_dcr(user['Buyer'])
        self.is_click(user['Buyer'])
        self.input_text(user['Buyer'], content)
        sleep(1)
        self.is_click(user['Buyer value'], content)

    @allure.step("新增销售单页面，输入Brand属性")
    def input_sales_brand(self, content):
        self.is_click(user['Sales Order Add Brand'])
        self.is_click_dcr(user['Sales Order Add Brand value'], content)

    @allure.step("新增销售单页面，输入product属性")
    def input_sales_product(self, content):
        self.is_click(user['Sales Order Add product'])
        self.input_text(user['Sales Order Add product'], content)
        sleep(2)
        self.is_click(user['Sales Order Add product value'], content)

    @allure.step("新增销售单页面，输入Quantity属性")
    def input_sales_quantity(self, content):
        self.is_click(user['Quantity'])
        self.input_text(user['Quantity'], content)

    @allure.step("新增销售单页面，点击Add Product添加多品牌按钮")
    def click_sales_order_add_product_button(self):
        self.is_click(user['Sales Order Add Product Button'])
        sleep(1)

    @allure.step("新增销售单页面，点击Add Product按钮后，选择第二个Brand值")
    def click_sales_order_add_brand2(self, itel):
        self.is_click(user['Sales Order Add Brand2'])
        self.is_click_dcr(user['Sales Order Add Brand value'], itel)

    @allure.step("新增销售单页面，点击Add Product按钮后，选择第二个Product值")
    def input_sales_order_add_product2(self, product):
        self.is_click(user['Sales Order Add product2'])
        self.input_text(user['Sales Order Add product2'], product)
        sleep(2)
        self.is_click(user['Sales Order Add product value'], product)

    @allure.step("新建销售单页面，点击提交按钮")
    def click_submit(self):
        """新建销售单页面，点击提交按钮"""
        self.is_click_dcr(user['Submit Sales'])
        sleep(1)

    @allure.step("新建销售单页面，点击提交后，然后点击确认OK按钮")
    def click_submit_OK(self):
        self.presence_sleep_dcr(user['保存成功确认OK'])
        self.is_click(user['保存成功确认OK'])
        sleep(3)

    @allure.step("销售单页面，按销售单ID条件筛选")
    def input_sales_order_ID(self, content):
        self.is_click(user['按销售单ID筛选'])
        self.input_text(user['按销售单ID筛选'], content)
        sleep(2)

    @allure.step("销售单页面，点击Search查询按钮")
    def click_search(self):
        self.is_click(user['Sales Order Search'])
        sleep(2.5)

    @allure.step("销售单页面，点击IMEI Detail打开详情页")
    def click_sales_order_imei_detail(self):
        self.is_click(user['Sales Order IMEI Detail'])
        sleep(1.5)

    @allure.step("销售单页面，点击关闭IMEI Detail详情页")
    def close_sales_order_imei_detail(self):
        self.is_click(user['Close Sales Order IMEI Detail'])

    @allure.step("销售单页面，打开IMEI Detail详情页，获取分页总条数")
    def get_sales_imei_detail_total(self):
        get_total = self.element_text(user['Get Sales IMEI Detail Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("销售单页面，获取销售单ID文本")
    def get_text_sales_id(self):
        self.presence_sleep_dcr(user['获取Sales Order ID文本'])
        sales_order_id = self.element_text(user['获取Sales Order ID文本'])
        return sales_order_id

    @allure.step("销售单页面，获取销售单状态文本")
    def get_sales_status_text(self):
        self.presence_sleep_dcr(user['获取列表Status文本'])
        status = self.element_text(user['获取列表Status文本'])
        return status


    """勾选新建的销售单，直接出库"""
    @allure.step("勾选新建的 第一条销售单ID")
    def click_checkbox_orderID(self):
        self.is_click_dcr(user['勾选第一条销售单ID'])

    @allure.step("点击Delivery button出库按钮")
    def click_Delivery_button(self):
        self.is_click(user['Delivery button'])
        sleep(2)

    @allure.step("新建出库单页面，输入Payment Mode支持方式属性")
    def input_Payment_Mode(self, content):
        self.presence_sleep_dcr(user['Payment Mode'])
        self.is_click(user['Payment Mode'])
        self.input_text(user['Payment Mode'], txt=content)
        self.presence_sleep_dcr(user['Payment Mode value'], content)
        self.is_click(user['Payment Mode value'], content)
        sleep(1)

    @allure.step("新建出库单页面，输入IMEI属性")
    def input_imei(self, content):
        self.is_click(user['Input IMEI'])
        self.input_text(user['Input IMEI'], content)
        sleep(1)

    @allure.step("新建出库单页面，点击check检查IMEI按钮")
    def click_check(self):
        self.is_click_dcr(user['Check'])
        sleep(2)

    @allure.step("Add新增出库单页面，点击check后，右侧Delivery Quan属性下显示出库数量")
    def get_delivery_quantity(self):
        get_deli_quantity = self.element_text(user['Get Delivery Quantity'])
        return get_deli_quantity

    @allure.step("Add新增出库单页面，点击check后，Order Detail列表Delivery Quan属性下显示出库数量")
    def get_order_detail_deli_quantity(self):
        get_order_deli_quantity = self.element_text(user['Get Order Detail Deli Quantity'])
        return get_order_deli_quantity

    @allure.step("Add新增出库单页面，点击check后，Scan Record扫码记录下侧显示Success")
    def get_Deli_Scan_Record_Success(self):
        self.presence_sleep_dcr(user['Get Delivery Scan Record Success'])
        scan_record_success = self.element_text(user['Get Delivery Scan Record Success'])
        return scan_record_success

    @allure.step("Add新增出库单页面，点击check后，Scan Record扫码记录下侧出现显示IMEI")
    def get_Deli_Scan_Record_IMEI(self, imei):
        self.presence_sleep_dcr(user['Get Delivery Scan Record IMEI'], imei)
        scan_record_imei = self.element_text(user['Get Delivery Scan Record IMEI'], imei)
        return scan_record_imei

    @allure.step("新建出库单页面，点击Submit Delivery提交出库单按钮")
    def click_submit_delivery(self):
        self.is_click_dcr(user['Submit Delivery'])
        sleep(0.6)


    @allure.step("查询数据库,最近新建的销售单ID")
    def query_sql_sales_order_id(self, warehouse, seller, buyer, status):
        sql1 = SQL('DCR', 'test')
        sql_val1 = f"select order_code from t_channel_sale_ticket where warehouse_id = '{warehouse}' and seller_id = '{seller}' and buyer_id = '{buyer}' and status = {status} order by created_time desc limit 1"
        result = sql1.query_db(sql_val1)
        sales_order = result[0].get("order_code")
        return sales_order

    @allure.step("查询数据库,最近新建的出库单ID，返回销售单ID与出库单id")
    def query_sql_delivery_order_id2(self, warehouse, seller, buyer, status):
        sql3 = SQL('DCR', 'test')
        var_sql3 = f"select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='{warehouse}' and seller_id='{seller}' and buyer_id='{buyer}' and status={status} order by created_time desc limit 1"
        result = sql3.query_db(var_sql3)
        sales_id = result[0].get("order_code")
        delivery_id = result[0].get("delivery_code")
        return sales_id, delivery_id

    @allure.step("查询数据库,最近新建的出库单ID，返回出库单id")
    def query_sql_delivery_order_id1(self, warehouse, seller, buyer, status):
        sql4 = SQL('DCR', 'test')
        var_sql4 = f"select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='{warehouse}' and seller_id='{seller}' and buyer_id='{buyer}' and status={status} order by created_time desc limit 1"
        result = sql4.query_db(var_sql4)
        delivery_code = result[0].get("delivery_code")
        return delivery_code



    #筛选IMEI Inventory Query页面，product对应的IMEI 元素定位
    @allure.step("IMEI Inventory Query页面，点击Unfold展开筛选按钮")
    def click_unfold(self):
        self.is_click(user['IMEI Inventory Unfold'])
        sleep(1.5)

    @allure.step("IMEI Inventory Query页面，点击Fold收起筛选按钮")
    def click_fold(self):
        self.is_click(user['IMEI Inventory Fold'])

    @allure.step("IMEI Inventory Query页面，输入material字段 ")
    def input_material_id(self, content1):
        self.presence_sleep_dcr(user['IMEI Inventory Material ID'])
        self.is_click(user['IMEI Inventory Material ID'])
        self.input_text(user['IMEI Inventory Material ID'], txt=content1)

    @allure.step("IMEI库存页面，输入Warehouse查询仓库下的IMEI")
    def input_warehouse_query(self, warehouse):
        self.is_click(user['IMEI Inventory Warehouse'])
        self.input_text(user['IMEI Inventory Warehouse'], warehouse)
        sleep(2)
        self.presence_sleep_dcr(user['IMEI Inventory Warehouse Value'], warehouse)
        self.is_click_dcr(user['IMEI Inventory Warehouse Value'], warehouse)

    @allure.step("IMEI库存页面，根据Brand 查询仓库下的IMEI")
    def select_brand_query(self, brand):
        self.is_click(user['IMEI库存点击Brand'])
        self.is_click(user['IMEI库存select brand'], brand)

    @allure.step("IMEI库存页面，根据Box_ID 查询箱号下的IMEI")
    def input_box_id_query(self, box_id):
        self.input_text(user['Query Box ID'], box_id)

    @allure.step("IMEI Inventory Query页面，点击查询按钮")
    def click_inventory_search(self):
        self.is_click(user['IMEI库存查询按钮'])
        sleep(4)

    @allure.step("IMEI Inventory Query页面，获取列表 第一行IMEI文本内容")
    def get_text_imei_inventory1(self):
        self.presence_sleep_dcr(user['获取IMEI文本内容1'])
        imei = self.element_text(user['获取IMEI文本内容1'])
        return imei

    @allure.step("IMEI Inventory Query页面，获取列表IMEI文本内容")
    def get_text_imei_inventory(self):
        self.presence_sleep_dcr(user['获取IMEI文本内容'])
        imei = self.element_text(user['获取IMEI文本内容'])
        return imei

    @allure.step("IMEI Inventory Query页面，获取列表IMEI文本内容")
    def get_text_imei_inventory2(self):
        imei2 = self.element_text(user['获取IMEI文本内容2'])
        return imei2

    @allure.step("IMEI Inventory Query页面，获取列表box id文本内容")
    def get_list_box_id_text(self):
        box_id = self.element_text(user['Get list Box ID text'])
        return box_id

    @allure.step("刷新页面")
    def click_refresh(self, drivers):
        Base(drivers).refresh()

    @allure.step("关闭Sales Order销售单菜单")
    def click_close_sales_order(self):
        self.is_click(user['关闭销售单菜单'])


    @allure.step("关闭IMEI Inventory query菜单")
    def click_close_imei_inventory(self):
        self.is_click(user['关闭IMEI Inventory Query'])


    @allure.step("IMEI Inventory Query菜单, 根据box id筛选指定箱号记录")
    def query_inventory_box_id(self, box_id):
        self.input_box_id_query(box_id)
        self.click_inventory_search()

    @allure.step("IMEI Inventory Query菜单，获取列表total分页总条数")
    def get_inventory_list_total(self):
        get_list_total = self.element_text(user['Get list Total'])
        get_list_total1 = get_list_total[6:]
        return get_list_total1

    @allure.step("IMEI Inventory Query菜单, 根据IMEI条件筛选库存IMEI记录")
    def imei_inventory_query_imei(self, query_imei):
        self.click_unfold()
        self.input_text(user['IMEI Inventory Query IMEI'], query_imei)
        self.click_fold()
        self.click_inventory_search()

    @allure.step("IMEI Inventory Query菜单, 根据Warehouse、brand与Activated条件筛选库存IMEI记录")
    def imei_inventory_query_imei2(self, warehouse, brand, activated):
        self.click_unfold()
        self.is_click(user['IMEI Inventory Warehouse'])
        self.is_click(user['IMEI Inventory Warehouse Value'], warehouse)
        self.is_click(user['IMEI库存点击Brand'])
        self.is_click(user['IMEI库存select brand'], brand)
        self.is_click(user['IMEI Inventory Activated'])
        self.is_click(user['IMEI Inventory Activated Value'], activated)
        self.click_fold()
        self.click_inventory_search()


    #筛选Shop Sales Query页面，IMEI 条件的门店销量数据
    @allure.step("Shop Sales Query菜单, 根据Shop 与IMEI 筛选列表门店销量IMEI记录")
    def shop_sales_query_imei(self, imei):
        self.input_text(user['Shop Sales Query IMEI SN'], imei)
        self.is_click(user['IMEI库存查询按钮'])
        sleep(4)

    @allure.step("Shop Sales Query菜单, 获取列表分页总条数")
    def shop_sales_assert_total(self):
        self.presence_sleep_dcr(user['Get Shop Sales list Total'])
        get_total = self.element_text(user['Get Shop Sales list Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("Shop Sales Query菜单, 获取列表字段内容")
    def get_list_field_text(self, field):
        self.presence_sleep_dcr(user[field])
        get_field = self.element_text(user[field])
        return get_field


    @allure.step("断言 Shop Purchase Query列表，字段列、字段内容是否与预期的字段内容值一致，有滚动条")
    def assert_shop_purchase_query_field(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格指定列内容'], header, content, sc_element=user['滚动条'])


    @allure.step("Shop Sales Query菜单, 勾选记录，然后点击删除功能")
    def shop_sales_query_delete(self):
        self.is_click(user['Shop Sales Query check box'])
        self.is_click(user['Shop Sales Query Delete'])
        sleep(0.5)
        self.is_click(user['Shop Sales Query Confirm Del'])


    #筛选Shop Purchase Query页面，IMEI 条件的数据门店采购数据
    @allure.step("Shop Purchase Query菜单, 根据Shop 与IMEI 筛选列表门店销量IMEI记录")
    def shop_purchase_query_imei(self, imei):
        self.input_text(user['Shop Purchase Query IMEI'], imei)
        self.is_click(user['IMEI库存查询按钮'])
        sleep(4)

    @allure.step("Shop Purchase Query菜单, 勾选记录，然后点击删除功能")
    def shop_purchase_query_cancel(self):
        self.is_click(user['Shop Purchase Query check box'])
        self.is_click(user['Shop Purchase Query Cancel'])
        sleep(0.6)
        self.is_click(user['Shop Purchase Query Confirm Cancel'])

    #Shop Inventory IMEI Query页面，筛选IMEI的门店库存数据
    @allure.step("Shop Inventory IMEI Query菜单, 筛选IMEI查询门店库存数据")
    def shop_inventory_imei_query_imei(self, imei):
        self.is_click(user['Shop Inventory IMEI Query IMEI1'])
        sleep(1)
        self.input_text(user['Shop Inventory IMEI Query IMEI2'], imei)
        self.is_click(user['Sales Order Search'])
        sleep(3)

    @allure.step("Shop Inventory IMEI Query菜单, 获取列表Total分页总条数")
    def get_shop_inventory_imei_total(self):
        shop_inventory_total = self.element_text(user['Get Shop Inventory IMEI Total'])
        shop_inventory_total1 = shop_inventory_total[6:]
        return shop_inventory_total1



class InboundReceiptPage(Base):
    """InboundReceiptPage快速收货定位方法"""
    @allure.step("快速收货页面，输入销售单ID条件筛选")
    def input_salesOrder(self, content):
        self.input_text(user['Sales Order ID'], txt=content)

    @allure.step("快速收货页面，输入出库单ID条件筛选")
    def input_deliveryOrder(self, content):
        self.input_text(user['Delivery Order ID'], txt=content)

    @allure.step("快速收货页面，点击Search")
    def click_inbound_receipt_search(self):
        self.is_click(user['Inbound Receipt Search'])
        sleep(4)

    @allure.step("获取列表第一个销售单ID")
    def get_text_salesOrder(self):
        self.presence_sleep_dcr(user['获取列表第一个销售单ID'])
        salesorder = self.element_text(user['获取列表第一个销售单ID'])
        return salesorder

    @allure.step("获取列表第一个出库单ID")
    def get_text_deliveryOrder(self):
        delivery_order = self.element_text(user['获取列表第一个出库单ID'])
        return delivery_order

    @allure.step("快速收货页面，勾选第一个复选框")
    def click_checkbox(self):
        self.presence_sleep_dcr(user['第一个复选框'])
        self.is_click_dcr(user['第一个复选框'])

    @allure.step("快速收货页面，点击Quick Received按钮")
    def click_quick_received(self):
        """快速收货页面，点击Quick Received按钮"""
        self.is_click_dcr(user['快速收货按钮'])
        sleep(2)

    @allure.step("快速收货页面，点击Save按钮")
    def click_save(self):
        self.is_click_dcr(user['保存'])
        sleep(0.7)

    @allure.step("快速收货页面，提交成功后获取提交成功提示语")
    def get_successfully_text(self):
        success = self.element_text(user['获取收货成功提示'])
        return success

    @allure.step("快速收货页面，获取列表第一条记录的最新状态")
    def get_text_status(self):
        self.presence_sleep_dcr(user['获取第一个Status'])
        status = self.element_text(user['获取第一个Status'])
        return status

    @allure.step("快速收货页面，点击Reset重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])

    @allure.step("快速收货页面，点击关闭Inbound Receipt菜单")
    def click_close_inbound_receipt(self):
        self.is_click(user['关闭二代收货菜单'])



if __name__ == '__main__':
    pass