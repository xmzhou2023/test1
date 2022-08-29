from time import sleep

from project.TES.page_object.BOM import UserPage

import allure
import pytest

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
    @allure.story("二级标题") # 场景名称
    @allure.title("三级标题")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        instance = UserPage(drivers)
        # 点击菜单
        # instance.click_muen()

        # 点击新增按钮
        # instance.click('新增')

        # 直接进入 新增页面
        instance.jump_to('http://bom-sit.transsion.com/#/start-flow/add')

        # BOM信息录入
        instance.BOM_select_info_input('Bom信息-品牌', 'Bom信息-Infinix')
        instance.BOM_select_info_input('Bom信息-市场', 'Bom信息-孟加拉')
        instance.BOM_select_info_input('Bom信息-阶段', 'Bom信息-量产阶段')

        instance.BOM_select_info_input('Bom信息-制作类型', 'Bom信息-生产BOM')
        instance.BOM_select_info_input('Bom信息-机型', 'Bom信息-X559', ' ')

        sleep(1)

        # BOM Tree 录入 点击新增 BOM
        instance.click('新增Bom')
        instance.BOM_select_info_input('新增Bom-Bom类型', '新增Bom-国内生产BOM')
        instance.BOM_select_info_input('新增Bom-Bom状态', '新增Bom-转量产')
        # 点击编辑按钮
        instance.click('新增Bom-编辑')

        sleep(1)
        instance.normal_input('新增Bom-物料编码', '10000001')
        instance.click('新增Bom-10000001')

        instance.normal_input('新增Bom-用量', '1')

        # 录入结束, 点击确认
        instance.click('新增Bom-确定')

        # 业务评审
        instance.click('审核人设置-MPM')
        instance.normal_input('用户输入', '18645960')
        instance.click('用户选择')
        instance.click('审核人设置-确定')

        # 业务审核
        instance.click('审核人设置-采购部')
        instance.normal_input('用户输入', '18645960')
        instance.click('用户选择')
        instance.click('审核人设置-确定')

        # 提交
        instance.click('提交')
        sleep(1)
        DomAssert(drivers).assert_att('提交成功')


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
