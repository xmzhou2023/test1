from time import sleep

import allure
import pytest

from project.PDC.page_object.RMManagement_RMMaintenance import UserPage
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
    @allure.story("事业部RM维护") # 场景名称
    @allure.title("新增路线图")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):
        # pytest ./project/PDC/test_case/RMManagement_RMMaintenance.py::TestUtil::test_001_001
        # __________________________ 新增路线图 ____________________________
        form = ['fxy年度计划3', '2023', '北非', 'TECNO']
        i = UserPage(drivers)
        i.switch_location('http://bom-sit.transsion.com:10000/#/roadmap/roadmap-division')
        i.click('button', '+新增路线图')
        i.readonly_input_text('提示-form-input', form[0], 'RM名称')
        i.select_info_input('提示-form-input', form[1], '规划年度')
        i.select_info_input('提示-form-input', form[2], '地区')
        i.select_info_input('提示-form-input', form[3], '品牌')
        i.click('提示-button', '确定')
        DomAssert(drivers).assert_att('新增成功')

        # 返回一个数组 [实例i, 新建好的RM名称(例如:2023北非TECNO-fxy年度计划) ]
        return [i, f'{form[1]}{form[2]}{form[3]}-{form[0]}']

    @allure.story("事业部RM维护后,编辑,选品,提交") # 场景名称
    @allure.title("新增路线图")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers):
        # pytest ./project/PDC/test_case/RMManagement_RMMaintenance.py::TestUtil::test_001_002
        [i, name] = self.test_001_001(drivers)
        # i = UserPage(drivers)
        # name = '2023北非TECNO-fxy年度计划2'
        i.switch_location('http://bom-sit.transsion.com:10000/#/roadmap/roadmap-division')
        i.click('table-button', name, '编辑')
        i.click('button', '选品')
        i.click('sku点击')
        i.click('button', '确定')
        # ______________________________右侧表单必填项填写____________________________
        i.select_info_input('form-input', '是', '是否爆款')
        i.readonly_input_text('form-textarea', 'fxy测试测试', '描述')
        i.readonly_input_text('form-input', '123', 'FOB')
        i.select_info_input('form-input', 'USD', '零售价币种')
        i.readonly_input_text('form-input', '123', '零售价')
        i.readonly_input_text('form-input', '123', '整机成本')
        i.readonly_input_text('form-input', '20', '销售量（K）')
        i.readonly_input_text('form-input', '10', '首单量（K）')
        i.readonly_input_text('form-input', '10', '边际利润（W）')
        i.readonly_input_text('form-input', '3', '毛利率')
        i.input_text('form-input', '2022-08-04', '立项时间')
        i.input_text('form-input', '2022-09-04', '上市时间')
        i.readonly_input_text('form-input', '3', '生命周期（月）')
        # ___________________________如果选的是 北非, 还有一下几个选项 _______________________________
        if name[4:6] == '北非':
            i.select_info_input('form-input', '无', 'Sar sensor（欧盟标配）')
            i.select_info_input('form-input', '无', '气压传感器（北美标配）')

        i.click('button', '保存')
        # 等待5秒, 或许要更长时间
        sleep(5)
        DomAssert(drivers).assert_att('保存成功')

        return [i, name]

    @allure.story("事业部RM维护后,编辑,选品,提交") # 场景名称
    @allure.title("新增路线图")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_003(self, drivers):
        # pytest ./project/PDC/test_case/RMManagement_RMMaintenance.py::TestUtil::test_001_003
        [i, name] = self.test_001_002(drivers)
        # i = UserPage(drivers)
        # name = '2023北非TECNO-fxy年度计划'
        i.switch_location('http://bom-sit.transsion.com:10000/#/roadmap/roadmap-division')
        i.refresh()
        sleep(1)
        i.click('table-button', name, '提交')
        i.click('message-box-button', '确定')
        DomAssert(drivers).assert_att('提交成功')



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
