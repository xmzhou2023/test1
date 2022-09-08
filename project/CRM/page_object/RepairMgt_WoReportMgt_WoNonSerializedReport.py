import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
from datetime import datetime

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class WONonSerializedReport(Base):
    """非序列化工单报表"""
    given_data = datetime.today().date()
    logging.info('今天的日期: {} '.format(given_data))
    first_day_of_month = given_data.replace(day=1)
    logging.info('本月的第一天是:{}'.format(first_day_of_month))

    @allure.step("非序列化工单报表查询")
    def search_NonwoserlistReport(self, scope):
        self.refresh()
        sleep(1)
        self.is_click(user['WO Non Serialized Date开始日期搜索框'])
        self.hover(user['WO Non Serialized Date开始日期搜索框'])
        self.is_click(user['清除时间搜索框'])
        if scope == all:
            # 查询非序列化工单报表所有数据
            self.is_click(user['WO NonSerialized Report Search'])
        else:
            # 查询非序列化工单报表当月SL国家的数据
            self.is_click(user['WO Non Serialized Date开始日期搜索框'])
            self.input_text(user['WO Non Serialized Date开始日期搜索框'], txt=str(WONonSerializedReport.first_day_of_month))
            self.is_click(user["Country搜索框"])
            self.input_text(user["Country搜索框"], txt='SL')
            sleep(1)
            self.hover(user['Country下拉选择'], choice='SL')
            self.is_click(user["Country下拉选择"])
            self.is_click(user['WO NonSerialized Report Search'])

    @allure.step("菜单刷新")
    def refresh_page(self):
        self.is_click(user['Dashboard'])
        self.refresh()
        self.wait.until(EC.presence_of_element_located(user['Dashboard']), message="页面刷新失败")

    @allure.step("查询非序列化工单报表数量")
    def search_stock(self, stock):
        sql = SQL('CRM', 'test')
        if stock == all:  # 查询非序列化工单所有数据
            record = sql.query_db('SELECT count(*) FROM crm_rc_deserialize_work_order dwo LEFT JOIN crm_rc_deserialize_repair_result drr ON dwo.id = drr.work_order_id AND drr.is_deleted = 0 LEFT JOIN crm_rc_deserialize_repair_result_detail drrd ON drr.id = drrd.result_id AND drrd.is_deleted = 0 WHERE dwo.is_deleted = 0')

        else:  # 有条件的查询非序列化工单数据
            record = sql.query_db("SELECT count(*) FROM crm_rc_deserialize_work_order dwo LEFT JOIN crm_rc_deserialize_repair_result drr ON dwo.id = drr.work_order_id AND drr.is_deleted = 0 LEFT JOIN crm_rc_deserialize_repair_result_detail drrd ON drr.id = drrd.result_id AND drrd.is_deleted = 0 WHERE dwo.is_deleted = 0 and dwo.creation_time>='{}' and dwo.warehouse_country_code='SL'".format(WONonSerializedReport.first_day_of_month))

        dict_record = record[0]
        print(dict_record)
        record_value = dict_record['count(*)']
        logging.info('数据库查询到的非序列化工单报表数据为:{}'.format(record_value))
        search_num = self.get_element_attribute(user['报表总数'], 'textContent')
        num = ''.join(filter(str.isdigit, search_num))
        num = int(num)
        logging.info('非序列化工单报表查询页查到的数量:{}'.format(num))

        return record_value, num




    @allure.step("报表导出")
    def download_report(self, scope):
        self.refresh()
        sleep(1)
        self.is_click(user['WO Non Serialized Date开始日期搜索框'])
        self.hover(user['WO Non Serialized Date开始日期搜索框'])
        self.is_click(user['清除时间搜索框'])
        if scope == all:

            self.is_click(user['WO NonSerialized Report Search'])
            self.is_click(user['WO NonSerialized Report Export'], 'Export')
            self.is_click(user['确认导出'], 'OK')
        # logging.info("输入框键入{}".format(content))
            self.refresh()
        else:
            self.is_click(user["Country搜索框"])
            self.input_text(user["Country搜索框"], txt='SL')
            sleep(1)
            self.hover(user['Country下拉选择'], choice='SL')
            self.is_click(user["Country下拉选择"])
            self.is_click(user['WO NonSerialized Report Search'])
            self.is_click(user['WO NonSerialized Report Export'], 'Export')
            self.is_click(user['确认导出'], 'OK')
            self.refresh()
if __name__ == '__main__':
    pass
