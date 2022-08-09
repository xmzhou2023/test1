from libs.common.time_ui import sleep
from project.IPM.login.login import *
from project.IPM.page_object.ProcessCenter_MaterialRequisition_Add import PubicMethod, MaterialRequisition
import allure
import pytest
from project.IPM.page_base.pathconfig import *


@allure.feature('IPM-流程中心-物料申请-前后端物料描述对比')
class TestAddMaterialContrast:

    @allure.story("整机-正常场景1")
    @allure.title("手机物料-整机1")
    @allure.description("整机-物料描述前后端对比1”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_001(self, drivers):
        """用户管理-登录用户"""
        user = LoginPage(drivers)
        user.login(drivers,account='18645960')
        sleep(3)

    @allure.story("整机-正常场景")
    @allure.title("手机物料-整机")
    @allure.description("整机-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_002(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', '整机_100', '整机', Mobile_Material,'手机_整机_100_整机.xlsx')
        sleep(4)
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("CKD-正常场景")
    @allure.title("手机物料-CKD")
    @allure.description("CKD-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_003(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', 'CKD_110', 'CKD', Mobile_Material,'手机-CKD_110-CKD.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("其他类贴片主板-正常场景")
    @allure.title("手机物料-其他类贴片主板")
    @allure.description("其他类贴片主板-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_004(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', 'PCBA_121', '其他类贴片主板', Mobile_Material,'手机-PCBA_121-其他类贴片主板.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    # @allure.story("SKD-正常场景")
    # @allure.title("手机物料-SKD")
    # @allure.description("SKD-物料描述前后端对比”")
    # @allure.severity("trivial")
    # @pytest.mark.smoke
    # def test_005(self, drivers):
    #     Add = MaterialRequisition(drivers)
    #     Add.url_MaterialRequisition()
    #     Add.information('测试', '手机物料')
    #     Add.import_material('手机', 'SKD_107', 'SKD', Mobile_Material,'手机-SKD_107-SKD.xlsx')
    #     Add.delete_MaterialType('1')
    #     Add.Material_Comparison("1")
    #     Add.assert_material('物料描述CN')
    #     Add.assert_material('物料描述EN')
    #     Add.assert_material('物料长描述CN')

    @allure.story("预加工外包料-正常场景")
    @allure.title("手机物料-预加工外包料")
    @allure.description("预加工外包料-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_006(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', '外包料_128', '预加工外包料',Mobile_Material, '手机-外包料_128-预加工外包料.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("手机-套料PCBA_129-套料存储副板（FLASH）-正常场景")
    @allure.title("手机物料-套料存储副板（FLASH）")
    @allure.description("手机-套料PCBA_129-套料存储副板（FLASH）-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_007(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', '套料PCBA_129', '套料存储副板（FLASH）',Mobile_Material, '手机-套料PCBA_129-套料存储副板（FLASH）.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("机头包_102-正常场景")
    @allure.title("手机物料-机头包_102")
    @allure.description("机头包_102-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_008(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', '机头包_102', '机头包',Mobile_Material, '手机-机头包_102-机头包.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("机模-正常场景")
    @allure.title("手机物料-机模")
    @allure.description("机模-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_009(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', '机模_104', '机模',Mobile_Material, '手机-机模_104-机模.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("海运配件包-正常场景")
    @allure.title("手机物料-海运配件包")
    @allure.description("海运配件包-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_010(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', '海运配件包_101', '海运配件包', Mobile_Material,'手机-海运配件包_101-海运配件包.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("电池包-正常场景")
    @allure.title("手机物料-电池包")
    @allure.description("电池包-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_011(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', '独立发运包_132', '电池包', Mobile_Material,'手机-独立发运包_132-电池包.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("虚拟共用件-正常场景")
    @allure.title("手机物料-虚拟共用件")
    @allure.description("虚拟共用件-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_012(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', '虚拟件_123', '虚拟共用件', Mobile_Material,'手机-虚拟件_123-虚拟共用件.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("主板预加工-正常场景")
    @allure.title("手机物料-主板预加工")
    @allure.description("主板预加工-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_013(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('手机', '预加工_122', '主板预加工',Mobile_Material, '手机-预加工_122-主板预加工.xlsx')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("普通数据线-正常场景")
    @allure.title("手机物料-普通数据线")
    @allure.description("普通数据线-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_014(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('安规器件', '数据线_253', '普通数据线',Mobile_Material, '安规器件-数据线_253-普通数据线')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("广告标签-正常场景")
    @allure.title("手机物料-广告标签")
    @allure.description("广告标签-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_014(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('包材', '标贴_238', '广告标签', Mobile_Material,'包材-标贴_238-广告标签')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_PE袋-正常场景")
    @allure.title("手机物料-功能机_PE袋")
    @allure.description("功能机_PE袋-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_015(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('包材', '塑胶袋_383', '功能机_PE袋',Mobile_Material, '包材-塑胶袋_383-功能机_PE袋')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("封套-正常场景")
    @allure.title("手机物料-封套")
    @allure.description("封套-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_016(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('包材', '销售包装组件_382', '封套', Mobile_Material,'包材-销售包装组件_382-封套')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')
    #

    @allure.story("广告膜-正常场景")
    @allure.title("手机物料-广告膜")
    @allure.description("广告膜-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_017(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('包材', '销售护膜_385', '广告膜',Mobile_Material, '包材-销售护膜_385-广告膜')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("卡通箱-正常场景")
    @allure.title("手机物料-卡通箱")
    @allure.description("卡通箱-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_018(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('包材', '运输包装组件_384', '卡通箱',Mobile_Material, '包材-运输包装组件_384-卡通箱')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("说明书-正常场景")
    @allure.title("手机物料-说明书")
    @allure.description("说明书-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_019(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('包材', '纸卡册_386', '说明书', Mobile_Material,'包材-纸卡册_386-说明书')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("驻极体麦克-正常场景")
    @allure.title("手机物料-驻极体麦克")
    @allure.description("驻极体麦克-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_020(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电声器件', 'MIC_192', '驻极体麦克',Mobile_Material, '电声器件-MIC_192-驻极体麦克')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    # @allure.story("有线耳机-正常场景")
    # @allure.title("手机物料-有线耳机")
    # @allure.description("有线耳机-物料描述前后端对比”")
    # @allure.severity("trivial")
    # @pytest.mark.smoke
    # def test_021(self, drivers):
    #     Add = MaterialRequisition(drivers)
    #     Add.url_MaterialRequisition()
    #     Add.information('测试', '手机物料')
    #     Add.import_material('电声器件', '耳机_252', '有线耳机',Mobile_Material, '电声器件-耳机_252-有线耳机')
    #     Add.delete_MaterialType('1')
    #     Add.Material_Comparison("1")
    #     Add.assert_material('物料描述CN')
    #     Add.assert_material('物料描述EN')
    #     Add.assert_material('物料长描述CN')

    @allure.story("功能机_BOX喇叭-正常场景")
    @allure.title("手机物料-功能机_BOX喇叭")
    @allure.description("功能机_BOX喇叭-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_022(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电声器件', '喇叭_194', '功能机_BOX喇叭',Mobile_Material, '电声器件-喇叭_194-功能机_BOX喇叭')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("圆形受话器-正常场景")
    @allure.title("手机物料-圆形受话器")
    @allure.description("圆形受话器-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_023(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电声器件', '听筒_195', '圆形受话器',Mobile_Material, '电声器件-听筒_195-圆形受话器')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("MTK主芯片-正常场景")
    @allure.title("手机物料-MTK主芯片")
    @allure.description("MTK主芯片-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_024(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', 'APU套片_156', 'MTK主芯片', Mobile_Material,'电子元器件-APU套片_156-MTK主芯片')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("EMI_Filter-正常场景")
    @allure.title("手机物料-EMI_Filter")
    @allure.description("EMI_Filter-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_025(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', 'EMI_Filter_332', 'EMI_Filter', Mobile_Material,'电子元器件-EMI_Filter_332-EMI_Filter')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_手电灯-正常场景")
    @allure.title("手机物料-功能机_手电灯")
    @allure.description("功能机_手电灯-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_026(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', 'LED类_333', '功能机_手电灯', Mobile_Material,'电子元器件-LED类_333-功能机_手电灯')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_手电灯-正常场景")
    @allure.title("手机物料-功能机_手电灯")
    @allure.description("功能机_手电灯-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_027(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', 'LNA_334', '功能机_FMLNA',Mobile_Material, '电子元器件-LNA_334-功能机_FMLNA')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("功能机_蓝牙天线-正常场景")
    @allure.title("手机物料-功能机_蓝牙天线")
    @allure.description("功能机_蓝牙天线-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_028(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', 'LTCC_335', '功能机_蓝牙天线',Mobile_Material, '电子元器件-LTCC_335-功能机_蓝牙天线')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_2GPA-正常场景")
    @allure.title("手机物料-功能机_2GPA")
    @allure.description("功能机_2GPA-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_029(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', 'RFPA_336', '功能机_2GPA',Mobile_Material, '电子元器件-RFPA_336-功能机_2GPA')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    '''    @allure.story("SAR_SENSOR-正常场景")
        @allure.title("手机物料-SAR_SENSOR")
        @allure.description("SAR_SENSOR-物料描述前后端对比”")
        @allure.severity("trivial")
        @pytest.mark.smoke
        def test_030(self, drivers):
            Add = MaterialRequisition(drivers)
            Add.url_MaterialRequisition()
            Add.information('测试', '手机物料')
            Add.import_material('电子元器件', 'sensor类_145', 'SAR_SENSOR',Mobile_Material, '电子元器件-sensor类_145-SAR_SENSOR')
            Add.delete_MaterialType('1')
            Add.Material_Comparison("1")
            Add.assert_material('物料描述CN')
            Add.assert_material('物料描述EN')
            Add.assert_material('物料长描述CN')'''

    @allure.story("功能机_热敏电阻-正常场景")
    @allure.title("手机物料-功能机_热敏电阻")
    @allure.description("功能机_热敏电阻-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_031(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '被动器件_151', '功能机_热敏电阻',Mobile_Material, '电子元器件-被动器件_151-功能机_热敏电阻')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_EMCP-正常场景")
    @allure.title("手机物料-功能机_EMCP")
    @allure.description("功能机_EMCP-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_032(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '存储芯片_142', '功能机_EMCP', Mobile_Material,'电子元器件-存储芯片_142-功能机_EMCP')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("TVS-正常场景")
    @allure.title("手机物料-TVS")
    @allure.description("TVS-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_033(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '分立器件_341', 'TVS',Mobile_Material, '电子元器件-分立器件_341-TVS')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("数字电位器芯片-正常场景")
    @allure.title("手机物料-数字电位器芯片")
    @allure.description("数字电位器芯片-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_034(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '功能芯片_342', '数字电位器芯片',Mobile_Material, '电子元器件-功能芯片_342-数字电位器芯片')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_普通晶体-正常场景")
    @allure.title("手机物料-功能机_普通晶体")
    @allure.description("功能机_普通晶体-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_035(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '晶体_149', '功能机_普通晶体', Mobile_Material,'电子元器件-晶体_149-功能机_普通晶体')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_其他开关-正常场景")
    @allure.title("手机物料-功能机_其他开关")
    @allure.description("功能机_其他开关-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_036(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '开关类_343', '功能机_其他开关',Mobile_Material, '电子元器件-开关类_343-功能机_其他开关')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("334-2.4G wifi saw-正常场景")
    @allure.title("手机物料-334-2.4G wifi saw")
    @allure.description("334-2.4G wifi saw-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_037(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '滤波器类_334', '2.4G wifi saw',Mobile_Material, '电子元器件-滤波器类_334-2.4Gwifisaw')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("耦合器_345-正常场景")
    @allure.title("手机物料-耦合器_345")
    @allure.description("耦合器_345-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_038(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '耦合器_345', '耦合器_345', Mobile_Material,'电子元器件-耦合器_345-耦合器')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("闪光灯驱动-正常场景")
    @allure.title("手机物料-闪光灯驱动")
    @allure.description("闪光灯驱动-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_039(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '驱动类_346', '闪光灯驱动', Mobile_Material,'电子元器件-驱动类_346-闪光灯驱动')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("LFEM-正常场景")
    @allure.title("手机物料-LFEM")
    @allure.description("LFEM-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_040(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '射频收发模组_353', 'LFEM',Mobile_Material, '电子元器件-射频收发模组_353-LFEM')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("AB_D类-正常场景")
    @allure.title("手机物料-AB_D类")
    @allure.description("AB_D类-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_040(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('电子元器件', '音频类_147', 'AB_D类',Mobile_Material, '电子元器件-音频类_147-AB_D类')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("OIS马达-正常场景")
    @allure.title("手机物料-OIS马达")
    @allure.description("OIS马达-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_040(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('机电器件', 'VCM_982', 'OIS马达',Mobile_Material, '机电器件-VCM_982-OIS马达')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("圆柱形振动马达-正常场景")
    @allure.title("手机物料-圆柱形振动马达")
    @allure.description("圆柱形振动马达-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_041(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('机电器件', '振动马达_193', '圆柱形振动马达',Mobile_Material, '机电器件-振动马达_193-圆柱形振动马达')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("DOME片-正常场景")
    @allure.title("手机物料-DOME片")
    @allure.description("DOME片-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_042(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', 'DOME片_231', 'DOME片',Mobile_Material, '结构件-DOME片_231-DOME片')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("功能机_LCD镜片-正常场景")
    @allure.title("手机物料-功能机_LCD镜片")
    @allure.description("功能机_LCD镜片-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_043(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', 'PC镜片_370', '功能机_LCD镜片',Mobile_Material, '结构件-PC镜片_370-功能机_LCD镜片')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("PET装饰件-正常场景")
    @allure.title("手机物料-PET装饰件")
    @allure.description("PET装饰件-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_044(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', 'PET件_371', 'PET装饰件', Mobile_Material,'结构件-PET件_371-PET装饰件')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("升降模组-正常场景")
    @allure.title("手机物料-升降模组")
    @allure.description("升降模组-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_045(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '升降模组_378', '升降模组',Mobile_Material, '结构件-升降模组_378-升降模组')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_钢片注塑卡托-正常场景")
    @allure.title("手机物料-功能机_钢片注塑卡托")
    @allure.description("功能机_钢片注塑卡托-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_046(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '卡托_376', '功能机_钢片注塑卡托',Mobile_Material, '结构件-卡托_376-功能机_钢片注塑卡托')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_复合板材镜片-正常场景")
    @allure.title("手机物料-功能机_复合板材镜片")
    @allure.description("功能机_复合板材镜片-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_047(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '复合板材_373', '功能机_复合板材镜片',Mobile_Material, '结构件-复合板材_373-功能机_复合板材镜片')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_复合板材镜片-正常场景")
    @allure.title("手机物料-功能机_复合板材镜片")
    @allure.description("功能机_复合板材镜片-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_048(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '天线_190', '功能机_FPC天线',Mobile_Material, '结构件-天线_190-功能机_FPC天线')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("散热膜-正常场景")
    @allure.title("手机物料-散热膜")
    @allure.description("散热膜-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_049(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '散热_388', '散热膜', Mobile_Material,'结构件-散热_388-散热膜')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("功能机_辅料-正常场景")
    @allure.title("手机物料-功能机_辅料")
    @allure.description("功能机_辅料-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_050(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '模切件_233', '功能机_辅料',Mobile_Material, '结构件-模切件_233-功能机_辅料')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("功能机_IML电池盖组件-正常场景")
    @allure.title("手机物料-功能机_IML电池盖组件")
    @allure.description("功能机_IML电池盖组件-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_051(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '注塑件_381', '功能机_IML电池盖组件', Mobile_Material,'结构件-注塑件_381-功能机_IML电池盖组件')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("功能机_玻璃护膜-正常场景")
    @allure.title("手机物料-功能机_玻璃护膜")
    @allure.description("功能机_玻璃护膜-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_052(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '玻璃件_372', '功能机_玻璃护膜',Mobile_Material, '结构件-玻璃件_372-功能机_玻璃护膜')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("玻纤板电池盖组件-正常场景")
    @allure.title("手机物料-玻纤板电池盖组件")
    @allure.description("玻纤板电池盖组件-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_053(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '玻纤板材_387', '玻纤板电池盖组件',Mobile_Material, '结构件-玻纤板材_387-玻纤板电池盖组件')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_硅胶套-正常场景")
    @allure.title("手机物料-功能机_硅胶套")
    @allure.description("功能机_硅胶套-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_054(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '硅胶套_374', '功能机_硅胶套',Mobile_Material, '结构件-硅胶套_374-功能机_硅胶套')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("功能机_冲压电池盖-正常场景")
    @allure.title("手机物料-功能机_冲压电池盖")
    @allure.description("功能机_冲压电池盖-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_055(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料')
        Add.import_material('结构件', '金属件_375', '功能机_冲压电池盖',Mobile_Material, '结构件-金属件_375-功能机_冲压电池盖')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("铝壳锂离子电池-正常场景")
    @allure.title("手机物料-二级BOM_铝壳锂离子电池")
    @allure.description("铝壳锂离子电池-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_056(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料-二级BOM')
        Add.import_material('安规器件', '锂离子电池_250', '铝壳锂离子电池',Mobile_SecondaryMaterial, '安规器件-锂离子电池_250-铝壳锂离子电池')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




    # @allure.story("带线充电器-正常场景")
    # @allure.title("手机物料-二级BOM-带线充电器")
    # @allure.description("带线充电器-物料描述前后端对比”")
    # @allure.severity("trivial")
    # @pytest.mark.smoke
    # def test_057(self, drivers):
    #     Add = MaterialRequisition(drivers)
    #     Add.url_MaterialRequisition()
    #     Add.information('测试', '手机物料-二级BOM')
    #     Add.import_material('安规器件', '充电器_251', '带线充电器',Mobile_SecondaryMaterial, '安规器件-充电器_251-带线充电器')
    #     Add.delete_MaterialType('1')
    #     Add.Material_Comparison("1")
    #     Add.assert_material('物料描述CN')
    #     Add.assert_material('物料描述EN')
    #     Add.assert_material('物料长描述CN')




    @allure.story("功能机_显示屏-正常场景")
    @allure.title("手机物料-二级BOM-功能机_显示屏")
    @allure.description("功能机_显示屏-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_058(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料-二级BOM')
        Add.import_material('屏幕', '显示屏模组_170', '功能机_显示屏', Mobile_SecondaryMaterial,'屏幕-显示屏模组_170-功能机_显示屏')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




    @allure.story("电容屏-正常场景")
    @allure.title("手机物料-二级BOM-电容屏")
    @allure.description("电容屏-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_059(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料-二级BOM')
        Add.import_material('屏幕', '触摸屏模组_171', '电容屏', Mobile_SecondaryMaterial,'屏幕-触摸屏模组_171-电容屏')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




    @allure.story("Incell-正常场景")
    @allure.title("手机物料-二级BOM-Incell")
    @allure.description("Incell-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_060(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料-二级BOM')
        Add.import_material('屏幕', '全贴合组件_174', 'Incell',Mobile_SecondaryMaterial, '屏幕-全贴合组件_174-Incell')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("功能机_CSP模组-正常场景")
    @allure.title("手机物料-二级BOM-功能机_CSP模组")
    @allure.description("功能机_CSP模组-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_061(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料-二级BOM')
        Add.import_material('摄像头', '摄像头模组_172', '功能机_CSP模组',Mobile_SecondaryMaterial, '摄像头-摄像头模组_172-功能机_CSP模组')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')





    @allure.story("电容式指纹模组-正常场景")
    @allure.title("手机物料-二级BOM-电容式指纹模组")
    @allure.description("电容式指纹模组-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_062(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '手机物料-二级BOM')
        Add.import_material('指纹模组', '指纹模组_176', '电容式指纹模组',Mobile_SecondaryMaterial, '指纹模组-指纹模组_176-电容式指纹模组')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    #
    # @allure.story("无线充电器-正常场景")
    # @allure.title("配件物料-无线充电器")
    # @allure.description("无线充电器-物料描述前后端对比”")
    # @allure.severity("trivial")
    # @pytest.mark.smoke
    # def test_063(self, drivers):
    #     Add = MaterialRequisition(drivers)
    #     Add.url_MaterialRequisition()
    #     Add.information('测试', '配件物料')
    #     Add.import_material('安规器件', '充电器_251', '无线充电器',AccessoryMaterials, '安规器件-充电器_251-无线充电器')
    #     Add.delete_MaterialType('1')
    #     Add.Material_Comparison("1")
    #     Add.assert_material('物料描述CN')
    #     Add.assert_material('物料描述EN')
    #     Add.assert_material('物料长描述CN')

    @allure.story("电芯-正常场景")
    @allure.title("配件物料-电芯")
    @allure.description("电芯-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_064(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('安规器件', '电芯_931', '电芯',AccessoryMaterials, '安规器件-电芯_931-电芯')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("铝壳锂离子电池-正常场景")
    @allure.title("配件物料-铝壳锂离子电池")
    @allure.description("铝壳锂离子电池-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_065(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('安规器件', '锂离子电池_250', '铝壳锂离子电池',AccessoryMaterials, '安规器件-锂离子电池_250-铝壳锂离子电池')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




    @allure.story("普通数据线-正常场景")
    @allure.title("配件物料-普通数据线")
    @allure.description("普通数据线-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_066(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('安规器件', '数据线_253', '普通数据线',AccessoryMaterials, '安规器件-数据线_253-普通数据线')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("广告标签-正常场景")
    @allure.title("配件物料-广告标签")
    @allure.description("广告标签-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_067(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('包材', '标贴_238', '广告标签',AccessoryMaterials, '包材-标贴_238-广告标签')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("功能机_PE袋-正常场景")
    @allure.title("配件物料-功能机_PE袋")
    @allure.description("功能机_PE袋-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_068(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('包材', '塑胶袋_383', '功能机_PE袋',AccessoryMaterials, '包材-塑胶袋_383-功能机_PE袋')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("封套-正常场景")
    @allure.title("配件物料-封套")
    @allure.description("封套-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_069(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('包材', '销售包装组件_382', '封套',AccessoryMaterials, '包材-销售包装组件_382-封套')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')

    @allure.story("广告膜-正常场景")
    @allure.title("配件物料-广告膜")
    @allure.description("广告膜-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_070(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('包材', '销售护膜_385', '广告膜',AccessoryMaterials, '包材-销售护膜_385-广告膜')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("广告膜-正常场景")
    @allure.title("配件物料-广告膜")
    @allure.description("广告膜-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_071(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('包材', '销售护膜_385', '广告膜',AccessoryMaterials, '包材-销售护膜_385-广告膜')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("卡通箱-正常场景")
    @allure.title("配件物料-卡通箱")
    @allure.description("卡通箱-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_072(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('包材', '运输包装组件_384', '卡通箱',AccessoryMaterials, '包材-运输包装组件_384-卡通箱')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("说明书-正常场景")
    @allure.title("配件物料-说明书")
    @allure.description("说明书-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_073(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('包材', '纸卡册_386', '说明书',AccessoryMaterials, '包材-纸卡册_386-说明书')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("有线耳机-正常场景")
    @allure.title("配件物料-有线耳机")
    @allure.description("有线耳机-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_074(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '配件物料')
        Add.import_material('电声器件', '耳机_252', '有线耳机',AccessoryMaterials, '电声器件-耳机_252-有线耳机')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')





    @allure.story("封套-正常场景")
    @allure.title("ODM物料-封套")
    @allure.description("封套-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_075(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('包材', '销售包装组件_382', '封套',ODM_Material, '包材-销售包装组件_382-封套')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




    @allure.story("功能机_1阶HDI主板-正常场景")
    @allure.title("ODM物料-功能机_1阶HDI主板")
    @allure.description("功能机_1阶HDI主板-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_076(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('印刷电路板', 'HDI_155', '功能机_1阶HDI主板',ODM_Material, '印刷电路板-HDI_155-功能机_1阶HDI主板')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')






    @allure.story("功能机_1阶HDI主板-正常场景")
    @allure.title("ODM物料-功能机_1阶HDI主板")
    @allure.description("功能机_1阶HDI主板-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_077(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('印刷电路板', 'HDI_155', '功能机_1阶HDI主板',ODM_Material, '印刷电路板-HDI_155-功能机_1阶HDI主板')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("功能机_显示屏-正常场景")
    @allure.title("ODM物料-功能机_显示屏")
    @allure.description("功能机_显示屏-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_078(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('屏幕', '显示屏模组_170', '功能机_显示屏',ODM_Material, '屏幕-显示屏模组_170-功能机_显示屏')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("整机-正常场景")
    @allure.title("ODM物料-整机")
    @allure.description("整机-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_079(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('手机', '整机_100', '整机',ODM_Material, '手机-整机_100-整机')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')





    @allure.story("电容式指纹模组-正常场景")
    @allure.title("ODM物料-电容式指纹模组")
    @allure.description("电容式指纹模组-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_080(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('指纹模组', '指纹模组_176', '电容式指纹模组',ODM_Material, '指纹模组-指纹模组_176-电容式指纹模组')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




    @allure.story("圆柱形振动马达-正常场景")
    @allure.title("ODM物料-圆柱形振动马达")
    @allure.description("圆柱形振动马达-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_081(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('机电器件', '振动马达_193', '圆柱形振动马达',ODM_Material, '机电器件-振动马达_193-圆柱形振动马达')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("功能机_CSP模组-正常场景")
    @allure.title("ODM物料-功能机_CSP模组")
    @allure.description("功能机_CSP模组-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_082(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('摄像头', '摄像头模组_172', '功能机_CSP模组',ODM_Material, '摄像头-摄像头模组_172-功能机_CSP模组')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("圆柱形振动马达-正常场景")
    @allure.title("ODM物料-圆柱形振动马达")
    @allure.description("圆柱形振动马达-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_083(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('机电器件', '振动马达_193', '圆柱形振动马达',ODM_Material, '机电器件-振动马达_193-圆柱形振动马达')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')


    @allure.story("功能机_BOX喇叭-正常场景")
    @allure.title("ODM物料-功能机_BOX喇叭")
    @allure.description("功能机_BOX喇叭-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_084(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('电声器件', '喇叭_194', '功能机_BOX喇叭',ODM_Material, '电声器件-喇叭_194-功能机_BOX喇叭')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




    @allure.story("MTK主芯片-正常场景")
    @allure.title("ODM物料-MTK主芯片")
    @allure.description("MTK主芯片-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_085(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('电子元器件', 'APU套片_156', 'MTK主芯片',ODM_Material, '电子元器件-APU套片_156-MTK主芯片')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("DOME片-正常场景")
    @allure.title("ODM物料-DOME片")
    @allure.description("DOME片-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_086(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('结构件', 'DOME片_231', 'DOME片',ODM_Material, '结构件-DOME片_231-DOME片')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')







    @allure.story("功能机_弹片-正常场景")
    @allure.title("ODM物料-功能机_弹片")
    @allure.description("功能机_弹片-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_087(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', 'ODM物料')
        Add.import_material('连接器', '贴片五金件_154', '功能机_弹片',ODM_Material, '连接器-贴片五金件_154-功能机_弹片')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("功能机_TP IC-正常场景")
    @allure.title("二级物料-功能机_TP IC")
    @allure.description("功能机_TP IC-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_088(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '二级物料')
        Add.import_material('电子元器件', '驱动芯片_965', '功能机_TP IC',SecondaryMaterial, '电子元器件-驱动芯片_965-功能机_TPIC')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    @allure.story("OIS马达-正常场景")
    @allure.title("二级物料-OIS马达")
    @allure.description("OIS马达-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_089(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '二级物料')
        Add.import_material('机电器件', 'VCM_982', 'OIS马达',SecondaryMaterial, '机电器件-VCM_982-OIS马达')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




    @allure.story("2D盖板-正常场景")
    @allure.title("二级物料-2D盖板")
    @allure.description("2D盖板-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_090(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '二级物料')
        Add.import_material('结构件', '屏幕盖板_961', '2D盖板',SecondaryMaterial, '结构件-屏幕盖板_961-2D盖板')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




    @allure.story("功能机_a-Si-正常场景")
    @allure.title("二级物料-功能机_a-Si")
    @allure.description("功能机_a-Si-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_091(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '二级物料')
        Add.import_material('屏幕', '液晶面板_964', '功能机_a-Si',SecondaryMaterial, '屏幕-液晶面板_964-功能机_a-Si')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




    @allure.story("5P以上玻塑镜头-正常场景")
    @allure.title("二级物料-5P以上玻塑镜头")
    @allure.description("5P以上玻塑镜头-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_092(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '二级物料')
        Add.import_material('摄像头', '镜头_981', '5P以上玻塑镜头',SecondaryMaterial, '摄像头-镜头_981-5P以上玻塑镜头')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')



    # @allure.story("屏幕FPC-正常场景")
    # @allure.title("二级物料-屏幕FPC")
    # @allure.description("屏幕FPC-物料描述前后端对比”")
    # @allure.severity("trivial")
    # @pytest.mark.smoke
    # def test_092(self, drivers):
    #     Add = MaterialRequisition(drivers)
    #     Add.url_MaterialRequisition()
    #     Add.information('测试', '二级物料')
    #     Add.import_material('印刷电路板', '屏幕FPC_963', '屏幕FPC',SecondaryMaterial, '印刷电路板-屏幕FPC_963-屏幕FPC')
    #     Add.delete_MaterialType('1')
    #     Add.Material_Comparison("1")
    #     Add.assert_material('物料描述CN')
    #     Add.assert_material('物料描述EN')
    #     Add.assert_material('物料长描述CN')


    @allure.story("电芯-正常场景")
    @allure.title("二级物料-电芯")
    @allure.description("电芯-物料描述前后端对比”")
    @allure.severity("trivial")
    @pytest.mark.smoke
    def test_093(self, drivers):
        Add = MaterialRequisition(drivers)
        Add.url_MaterialRequisition()
        Add.information('测试', '二级物料')
        Add.import_material('安规器件', '电芯_931', '电芯',SecondaryMaterial, '安规器件-电芯_931-电芯')
        Add.delete_MaterialType('1')
        Add.Material_Comparison("1")
        Add.assert_material('物料描述CN')
        Add.assert_material('物料描述EN')
        Add.assert_material('物料长描述CN')




































if __name__ == '__main__':
    pytest.main('test_ProcessCenter_MaterialRequisition_Add.py')
    #allure serve ./project/IPM/test_case/allure-reports
