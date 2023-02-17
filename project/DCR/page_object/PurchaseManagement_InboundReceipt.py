import random

from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base, random_list
from ..test_case.conftest import *
import logging

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class InboundReceiptPage(Base):
    """InboundReceiptPage类"""

    @allure.step("快速收货页面，输入销售单ID条件筛选")
    def input_salesOrder(self, content):
        """快速收货页面，输入销售单ID条件筛选"""
        self.input_text(user['Input Sales Order ID'], txt=content)

    @allure.step("快速收货页面，输入出库单ID条件筛选")
    def input_deliveryOrder(self, content):
        """快速收货页面，输入出库单ID条件筛选"""
        self.input_text(user['Input Delivery Order ID'], txt=content)

    @allure.step("快速收货页面，点击出库单ID筛选输入框")
    def click_deliver_Order(self):
        self.is_click(user['Input Delivery Order ID'])

    @allure.step("快速收货页面，点击Search")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("获取列表第一个销售单ID")
    def text_salesOrder(self):
        self.presence_sleep_dcr(user['获取列表第一个销售单ID'])
        salesorder = self.element_text(user['获取列表第一个销售单ID'])
        return salesorder

    @allure.step("获取列表第一个出库单ID")
    def text_deliveryOrder(self):
        deliveryorder = self.element_text(user['获取列表第一个出库单ID'])
        return deliveryorder

    @allure.step("获取列表文本字段内容")
    def get_list_field_text(self, context):
        self.presence_sleep_dcr(user[context])
        field = self.element_text(user[context])
        return field

    @allure.step("快速收货页面，勾选第一个复选框")
    def select_checkbox(self):
        self.is_click_dcr(user['收货第一个复选框'])

    @allure.step("快速收货页面，点击Quick Received按钮")
    def click_quick_received(self):
        self.is_click_dcr(user['快速收货按钮'])
        sleep(1)

    @allure.step("点击快速收货按钮后，弹出快速收货窗口，有多个仓库时需要选择仓库")
    def input_select_warehouse(self, warehouse):
        self.presence_sleep_dcr(user['Quick Received select Warehouse'])
        self.is_click(user['Quick Received select Warehouse'])
        self.input_text(user['Quick Received select Warehouse'], warehouse)
        sleep(0.6)
        self.is_click(user['Select Warehouse Value'], warehouse)

    @allure.step("快速收货页面，点击Save按钮")
    def click_save(self):
        self.presence_sleep_dcr(user['保存'])
        self.is_click(user['保存'])
        sleep(0.5)

    @allure.step("快速收货页面，提交成功后获取提交成功提示语")
    def get_successfully_text(self):
        success = self.element_text(user['获取收货成功提示'])
        return success

    @allure.step("快速收货页面，获取列表第一条记录的最新状态")
    def text_status(self):
        status = self.element_text(user['获取列表状态'])
        return status

    @allure.step("快速收货页面，点击Reset重置按钮")
    def click_reset(self):
        """快速收货页面，点击Reset重置按钮"""
        self.is_click(user['Reset'])
        sleep(8)

    @allure.step("快速收货页面，点击Unfold展开筛选按钮")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("快速收货页面，点击Fold收起筛选按钮")
    def click_fold(self):
        self.is_click(user['Fold'])
        sleep(1)

    @allure.step("输入出库单日期条件，进行筛选操作")
    def input_delivery_date(self, content):

        self.is_click(user['Input Delivery Start Date'])
        self.input_text_dcr(user['Input Delivery Start Date'], content)
        sleep(0.5)
        self.is_click(user['点击筛选项label'], 'Delivery Date')

    @allure.step("输入品牌条件，进行筛选操作")
    def click_select_brand(self):
        self.is_click_dcr(user['Click Select Brand'])
        sleep(1)
        self.presence_sleep_dcr(user['Select itel'])
        self.is_click(user['Select itel'])
        self.is_click(user['Select TECNO'])
        self.is_click(user['点击筛选项label'], 'Brand')

    @allure.step("获取列表Delivery Date文本")
    def get_delivery_date_text(self):
        delivery_date = self.element_text(user['Get Delivery Date'])
        return delivery_date

    @allure.step("获取收货页面，列表Status文本")
    def get_status_text(self):
        status = self.element_text(user['Get Status'])
        return status

    @allure.step("获取列表Product文本")
    def get_product_text(self):
        self.presence_sleep_dcr(user['Get Product'])
        product = self.element_text(user['Get Product'])
        return product

    @allure.step("获取列表Product文本")
    def get_itel_text(self):
        itel = self.element_text(user['Get Item'])
        return itel

    @allure.step("获取列表Product文本")
    def get_brand_text(self):
        self.presence_sleep_dcr(user['Get Brand'])
        self.scroll_into_view(user['Get Brand'])
        brand = self.element_text(user['Get Brand'])
        return brand

    @allure.step("获取列表total文本")
    def get_total_text(self):
        total = self.element_text(user['Get Total Text'])
        total1 = int(total[6:])
        return total1

    @allure.step("Inbound Receipt列表点击 IMEI Detail按钮")
    def click_imei_detail(self):
        self.is_click(user['Click IMEI Detail'])
        sleep(2)

    # IMEI Detail页面元素定位方法
    @allure.step("获取IMEI Detail页面 material_id字段内容")
    def get_imei_detail_material_id(self):
        self.presence_sleep_dcr(user['Get IMEI Detail Material ID'])
        material = self.element_text(user['Get IMEI Detail Material ID'])
        return material

    @allure.step("获取IMEI Detail页面 Product字段内容")
    def get_imei_detail_product(self):
        product = self.element_text(user['Get IMEI Detail Product'])
        return product

    @allure.step("获取IMEI Detail页面 itel字段内容")
    def get_imei_detail_itel(self):
        item = self.element_text(user['Get IMEI Detail Item'])
        return item

    @allure.step("获取IMEI Detail页面 Brand字段内容")
    def get_imei_detail_brand(self):
        brand = self.element_text(user['Get IMEI Detail Brand'])
        return brand

    @allure.step("获取IMEI Detail页面 IMEI字段内容")
    def get_imei_detail_imei(self):
        imei = self.element_text(user['Get IMEI Detail IMEI'])
        return imei

    @allure.step("获取IMEI Detail页面 total字段内容")
    def get_imei_detail_total(self):
        total = self.element_text(user['Get IMEI Detail Total'])
        total1 = total[6:]
        return total1

    @allure.step("获取IMEI Detail页面 Export字段内容")
    def get_imei_detail_export(self):
        get_export = self.element_text(user['Get IMEI Detail Export'])
        return get_export

    @allure.step("快速收货页面，点击关闭Inbound Receipt菜单")
    def click_close_inbound_receipt(self):
        self.is_click(user['关闭二代收货菜单'])

    @allure.step("快速收货页面，点击关闭IMEI Detail窗口")
    def click_close_inbound_imei_detail(self):
        self.is_click(user['关闭二代收货IMEI Detail'])

    @allure.step("断言 列表取分页总数判断是否有数据")
    def assert_total(self, total):
        if int(total) > 0:
            logging.info("Inbound Receipt列表，分页总条数为{}".format(total))
        else:
            logging.info("Inbound Receipt列表，分页总条数为{}".format(total))

    # 扫码收货
    @allure.step("点击Stock in by Scan 扫码收货按钮")
    def click_scan_imei_receipt(self):
        self.is_click(user['Stock in by Scan'])
        sleep(2)

    @allure.step("输入扫码的IMEI")
    def input_scan_imei(self, imei):
        self.is_click(user['Scan IMEI'])
        self.input_text(user['Scan IMEI'], imei)

    @allure.step("点击Check检查按钮")
    def click_check(self):
        self.is_click(user['Check'])
        sleep(1.5)

    @allure.step("点击Submit提交按钮")
    def click_submit(self):
        self.is_click(user['Submit'])

    @allure.step("创建Inbound Order页面，点击check后，获取Scanned属性下显示出库数量")
    def get_scanned(self):
        get_scanned = self.element_text(user['Get Scanned'])
        return get_scanned

    @allure.step("创建Inbound Order页面，点击check后，获取Scan Record扫码记录下侧显示Success")
    def get_inbound_scan_record_success(self):
        self.presence_sleep_dcr(user['Get Deli Scan Record Success'])
        scan_record_success = self.element_text(user['Get Deli Scan Record Success'])
        return scan_record_success

    @allure.step("创建Inbound Order页面，点击check后，获取Scan Record扫码记录下侧出现显示IMEI")
    def get_inbound_scan_record_imei(self, imei):
        self.presence_sleep_dcr(user['Get Deli Scan Record IMEI'], imei)
        scan_record_imei = self.element_text(user['Get Deli Scan Record IMEI'], imei)
        return scan_record_imei

    @allure.step("创建Inbound Order页面，点击check后，获取Order Detail列表下显示Scanned字段")
    def get_order_detail_scanned(self):
        order_detail_scanned = self.element_text(user['Get Order Detail Scanned'])
        return order_detail_scanned

    @allure.step("Inbound Receipt页面，获取列表Status字段内容")
    def get_list_status(self):
        self.presence_sleep_dcr(user['Get list Status'])
        get_status = self.element_text(user['Get list Status'])
        return get_status

    @allure.step("查询最近新建的销售单ID与出库单ID,进行快速收货")
    def inbound_quick_received(self, order_code, delivery_code):
        self.input_salesOrder(order_code)
        self.input_deliveryOrder(delivery_code)
        self.click_search()
        self.select_checkbox()
        self.click_quick_received()

    def input_text(self, locator, txt, *choice):
        """输入文本"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        ele.clear()
        ele.send_keys(txt)
        logging.info("输入文本：{}".format(txt))

    @allure.step("查找菜单")
    def click_menu(self, *content):
        self.refresh()
        self.is_click_tbm(user['菜单栏'])
        self.refresh()
        for i in range(len(content)):
            self.is_click_tbm(user['菜单'], content[i])
            logging.info('点击菜单：{}'.format(content[i]))
        self.refresh()
        self.element_exist(user['Loading'])

    @allure.step("点击Unfold 展开筛选项")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        logging.info('点击Unfold 展开筛选项')

    @allure.step("user management页面，输入查询条件")
    def input_search(self, header, content):
        """
        @header： 输入框名称
        @content： 输入内容
        """
        textarea_list = ['IMEI', 'Box']
        input_list = ['Sales Order ID', 'Delivery Order ID']
        country_list = ['Buyer Region', 'Seller Region']
        Date_list = ['Delivery Date']
        fuzzySelect_list = ['Buyer', 'Seller']
        exactSelect_list = ['Status', 'Return or not']
        inputSelect_list = ['Brand', 'Buyer Category', 'Model', 'Market Name', 'Buyer Country', 'Seller Country']
        inputSelect_list2 = []
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in textarea_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框3'], content, header)
            elif header in input_list:
                self.input_text(user['输入框'], content, header)
            elif header in exactSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in fuzzySelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框2'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
            elif header in country_list:
                country = content.split('_')
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], country[2], header)
                self.is_click_tbm(user['地区选择框'], country[0], country[1], country[2])
            elif header in inputSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框4'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
                self.is_click_tbm(user['输入框名称'], header)
            elif header in inputSelect_list2:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
            elif header in Date_list:
                createDate = content.split('To')
                for i in range(len(createDate)):
                    self.input_text(user['时间输入框'], createDate[i], header, i + 1)
                    self.is_click_tbm(user['输入框名称'], header)
            else:
                logging.error('请输入正确的查询条件')
                raise ValueError('请输入正确的查询条件')

    @allure.step("点击搜索功能")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("判断空值")
    def assert_None(self, result):
        try:
            assert result == '', logging.warning("断言失败: 该值不为None | x:{}".format(result))
            logging.info("断言成功: 该值为None | x:{}".format(result))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("断言：页面查询结果")
    def assert_Query_result(self, header, content):
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['menu表格字段'], user['表格内容'], header, content,
                                                             sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
        if content != '':
            id_list = ['Buyer', 'Seller']
            Date_list = ['Delivery Date']
            Region_list = ['Buyer Region', 'Seller Region']
            if header in id_list:
                self.assert_Query_result(f'{header} ID', content)
            elif header in Region_list:
                country = content.split('_')
                for i in range(3):
                    assert_result = False
                    column = self.get_table_info(user['menu表格字段'], f'{header} {3 - i}', sc_element=user['滚动条'],
                                                 h_element=user['表头文本'])
                    contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
                    for j in contents:
                        if ''.join(j.split()) != '':
                            ValueAssert.value_assert_equal(j, country[2])
                            assert_result = True
                        else:
                            logging.info(f'{header} {3 - i} 区域为空，继续比对上级区域')
                            break
                    if assert_result:
                        logging.info('断言结束')
                        break
            elif header in Date_list:
                if header == 'Activated Date':
                    column = self.get_table_info(user['menu表格字段'], 'Activation Date', sc_element=user['滚动条'],
                                                 h_element=user['表头文本'])
                else:
                    column = self.get_table_info(user['menu表格字段'], header, sc_element=user['滚动条'],
                                                 h_element=user['表头文本'])
                contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
                createDate = content.split('To')
                for i in contents:
                    # timeArray = time.strptime(i, "%Y-%m-%d %H:%M:%S")
                    # a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.mktime(timeArray) + 28800))
                    logging.info(f'实际时间：{i}')
                    # logging.info(f'修正时区后时间：{a}')
                    try:
                        assert createDate[0] <= i <= createDate[1] + ' 23:59:59'
                        logging.info(f'断言成功：创建时间：{i} 在筛选时间 {content} 区间')
                    except:
                        logging.info(f'断言失败：创建时间：{i} 与筛选时间 {content} 不符')
                        raise
            elif header == 'Return or not':
                column = self.get_table_info(user['menu表格字段'], 'Return Quantity', sc_element=user['滚动条'],
                                             h_element=user['表头文本'])
                ac_content = self.find_elements(user['表格退货标签'], column)
                class_value = 'danger'
                if content == 'Yes':
                    for i in ac_content:
                        ValueAssert.value_assert_Notequal(i.text, '0')
                        style = i.get_attribute('class')
                        ValueAssert.value_assert_equal(style, class_value)
                else:
                    for i in ac_content:
                        ValueAssert.value_assert_equal(i.text, '0')
                        style = i.get_attribute('class')
                        ValueAssert.value_assert_IsNone(style)
            else:
                self.assert_Query_result(header, content)


    @allure.step("组合查询 组合方法")
    def random_Query_Method(self, kwargs):
        self.input_search('Delivery Date', '2023-01-01To2023-02-28')
        list_query = []
        num = random.randint(3, 8)
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        list_random = random_list(list_query, num)
        logging.info(f'随机组合：输入框：{list_random}')
        for i in list_random:
            logging.info(f'随机组合：{i} 输入框输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_random:
            self.assert_search_result(i, kwargs[i])

    @allure.step("点击click to check!")
    def click_check(self):
        self.is_click_tbm(user['ClickToCheck'])
        logging.info('点击click to check!')

    @allure.step("断言：点击click to check后显示未收货订单，提示数量与搜索结果数量一致")
    def assert_check_num(self):
        logging.info('开始断言：点击click to check后显示未收货订单，提示数量与搜索结果数量一致')
        TipNum = self.element_text(user['TipNum'])
        logging.info(f'提示数量：{TipNum}')
        Total = self.element_text(user['Get Total Text'])
        TotalNum = Total[Total.index(' ') + 1:]
        logging.info(f'页面查询数量：{TotalNum}')
        ValueAssert.value_assert_equal(TipNum, TotalNum)

    @allure.step("点击功能按钮")
    def click_function_button(self, function):
        """
        @:param function: 需要点击的功能按钮，具体如下：
        Export, Quick Received, Stock-in by Scan, IMEI Detail
        """
        logging.info(f'点击功能按钮： {function}')
        self.is_click(user['功能按钮'], function)
        if function == 'IMEI Detail':
            self.element_exist(user['弹窗Loading'])

    @allure.step("断言：点击导出有进度条")
    def assert_export_success(self):
        DomAssert(self.driver).assert_control(user['导出进度条'])
        logging.info('开始断言：点击导出存在进度条')


if __name__ == '__main__':
    pass
