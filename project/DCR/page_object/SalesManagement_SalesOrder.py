from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class SalesOrderPage(Base):
    """SalesOrderPage页面定位方法"""

    @allure.step("Sales Order页面，点击Add新增销售单按钮")
    def click_add_sales(self):
        sleep(1.5)
        self.presence_sleep_dcr(user['Add'])
        self.is_click(user['Add'])
        sleep(2.5)

    @allure.step("Add新增销售单页面，输入Buyer属性")
    def input_sales_buyer(self, content):
        self.presence_sleep_dcr(user['Buyer'])
        self.is_click(user['Buyer'])
        self.input_text(user['Buyer'], txt=content)
        sleep(2)
        self.is_click(user['Buyer value'], content)

    @allure.step("新建销售单页面，输入Brand属性")
    def input_sales_brand(self, content):
        self.is_click(user['Brand'])
        self.input_text(user['Brand'], txt=content)
        sleep(0.8)
        self.is_click(user['Brand value'], content)

    @allure.step("新建销售单页面，输入product属性")
    def input_sales_product(self, content):
        self.is_click(user['product'])
        self.input_text(user['product'], txt=content)
        sleep(3)
        self.is_click(user['product value'], content)

    @allure.step("新建销售单页面，输入Quantity属性")
    def input_sales_quantity(self, content):
        self.is_click(user['Quantity'])
        self.input_text(user['Quantity'], txt=content)

    @allure.step("新建销售单页面，点击提交Submit按钮")
    def click_submit(self):
        self.is_click_dcr(user['Submit Sales'])
        sleep(1)

    @allure.step("新建销售单页面，点击确认OK按钮")
    def click_submit_OK(self):
        self.presence_sleep_dcr(user['保存成功确认OK'])
        self.is_click(user['保存成功确认OK'])
        sleep(2)

    @allure.step("销售单页面，按销售单ID条件筛选")
    def input_sales_order_ID(self, content):
        self.is_click(user['按销售单ID筛选'])
        self.input_text(user['按销售单ID筛选'], content)

    @allure.step("销售单页面，点击Search查询按钮")
    def click_search(self):
        """销售单页面，点击Search查询按钮"""
        self.is_click(user['Search'])
        self.element_text(user['Loading'])

    @allure.step("获取列表Sales Order ID文本内容")
    def get_text_sales_id(self):
        """销售单页面，获取销售单ID文本"""
        self.presence_sleep_dcr(user['获取Sales Order ID文本'])
        sales_order_id = self.element_text(user['获取Sales Order ID文本'])
        return sales_order_id

    @allure.step("销售单页面，获取销售单状态 Pending文本")
    def get_text_sales_status(self, status):
        """销售单页面，获取销售单状态文本"""
        self.presence_sleep_dcr(user['获取列表Status文本'], status)
        status = self.element_text(user['获取列表Status文本'], status)
        return status

    """勾选新建的销售单，直接出库"""

    @allure.step("勾选第一条销售单ID")
    def click_checkbox_orderID(self):
        sleep(1.5)
        # self.presence_sleep_dcr(user['勾选第一条销售单ID'])
        self.is_click_dcr(user['勾选第一条销售单ID'])

    @allure.step("点击Delivery button出库按钮")
    def click_Delivery_button(self):
        self.is_click(user['Delivery button'])
        sleep(1)

    @allure.step("输入Payment Mode支付方式属性")
    def input_Payment_Mode(self, content):
        self.presence_sleep_dcr(user['Payment Mode'])
        self.is_click(user['Payment Mode'])
        self.input_text(user['Payment Mode'], txt=content)
        sleep(2)
        self.is_click(user['Payment Mode value'], content)

    @allure.step("出库单页面，输入IMEI属性")
    def input_imei(self, content):
        self.is_click(user['Input IMEI'])
        self.input_text(user['Input IMEI'], txt=content)
        sleep(1)

    @allure.step("点击check 检查按钮")
    def click_check(self):
        self.is_click_dcr(user['Check'])
        sleep(2.5)

    @allure.step("点击Submit Delivery提交出库单按钮")
    def click_submit_delivery(self):
        self.is_click_dcr(user['Submit Delivery'])
        sleep(3)

    @allure.step("获取销售单列表状态Status")
    def get_list_status_text(self):
        status = self.element_text(user['Get list Status Text'])
        return status

    @allure.step("出库操作时，输入IMEI点击Check后，Scan Record里面显示该IMEI扫码成功记录")
    def get_scan_record_success(self):
        get_success = self.element_text(user['Get Scan Record Success'])
        return get_success

    @allure.step("出库操作时，输入IMEI点击Check后，Scan Record里面显示该IMEI扫码成功记录")
    def get_scan_record_imei(self, imei):
        get_imei = self.element_text(user['Get Scan Record IMEI'], imei)
        return get_imei


    # 筛选IMEI Inventory Query页面，product对应的IMEI 元素定位
    @allure.step("销售单页面，点击IMEI Detail打开详情页")
    def click_sales_order_imei_detail(self):
        self.is_click(user['Sales Order IMEI Detail'])
        sleep(1.5)

    @allure.step("销售单页面，打开IMEI Detail打开详情页,获取对话框头文本")
    def get_sales_order_imei_detail_header(self):
        get_header = self.element_text(user['Sales Order IMEI Detail Header'])
        return get_header

    @allure.step("销售单页面，打开IMEI Detail打开详情页, 获取分页总条数文本")
    def get_sales_order_imei_detail_total(self):
        get_imei_detail_total = self.element_text(user['Sales Order IMEI Detail Total'])
        get_imei_detail_total1 = get_imei_detail_total[6:]
        return get_imei_detail_total1

    @allure.step("销售单页面，点击关闭IMEI Detail详情页")
    def close_sales_order_imei_detail(self):
        self.is_click(user['Close Sales Order IMEI Detail'])


    #筛选IMEI Inventory Query页面，product对应的IMEI 元素定位
    @allure.step("IMEI Inventory Query页面，进入iframe")
    def imei_inventory_iframe(self):
        imei_iframe = self.find_element(user['imei inventory iframe'])
        self.driver.switch_to.frame(imei_iframe)
        sleep(1)

    @allure.step("点击Unfold展开筛选按钮")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("IMEI库存页面，输入Material ID 查询")
    def input_material_id(self, content1):
        self.presence_sleep_dcr(user['Material ID'])
        self.is_click(user['Material ID'])
        self.input_text(user['Material ID'], txt=content1)
        sleep(1)

    @allure.step("IMEI库存页面，点击查询按钮")
    def click_inventory_search(self):
        self.is_click(user['IMEI库存查询按钮'])
        sleep(4)

    @allure.step("获取IMEI库存页面，IMEI文本内容")
    def get_text_imei_inventory(self):
        self.presence_sleep_dcr(user['获取IMEI文本内容'])
        imei = self.element_text(user['获取IMEI文本内容'])
        return imei

    @allure.step("关闭IMEI Inventory Query 菜单")
    def close_imei_inventory_query(self):
        self.is_click(user['关闭IMEI Inventory Query'])

    @allure.step("关闭Sales Order 菜单")
    def click_close_sales_order(self):
        self.is_click(user['关闭销售单菜单'])

    @allure.step("点击删除按钮")
    def click_delete_sales(self):
        self.is_click(user['Delete Sales Order'])
        sleep(1)

    @allure.step("点击确认删除按钮")
    def click_confirm_delete(self):
        self.presence_sleep_dcr(user['Confirm Delete'])
        self.is_click(user['Confirm Delete'])

    @allure.step("点击Reset按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        self.element_text(user['Loading'])

    @allure.step("销售单页面，输入Status状态筛选销售单")
    def input_status_query(self, status):
        self.is_click(user['list Input Status Query'])
        sleep(1.5)
        self.is_click(user['list Click Status Value'], status)


    """新建出库单时，新建临时客户"""
    @allure.step("点击新建临时客户")
    def click_temporary_customer(self):
        self.presence_sleep_dcr(user['Create Temporary Customer'])
        self.is_click(user['Create Temporary Customer'])
        sleep(1.5)

    @allure.step("输入临时客户名称")
    def input_temporary_customer_name(self, content):
        self.presence_sleep_dcr(user['Temporary Customer Name'])
        self.is_click(user['Temporary Customer Name'])
        self.input_text(user['Temporary Customer Name'], content)

    @allure.step("输入临时客户联系电话")
    def input_customer_contact_no(self, content):
        self.is_click(user['Temporary Contact No'])
        self.input_text(user['Temporary Contact No'], content)

    @allure.step("点击业务类型下拉框")
    def click_business_type(self, business):
        self.is_click(user['Business Type'])
        sleep(1)
        self.is_click(user['Business Type value'], business)

    @allure.step("随机生成数字")
    def customer_random(self):
        num = str(random.randint(100, 999))
        return num

    """对销售单进行出库操作，产品为无码的出库单"""

    @allure.step("点击无码单选按钮")
    def click_quantity_radio_button(self):
        self.is_click(user['Quantity Radio Button'])

    @allure.step("输入出库数量")
    def input_delivery_quantity(self, quantity):
        self.presence_sleep_dcr(user['Input Delivery Quantity'])
        self.is_click(user['Input Delivery Quantity'])
        self.input_text(user['Input Delivery Quantity'], txt=quantity)
        sleep(1)

    @allure.step("新建无码出库单时，获取Order Detail下的Product属性")
    def get_order_detail_product(self):
        product = self.element_text(user['Get Order Detail Product'])
        return product

    @allure.step("新建无码出库单时，获取Delivery Quantity属性")
    def get_new_delivery_quantity(self):
        quantity = self.element_text(user['Get New Delivery Quantity'])
        return quantity

    @allure.step("新建无码出库单时，点击delivery quantity属性")
    def click_delivery_quantity(self):
        self.is_click(user['Get New Delivery Quantity'])
        sleep(1)

    """Sales Order页面，导出销售单记录，操作成功后验证"""

    @allure.step("销售单页面，点击Unfold展开筛选条件")
    def click_sales_order_unfold(self):
        self.is_click(user['Sales Order Unfold'])
        sleep(2)

    @allure.step("销售单页面，输入Create Date时间筛选")
    def list_input_create_date(self, date, date1):
        self.presence_sleep_dcr(user['列表筛选创建开始日期'])
        self.is_click(user['列表筛选创建开始日期'])
        self.input_text(user['列表筛选创建开始日期'], date)
        self.is_click(user['列表筛选创建开始日期'])
        self.input_text(user['列表筛选创建截止日期'], date1)

    @allure.step("点击More Option更多操作按钮")
    def click_more_option(self):
        self.is_click(user['More Option'])
        sleep(1.5)

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])

    @allure.step("销售单页面，点击Export导出按钮")
    def click_export(self):
        self.is_click(user['Export'])
        sleep(2)

    @allure.step("销售单页面，点击Export Detail导出销售单详情按钮")
    def click_export_detail(self):
        self.is_click(user['Export Detail'])
        sleep(2)

    @allure.step("点击下载Download Icon,more更多按钮")
    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        self.element_text(user['Loading'])

    @allure.step("下拉输入选择的值的文本框，公共方法")
    def click_input_text(self, yamal1, yamal2, content1):
        self.is_click(user[yamal1])
        self.input_text(user[yamal1], content1)
        sleep(1.5)
        self.is_click(user[yamal2], content1)

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], content)
        sleep(0.5)
        if 'Sales Order Detail' == content:
            self.is_click(user['Task Name value'], content)
        else:
            self.is_click_dcr(user['Task Name value'], content)


    @allure.step("输入Create Date 开始日期筛选该任务的导出记录")
    def export_record_create_date_query(self, start_date):
        self.is_click(user['Export Record Create Date'])
        self.input_text(user['Export Record Create Date'], start_date)
        self.is_click(user['点击筛选项label'], 'Create Date')

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        down_status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
        return down_status

    @allure.step("导出记录页面，获取列表 Download Status文本")
    def get_download_status_text(self):
        status = self.element_text(user['获取下载状态文本'])
        return status

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_task_name_text(self):
        task_name = self.element_text(user['获取任务名称文本'])
        return task_name

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_file_size_text(self):
        file_size = self.element_text(user['获取文件大小文本'])
        file_size1 = file_size[0:1]
        return file_size1

    @allure.step("导出记录页面，获取列表 User ID文本")
    def get_task_user_id_text(self):
        self.scroll_into_view(user['获取用户ID文本'])
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    @allure.step("导出记录页面，获取列表 Create Date文本")
    def get_create_date_text(self):
        create_date = self.element_text(user['获取创建日期文本'])
        create_date1 = create_date[0:10]
        return create_date1

    @allure.step("导出记录页面，获取列表Complete Date文本")
    def get_complete_date_text(self):
        complete_date = self.element_text(user['获取完成日期文本'])
        complete_date1 = complete_date[0:10]
        return complete_date1

    @allure.step("导出记录页面，获取列表 Operation文本")
    def get_export_operation_text(self):
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("断言文件或导出时间是否有数据")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("Delivery Order导出成功，File Size 导出文件大于1KB:{}".format(file_size))
        else:
            logging.info("Delivery Order导出失败，File Size 导出文件小于1KB:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Delivery Order导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Delivery Order导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))

    @allure.step("断言精确查询结果 Sales Order列表，字段列、字段内容是否与预期的字段内容值一致，有滚动条")
    def assert_sales_order_field(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格指定列内容'], header, content,
                                                    sc_element=user['水平滚动条'])

    @allure.step("后端断言，创建销售单成功后，数据库表是否新增销售单记录")
    def select_sql_sales_order(self, warehouse, seller, buyer):
        sql2 = SQL('DCR', 'test')
        varsql1 = f"select order_code from t_channel_sale_ticket where warehouse_id = '{warehouse}' and seller_id = '{seller}' and buyer_id = '{buyer}' and status = 0 order by created_time desc limit 1"
        result = sql2.query_db(varsql1)
        order_code = result[0].get("order_code")
        logging.info("打印数据库查询的销售单ID order_code{}".format(order_code))
        return order_code


    @allure.step("查询订单状态")
    def search_sales_status(self, status):
        self.is_click(user['订单状态查询'])
        self.is_click(user['状态_品牌_model_ActivatedLossOrNot_单据类型_选择'], status)

    @allure.step("查询买家信息")
    def search_sales_buyer(self, buyer):
        self.is_click(user['订单买家点击'])
        self.input_text(user['订单买家查询'], buyer)
        self.is_click(user['订单买家和卖家选择'], buyer)

    @allure.step("查询卖家信息")
    def search_sales_seller(self, seller):
        self.is_click(user['订单卖家点击'])
        self.input_text(user['订单卖家查询'], seller)
        self.is_click(user['订单买家和卖家选择'], seller)

    @allure.step("查询物料ID信息")
    def search_material(self, material):
        self.is_click(user['物料ID查询'])
        self.input_text(user['物料ID查询'], material)

    @allure.step("点击物料ID信息")
    def click_material(self):
        self.is_click(user['物料ID查询'])

    @allure.step("查询品牌信息")
    def search_brand(self, brand):
        self.is_click(user['品牌查询'])
        self.is_click(user['状态_品牌_model_ActivatedLossOrNot_单据类型_选择'], brand)

    @allure.step("查询model信息")
    def search_model(self, model):
        self.is_click(user['Model点击'])
        logging.info('click succ')
        self.input_text(user['Model输入'], model)
        logging.info('input succ')
        self.is_click(user['状态_品牌_model_ActivatedLossOrNot_单据类型_选择'], model)

    @allure.step("查询Market Name信息")
    def search_market(self, market):
        self.is_click(user['MarketName查询'])
        self.input_text(user['MarketName输入'], market)
        self.is_click(user['状态_品牌_model_ActivatedLossOrNot_单据类型_选择'], market)

    @allure.step("查询丢失激活信息")
    def search_active(self, active):
        self.is_click(user['ActivatedLossOrNot查询'])
        self.is_click(user['状态_品牌_model_ActivatedLossOrNot_单据类型_选择'], active)

    @allure.step("查询创建人信息")
    def search_creator(self, creator):
        self.is_click(user['创建人查询'])
        self.input_text(user['创建人输入'], creator)
        self.is_click(user['订单买家和卖家选择'], creator)

    @allure.step("查询订单类型信息")
    def search_type(self, type):
        self.is_click(user['订单类型查询'])
        self.is_click(user['状态_品牌_model_ActivatedLossOrNot_单据类型_选择'], type)  # type不能为sales order，否则不能唯一定位

    @allure.step("查询买家类型信息")
    def search_buyer_type(self, type):
        self.is_click(user['买家类型'])
        self.is_click(user['买家类型选择'], type)

    @allure.step("查询卖家类型信息")
    def search_seller_type(self, type):
        self.is_click(user['卖家类型'])
        self.is_click(user['卖家类型选择'], type)

    @allure.step("点击IMEI Deatail信息")
    def click_imei_detail(self):
        self.is_click(user['第一行的IMEIDeatail'])
        sleep()

    @allure.step("获取列表第一行数据")
    def get_table_txt(self, num):
        txt = self.element_text(user['获取列表第一行数据'], num)
        return txt

    @allure.step("获取IMEI Deatail页面的物料信息")
    def get_detail_txt(self,num):
        txt = self.element_text(user['IMEIDeatail页面的物料id'],num)
        self.is_click(user['IMEIDeatail页面关闭按钮'])
        return txt


if __name__ == '__main__':
    pass
