import allure
import pytest

from project.XHR.page_object.Schedule_Setting import ScheduleSetting
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("考勤管理-班次设置") # 模块名称
class TestAdd:
    @allure.story("班次设置") # 场景名称
    @allure.title("新增班次")  # 用例名称
    @allure.description("成功新增班次")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        a = ScheduleSetting(drivers)
        a.schedule_setting()
        a.click_add()
        a.input_name('SN_AUTOTEST')
        a.click_selectcompany('Transsion_SN(XD)')
        a.input_atstime('考勤时间', '09:00', '18:00')
        a.input_atstime('休息时间', '12:00', '13:00')
        a.input_ClockTime('上班最早取卡时间提前', '120')
        a.input_ClockTime('下班最晚取卡时间延后', '120')
        a.click_sure()
        DomAssert(drivers).assert_att('保存成功')
        a.delete_banci('SN_AUTOTEST')
        a.sure_del()

    @allure.story("班次设置")  # 场景名称
    @allure.title("编辑班次，校验上班最早取卡时间不能为空")  # 用例名称
    @allure.description("校验上班最早取卡时间不能为空")
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = ScheduleSetting(drivers)
        a.schedule_setting()
        a.click_add()
        a.input_name('SN_AUTOTEST')
        a.click_selectcompany('Transsion_SN(XD)')
        a.input_atstime('考勤时间', '09:00', '18:00')
        a.input_atstime('休息时间', '12:00', '13:00')
        a.input_ClockTime('下班最晚取卡时间延后', '120')
        a.click_sure()
        DomAssert(drivers).assert_att('不能为空')

    @allure.story("班次设置")  # 场景名称
    @allure.title("编辑班次，班次名称不能为空")  # 用例名称
    @allure.description("校验班次名称不能为空")
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = ScheduleSetting(drivers)
        a.schedule_setting()
        a.click_add()
        a.input_name('')
        a.click_blank()
        DomAssert(drivers).assert_att('不能为空')

@allure.feature("考勤管理-班次设置")  # 模块名称
class TestSearch:
    @allure.story("班次查询")  # 场景名称
    @allure.title("查询班次")  # 用例名称
    @allure.description("查询某个班次")
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = ScheduleSetting(drivers)
        a.schedule_setting()
        a.click_add()
        a.input_name('SN_AUTOTEST')
        a.input_alltime()
        DomAssert(drivers).assert_att('保存成功')
        a.click_searchitem()
        a.input_condition('SN_AUTOTEST')
        a.click_searchbutton()
        a.click_closebutton()
        a.assert_search('班次名称', 'SN_AUTOTEST')

@allure.feature("考勤管理-班次设置")  # 模块名称
class TestDelete:
    @allure.story("班次设置")  # 场景名称
    @allure.title("删除班次")  # 用例名称
    @allure.description("删除新增的班次")
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = ScheduleSetting(drivers)
        a.schedule_setting()
        a.click_add()
        a.input_name('SN_AUTOTEST')
        a.input_alltime()
        DomAssert(drivers).assert_att('保存成功')
        a.click_searchitem()
        a.input_condition('SN_AUTOTEST')
        a.click_searchbutton()
        a.click_closebutton()
        a.delete_banci('SN_AUTOTEST')
        a.sure_del()
        DomAssert(drivers).assert_att('删除成功')


if __name__ == '__main__':
    pytest.main(['project/xHR/testcase/run_code.py'])
