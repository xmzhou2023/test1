from libs.common.read_element import Element
import logging
from public.base.basics import Base
from libs.common.time_ui import sleep
from public.base.assert_ui import ValueAssert
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ReturnOrderPage(Base):
    """ReturnOrderPage 类"""
    @allure.step("退货单页面，点击Add")
    def click_Add(self):
        self.presence_sleep_dcr(user['Add'])
        self.is_click(user['Add'])
        sleep(1)

    @allure.step("退货单页面，点击退货到Return To Seller卖家")
    def click_Return_Type(self):
        self.presence_sleep_dcr(user['Return To Seller'])
        self.is_click(user['Return To Seller'])

    @allure.step("退货单页面，点击单选按钮BoxID IMEI输入IMEI退货")
    def radio_Boxid_IMEI(self):
        self.presence_sleep_dcr(user['Radio BoxID IMEI'])
        self.is_click(user['Radio BoxID IMEI'])

    @allure.step("退货单页面，点击单选按钮Delivery order出库单退货")
    def radio_Delivery_order(self):
        self.is_click(user['Radio Delivery order'])


    @allure.step("退货单页面，点击BoxIDIMEI单选按钮后，输入IMEI or Box ID退货")
    def input_BoxID_IMEI(self, imei):
        self.is_click(user['Input BoxID IMEI'])
        self.input_text(user['Input BoxID IMEI'], txt=imei)

    @allure.step("退货单页面，点击Delivery Order单选按钮后，输入Delivery Order ID退货")
    def input_Delivery_order(self, content):
        self.is_click(user['Input Delivery Order'])
        sleep(1)
        self.input_text(user['Input Delivery Order'], txt=content)

    @allure.step("新建退货单页面，点击Check")
    def click_Check(self):
        self.is_click_dcr(user['Click Check'])
        sleep(1)

    @allure.step("退货单页面，点击check按钮，获取结果Succeed文本")
    def get_text_Record(self):
        self.presence_sleep_dcr(user['Get Scan Record'], "Success")
        record = self.element_text(user['Get Scan Record'], "Success")
        return record

    @allure.step("退货单页面，点击check按钮，获取结果IMEI文本内容")
    def get_Scan_Record_IMEI(self, imei):
        get_imei = self.element_text(user['Get Scan Record IMEI'], imei)
        return get_imei

    @allure.step("退货单页面，点击check按钮，获取 Scanned 扫码数量文本内容")
    def get_scanned_number(self):
        get_scanned = self.element_text(user['Get Scanned number'])
        return get_scanned

    @allure.step("退货单页面，点击check后，获取Order Detail列表的Delivery Order ID文本")
    def get_Order_Detail_Deli_Order_ID(self):
        delivery_order_id = self.element_text(user['Get Order Detail Deli Order ID'])
        return delivery_order_id

    @allure.step("退货单页面，点击check后，获取Order Detail列表的Seller ID文本")
    def get_Order_Detail_Seller_ID(self):
        seller_id = self.element_text(user['Get Order Detail Seller ID'])
        return seller_id

    @allure.step("退货单页面，点击check后，获取Order Detail列表的Buyer Name文本")
    def get_Order_Detail_Buyer_ID(self):
        self.scroll_into_view(user['Get Order Detail Buyer ID'])
        buyer_id = self.element_text(user['Get Order Detail Buyer ID'])
        return buyer_id

    @allure.step("退货单页面，点击check后，获取Order Detail列表的Buyer Name文本")
    def get_Order_Detail_Return_Quantity(self):
        return_quantity = self.element_text(user['Get Order Detail Return Quantity'])
        return return_quantity


    @allure.step("退货单页面，点击Submit")
    def click_Submit(self):
        self.is_click(user['Submit'])
        sleep(0.5)

    @allure.step("获取提交退货成功提示语")
    def get_submit_success_text(self):
        submit_success = self.element_text(user['获取退货成功提示'])
        return submit_success

    @allure.step("退货单列表页面，筛选出库单ID")
    def input_Delivery_Orderid(self, content):
        self.presence_sleep_dcr(user['Input Delivery Order ID'])
        self.is_click(user['Input Delivery Order ID'])
        self.input_text(user['Input Delivery Order ID'], txt=content)

    @allure.step("退货单列表页面，点击Search")
    def click_Search(self):
        self.is_click(user['Search'])
        sleep(3)

    @allure.step("退货单列表页面， 获取第筛选后的第一个出库单ID")
    def get_text_deliveryID(self):
        self.presence_sleep_dcr(user['获取列表第一个出库单'])
        deliveryorder = self.element_text(user['获取列表第一个出库单'])
        return deliveryorder

    @allure.step("获取退货单列表，退货状态")
    def get_return_status(self):
        self.presence_sleep_dcr(user['获取列表退货状态'])
        return_status = self.element_text(user['获取列表退货状态'])
        return return_status

    @allure.step("获取退货单列表，Return Order ID退货单ID")
    def get_list_return_order_id(self):
        self.presence_sleep_dcr(user['获取列表第一个退货单'])
        return_order_id = self.element_text(user['获取列表第一个退货单'])
        return return_order_id

    @allure.step("退货单列表页面，勾选第一个复选框进行退货")
    def click_checkbox(self):
        self.is_click_dcr(user['退货复选框勾选'])

    @allure.step("退货单列表页面，点击Approve按钮")
    def click_Approve_button(self):
        self.is_click(user['Approve button'])
        sleep(3)

    @allure.step("退货单列表页面，输入退货评价")
    def input_remark(self, content):
        self.presence_sleep_dcr(user['Remark'])
        self.is_click(user['Remark'])
        self.input_text(user['Remark'], txt=content)
        sleep(1)

    @allure.step("是否确认退货对话框，输入是否同意退货")
    def click_agree(self):
        self.is_click(user['Agree'])

    @allure.step("退货单列表页面， 获取退货成功后的第一个Status Approved")
    def get_text_Status(self):
        self.presence_sleep_dcr(user['获取列表退货状态'])
        status = self.element_text(user['获取列表退货状态'])
        return status

    @allure.step("退货单页面， 获取列表Return Type字段内容")
    def get_list_return_type(self):
        get_return_type = self.element_text(user['获取列表退货类型'])
        return get_return_type

    @allure.step("获取审批成功提示语")
    def get_Approval_Success(self):
        success = self.element_text(user['Approval Successfully'])
        return success


    """无码申请退货"""
    @allure.step("新建退货页面，点击无码退货单选按钮")
    def click_radio_quantity(self):
        self.is_click(user['Radio Quantity'], "Quantity")
        sleep(1)

    @allure.step("新建退货页面，输入退货的客户")
    def input_quantity_customer(self, content):
        self.presence_sleep_dcr(user['Quantity Customer'])
        self.is_click(user['Quantity Customer'])
        sleep(1)
        self.input_text(user['Quantity Customer'], txt=content)
        sleep(2.5)
        self.is_click(user['Quantity Customer value'], content)
        sleep(2)


    @allure.step("新建退货页面，输入Quantity无码退货的出库单ID")
    def input_quantity_delivery_order(self, content):
        self.is_click(user['Quantity Delivery Order ID'])
        self.input_text(user['Quantity Delivery Order ID'], txt=content)
        sleep(3)
        self.is_click(user['Quantity Delivery Order ID value'], content)

    @allure.step("新建退货页面，输入退货的product")
    def click_quantity_product(self, content):
        self.is_click(user['Quantity Product'])
        sleep(1.5)
        self.is_click(user['Quantity Product value'], content)

    @allure.step("新建退货页面，输入退货的数量")
    def input_return_quantity(self, content):
        self.is_click(user['Return Quantity'])
        self.input_text(user['Return Quantity'], txt=content)

    @allure.step("新建退货页面，切换无码退货单选按钮，点击Chek后，获取Delivery Order ID")
    def get_quantity_deli_order_text(self, content):
        self.presence_sleep_dcr(user['Get Quantity Delivery Order Text'], content)
        get_quantity_deli = self.element_text(user['Get Quantity Delivery Order Text'], content)
        return get_quantity_deli

    @allure.step("新建退货页面，切换无码退货单选按钮，点击Chek后，获取Seller ID")
    def get_quantity_seller_id_text(self, content):
        get_seller_id = self.element_text(user['Get Quantity Seller ID Text'], content)
        return get_seller_id

    @allure.step("新建退货页面，切换无码退货单选按钮，点击Chek后，获取Buyer ID")
    def get_quantity_buyer_id_text(self, content):
        get_buyer_id = self.element_text(user['Get Quantity Buyer ID Text'], content)
        return get_buyer_id

    @allure.step("退货页面，点击关闭退货菜单")
    def click_close_return_order(self):
        self.is_click(user['关闭退货菜单'])
        #sleep(1)

    @allure.step("退货单页面，点击More Option，然后点击Recall按钮")
    def click_more_option_recall(self):
        self.is_click(user['More Option'])
        sleep(1)
        self.presence_sleep_dcr(user['Recall'])
        self.is_click(user['Recall'])
        sleep(1)
        self.presence_sleep_dcr(user['Confirm Recall'])
        self.is_click(user['Confirm Recall'])
        sleep(0.6)

    @allure.step("退货单页面，点击添加退货单操作")
    def add_return_order(self, box_id):
        self.click_Add()
        """点击退货给卖家类型"""
        self.click_Return_Type()
        self.radio_Boxid_IMEI()
        self.input_BoxID_IMEI(box_id)
        self.click_Check()

    @allure.step("退货单页面，卖家进行审核退货单操作")
    def approve_return_order(self, delivery_code):
        self.input_Delivery_Orderid(delivery_code)
        self.click_Search()
        self.click_checkbox()
        self.click_Approve_button()
        self.input_remark("同意退货")
        self.click_agree()

    @allure.step("退货单列表页，根据出库单号，查询退货单记录")
    def query_return_order(self, delivery_code):
        self.input_Delivery_Orderid(delivery_code)
        self.click_Search()


class ReturnOrderQuery(Base):
    """用户类"""

    @allure.step("退货单列表页面，点击Search")
    def click_search(self):
        self.is_click(user['Search'])
        sleep()

    @allure.step("退货单列表页面，点击export按钮")
    def click_export(self):
        self.is_click(user['导出按钮'])
        sleep()

    @allure.step("获取导出状态")
    def export_status(self):
        time=0
        try:
            while time<3:
                txt = self.element_text(user['导出界面显示'])
                sleep(time)
                time = time + 0.5
        except:
            logging.info('get download status unsuccessful')
        return txt

    @allure.step("退货单列表页面，点击export detail按钮")
    def click_export_detail(self):
        self.hover_move_click(user['更多操作'],user['导出详情'])
        sleep()

    @allure.step("获取第一行文本内容")
    def get_table_txt(self, num):
        txt = self.element_text(user['列表第一行'],num)
        return txt

    @allure.step("输入退单日期")
    def input_return_date(self, startdate, enddate):
        self.is_click(user['退货单开始日期'])
        self.input_text(user['退货单开始日期'], txt=startdate)
        self.is_click(user['退货单结束日期'])
        self.input_text(user['退货单结束日期'], txt=enddate)
        sleep()

    @allure.step("点击退货单unfold")
    def click_unfold(self):
        self.is_click(user['展开折叠'])

    @allure.step("点击reset按钮")
    def click_reset(self):
        self.is_click(user['点击重置'])

    @allure.step("点击退单ID")
    def click_return_order(self):
        self.is_click(user['退货单ID'])

    @allure.step("点击IMEI Detail")
    def click_detail(self):
        sleep()
        logging.info('begin click IMEI detail')
        self.is_click_dcr(user['IMEI详情'])
        logging.info('success click IMEI detail')

    @allure.step("点击IMEI Detail")
    def get_phone_detail(self):
        txt = self.element_text(user['详情页IMEI'])
        return txt

    @allure.step("关闭IMEI Detail")
    def close_phone_detail(self):
        self.is_click(user['关闭IMEI详情'])

    @allure.step("输入退单ID查询")
    def input_return_order(self, data):
        self.is_click(user['退货单ID'])
        self.input_text(user['退货单ID'], txt=data)

    @allure.step("输入出库单ID查询")
    def input_delivery_order(self, data):
        self.is_click(user['出库单ID'])
        self.input_text(user['出库单ID'], txt=data)

    @allure.step("输入退货单品牌查询")
    def input_brand(self, data):
        self.is_click(user['退货单品牌'])
        self.is_click(user['品牌_状态_类型选择'], data)
        self.is_click(user['退货单ID'])

    @allure.step("点击退货单状态查询")
    def input_return_status(self, data):
        self.is_click(user['退货单状态'])
        self.is_click(user['品牌_状态_类型选择'], data)

    @allure.step("点击退货单退货类型查询")
    def input_return_type(self, data):
        self.is_click(user['退货单类型'])
        self.is_click(user['品牌_状态_类型选择'], data)

    @allure.step("点击退货单卖家查询")
    def input_seller(self, data):
        self.is_click(user['退货单卖家'])
        self.input_text(user['退货单卖家'], txt=data)
        self.is_click(user['买家_卖家选择'], data)

    @allure.step("点击退货单买家查询")
    def input_buyer(self, data):
        self.is_click(user['退货单买家'])
        self.input_text(user['退货单买家'], txt=data)
        self.is_click(user['买家_卖家选择'], data)

    @allure.step("点击卖家仓库地址查询")
    def input_seller_area(self, data):
        self.is_click(user['卖家仓库地址'])
        self.input_text(user['卖家仓库地址'], txt=data)
        self.is_click(user['卖家_买家仓库地址选择'], data)

    @allure.step("点击买家仓库地址查询")
    def input_buyer_area(self, data):
        self.is_click(user['买家仓库地址'])
        self.input_text(user['买家仓库地址'], txt=data)
        self.is_click(user['卖家_买家仓库地址选择'], data)

    @allure.step("点击退货型号查询")
    def input_model(self, data):
        self.is_click(user['退货型号'])
        self.input_text(user['退货型号输入'], txt=data)
        sleep()
        self.is_click(user['退货型号选择'], data)

    @allure.step("点击退货市场名字查询")
    def input_market_name(self, data):
        self.is_click(user['市场名字'])
        self.input_text(user['市场名字输入'], txt=data)
        sleep()
        self.is_click(user['市场名字选择'], data)

    @allure.step("点击输入IMEI查询")
    def input_phone(self, data):
        self.is_click(user['IMEI点击'])
        self.input_text(user['IMEI输入'], txt=data)

    @allure.step("点击卖家国家查询")
    def input_seller_country(self, data):
        self.is_click(user['卖方国家'])
        self.input_text(user['卖方国家输入'], txt=data)
        self.is_click(user['卖方国家选择'], data)


if __name__ == '__main__':
    pass
