import string
from datetime import datetime

import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from .Center_Component import NavPage
from ..test_case.conftest import *
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class WOSerializedListAdd(Base):

    """序列化工单新增类"""
    @allure.step("新建序列化工单")
    def add_woserlist(self, Warehouse=None, imei=None):
        self.refresh()
        self.is_click(user['序列化工单查询页Add按钮'])
        self.is_click(user['序列化工单新增页Warehouse Name搜索框'])
        self.input_text(user['序列化工单新增页Warehouse Name搜索框'], txt=Warehouse)

        self.hover(user['序列化工单新增页Warehouse Name选择框'], choice=Warehouse)
        self.is_click(user['序列化工单新增页Warehouse Name选择框'])
        self.is_click(user['序列化工单新增页SN/IMEI No1输入框'])
        self.input_text(user['序列化工单新增页SN/IMEI No1输入框'], txt=imei)
        self.is_click(user['序列化工单新增页空白处'])
        self.is_click(user['序列化工单页Save按钮'])
        self.find_element(user['页签切换'], 'WO Serialized List').click()
        # self.switch_window(n=0)
        self.wait.until(EC.presence_of_element_located(user['序列化工单查询页Add按钮']), message='当前不在查询页')

        self.is_click(user["序列化Search按钮"])

    @allure.step("菜单刷新")
    def refresh_page(self):
        self.find_element(user['页签切换'], 'Dashboard').click()
        self.refresh()
        self.wait.until(EC.presence_of_element_located(user['Dashboard']), message="页面刷新失败")

    @allure.step("新增物料库存")
    def add_material(self):
        self.refresh()
        sleep(2)
        self.is_click(user['库存初始化查询页Add按钮'])
        # 记得修改成显示等待
        self.is_click(user['库存初始化新增页Warehouse Name搜索框'])
        self.input_text(user['库存初始化新增页Warehouse Name搜索框'], txt='API_母仓')
        self.hover(user['库存初始化新增页Warehouse Name下拉选择'], choice='API_母仓')
        self.is_click(user['库存初始化新增页Warehouse Name下拉选择'])
        self.is_click(user["库存初始化新增页添加按钮"])
        logging.info("000")
        sleep(1)
        self.is_click(user['库存初始化新增页物料搜索框'])
        self.input_text(user["库存初始化新增页物料搜索框"], txt='10015788')
        self.hover(user['库存初始化新增页物料选择框'], choice='10015788')
        self.is_click(user['库存初始化新增页物料选择框'])
        # 这里等待物料描述值出现
        sleep(1)
        self.is_click(user["库存初始化新增页物料状态搜索框"])
        self.input_text(user["库存初始化新增页物料状态搜索框"], txt='Defective')
        self.hover(user['库存初始化新增页物料状态选择框'], choice='Defective')
        self.is_click(user['库存初始化新增页物料状态选择框'])
        # 这里要写个获取字符串的方法WS+一串数字且要先查询
        self.is_click(user["库存初始化新增页IMEI输入框"])
        self.input_text(user["库存初始化新增页IMEI输入框"], txt=WOSerializedListAdd.add_imei(self))
        self.is_click(user["库存初始化新增页Zone搜索框"])
        # self.input_text(user["库存初始化新增页Zone搜索框"], txt='Phone')
        self.hover(user['库存初始化新增页Zone选择框'], choice='Phone')
        self.is_click(user["库存初始化新增页Zone选择框"])
        self.is_click(user["库存初始化新增页Bin搜索框"])
        self.input_text(user["库存初始化新增页Bin搜索框"], txt='Defective_1')
        self.hover(user['库存初始化新增页Bin选择框'], choice='Defective_1')
        self.is_click(user["库存初始化新增页Bin选择框"])
        self.is_click(user["库存初始化新增页Save按钮"])
        # 判断是否在库存初始化查询页
        # self.switch_window(n=0)
        sleep(1)
        # NavPage(self).switch_tab(txt='Initialize Inventory')

        self.find_element(user['页签切换'], 'Initialize Inventory').click()

        # self.is_click(user["库存初始化查询页签"])
        # logging.info('11111')

        self.wait.until(EC.presence_of_element_located(user['库存初始化查询页Add按钮']), message='当前不在查询页')
        self.is_click(user["库存初始化查询页confirm按钮"])
        self.is_click(user["库存初始化二次确认框Yes按钮"])
        self.is_click(user["库存初始化Search按钮"])
        self.find_element(user['页签关闭'], 'Initialize Inventory').click()

        # 查询数据库是否有该物料

    @allure.step("新增imei库存")
    def add_imei(self):
        IMEI = "WS2022"
        num = string.digits
        for i in range(10):
            IMEI += random.choice(num)
        user1 = SQL('CRM', 'test')
        record = user1.query_db("SELECT sn_num1 from crm_wms_stock_sn WHERE sn_num1='{}' and status=1 and is_enable=1 AND is_deleted=0".format(IMEI))
        if record is None:
            return IMEI
        else:
            IMEI += random.choice(num)
            return IMEI

    @allure.step("查询imei库存")
    def search_imei_stock(self):
        sql = SQL('CRM', 'test')
        imei = sql.query_db("SELECT SN.sn_num1 FROM crm_wms_stock st LEFT JOIN crm_wms_stock_sn SN ON st.stock_id = SN.stock_id WHERE st.is_deleted = 0 AND st.is_enable = 1 AND st.material_status_id = '1250686603403034625' and st.material_id='1283374022050050050' AND st.num_available != 0 AND SN.is_deleted = 0 AND SN.is_enable = 1 AND SN.`status` = 1 AND st.warehouse_id = '4f54a35e0fcae869aa2c0faf2702b3e4' GROUP BY SN.creation_time DESC")
        dict_imei = imei[0]
        imei_value = dict_imei['sn_num1']
        print(imei_value)
        return imei_value



class WOSerializedListSearch(Base):
    given_data = datetime.today().date()
    logging.info('今天的日期: {} '.format(given_data))
    first_day_of_month = given_data.replace(day=1)
    logging.info('本月的第一天是:{}'.format(first_day_of_month))

    @allure.step("序列化工单查询")
    def search_woserlist(self, scope):
        self.refresh()
        # 查询序列化工单所有数据
        sleep(1)
        self.is_click(user['序列化工单查询页From Date输入框'])
        self.hover(user['序列化工单查询页From Date输入框'])
        self.is_click(user['序列化工单查询页From Date清除按钮'])

        while True:
            if scope == all:

                self.is_click(user['序列化Search按钮'])
                break

            # 查询序列化工单当月created状态的数据,即时间+document status组合查询
            else:
                self.is_click(user['序列化工单查询页From Date输入框'])
                self.input_text(user['序列化工单查询页From Date输入框'], txt=str(WOSerializedListSearch.first_day_of_month))
                self.is_click(user['序列化工单查询页Document Status输入框'])
                # self.input_text(user['序列化工单查询页Document Status输入框'],choice='Created')
                self.hover((user['序列化工单查询页Document Status下拉选择框']))
                self.is_click(user['序列化工单查询页Document Status下拉选择框'])
                # self.is_click(user['序列化Search按钮'])
                self.is_click(user['序列化Search按钮'])

                break

        # self.find_element(user['页签关闭'], 'WO Serialized List').click()

    @allure.step("查询序列化工单数量")
    def search_stock(self, stock):

        sql = SQL('CRM', 'test')
        if stock == all:  # 查询序列化工单所有数据
            record = sql.query_db("SELECT count(*) FROM crm_rc_serialize_work_order WHERE is_deleted=0 AND is_enable=1")
        else:  # 有条件的查询序列化工单数据
            record = sql.query_db("SELECT count(*) FROM crm_rc_serialize_work_order WHERE is_deleted=0 AND is_enable=1 and creation_time>='{}' and status=1".format(WOSerializedListSearch.first_day_of_month))

        dict_record = record[0]
        print(dict_record)
        record_value = dict_record['count(*)']
        logging.info('数据库查询到的序列化工单数据为:{}'.format(record_value))
        search_num = self.get_element_attribute(user['序列化工单total数'], 'textContent')
        num = ''.join(filter(str.isdigit, search_num))
        num = int(num)
        logging.info('序列化工单查询页查到的数量:{}'.format(num))

        return record_value, num


if __name__ == '__main__':
    pass
