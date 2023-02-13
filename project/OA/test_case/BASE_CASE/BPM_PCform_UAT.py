import allure
import pytest
import base64
import pytest, logging

from project.OA.page_object.BPM_PCform import BPM_PCform_Page
from project.OA.page_object.BPM_definition import BPM_definition_Page
from project.OA.page_object.OA_login import OAdnluPage
from project.OA.page_object.BPM_modeling import BPM_modeling_Page
from public.base.assert_ui import *
from libs.common.read_config import *
import random

pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""


@allure.feature("BPM流程搭建--UAT环境")  # 模块名称
class TestBPM:
    a = random.randint(1000, 9999)
    global modeling_name
    modeling_name = "机器人数据建模" + str(a)

    global master_entity
    master_entity = "建模的主实体描述" + str(a)

    global process_definition
    process_definition = "机器人流程定义" + str(a)

    @allure.story("BPM流程搭建--UAT环境")  # 场景名称
    @allure.title("三级标题：BPM数据建模首次建模保存成功")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAdnluPage(drivers)
        OA.BPMlog(options=2)
        bmmA = BPM_modeling_Page(drivers)
        bmmA.click_level_one("设计中心")
        bmmA.click_level_two("业务表单")
        bmmA.click_level_three("数据建模")
        bmmA.click_buttons("添加")
        bmmA.input_modeling_name(modeling_name)
        sleep(2)
        bmmA.click_physical_button()
        bmmA.input_master_entity(master_entity)
        # bmmA.click_from_button()
        bmmA.input_note()
        bmmA.click_save()
        itexis = bmmA.ismodeling_success()
        if itexis:
            logging.info("业务建模保存成功")
            assert True
        else:
            logging.info("业务建模保存失败")
            assert False

    @allure.story("BPM流程搭建--UAT环境")  # 场景名称
    @allure.title("三级标题：BPM数据建模首次建模发布成功")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAdnluPage(drivers)
        OA.open_url("http://10.132.68.237:9081/mvue")  # 打开BPM测试环境管理端
        bmmA = BPM_modeling_Page(drivers)
        bmmA.click_level_one("设计中心")
        bmmA.click_level_two("业务表单")
        bmmA.click_level_three("数据建模")
        bmmA.input_modeling(modeling_name)
        bmmA.click_modeling_search()
        bmmA.click_release()
        itexis = bmmA.ismodeling_srelease()
        if itexis:
            logging.info("业务建模发布成功")
            assert True
        else:
            logging.info("业务建模发布失败")
            assert False

    @allure.story("BPM流程搭建--UAT环境")  # 场景名称
    @allure.title("三级标题： PC表单首次添加保存上刚新建数据建模的表单")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAdnluPage(drivers)
        OA.open_url("http://10.132.68.237:9081/mvue")  # 打开BPM测试环境管理端
        bmmA = BPM_modeling_Page(drivers)
        bmmA.click_level_one("设计中心")
        bmmA.click_level_two("业务表单")
        bmmA.click_level_three("pc表单")
        bmmB = BPM_PCform_Page(drivers)
        bmmB.click_add("添加")
        bmmB.input_enter(modeling_name)
        bmmB.click_Inquire("查询")
        bmmB.click_tick()
        bmmB.click_yes()
        bmmB.click_template()
        bmmB.click_template_ok()
        bmmB.click_save()

        itexis = bmmB.ismodeling_save()
        if itexis:
            logging.info("PC表单保存成功")
            assert True
        else:
            logging.info("PC表单保存失败")
            assert False

    @allure.story("BPM流程搭建--UAT环境")  # 场景名称
    @allure.title("三级标题： PC表单首次添加保存上刚新建数据建模的表单")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAdnluPage(drivers)
        OA.open_url("http://10.132.68.237:9081/mvue")  # 打开BPM测试环境管理端
        # OA.BPMlog(options=1)
        bmmA = BPM_modeling_Page(drivers)
        bmmA.click_level_one("设计中心")
        bmmA.click_level_two("业务表单")
        bmmA.click_level_three("pc表单")
        bmmB = BPM_PCform_Page(drivers)
        bmmB.input_PCenter(modeling_name)
        bmmB.click_PCrelease()
        bmmB.click_name()
        bmmB.click_release()
        itexis = bmmB.ismodeling_release()
        if itexis:
            logging.info("PC表单保存成功")
            assert True
        else:
            logging.info("PC表单保存失败")
            assert False

    @allure.story("BPM流程搭建--UAT环境")  # 场景名称
    @allure.title("三级标题： 新建一条流程定义单设置简单的流程图，进行保存")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAdnluPage(drivers)
        OA.open_url("http://10.132.68.237:9081/mvue")  # 打开BPM测试环境管理端
        # OA.BPMlog(options=1)
        bmmA = BPM_modeling_Page(drivers)
        bmmA.click_level_one("流程管理")
        bmmA.click_level_two("流程设计")
        bmmA.click_level_three("流程定义")
        bmmC = BPM_definition_Page(drivers)
        bmmC.click_add("新增")
        bmmC.click_Classification()
        bmmC.click_Category_selection("BPM机器人勿动")
        bmmC.click_confirm()
        bmmC.input_enter(process_definition)  # "机器人流程定义2222"
        bmmC.click_userA()
        bmmC.click_Add_user()
        bmmC.click_Finish()
        bmmC.click_userB()
        bmmC.input_userenter("用户任务1")
        sleep(3)
        bmmC.move_houseA(drivers, 500, 500)
        bmmC.click_save()
        itexis = bmmC.ismodeling_save()
        if itexis:
            logging.info("流程设计保存成功")
            assert True
        else:
            logging.info("流程设计保存失败")
            assert False

    @allure.story("BPM流程搭建--UAT环境")  # 场景名称
    @allure.title("三级标题： 05用例新建的流程定义数据，进行发布")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAdnluPage(drivers)
        OA.open_url("http://10.132.68.237:9081/mvue")  # 打开BPM测试环境管理端
        # OA.BPMlog(options=1)
        bmmA = BPM_modeling_Page(drivers)
        bmmA.click_level_one("流程管理")
        bmmA.click_level_two("流程设计")
        bmmA.click_level_three("流程定义")
        bmmC = BPM_definition_Page(drivers)
        bmmC.input_name(process_definition)  # " process_definition""机器人流程定义1123"
        bmmC.click_search()
        bmmC.click_name()
        bmmC.click_release()
        itexis = bmmC.ismodeling_release()
        if itexis:
            logging.info("流程设计发布成功")
            assert True
        else:
            logging.info("流程设计发布失败")
            assert False

    @allure.story("BPM流程搭建--UAT环境")  # 场景名称
    @allure.title("三级标题： 05用例新建的流程定义数据，进行配置节点审批人")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_007(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAdnluPage(drivers)
        OA.open_url("http://10.132.68.237:9081/mvue")  # 打开BPM测试环境管理端
        # OA.BPMlog(options=1)
        bmmA = BPM_modeling_Page(drivers)
        bmmA.click_level_one("流程管理")
        bmmA.click_level_two("流程设计")
        bmmA.click_level_three("流程定义")
        bmmC = BPM_definition_Page(drivers)
        bmmC.input_name(process_definition)  # " process_definition""机器人流程定义1123"
        # bmmC.input_name("机器人流程定义6654")  # " process_definition"""
        bmmC.click_search()
        bmmC.click_name()
        bmmC.click_Table()
        bmmC.click_global()
        bmmC.click_PC()
        # bmmC.click_input_globalA("机器人数据建模8544")  # modeling_name ""
        bmmC.click_input_globalA(modeling_name)  # modeling_name "机器人数据建模8544"
        bmmC.click_SLPC()
        bmmC.click_input_globalB(modeling_name)
        itexis = bmmC.ismodeling_form()
        bmmC.click_configuration()
        itexisB = bmmC.ismodeling_configuration()

        if itexis and itexisB:
            logging.info("全局设置的PC表单保存成功，并且保存配置成功")
            assert True
        else:
            logging.info("全局设置的PC表单保存失败，并且保存配置失败")
            assert False
        sleep(5)

    @allure.story("BPM流程搭建--UAT环境")  # 场景名称
    @allure.title("三级标题： 05用例新建的流程定义数据，进行配置节点审批人")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_008(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAdnluPage(drivers)
        OA.open_url("http://10.132.68.237:9081/mvue")  # 打开BPM测试环境管理端
        # OA.BPMlog(options=1)
        bmmA = BPM_modeling_Page(drivers)
        bmmA.click_level_one("流程管理")
        bmmA.click_level_two("流程设计")
        bmmA.click_level_three("流程定义")
        bmmC = BPM_definition_Page(drivers)
        bmmC.input_name(process_definition)  # " process_definition""机器人流程定义1123"
        bmmC.click_search()
        bmmC.click_name()
        bmmC.click_Table()
        bmmC.click_input_big("18647220")
        itexis = bmmC.ismodeling_user()
        bmmC.click_configuration()
        bmmC.click_Design()
        bmmC.click_release()
        itexisB = bmmC.ismodeling_release()
        if itexis and itexisB:
            logging.info("流程编辑添加02节点审批人员成功,且发版成功")
            assert True
        else:
            logging.info("流程编辑添加02节点审批人员失败,且发版失败")
            assert False
        sleep(5)


if __name__ == '__main__':
    # pytest.main(['project/DRP/testcase/run_code.py'])
    #     pytest .\project\OA\test_case\BPM_PCform.py
    pass
