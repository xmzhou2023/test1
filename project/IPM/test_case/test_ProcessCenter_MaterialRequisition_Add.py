from libs.common.time_ui import sleep
from project.IPM.login.login import LoginView
from project.IPM.page_object.ProcessCenter_MaterialRequisition_Add import PubicMethod, MaterialRequisition
import allure
import pytest
@allure.feature('IPM-流程中心-物料申请')
class TestAddMaterial:

    def test_001(self, drivers):
        """用户管理-登录用户"""
        user = LoginView(drivers)
        user.login(drivers,'18646295')
        sleep(3)


    @allure.story("整机-正常场景")
    @allure.title("整机")
    @allure.description("整机-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_002(self,drivers):

        Add=MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试','手机物料')
        sleep(1)
        Add.import_material('手机','整机_100','整机','手机_整机_100_整机.xlsx')
        sleep(4)
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)

    @allure.story("CKD-正常场景")
    @allure.title("CKD")
    @allure.description("CKD-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_003(self,drivers):

        Add=MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试','手机物料')
        sleep(1)
        Add.import_material('手机','CKD_110','CKD','手机-CKD_110-CKD.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)

    @allure.story("其他类贴片主板-正常场景")
    @allure.title("其他类贴片主板")
    @allure.description("其他类贴片主板-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_004(self,drivers):

        Add=MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试','手机物料')
        sleep(1)
        Add.import_material('手机','PCBA_121','其他类贴片主板','手机-PCBA_121-其他类贴片主板.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)

    @allure.story("SKD-正常场景")
    @allure.title("SKD")
    @allure.description("SKD-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_005(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试', '手机物料')
        sleep(1)
        Add.import_material('手机', 'SKD_107', 'SKD', '手机-SKD_107-SKD.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)

    @allure.story("预加工外包料-正常场景")
    @allure.title("预加工外包料")
    @allure.description("预加工外包料-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_006(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试', '手机物料')
        sleep(1)
        Add.import_material('手机', '外包料_128', '预加工外包料', '手机-外包料_128-预加工外包料.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)

    @allure.story("手机-套料PCBA_129-套料存储副板（FLASH）-正常场景")
    @allure.title("手机-套料PCBA_129-套料存储副板（FLASH）")
    @allure.description("手机-套料PCBA_129-套料存储副板（FLASH）-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_007(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试', '手机物料')
        sleep(1)
        Add.import_material('手机', '套料PCBA_129', '套料存储副板（FLASH）', '手机-套料PCBA_129-套料存储副板（FLASH）.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)

    @allure.story("机头包_102-正常场景")
    @allure.title("机头包_102")
    @allure.description("机头包_102-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_008(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试', '手机物料')
        sleep(1)
        Add.import_material('手机', '机头包_102', '机头包', '手机-机头包_102-机头包.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)

    @allure.story("机模-正常场景")
    @allure.title("机模")
    @allure.description("机模-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_009(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试', '手机物料')
        sleep(1)
        Add.import_material('手机', '机模_104', '机模', '手机-机模_104-机模.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)

    @allure.story("海运配件包-正常场景")
    @allure.title("海运配件包")
    @allure.description("海运配件包-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_010(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试', '手机物料')
        sleep(1)
        Add.import_material('手机', '海运配件包_101', '海运配件包', '手机-海运配件包_101-海运配件包.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)



    @allure.story("电池包-正常场景")
    @allure.title("电池包")
    @allure.description("电池包-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_011(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试', '手机物料')
        sleep(1)
        Add.import_material('手机', '独立发运包_132', '电池包', '手机-独立发运包_132-电池包.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)

    @allure.story("虚拟共用件-正常场景")
    @allure.title("虚拟共用件")
    @allure.description("虚拟共用件-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_012(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试', '手机物料')
        sleep(1)
        Add.import_material('手机', '虚拟件_123', '虚拟共用件', '手机-虚拟件_123-虚拟共用件.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)

    @allure.story("主板预加工-正常场景")
    @allure.title("主板预加工")
    @allure.description("主板预加工-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_013(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        sleep(2)
        Add.information('测试', '手机物料')
        sleep(1)
        Add.import_material('手机', '预加工_122', '主板预加工', '手机-预加工_122-主板预加工.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        sleep(4)



if __name__ == '__main__':
    pytest.main('test_ProcessCenter_MaterialRequisition_Add.py')