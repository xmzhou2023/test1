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
from libs.common.action import KeyWord
import allure
@allure.feature("V2_10_8_2计划")  # 迭代名称
class Teststory_172:
    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面页面检查")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==检查页面")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10452(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面查询")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==输入工号、姓名关键字，进行查询==点击【重置】==进入前后翻页/指定页数，页面显示数据调整")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10453(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增重复数据")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【新增】按钮，新增一个重复的用户")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10454(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增用户")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【新增】按钮，新增正常的用户")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10455(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面导入模板下载")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【导入】按钮，点击【下载导入模板】，模板下载成功。查看文件")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10456(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面导入用户")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【导入】按钮，导入文件中用户工号、姓名、组织权限正确，点击【导入】")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10457(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面导入重复数据")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【导入】按钮，导入文件中存在页面已经存在的用户，点击【导入】")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10458(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面导入用户号不存在")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【导入】按钮，导入文件中的用户号不存在，点击【导入】")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10459(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面权限清单明细导入模板下载")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【限清单明细导入】按钮，点击【下载导入模板】，模板下载成功。查看文件")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10460(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面权限清单明细导入")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【权限清单明细导入】按钮，导入文件中工号、姓名、管理维度、品牌、国家、评审版本、操作权限正确，点击【导入】")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10461(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面权限清单明细导入不存在的数据")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【权限清单明细导入】按钮，导入文件中工号、姓名、管理维度、品牌、国家、评审版本存在页面没有的数据，点击【导入】")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10462(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面权限清单总量导入模板下载")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【限清单明细导入】按钮，点击【下载导入模板】，模板下载成功。查看文件")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10463(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面权限清单总量导入")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【权限清单总量导入】按钮，导入文件中工号、姓名、管理维度、品牌、市场分类、评审版本、操作权限正确，点击【导入】")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10464(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面权限清单总量导入不存在的数据")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【权限清单总量导入】按钮，导入文件中工号、姓名、管理维度、品牌、市场分类、评审版本存在页面没有的数据，点击【导入】")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10465(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面导出用户名单")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【导出】按钮，选择用户民法典，文件导出成功")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10466(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面导出权限清单")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==点击【导出】按钮，选择权限清单，文件导出成功")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10467(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增组织权限")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个组织权限为空的用户，点击【编辑】，进入勾选用户组织权限，点击【确认】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10468(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限明细新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入【新增】用户数据明细权限，点击【确认】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10469(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限总量新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入【新增】用户数据总量权限，点击【确认】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10470(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限明细新增重复")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入【新增】用户数据明细权限，点击【确认】==再次新增一条相同的数据明细权限")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10471(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限总量新增重复")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入【新增】用户数据总量权限，点击【确认】==再次新增一条相同的数据总量权限")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10472(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限明细修改")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入用户数据明细权限页面，选择一条数据点击【编辑】，修改数据，点击【保存】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10473(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限总量修改")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入用户数据总量权限页面，选择一条数据点击【编辑】，修改数据，点击【保存】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10474(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.112.166:9000/#/dashboard")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'系统管理')]").click()
        robot.AI_find_element(By.XPATH, "//span[contains(.,'用户管理')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("18")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'18647045')]").click()
        robot.AI_find_element(By.XPATH, "(//button[@type='button'])[6]").click()
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/section/div/div/div/form/div/div[3]/button[2]/span").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("huang")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'黄盼盼')]").click()
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/section/div/div/div/form/div/div[3]/button/span").click()
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/section/div/div/div/form/div/div[3]/button[2]/span").click()


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限明细删除")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入用户数据明细权限页面，选择一条数据点击【删除】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10475(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.112.166:9000/#/dashboard")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'系统管理')]").click()
        robot.AI_find_element(By.XPATH, "//div[12]/ul/div/a/li/span").click()
        element = robot.AI_find_element(By.XPATH, "//li[contains(.,'用户管理旧版')]")
        actions = ActionChains(robot)
        actions.move_to_element(element).perform()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("186")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'18647045')]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").click()
        robot.AI_find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("黄")
        robot.AI_find_element(By.XPATH, "//span[contains(.,'黄盼盼')]").click()
        robot.AI_find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/section/div/div/div/form/div/div[3]/button/span").click()
        robot.AI_find_element(By.XPATH, "(//button[@type='button'])[7]").click()


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限总量删除")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入用户数据总量权限页面，选择一条数据点击【删除】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10476(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限明细批量删除")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入用户数据明细权限页面，选择多条数据点击【批量删除】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10477(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限总量批量删除")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入用户数据总量权限页面，选择多条数据点击【批量删除】")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10478(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限明细导出")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入用户数据明细权限页面，点击【导出】，导出成功，查看导出文件")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10479(self, drivers):
        pass


    @allure.story("用户管理查询界面及功能优化")  # 用户故事名称
    @allure.title("用户管理主界面新增数据权限总量导出")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt用户管理进入页面。==选择一个用户，点击【编辑】，进入用户数据总量权限页面，点击【导出】，导出成功，查看导出文件")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10480(self, drivers):
        pass


@allure.feature("V2_10_8_2计划")  # 迭代名称
class Teststory_971:
    @allure.story("发运版报表合计值优化")  # 用户故事名称
    @allure.title("DRP报表发运版报表")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gtDRP报表gt发运版报表进入页面。==选择不同管理维度、提报周期、品牌进行查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10481(self, drivers):
        pass


@allure.feature("V2_10_8_2计划")  # 迭代名称
class Teststory_1315:
    @allure.story("集团报表筛选功能优化")  # 用户故事名称
    @allure.title("DRP报表集团报表筛选")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gtDRP报表gt集团报表进入页面。==选择不同管理维度、品牌、功智能机进行查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10482(self, drivers):
        pass


@allure.feature("V2_10_8_2计划")  # 迭代名称
class Teststory_1313:
    @allure.story("集团报表数据排序整改优化")  # 用户故事名称
    @allure.title("DRP报表集团报表表单排序")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gtDRP报表gt集团报表进入页面。==选择不同管理维度、提报周期、品牌进行查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10483(self, drivers):
        pass


if __name__ == '__main__':
      pass
