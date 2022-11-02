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
        sleep(3)

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
        sleep(1.5)
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
        sleep(0.8)

    @allure.step("新建销售单页面，点击确认OK按钮")
    def click_submit_OK(self):
        self.presence_sleep_dcr(user['保存成功确认OK'])
        self.is_click(user['保存成功确认OK'])
        sleep(3)

    @allure.step("销售单页面，按销售单ID条件筛选")
    def input_sales_order_ID(self, content):
        self.is_click(user['按销售单ID筛选'])
        self.input_text(user['按销售单ID筛选'], txt=content)
        sleep(2)

    @allure.step("销售单页面，点击Search查询按钮")
    def click_search(self):
        """销售单页面，点击Search查询按钮"""
        self.is_click(user['Search'])
        sleep(2)

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
        #self.presence_sleep_dcr(user['勾选第一条销售单ID'])
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

    @allure.step("刷新页面")
    def click_refresh(self, drivers):
        ref = Base(drivers)
        ref.refresh()

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
        sleep(1)

    @allure.step("点击删除按钮")
    def click_delete_sales(self):
        self.is_click_dcr(user['Delete Sales Order'])
        sleep(1)

    @allure.step("点击确认删除按钮")
    def click_confirm_delete(self):
        self.presence_sleep_dcr(user['Confirm Delete'])
        self.is_click(user['Confirm Delete'])

    @allure.step("点击Reset按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(2)

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
    def click_business_type(self):
        self.is_click(user['Business Type'])
        sleep(2)
        self.is_click(user['Business Type value'], "Retail&Wholesale")

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
        sleep(1)

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
        self.is_click(user['Download Icon'])
        sleep(1)
        self.presence_sleep_dcr(user['More'])
        self.is_click(user['More'])
        sleep(8)

    @allure.step("下拉输入选择的值的文本框，公共方法")
    def click_input_text(self, yamal1, yamal2, content1):
        self.is_click(user[yamal1])
        self.input_text(user[yamal1], content1)
        sleep(1.5)
        self.is_click(user[yamal2], content1)

    # @allure.step("输入Task Name筛选该任务的导出记录")
    # def input_task_name(self, content):
    #     self.is_click(user['Input Task Name'])
    #     self.input_text(user['Input Task Name'], txt=content)
    #     sleep(2)
    #     self.is_click(user['Task Name value'], content)

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
        sleep(1)

if __name__ == '__main__':
    pass