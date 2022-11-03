import allure
import pytest
from libs.common.time_ui import sleep

from project.PDC.page_object.RMManagement_PMTAreaRMMaintenance import UserPage
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("脚本名称") # 模块名称
class TestUtil:
    @allure.story("PMT区域RM维护") # 场景名称
    @allure.title("汇总")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):
      # pytest ./project/PDC/test_case/RMManagement_PMTAreaRMMaintenance.py::TestUtil::test_001_001
      rmName = "2023北非TECNO-fxy年度计划3"
      pageUrl = 'http://bom-sit.transsion.com:10000/#/roadmap/roadmap-region/collect-roadmap/collect'
      inputData = ['fxy区域汇总2', '2023', '北非']
      i = UserPage(drivers)
      i.switch_location(pageUrl)
      # 表单录入
      i.input_text('form-input', inputData[0], '区域RM名称')
      i.select_info_input('form-input', inputData[1], '规划年度')
      i.select_info_input('form-input', inputData[2], '地区')
      i.click('form-input', '基础RM')

      # 选择事业部RM
      i.input_text('form-input', rmName, 'RM名称')
      i.click('button', '查询')
      # 选中第一行
      i.click('transform-table-select', "1")
      # 点击右箭头按钮
      i.click('icon-button', 'el-icon-arrow-right')
      i.click('transform-button', '确定')

      # 然后保存
      i.click('button', '保存')
      DomAssert(drivers).assert_att('保存成功')
      collectName = f'{inputData[1]}{inputData[2]}-{inputData[0]}'
      return (i, collectName)

    @allure.story("PMT区域RM维护") # 场景名称
    @allure.title("提交评估")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers):
      # pytest ./project/PDC/test_case/RMManagement_PMTAreaRMMaintenance.py::TestUtil::test_001_002
      # (i, collectName) = self.test_001_001(drivers)
      i = UserPage(drivers)
      collectName = '2023北非-fxy区域汇总2'
      # PMT区域RM维护 页面的url
      pageUrl = 'http://bom-sit.transsion.com:10000/#/roadmap/roadmap-region'
      i.switch_location(pageUrl)
      i.click('table-button', collectName, '提交评估')
      i.click('分发方案')
      i.select_info_input('form-input', '自动化测试评估方案', '方案名称', True)
      i.click('button', '查询')
      i.click('dialog-table-radio')
      i.click('分发方案-确定')
      i.click('button', '提交')
      DomAssert(drivers).assert_att('提交成功')
      return (i, collectName)

    @allure.story("代办列表列表中的我的代办") # 场景名称
    @allure.title("完成五轮评估操作")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_003(self, drivers):
      # pytest ./project/PDC/test_case/RMManagement_PMTAreaRMMaintenance.py::TestUtil::test_001_003
      # (i, collectName) = self.test_001_002(drivers)
      i = UserPage(drivers)
      collectName = '2023北非-fxy区域汇总2'
      # 代办列表-我的代办 页面的url
      pageUrl = 'http://bom-sit.transsion.com:10000/#/process/holdon'
      i.switch_location(pageUrl)
      sleep(1)
      i.refresh()
      for j in range(5):
        # 进入 iframe
        i.frame_enter('iframe')
        if j == 0:
          i.click('oneworks-视图切换')
        # 刷新表格数据
        for __ in range(2):
          i.click('oneworks-刷新按钮')
        i.click('oneworks-查看详情-by-rm_name', collectName)
        # 此时会打开窗口, 选择新窗口
        i.switch_window(1)
        if j == 0:
          sleep(20)
        else:
          sleep(5)
        i.click('button', '同 意')
        sleep(1)
        i.click('提示-确定同意')
        sleep(1)
        DomAssert(drivers).assert_att('处理成功，审核通过')
        i.close_switch(1)
