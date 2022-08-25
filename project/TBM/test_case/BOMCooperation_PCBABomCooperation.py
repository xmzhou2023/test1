import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from public.base.assert_ui import *
from project.TBM.page_object.BOMCooperation_PCBABomCooperation import PCBABomCooperation
@allure.feature("BOM协作-PCBA BOM协作")  # 模块名称
class TestCreateProcess:
    @allure.story("创建流程")  # 场景名称
    @allure.title("创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，能提交成功并且提示“建流程成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        drivers.get("http://10.250.113.16/")
        drivers.set_window_size(1552, 840)
        drivers.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(4) > .el-submenu__title > span").click()
        drivers.find_element(By.CSS_SELECTOR, ".el-menu-item:nth-child(4) > span").click()
        drivers.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(3) > .el-table_1_column_3").click()
        drivers.find_element(By.CSS_SELECTOR, ".el-table__body-wrapper .el-table__row:nth-child(6) > .el-table_2_column_12 span").click()
        drivers.find_element(By.CSS_SELECTOR, ".el-table__fixed-body-wrapper .el-table__row:nth-child(4) .el-button:nth-child(2) > span").click()
        drivers.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
@allure.feature("BOM协作-PCBA BOM协作")  # 模块名称
class TestCreateProcessExceptionScenario:
    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("导入Bom之前需要选中模板")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，选择一个不存在模板的品牌，其他内容正确填写，查看BOM Tree，无新增BOM按钮；点击导入提示-导入Bom之前需要选中模板")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', 'PCBA BOM制作')
        user.input_add_bom_info('品牌', 'aaaaa')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '试产阶段')
        user.input_add_bom_info('制作虚拟贴片/套片', '否')
        user.assert_add_bomtree_exist(False)
        user.click_bom_import()
        user.assert_toast('导入Bom之前需要选中模板')
    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM tree不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，在BOM tree中不点击新增BOM，其他内容正确填写，点击提交，提示BOM tree不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.select_business_review('李小素')
        user.select_business_review('李小素', '射频&天线工程师')
        user.click_add_submit()
        user.assert_toast('Bom Tree不能为空！')
    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，在BOM tree中点击新增BOM，不选择BOM状态，其他内容正确填写，点击提交，提示BOM状态不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_003(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('物料编码', '12105866')
        user.input_bomtree('用量', '1')
        user.click_add_submit()
        user.assert_toast('BOM状态不能为空')
    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM编码[null]的物料组在对应的模板中未设置！")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，在BOM tree中点击新增BOM，不填写物料编码，其他内容正确填写，点击提交，提示BOM编码空的物料组在对应的模板中未设置！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_004(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.add_bom_info()
        user.click_add_bomtree()
        user.input_bomtree('BOM状态', '试产')
        user.input_bomtree('用量', '1')
        user.select_business_review('李小素')
        user.select_business_review('李小素', '射频&天线工程师')
        user.click_add_submit()
        user.assert_toast('BOM编码[null]的物料组在对应的模板中未设置！')
    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("BOM编码[null]的物料组在对应的模板中未设置！")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBA BOM制作，在BOM tree中点击新增BOM，不填写物料编码，其他内容正确填写，点击提交，提示BOM编码空的物料组在对应的模板中未设置！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_005(self, drivers):
        user = PCBABomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_bom_info('制作类型', 'PCBA BOM制作')
        user.input_add_bom_info('品牌', 'aaaaa')
        user.input_add_bom_info('机型', 'JMB-01')
        user.input_add_bom_info('阶段', '试产阶段')
        user.input_add_bom_info('制作虚拟贴片/套片', '否')
        user.click_add_submit()
        user.assert_toast('请完善Bom信息')
print(121111)
