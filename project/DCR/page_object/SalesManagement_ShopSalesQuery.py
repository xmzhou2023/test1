import logging
from datetime import datetime

from openpyxl import load_workbook

from libs.common.read_element import Element
from libs.common.time_ui import sleep
from libs.config.conf import BASE_DIR
from public.base.basics import Base
from pykeyboard import PyKeyboard
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopSaleQueryPage(Base):
    """ShopSalesQueryPage，生产环境，Shop Sales Query页面元素定位"""

    @allure.step("Shop Sales Query页面，根据Shop ID条件筛选 门店销售数据")
    def input_query_shop_id(self, content):
        self.is_click_dcr(user['筛选门店'])
        self.input_text_dcr(user['筛选门店'], txt=content)
        sleep(3)
        self.is_click(user['Select Shop Value'])

    @allure.step("点击Unfold展开筛选项按钮")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("点击fold收起筛选项按钮")
    def click_fold(self):
        self.is_click(user['Fold'])
        sleep(1)

    @allure.step("输入Upload Date筛选项的开始时间")
    def input_upload_start_date(self, content):
        self.is_click(user['Input Upload Start Date'])
        self.input_text(user['Input Upload Start Date'], txt=content)

    @allure.step("输入销售日期开始时间与结束时间Sales Date Start Date")
    def input_sales_date(self, content1, content2):
        self.is_click(user['Sales Date Start Date'])
        self.input_text(user['Sales Date Start Date'], txt=content1)
        self.is_click(user['Sales Date End Date'])
        self.input_text(user['Sales Date End Date'], txt=content2)

    @allure.step("Shop Sales Query页面，筛选Shop ID后，点击Search按钮")
    def click_search(self):
        self.is_click_dcr(user['Search'])
        sleep(5)

    @allure.step("Shop Sales Query页面，筛选Shop ID后，点击Search按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(5)

    @allure.step("Shop Sales Query页面，获取列表Shop ID 文本内容")
    def get_shop_id_text(self):
        self.presence_sleep_dcr(user['获取门店ID文本'])
        shop_id = self.element_text(user['获取门店ID文本'])
        return shop_id

    @allure.step("Shop Sales Query页面，获取列表Shop ID 文本内容")
    def get_shop_name_text(self):
        shop_name = self.element_text(user['获取门店名称文本'])
        return shop_name

    @allure.step("Shop Sales Query页面，获取列表Status文本内容")
    def get_status_text(self):
        status = self.element_text(user['获取状态文本'])
        return status

    @allure.step("Shop Sales Query页面，获取列表sales date销售日期文本")
    def get_sales_date_text(self):
        sales_date = self.element_text(user['获取销售日期文本'])
        return sales_date

    @allure.step("Shop Sales Query页面，获取列表获取Public ID文本内容")
    def get_public_id_text(self):
        public_id = self.element_text(user['获取Public ID文本'])
        return public_id

    @allure.step("Shop Sales Query页面，获取列表获取总条数文本")
    def get_total_text(self):
        self.presence_sleep_dcr(user['获取总条数文本'])
        total = self.element_text(user['获取总条数文本'])
        total1 = total[6:]
        return total1

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])
        #sleep(1)

    @allure.step("关闭门店销售查询菜单")
    def click_close_shop_sales_query(self):
        self.is_click(user['关闭门店销售查询菜单'])
        #sleep(1)

    @allure.step("点击Upload Date结束时间日期框")
    def click_upload_end_date(self):
        self.is_click(user['Click Upload End Date'])



    #门店销售查询，导出功能验证
    @allure.step("Shop Sales Query页面，点击Export 导出门店销量查询数据")
    def click_export(self):
        self.is_click(user['Export'])
        sleep(2)

    @allure.step("点击异步导出，点击更多按钮")
    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        sleep(3)

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(0.5)
        self.is_click_dcr(user['Task Name value'], content)

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

    @allure.step("")
    def get_export_time_text(self):
        """导出记录页面，获取列表导出时间文本"""
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 0:
            logging.info("Shop Sales Query列表，按Shop ID筛选，加载筛选后的数据正常，分页总条数Total：{}".format(total))
        else:
            logging.info("查看Shop Sales Query列表，未加载筛选后的数据失败，分页总条数Total：{}".format(total))

    @allure.step("断言分页总数是否存在数据")
    def assert_total2(self, total):
        if int(total) > 100:
            logging.info("查看Shop Sales Query列表，加载所有数据正常，分页总条数Total：{}".format(total))
        else:
            logging.info("查看Shop Sales Query列表，加载所有数据正常，分页总条数Total：{}".format(total))

    @allure.step("断言文件或导出时间是否有数据 ")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("Shop Sales Query导出成功，File Size 导出文件大于0KB:{}".format(file_size))
        else:
            logging.info("Shop Sales Query导出成功，File Size 导出文件小于0KB:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Shop Sales Query导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Shop Sales Query导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))
        sleep(1)

    @allure.step("点击Import按钮")
    def click_import(self):
        self.is_click(user['Import'])
        logging.info('点击Import按钮')
        self.click_upload()

    @allure.step("点击Export按钮")
    def click_export(self):
        self.is_click(user['Export'])
        logging.info('点击Export按钮')

    @allure.step("点击Upload按钮")
    def click_upload(self):
        self.is_click(user['Upload'])
        logging.info('点击upload按钮')
        sleep(2)
        k = PyKeyboard()
        k.tap_key(k.escape_key)

    @allure.step("导入文件")
    def import_file(self, name):
        file_path = os.path.join(BASE_DIR, 'project', 'DCR', 'data', name)
        logging.info("文件地址：{}".format(file_path))
        self.upload_file(user['导入'], file_path)

    @allure.step("导入门店销量文件")
    def import_ShopSalesQuery_file(self, name):
        file_path = os.path.join(BASE_DIR, 'project', 'DCR', 'data', name)
        logging.info("文件地址：{}".format(file_path))
        today = datetime.now().strftime('%Y-%m-%d')
        workbook = load_workbook(filename=file_path)
        sheet = workbook.active
        cells = sheet['A']
        for cell in cells[1:]:
            cell.value = today
        workbook.save(filename=file_path)
        self.upload_file(user['导入'], file_path)

    @allure.step("点击Save按钮")
    def click_save(self):
        self.is_click(user['Save'])
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

    @allure.step("获得ImportRecord指定内容")
    def get_Record_info(self, menu, name, header):
        """
        :param menu: 输入文件名
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        """
        for i in range(20):
            ac_menu = self.element_text(user['当前菜单'])
            if ac_menu == menu:
                column = self.get_table_info(user['表格字段'], header, h_element=user['表头文本'])
                content = self.element_text(user['表格指定列内容'], name, column)
                return content

    @allure.step("断言：ImportRecord导入结果")
    def assert_ImportRecord_result(self, name, header, result):
        """
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        :param result: 需要断言的值 比如状态，数量，时间
        """
        ac_result = self.get_Record_info('Import Record', name, header)
        ValueAssert.value_assert_In(result, ac_result)

    @allure.step("断言：ImportRecord导入结果")
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

    @allure.step("ShopSalesQuery页面，输入查询条件")
    def input_ShopSalesQuery_query(self, header, content):
        """
        :param header: 字段名
        :param content: 内容
        """
        click_list = ['Status']
        imei_list = ['IMEI/SN', 'IMEI']
        select_list = ['Shop']
        if header in click_list:
            self.input_text(user['输入框'], header, content)
            self.is_click_tbm(user['输入框结果'], content)
        elif header in imei_list:
            self.is_click_tbm(user['输入框'], header)
            self.input_text(user['输入框2'], content, header)
        elif header in select_list:
            self.is_click_tbm(user['输入框'])
            self.input_text(user['输入框3'], content, header)
            self.is_click_tbm(user['输入框结果'], content)
        logging.info('查询{}：{}'.format(header, content))

    @allure.step("ShopSalesQuery页面，输入查询条件")
    def input_ShopPurchaseQuery_query(self, header, content):
        """
        :param header: 字段名
        :param content: 内容
        """
        click_list = ['Status']
        imei_list = ['IMEI/SN', 'IMEI']
        select_list = ['Shop']
        if header in click_list:
            self.is_click_tbm(user['ShopPurchaseQuery输入框'], header)
            self.is_click_tbm(user['输入框结果'], content)
        elif header in imei_list:
            self.is_click_tbm(user['ShopPurchaseQuery输入框'], header)
            self.input_text(user['ShopPurchaseQuery输入框2'], content, header)
        elif header in select_list:
            self.is_click_tbm(user['输入框'], header)
            self.input_text(user['输入框3'], content, header)
            self.is_click_tbm(user['输入框结果'], content)
        logging.info('查询{}：{}'.format(header, content))

    @allure.step("断言：ShopSalesQuery导入结果")
    def assert_Query_result(self, header, content):
        """
        :param header: 需要获取的指定字段
        :param content: 需要断言的值
        """
        DomAssert(self.driver).assert_search_result(user['menu表格字段'], user['ShopSalesQuery表格内容'], header, content, sc_element=user['ShopSalesQuery滚动条'], index='1', h_element=user['表头文本'])

    @allure.step("点击复选框")
    def click_checkbox(self, content):
        """
        :param content: 指定值，如imei
        """
        rowid = self.get_table_info(user['指定行'], content, attr='rowid', sc_element=user['ShopSalesQuery滚动条'])
        self.is_click_tbm(user['指定复选框'], rowid)

    @allure.step("点击删除")
    def click_delete(self):
        self.is_click_tbm(user['Delete'])
        self.is_click_tbm(user['Confirm'])

    @allure.step("点击删除")
    def click_cancel(self):
        self.is_click_tbm(user['Cancel'])
        self.is_click_tbm(user['Confirm'])

    @allure.step("重置")
    def reset_ShopSalesQuery_import(self, imei):
        """Shop Sales Query页面点击指定imei复选框，删除"""
        self.input_ShopSalesQuery_query('IMEI/SN', imei)
        self.click_search()
        total_text = self.element_text(user['Total'])
        total = total_text[total_text.index(' ')+1:]
        logging.info(total_text)
        if total != '0':
            self.click_checkbox(imei)
            self.click_delete()
            DomAssert(self.driver).assert_att('Deleted Successfully')
            sleep(3)

    @allure.step("重置")
    def reset_ShopPurchaseQuery_import(self, imei):
        """Shop Sales Query页面点击指定imei复选框，删除"""
        self.click_unfold()
        self.input_ShopPurchaseQuery_query('IMEI', imei)
        self.input_ShopPurchaseQuery_query('Status', 'Committed')
        self.click_search()
        total_text = self.element_text(user['Total'])
        total = total_text[total_text.index(' ')+1:]
        logging.info(total_text)
        if total != '0':
            self.click_checkbox(imei)
            self.click_cancel()
            DomAssert(self.driver).assert_att('Cancel success')
            sleep(3)

    @allure.step("查找菜单")
    def click_menu(self, *content):
        self.is_click_tbm(user['菜单栏'])
        self.refresh()
        for i in range(len(content)):
            self.is_click_tbm(user['菜单'], content[i])
            logging.info('点击菜单：{}'.format(content[i]))
        self.refresh()
if __name__ == '__main__':
    pass
