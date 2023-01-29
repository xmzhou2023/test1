import logging
from datetime import datetime

from openpyxl import load_workbook

from libs.common.read_element import Element
from libs.common.time_ui import sleep
from libs.config.conf import BASE_DIR
from public.base.basics import Base
# from pykeyboard import PyKeyboard
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
        self.is_click(user['Select Shop Value'],content)

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
        self.input_text(user['Input Upload Start Date'], content)
        self.is_click(user['点击筛选项label'], 'Upload Date')

    @allure.step("输入销售日期开始时间与结束时间Sales Date Start Date")
    def input_sales_date(self, content1, content2):
        self.is_click(user['Sales Date Start Date'])
        self.input_text(user['Sales Date Start Date'], content1)
        self.is_click(user['Sales Date End Date'])
        self.input_text(user['Sales Date End Date'], content2)
        self.is_click(user['点击筛选项label'], 'Sales Date')

    @allure.step("Shop Sales Query页面，筛选Shop ID后，点击Search按钮")
    def click_search(self):
        self.is_click_dcr(user['Search'])
        self.element_text(user['Loading'])

    @allure.step("Shop Sales Query页面，筛选Shop ID后，点击Search按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        self.element_text(user['Loading'])

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
        self.element_text(user['Loading'])

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(0.5)
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
        # k = PyKeyboard()
        # k.tap_key(k.escape_key)

    @allure.step("导入文件")
    def import_file(self, name):
        """
        :param name： 传入存放在data文件夹里的文件名
        """
        file_path = os.path.join(BASE_DIR, 'project', 'DCR', 'data', name)
        logging.info("文件地址：{}".format(file_path))
        self.upload_file(user['导入'], file_path)
        logging.info("导入文件：{}".format(file_path))

    @allure.step("导入门店销量文件")
    def import_ShopSalesQuery_file(self, name):
        """
        :param name： 传入存放在data文件夹里的文件名
        """
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
        logging.info("导入门店销量文件：{}".format(file_path))

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
        logging.info("开始断言：导入成功状态")
        DomAssert(self.driver).assert_control(user['导入成功状态'])

    @allure.step("获得Record指定内容")
    def get_Record_info(self, menu, name, header):
        """
        :param menu: 输入菜单名
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

    @allure.step("断言：ImportRecord导入结果")
    def assert_ImportRecord_result(self, name, header, result):
        """
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        :param result: 需要断言的值 比如状态，数量，时间
        """
        logging.info('开始断言：ImportRecord导入结果')
        ac_result = self.get_Record_info('Import Record', name, header)
        ValueAssert.value_assert_In(result, ac_result)

    @allure.step("断言：Record导入结果")
    def assert_Record_result(self, menu, name, header, result=None):
        """
        :param menu: 菜单
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        :param result: 需要断言的值 比如状态，数量，时间
        """
        logging.info(f'开始断言：{menu} Record导入结果')
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
        logging.info('查询 {}：{}'.format(header, content))

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
        logging.info('查询 {}：{}'.format(header, content))

    @allure.step("断言：ShopSalesQuery导入结果")
    def assert_Query_result(self, header, content):
        """
        :param header: 需要获取的指定字段
        :param content: 需要断言的值
        """
        logging.info('开始断言：ShopSalesQuery导入结果')
        DomAssert(self.driver).assert_search_result(user['menu表格字段'], user['ShopSalesQuery表格内容'], header, content, sc_element=user['ShopSalesQuery滚动条'], index='1', h_element=user['表头文本'])

    @allure.step("点击复选框")
    def click_checkbox(self, content):
        """
        :param content: 指定值，如imei
        """
        rowid = self.get_table_info(user['指定行'], content, attr='rowid', sc_element=user['ShopSalesQuery滚动条'])
        self.is_click_tbm(user['指定复选框'], rowid)
        logging.info(f'点击 {content} 复选框')

    @allure.step("点击删除")
    def click_delete(self):
        self.is_click_tbm(user['Delete'])
        self.is_click_tbm(user['Confirm'])
        logging.info('点击删除')

    @allure.step("点击取消")
    def click_cancel(self):
        self.is_click_tbm(user['Cancel'])
        self.is_click_tbm(user['Confirm'])
        logging.info('点击取消')

    @allure.step("重置ShopSalesQuery导入数据")
    def reset_ShopSalesQuery_import(self, imei):
        """Shop Sales Query页面点击指定imei复选框，删除"""
        self.click_menu("Sales Management", "Shop Sales Query")
        logging.info('开始重置ShopSalesQuery导入数据')
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

    @allure.step("重置ShopPurchaseQuery导入数据")
    def reset_ShopPurchaseQuery_import(self, imei):
        """ShopPurchaseQuery页面点击指定imei复选框，删除"""
        logging.info('开始重置ShopPurchaseQuery导入数据')
        self.click_menu("Purchase Management", "Shop Purchase Query")
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

    @allure.step("输入Upload Date筛选项的开始和结束时间")
    def input_upload_date(self, startdate,enddata):
        self.is_click(user['Input Upload Start Date'])
        self.input_text(user['Input Upload Start Date'], txt=startdate)
        self.is_click(user['Click Upload End Date'])
        self.input_text(user['Click Upload End Date'], txt=enddata)


    @allure.step("点击IMEI/SN")
    def click_imei(self):
        self.is_click(user['选择IMEI/SN'])

    @allure.step("输入IMEI/SN选择")
    def input_imei(self,content):
        self.is_click(user['选择IMEI/SN'])
        self.input_text(user['输入IMEI/SN'],txt=content)

    @allure.step("输入model选择")
    def input_model(self,content):
        self.is_click(user['选择model'])
        self.input_text(user['输入model'],txt=content)
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'],content)

    @allure.step("输入model type选择")
    def input_model_type(self,content):
        self.is_click(user['modeltype'])
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'],content)

    @allure.step("选择Mid&High")
    def input_mid_high(self):
        self.is_click(user['选择model'])
        self.is_click(user['中高端选择Yes'])

    @allure.step("输入item选择")
    def input_item(self,content):
        self.is_click(user['门店销量项目'])
        self.input_text(user['门店销量项目输入'],txt=content)
        sleep(2)
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'],content)

    @allure.step("输入销售区域选择")
    def input_sales_region(self,content):
        self.is_click(user['门店销量区域'])
        self.input_text(user['门店销量区域'],txt=content)
        self.is_click(user['门店销量区域选择'],content)

    @allure.step("选择城市级别")
    def input_city_tier(self,content):
        self.is_click(user['门店销量城市级别'])
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'],content)

    @allure.step("选择brand")
    def input_brand(self,content):
        self.is_click(user['门店销量品牌'])
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'],content)

    @allure.step("输入市场名字选择")
    def input_market_name(self,content):
        self.is_click(user['门店销量市场名字'])
        self.input_text(user['门店销量市场名字输入'],txt=content)
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'],content)

    @allure.step("输入品牌系列选择")
    def input_series(self,content):
        self.is_click(user['品牌系列'])
        self.input_text(user['品牌系列输入'],txt=content)
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'],content)

    @allure.step("选择SP/FP")
    def input_sp_fp(self,content):
        self.is_click(user['SPFP'])
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'],content)

    @allure.step("输入上传人员ID选择")
    def input_uploaderid(self,content):
        self.is_click(user['上传人员ID'])
        self.input_text(user['上传人员输入'],txt=content)

    @allure.step("选择激活状态")
    def input_activation_status(self,content):
        self.is_click(user['激活状态'])
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'],content)

    @allure.step("输入职位选择")
    def input_position(self,content):
        self.is_click(user['职位'])
        self.input_text(user['职位输入'],txt=content)
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'],content)

    @allure.step("输入激活日期选择")
    def input_activattion_date(self,startdate,enddate):
        self.is_click(user['激活日期开始'])
        self.input_text(user['激活日期开始'],txt=startdate)
        self.input_text(user['激活日期结束'],txt=enddate)

    @allure.step("输入国家选择")
    def input_sale_country(self,content):
        self.is_click(user['店铺销量国家'])
        self.input_text(user['国家输入'],txt=content)
        self.is_click(user['国家选择'],content)

    @allure.step("选择是否有促销员")
    def input_manpower(self,content):
        self.is_click(user['是否有促销员'])
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'], content)

    @allure.step("选择门店形象等级")
    def input_image_type(self,content):
        self.is_click(user['门店形象等级'])
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'], content)

    @allure.step("选择门店形象等级")
    def input_time_zone(self):
        self.is_click(user['时区'])
        self.is_click(user['时区选择'])

    @allure.step("选择上传类型")
    def input_upload_type(self,content):
        self.is_click(user['上传类型'])
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'], content)

    @allure.step("选择是否达成")
    def input_achieve_ornot(self,content):
        self.is_click(user['是否达成'])
        self.is_click(user['城市级别_品牌_市场名_SP/FP_激活状态_职位_Manpower_形象等级_上传类型选择_销量状态_激活国家_发货国家'], content)

    @allure.step("选择销量状态")
    def input_status(self,content):
        self.is_click(user['销量状态'])
        self.is_click(user['提供人员选择'], content)

    @allure.step("输入激活国家选择")
    def input_activation_country(self,content):
        self.is_click(user['激活国家'])
        self.input_text(user['激活国家输入'],txt=content)
        self.is_click(user['激活国家_发货国家选择'], content)

    @allure.step("输入发货国家选择")
    def input_delivery_country(self,content):
        self.is_click(user['发货国家'])
        self.input_text(user['发货国家输入'],txt=content)
        self.is_click(user['激活国家_发货国家选择'], content)

    @allure.step("输入提供人员选择")
    def input_supplier(self,content):
        self.is_click(user['提供人员'])
        self.input_text(user['提供人员输入'],txt=content)
        self.is_click(user['提供人员选择'], content)

    @allure.step("获取第一行文本内容")
    def get_table_txt(self, num):
        txt = self.element_text(user['列表第一行'],num)
        return txt

    @allure.step("根据表头获取列值")
    def get_table_column(self, header):
        #self.DivRolling(user['表头字段'])
        attribute=self.get_table_info(user['表头列'],header,attr='colid',sc_element=user['sc_element'])
        logging.info('列元素的属性是%s'%attribute)
        #number=int(attribute[4:])
        return attribute

    @allure.step("获取表格文本")
    def get_table_content(self,attribute):
        txt = self.element_text(user['表格具体字段'],attribute)
        return txt
    @allure.step("断言：ShopSalesQuery查询结果")
    def assert_Query_result(self, header, content):
        """
        :param header: 需要获取的指定字段
        :param content: 需要断言的值
        """
        DomAssert(self.driver).assert_search_result(user['表格头部字段'], user['列表第一行'], header, content)


    @allure.step("断言精确查询结果 Shop Sales Query列表，字段列、字段内容是否与预期的字段内容值一致，有滚动条")
    def assert_shop_sales_query_field(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['指定列内容'], header, content,
                                                    sc_element=user['水平滚动条'])



if __name__ == '__main__':
    pass
