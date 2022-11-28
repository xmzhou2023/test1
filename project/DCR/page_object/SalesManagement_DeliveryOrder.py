from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from public.base.assert_ui import ValueAssert
import random
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class DeliveryOrderPage(Base):
    """DeliveryOrderPage类，Delivery Order页面，查询与新建出库单功能 元素定位"""

    @allure.step("出库单页面，输入销售订单号")
    def input_salesorder(self, content):
        self.input_text(user['Input Sales Order ID'], txt=content)
        sleep(1)

    @allure.step("出库单页面，输入出库订单号")
    def input_deliveryorder(self, content):
        self.input_text(user['Input Delivery Order ID'], txt=content)
        sleep(1)

    @allure.step("出库单页面，点击Search")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(4)

    @allure.step("出库单页面，点击Reset")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(3)

    @allure.step("出库单页面，点击Add新增出库单")
    def click_add(self):
        self.presence_sleep_dcr(user['新增出库单'])
        self.is_click(user['新增出库单'])
        sleep(2)

    @allure.step("Add新增出库单页面，选择仓库")
    def select_warehouse_name(self, warehouse):
        self.is_click(user['Warehouse Name'])
        sleep(1)
        self.is_click(user['Warehouse Name Value'], warehouse)

    @allure.step("Add新增出库单页面，输入国包账号的Buyer属性")
    def input_sub_buyer(self, content):
        self.presence_sleep_dcr(user['Buyer'])
        self.is_click(user['Buyer'])
        self.input_text(user['Buyer'], content)
        sleep(1.5)
        self.presence_sleep_dcr(user['Buyer sub value'], content)
        self.is_click(user['Buyer sub value'], content)

    @allure.step("Add新增出库单页面，输入二代账号的Buyer属性")
    def input_retail_buyer(self, content):
        self.presence_sleep_dcr(user['Buyer'])
        self.is_click(user['Buyer'])
        self.input_text(user['Buyer'], content)
        sleep(2)
        self.is_click(user['Buyer retail value'], content)

    @allure.step("Add新增出库单页面，payment mode属性")
    def input_deli_pay_mode(self, content):
        self.presence_sleep_dcr(user['payment mode'])
        self.is_click(user['payment mode'])
        self.input_text(user['payment mode'], content)
        sleep(1)
        self.is_click(user['payment mode Online'], content)

    @allure.step("Add新增出库单页面，IMEI属性")
    def input_imei(self, content):
        self.input_text(user['Input IMEI'], content)

    @allure.step("Add新增出库单页面，Check按钮")
    def click_check(self):
        self.is_click_dcr(user['Check'])


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

    @allure.step("Add新增出库单页面，点击Check按钮后，获取Order Detail列表Product内容")
    def get_delivery_order_detail_product(self):
        get_delivery_product = self.element_text(user['Get Delivery Order Detail Product'])
        return get_delivery_product


    @allure.step("Add新增出库单页面，点击check后，Scan Record扫码记录下侧出现显示IMEI")
    def get_Deli_Scan_Record_IMEI(self, imei):
        self.presence_sleep_dcr(user['Get Delivery Scan Record IMEI'], imei)
        scan_record_imei = self.element_text(user['Get Delivery Scan Record IMEI'], imei)
        return scan_record_imei

    @allure.step("Add新增出库单页面，Submit按钮")
    def click_submit(self):
        self.is_click(user['Submit'])
        sleep(0.6)

    @allure.step("Add新增出库单页面，Submit按钮")
    def get_text_submit(self):
        submit = self.element_text(user['Submit'])
        return submit

    @allure.step("Add新增出库单页面，确认Submit按钮")
    def get_text_submit_affirm(self):
        self.presence_sleep_dcr(user['Affirm Submit'])
        affirm = self.element_text(user['Affirm Submit'])
        return affirm

    @allure.step("Add新增出库单页面，确认Submit按钮")
    def click_submit_affirm(self):
        self.is_click(user['Affirm Submit'])
        sleep(1)

    @allure.step("获取出库单列表的 销售单ID文本")
    def text_sales_order(self):
        self.presence_sleep_dcr(user['Get Sales Order ID Text'])
        sales_order = self.element_text(user['Get Sales Order ID Text'])
        return sales_order

    @allure.step("获取出库单列表的 出库单ID文本")
    def text_delivery_order(self):
        self.presence_sleep_dcr(user['Get Delivery Order ID Text'])
        delivery_order = self.element_text(user['Get Delivery Order ID Text'])
        return delivery_order

    @allure.step("获取出库单列表的 Status文本")
    def text_delivery_Status(self):
        delivery_status = self.element_text(user['Get Status Text'])
        return delivery_status

    def delivery_convert_status(self, content):
        if content == 80200000:
            status = "On Transit"
            return status

    """Delivery Order页面查询与导出功能元素定位"""
    @allure.step("点击Unfold展开筛选条件")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("点击Fold 合拢筛选条件")
    def click_fold(self):
        self.is_click(user['Fold'])
        sleep(1)

    @allure.step("输入Delivery Date开始与结束日期筛选")
    def input_delivery_date(self, content1, content2):
        self.is_click(user['Delivery Start Date'])
        self.input_text(user['Delivery Start Date'], txt=content1)
        sleep(1)
        self.is_click(user['Delivery End Date'])
        self.input_text(user['Delivery End Date'], txt=content2)

    @allure.step("点击 Status输入框")
    def click_status_input_box(self):
        self.is_click(user['点击状态输入框'])

    @allure.step("获取Total分页总条数文本")
    def get_total_text(self):
        total = self.element_text(user['Total'])
        total1 = total[6:]
        return total1

    @allure.step("获取列表Sales Order ID文本内容")
    def get_sales_order_text(self):
        self.presence_sleep_dcr(user['Get Sales Order ID Text'])
        sales_order = self.element_text(user['Get Sales Order ID Text'])
        return sales_order

    @allure.step("获取列表Delivery Order ID文本内容")
    def get_delivery_order_text(self):
        self.presence_sleep_dcr(user['Get Delivery Order ID Text'])
        delivery_order = self.element_text(user['Get Delivery Order ID Text'])
        return delivery_order

    @allure.step("获取列表Delivery Date文本内容")
    def get_delivery_date_text(self):
        deli_date = self.element_text(user['Get Delivery Date Text'])
        return deli_date

    @allure.step("获取列表Status文本内容")
    def get_status_text(self):
        status = self.element_text(user['Get Status Text'])
        return status

    @allure.step("出库单页面，no Data文本内容")
    def get_no_data(self):
        get_no_data = self.element_text(user['No Data'])
        return get_no_data

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])
        #sleep(1)

    @allure.step("出库单页面，关闭出库单菜单")
    def click_close_delivery_order(self):
        self.is_click(user['关闭出库单菜单'])
        #sleep(1)

    @allure.step("出库单页面，关闭IMEI Detail详情页")
    def click_close_imei_detail(self):
        self.is_click(user['关闭IMEI详情页'])
        #sleep(1)


    #Delivery Order列表数据筛选后，导出操作成功后验证
    @allure.step("Delivery Order页面，点击导出功能")
    def click_export(self):
        self.find_element(user['Click Export'])
        self.is_click(user['Click Export'])
        sleep(2)

    @allure.step("点击下载Download Icon,more更多按钮")
    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        sleep(3)

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(2)
        self.is_click_dcr(user['Task Name value'], content)

    @allure.step("循Base环点击查询，直到获取到下载状态为COMPLETE")
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
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    @allure.step("导出记录页面，获取列表 Create Date文本")
    def get_create_date_text(self):
        self.scroll_into_view(user['获取创建日期文本'])
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

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 1:
            logging.info("查看Delivery Order列表，加载数据正常，分页总记录数：{}".format(total))
        else:
            logging.info("查看Delivery Order列表，加载数据失败，分页总记录数：{}".format(total))

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
        sleep(1)

    @allure.step("获取出库单列表，字段内容")
    def get_list_field_text(self, field):
        self.scroll_into_view(user[field])
        get_field = self.element_text(user[field])
        return get_field

    @allure.step("获取复选框对应的 Class属性是否包含is-checked")
    def get_field_style_color(self, field):
        ss = self.find_element(user[field])
        get_check_style = ss.get_attribute('style')
        return get_check_style


    @allure.step("后端断言，创建出库单成功后，数据库表是否新增出库单记录")
    def select_sql_delivery_order(self, warehouse, seller, buyer):
        sql2 = SQL('DCR', 'test')
        varsql2 = f"select order_code, delivery_code from t_channel_delivery_ticket where warehouse_id='{warehouse}' and seller_id='{seller}' and buyer_id='{buyer}' and status=80200000 order by created_time desc limit 1"
        result = sql2.query_db(varsql2)
        order_code = result[0].get("order_code")
        delivery_code = result[0].get("delivery_code")
        logging.info("打印数据库查询的销售单ID order_code{}".format(order_code))
        logging.info("打印数据库查询的出库单ID delivery_code{}".format(delivery_code))
        ValueAssert.value_assert_equal(order_code, delivery_code)
        return order_code


    @allure.step("创建出库单的操作步骤,封装公共方法")
    def create_delivery_order(self, buyer, pay, box_id):
        self.click_add()
        self.input_retail_buyer(buyer)
        self.input_deli_pay_mode(pay)
        self.input_imei(box_id)
        self.click_check()
        sleep(0.8)

    @allure.step("创建出库单，选择卖家仓库，输入多个IMEI 场景操作步骤,封装公共方法")
    def create_delivery_order_many_imei(self, warehouse, buyer, pay, imei1, imei2):
        self.click_add()
        self.select_warehouse_name(warehouse)
        self.input_retail_buyer(buyer)
        self.input_deli_pay_mode(pay)
        self.input_imei(imei1)
        self.click_check()
        sleep(0.8)
        self.input_imei(imei2)
        self.click_check()
        sleep(0.8)

    @allure.step("创建出库单，选择卖家仓库，输入一个IMEI 场景操作步骤,封装公共方法")
    def create_delivery_order_imei(self, warehouse, buyer, pay, imei1):
        self.click_add()
        self.select_warehouse_name(warehouse)
        self.input_retail_buyer(buyer)
        self.input_deli_pay_mode(pay)
        self.input_imei(imei1)
        self.click_check()
        sleep(0.8)


    """创建出库单，产品为无码的出库单"""
    @allure.step("点击无码单选按钮")
    def click_quantity_radio_button(self):
        self.is_click(user['Quantity Radio Button'])
        sleep(2)

    @allure.step("点击无码对应的Add")
    def click_quantity_add(self):
        self.is_click(user['Quantity Add'])
        sleep(1.5)

    @allure.step("输入出库单无码产品")
    def click_quantity_product(self, content):
        self.scroll_into_view(user['Quantity Input Product'])
        self.presence_sleep_dcr(user['Quantity Input Product'])
        self.is_click(user['Quantity Input Product'])
        sleep(2)
        self.is_click(user['Quantity Input Product Value'], content)

    @allure.step("输入出库单无码数量")
    def input_delivery_quantity(self, content):
        self.is_click(user['Delivery Input Quantity'])
        self.input_text(user['Delivery Input Quantity'], txt=content)
        sleep(2)
        self.is_click(user['Get Delivery Quantity Text'])

    @allure.step("获取Delivery Quantity文本内容")
    def get_delivery_quantity_text(self):
        get_quantity_text = self.element_text(user['Get Delivery Quantity Text'])
        return get_quantity_text

    @allure.step("点击Delivery Quantity出库单数量文本")
    def click_delivery_quantity_text(self):
        self.is_click(user['Get Delivery Quantity Text'])


    """新建出库单时，新建临时客户"""
    @allure.step("点击新建临时客户")
    def click_temporary_customer(self):
        self.is_click(user['Create Temporary Customer'], "Create Temporary Customer")
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


    """查询出库单的IMEI Detail 详情信息"""
    @allure.step("点击出库单的IMEI Detail 详情信息")
    def click_imei_detail(self):
        self.is_click_dcr(user['Click IMEI Detail'])
        sleep(2.5)

    @allure.step("获取列表Product文本")
    def get_list_product_text(self):
        self.scroll_into_view(user['Get List Product Text'])
        get_list_product = self.element_text(user['Get List Product Text'])
        return get_list_product

    @allure.step("获取列表Item文本")
    def get_list_item_text(self):
        self.scroll_into_view(user['Get List Item Text'])
        get_list_item = self.element_text(user['Get List Item Text'])
        return get_list_item


    @allure.step("IMEI Detail页面，获取Title标题的Sales Order")
    def get_detail_title_sale_text(self):
        self.presence_sleep_dcr(user['Get IMEI Detail Title'])
        get_detail_title = self.element_text(user['Get IMEI Detail Title'])
        return get_detail_title

    @allure.step("IMEI Detail页面，获取Product文本")
    def get_detail_product_text(self):
        get_detail_product = self.element_text(user['Get IMEI Detail Product Text'])
        return get_detail_product

    @allure.step("IMEI Detail页面，获取Item文本")
    def get_detail_item_text(self):
        get_detail_item = self.element_text(user['Get IMEI Detail Item Text'])
        return get_detail_item

    @allure.step("IMEI Detail页面，获取IMEI文本")
    def get_detail_imei_text(self):
        get_detail_imei = self.element_text(user['Get IMEI Detail IMEI Text'])
        return get_detail_imei

    @allure.step("IMEI Detail页面，获取Total文本")
    def get_detail_total_text(self):
        get_detail_total = self.element_text(user['Get IMEI Detail Total Text'])
        return get_detail_total

    @allure.step("Delivery Order页面，根据销售单与出库单号筛选新增的出库单记录")
    def query_delivery_order(self, order_code, delivery_code):
        self.input_salesorder(order_code)
        self.input_deliveryorder(delivery_code)
        self.click_search()




if __name__ == '__main__':
    pass