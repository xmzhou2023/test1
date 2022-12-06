import allure
import pytest
from project.IPM.page_object.ProjectManagement_CreateProject import *
from project.IPM.page_base.assert_pubic import *

@allure.feature("项目管理")  # 迭代名称
class Teststory_3259:
    @allure.story("创建项目")  # 用户故事名称
    @allure.title("新增项目成功")  # 用例名称
    @allure.description("点击新增==输入项目信息==保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20708(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("项目经理有创建项目并维护管理权限，不同的项目经理有不同项目的创建及维护权限")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23742(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("新增按钮点击新增按钮，可新增项目，新增成功的项目在项目清单页面展示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23743(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        test = CreateProject(drivers)
        test.Create_project('保存','IT项目模板',f'IPM自动化{now_times}',f'IPM自动化项目描述{now_times}')
        ass = Assert_result(drivers)
        ass.assert_Create_project(f'IPM自动化{now_times}')

    @allure.story("创建项目")  # 用户故事名称
    @allure.title("新增项目基本属性项目模板、项目名称、项目描述")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23744(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("项目模板项目模板管理处维护，启用后可应用模板创建新项目")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23745(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("项目名称必填项、单行文本框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23746(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("项目名称填写符合要求的名称，创建项目成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23747(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("项目名称不填写项目名称，新增项目失败，提示必填项未填写")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23748(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("项目名称填写了重复的项目名，新建失败，提示项目名称不能重复")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23749(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("产品项目名称产品项目新建成功后，项目名称是根据项目名主板名自动合成的，更改了项目名和主板名后，产品项目需要同步变更")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23750(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("技术项目名称技术项目名称新建成功后，项目名称与项目名必须保持一致，若项目名更改了，项目名称要保持一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23751(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("项目状态根据项目对象关联的生命周期模板，获取项目的生命周期状态及初始的状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23752(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("项目描述非必填，多行文本框、字符长度1000")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23753(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("项目描述不填写项目描述，新建项目成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23754(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        test = CreateProject(drivers)
        test.Create_project('保存', 'IT项目模板', f'IPM自动化{now_times}')
        ass = Assert_result(drivers)
        ass.assert_Create_project(f'IPM自动化{now_times}')


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("项目描述填写了项目描述，符合要求，新建项目成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23755(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("确定按钮点击确认按钮，校验必填项是否填写，校验通过，创建项目成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23756(self, drivers):
        pass


    @allure.story("创建项目")  # 用户故事名称
    @allure.title("取消按钮点击取消按钮，取消创建项目")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23757(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3275:
    @allure.story("基本信息")  # 用户故事名称
    @allure.title("必填项填写完成保存成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20711(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3345:
    @allure.story("计划_里程碑新里程碑视图_查询")  # 用户故事名称
    @allure.title("点击【里程碑】图标按钮，查看里程碑视图")  # 用例名称
    @allure.description("进入项目管理》项目》计划》点击【里程碑】图标按钮，查看里程碑视图")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20957(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查询")  # 用户故事名称
    @allure.title("点击【里程碑】图标按钮，里程碑视图显示最新的里程碑视图")  # 用例名称
    @allure.description("项目管理》项目》计划》点击【里程碑】图标按钮，查看里程碑视图")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20958(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查询")  # 用户故事名称
    @allure.title("点击【里程碑】图标按钮，弹出方式为【弹出框式】")  # 用例名称
    @allure.description("项目管理》项目》计划》点击【里程碑】图标按钮，查看里程碑视图的弹出方式")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20959(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查询")  # 用户故事名称
    @allure.title("【里程碑】图标按钮TIP显示【里程碑视图】")  # 用例名称
    @allure.description("项目管理》项目》计划》鼠标移动到【里程碑】图标按钮悬停，查看【里程碑视图】按钮的TIP显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20960(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3346:
    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("登录【项目经理】权限账号，编辑【计划开始时间】和【计划结束时间】，能正常编辑保存")  # 用例名称
    @allure.description("登录【项目经理】权限账号，选择项目》计划中关联里程碑的任务点击==编辑【计划开始时间】和【计划结束时间】，点击【保存】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20961(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("登录【其他角色】权限账号（非项目经理角色），【计划开始时间】和【计划结束时间】无法编辑；只能查看")  # 用例名称
    @allure.description("登录【其他角色】权限账号（非项目经理角色），选择项目》计划中关联里程碑的任务点击==编辑【计划开始时间】和【计划结束时间】")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20962(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("任务弹窗中的字段新增加【实际开始时间】字段，【实际开始时间】为【日期型】，不可编辑，只能查看")  # 用例名称
    @allure.description("分别点击不同任务类型的任务，查看任务弹窗中的字段显示==编辑【实际开始时间】字段")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20963(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("当任务由未开始改变为进行中保存后，查看该任务的【实际开始时间】字段显示，显示【未开始】到【进行中】保存后的时间")  # 用例名称
    @allure.description("当任务由未开始改变为进行中保存后，查看该任务的【实际开始时间】字段显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20964(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("选择任务的里程碑在非正式版本时，对该任务的【计划开始时间】和【计划结束时间】进行编辑保存，编辑保存成功")  # 用例名称
    @allure.description("选择任务的里程碑在非V1.0时，对该任务的【计划开始时间】和【计划结束时间】进行编辑保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20965(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("选择任务的里程碑在正式版本审核中及正式版本审核通过之后的版本时，【计划开始时间】和【计划结束时间】不可以被编辑，只能查看")  # 用例名称
    @allure.description("选择任务的里程碑在在V1.0审核中及V1.0审核通过之后的版本时，对该任务的【计划开始时间】和【计划结束时间】进行编辑保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20966(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图未提交审批时，为【非正式版本】，视图左上角不显示任何标记")  # 用例名称
    @allure.description("里程碑视图未提交审批时，查看里程碑视图状态")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20968(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图提交审批，在审核中时，为【正式版本且审核中】，视图左上角显示【审核中】")  # 用例名称
    @allure.description("里程碑视图提交审批，在审核中时，查看里程碑视图状态")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20969(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图提交审批且通过后，为【正式版且审核通过】，视图左上角显示【V1.0，V2.0...依次类推】")  # 用例名称
    @allure.description("里程碑视图提交审批且通过后，为【正式版且审核通过】，查看里程碑视图状态")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20970(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图点击【发布】按钮，提交第一次审批在审核中阶段，里程碑视图的左上角显示V1.0（审批中）")  # 用例名称
    @allure.description("里程碑视图点击【发布】按钮，提交第一次审批在审核中阶段，查看里程碑视图的左上角显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20971(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图点击【发布】按钮，提交第N次审批在审批中阶段，里程碑视图的左上角显示VN.0（审批中）")  # 用例名称
    @allure.description("里程碑视图点击【发布】按钮，提交第N次审批在审批中阶段，查看里程碑视图的左上角显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20972(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图点击【发布】按钮，提交第一次审批且流程审批通过后，里程碑视图的左上角显示V1.0（审批通过）")  # 用例名称
    @allure.description("里程碑视图点击【发布】按钮，提交第一次审批且流程审批通过后，查看里程碑视图的左上角显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20973(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图点击【发布】按钮，提交第N次审批且流程审批通过后，里程碑视图的左上角显示VN.0（审批通过）")  # 用例名称
    @allure.description("里程碑视图点击【发布】按钮，提交第N次审批且流程审批通过后，查看里程碑视图的左上角显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20974(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图的【新增】按钮，项目经理和超级管理员账号均可【查看】和【操作】")  # 用例名称
    @allure.description("登录项目经理和超管账号，在里程碑视图中查看【新增】按钮并点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20981(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图的【新增】按钮，团队中其他成员和非团队成员无法查看【新增】按钮（超管账号除外）")  # 用例名称
    @allure.description("其他成员和非团队成员账号，在里程碑视图中查看【新增】按钮并点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20982(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图的【保存】按钮，项目经理和超级管理员账号均可【查看】和【操作】")  # 用例名称
    @allure.description("登录项目经理和超管账号，在里程碑视图中查看【保存】按钮并点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20983(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图的【保存】按钮，团队中其他成员和非团队成员账号无法查看【保存】按钮（超管账号除外）")  # 用例名称
    @allure.description("其他成员和非团队成员账号，在里程碑视图中查看【保存】按钮并点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20984(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图的【发布】按钮，项目经理和超级管理员账号均可【查看】和【操作】")  # 用例名称
    @allure.description("登录项目经理和超管账号，在里程碑视图中查看【发布】按钮并点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20985(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("里程碑视图的【发布】按钮，团队中其他成员和非团队成员账号无法查看【发布】按钮（超管账号除外）")  # 用例名称
    @allure.description("其他成员和非团队成员账号，在里程碑视图中查看【发布】按钮并点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20986(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为正式版本且流程审核通过时，项目经理和超级管理员账号可以对【新增】按钮进行【操作】")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为正式版本且流程审核通过时，项目经理和超级管理员账号对【新增】按钮点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20990(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为正式版本且流程审核通过时，非项目经理和非超管账号均不可对【新增】按钮【操作】")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为正式版本且流程审核通过时，非项目经理和非超级管理员账号对【新增】按钮点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20991(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为非正式版或正式版本且在审核中时，所有账号均不可对【新增】按钮进行【操作】（包含项目经理和超管账号）")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为非正式版或正式版本且在审核中时，登录项目经理和超管账号点击【新增】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20992(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为非正式版时，项目经理和超级管理员账号可以对【保存】按钮进行【操作】")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为非正式版时，登录项目经理和超管账号点击【保存】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20993(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为非正式版时，非项目经理和非超管账号账号均不可对【保存】按钮【操作】")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为非正式版时，登录非项目经理和非超管账号点击【保存】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20994(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为正式版本时（包含正式版本【审核中】和正式版本【审核通过】），所有账号均不可对【保存】按钮进行【操作】（包含项目经理和超管账号）")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为正式版本时，登录项目经理和超管账号点击【保存】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20995(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为非正式版时，项目经理和超级管理员账号可以对【发布】按钮进行【操作】")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为非正式版时，登录项目经理和超管账号点击【发布】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20996(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为非正式版时，非项目经理和非超管账号均不可对【发布】按钮【操作】")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为非正式版时，登录非项目经理和非超管账号点击【发布】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20997(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为正式版本时（包含正式版本【审核中】和正式版本【审核通过】），所有账号均不可对【发布】按钮进行【操作】（包含项目经理和超管账号）")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为正式版本时，登录项目经理和超管账号点击【发布】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20998(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("清空【计划开始时间】，【保存】，提示【计划开始时间】不能为空")  # 用例名称
    @allure.description("在里程碑视图中选择【非正式版本】的里程碑进行点击，在里程碑弹窗中编辑【计划开始时间】和【计划完成时间】，清空【计划开始时间】，点击【保存】")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21034(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_新增保存发布")  # 用户故事名称
    @allure.title("清空【计划结束时间】，【保存】，提示【计划结束时间】不能为空")  # 用例名称
    @allure.description("在里程碑视图中选择【非正式版本】的里程碑进行点击，在里程碑弹窗中编辑【计划开始时间】和【计划完成时间】，清空【计划结束时间】，点击【保存】")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21035(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3355:
    @allure.story("计划_里程碑里程碑的时间显示优化")  # 用户故事名称
    @allure.title("登录项目经理角色账号，在PD基线和IPD模块化项目》计划中查看表头的【里程碑】按钮，【里程碑】按钮在表头正常显示")  # 用例名称
    @allure.description("登录项目经理角色账号，在PD基线和IPD模块化项目》计划中查看表头的【里程碑】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20967(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3348:
    @allure.story("计划_里程碑新里程碑视图_导出")  # 用户故事名称
    @allure.title("里程碑视图的【导出】按钮，团队成员账号均可【查看】和【操作】")  # 用例名称
    @allure.description("登录团队成员和超管账号，在里程碑视图中查看【导出】按钮并点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20975(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导出")  # 用户故事名称
    @allure.title("里程碑视图的【导出】按钮，非团队成员无法【查看】和【操作】（超管账号除外）")  # 用例名称
    @allure.description("登录非团队成员账号，在里程碑视图中查看【导出】按钮并点击（超管账号除外）")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20976(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导出")  # 用户故事名称
    @allure.title("导出的Excel文件中的sheet1中的里程碑版本时间显示对应的计划开始时间和计划结束时间")  # 用例名称
    @allure.description("在里程碑视图弹窗中，点击【导出】按钮，查看导出文件中的sheet1页显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21104(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导出")  # 用户故事名称
    @allure.title("导出的Excel文件中的sheet2中的里程碑版本时间显示对应配置的开始时间或结束时间")  # 用例名称
    @allure.description("在里程碑视图弹窗中，点击【导出】按钮，查看导出文件中的sheet2页显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21105(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导出")  # 用户故事名称
    @allure.title("里程碑视图中导出，导出中Excel文件中的sheet2中包含一个只展示【非正式版本】里程碑时间列表，根据阿波罗配置，显示对应的开始/结束时间对比")  # 用例名称
    @allure.description("在里程碑视图弹窗中，点击【导出】按钮，查看导出文件中的sheet2页显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21106(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导出")  # 用户故事名称
    @allure.title("里程碑视图中导出，导出中Excel文件中的sheet2中包含一个只展示【正式版本】里程碑时间列表，根据阿波罗配置，显示对应的开始/结束时间对比")  # 用例名称
    @allure.description("在里程碑视图弹窗中，点击【导出】按钮，查看导出文件中的sheet2页显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21107(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导出")  # 用户故事名称
    @allure.title("里程碑视图中导出，导出中Excel文件中的sheet2中包含一个展示【非正式和正式版本】里程碑时间列表，根据阿波罗配置，显示对应的开始/结束时间对比")  # 用例名称
    @allure.description("在里程碑视图弹窗中，点击【导出】按钮，查看导出文件中的sheet2页显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21108(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导出")  # 用户故事名称
    @allure.title("导出列表左上方会显示【对应项目的项目名称】")  # 用例名称
    @allure.description("在里程碑视图弹窗中，点击【导出】按钮，查看导出文件中列表的左上方显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21109(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导出")  # 用户故事名称
    @allure.title("导出列表左上方会显示【开发周期】，开发周期为项目的计划结束时间项目的计划开始日期")  # 用例名称
    @allure.description("在里程碑视图弹窗中，点击【导出】按钮，查看导出文件中列表的左上方显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21110(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3349:
    @allure.story("计划_里程碑新里程碑视图_流程记录")  # 用户故事名称
    @allure.title("里程碑视图的【流程记录】按钮，团队成员和超管账号均可【查看】和【操作】")  # 用例名称
    @allure.description("登录团队成员和超管账号，在里程碑视图中查看【流程记录】按钮并点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20977(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_流程记录")  # 用户故事名称
    @allure.title("里程碑视图的【流程记录】按钮，非团队成员无法【查看】和【操作】（超管账号除外）")  # 用例名称
    @allure.description("登录非团队成员账号，在里程碑视图中查看【流程记录】按钮并点击（超管账号除外）")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20978(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_流程记录")  # 用户故事名称
    @allure.title("里程碑正式版本（审批中）时，再【发布】，提示【有审批中的里程碑，请在工作台我的申请查看对应单据】")  # 用例名称
    @allure.description("发起页面中，当里程碑正式版本（审批中）时，再点击【发布】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21076(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_流程记录")  # 用户故事名称
    @allure.title("提交和保存的单据信息在对应数据库表中，校验与保存提交的表单信息保持一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21077(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_流程记录")  # 用户故事名称
    @allure.title("流程记录弹窗，显示历史审核中，审批拒绝，审批通过的【流程记录数据】")  # 用例名称
    @allure.description("在里程碑视图中，点击【流程记录】按钮，查看流程记录弹窗显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21111(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_流程记录")  # 用户故事名称
    @allure.title("校验【版本】、【流程编码】、【单据状态】、【提单人】、【提单时间】、【审批通过时间】字段对应的值显示")  # 用例名称
    @allure.description("在里程碑视图中，点击【流程记录】按钮，查看流程记录弹窗中的【版本】、【流程编码】、【单据状态】、【提单人】、【提单时间】、【审批通过时间】字段显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21112(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_流程记录")  # 用户故事名称
    @allure.title("流程记录弹窗中【流程记录】按照流程提单时间降序排列")  # 用例名称
    @allure.description("在里程碑视图中，点击【流程记录】按钮，查看流程记录弹窗中的流程记录排序显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21113(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_流程记录")  # 用户故事名称
    @allure.title("流程记录弹窗中【流程编码】为超链接，点击对应【流程编码】链接，进入对应流程单据详情页")  # 用例名称
    @allure.description("在里程碑视图中，点击【流程记录】按钮，点击对应【流程编码】链接")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21114(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3347:
    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("里程碑视图的【导入】按钮，项目经理和超级管理员账号均可【查看】和【操作】")  # 用例名称
    @allure.description("登录项目经理和超管账号，在里程碑视图中查看【导入】按钮并点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20979(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("里程碑视图的【导入】按钮，团队中其他成员和非团队成员账号无法查看【导入】按钮；（超管账号除外）")  # 用例名称
    @allure.description("其他成员和非团队成员账号，在里程碑视图中查看【导入】按钮并点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20980(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为非正式版本时，项目经理和超级管理员账号可以【操作】【导入】按钮")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为非正式版本时，登录项目经理和超管账号，点击【导入】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20987(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为非正式版本时，非项目经理和非超级管理员账号账号均不可以【操作】【导入】按钮")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为非正式版本时，登录非项目经理和非超管账号，点击【导入】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20988(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为正式版本时（包含正式版本【审核中】和正式版本【审核通过】），所有账号均不可对【导入】按钮进行【操作】（包含项目经理和超管账号）")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为正式版本时（包含正式版本【审核中】和正式版本【审核通过】），登录超管和项目经理账号对【导入】按钮点击")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20989(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("导入模板与当前里程碑视图列表保持一致，导入模板能正常下载")  # 用例名称
    @allure.description("里程碑视图弹窗中，点击【导入】按钮，在导入弹窗中，点击【导入模板】按钮==下载成功后，对比查看导入模板与里程碑视图列表")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21097(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("导入非Excel文件，导入文件后校验文件类型错误，并提示'文件不匹配！'")  # 用例名称
    @allure.description("里程碑视图弹窗中，点击【导入】按钮，在导入弹窗中，选择导入非Excel文件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21098(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("导入的Excel文件中的阶段与项目中的阶段不一致，则提示'碑阶段与项目阶段不匹配！'不显示导入校验结果")  # 用例名称
    @allure.description("里程碑视图弹窗中，点击【导入】按钮，在导入弹窗中，选择导入一个阶段与项目中的阶段不一致的Excel文件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21099(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("导入的Excel文件中的阶段与里程碑视图中的阶段不一致，则提示'里程碑与项目里程碑不匹配！'不显示导入校验结果")  # 用例名称
    @allure.description("里程碑视图弹窗中，点击【导入】按钮，在导入弹窗中，选择导入一个阶段与里程碑视图中的阶段不一致的Excel文件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21100(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("导入的Excel文件中的时间与里程碑视图中的时间格式不一致，则提示'XXXX的计划开始时间或计划结束时间不正确格式不匹配'")  # 用例名称
    @allure.description("里程碑视图弹窗中，点击【导入】按钮，在导入弹窗中，导入文件时间与里程碑视图中的时间格式不一致")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21101(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("导入的Excel文件中的无非正式版本数据，则提示'无里程碑数据，请编辑后再导入。'")  # 用例名称
    @allure.description("里程碑视图弹窗中，点击【导入】按钮，在导入弹窗中，导入文件无非正式版本数据")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21102(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_导入")  # 用户故事名称
    @allure.title("导入的Excel文件中的正式版本数据自动过滤，只导入非正式版的里程碑数据")  # 用例名称
    @allure.description("里程碑视图弹窗中，点击【导入】按钮，在导入弹窗中，导入文件")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21103(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3353:
    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("项目经理及超管账号，可以在里程碑视图列表中对里程碑日期进行编辑；其余账号，不能在里程碑视图列表中对里程碑日期进行编辑")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为正式版本时，登录非项目经理和非超管账号点击【发布】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20999(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为非正式版时，项目经理和超级管理员账号可以对里程碑节点日期进行【编辑修改】")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为非正式版时，登录项目经理和超管账号对里程碑节点日期进行【编辑修改】")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21000(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为非正式版时，非项目经理和非超管账号无法对里程碑节点日期进行【编辑修改】")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为非正式版时，登录非项目经理和非超管账号对里程碑节点日期进行【编辑修改】")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21001(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("当前里程碑视图的最新版本为正式版本时（包含正式版本【审核中】和正式版本【审核通过】），所有账号均不能对里程碑节点日期进行【编辑修改】（包含项目经理和超管账号）")  # 用例名称
    @allure.description("当前里程碑视图的最新版本为正式版本时。登录项目经理和超管账号对里程碑节点日期进行【编辑修改】")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21002(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("设置里程碑的配置，配置项有'以开始时间计算'、'以结束时间计算'")  # 用例名称
    @allure.description("在阿波罗配置项中配置'以开始时间计算'、'以结束时间计算'")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21003(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("如果第一层WBS下存在里程碑，则在里程碑视图中显示该阶段名称")  # 用例名称
    @allure.description("在第一层WBS下将一个任务设置里程碑，在里程碑视图中，查看对应的阶段名称")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21004(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("如果第一层WBS下不存在任何里程碑，则在里程碑视图中不显示该阶段")  # 用例名称
    @allure.description("当一个第一层WBS下一个任务均没有设置里程碑，在里程碑视图中，查看对应的阶段名称")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21005(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("如果第一层WBS本身就是'TR'、'DCP'、quot里程碑'中类型的计划，则该阶段名称也在该阶段下第一层的里程碑名称中显示")  # 用例名称
    @allure.description("分别选择三个第一层WBS下没有设置里程碑的任务的阶段，对这三个阶段分别设置'TR'、'DCP'、quot里程碑'，在里程碑视图中查看这三个阶段的显示==分别选择三个第一层WBS下没有设置里程碑的任务的阶段，对这三个阶段分别设置'TR'、'DCP'、quot里程碑'，在里程碑视图中查看这三个阶段的显示==分别选择三个第一层WBS下没有设置里程碑的任务的阶段，对这三个阶段分别设置'TR'、'DCP'、quot里程碑'，在里程碑视图中查看这三个阶段的显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21006(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("里程碑视图中的阶段名称下的里程碑名称取的是对应阶段下的'TR'、'DCP'、quot里程碑'类型的计划")  # 用例名称
    @allure.description("选择一个第一层WBS，在其下选择三个任务分别设置'TR'、'DCP'、quot里程碑'，进入里程碑视图中，查看对应阶段下的该三个任务显示==选择一个第一层WBS，在其下选择三个任务分别设置'TR'、'DCP'、quot里程碑'，进入里程碑视图中，查看对应阶段下的该三个任务显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21007(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("根据阶段下的任务排序，按顺序显示第一层、第二层、第N层里程碑；如果阶段本身为'TR'、'DCP'、quot里程碑'类型的计划，则第一层里程碑为阶段名称本身")  # 用例名称
    @allure.description("选择在一个阶段下建立多个层级任务，在该阶段下的任务，分别建立'TR'、'DCP'、quot里程碑'类型的计划==在里程碑视图中查看该阶段显示和阶段下的里程碑显示==选择在一个阶段下建立多个层级任务，在该阶段下的任务，分别建立'TR'、'DCP'、quot里程碑'类型的计划==在里程碑视图中查看该阶段显示和阶段下的里程碑显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21008(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("【里程碑信息】不可编辑，只读")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21071(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("【里程碑信息】中显示当前版本的及历史所有正式版本的里程碑信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21072(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("【里程碑信息】可以根据选择的【阶段名称】进行筛选显示，点击导出按钮，导出全部里程碑信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21073(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("流程审批基本信息不可编辑，默认展示")  # 用例名称
    @allure.description("查看流程审批页面中的基本信息模块显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21115(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_查看单据")  # 用户故事名称
    @allure.title("流程审批支持查看里程碑版本的TIP值")  # 用例名称
    @allure.description("鼠标浮动到里程碑版本位置，查看对应显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21118(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3354:
    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("【版本时间】配置【计划开始时间】和【计划结束时间】保存后，里程碑配置项选择的【以开始时间计算】则在里程碑视图的版本时间按【计划开始时间】显示，TIP方式不变")  # 用例名称
    @allure.description("在【里程碑视图】中的里程碑【版本时间】配置【计划开始时间】和【计划结束时间】后，点击保存==阿波罗中配置项为【以开始时间计算】，查看里程碑视图中的版本时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21009(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("【版本时间】配置【计划开始时间】和【计划结束时间】保存后，里程碑配置项选择的【以结束时间计算】则在里程碑视图的版本时间按【计划结束时间】显示，TIP方式不变")  # 用例名称
    @allure.description("在【里程碑视图】中的里程碑【版本时间】配置【计划开始时间】和【计划结束时间】后，点击保存==阿波罗中配置项为【以结束时间计算】，查看里程碑视图中的版本时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21010(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑配置项选择的【以开始时间计算】则在里程碑视图的【实际】按【实际开始时间】显示")  # 用例名称
    @allure.description("阿波罗中配置项为【以开始时间计算】，查看里程碑视图中的【实际】时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21011(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑配置项选择的【以结束时间计算】则在里程碑视图的【实际】按【实际结束时间】显示")  # 用例名称
    @allure.description("阿波罗中配置项为【以结束时间计算】，查看里程碑视图中的【实际】时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21012(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑配置项选择的【以开始时间计算】，里程碑视图的【偏差】行，则根据对应的最新正式版本的里程碑计划开始时间实际开始时间")  # 用例名称
    @allure.description("阿波罗中配置项为【以开始时间计算】，查看里程碑视图中的【偏差】时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21013(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("计划开始时间【大于】实际开始时间，则对应偏差行显示为【正整数】")  # 用例名称
    @allure.description("阿波罗中配置项为【以开始时间计算】，计划开始时间【大于】实际开始时间，查看里程碑视图中的【偏差】时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21014(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("计划开始时间【小于】实际开始时间，则对应偏差行显示为【负整数】")  # 用例名称
    @allure.description("阿波罗中配置项为【以开始时间计算】，计划开始时间【小于】实际开始时间，查看里程碑视图中的【偏差】时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21015(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("计划开始时间【等于】实际开始时间，则对应偏差行显示为【0】")  # 用例名称
    @allure.description("阿波罗中配置项为【以开始时间计算】，计划开始时间【等于】实际开始时间，查看里程碑视图中的【偏差】时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21016(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑配置项选择的【以结束时间计算】，里程碑视图的【偏差】行，则根据对应的最新正式版本的里程碑计划结束时间实际结束时间")  # 用例名称
    @allure.description("阿波罗中配置项为【以结束时间计算】，查看里程碑视图中的【偏差】时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21017(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("计划结束时间【大于】实际结束时间，则对应偏差行显示为【正整数】")  # 用例名称
    @allure.description("阿波罗中配置项为【以结束时间计算】，计划开始时间【大于】实际开始时间，查看里程碑视图中的【偏差】时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21018(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("计划结束时间【小于】实际结束时间，则对应偏差行显示为【负整数】")  # 用例名称
    @allure.description("阿波罗中配置项为【以结束时间计算】，计划开始时间【小于】实际开始时间，查看里程碑视图中的【偏差】时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21019(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("计划结束时间【等于】实际结束时间，则对应偏差行显示为【0】")  # 用例名称
    @allure.description("阿波罗中配置项为【以结束时间计算】，计划开始时间【等于】实际开始时间，查看里程碑视图中的【偏差】时间显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21020(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑视图中的复选框，默认显示所有存在里程碑的第一层WBS计划和全选按钮，默认勾选【全选】复选框")  # 用例名称
    @allure.description("进入里程碑视图中，查看里程碑视图的复选框选项")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21021(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("复选框支持单选，多选，全选")  # 用例名称
    @allure.description("对里程碑视图的复选框选项，进行单选，多选，全选")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21022(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("只展示选择的对应阶段的里程碑字段，未勾选的阶段则把相关阶段的里程碑字段全部隐藏")  # 用例名称
    @allure.description("对里程碑视图的复选框选项进行勾选后，查看里程碑信息显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21023(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("【计划】页面中，【里程碑视图】按钮TIP显示【里程碑视图】")  # 用例名称
    @allure.description("【计划】页面中，鼠标移动到【里程碑视图】按钮处悬停")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21024(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("非正式版本和正式版本的【版本时间】和【实际】TIP显示对应的【开始时间】和【结束数据】XXXXXXXX")  # 用例名称
    @allure.description("在【里程碑视图】中，鼠标移动到非正式版本和正式版本的【版本时间】和【实际】对应里程碑上悬停")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21025(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("【版本时间】弹窗中的【计划开始时间】和【计划结束时间】显示对应里程碑在任务详情设置的时间")  # 用例名称
    @allure.description("设置了【里程碑】、【TR】、【DCP】计划类型的任务中，保存了【计划开始时候】和【计划结束时间】==进入里程碑视图中，点击里程碑的【版本时间】，查看弹窗中的【计划开始时间】和【计划结束时间】显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21026(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("第一次进入【里程碑视图】中，对应里程碑的【版本时间】显示对应里程碑的【计划开始时间】/【计划结束时间】（受里程碑配置开始/结束时间控制显示）")  # 用例名称
    @allure.description("设置了【里程碑】、【TR】、【DCP】计划类型的任务中，保存了【计划开始时候】和【计划结束时间】==进入里程碑视图中查看对应里程碑的【版本时间】显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21027(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑视图中当前里程碑最新版本为【非正式版本】，【里程碑视图】弹窗左上角显示提示【编辑中，编辑完成后，可保存、可发布】")  # 用例名称
    @allure.description("当里程碑视图中当前里程碑最新版本为【非正式版本】，查看【里程碑视图】弹窗左上角显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21028(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑视图中当前里程碑最新版本为【正式版本（发布中）】，【里程碑视图】弹窗左上角显示提示【正在审批中，不可进行调整操作】")  # 用例名称
    @allure.description("当里程碑视图中当前里程碑最新版本为【正式版本（发布中）】，查看【里程碑视图】弹窗左上角显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21029(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑视图中当前里程碑最新版本为【正式版本（已发布）】，【里程碑视图】弹窗左上角显示提示【里程碑已审批通过，可进行调整操作】")  # 用例名称
    @allure.description("当里程碑视图中当前里程碑最新版本为【正式版本（已发布）】，查看【里程碑视图】弹窗左上角显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21030(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("【里程碑视图】弹窗列表中在最新版本显示当前日期的时间线，根据里程碑最新版本的【版本时间】显示在其中")  # 用例名称
    @allure.description("在里程碑视图中，查看当前日期的时间线")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21031(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("当前版本与上一正式版本【版本时间】进行对比，当【版本时间】有变化，则对应变化里程碑最新版本背景色显示为【浅红色】")  # 用例名称
    @allure.description("【里程碑视图】中，当前版本与上一正式版本进行对比，里程碑【版本时间】查看")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21032(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑视图中修改保存里程碑的【版本时间】中的【计划开始时间】/【计划结束时间】，同步到对应的WBS计划的【计划开始时间】/【计划结束时间】")  # 用例名称
    @allure.description("里程碑视图中修改保存里程碑的【版本时间】中的【计划开始时间】/【计划结束时间】==在对应的WBS计划的任务详情页中查看【计划开始时间】/【计划结束时间】")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21033(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("编辑里程碑的【版本时间】前，会把对应任务的【计划开始时间】和【计划结束时间】带入里程碑【版本时间】的弹窗中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21036(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("修改保存里程碑的【版本时间】的【计划开始时间】和【计划结束时间】会同步到对应任务的详情页和列表WBS中显示")  # 用例名称
    @allure.description("在里程碑视图中对里程碑【版本时间】进行修改保存，在对应里程碑任务的详情页和WBS查看显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21037(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("【版本时间】编辑保存后，配置中【以开始时间显示】，则只显示【计划开始时间】")  # 用例名称
    @allure.description("在里程碑视图中对里程碑【版本时间】进行修改保存，查看对应里程碑显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21038(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("【版本时间】编辑保存后，配置中【以结束时间显示】，则只显示【计划结束时间】")  # 用例名称
    @allure.description("在里程碑视图中对里程碑【版本时间】进行修改保存，查看对应里程碑显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21039(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("【计划开始时间】和【计划结束时间】被【置为不存在/】，【版本时间】的【计划开始时间】和【计划结束时间】显示为空")  # 用例名称
    @allure.description("编辑里程碑【版本时间】，将【计划开始时间】和【计划结束时间】，分别点击【置为不存在/】按钮，点击【保存】按钮==查看对应里程碑【版本时间】显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21040(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("新增一条非正式版本，会将上一个正式版本的所有里程碑的【计划开始时间】和【计划结束时间】带到当前非正式版本的【版本时间】中去")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21041(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("新增一条非正式版本，未点击保存，将【里程碑视图】弹窗关闭，再点击【里程碑视图】按钮，新增的非正式版本里程碑不显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21042(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("新增一条非正式版本，点击保存，将【里程碑视图】弹窗关闭，再点击【里程碑视图】按钮，新增的非正式版本里程碑显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21043(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("非正式版本有里程碑【版本时间】为空，点击保存后，保存成功")  # 用例名称
    @allure.description("在里程碑视图中，当前非正式版本中有里程碑【版本时间】为空，点击保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21044(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑视图中，当前非正式版本里程碑中存在【计划开始日期】/【计划结束日期】为空时，点击【发布】按钮，提示【存在里程碑的时间为空，请检查后发布】，并不打开发起页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21045(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("在发起流程后生成；【导入】、【导出】、【流程记录】、【新增】、【保存】、【发布】按钮可查看，可操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21082(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑流程在途流程时，WBS的里程碑的计划开始/结束时间，计划列表中任务的计划开始/结束时间，任务详情页中的计划开始/结束时间均无法编辑")  # 用例名称
    @allure.description("对里程碑视图的计划开始/结束时间，计划列表中任务的计划开始/结束时间，任务详情页中的计划开始/结束时间进行编辑")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21121(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑生成了正式版本后，如V1.0，WBS的里程碑的计划开始/结束时间，计划列表中任务的计划开始/结束时间，任务详情页中的计划开始/结束时间均无法编辑")  # 用例名称
    @allure.description("对里程碑视图的计划开始/结束时间，计划列表中任务的计划开始/结束时间，任务详情页中的计划开始/结束时间进行编辑")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21122(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑变更的审批流程若不通过（拒绝），里程碑的【计划开始/结束时间】显示上一个版本，并同步到对应的任务的列表和详情页显示")  # 用例名称
    @allure.description("查看里程碑视图的【计划开始/结束时间】显示==查看对应任务的列表和详情页显示的【计划开始/结束时间】显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21123(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("里程碑变更的审批流程若不通过（拒绝）且无没有历史版本，【计划开始/结束时间】不变化")  # 用例名称
    @allure.description("查看里程碑视图的【计划开始/结束时间】显示==查看对应任务的列表和详情页显示的【计划开始/结束时间】显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21124(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("'计划任务'详情页中的【实际开始时间】【实际结束时间】属性可编辑（任务状态不为【已完成】）")  # 用例名称
    @allure.description("选择计划任务，进入详情页，对【实际开始时间】【实际结束时间】进行编辑")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21125(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("任务状态更改为已经进行中或者评审中，将'系统的时间'写入到'实际开始时间中'，【实际开始时间】仍然可编辑")  # 用例名称
    @allure.description("任务状态更改为已经进行中或者评审中，查看对应任务的【实际开始时间】显示==编辑【实际开始时间】")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21126(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("任务状态更改为已经进行中或者评审中，【实际开始时间】不改变")  # 用例名称
    @allure.description("任务状态更改为已经进行中或者评审中，查看对应任务的【实际开始时间】显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21127(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("DCP任务，任务状态更改为【已完成】，【实际结束时间】获取的是结论为GO/GOwithrisk时的上会时间")  # 用例名称
    @allure.description("任务状态更改为【已完成】，查看对应任务的【实际结束时间】显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21128(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("非DCP任务，任务状态更改为【已完成】，'系统的时间'写入到'实际结束时间中'，且无法再进行编辑")  # 用例名称
    @allure.description("任务状态更改为【已完成】，查看对应任务的【实际结束时间】显示==对【实际结束时间】进行编辑")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21129(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("任务状态更改为【已完成】，【实际结束时间】不改变，且无法再进行编辑")  # 用例名称
    @allure.description("任务状态更改为【已完成】，查看对应任务的【实际结束时间】显示==对【实际结束时间】进行编辑")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21130(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("任务详情页中【实际开始时间】和【实际结束时间】字段无法编辑")  # 用例名称
    @allure.description("选择计划任务，进入任务详情页，对【实际开始时间】和【实际结束时间】进行编辑")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21131(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("'模块化IPD/基线IPD/非IPD'的里程碑功能的显示值按照配置文件进行取值")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21132(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑封板逻辑及wbs同步逻辑")  # 用户故事名称
    @allure.title("字典中按照配置文件中任务进行对应的实际取值配置，里程碑任务WBS中进行对照校验")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21133(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3351:
    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("里程碑视图中，当前非正式版本里程碑中所有【计划开始日期】/【计划结束日期】都存在值，点击【发布】按钮，成功打开发起页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21046(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("【项目经理】/【超管账号】点击【发布】，进入发起页面，发起页面的标题自动回显'[项目名]项目[正式版本号]里程碑发布申请'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21066(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("发起页面中【调整原因】带必填项标识")  # 用例名称
    @allure.description("在里程碑审批发起页面中查看【调整原因】字段标识")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21067(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("【调整原因】为空后【提交】，提示对应【调整原因】不能为空错误")  # 用例名称
    @allure.description("在里程碑审批发起页面中，不填写【调整原因】，点击【提交】")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21068(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("发起页面中，【基本信息】、【里程碑信息】、【附件】模块均默认展开")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21069(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("【基本信息】中的【标题】、【申请人】、【调整原因】字段均是可编辑的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21070(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("附件中可以上传文件，已上传的文件，可以点击下载文件，下载对应文件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21074(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("发起页面中的【里程碑信息】与【里程碑视图】中待发布的里程碑数据不一致，【发布】，提示【发布的里程碑与最新的里程碑不一致，请重新发布再提交！】")  # 用例名称
    @allure.description("发起页面中的【里程碑信息】与【里程碑视图】中待发布的里程碑数据不一致，点击【发布】按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21075(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("发起页面【申请部门】根据申请人自动带出")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21080(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("发起页面【申请日期】默认为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21081(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发起页面")  # 用户故事名称
    @allure.title("发起页面的【筛选框】，选择后，只显示已筛选的阶段对应的列；【附近】可上传/下载")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21083(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3352:
    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("里程碑视图中非正式版本里程碑成功发起流程后，发起人的直接领导，在【工作台】中【我的待办】TAB页中，存在相关审批流程节点")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21047(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接上级】审批通过后，发起人对应的二级领导（发起人直接领导的直接领导）在【工作台】中【我的待办】TAB页中，存在相关审批流程节点")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21048(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【二级领导】审批通过后，里程碑版本审批流程完成，结束后，发送邮件通知【发起人】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21049(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("当【直接领导】审批同意之前，【发起人】可以在【我的申请】TAB页下找到对应审批流程任务，点击进入，点击【撤回】按钮，撤回审批流程")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21050(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("审批流程【撤回】后，撤回的【里程碑版本】会同步到【申请人】的【我的申请】TAB页下")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21051(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("流程全部【通过】后，【流程状态】变更为【审批通过】，并邮件通知【发起人】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21052(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("流程中【直接领导】审批节点【拒绝】后，【流程状态】变更为【审批拒绝】，并邮件通知【发起人】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21053(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【里程碑发起】点击【提交】按钮后，同步到【申请人】的【直接领导】对应的【我的待办】TAB页下")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21054(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导审批】页面中存在【同意/拒绝/转交/加签】按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21055(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导审批】页面中点击【同意】按钮，流程扭转到下一个流程节点")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21056(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导审批】页面中点击【拒绝】按钮，流程审批结束，流程状态为【审批拒绝】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21057(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导审批】页面中点击【转交】按钮，选择【转交人】，转交成功后，同步到【转交人】的【我的待办】TAB页中，【直接领导】的审批任务消失")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21058(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导审批】页面中点击【加签】按钮，选择【加签人员】，【加签】成功后，【直接领导】审批通过后，还需【加签成员】审批通过后，再扭转到下一个流程节点")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21059(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【二级领导审批】页面中存在【同意/转交/回退/加签】按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21060(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【二级领导审批】页面中点击【同意】，流程审批节点全部通过，里程碑视图中的里程碑状态更新为【评审通过提示】，里程碑正式版本为【评审通过】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21061(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【二级领导审批】页面中点击【转交】按钮，选择【转交人】，转交成功后，同步到【转交人】的【我的待办】TAB页中，【二级领导】的审批任务消失")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21062(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【二级领导审批】页面中点击【回退】按钮，审批流程结束，【发起审批】退回到【申请人】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21063(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【二级领导审批】页面中【加签】成功后，【二级领导】审批通过后，还需【加签成员】审批通过后，")  # 用例名称
    @allure.description("【二级领导审批】页面中点击【加签】按钮，选择【加签人员】")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21064(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【发起的里程碑审批过程中】点击【撤回】/点击【拒绝】/点击【退回申请人】按钮后，对应审批的正式版本里程碑失效，由正式版本（审批中），还原为非正式版本，数据不变")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21065(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导】审核和【二级领导】审核单据中的【基本信息】模块【默认折叠】，不可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21084(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导】审核和【二级领导】审核单据中的【里程碑信息】模块【默认展示】，不可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21085(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导】审核和【二级领导】审核单据中的【里程碑信息】模块显示当前版本的及历史所有正式版本的里程碑信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21086(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导】审核和【二级领导】审核单据中的【里程碑信息】模块中，【里程碑版本】会显示对应版本的【TIP值】")  # 用例名称
    @allure.description("【直接领导】审核和【二级领导】审核单据中，鼠标移到到【里程碑版本】位置悬停")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21087(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导】审核和【二级领导】审核单据中的【里程碑信息】模块中，【导出】按钮，导出【里程碑信息】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21088(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导】审核和【二级领导】审核单据中，可以通过选择【阶段名称】筛选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21089(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("【直接领导】审核和【二级领导】审核单据中的【附件】模块，默认折叠不展示，不可以被编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21090(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("流程审批支持筛选及导出")  # 用例名称
    @allure.description("在审批页面的里程碑信息模块中点击筛选按钮，选择需要展示的阶段==点击导出按钮")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21119(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_直接领导审核二级领导审核")  # 用户故事名称
    @allure.title("流程审批附件不可编辑，默认折叠")  # 用例名称
    @allure.description("查看流程审批页面中的附件模块显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21120(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3350:
    @allure.story("计划_里程碑新里程碑视图_发布流程图")  # 用户故事名称
    @allure.title("提交审批流程成功后，扭转到工作台的流程任务，生成对应的流程编号，流程编号前缀为【PSFF】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21078(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发布流程图")  # 用户故事名称
    @allure.title("流程任务同步到【申请人】的【直接领导】下，对应的里程碑版本置为【审批中】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21079(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发布流程图")  # 用户故事名称
    @allure.title("流程审批通过后，对应流程任务状态置为【审批通过】状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21091(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发布流程图")  # 用户故事名称
    @allure.title("审批过程中【里程碑信息】不可编辑，计划开始/结束时间不会有改变")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21092(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发布流程图")  # 用户故事名称
    @allure.title("审批页面中【申请部门】根据申请人自动带出")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21093(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发布流程图")  # 用户故事名称
    @allure.title("审批页面中【申请日期】默认为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21094(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发布流程图")  # 用户故事名称
    @allure.title("审批页面中【筛选框】选择后，只显示已筛选的阶段对应的列")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21095(self, drivers):
        pass


    @allure.story("计划_里程碑新里程碑视图_发布流程图")  # 用户故事名称
    @allure.title("审批页面中【附件】中文件可下载")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21096(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3343:
    @allure.story("计划_里程碑里程碑视图调整")  # 用户故事名称
    @allure.title("流程审批里程碑信息不可编辑，默认展示")  # 用例名称
    @allure.description("查看流程审批页面中的里程碑信息模块显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21116(self, drivers):
        pass


    @allure.story("计划_里程碑里程碑视图调整")  # 用户故事名称
    @allure.title("里程碑信息显示当前版本的及历史所有正式版本的里程碑信息")  # 用例名称
    @allure.description("查看流程审批页面中的里程碑信息模块内容显示")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21117(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3312:
    @allure.story("计划_TR风险导入")  # 用户故事名称
    @allure.title("进入风险关系中，查看风险页面是否和原型图一致，所有字段是否都存在")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22368(self, drivers):
        pass


    @allure.story("计划_TR风险导入")  # 用户故事名称
    @allure.title("进入风险关系中，点击选取按钮，查看选取按钮是否可用")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22369(self, drivers):
        pass


    @allure.story("计划_TR风险导入")  # 用户故事名称
    @allure.title("进入风险关系中，点击新建，查看新建按钮是否可用")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22370(self, drivers):
        pass


    @allure.story("计划_TR风险导入")  # 用户故事名称
    @allure.title("进入风险关系中，点击新建，查看是否弹出新建页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22371(self, drivers):
        pass


    @allure.story("计划_TR风险导入")  # 用户故事名称
    @allure.title("进入风险关系中，点击新建，查看新建页面是否和原型图一致，所有字段都存在")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22372(self, drivers):
        pass


    @allure.story("计划_TR风险导入")  # 用户故事名称
    @allure.title("进入风险关系，点击新增，查看所有项都不进行填写，查看是否能提交成功，比填项风险点、风险等级、涉及维度、提出人、提出日期、目标时间是否给出必填提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22373(self, drivers):
        pass


    @allure.story("计划_TR风险导入")  # 用户故事名称
    @allure.title("进入风险关系，点击新增，所有内容都正确填写，点击保存关闭页面，查看任务中该条风险是否添加成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22374(self, drivers):
        pass


    @allure.story("计划_TR风险导入")  # 用户故事名称
    @allure.title("进入风险关系，点击新增，所有内容都正确填写，点击取消，查看任务中是否存在该条风险对象")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22375(self, drivers):
        pass


    @allure.story("计划_TR风险导入")  # 用户故事名称
    @allure.title("进入风险关系，点击新增，所有内容都正确填写，点击取消，取消后再次点击新建，查看页面中是否还保存上一次填写的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22376(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3317:
    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在项目中发起一个流程的任务，发起后，查看工作台中的流程任务tab页是否有该条流程信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22380(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("发起流程后，查看流程任务是否和原型图一致，包括标题XX项目TRx流程PQA预审、单据号、当前节点、状态、申请人、审批人、申请时间、到达时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22381(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，点击流程任务，查看是否弹出流程任务详情")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22382(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，点击流程任务，查看流程和任务中的信息是否可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22383(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，点击流程任务，查看下面的要素是否是TR任务的全部要素")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22384(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，点击流程任务，查看下面的要素进入要素详情页，是可编辑要素中的所有信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22385(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，点击流程任务，查看下面的要素进入要素详情页，查看是否可编辑交付物信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22386(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，点击一条状态为open的要素，点击变更驳回后，查看该条要素是否回到所属领域角色的待办中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22387(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，点击一条状态为open的要素，点击审核驳回后，查看该条要素是否回到所属领域角色的待办中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22388(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，点击一条状态为close的要素，点击变更驳回后，查看该条要素是否回到所属领域角色的待办中，状态是否为open")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22389(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，点击一条状态为close的要素，点击审核驳回后，查看该条要素是否回到所属领域角色的待办中，状态是否为open")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22390(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，其中有多条要素的状态都为open，点击同意，查看是否能提交成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22391(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，其中有多条要素的状态都为open，点击拒绝，查看是否能提交成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22392(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，其中一条要素的状态为open，点击同意，查看是否能提交成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22393(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，其中一条要素的状态为open，点击拒绝，查看是否能提交成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22394(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程，并且所有要素的状态都为close时，点击同意，查看是否能提交成功，我的待办中是否还存在该条数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22395(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程，并且所有要素的状态都为close时，点击拒绝，查看我的待办中是否还存在该条数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22396(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，进入该条流程任务，查看是否能问题和风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22397(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("在发起流程后，进入该条流程任务，新增了问题和风险，进入我的项目中进入该条任务，查看是否能看到在流程中新增的问题和风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22398(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("发起流程后，多个要素存在多个还没有互检或者自检完成的要素，点击催办，查看是否给相应的人员发送飞书邮件消息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22399(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("发起流程后发起了催办消息，查看发送到飞书邮件消息是否格式正确收件人要素涉及的角色标题XX项目TRx要素催办内容您好xx项目的TRx要素需要及时处理，请在IPM待办中尽快完成")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22400(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("点击PDT自检节点待办,弹出流程任务详情，流程和任务信息是否不能编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23679(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT自检节点待办,要素关系中，仅显示当前角色是要素的所属领域角色的要素")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23680(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT自检节点待办,要素页面仅可编辑当前角色行的检查结果、检查备注列，仅可只读交付物关系中的交付物")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23681(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT自检节点待办,当前角色完成所有要素检查结果、有交付物的必须完成交付物上传，且每个交付物必须要有两个文件，其中一个名称必须包括内审表，才能同意该流程节点")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23682(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT自检节点待办,某领域的人员提交互评后，该领域的要素不能再编辑，除非PQA驳回要素，才能编辑，该流程节点所有人员同意才能完成该流程节点")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23683(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT自检节点待办,点击拒绝，结束流程")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23684(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT自检节点待办,结束的流程活动，进入到我的已办")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23685(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT自检节点待办,自检过程中，互评角色可添加问题和风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23686(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT互评节点待办,在IPM流程任务中，我的待办，可查看流程任务")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23687(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT互评节点待办,流程和任务信息只读")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23688(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT互评节点待办,要素关系中，仅显示当前角色是要素的互评角色的要素")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23689(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT互评节点待办,要素页面仅可编辑当前角色行的检查结果、检查备注列，仅可只读交付物关系中的交付物")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23690(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT互评节点待办,当前角色完成所有要素检查结果才能同意该流程节点")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23691(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT互评节点待办,某领域的人员提交互评后，该领域的要素不能再编辑，除非PQA驳回要素，才能编辑，该流程节点所有人员同意才能完成该流程节点")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23692(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT互评节点待办,点击拒绝，结束流程")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23693(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT互评节点待办,结束的流程活动，进入到我的已办")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23694(self, drivers):
        pass


    @allure.story("计划_TRPQA审核节点")  # 用户故事名称
    @allure.title("评审流程——PDT互评节点待办,自检过程中，互评角色可添加问题和风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23695(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3318:
    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("进入IPM流程任务中，我的已办，查看是否可以查看流程任务信息，XX项目TRx流程PQA发布结果")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22401(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，并且流程完成点击流程任务，查看是否弹出流程任务详情")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22402(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，点击流程任务，查看流程和任务中的信息是否可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22403(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，流程完成后，查看下面的要素是否是TR任务的全部要素")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22404(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，流程完成后，查看下面的要素进入要素详情页，是可编辑要素中的所有信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22405(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，PQA角色查看是否能新增、编辑结论关系中的结论对象")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22406(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，到流程结束前一步，当结论为空时，状态为已发布，点击同意，查看是否能提交成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22407(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，到流程结束前一步，当结论有值时，状态为编辑中，点击同意，查看是否能提交成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22408(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，到流程结束前一步，当结论有值时，状态为已发布，点击同意，查看是否能提交成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22409(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，到流程结束前一步，当结论有值时，状态为已发布，点击同意，同意后该条流程任务是否到我的已办中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22410(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，进入该条流程任务，查看是否能问题和风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22411(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程后，进入该条流程任务，新增了问题和风险，进入我的项目中进入该条任务，查看是否能看到在流程中新增的问题和风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22412(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起流程，并且所有要素的状态都为close时，点击拒绝，查看我的待办中是否还存在该条数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22413(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中点击进行结论关系，查看右上角是否存在'分发'按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22414(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起时不选择结论，且状态为编辑中，发起流程后，查看点击'分发'按钮，是否能进行分发")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22415(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起时选择结论，而状态为编辑中，发起流程后，查看点击'分发'按钮，是否能进行分发")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22416(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在发起时不选择结论，而状态为已发布，发起流程后，查看点击'分发'按钮，是否能进行分发")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22417(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程后，编辑结论为空，查看点击'分发'按钮，是否能进行分发")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22418(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程，编辑状态为编辑中，查看点击'分发'按钮，是否能进行分发")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22419(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为已发布，点击发布，查看是否弹出分发确认页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22420(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为已发布，点击发布，查看弹出分发确认页面是否和原型图一致，存在'接收人、抄送人、内容、主题'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22421(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为已发布，点击发布，查看接收人是否所属项目的角色对应人员，包括LPDT、PM、研发代表、采购代表、质量代表、制造代表、计划代表、销管代表、PQA、GTM代表、财务代表；")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22422(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为已发布，点击发布，查看抄送人是否可以输入并且可以全局搜索人员并选择")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22423(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为已发布，点击发布，查看内容的默认信息是否为XX项目的TRn，结论为y")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22424(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为已发布，点击发布，查看内容是否可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22425(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为已发布，点击发布，查看主题默认信息是否为XX项目TRn结论")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22426(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为已发布，点击发布，查看主题是否可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22427(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为已发布，点击发布，其他信息正确填写，点击发布，查看接收人和抄送人是否都能收到邮件和飞书")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22428(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为已发布，点击发布，其他信息正确填写，点击发布，查看状态是否还是已发布")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22429(self, drivers):
        pass


    @allure.story("计划_TRPQA发布结论节点")  # 用户故事名称
    @allure.title("在流程中结论存在且状态为编辑中，点击发布，其他信息正确填写，点击发布，发布后，结论状态是否变为已发布")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22430(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3315:
    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("查看在IPM工作台中，我的检查中是否包含了相应的待办的要素，包括a.当前角色是领域自检角色，b.当前角色是互评角色")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22432(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("查看在IPM工作台中，我的检查中点击其中一条要素，查看是否弹出要素页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22433(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("发起时发起一条含有一条交付物的要素，点击该条要素，点击该条交付物，查看是否能直接点击打开交付物")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22434(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("发起时发起一条含有多条交付物的要素，点击该条要素，点击该条交付物，查看是否能直接点击打开交付物")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22435(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("发起时发起一条含有多条交付物的要素，点击该条要素，将鼠标移动到交付件上，查看交付件表格旁自动显示交付件清单")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22436(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("发起时发起一条含有多条交付物的要素，点击该条要素，将鼠标移动到交付件上，点击交付件表格旁自动显示交付件清单，点击其中一条交付物，查看是否能打开对应的交付物")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22437(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("发起流程后，进入该条要素，如果当前角色是自检角色，查看是否能编辑要素中的所有信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22438(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("在系统管理，映射管理，TR映射管理下，基线、模块化模板中，把文件放交付物中,查看是否可以添加成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23696(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("TR任务选择TR阶段时候，检查是否自动将模板的文件带入TR任务的要素中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23697(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("要素映射的交付物，自检提交时校验交付物是否有文件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23698(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("要素自检时，查看检查自检与互评结果，是否存在不涉及")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23699(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("新增要素时只加交付物不加文件，要素自检时如果领域要素自检结果为'不涉及'，验证对应的交付件是否不检查")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23700(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("TR要素下载功能优化，项目经理PQALPDT9大代表，可在项目任务的TRTab页中下载交付物文件的权限")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23701(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("TR要素下载功能优化，项目经理PQALPDT9大代表，可在TR看板Tab页中下载交付物文件的权限")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23702(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("TR要素下载功能优化，项目经理PQALPDT9大代表，可在TR任务流程中Tab页中下载交付物文件的权限")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23703(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("TR要素下载功能优化，登录其他人员查看没有下载权限")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23704(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("TR要素下载功能优化，下载文件名要素名交付物名文件名")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23705(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("TR要素下载功能优化，其中长度大于20的要素名称截取前后各10个字符（50个字截取110字、4150字）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23706(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("TR要素下载功能优化，交付物文件名重名是否能全部下载")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23707(self, drivers):
        pass


    @allure.story("计划_TR要素自检节点")  # 用户故事名称
    @allure.title("工作台中，我的待办改为我的TR")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23720(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3316:
    @allure.story("计划_TR要素互评节点")  # 用户故事名称
    @allure.title("发起流程后，进入该条要素，如果当前角色也是自检角色也是互评角色，且还没有进行自检，查看该角色能编辑互评角色行的结果和检查备注")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22439(self, drivers):
        pass


    @allure.story("计划_TR要素互评节点")  # 用户故事名称
    @allure.title("发起流程后，进入该条要素，如果当前角色也是自检角色也是互评角色，点击提交互评，查看是否能提交成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22440(self, drivers):
        pass


    @allure.story("计划_TR要素互评节点")  # 用户故事名称
    @allure.title("发起流程后，进入该条要素，如果当前角色也是自检角色也是互评角色，自检角色点击提交互评，到了该角色的互评节点，选择了检查结果后，点击'提交PQA审批'，查看该条要素是否还存在我的已办中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22441(self, drivers):
        pass


    @allure.story("计划_TR要素互评节点")  # 用户故事名称
    @allure.title("发起流程后，进入该条要素，如果当前角色也是自检角色也是互评角色，自检已经完成，互检也已经完成，查看是否有'提交互评'按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22442(self, drivers):
        pass


    @allure.story("计划_TR要素互评节点")  # 用户故事名称
    @allure.title("发起流程后，进入该条要素，如果当前角色也是自检角色也是互评角色，自检已经完成，点击提交互评后，查看要素中的交付物是否可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22443(self, drivers):
        pass


    @allure.story("计划_TR要素互评节点")  # 用户故事名称
    @allure.title("发起流程后，进入该条要素，要素中的自检和互评全部完成后，该条要素是否从我的待办中移动到我的已办中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22444(self, drivers):
        pass


    @allure.story("计划_TR要素互评节点")  # 用户故事名称
    @allure.title("TR任务流程走到互评，使用两个不同的领域的账号同时进行提交，查看互评提交的内容和任务的状态是否正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23733(self, drivers):
        pass


    @allure.story("计划_TR要素互评节点")  # 用户故事名称
    @allure.title("TR任务流程走到互评，其中一个人转交该领域下的其他人，两个人同时进行提交，查看互评提交的内容和任务的状态是否正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23734(self, drivers):
        pass


    @allure.story("计划_TR要素互评节点")  # 用户故事名称
    @allure.title("TR任务流程走到互评，两个人转交该领域下的其他人，两个人同时进行提交，查看互评提交的内容和任务的状态是否正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23735(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3313:
    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("登录账号为责任人，在我的工作台中的问题中，查看是否存在待办问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22446(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("登录账号为责任人，点击在某一行的问题，查看是否弹出问题的页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22447(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("登录账号为PQA的角色且是责任人，点击某一行的问题，查看是否能够进行检出并且仅能够编辑进度和文件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22448(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("登录账号为PQA的角色且是责任人，在我的工作台中是否会出现两条相同的问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22449(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("登录账号为责任人，进入项目中，状态为close的问题，是否还会出现在项目中的问题中，是否会有提交按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22450(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("登录账号为PQA，进入项目中，已经提交成功后，状态改为close，查看是否会该条问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22451(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("点击进入了问题详情页中的页面，点击提交，查看提交后是否可关闭当前问题详情页")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22452(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在我的工作台已经提交成功过的问题，再次进入查看问题的详情页，查看详情页和列表中的提交按钮是否可点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22453(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("已经提交成功过的问题，再次进入查看问题的详情页，查看进度和文件是否可以进行编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22454(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在项目中的问题已经提交成功过的问题，再次进入查看问题的详情页，查看详情页和列表中的提交按钮是否可点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22455(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在我的待办中点击一条问题，直接点击提交按钮，查看是否弹出确认提交对话框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22456(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("登录账号为责任人，在项目问题下中点击一条问题，直接点击提交按钮，查看是否弹出确认提交对话框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22457(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在我的待办中点击一条问题待办，在确认提交对话框中点了确认之后，是否提交问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22458(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在我的待办中点击一条问题待办，在确认提交对话框中点了取消之后，是否能提交问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22459(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在项目中的问题下中点击一条问题待办，在确认提交对话框中点了确认之后，是否提交问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22460(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在项目中的一条问题点击一条问题待办，在确认提交对话框中点了取消之后，是否能提交问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22461(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("又是PQA又是责任人，在我的待办中点击了提交问题，查看我的待办中是否还存在待办的问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22462(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("又是PQA又是责任人，在项目中的问题下点击了提交问题，查看项目中的问题下是否还存在待办的问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22463(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("是PQA又是责任人，在我的待办中点击了确认完成的按钮，查看是否还可以点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22464(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("是PQA又是责任人，在项目中的问题下中点击了确认完成的按钮，查看是否还可以点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22465(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("是PQA又是责任人，在我的待办中点击了确认完成的按钮后，在项目下的问题和详情中是否还存在该按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22466(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("是PQA又是责任人，在我项目中的问题下点击了确认完成的按钮后，在项目下的问题和详情中是否还存在该按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22467(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("是PQA角色，在项目中的待办问题中，点击确认完成按钮后是否弹出确认框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22468(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("是PQA角色，在项目中的待办问题中，点击确认完成后，点击确认，查看问题状态是否有ongoing变为close")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22469(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("是PQA角色，在项目中的待办问题中，点击确认完成后，点击取消，查看问题状态是否有ongoing变为close")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22470(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("是PQA角色，在项目中的待办问题中，点击确认完成以后，查看工作台的问题列表和详情，是否还会存在提交、确认完成、驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22471(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("是PQA角色，在项目中的待办问题中已经完成得问题，是否存在重新开启按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22472(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("只是PQA角色，在重新开启后，查看是否能进行编辑进度和文件，查看是否有提交按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22473(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("只是责任人，在项目中的待办问题中已经完成得问题，是否存在重新开启按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22474(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("只是责任人，在PQA角色进行重新开启了问题，查看责任人是否能编辑进度和文件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22475(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在项目中的待办问题中已经完成的问题重新开启，开启后状态是否变为ongoing")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22476(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在项目中的待办将待办的问题中点击确认完成，完成后的问题到了我的已办，查看该条问题是否存在驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22477(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("为PQA角色，在项目中的问题中，点击驳回，驳回弹出确认框，点击确认后，查看该条问题是否不存在确认完成按钮和驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22478(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("登录为责任人，在项目中的问题中，点击驳回，驳回弹出确认框，点击确认后，查看该条问题是否不存在确认完成按钮和驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22479(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在我的工作台的待办问题中已经完成的问题重新开启，开启后状态是否变为ongoing")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22480(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在我的工作台的待办将待办的问题中点击确认完成，完成后的问题到了我的已办，查看该条问题是否存在驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22481(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("为PQA角色，在我的工作台的待办问题中，点击驳回，驳回弹出确认框，点击确认后，查看该条问题是否不存在确认完成按钮和驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22482(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("登录为责任人，在我的工作台的待办问题中，点击驳回，驳回弹出确认框，点击确认后，查看该条问题是否不存在确认完成按钮和驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22483(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("登录为责任人，在项目中的问题中，点击驳回，驳回弹出确认框，点击确认后，被驳回的问题到责任人中，责任人是否可编辑进度和文件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22484(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("又是PQA和责任人，在项目中的问题中，点击驳回，驳回弹出确认框，点击确认后，被驳回的问题是否出现提交按钮，是否可编辑进度和文件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22485(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("在已经确认完成的问题中查看实际关闭时间是否为确认完成时的时间，状态是否为close")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22486(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("又是PQA又是责任人又是创建人，在待办问题中，查看是否能够检出")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22487(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("又是PQA又是责任人又是创建人，在待办问题中，进行检出后，是否可以编辑所有的信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22488(self, drivers):
        pass


    @allure.story("计划_TR问题创建")  # 用户故事名称
    @allure.title("又是PQA又是责任人又是创建人，在待办问题中，点击提交后，查看是否还是该条问题出现确认完成和驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22489(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3311:
    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("登录账号为责任人，在我的工作台中的风险中，查看是否存在待办风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22494(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("登录账号为责任人，点击在某一行的风险，查看是否弹出风险的页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22495(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("登录账号为PQA的角色且是责任人，点击某一行的风险，查看是否能够进行检出并且仅能够编辑措施和文件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22496(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("登录账号为PQA的角色且是责任人，在我的工作台中是否会出现两条相同的风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22497(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("登录账号为责任人，进入项目中，状态为close的风险，是否还会出现在项目中的风险中，是否会有提交按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22498(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("登录账号为PQA，进入项目中，已经提交成功后，状态改为close，查看是否会该条风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22499(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("点击进入了风险详情页中的页面，点击提交，查看提交后是否可关闭当前风险详情页")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22500(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在我的工作台已经提交成功过的风险，再次进入查看风险的详情页，查看详情页和列表中的提交按钮是否可点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22501(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("已经提交成功过的风险，再次进入查看风险的详情页，查看措施和文件是否可以进行编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22502(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在项目中的风险已经提交成功过的风险，再次进入查看风险的详情页，查看详情页和列表中的提交按钮是否可点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22503(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在我的待办中点击一条风险，直接点击提交按钮，查看是否弹出确认提交对话框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22504(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("登录账号为责任人，在项目风险下中点击一条风险，直接点击提交按钮，查看是否弹出确认提交对话框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22505(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在我的待办中点击一条风险待办，在确认提交对话框中点了确认之后，是否提交风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22506(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在我的待办中点击一条风险待办，在确认提交对话框中点了取消之后，是否能提交风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22507(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在项目中的风险下中点击一条风险待办，在确认提交对话框中点了确认之后，是否提交风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22508(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在项目中的一条风险点击一条风险待办，在确认提交对话框中点了取消之后，是否能提交风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22509(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("又是PQA又是责任人，在我的待办中点击了提交风险，查看我的待办中是否还存在待办的风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22510(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("又是PQA又是责任人，在项目中的风险下点击了提交风险，查看项目中的风险下是否还存在待办的风险")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22511(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("是PQA又是责任人，在我的待办中点击了确认完成的按钮，查看是否还可以点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22512(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("是PQA又是责任人，在项目中的风险下中点击了确认完成的按钮，查看是否还可以点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22513(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("是PQA又是责任人，在我的待办中点击了确认完成的按钮后，在项目下的风险和详情中是否还存在该按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22514(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("是PQA又是责任人，在我项目中的风险下点击了确认完成的按钮后，在项目下的风险和详情中是否还存在该按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22515(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("是PQA角色，在项目中的待办风险中，点击确认完成按钮后是否弹出确认框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22516(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("是PQA角色，在项目中的待办风险中，点击确认完成后，点击确认，查看风险状态是否有ongoing变为close")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22517(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("是PQA角色，在项目中的待办风险中，点击确认完成后，点击取消，查看风险状态是否有ongoing变为close")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22518(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("是PQA角色，在项目中的待办风险中，点击确认完成以后，查看工作台的风险列表和详情，是否还会存在提交、确认完成、驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22519(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("是PQA角色，在项目中的待办风险中已经完成得风险，是否存在重新开启按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22520(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("只是PQA角色，在重新开启后，查看是否能进行编辑措施和文件，查看是否有提交按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22521(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("只是责任人，在项目中的待办风险中已经完成得风险，是否存在重新开启按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22522(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("只是责任人，在PQA角色进行重新开启了风险，查看责任人是否能编辑措施和文件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22523(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在项目中的待办风险中已经完成的风险重新开启，开启后状态是否变为ongoing")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22524(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在项目中的待办将待办的风险中点击确认完成，完成后的风险到了我的已办，查看该条风险是否存在驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22525(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("为PQA角色，在项目中的风险中，点击驳回，驳回弹出确认框，点击确认后，查看该条风险是否不存在确认完成按钮和驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22526(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("登录为责任人，在项目中的风险中，点击驳回，驳回弹出确认框，点击确认后，查看该条风险是否不存在确认完成按钮和驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22527(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在我的工作台的待办风险中已经完成的风险重新开启，开启后状态是否变为ongoing")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22528(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在我的工作台的待办将待办的风险中点击确认完成，完成后的风险到了我的已办，查看该条风险是否存在驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22529(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("为PQA角色，在我的工作台的待办风险中，点击驳回，驳回弹出确认框，点击确认后，查看该条风险是否不存在确认完成按钮和驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22530(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("登录为责任人，在我的工作台的待办风险中，点击驳回，驳回弹出确认框，点击确认后，查看该条风险是否不存在确认完成按钮和驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22531(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("登录为责任人，在项目中的风险中，点击驳回，驳回弹出确认框，点击确认后，被驳回的风险到责任人中，责任人是否可编辑措施和文件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22532(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("又是PQA和责任人，在项目中的风险中，点击驳回，驳回弹出确认框，点击确认后，被驳回的风险是否出现提交按钮，是否可编辑措施和文件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22533(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("在已经确认完成的风险中查看实际关闭时间是否为确认完成时的时间，状态是否为close")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22534(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("又是PQA又是责任人又是创建人，在待办风险中，查看是否能够检出")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22535(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("又是PQA又是责任人又是创建人，在待办风险中，进行检出后，是否可以编辑所有的信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22536(self, drivers):
        pass


    @allure.story("计划_TR风险创建")  # 用户故事名称
    @allure.title("又是PQA又是责任人又是创建人，在待办风险中，点击提交后，查看是否还是该条风险出现确认完成和驳回按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22537(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3328:
    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("在DCPPMToffice反馈跟踪问题节点进行驳回交付物，进入交付物待办，查看交付物是否存在查看问题按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22538(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("在DCPPMToffice反馈跟踪问题节点进行驳回交付物，进入交付物待办，点击查看问题按钮，查看页面是否跳转到当前流程任务页面，并且直接能定位到问题TAB页")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22539(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("在上会节点之前，LPDT已办节点进入我的已办，查看已办流程下问题TAB页是否能添加问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22540(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("在上会节点之前，PQA已办节点进入我的已办，查看已办流程下问题TAB页是否能添加问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22541(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("在上会节点之前，PMToffice已办节点进入我的已办，查看已办流程下问题TAB页是否能添加问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22542(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("在上会节点之前，PMT区域组长已办节点进入我的已办，查看已办流程下问题TAB页是否能添加问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22543(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("在上会节点之后，LPDT、PQA、PMToffice、PMT区域组长进入我的已办，查看个角色已办流程下问题TAB页中是否还能添加问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22544(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("LPDT提交后，查看是否生成三个待办数据，PQA、PMToffice、PMT区域组长的待办")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22545(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("LPDT提交后，查看PMT区域组长是否是自动提交")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22546(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("DCP流程中，交付物被PMToffice反馈跟踪法问题节点驳回，查看LPDT是否有交付物待办")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23652(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("LPDT提交交付物，接收人PMToffice内审、PQA、如果有PMT区域组长，则发送PMT区域组长，查看接收人是否有交付物待办")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23653(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("所有角色完成审核后，接收人PMToffice，查看接收人是否有交付物待办")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23654(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("查看在交付物待办右上角加'查看问题'按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23655(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("点击'查看问题'，查看是否弹出该任务各自的已办的问题Tab页")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23656(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("在上会节点前，查看LPDT、PQA、PMToffice、PMT区域组长是否都允许在已办流程的问题tab页下添加问题")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23657(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("PQA、PMToffice内审、PMT区域组长（自动提交，不做强制等待）收到交付物待办，提交或驳回，提交后到PMToffice，驳回后到LPDT")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23658(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("提交到PMToffice后，PMToffice在交付物待办中，查看是否可以提交或拒绝")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23659(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("PMToffice在交付物待办提交后，在流程任务上，点击同意，查看是否成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23660(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice汇总反馈跟踪问题")  # 用户故事名称
    @allure.title("PMToffice在交付物待办未提交后，点击同意，查看是否有失败提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23661(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3322:
    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("进入项目进行创建DCP任务，预约成功后发起，查看发起页面是否和原型图一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22547(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，点击进行选取，查看是否弹出选取页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22548(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，点击进行选取，查看选取页面中所有的数据是否为该DCP任务责任人所有项目下该责任人所有的DCP任务")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22549(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，点击进行选取，查看在流程中的DCP任务是否能选取到")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22550(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，点击进行选取，查看已经走完流程并且结论值为GO、gowithrisk的DCP任务是否能进行选取")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22551(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，点击进行选取，查看已经走完流程并且结论值为非GO、gowithrisk的DCP任务是否能进行选取")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22552(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，选取后的多个DCP任务，点击发起流程，查看是否会弹出确认框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22553(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，选取多个DCP任务后，点击发起流程，同意强制刷新到关联中的DCP任务，查看是否所有的DCP任务是否是同样的问题和交付物")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22554(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，选取多个DCP任务后，点击发起流程，同意强制刷新到关联中的DCP任务，查看被选取的所有DCP任务中交付物的待办和问题的待办是否还存在")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22555(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，选取多个DCP任务后，点击发起流程，同意强制刷新到关联中的DCP任务，发起流程后，查看待办数据是否存在多条")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22556(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，选取多个DCP任务后，重新创建一个DCP任务选取刚刚选取过的任务，点击发起流程，查看流程是否能发起成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22557(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("在确认页面中，选取多个DCP任务后，重新创建一个DCP任务选取刚刚选取过的任务，点击发起流程，发起后又将第一个DCP任务点击发起，查看是否能发起成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22558(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("选取多个DCP任务后进行发起流程，流程发起后，查看是否所有被选取的DCP任务也会收到相应的流程待办")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22559(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("进行选取DCP任务后，将流程发起，发起后在其中一个项目中将问题提交，提交后，查看其他项目下问题是否还能被提交")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22560(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("进行选取DCP任务后，将流程发起后，在PMToffice汇总反馈跟踪问题节点，将交付物进行驳回，查看所有项目的LPDT是否能收到待办")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22561(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("进行选取了DCP任务后将流程发起后，到最后一个节点创建了结论，查看其他选取的交付物，是否是相同的结论")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22562(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("进行选取了DCP任务发起流程后，到最后结论值为空，再创建任务选中该任务，查看问题结论是否为完成流程后的问题和结论")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22563(self, drivers):
        pass


    @allure.story("计划_DCP任务发起")  # 用户故事名称
    @allure.title("进行关联DCP任务后，将确认页面关闭，再进入进行发起，查看确认页面是否还存在刚刚关联过的DCP任务")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22564(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3287:
    @allure.story("计划任务")  # 用户故事名称
    @allure.title("点击项目，点击任务，点击查看，任务类型选择'TR任务'，选择任务阶段，查看是否自动带出要素")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22645(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("点击项目，点击任务，点击查看，任务类型选择'TR任务'，选择任务阶段，如果切换选择TR阶段，提醒'是否选用新的阶段，并清除已选要素？'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22658(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("点击项目，点击任务，点击查看，任务类型选择'TR任务'，选择任务阶段，切换选择TR阶段，如果选择是，移除该任务已有关联的要素关系，并且按新TR阶段，加载要素")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22659(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("点击项目，点击任务，点击查看，任务类型选择'TR任务'，选择任务阶段，切换选择TR阶段，如果否，退回原TR阶段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22660(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("任务通用流程，申请人撤回任务后，任务的状态更改为进行中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23644(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("任务撤回后，任务的数据能够重新编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23645(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("流程任务点击重新提交，任务的状态更改为评审中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23646(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("普通用户不能编辑、发起任务")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23647(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("任务发起后任何人不可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23648(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("责任人（系统角色中的所有者）可编辑任务")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23649(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("创建者（系统角色中的创建者）可编辑任务")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23650(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("汇总责任人权限（父子任务）可编辑任务")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23651(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("查看历史IPD模块化、基线项目团队数据在PMToffice角色是否自动增加pmtoffice用户")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23662(self, drivers):
        pass


    @allure.story("计划任务")  # 用户故事名称
    @allure.title("新增项目自动有用户")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23663(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3299:
    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("查看项目任务是否有按钮'发起评审'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23664(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("查看该TR任务要素所属领域，查看是否有自检")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23665(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("点击发起评审，查看不存在自检，是否提示'XX要素的角色未配置！'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23666(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("要素自检添加领域角色，查看该TR任务的项目团队成员管理，是否有该角色成员")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23667(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("新增要素，添加自检所属领域角色，进入评审流程确认页面，点击'发起流程'，则发起并关闭确认页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23668(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("查看审批流程节点是否包括PDT提交自检、PDT互评、PQA审核、PQA发布结果")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23669(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("PDT提交自检，同意后，查看该流程节点是否完成")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23670(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("PDT提交自检，拒绝后，查看该流程是否结束")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23671(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("PDT互评，同意后，查看该流程节点是否完成")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23672(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("PDT互评，拒绝后，查看该流程是否结束")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23673(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("PQA审核，同意后，查看该流程节点是否完成")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23674(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("PQA审核，拒绝后，查看该流程是否结束")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23675(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("PQA发布结果，同意后，查看该流程节点是否完成")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23676(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("PQA发布结果，拒绝后，查看该流程是否结束")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23677(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("在TR流程任务中，查看我的待办是否有该流程任务")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23678(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("在我的检查、风险、问题、交付物中，如果该待办已打开，且该待办已经更新，则提示该待办已更新，并自动刷新打开的该待办")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23711(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR流程发起后，在任务页面，要素中点击'下载进度'按钮，下载当前状态该TR下要素的自检互评进度表格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23712(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR流程发起后，TR看板页面，要素中点击'下载进度'按钮，下载当前状态该TR下要素的自检互评进度表格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23713(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR流程发起后，流程中的页面，要素中点击'下载进度'按钮，下载当前状态该TR下要素的自检互评进度表格")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23714(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR要素自检、互评状况清单下载，打开EXCLE，查看颜色，已评为绿色，未评为红色")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23715(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR要素自检、互评状况清单下载，打开EXCLE，列出所属项目、TR阶段、要素名称、指标统计说明、自检领域、自检结果、互评结果、互评人员、互评结果、备注，自检人员名称工号，以自检人员为一行")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23716(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR要素自检、互评状况清单下载，打开EXCLE，查看下载内容正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23717(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR要素自检、互评状况清单下载，自检两个人时，未自检时显示两个人，已经自检显示已经自检的一个人")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23718(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("待办的名称（TR、DCP、问题、风险、交付物）颜色改为蓝色，全部改成蓝色")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23721(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("待办的名称（TR、DCP、问题、风险、交付物）点击蓝色字，查看是否可以进入要素待办页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23722(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR看板多个要素多个交付物下载")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23725(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR看板一个要素一个交付物下载")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23726(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("要素状态为进行中时要素下载")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23727(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("要素状态为评审中时要素下载")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23728(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("要素状态为已完成时要素下载")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23729(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("要素状态为评审中自检时删掉交付物再上传后要素下载")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23730(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR任务要素中交付物下载，切换账号，PQA能下，普通人不能下")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23731(self, drivers):
        pass


    @allure.story("计划_TR任务发起")  # 用户故事名称
    @allure.title("TR任务要素中交付物下载，只有自检没有互评是否报错")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23732(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3331:
    @allure.story("计划_DCPPMToffice发布结果")  # 用户故事名称
    @allure.title("在DCP流程中，PMToffice发布结果节点，新增结论，点击同意，查看流程是否结束")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23708(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice发布结果")  # 用户故事名称
    @allure.title("TR流程发布结果节点，新增结论，点击发布，点击同意，查看流程是否结束")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23709(self, drivers):
        pass


    @allure.story("计划_DCPPMToffice发布结果")  # 用户故事名称
    @allure.title("在DCP流程中，PMToffice发布结果节点，没有结论，点击同意，查看是否同意失败")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23710(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3326:
    @allure.story("计划_DCPPQA审核节点")  # 用户故事名称
    @allure.title("PQA驳回后检查按钮是否可以正常提交互评")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23736(self, drivers):
        pass


    @allure.story("计划_DCPPQA审核节点")  # 用户故事名称
    @allure.title("正常自检互评后，看PQA审核是否能正常审批")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23737(self, drivers):
        pass


    @allure.story("计划_DCPPQA审核节点")  # 用户故事名称
    @allure.title("PQA驳回后不自检互评，检查PQA审核是否可以审批，应该不可以审批")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23738(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3261:
    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("编辑项目单击项目卡片视图，选择编辑，进入项目编辑页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23914(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("编辑项目卡片显示视图切换到表格显示视图，点击操作下的修改按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23915(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("编辑项目先进入项目查看页面，再点击编辑按钮，查看转换为编辑页面状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23916(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目名称单行文本，必填，字符长度可在视图上做限制")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23917(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目名称可编辑，产品项目名称是项目名和主板名合成的，技术项目名称是与项目名保持一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23918(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目分类下拉文本，单选，必填，字符长度50，数据字典中获取")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23919(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目编号不可编辑，创建项目自动生成，8位日期3位流水")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23920(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目状态初始拿项目对象绑定的生命周期模板的初始状态，初始状态下不可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23921(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目状态不同项目初始状态不同")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23922(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目状态项目启动后，项目状态可编辑，状态根据生命周期状态扭转")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23923(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("计划开始/结束时间项目计划开始结束时间，可在视图上设置是否可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23924(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("实际开始时间/实际结束时间项目的实际开始结束时间，在视图上可设置是否可编辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23925(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目定级下拉文本，单选，数据字典里获取")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23926(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目描述多行文本，字符长度1000")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23927(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("所属领域下拉单选，可编辑、非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23928(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目状况下拉单选，可编辑、非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23929(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("是否年度规划下拉单选，可编辑，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23930(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目阶段下拉单选，可编辑，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23931(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("预算总金额输入框，字符长度50")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23932(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("延期描述可编辑、非必填项、字符长度1000")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23933(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目名可编辑，必填项，字符长度50")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23934(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("主板名可编辑，字符长度50，产品项目中必填，其他项目非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23935(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("上市时间可编辑，必填项，时间选择框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23936(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("系列可编辑，字符长度50")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23937(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("品牌必填项，下拉单选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23938(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("平台必填项，字符长度50")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23939(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("平台编码下拉单选，必填项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23940(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("研发模式必填项、下拉单选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23941(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("机型分类必填项，下拉单选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23942(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("基线名称非必填项，字符长度1000")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23943(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("定级系数非必填项，字符长度200")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23944(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("SAP订单号必填项，SAP返回的单号")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23945(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("产品使命非必填项，字符长度1000")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23946(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("专项类型非必填、下拉单选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23947(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("责任领域非必填，下拉单选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23948(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("产品项目产品项目保存存成后，根据传输的信息，SAP系统先返回SAP订单号，在同步项目信息给OA系统")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23949(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("编辑产品项目编辑产品项目信息后，SAP订单号不能更改，但同步给OA系统的信息如有改动会同步更新到OA系统")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23950(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("技术项目技术项目保存后，根据传输的信息，SAP系统先返回SAP订单号，在同步项目信息给OA系统")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23951(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("编辑技术项目编辑技术项目信息后，SAP订单号不能更改，但同步给OA系统的信息如有改动会同步更新到OA系统")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23952(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目启动初始状态不可编辑，启动项目后，可编辑项目状态，状态根据生命周期状态规则扭转")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23956(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目启动项目启动后，会给项目团队中的人员发送启动通知")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23957(self, drivers):
        pass


    @allure.story("编辑项目")  # 用户故事名称
    @allure.title("项目启动项目未启动显示初始状态，启动后状态自动更改为进行中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23958(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3262:
    @allure.story("删除项目")  # 用户故事名称
    @allure.title("项目删除项目未启动，项目可被删除，启动后不可删除")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23953(self, drivers):
        pass


    @allure.story("删除项目")  # 用户故事名称
    @allure.title("项目删除项目的创建者，项目经理，系统管理员，有权删除项目")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23954(self, drivers):
        pass


    @allure.story("删除项目")  # 用户故事名称
    @allure.title("项目删除普通成员不可删除项目，若配置了删除权限可删除项目")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23955(self, drivers):
        pass


@allure.feature("项目管理")  # 迭代名称
class Teststory_3263:
    @allure.story("查询项目")  # 用户故事名称
    @allure.title("查询按钮在项目清单页面右上角有个筛选按钮和搜索名称栏，两者都可查询")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23959(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("查询条件项目名称、项目分类、项目状态、所属领域")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23960(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("卡片视图卡片视图上的属性有项目分类、项目项目创建者、项目状态、项目进度率、项目名称，更多操作...")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23961(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("项目进度率项目指示灯，绿色标识里程碑及阶段正常无风险障碍；黄色需要注意，里程碑超期02天或阶段延迟lt=10；红色高风险警报，里程碑超期3天未完成或阶段延迟gt10")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23962(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("项目分类显示不同项目的类型")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23963(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("项目分类下拉单选，根据选择的类型，查询到对应类型的项目")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23964(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("项目状态显示项目不同的状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23965(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("项目状态下拉多选，根据选择的项目查询到对象状态的项目，默认是勾选筹备中和进行中的项，其他的需要勾选才显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23966(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("项目名称显示项目名称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23967(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("项目名称输入框，根据输入的名称，可查询到相关联的项目，可支持模糊查询")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23968(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("项目创建者显示项目的创建者")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23969(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("所属领域下拉单选，根据选择的领域查询到对应领域的项目数，值字典配置的")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23970(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("更多操作有删除、编辑操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23971(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("列表视图列表区显示的属性有项目名称、项目状态、项目分类，项目时间、创建者、更多操作等")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23972(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("列表视图在项目列表视图区，有自定义表头功能，可配置列表表头显示的字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23973(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("项目排序创建者的项目按照先后降序排列")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23974(self, drivers):
        pass


    @allure.story("查询项目")  # 用户故事名称
    @allure.title("项目列表显示默认显示筹备中和进行中的项目，其他状态勾选后可显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23975(self, drivers):
        pass


if __name__ == '__main__':
      pass
