import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from public.base.assert_ui import DomAssert
import logging
from ..test_case.conftest import *
from datetime import datetime

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class WOSerializedReport(Base):
    """序列化工单报表"""
    given_data = datetime.today().date()
    logging.info('今天的日期: {} '.format(given_data))
    first_day_of_month = given_data.replace(day=1)
    logging.info('本月的第一天是:{}'.format(first_day_of_month))

    @allure.step("序列化工单报表页面查询")
    def Search_WoserlistReport(self, scope):
        self.refresh()
        sleep(1)
        self.is_click(user['WO Serialized Date开始日期搜索框'])
        self.hover(user['WO Serialized Date开始日期搜索框'])
        self.is_click(user['清除时间搜索框'])
        if scope == all:
            # 查询序列化工单报表所有数据
            self.is_click(user['WO Serialized Report Search'])
            sleep(2)
        else:
            # 查询序列化工单报表当月IN国家的数据
            self.is_click(user['WO Serialized Date开始日期搜索框'])
            self.input_text(user['WO Serialized Date开始日期搜索框'], txt=str(WOSerializedReport.first_day_of_month))
            sleep(2)
            self.is_click(user["Country搜索框"])
            self.input_text(user["Country搜索框"], txt='IN')
            self.hover(user['Country下拉选择'], choice='IN')
            self.is_click(user["Country下拉选择"])
            self.is_click(user['WO Serialized Report Search'])
            # self.wait.until(EC.presence_of_element_located(user['序列化工单查询页表格country字段']), message='数据未加载完成')

    @allure.step("数据库查询序列化工单报表数量")
    def search_stock(self, stock):
        sql = SQL('CRM', 'test')
        if stock == all:
            # 查询序列化工单所有数据
            record = sql.query_db('SELECT count(*) FROM crm_rc_serialize_work_order swo LEFT JOIN crm_rc_serialize_repair_process srp ON swo.id = srp.work_order_id AND srp.is_deleted = 0 LEFT JOIN crm_rc_serialize_repair_process_detail srpd ON srp.id = srpd.repair_process_id AND srpd.is_deleted = 0 WHERE swo.is_deleted = 0 ')
            logging.info("数据库查询了第一条语句")
        else:
            # 根据国家和时间过滤查询序列化工单数据
            record = sql.query_db("SELECT count(*) FROM crm_rc_serialize_work_order swo LEFT JOIN crm_rc_serialize_repair_process srp ON swo.id = srp.work_order_id AND srp.is_deleted = 0 LEFT JOIN crm_rc_serialize_repair_process_detail srpd ON srp.id = srpd.repair_process_id AND srpd.is_deleted = 0 WHERE swo.is_deleted = 0 and swo.creation_time>='{}' and swo.warehouse_country_code='IN'".format(WOSerializedReport.first_day_of_month))
            logging.info("数据库查询了第二条语句")
        dict_record = record[0]
        print(dict_record)
        record_value = dict_record['count(*)']
        logging.info('数据库查询到的序列化工单报表数据为:{}'.format(record_value))
        search_num = self.get_element_attribute(user['报表总数'], 'textContent')
        num = ''.join(filter(str.isdigit, search_num))
        num = int(num)
        logging.info('序列化工单报表查询页查到的数量:{}'.format(num))

        return record_value, num




    @allure.step("序列化工单报表导出")
    def download_report(self, scope):
        self.refresh()
        sleep(1)
        self.is_click(user['WO Serialized Date开始日期搜索框'])
        self.hover(user['WO Serialized Date开始日期搜索框'])
        self.is_click(user['清除时间搜索框'])
        if scope == all:
            self.is_click(user['WO Serialized Report Search'])
        else:
            self.is_click(user["Country搜索框"])
            self.input_text(user["Country搜索框"], txt='IN')
            sleep(1)
            self.hover(user['Country下拉选择'], choice='IN')
            self.is_click(user["Country下拉选择"])
            self.is_click(user['WO Serialized Report Search'])

        self.is_click(user['WO Serialized Report Export'], 'Export')
        self.is_click(user['确认导出'], 'OK')
        self.find_element(user['页签关闭'], 'WO Serialized Report').click()



    @allure.step("任务列表文件下载")
    def download_task(self):
        self.is_click(user["导出列表页隐藏任务勾选框"])
        self.is_click(user['任务列表页查询按钮'])
        # sleep(15)
        # self.is_click(user['任务列表页查询按钮'])




if __name__ == '__main__':
    pass
