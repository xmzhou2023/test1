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
        sleep(5.5)

    @allure.step("出库单页面，点击Reset")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(3)

    @allure.step("出库单页面，点击Add新增出库单")
    def click_add(self):
        Base.presence_sleep_dcr(self, user['新增出库单'])
        self.is_click(user['新增出库单'])
        sleep(2)

    @allure.step("Add新增出库单页面，输入国包账号的Buyer属性")
    def input_sub_buyer(self, content):
        Base.presence_sleep_dcr(self, user['Buyer'])
        self.is_click(user['Buyer'])
        sleep(1)
        self.input_text(user['Buyer'], txt=content)
        sleep(2.5)
        self.is_click(user['Buyer sub value'], "BD2915")

    @allure.step("Add新增出库单页面，输入二代账号的Buyer属性")
    def input_retail_buyer(self, content):
        Base.presence_sleep_dcr(self, user['Buyer'])
        self.is_click(user['Buyer'])
        self.input_text(user['Buyer'], txt=content)
        sleep(2)
        self.is_click(user['Buyer retail value'], "EG000562")

    @allure.step("Add新增出库单页面，payment mode属性")
    def input_deli_pay_mode(self, content):
        Base.presence_sleep_dcr(self, user['payment mode'])
        self.is_click(user['payment mode'])
        self.input_text(user['payment mode'], txt=content)
        sleep(1)
        self.is_click(user['payment mode Online'], content)

    @allure.step("Add新增出库单页面，IMEI属性")
    def input_imei(self, content):
        self.input_text(user['Input IMEI'], txt=content)

    @allure.step("Add新增出库单页面，Check按钮")
    def click_check(self):
        self.is_click_dcr(user['Check'])
        sleep(1)

    @allure.step("Add新增出库单页面，Submit按钮")
    def click_submit(self):
        self.is_click(user['Submit'])
        sleep(1)

    @allure.step("Add新增出库单页面，Submit按钮")
    def get_text_submit(self):
        submit = self.element_text(user['Submit'])
        return submit

    @allure.step("Add新增出库单页面，确认Submit按钮")
    def get_text_submit_affirm(self):
        Base.presence_sleep_dcr(self, user['Affirm Submit'])
        affirm = self.element_text(user['Affirm Submit'])
        return affirm

    @allure.step("Add新增出库单页面，确认Submit按钮")
    def click_submit_affirm(self):
        self.is_click(user['Affirm Submit'])
        sleep(1)

    @allure.step("获取出库单列表的 销售单ID文本")
    def text_sales_order(self):
        Base.presence_sleep_dcr(self, user['Get Sales Order ID Text'])
        sales_order = self.element_text(user['Get Sales Order ID Text'])
        return sales_order

    @allure.step("获取出库单列表的 出库单ID文本")
    def text_delivery_order(self):
        delivery_order = self.element_text(user['Get Delivery Order ID Text'])
        return delivery_order

    @allure.step("获取出库单列表的 Status文本")
    def text_delivery_Status(self):
        delivery_status = self.element_text(user['Get Status Text'])
        return delivery_status


    """DeliveryOrderPage类，测试环境，Delivery Order页面查询与导出功能元素定位"""
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
        Base.presence_sleep_dcr(self, user['Get Sales Order ID Text'])
        sales_order = self.element_text(user['Get Sales Order ID Text'])
        return sales_order

    @allure.step("获取列表Delivery Order ID文本内容")
    def get_delivery_order_text(self):
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
        sleep(2)

    @allure.step("出库单页面，关闭出库单菜单")
    def click_close_delivery_order(self):
        self.is_click(user['关闭出库单菜单'])
        sleep(2)

    @allure.step("出库单页面，关闭IMEI Detail详情页")
    def click_close_imei_detail(self):
        self.is_click(user['关闭IMEI详情页'])
        sleep(1.5)

    #Delivery Order列表数据筛选后，导出操作成功后验证
    @allure.step("Delivery Order页面，点击导出功能")
    def click_export(self):
        Base.find_element(self, user['Click Export'])
        self.is_click(user['Click Export'])
        sleep(2)

    @allure.step("点击下载Download Icon,more更多按钮")
    def click_download_more(self):
        self.is_click(user['Download Icon'])
        sleep(1)
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        sleep(5)

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        down_status = Base.export_download_status(self, user['Export Record Search'], user['获取下载状态文本'])
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


    """#创建出库单，产品为无码的出库单"""
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
        Base.presence_sleep_dcr(self, user['Quantity Input Product'])
        self.is_click(user['Quantity Input Product'])
        sleep(2)
        self.is_click(user['Quantity Input Product Value'], content)
        sleep(1)

    @allure.step("输入出库单无码数量")
    def input_delivery_quantity(self, content):
        self.is_click_dcr(user['Delivery Input Quantity'])
        sleep(1)
        self.input_text_dcr(user['Delivery Input Quantity'], txt=content)
        sleep(1)
        self.is_click(user['Get Delivery Quantiry Text'])

    @allure.step("获取Delivery Quantity文本值")
    def get_delivery_quantity_text(self, content):
        get_quantiry_text = self.element_text(user['Get Delivery Quantiry Text'])
        ValueAssert.value_assert_equal(content, get_quantiry_text)
        sleep(1)


    """新建出库单时，新建临时客户"""
    @allure.step("点击临时客户")
    def click_temporary_customer(self):
        self.is_click(user['Create Temporary Customer'], "Create Temporary Customer")
        sleep(1.5)

    @allure.step("输入临时客户名称")
    def input_temporary_customer_name(self, content):
        Base.presence_sleep_dcr(self, user['Temporary Customer Name'])
        self.is_click(user['Temporary Customer Name'])
        self.input_text(user['Temporary Customer Name'], content)

    @allure.step("输入临时客户联系电话")
    def input_customer_contact_no(self, content):
        self.is_click(user['Temporary Contact No'])
        self.input_text(user['Temporary Contact No'], content)

    @allure.step("点击业务类型下拉框")
    def click_business_type(self):
        self.is_click(user['Business Type'])
        sleep(2)
        self.is_click(user['Business Type value'], "Retail&Wholesale")

    @allure.step("随机生成数字")
    def customer_random(self):
        num = str(random.randint(100, 999))
        return num


    """查询出库单的IMEI Detail 详情信息"""
    @allure.step("查询出库单的IMEI Detail 详情信息")
    def click_imei_detail(self):
        self.is_click(user['Click IMEI Detail'])
        sleep(2.5)

    @allure.step("获取列表Product文本")
    def get_list_product_text(self):
        get_list_product = self.element_text(user['Get List Product Text'])
        return get_list_product

    @allure.step("获取列表Item文本")
    def get_list_item_text(self):
        get_list_item = self.element_text(user['Get List Item Text'])
        return get_list_item


    @allure.step("IMEI Detail页面，获取Title标题的Sales Order")
    def get_detail_title_sale_text(self):
        Base.presence_sleep_dcr(self, user['Get IMEI Detail Title'])
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


if __name__ == '__main__':
    pass