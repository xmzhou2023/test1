import os
from libs.config.conf import BASE_DIR
from project.MES_DAP.page_object.OTPQuery_ModuleBatchQuery import ModuleBatchQuery
from project.MES_DAP.page_object.Center_Component import NavPage, PageInfo, ReadData
from project.MES_DAP.test_case.conftest import pro_name
from public.base.assert_ui import DomAssert, SQLAssert, ValueAssert
import pytest
import logging
import allure
import datetime

@pytest.fixture(scope='module', autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往“OTP数据查询-模组批次数据查询”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("OTP数据查询", "模组批次数据查询")
    result = DomAssert(drivers)
    result.assert_url("/otpQuery/moduleBatch")

@allure.feature("OTP数据查询-模组批次数据查询")
class TestQuerryModuleBatchData:
    querry_data = ReadData().read_excel(os.path.join(BASE_DIR, 'project', 'MES_DAP', 'data', 'parametrize.xls'), 'ModuleBatchQuery', 'row', rows=1)
    @allure.story("模组批次数据查询")
    @allure.title("按各条件查询，正确返回查询结果")
    @allure.description("依次选择查询条件查询/各条件组合查询》正确返回查询结果")
    @allure.severity("blocker")
    @pytest.mark.parametrize('matcode, sensorID, sn, cartonNo, supplierName, factoryName, starProduceTime, endProduceTime, sql', querry_data)
    def test_22490(self, drivers, matcode, sensorID, sn, cartonNo, supplierName, factoryName, starProduceTime, endProduceTime, sql):
        data = ModuleBatchQuery(drivers)
        data.click_reset()
        data.input_matcode(matcode)
        data.input_sensorID(sensorID)
        data.input_sn(sn)
        data.input_cartonNo(cartonNo)
        data.input_supplierName(supplierName)
        data.input_factoryName(factoryName)
        data.input_ProduceTime(starProduceTime, endProduceTime)
        data.click_querry()
        count = PageInfo(drivers).get_count()
        db = SQLAssert(pro_name, 'test')
        db.assert_sql_count(count, eval(sql))
