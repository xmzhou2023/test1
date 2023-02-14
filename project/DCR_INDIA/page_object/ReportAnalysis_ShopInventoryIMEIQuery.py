from libs.common.read_element import Element
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class ShopInventoryIMEIQueryPage(Base):
    """ShopInventoryIMEIQueryPage，生产环境，Shop Inventory IMEI Query 页面元素定位"""
    def click_unfold(self):
        """Shop Inventory IMEI Query页面，点击Unfold展开筛选条件"""
        self.is_click(user['Unfold'])
        sleep(2)

    def input_shop_id(self, content):
        """Shop Inventory IMEI Query页面，输入shop ID，进行筛选"""
        self.is_click_dcr(user['筛选门店'])
        sleep(1)
        self.input_text_dcr(user['筛选门店'], txt=content)
        sleep(3)
        self.is_click_dcr(user['选中筛选门店值'])

    def input_inbound_date(self, content):
        """Shop Inventory IMEI Query页面，输入筛选开始日期"""
        Base.presence_sleep_dcr(self, user['Inbound Date Start Time'])
        self.is_click(user['Inbound Date Start Time'])
        sleep(1)
        self.input_text(user['Inbound Date Start Time'], txt=content)
        sleep(1)

    def click_search(self):
        """Shop Inventory IMEI Query页面，点击Search按钮"""
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    def click_reset(self):
        """Shop Inventory IMEI Query页面，点击Search按钮"""
        self.is_click(user['Reset'])
        self.element_exist(user['Loading'])

    def click_fold(self):
        """Shop Inventory IMEI Query页面，点击Fold收起筛选条件按钮"""
        self.is_click(user['Fold'])
        sleep(1)

    def get_total_text(self):
        """Shop Inventory IMEI Query页面，获取分页功能总条数文本"""
        Base.presence_sleep_dcr(self, user['获取总条数文本'])
        total = self.element_text(user['获取总条数文本'])
        total1 = total[6:]
        return total1

    def get_shop_id_text(self):
        """Shop Inventory IMEI Query页面，获取列表Shop ID文本"""
        Base.presence_sleep_dcr(self, user['获取Shop ID文本'])
        shop_id = self.element_text(user['获取Shop ID文本'])
        return shop_id

    def get_shop_name_text(self):
        shop_name = self.element_text(user['获取Shop Name文本'])
        return shop_name

    def get_brand_text(self):
        brand = self.element_text(user['获取Brand文本'])
        return brand

    def get_series_text(self):
        series = self.element_text(user['获取Series文本'])
        return series

    def get_model_text(self):
        model = self.element_text(user['获取Model文本'])
        return model


    # 门店库存IMEI查询记录，导出功能验证
    def click_export(self):
        """Visit Record页面，点击Export导出按钮"""
        self.is_click(user['Export'])
        sleep(2)

    def click_download_more(self):
        """点击下载-更多按钮"""
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        self.element_exist(user['Loading'])

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], content)
        sleep(1)
        self.is_click_dcr(user['Task Name value'], content)

    @allure.step("输入Create Date开始日期筛选当天日期的导出记录")
    def export_record_create_date_query(self, start_date):
        self.is_click(user['导出记录筛选创建日期'])
        self.input_text(user['导出记录筛选创建日期'], start_date)
        self.is_click(user['点击筛选标签'], 'Create Date')

    def click_export_search(self):
        """循环点击查询，直到获取到下载状态为COMPLETE """
        down_status = Base.export_download_status(self, user['Export Record Search'], user['获取下载状态文本'])
        return down_status

    def get_download_status_text(self):
        """导出记录页面，获取列表 Download Status文本"""
        status = self.find_element(user['获取下载状态文本'])
        while status != "COMPLETE":
            status1 = self.element_text(user['获取下载状态文本'])
            return status1

    def get_task_name_text(self):
        """导出记录页面，获取列表 Task Name文本"""
        Base.presence_sleep_dcr(self, user['获取任务名称文本'])
        task_name = self.element_text(user['获取任务名称文本'])
        return task_name

    def get_file_size_text(self):
        """导出记录页面，获取列表 Task Name文本"""
        file_size = self.element_text(user['获取文件大小文本'])
        file_size1 = file_size[0:1]
        return file_size1

    def get_task_user_id_text(self):
        """导出记录页面，获取列表 User ID文本"""
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    def get_create_date_text(self):
        """导出记录页面，获取列表 Create Date文本"""
        create_date = self.element_text(user['获取创建日期文本'])
        create_date1 = create_date[0:10]
        return create_date1

    def get_complete_date_text(self):
        """导出记录页面，获取列表Complete Date文本"""
        complete_date = self.element_text(user['获取完成日期文本'])
        complete_date1 = complete_date[0:10]
        return complete_date1

    def get_export_operation_text(self):
        """导出记录页面，获取列表 Operation文本"""
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    def get_export_time_text(self):
        """导出记录页面，获取列表导出时间文本"""
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1


    def assert_total(self, total):
        """断言分页总数是否存在数据"""
        if int(total) > 1000:
            logging.info("查看Shop Inventory IMEI Query列表，加载所有数据正常，分页总条数Total：{}".format(total))
        else:
            logging.info("查看Shop Inventory IMEI Query列表，加载所有数据正常，分页总条数Total：{}".format(total))

    def assert_file_time_size(self, file_size, export_time):
        """断言文件或导出时间是否有数据 """
        if int(file_size) > 0:
            logging.info("Shop Inventory IMEI Query导出成功，File Size 导出文件大于1KB:{}".format(file_size))
        else:
            logging.info("Shop Inventory IMEI Query导出失败，File Size 导出文件小于1KB:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Shop Inventory IMEI Query导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Shop Inventory IMEI Query导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))

    @allure.step("查找菜单")
    def click_menu(self, *content):
        self.refresh()
        self.is_click_tbm(user['菜单栏'])
        self.refresh()
        for i in range(len(content)):
            self.is_click_tbm(user[f'菜单{i + 1}'], content[i])
            logging.info('点击菜单：{}'.format(content[i]))
        self.refresh()
        self.element_exist(user['Loading'])

    def input_text(self, locator, txt, *choice):
        """输入文本"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        ele.clear()
        ele.send_keys(txt)
        logging.info("输入文本：{}".format(txt))

    @allure.step("输入查询条件")
    def input_search(self, header, content):
        exactSelect_list = ['Activation Status']
        Date_list = ['Activated Date', 'Inbound Date']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in exactSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in Date_list:
                createDate = content.split('To')
                for i in range(len(createDate)):
                    self.input_text(user['时间输入框'], createDate[i], header, i+1)
                    self.is_click_tbm(user['输入框名称'], header)
            else:
                logging.error(f'无效字段：{header}，请输入正确的查询条件')
                raise ValueError(f'无效字段：{header}，请输入正确的查询条件')

    @allure.step("断言：查询结果为空")
    def assert_NoData(self):
        logging.info('开始断言：查询结果为空')
        total_text = self.element_text(user['Total'])
        total = total_text[total_text.index(' ') + 1:]
        logging.info(total_text)
        ValueAssert.value_assert_equal(total, '0')


if __name__ == '__main__':
    pass