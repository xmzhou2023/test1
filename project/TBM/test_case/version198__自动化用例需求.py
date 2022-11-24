import allure
import pytest
@allure.feature("自动化用例需求")  # 迭代名称
class Teststory_3247:
    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，能提交成功创建流程成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20202(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=多物料，创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，在指纹模组中新增两颗物料，添加替代组都为A1，份额为一个20，一个80，其他内容正确填写，点击提交，能提交成功并且提示创建流程成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20203(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=正确选择物料编码，点击一键填写，填写内容保存正确")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在单机头中和PCBA中正确选择物料编码，选中两颗物料，点击一键填写，填写用量和1000点击确认，页面上显示两颗物料用量都为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20204(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOMtree中不选择物料，页面上不存在删除按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，不选择物料，页面上不存在删除按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20205(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=选择物料，页面上存在删除按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择物料，页面上存在删除按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20206(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=选中父节点物料后点击删除，删除页面数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20207(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=选中子节点物料后点击删除，清子节点内容")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20208(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=选择正确的文件进行导入，并应用，显示的数据与模板的数据一致")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20209(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=导入Bom之前需要选中模板")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个不存在模板的品牌，其他内容正确填写，查看BOMTree，无新增BOM按钮；点击导入提示导入Bom之前需要选中模板")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20210(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=不添加BOM内容，提示BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOMtree中点击新增BOM，不添加BOM内容，其他内容正确填写，点击提交，提示BOM状态不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20211(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=不选择BOM状态，提示BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOMtree中点击新增BOM，不选择BOM状态，其他内容正确填写，点击提交，提示BOM状态不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20212(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM编码[null]的物料组在对应的模板中未设置！")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOMtree中点击新增BOM，不填写物料编码，其他内容正确填写，点击提交，提示BOM编码[null]的物料组在对应的模板中未设置！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20213(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=xxxxxxxx的数量为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量不进行填写，点击提交，不能提交成功并给出提示xxxxxxxx的数量为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20214(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=父阶BOM料号xxxxxxxx用量不为1000")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为1，点击提交，不能提交成功并给出提示父阶BOM料号xxxxxxxx用量不为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20215(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=用量只能填写非0数字最多3位小数")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为非数字类型，点击提交，不能提交成功并给出提示用量只能填写非0数字最多3位小数")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20216(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=父阶BOM料号XXXXXXXX下的子阶BOM料号XXXXXXXX用量不为1000")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，选择单机头的物料编码，输入PCBA用量为1，点击提示，不能提交成功并给出提示父阶BOM料号XXXXXXXX下的子阶BOM料号XXXXXXXX用量不为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20217(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=业务评审MPM不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示业务评审MPM不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20218(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=业务评审MPM不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，业务评审MPM不选择评审人员，其他选择审批人员，点击提交，不能提交成功，并给出提示业务评审MPM不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20219(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=[XXXXXX]替代组[XX]的份额总和不为100")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，在充电器中新增两颗物料，添加替代组都为A1，份额为一个20，一个20，其他内容正确填写，点击提交，不能提交成功并且提示替代组份额相加不为100")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20220(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=填入产成品数据，不选择物料，一键填写用量，页面上没有填写上任何数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，不选择物料，点击一键填写，填写用量为1000，点击确定，页面上没有填写上任何数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20221(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=不填写产成品数据，全选一键填写用量，页面上没有填写上任何数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产成品中不选择物料编码，全选选中物料，点击一键填写，一键填写时选择用量和1000，点击确定，页面上不会新增用量数量")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20222(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=文件类型非excel")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示文件类型非excel")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20223(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=模板正确内容错误的文件导入失败，并在校验结果给出相应错误提示，导出校验可点击")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20224(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=[XXXXX]替代组[XX]只有一颗物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入数据，新增一颗物料，添加替代组为A1，份额为20，其他内容正确填写，点击提交，不能提交成功并且提示替代组只有一颗物料")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20225(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=发起流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个单机头BOM协作，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20226(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=补充工厂页面，审批成功")  # 用例名称
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示处理成功，并且页面成功跳转成功处理了补充工厂审核点，我的待办中不存在该条单据在补充工厂审核节点（建议校验单据号和当前节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20227(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=结构工程师审核页面，审批成功")  # 用例名称
    @allure.description("结构工程师审核页面中，所有数据都正确，点击同意，可以提交成功并给出提示处理成功，审核通过，页面成功跳转成功处理了结构工程师审核点，我的待办中不存在该条单机在BOM工程师审核节点（建议校验单据号和当前节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20228(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=结构工程师审批页面，物料编码和物料描述不能编辑")  # 用例名称
    @allure.description("在结构工程师审批页面中，多次点击单机头列数据，该列物料编码和物料描述是不能再进行编辑")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20229(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=结构工程师审批回退到申请人成功")  # 用例名称
    @allure.description("在结构工程师审批页面中，点击回退，选择回退到申请人，查看我的申请中有该单据，显示回退到申请人")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20230(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=结构工程师审批页面，回退到补充工厂再审核，还是结构工程师审批节点")  # 用例名称
    @allure.description("在我的待办中审批从结构工程师审批页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是结构工程师审批")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20231(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=结构工程师审批页面，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在结构工程师审批页面中，点击转交，不选择转交的人直接点击确认，选择框自动关闭，下面只有选择转交人和取消按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20232(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=结构工程师审批页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在结构工程师审批页面中，点击转交，选择转交的人直接点击确认，转交成功，可在转交人账号看到该待办消息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20233(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=结构工程师审批页面，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在结构工程师审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20234(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=结构工程师审批页面，转交单据成功")  # 用例名称
    @allure.description("在结构工程师审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20235(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=业务审核页面，产成品数据不能编辑")  # 用例名称
    @allure.description("在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20236(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=业务审核成功")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择质量部，在检查结果中选择通过，点击同意按钮，给出提示，并且页面跳转成功，跳转成功后，我的待办中不存在该条业务审核单据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20237(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=业务审核页面，回退到补充工厂再审核，还是业务审核节点")  # 用例名称
    @allure.description("在我的待办中审批从业务审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是业务审核节点，而不是BOM工程师节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20238(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=业务审核页面，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在业务页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20239(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=业务审核页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20240(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=业务审核页面，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20241(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=业务审核页面，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20242(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师页面，检查失败项为0，提交成功")  # 用例名称
    @allure.description("在BOM工程师审批中，检查失败项为0时，不填写任何内容，点击同意，可以提交成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20243(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师页面，检查失败项不为0，提交成功")  # 用例名称
    @allure.description("在BOM工程师审批中，检查失败项不为0时，不填写任何内容，点击同意，可以提交成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20244(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=更新子阶BOM，提示刷新成功")  # 用例名称
    @allure.description("在BOM工程师审批中，在BOM工程师审批中，点击更多操作更新子阶BOM，提示刷新成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20245(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在BOM工程师页面，拒绝成功")  # 用例名称
    @allure.description("在BOM工程师审批中，点击拒绝，会显示处理成功，并且页面跳转")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20246(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师审批回退到结构工程师审批成功")  # 用例名称
    @allure.description("在BOM工程师审批中，点击回退，选择回退到结构工程师审批页面，查看我的待办中存在结构工程师审批节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20247(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师审批回退到业务审核成功")  # 用例名称
    @allure.description("在BOM工程师审批中，点击回退，选择回退到业务审核页面，查看我的待办中存在业务审核节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20248(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师审批回退到申请人成功")  # 用例名称
    @allure.description("在BOM工程师审批中，点击回退，选择回退到申请人，查看我的申请中有该单据，显示回退到申请人")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20249(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师审批页面，回退到补充工厂再审核，还是BOM工程师审批节点")  # 用例名称
    @allure.description("在我的待办中审批从BOM工程师审批回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是BOM工程师审批")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20250(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师审批页面，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在BOM工程师审批页面中，点击转交，不选择转交的人直接点击确认，选择框自动关闭，下面只有选择转交人和取消按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20251(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师审批页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在BOM工程师审批页面中，点击转交，选择转交的人直接点击确认，转交成功，可在转交人账号看到该待办消息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20252(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师审批页面，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在BOM工程师审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20253(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师审批页面，转交单据成功")  # 用例名称
    @allure.description("在BOM工程师审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20254(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=数据组审批页面，回退到补充工厂再审核，还是BOM工程师审批节点")  # 用例名称
    @allure.description("在我的待办中审批从数据组审批回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是数据组审批")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20255(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=数据组审批页面，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批批页面中，点击转交，不选择转交的人直接点击确认，选择框自动关闭，下面只有选择转交人和取消按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20256(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=数据组审批页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，转交成功，可在转交人账号看到该待办消息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20257(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=数据组审批页面，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20258(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=数据组审批页面，转交单据成功")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20259(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查为成功，点击同意，能提交成功，并且给出提交成功的提示")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20260(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=【生产工厂信息】物料xxxxxx的组包工厂不能为空")  # 用例名称
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示【生产工厂信息】物料xxxxxx的组包工厂不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20261(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=未选择BOM,一键填写按钮无法被点击")  # 用例名称
    @allure.description("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20262(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=请选择工厂分类")  # 用例名称
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，不进行工厂分类，点击确认，不能进行确认并给出必填提示请选择工厂分类")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20263(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=请选择工厂")  # 用例名称
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，不进行选择工厂，点击确认，不能进行确认并给出必填提示请选择工厂")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20264(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=检查贴片工厂不能为空！")  # 用例名称
    @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示检查贴片工厂不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20265(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=父阶BOM料号xxxxxxxx用量不为1000")  # 用例名称
    @allure.description("在结构工程师审批页面中，在BomTree中点编辑，将用量编辑为1，点击同意，不能提交成功页面给出提示父阶BOM料号xxxxxxxx用量不为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20266(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=自检清单检查角色未选择")  # 用例名称
    @allure.description("在业务审核页面中，不填写任何内容，点击同意，不能提交成功，并给出提示自检清单检查角色未选择")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20267(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不通过，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20268(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不涉及，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20269(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师审批，点击删除BOMTree，提示不能删除BOM")  # 用例名称
    @allure.description("在BOM工程师审批中，在BOMTree中，点击删除，提示不能删除BOM")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20270(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=BOM工程师审批，父阶BOM料号12012025用量不为1000")  # 用例名称
    @allure.description("在BOM工程师审批中，在BOMTree中，点击编辑，可更改用量，将用量改为10000，点击确定，点击同意，提示父阶BOM料号xxxxxxxx用量不为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20271(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=数据组审批页面，检查失败项不为0，提交失败")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查有失败项，点击同意，不能提交成功，并且给出提交失败的提示")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20272(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=补充工厂页面中，导出的xlsx表的数据和页面的数据是一致")  # 用例名称
    @allure.description("在补充工厂页面中，点击导出，导出的xlsx表的数据和页面的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20273(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=结构工程师审批页面，BomTree导出数据一致")  # 用例名称
    @allure.description("在结构工程师审批页面中，在BomTree中点导出，导出的数据和BomTree的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20274(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在业务审核页面中，在生产工厂信息导出的数据和页面的数据是一致的")  # 用例名称
    @allure.description("在业务审核页面中，在生产工厂信息中点击导出，导出文件中的数据和页面的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20275(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在业务审核页面中，在BOMTree导出的数据和页面的数据是一致的")  # 用例名称
    @allure.description("在业务审核页面中，点击BOMTree中的导出，导出文件中的数据和页面中的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20276(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在BOM工程师审批中，子阶BOM检查内容导出和页面的数据是一致的")  # 用例名称
    @allure.description("在BOM工程师审批中，在BOM工程师审批中，点击导出，可以导出子阶BOM检查内容")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20277(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，标题查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入'李小素'，点击查询，查询结果为所有标题包含'李小素'的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20278(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，查询不存在标题，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的标题，点击查询，查询结果为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20279(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，流程编码查询结果正确")  # 用例名称
    @allure.description("在查询页面，流程编码输入框输入'1'，点击查询，查询结果为所有流程编码包含'1'的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20280(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，查询不存在流程编码，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的流程编码，点击查询，查询结果为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20281(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，单机头BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为单机头BOM制作，点击查询，查询结果为所有制作类型为单机头BOM制作的信息息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20282(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，单机头BOM衍生查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为单机头BOM衍生，点击查询，查询结果为所有制作类型为单机头BOM衍生的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20283(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，二级BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为二级BOM制作，点击查询，查询结果为所有制作类型为二级BOM制作的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20284(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，预加工件/虚拟件制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为预加工件/虚拟件制作，点击查询，查询结果为所有制作类型为预加工件/虚拟件制作的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20285(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，预加工件/虚拟件衍生查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为预加工件/虚拟件衍生，点击查询，查询结果为所有制作类型为预加工件/虚拟件衍生的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20286(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，组合查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入'李小素'，流程编码输入框输入'1'，下拉框选择为单机头BOM制作，点击查询，查询结果为所有标题包含'李小素'、流程编码包含'1'、制作类型为客供BOM制作的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20287(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，编辑正常")  # 用例名称
    @allure.description("在查询页面，点击编辑，跳转至oneworks编辑页面，可以编辑页面信息、提交、保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20288(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作单机头BOM协作=在查询页面，删除取消无变动")  # 用例名称
    @allure.description("在查询页面，点击删除，提示是否确认删除，点击取消，取消成功，页面无变动")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20289(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，在生产工厂信息点击刷新按钮，点击提交，能提交成功创建流程成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20290(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=新增同组物料两颗，份额合计100,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据；新增两颗物料，添加替代组都为A1，份额为一个20，一个80，其他内容正确填写，点击提交，能提交成功并且提示'创建流程成功'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20291(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=选择物料编码，点击一键填写，填写内容保存正确")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选中两颗物料，点击一键填写，填写用量和1000点击确认，页面上显示两颗物料用量都为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20292(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=BOMtree中不选择物料，页面上不存在删除按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，不选择物料，页面上不存在删除按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20293(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=选择物料，页面上存在删除按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择物料，页面上存在删除按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20294(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=选中父节点物料后点击删除，删除页面数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20295(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=选中子节点物料后点击删除，清子节点内容")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20296(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=选择正确的文件进行导入，并应用，显示的数据与模板的数据一致")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20297(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=客供BOM衍生,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息包含新增为128开头的物料，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，提示发起成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20298(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=客供BOM衍生,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息包含新增为128开头的物料，再新增1颗物料，添加替代组都为A1，份额为一个20，一个80，其他内容正确填写，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，能提交成功并且提示'创建流程成功'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20299(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=客供BOM衍生导入模板,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，下载模板，模板内容正确填写包含新增为128开头的物料，在衍生差异点击导入，文件导入成功，点击生成BOM，点击刷新，填写业务审核，点击提交，流程发起成功并提示流程创建成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20300(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=客供BOM衍生,物料信息删除成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中新增物料后，点击删除按钮，物料信息删除成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20301(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=生产工厂信息导入正确,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中新增物料后，点击生成BOM，点击生产工厂信息中的导入，下载模板，填写正确的信息，选择正确的模板，点击应用，导入内容正确，填写业务审核，点击提交，提示流程发起成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20302(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=生产工厂信息导入正确,取消导入")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中新增物料后，点击生成BOM，点击生产工厂信息中的导入，下载模板，填写正确的信息，选择正确的模板，点击取消，导入失败")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20303(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=客供BOM衍生导入模板,应用成功并提交成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击导入，下载模板，正确填写信息，选择正确的模板文件，点击应用，信息导入成功，点击生成BOM，点击刷新，填写业务审核，点击提交，提示流程发起成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20304(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=客供BOM衍生导入模板,取消导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击导入，下载模板，正确填写信息，选择正确的模板文件，点击取消，导入失败")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20305(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=客供BOM衍生,附件删除成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，点击附件的加号，选择文件，上传成功后点击删除，文件删除成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20306(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=客供BOM衍生上传附件,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中新增物料，点击生成BOM，点击刷新，填写业务审核，点击提交，点击附件的加号，选择文件，点击打开，导入附件成功，提示流程发起成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20307(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=生产工厂信息不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，提示生产工厂信息不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20308(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，不选择BOM状态，正确填写物料编码等其他内容，点击提交，不能提交成功并给出提示BOM状态不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20309(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=[XXXXX]下必须存在物料组为128的子阶物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，只加一个BOM，不在下面添加子BOM，点击提交，不能成功并给出提示[12010003]下必须存在物料组为128的子阶物料")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20310(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=xxxxxxx用量不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量不进行填写，点击提交，不能提交成功并给出提示xxxxxx用量不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20311(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=父阶BOM料号xxxxxxxx用量不为1000")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为1，点击提交，不能提交成功并给出提示父阶BOM料号10000001用量不为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20312(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=用量只能填写非0数字最多3位小数")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为非数字类型，点击提交，不能提交成功并给出提示用量只能填写非0数字最多3位小数")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20313(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=业务审核必填项需填写完整！")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示业务审核必填项需填写完整！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20314(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=只填写一个业务审核，提示业务审核必填项需填写完整！")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，其中一个业务审核不选择相应的审核人员，点击提交，不能提交成功，并给出提示业务审核必填项需填写完整！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20315(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=[XXXXX]替代组[XX]只有一颗物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入数据，新增一颗物料，添加替代组为A1，份额为20，其他内容正确填写，点击提交，不能提交成功并且提示替代组只有一颗物料")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20316(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=不选择物料，点击一键填写不生效")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，不选择物料，点击一键填写，填写用量为1000，点击确定，页面上没有填写上任何数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20317(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=一键填写无内容提示内容不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选中两颗物料，点击一键填写，选择用量，并且不填写字段值，点击确认，给出必填提示，提示为不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20318(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=文件类型非excel")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示文件类型非excel")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20319(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=正确内容错误的文件进行导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20320(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=[xxxxxxxx]下必须存在物料组为128的子阶物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM、新增物料，输入客供BOM的物料编码、用量，新增物料时输入物料编码不为128的料，点击刷新，点击提交，xxxxxxxx下必须存在物料组为128的子阶物料")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20321(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=BomTree与生产工厂信息数据不一致，请点击刷新按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择外研BOM，选择一个存在模板的品牌，在BOMtree中输入客供BOM的物料编码、用量，点刷新；修改客供BOM的物料编码，不点刷新，点击提交，提示BomTree与生产工厂信息数据不一致，请点击刷新按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20322(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=请先选择制作类型")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，不选择制作类型，点击新增BOM，提示请先选择制作类型")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20323(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=[xxxxx]下必须存在物料组为128的子阶物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，选择一个存在模板的品牌，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息不包含新增为128开头的物料，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，提示[xxxxxx]下必须存在物料组为128的子阶物料")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20324(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=请完善Bom信息！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息不填写完整，输入业务审核必填项，点击提交，提示请完善Bom信息！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20325(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=BomTree不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，不填写BOMTree点击提交，提示BomTree不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20326(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=不点击生成BOM，BomTree不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，不点击生成BOM，点击提交，提示BomTree不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20327(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=生产工厂信息不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，不点击生成BOM，点击提交，提示BomTree不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20328(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=业务审核必填项需填写完整！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，点击生成BOM，不填写业务审核，点击刷新，点击提交，提示业务审核必填项需填写完整！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20329(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生差异【第1行】用量只能填写非0数字最多3位小数")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，衍生差异的用量填0，点击生成BOM，提示衍生差异【第1行】用量只能填写非0数字最多3位小数")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20330(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx用量不为1000")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，衍生差异的用量填10，点击生成BOM，提示'父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx用量不为1000'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20331(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=业务审核必填项需填写完整！")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，输入业务审核必填项，填写衍生BOM制作需求，点击生成BOM，业务审核有一个必填项不填，点击刷新，点击提交，提示业务审核必填项需填写完整！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20332(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=xxxxxxxx替代组[xx]只有一颗物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息包含新增为128开头的物料添加替代组为A1，份额为20，其他内容正确填写，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，不能提交成功并且提示'xxxxxxxx替代组[xx]只有一颗物料'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20333(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=xxxxxxxx替代组[xx]的份额总和不为100")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息包含新增为128开头的物料添加替代组为A2，份额为20，再新增1颗物料添加替代组为A2，份额为20，其他内容正确填写，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，不能提交成功并且提示'xxxxxxxx替代组[xx]的份额总和不为100'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20334(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=发起流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个整机生产BOM，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20335(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=业务审核页面，审核成功")  # 用例名称
    @allure.description("在业务审核页面，所有数据正确填写，点击同意，能成功提交，并给出提示处理成功，并且页面成功跳转")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20336(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=业务审核页面，取消成功，页面无变化")  # 用例名称
    @allure.description("在业务审核页面，所有数据正确填写，点击同意，弹出弹框确认同意？，点击取消，取消成功，页面无变化")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20337(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在业务审核页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20338(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在业务审核页面中，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20339(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在业务审核页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20340(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在业务审核页面中，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20341(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在数据组审批页面中，回退到业务审核再审核，还是数据组审批节点")  # 用例名称
    @allure.description("在数据组审批页面中，点击回退，选择回退到业务审核页面，查看我的待办中存在业务审核节点，在业务审核同意并审核成功，下个节点是数据组审核节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20342(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在数据组审批页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20343(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在数据组审批页面中，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20344(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在数据组审批页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20345(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在数据组审批页面中，转交单据成功")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20346(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=发起客供BOM衍生流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个客供BOM衍生，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20347(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生业务审核页面，审核成功")  # 用例名称
    @allure.description("在业务审核页面，所有数据正确填写，点击同意，能成功提交，并给出提示处理成功，并且页面成功跳转")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20348(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生业务审核页面，取消成功，页面无变化")  # 用例名称
    @allure.description("在业务审核页面，所有数据正确填写，点击同意，弹出弹框确认同意？，点击取消，取消成功，页面无变化")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20349(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生在业务审核页面中，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20350(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生在业务审核页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20351(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生在业务审核页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20352(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生在业务审核页面中，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20353(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生业务审核页面，取消成功，页面无变化")  # 用例名称
    @allure.description("在业务审核页面，所有数据正确填写，点击同意，弹出弹框确认同意？，点击取消，取消成功，页面无变化")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20354(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生在数据组审批页面中，回退到业务审核再审核，还是数据组审批节点")  # 用例名称
    @allure.description("在数据组审批页面中，点击回退，选择回退到业务审核页面，查看我的待办中存在业务审核节点，在业务审核同意并审核成功，下个节点是数据组审核节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20355(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生在在数据组审批页面中，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20356(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生在数据组审核页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20357(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生在数据组审批页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20358(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生在数据组审核页面中，转交单据成功")  # 用例名称
    @allure.description("在数据组审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20359(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查为成功，点击同意，能提交成功，并且给出提交成功的提示")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20360(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=衍生BOM，数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查为成功，点击同意，能提交成功，并且给出提交成功的提示")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20361(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=数据组审批页面，检查失败项不为0，提交失败")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM/状态/物料检查为失败，点击同意，不能提交成功，并且给出提交失败的提示子阶bom检查失败，无法同步")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20362(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=数据组审批页面，检查失败项不为0，提交失败")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM/状态/物料检查为失败，点击同意，不能提交成功，并且给出提交失败的提示子阶bom检查失败，无法同步")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20363(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在查询页面，标题查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入'李小素'，点击查询，查询结果为所有标题包含'李小素'的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20364(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在查询页面，查询不存在标题，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的标题，点击查询，查询结果为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20365(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在查询页面，流程编码查询结果正确")  # 用例名称
    @allure.description("在查询页面，流程编码输入框输入'1'，点击查询，查询结果为所有流程编码包含'1'的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20366(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在查询页面，查询不存在流程编码，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的流程编码，点击查询，查询结果为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20367(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在查询页面，客供BOM衍生查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为客供BOM衍生，点击查询，查询结果为所有制作类型为客供BOM衍生的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20368(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在查询页面，客供BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为客供BOM制作，点击查询，查询结果为所有制作类型为客供BOM制作的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20369(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在查询页面，客供BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入'李小素'，流程编码输入框输入'1'，BOM编码输入'2'，下拉框选择为客供BOM制作，点击查询，查询结果为所有标题包含'李小素'、流程编码包含'1'、物料编码包含'2'、制作类型为客供BOM制作的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20370(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在查询页面，编辑正常")  # 用例名称
    @allure.description("在查询页面，点击编辑，跳转至oneworks编辑页面，可以编辑页面信息、提交、保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20371(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作外研BOM协作=在查询页面，删除取消无变动")  # 用例名称
    @allure.description("在查询页面，点击删除，提示是否确认删除，点击取消，取消成功，页面无变动")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20372(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，能提交成功，创建流程成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20373(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=新增物料，创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，在充电器中新增两颗物料，添加替代组都为A1，份额为一个20，一个80，其他内容正确填写，点击提交，能提交成功并且提示创建流程成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20374(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=正确选择物料编码，点击一键填写，填写内容保存正确")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产成品中和单机头中正确选择物料编码，选中两颗物料，点击一键填写，填写用量和1000点击确认，页面上显示两颗物料用量都为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20375(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOMtree中不选择物料，页面上不存在删除按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，不选择物料，页面上不存在删除按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20376(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOMtree中选择物料，页面上存在删除按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择物料，页面上存在删除按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20377(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=选中父节点物料后点击删除，删除页面数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20378(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=选中子节点物料后点击删除，清子节点内容")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20379(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=复制审批人成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，正确填入数据后，在审核人设置中点击复制审批人，会弹出选择单据号页面，查询结果正确显示，并且选择生效")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20380(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，填写BOM信息，在衍生BOM列表点击新增并正确填写信息，填写审核人设置，点击提交，能提交成功'创建流程成功'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20381(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，选择正确的文件进行导入，创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，填写业务评审和业务审核，点击提交，提交成功并流程发起成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20382(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=导入简易模式选择正确的文件进行导入成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入简易模式选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20383(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=导入选择正确的文件进行导入成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20384(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，导入选择正确的文件进行导入成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，点击附件中的加号，上传正确的文件，文件上传成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20385(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=请完善Bom信息！")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个不存在模板的品牌，其他内容正确填写，点击提交，不能提交成功并给出提示请完善Bom信息！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20386(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=产成品必须有物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，不添加BOM内容，其他内容正确填写，点击提交，不能提交成功并给出提示产成品必须有物料")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20387(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM类型不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，不选择BOM类型，正确填写物料编码等其他内容，点击提交，不能提交成功并给出提示BOM类型不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20388(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，不选择BOM状态，正确填写物料编码等其他内容，点击提交，不能提交成功并给出提示BOM状态不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20389(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=含有物料的节点，用量不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量不进行填写，点击提交，不能提交成功并给出提示含有物料的节点，用量不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20390(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=父阶BOM料号XXXXXXXX用量不为1000")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为1，点击提交，不能提交成功并给出提示父阶BOM料号10000001用量不为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20391(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=用量只能填写非数字（最多3位小数）")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为非数字类型，点击提交，不能提交成功并给出提示用量只能填写非数字（最多3位小数）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20392(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx用量不为1000")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，选择单机头的物料编码，输入单机头用量为1，点击提示，不能提交成功并给出提示父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx用量不为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20393(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=业务评审MPM不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示业务评审MPM不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20394(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=业务审核至少要选中一个")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，业务审核不选择相应的审核人员，点击提交，不能提交成功，并给出提示业务审核至少要选中一个！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20395(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=[国内生产BOM][XXXXXXXX]替代组[A1]的份额总和不为100")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，在充电器中新增两颗物料，添加替代组都为A1，份额为一个20，一个20，其他内容正确填写，点击提交，不能提交成功并且提示[国内生产BOM][XXXXXXXX]替代组[A1]的份额总和不为100")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20396(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=填入产成品数据，不选择物料，一键填写用量，页面上没有填写上任何数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，不选择物料，点击一键填写，填写用量为1000，点击确定，页面上没有填写上任何数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20397(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=不填写产成品数据，全选一键填写用量，页面上没有填写上任何数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产成品中不选择物料编码，全选选中物料，点击一键填写，一键填写时选择用量和1000，点击确定，页面上不会新增用量数量")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20398(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=一键填写，不填写内容提示为'不能为空'")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产成品中和单机头中正确选择物料编码，选中两颗物料，点击一键填写，选择用量，并且不填写字段值，点击确认，给出必填提示，提示为不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20399(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=[XXXXX]替代组[XX]只有一颗物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入数据，新增一颗物料，添加替代组为A1，份额为20，其他内容正确填写，点击提交，不能提交成功并且提示替代组只有一颗物料")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20400(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,请完善Bom信息！")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个不存在模板的品牌，其他内容正确填写，点击提交，不能提交成功并给出提示'请完善Bom信息！'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20401(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,衍生BOM列表不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，不添加BOM内容，其他内容正确填写，点击提交，不能提交成功并给出提示衍生BOM列表不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20402(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,【衍生BOM列表】新BOM类型不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，不添加BOM内容，其他内容正确填写，点击提交，不能提交成功并给出提示【衍生BOM列表】新BOM类型不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20403(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,业务评审MPM不能为空！")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示'业务评审MPM不能为空！'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20404(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,业务审核至少要选中一个！")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，正确填入产成品数据，业务审核不选择相应的审核人员，点击提交，不能提交成功，并给出提示业务审核至少要选中一个！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20405(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，文件类型非excel")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示'文件类型非excel'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20406(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=正确内容错误的文件进行导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20407(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=导入简易模式选择错误文件提示文件类型非excel")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入简易模式选择一个错误的文件格式进行导入，不能导入成功并提示文件类型非excel")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20408(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=导入简易模式选择内容错误的文件进行导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入简易模式选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20409(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=选择错误文件导入提示文件类型非excel")  # 用例名称
    @allure.description("进入新增页面制作类型选择生产BOM，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示文件类型非excel")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20410(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，选择内容错误的文件进行导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择衍生BOM，选择一个存在模板的品牌，在衍生BOM列表中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20411(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=发起流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个整机生产BOM，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20412(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在补充工厂页面，审批成功")  # 用例名称
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示'处理成功'，页面成功跳转，成功处理了补充工厂审核点，我的待办中不存在该条单据在补充工厂审核节点（建议校验单据号和当前节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20413(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM工程师页面，审批成功并给出提示'处理成功，审核通过'")  # 用例名称
    @allure.description("在BOM工程师页面中，所有数据都正确，点击同意，可以提交成功并给出提示'处理成功，审核通过'，页面成功跳转；成功处理了BOM工程师审核点，我的待办中不存在该条单机在BOM工程师审核节点（建议校验单据号和当前节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20414(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM工程师页面，点击一键填写按钮，能弹出一键填写的页面")  # 用例名称
    @allure.description("在BOM工程师页面中，点击一键填写按钮，能弹出一键填写的页面")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20415(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM工程师页面，回退到补充工厂页面")  # 用例名称
    @allure.description("在BOM工程师页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验单据号和节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20416(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM工程师页面，转交时不选择转交人，不存在确定转交按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20417(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM工程师页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20418(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM工程师页面，选择转交人转交后取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20419(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM工程师页面，转交单据成功")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20420(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM工程师页面，拒绝成功")  # 用例名称
    @allure.description("在BOM工程师页面中，点击拒绝，会显示处理成功，并且页面跳转")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20421(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=业务审核页面，产成品数据不能编辑")  # 用例名称
    @allure.description("在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20422(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=业务审核成功")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择通过，点击同意按钮，给出提示，并且页面跳转成功，跳转成功后，我的待办中不存在该条业务审核单据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20423(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=业务审核回退到补充工厂成功")  # 用例名称
    @allure.description("在业务审核页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验单据号和节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20424(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=业务审核回退到补充工厂重新审核，下一节点是业务审核")  # 用例名称
    @allure.description("在我的待办中审批从业务审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是业务审核节点，而不是BOM工程师节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20425(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在业务审核页面，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20426(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在业务审核页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20427(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在业务审核页面，选择转交人转交后取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20428(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在业务审核页面，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20429(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM/状态/物料检查为成功，点击同意，能提交成功，并且给出提交成功的提示")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20430(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=数据组审批页面，回退到补充工厂")  # 用例名称
    @allure.description("在数据组审批页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验单据号和节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20431(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=数据组审批页面，回退到补充工厂再审核，还是数据组审核节点")  # 用例名称
    @allure.description("在我的待办中审批从数据组审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是数据组审核节点，而不是BOM工程师节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20432(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=数据组审批页面，不选择转交人转交，不存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20433(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=数据组审批页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20434(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=数据组审批页面，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20435(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM工程师页面，选BOMTree中点击设置市场/配置按钮，保存成功")  # 用例名称
    @allure.description("在BOM工程师中，BOMTree中点击设置市场/配置按钮，弹出相应页面，在设置市场/配置页面中，填入组号和销售市场和机型配置，点击确认，能保存成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20436(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在BOM工程师中，BOMTree新增物料成功")  # 用例名称
    @allure.description("在BOM工程师中，BOMTree上点击新增物料，会出现新的物料节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20437(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=补充工厂页面中，导出的xlsx表的数据和页面的数据是一致的")  # 用例名称
    @allure.description("在补充工厂页面中，点击导出，导出的xlsx表的数据和页面的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20438(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=BOM工程师页面，BomTree导出数据一致")  # 用例名称
    @allure.description("在BOM工程师页面中，在BomTree中点导出，导出的数据和BomTree的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20439(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=业务审核页面，生产工厂信息导出数据和页面数据一致")  # 用例名称
    @allure.description("在业务审核页面中，在生产工厂信息中点击导出，导出文件中的数据和页面的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20440(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=业务审核页面，BOMTree导出数据和页面中数据一致")  # 用例名称
    @allure.description("在业务审核页面中，点击BOMTree中的导出，导出文件中的数据和页面中的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20441(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在数据组审批页面，生产工厂信息导出数据和页面数据一致")  # 用例名称
    @allure.description("在数据组审批页面中，在生产工厂信息中点击导出，导出的文件中的数据和页面中的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20442(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，发起流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个整机生产BOM，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20443(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，在补充工厂页面，审批成功")  # 用例名称
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示'处理成功'，并且页面成功跳转")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20444(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，BOM工程师页面，审批成功并给出提示'处理成功，审核通过'")  # 用例名称
    @allure.description("在BOM工程师页面中，所有数据都正确，点击同意，可以提交成功并给出提示'处理成功，审核通过'，页面成功跳转；成功处理了BOM工程师审核点，我的待办中不存在该条单机在BOM工程师审核节点（建议校验单据号和当前节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20445(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，BOM工程师页面，转交时不选择转交人，不存在确定转交按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20446(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，BOM工程师页面，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20447(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，BOM工程师页面，选择转交人转交后取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20448(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，BOM工程师页面，转交单据成功")  # 用例名称
    @allure.description("在BOM工程师页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20449(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，BOM工程师页面，拒绝成功")  # 用例名称
    @allure.description("在BOM工程师页面中，点击拒绝，会显示处理成功，并且页面跳转")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20450(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,BOM工程师中，新增物料成功")  # 用例名称
    @allure.description("在BOM工程师中，衍生BOM处理信息中点击新增物料，会出现新的物料节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20451(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,业务审核成功")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择通过，点击同意按钮，给出提示，并且页面跳转成功，跳转成功后，我的待办中不存在该条业务审核单据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20452(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,业务审核回退到补充工厂成功")  # 用例名称
    @allure.description("在业务审核页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验单据号和节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20453(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,在业务审核页面中，转交时不选择转交人，不存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20454(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,在业务审核页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20455(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,在业务审核页面中，选择转交人转交后取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20456(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,在业务审核页面中，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20457(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM/状态/物料检查为成功，点击同意，能提交成功，并且给出提交成功的提示")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20458(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,在数据组审批页面中回退到补充工厂成功")  # 用例名称
    @allure.description("在数据组审批页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验单据号和节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20459(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,在数据组审批页面中，转交时不选择转交人，不存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20460(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,在数据组审批页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20461(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM,在数据组审批页面中，选择转交人转交后取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20462(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=【生产工厂信息】物料XXXXXXXX的组包工厂不能为空")  # 用例名称
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示【生产工厂信息】物料xxxxxx的组包工厂不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20463(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=未选择BOM，无法点击一键填写按钮")  # 用例名称
    @allure.description("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20464(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=请选择工厂分类")  # 用例名称
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，不进行工厂分类，不进行选择工厂，点击确认，不能进行确认并给出必填提示请选择工厂分类，请选择工厂")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20465(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=检查贴片工厂不能为空！")  # 用例名称
    @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示检查贴片工厂不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20466(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=父阶BOM料号xxxxxxxx用量不为1000！")  # 用例名称
    @allure.description("在BOM工程师页面中，在BomTree中点编辑，将用量编辑为'1'，点击同意，不能提交成功页面给出提示父阶BOM料号xxxxxxxx用量不为1000")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20467(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=不能删除BOM！")  # 用例名称
    @allure.description("在BOM工程师页面中，在产成品中点击删除按钮，不能进行删除，并且给出提示不能删除BOM！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20468(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=自检清单检查角色未选择")  # 用例名称
    @allure.description("在业务审核页面中，不填写任何内容，点击同意，不能提交成功，并给出提示自检清单检查角色未选择")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20469(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=自检清单第【1】行检查结果未选择")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，选择后直接点击同意，不能提交成功，并给出提示自检清单第【1】行检查结果未选择")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20470(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不通过，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20471(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不涉及，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20472(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=[手机_itel_预研组_整机BOM]未配置自检清单！自检清单不能为空")  # 用例名称
    @allure.description("在业务审核页面中，选择检查角色没有配置的自检清单的检查角色，会提示[手机_itel_预研组_整机BOM]未配置自检清单！，直接点击同意，会提示自检清单不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20473(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，【生产工厂信息】物料XXXXXXXX的组包工厂不能为空")  # 用例名称
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示【生产工厂信息】物料xxxxxx的组包工厂不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20474(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，未选择BOM，无法点击一键填写按钮")  # 用例名称
    @allure.description("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20475(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，请选择工厂分类，请选择工厂")  # 用例名称
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，不进行工厂分类，不进行选择工厂，点击确认，不能进行确认并给出必填提示请选择工厂分类，请选择工厂")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20476(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，检查贴片工厂不能为空！")  # 用例名称
    @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示检查贴片工厂不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20477(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，自检清单第【1】行检查结果未选择")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，选择后直接点击同意，不能提交成功，并给出提示自检清单第【1】行检查结果未选择")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20478(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不通过，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20479(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=衍生BOM，自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择音频，在检查结果中选择不涉及，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20480(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在查询页面，制作类型和流程编码查询结果正确")  # 用例名称
    @allure.description("进入整机BOM协作页面，输入存在的制作类型和流程编码，点击查询，下方会显示相应的数据（建议校验制作类型和流程编码）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20481(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在查询页面，查询后点击重置，下方会显示所有的数据")  # 用例名称
    @allure.description("进入整机BOM协作页面，输入存在的流程编码和BOM编码，点击查询，查询后点击重置，下方会显示所有的数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20482(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在查询页面，查询不存在流程编码，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的流程编码，点击查询，查询结果为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20483(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作整机BOM协作=在查询页面，单机头BOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为单机头BOM制作，点击查询，查询结果为所有制作类型为单机头BOM制作的信息息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20484(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，能提交成功并且提示'建流程成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20485(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=添加替代组，创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，在充电器中新增两颗物料，添加替代组都为A1，份额为一个20，一个30，其他内容正确填写，点击提交，能提交成功并且提示'创建流程成功'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20486(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=一键填写生效")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在PCBA中和PCB中正确选择物料编码，选中两颗物料，点击一键填写，填写数量为1点击确认，页面上显示两颗物料用量都为1")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20487(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOMtree中不选择物料，页面上不存在删除按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，不选择物料，页面上不存在删除按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20488(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOMtree中选择物料，页面上存在删除按钮")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择物料，页面上存在删除按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20489(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=选中父节点物料后点击删除，删除页面数据")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20490(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=选中子节点物料后点击删除，清子节点内容")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20491(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=选择正确的文件进行导入，并应用，显示的数据与模板的数据一致")  # 用例名称
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20492(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=PCBABOM衍生,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，在衍生BOM制作需求中点击新增，输入物料信息，点击衍生差异输入物料信息包含新增为128开头的物料，点击生成BOM，点击生产工厂信息中的刷新，输入业务审核的必填项，点击提交，提示发起成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20493(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=PCBABOM衍生,不填写衍生差异信息，创建流程成功")  # 用例名称
    @allure.description("在PCBABOM制作新增页面，制作类型选择PCBABOM衍生，填写BOM信息，在衍生BOM制作需求点击新增正确填写信息，不填写衍生差异信息，点击生成BOM，填写业务评审和业务审核，点击提交，提交成功并流程发起成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20494(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=PCBABOM衍生导入模板,创建流程成功")  # 用例名称
    @allure.description("进入新增页面制作类型选择客供BOM衍生，BOM信息填写完整，下载模板，模板内容正确填写包含新增为128开头的物料，在衍生差异点击导入，文件导入成功，点击生成BOM，点击刷新，填写业务审核，点击提交，流程发起成功并提示流程创建成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20495(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=PCBABOM衍生,保存草稿成功")  # 用例名称
    @allure.description("在PCBABOM制作新增页面，制作类型选择PCBABOM衍生，填写BOM信息，在衍生BOM制作需求和衍生差异信息，点击新增正确填写信息，点击生成BOM，填写业务评审和业务审核，点击保存，提示保存草稿成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20496(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=导入Bom之前需要选中模板")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM制作，选择一个不存在模板的品牌，其他内容正确填写，查看BOMTree，无新增BOM按钮；点击导入提示导入Bom之前需要选中模板")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20497(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOMtree不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM制作，在BOMtree中不点击新增BOM，其他内容正确填写，点击提交，提示BOMtree不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20498(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM制作，在BOMtree中点击新增BOM，不选择BOM状态，其他内容正确填写，点击提交，提示BOM状态不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20499(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM编码[null]的物料组在对应的模板中未设置！")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM制作，在BOMtree中点击新增BOM，不填写物料编码，其他内容正确填写，点击提交，提示BOM编码空的物料组在对应的模板中未设置！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20500(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=请完善Bom信息")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM制作，选择一个不存在模板的品牌，其他内容正确填写，点击提交，不能提交成功并给出提示请完善Bom信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20501(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM状态不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM制作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，不添加BOM内容，其他内容正确填写，点击提交，不能提交成功并给出提示BOM状态不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20502(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=xxxxxxxx的数量为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，数量不进行填写，点击提交，不能提交成功并给出提示xxxxxxxx的数量为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20503(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=数量长度超3字符")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，数量填写为1000，点击提交，不能提交成功并给出提示数量长度超3字符")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20504(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=数量只能填写18位正整数")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产出品选择一个物料编码，数量填写为非数字类型，点击提交，不能提交成功并给出提示数量只能填写18位正整数")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20505(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=父阶BOM料号12105821下的子阶BOM料号12105820数量不为1")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，选择单机头的物料编码，输入单机头用量为2，点击提示，不能提交成功并给出提示父阶BOM料号xxxxxxxx下的子阶BOM料号xxxxxxxx数量不为1")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20506(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=业务评审必填项需填写完整")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示业务评审必填项需填写完整！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20507(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=不选择物料，一键填写不生效")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入PCBA数据，不选择物料，点击一键填写，填写数量为1，点击确定，页面上没有填写上任何数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20508(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=不填写产成品数据，选择物料一键填写不生效")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在PCBA中不选择物料编码，全选选中物料，点击一键填写，一键填写时选择数量为1，点击确定，页面上不会新增用量数量")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20509(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，在产成品中和单机头中正确选择物料编码，选中两颗物料，点击一键填写，选择用量，并且不填写字段值，点击确认，给出必填提示，提示为'不能为空'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20510(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=一键填写无内容提示内容不能为空")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示'文件类型非excel'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20511(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=模板正确内容错误的文件进行导入，导入失败")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20512(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=[XXXXX]替代组[XX]只有一颗物料")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，正确填入产成品数据，新增物料，添加替代组为A1，份额为20，其他内容正确填写，点击提交，不能提交成功并且提示'替代组只有一颗物料'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20513(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=输入位号U1001,U1002,U1003,U1004,U1005，数量自动变为5")  # 用例名称
    @allure.description("进入新增页面制作类型选择PCBABOM协作，选择一个存在模板的品牌，在BOMtree中点击新增BOM，输入正确的PCBA物料用量为1，在IC144输入物料编码为14400003，输入位号U1001,U1002,U1003,U1004,U1005，数量自动变为5")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20514(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，BomTree不能为空！")  # 用例名称
    @allure.description("在PCBABOM制作新增页面，制作类型选择PCBABOM衍生，填写BOM信息，衍生BOM制作需求不点击新增，填写业务评审和业务审核，点击提交，提示BomTree不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20515(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，请完善Bom信息！")  # 用例名称
    @allure.description("在PCBABOM制作新增页面，制作类型选择PCBABOM衍生，不填写BOM信息，在衍生制作需求点击新增，提示请完善Bom信息！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20516(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，不生成BOM提示BomTree不能为空！")  # 用例名称
    @allure.description("在PCBABOM制作新增页面，制作类型选择PCBABOM衍生，填写BOM信息，在衍生BOM制作需求和衍生差异信息，点击新增正确填写信息，不点击生成BOM，填写业务评审和业务审核，点击提交，提示BomTree不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20517(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，原始bom工厂不能为空！")  # 用例名称
    @allure.description("在PCBABOM制作新增页面，制作类型选择PCBABOM衍生，填写BOM信息，在衍生BOM制作需求点击新增不填写原始BOM工厂，点击生成BOM，提示原始bom工厂不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20518(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=PCBABOM衍生,数量长度超3字符")  # 用例名称
    @allure.description("在PCBABOM制作新增页面，制作类型选择PCBABOM衍生，填写BOM信息，在衍生BOM制作需求点击新增正确填写信息，衍生差异信息数量填1000，点击生成BOM，填写业务评审和业务审核，点击提交，提示数量长度超3字符")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20519(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=PCBABOM衍生,业务评审必填项需填写完整！")  # 用例名称
    @allure.description("在PCBABOM制作新增页面，制作类型选择PCBABOM衍生，填写BOM信息，在衍生BOM制作需求和衍生差异信息，点击新增正确填写信息，点击生成BOM，不填写业务评审和业务审核，点击提交，提示业务评审必填项需填写完整！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20520(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=发起流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个PCBABOM协作，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20521(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=补充工厂页面，审批成功")  # 用例名称
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示'处理成功'，并且页面成功跳转，成功处理了补充工厂审核点，我的待办中不存在该条单据在补充工厂审核节点（建议校验单据号和当前节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20522(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=基带工程师审批，审批成功")  # 用例名称
    @allure.description("基带工程师审批页面中，所有数据都正确，点击同意，可以提交成功并给出提示'处理成功，审核通过'，页面成功跳转成功处理了基带工程师审批节点，我的待办中不存在该条数据在基带工程师审批节点（建议校验单据号和当前节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20523(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=基带工程师审批回退到业务审核成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验单据号和节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20524(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在基带工程师审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20525(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在基带工程师审批页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20526(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在基带工程师审批页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20527(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在基带工程师审批页面中，转交单据成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20528(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在基带工程师审批页面中，拒绝成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击拒绝，会显示处理成功，并且页面跳转")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20529(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=采购审核（NPS）页面中，审批成功")  # 用例名称
    @allure.description("在采购审核（NPS）页面中，点击同意，可以提交成功并给出提示'处理成功，审核通过'，页面成功跳转成功处理了采购审核（NPS）节点，我的待办中不存在该条数据在采购审核（NPS）节点（建议校验单据号和当前节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20530(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=采购审核（NPS）页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例名称
    @allure.description("采购审核（NPS）页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20531(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=采购审核（NPS）页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("采购审核（NPS）页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20532(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=采购审核（NPS）页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("采购审核（NPS）页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20533(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=采购审核（NPS）页面中，转交单据成功")  # 用例名称
    @allure.description("采购审核（NPS）页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20534(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=采购审核（NPS）页面中，拒绝成功")  # 用例名称
    @allure.description("采购审核（NPS）页面中，点击拒绝，会显示处理成功，并且页面跳转")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20535(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=业务审核页面，产成品数据不能编辑")  # 用例名称
    @allure.description("在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20536(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=业务审核成功")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择通过，添加名字为检查结果的附件，点击同意按钮，给出提示，并且页面跳转成功，跳转成功后，我的待办中不存在该条业务审核单据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20537(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=业务审核页面，回退到补充工厂再审核，还是业务审核节点")  # 用例名称
    @allure.description("在我的待办中审批从业务审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是业务审核节点，而不是BOM工程师节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20538(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在业务页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例名称
    @allure.description("在业务页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20539(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在业务页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在业务页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20540(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在业务页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在业务页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20541(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在业务页面中，转交单据成功")  # 用例名称
    @allure.description("在业务页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20542(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在数据组审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20543(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在数据组审核页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20544(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在数据组审核页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在数据组审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20545(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在数据组审核页面中，转交单据成功")  # 用例名称
    @allure.description("在数据组审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20546(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=发起PCBABOM衍生流程，审批页面的数据和发起的数据是一致的")  # 用例名称
    @allure.description("发起一个PCBABOM衍生，进入待办中心，点击该条单据进行查看，查看页面的数据和发起的数据是一致的")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20547(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，补充工厂页面，审批成功")  # 用例名称
    @allure.description("在补充工厂页面，所有数据正确填写，点击同意，能成功提交，并给出提示'处理成功'，并且页面成功跳转，成功处理了补充工厂审核点，我的待办中不存在该条单据在补充工厂审核节点（建议校验单据号和当前节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20548(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在基带工程师审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20549(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在基带工程师审批页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20550(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在基带工程师审批页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20551(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在基带工程师审批页面中，转交单据成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20552(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，基带工程师审批，审批成功")  # 用例名称
    @allure.description("基带工程师审批页面中，所有数据都正确，点击同意，可以提交成功并给出提示'处理成功，审核通过'，页面成功跳转成功处理了基带工程师审批节点，我的待办中不存在该条数据在基带工程师审批节点（建议校验单据号和当前节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20553(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，基带工程师审批回退到业务审核成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击回退，选择回退到补充工厂页面，查看我的待办中存在补充工厂节点（校验单据号和节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20554(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在基带工程师审批页面中，拒绝成功")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击拒绝，会显示处理成功，并且页面跳转")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20555(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在采购审核（NPS）页面中，审批成功")  # 用例名称
    @allure.description("在采购审核（NPS）页面中，点击同意，可以提交成功并给出提示'处理成功，审核通过'，页面成功跳转成功处理了采购审核（NPS）节点，我的待办中不存在该条数据在采购审核（NPS）节点（建议校验单据号和当前节点）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20556(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在采购审核（NPS）页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例名称
    @allure.description("在采购审核（NPS）页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20557(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在采购审核（NPS）页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在采购审核（NPS）页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20558(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在采购审核（NPS）页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在采购审核（NPS）页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20559(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在采购审核（NPS）页面中，转交单据成功")  # 用例名称
    @allure.description("在采购审核（NPS）页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20560(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在采购审核（NPS）页面中，拒绝成功")  # 用例名称
    @allure.description("在采购审核（NPS）页面中，点击拒绝，会显示处理成功，并且页面跳转")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20561(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，业务审核页面，产成品数据不能编辑")  # 用例名称
    @allure.description("在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20562(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，业务审核成功")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择通过，添加名字为检查结果的附件，点击同意按钮，给出提示，并且页面跳转成功，跳转成功后，我的待办中不存在该条业务审核单据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20563(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，业务审核页面，回退到补充工厂再审核，还是业务审核节点")  # 用例名称
    @allure.description("在我的待办中审批从业务审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是业务审核节点，而不是BOM工程师节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20564(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20565(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在业务审核页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20566(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在业务审核页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20567(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在业务审核页面中，转交单据成功")  # 用例名称
    @allure.description("在业务审核页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20568(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在数据组审批页面中，回退到补充工厂再审核，还是业务审核节点")  # 用例名称
    @allure.description("在我的待办中审批从数据组审核页面回退到补充工厂页面的单据，在补充工厂同意并审核成功，下个节点是数据组审核节点，而不是基带工程师审批节点")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20569(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在数据组审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，不选择转交的人直接点击确认，是不存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20570(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在数据组审批页面中，选择转交人转交，存在确定转交按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，存在确定转交按钮")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20571(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在数据组审批页面中，选择转交人转交取消，存在转交，回退按钮")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人后点击取消按钮，页面中恢复到原来的页面（判断是否存在转交，回退按钮）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20572(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，在数据组审批页面中，转交单据成功")  # 用例名称
    @allure.description("在数据组审批页面中，点击转交，选择转交的人直接点击确认，点击确定转交，页面跳转，并且该条单据转交到选择的人身上")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20573(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查为成功，点击同意，能提交成功，并且给出提交成功的提示")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20574(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=衍生BOM，数据组审批页面，审批成功")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查为成功，点击同意，能提交成功，并且给出提交成功的提示")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20575(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=【生产工厂信息】物料xxxxxx的组包工厂不能为空")  # 用例名称
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示【生产工厂信息】物料xxxxxx的贴片工厂不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20576(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=未选择BOM,一键填写按钮无法被点击")  # 用例名称
    @allure.description("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20577(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=请选择工厂分类/请选择工厂")  # 用例名称
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，直接点击确认，不能进行确认并给出必填提示'请选择工厂分类'、'请选择工厂'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20578(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=检查贴片工厂不能为空！")  # 用例名称
    @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示检查贴片工厂不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20579(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=检查贴片工厂不能为空！")  # 用例名称
    @allure.description("在补充工厂页面中，不填写贴片工厂直接点击一键/，给出提示XXX物料必填一个贴片工厂")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20580(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=14400003的数量和位号个数不一致")  # 用例名称
    @allure.description("在基带工程师审批页面中，点击编辑，将14400003数量改为1，点击同意，提示'14400003的数量和位号个数不一致'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20581(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=业务审核的必填项需填写完整！")  # 用例名称
    @allure.description("在基带工程师审批页面中，业务审核不选择人，点击同意，提示'业务审核的必填项需填写完整！'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20582(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=自检清单检查角色未选择")  # 用例名称
    @allure.description("在业务审核页面中，不填写任何内容，点击同意，不能提交成功，并给出提示'自检清单检查角色未选择'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20583(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=自检清单第【1】行检查结果未选择")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，选择后直接点击同意，不能提交成功，并给出提示'自检清单第【1】行检查结果未选择'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20584(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择不通过，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20585(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择不涉及，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20586(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=自请上传检查结果")  # 用例名称
    @allure.description("在业务审核页面中，正确填写自检清单，不添加附件，点击同意，提示'请上传检查结果'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20587(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=只能上传文件名为‘检查结果’的文件")  # 用例名称
    @allure.description("在业务审核页面中，正确填写自检清单，添加名字不为检查结果的附件，提示'只能上传文件名为‘检查结果’的文件'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20588(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=数据组审批页面，检查失败项不为0，提交失败")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查有失败项，点击同意，不能提交成功，并且给出提交失败的提示")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20589(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，【生产工厂信息】物料12198883的贴片工厂不能为空")  # 用例名称
    @allure.description("在补充工厂页面中，不进行填写任何数据，点击同意，不能提交成功，并给出提示'【生产工厂信息】物料xxxxxxxx的贴片工厂不能为空'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20590(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，未选择BOM,一键填写按钮无法被点击")  # 用例名称
    @allure.description("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20591(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，请选择工厂分类/请选择工厂")  # 用例名称
    @allure.description("在补充工厂页面中，选择BOM，点击一键填写，直接点击确认，不能进行确认并给出必填提示'请选择工厂分类'、'请选择工厂'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20592(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，检查贴片工厂不能为空！")  # 用例名称
    @allure.description("在补充工厂页面中，不填写贴片工厂直接点击一键/，给出提示XXX物料必填一个贴片工厂")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20593(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，检查贴片工厂不能为空！")  # 用例名称
    @allure.description("在补充工厂页面中，不选择检查贴片工厂，点击同意，不能提交成功，并给出提示检查贴片工厂不能为空！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20594(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，BOM[XXXXXXX]中的物料[XXXXXXX]位号个数与数量不一致，请检查后提交")  # 用例名称
    @allure.description("在基带工程师审批页面中，衍生差异信息中位号填多个，将BOM数量改为1，点击生成BOM，提示'BOM[12198883]中的物料[12300002]位号个数与数量不一致，请检查后提交'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20595(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，自检清单检查角色未选择")  # 用例名称
    @allure.description("在业务审核页面中，不填写任何内容，点击同意，不能提交成功，并给出提示'自检清单检查角色未选择'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20596(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，自检清单第【1】行检查结果未选择")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，选择后直接点击同意，不能提交成功，并给出提示'自检清单第【1】行检查结果未选择'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20597(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择不通过，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不通过需填写原因及修改建议")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20598(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例名称
    @allure.description("在业务审核页面中，在自检清单中业务类型选择手机，检查角色选择检查人，在检查结果中选择不涉及，不填写原因及修改意见，直接点击同意按钮，不能提交成功，并给出提示自检清单第【1】行检查结果为不涉及需填写原因及修改建议")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20599(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，自请上传检查结果")  # 用例名称
    @allure.description("在业务审核页面中，正确填写自检清单，不添加附件，点击同意，提示'请上传检查结果'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20600(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，只能上传文件名为‘检查结果’的文件")  # 用例名称
    @allure.description("在业务审核页面中，正确填写自检清单，添加名字不为检查结果的附件，提示'只能上传文件名为‘检查结果’的文件'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20601(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=BOM衍生，数据组审批页面，检查失败项不为0，提交失败")  # 用例名称
    @allure.description("在数据组审批页面中，子阶BOM检查有失败项，点击同意，不能提交成功，并且给出提交失败的提示")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20602(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在查询页面，标题查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入'李小素'，点击查询，查询结果为所有标题包含'李小素'的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20603(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在查询页面，查询不存在标题，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的标题，点击查询，查询结果为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20604(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在查询页面，流程编码查询结果正确")  # 用例名称
    @allure.description("在查询页面，流程编码输入框输入'1'，点击查询，查询结果为所有流程编码包含'1'的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20605(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在查询页面，查询不存在流程编码，结果为空")  # 用例名称
    @allure.description("在查询页面，标题输入框输入不存在的流程编码，点击查询，查询结果为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20606(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在查询页面，PCBABOM衍生查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为客供BOM衍生，点击查询，查询结果为所有制作类型为PCBABOM衍生的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20607(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在查询页面，PCBABOM制作查询结果正确")  # 用例名称
    @allure.description("在查询页面，下拉框选择为PCBABOM制作，点击查询，查询结果为所有制作类型为PCBABOM制作的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20608(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在查询页面，组合查询结果正确")  # 用例名称
    @allure.description("在查询页面，标题输入框输入'李小素'，流程编码输入框输入'1'，BOM编码输入'2'，下拉框选择为PCBABOM制作，点击查询，查询结果为所有标题包含'李小素'、流程编码包含'1'、物料编码包含'2'、制作类型为PCBABOM制作的信息")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20609(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在查询页面，编辑正常")  # 用例名称
    @allure.description("在查询页面，点击编辑，跳转至oneworks编辑页面，可以编辑页面信息、提交、保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20610(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("BOM协作PCBABOM协作=在查询页面，删除取消无变动")  # 用例名称
    @allure.description("在查询页面，点击删除，提示是否确认删除，点击取消，取消成功，页面无变动")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20611(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=创建流程成功")  # 用例名称
    @allure.description("进入新增页面，输入项目信息（项目输入未存在的项目，其他随便填），填写业务审核，点击提交，提示操作成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20612(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=摄像头闪光灯节点，审批成功")  # 用例名称
    @allure.description("摄像头闪光灯节点，关键器件中的摄像头闪光灯节点，点击左侧三角，点击下面的模块，点击物料编码右侧的加号，物料编码下面出现一行，点击新出现这行的加号，填写代申请编码信息，点击其他模块保存成功（像这样随便填几个模块），点击同意，提示操作成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20613(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=硬件电子料基带节点，审批成功")  # 用例名称
    @allure.description("硬件电子料基带节点，关键器件中的硬件电子料基带节点，点击左侧三角，点击下面的模块，点击物料编码右侧的加号，物料编码下面出现一行，点击新出现这行的加号，填写代申请编码信息，点击其他模块保存成功（像这样随便填几个模块），点击同意，提示操作成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20614(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=标准化代表节点，审批成功")  # 用例名称
    @allure.description("标准化代表节点，找到标准化评估责任人，点击左侧全选，点击右侧一键填写，弹出一键填写框，字段名称选择责任人，责任人选择xxx，点击确定，提示已选分类的审批人设置成功，点击关闭按钮，弹框关闭，点击同意，提示操作成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20615(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=采购代表节点，审批成功")  # 用例名称
    @allure.description("采购代表节点，找到采购评估责任人，点击左侧全选，点击右侧一键填写，弹出一键填写框，字段名称选择资源商务，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购执行，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购PTC，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购SQM，责任人选择xxx，点击确定。提示已选分类的审批人设置成功，点击关闭按钮，弹框关闭，点击同意，提示操作成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20616(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=资源商务评估节点，审批成功")  # 用例名称
    @allure.description("资源商务评估节点，（所有前面填过信息的这里都可以填采购评估资源商务）勾选是否新供应商、国产化属性、供应商选择原因类别、是否客供物料、价格趋势（6个月）、是否NUDD、评审结论（选通过或者选建议修改，填原因及修改建议），填写供应商选择原因、份额（只能输数字1100）、关联物料（只能填物料）、NUDD说明、NUDD管理方案、原因及修改建议；点击同意，有必填不填时有提示，点击确定")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20617(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=采购执行评估节点，审批成功")  # 用例名称
    @allure.description("采购执行评估节点，（所有前面填过信息的这里都可以填采购评估采购执行）勾选产能评审结论（选通过或者选建议修改，填原因及修改建议），填写L/T天、最小下单量pcs、此项目峰值需求K/M、供应商总产能K/M、分配传音产能K/M、供应弹性、共用项目需求合计K/M、此项目产能分配")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20618(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=采购PTC评估节点，审批成功")  # 用例名称
    @allure.description("采购PTC评估节点，（所有前面填过信息的这里都可以填采购评估PTC）勾选评审结论（选通过或者选不同意，填原因及修改建议），填写原因及修改建议，，点击同意，有必填不填时有提示，点击确定")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20619(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=采购SQM评估节点，审批成功")  # 用例名称
    @allure.description("采购SQM评估节点，（所有前面填过信息的这里都可以填采购评估SQM）勾选评审结论（选通过或者选不同意，填原因及修改建议），填写原因及修改建议，点击同意，有必填不填时有提示，点击确定")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20620(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=标准化部评估节点，审批成功")  # 用例名称
    @allure.description("关键器件关键器件流程，查看单据状态已变为审批通过")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20621(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=请完善项目信息！")  # 用例名称
    @allure.description("进入关键器件新增页面，不输入项目，其他的内容正确填写，点击提交，提示请完善项目信息！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20622(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=不完全填写维护关键器件，提示请完善业务审核信息！")  # 用例名称
    @allure.description("进入关键器件新增页面，项目信息和评估关键器件信息完全填写，不完全填写维护关键器件，直接点击提示，提示请完善业务审核信息！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20623(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=不输入评估关键器件信息，提示请完善业务审核信息！")  # 用例名称
    @allure.description("进入关键器件新增页面，项目基本信息都完全填写，不输入评估关键器件信息，直接点击提交，提示请完善业务审核信息！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20624(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件查询=进入关键器件修订发起页面,查看关键器件业务审核维护关键器件显示是否正确")  # 用例名称
    @allure.description("进入关键器件修订发起页面，查看业务审核中维护关键器件部分的内容是否正确（例如摄像头闪光灯，硬件电子料基带）")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20625(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件查询=关键器件修订发起成功")  # 用例名称
    @allure.description("进入关键器件修订发起页面，选择业务审核中维护关键器件部分的人员为多个人，发起成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20626(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件查询=请勿重复维护关键器件角色！")  # 用例名称
    @allure.description("进入关键器件修订发起页面，选择业务审核中维护关键器件部分的人员为同一个人，点击提交，提示请勿重复维护关键器件角色！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20627(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=摄像头闪光灯节点，审批成功")  # 用例名称
    @allure.description("摄像头闪光灯节点，关键器件中的摄像头闪光灯节点，点击左侧三角，点击下面的模块，点击物料编码右侧的加号，物料编码下面出现一行，点击新出现这行的加号，填写代申请编码信息，点击其他模块保存成功（像这样随便填几个模块），点击同意，提示操作成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20628(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=硬件电子料基带节点，审批成功")  # 用例名称
    @allure.description("硬件电子料基带节点，关键器件中的硬件电子料基带节点，点击左侧三角，点击下面的模块，点击物料编码右侧的加号，物料编码下面出现一行，点击新出现这行的加号，填写代申请编码信息，点击其他模块保存成功（像这样随便填几个模块），点击同意，提示操作成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20629(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=标准化代表节点，审批成功")  # 用例名称
    @allure.description("标准化代表节点，找到标准化评估责任人，点击左侧全选，点击右侧一键填写，弹出一键填写框，字段名称选择责任人，责任人选择xxx，点击确定，提示已选分类的审批人设置成功，点击关闭按钮，弹框关闭，点击同意，提示操作成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20630(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=采购代表节点，审批成功")  # 用例名称
    @allure.description("采购代表节点，找到采购评估责任人，点击左侧全选，点击右侧一键填写，弹出一键填写框，字段名称选择资源商务，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购执行，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购PTC，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购SQM，责任人选择xxx，点击确定。提示已选分类的审批人设置成功，点击关闭按钮，弹框关闭，点击同意，提示操作成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20631(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=资源商务评估节点，审批成功")  # 用例名称
    @allure.description("资源商务评估节点，（所有前面填过信息的这里都可以填采购评估资源商务）勾选是否新供应商、国产化属性、供应商选择原因类别、是否客供物料、价格趋势（6个月）、是否NUDD、评审结论（选通过或者选建议修改，填原因及修改建议），填写供应商选择原因、份额（只能输数字1100）、关联物料（只能填物料）、NUDD说明、NUDD管理方案、原因及修改建议；点击同意，有必填不填时有提示，点击确定")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20632(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=采购执行评估节点，审批成功")  # 用例名称
    @allure.description("采购执行评估节点，（所有前面填过信息的这里都可以填采购评估采购执行）勾选产能评审结论（选通过或者选建议修改，填原因及修改建议），填写L/T天、最小下单量pcs、此项目峰值需求K/M、供应商总产能K/M、分配传音产能K/M、供应弹性、共用项目需求合计K/M、此项目产能分配")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20633(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=采购PTC评估节点，审批成功")  # 用例名称
    @allure.description("采购PTC评估节点，（所有前面填过信息的这里都可以填采购评估PTC）勾选评审结论（选通过或者选不同意，填原因及修改建议），填写原因及修改建议，，点击同意，有必填不填时有提示，点击确定")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20634(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=采购SQM评估节点，审批成功")  # 用例名称
    @allure.description("采购SQM评估节点，（所有前面填过信息的这里都可以填采购评估SQM）勾选评审结论（选通过或者选不同意，填原因及修改建议），填写原因及修改建议，点击同意，有必填不填时有提示，点击确定")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20635(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("关键器件关键器件流程=标准化部评估节点，审批成功后可以再次发起修订流程")  # 用例名称
    @allure.description("关键器件关键器件流程，查看单据状态已变为审批通过，可以再次点击修订勾选几个（例如摄像头闪光灯，硬件电子料基带），发起修订流程")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20636(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=创建流程成功")  # 用例名称
    @allure.description("项目信息随便填，产品定义信息随便填（品牌暂时选择Infinix），选择汇签/抄送人员，点击提交，提示请求成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20637(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=选择全球版本，汇签人员会自动获取人员")  # 用例名称
    @allure.description("进入出货国家流程后，点击进行新增，新增页面选择品牌后，在产品定义信息中点击新增，新增时选择全球版本，选择全球版本后，汇签人员会自动获取人员")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20638(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=新增产品经理和项目经理，查看抄送人员是自动添加登录人产品经理项目经理")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，在产品定义信息中，新增产品经理和项目经理，查看抄送人员是自动添加登录人产品经理项目经理")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20639(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=产品定义信息中存在该条已选择的数据")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，在产品定义信息中，点击变更已有产品，会弹出选择框，选中其中一条数据，点击选择，产品定义信息中存在该条已选择的数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20640(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=产品定义信息中新增一条数据，新增后点击复制成功")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，在产品定义信息中新增一条数据，新增后点击复制，查看是会出现一条相同的数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20641(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=产品定义信息中新增一条数据，删除成功")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，在产品定义信息中，新增多条数据，新增后选择一条进行删除，删除时会弹出提示框'确定删除吗?'，点击确定，该条数据会被删除，页面上不存在该条数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20642(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=上传附件成功")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面所有内容正确填写，点击附件，并且进行选择一个文件上传，能上传成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20643(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=产品部管理员审核成功")  # 用例名称
    @allure.description("出货国家产品部管理员审核,点击同意，提示请求成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20644(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=产品部汇签审核成功")  # 用例名称
    @allure.description("出货国家产品部汇签,点击同意，提示请求成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20645(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=产品经理修改审核成功")  # 用例名称
    @allure.description("出货国家产品经理修改,产品定义信息点击编辑，修改信息后，点击确定，点击同意")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20646(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=产品部管理员复核审核成功")  # 用例名称
    @allure.description("出货国家产品部管理员复核,点击同意，提示请求成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20647(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=项目经理审批审核成功后，流程结束，状态变为审批通过")  # 用例名称
    @allure.description("出货国家抄送（自动抄送，不需要操作）,出货国家出货国家流程，查看单据状态已变为审批通过")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20648(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=请完善项目信息！")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，不填写项目名称，在产品定义信息中进行新增一条数据，点击提交，会提示'请完善项目信息！'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20649(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=产品定义信息不能为空")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，填写项目名称后，不进行新增产品定义信息，点击提交，会给出提示'产品定义信息不能为空'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20650(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=No.1行xxxxx不能为空")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，填写项目名称，在产品定义信息中点击新增，其中一项内容不填写，其他内容正确填写，点击提交，给出提示No.1行xxxxx不能为空")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20651(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=汇签人不能为空")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，所有内容都正确填写，汇签人员进行全部删除，点击提交，会给出提示'汇签人不能为空'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20652(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=抄送人不能为空")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，所有内容都正确填写，汇签人员进行全部删除，点击提交，会给出提示'抄送人不能为空'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20653(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=第2行与第1行产品重复！")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，所有内容都正确填写，将已经填写好的产品定义信息再复制一行，直接提交，会给出提示'第2行与第1行产品重复！'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20654(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家流程=产品定义信息不能为空")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增后产品定义信息不进行新增，直接点击提交，会给出提示'产品定义信息不能为空'")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20655(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=出货国家查询页面，发起变更产品，跳转发起流程页面")  # 用例名称
    @allure.description("进入出货国家查询页面，品牌暂时选择infinix，点击查询，勾选几条，点击变更产品，提示变更产品的产品经理不是当前登录人，是否继续？，点击【是】，提示变更产品的项目名称不一致，是否继续？点击【是】，跳转至单据发起流程页面")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20656(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更产品流程发起成功")  # 用例名称
    @allure.description("进入单据发起流程页面，修改产品定义信息，选择汇签/抄送人员，点击提交，提示请求成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20657(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更国家，变更已有产品成功")  # 用例名称
    @allure.description("选择一条数据点击变更国家，进入变更国家页面，点击变更已有产品，选择一个产品，页面上会多一条选择的产品")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20658(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=查看版本记录，显示不同的版本")  # 用例名称
    @allure.description("选中一条数据点击市场名称进入，进入后点击查看版本记录，会弹出页面，显示不同的版本")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20659(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=查看变更记录，显示变更数据")  # 用例名称
    @allure.description("选中一条数据点击市场名称进入，进入后点击查看变更记录，会弹出新页面，显示变更数据")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20660(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=批量编辑出货/认证备份，变成成功")  # 用例名称
    @allure.description("选中一条数据点击变更国家，进入变更国家页面再次点击变更已有产品，选择多个产品后，点击批量修改，会出现批量修改弹出框，，选择国家区域后，再选择出货/认证备份全部为出货，确定后，所有的产品选择的国家区域都为出货")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20661(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更产品，产品部管理员审核成功")  # 用例名称
    @allure.description("产品部管理员审核点击同意，提示请求成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20662(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更产品，产品部汇签审核成功")  # 用例名称
    @allure.description("产品部汇签点击同意，提示请求成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20663(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更产品，产品经理修改审核成功")  # 用例名称
    @allure.description("产品经理修改产品定义信息点击编辑，修改信息后，点击确定，点击同意")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20664(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更产品，产品部管理员复核审核成功")  # 用例名称
    @allure.description("产品部管理员复核点击同意，提示请求成功")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20665(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更产品成功,单据状态已变为审批通过")  # 用例名称
    @allure.description("变更产品抄送自动抄送，不需要操作出货国家出货国家流程，查看单据状态已变为审批通过")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20666(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更国家成功,区域配置生效")  # 用例名称
    @allure.description("用例流程未配置区域发起流程更改为认证备份，走完流程检查是否为认证备份；")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20667(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更国家，发起流程，流程流转到产品部管理员审核")  # 用例名称
    @allure.description("选择一条数据点击变更国家，进行变更国家页面进行发起流程，流程流转到产品部管理员审核")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20668(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更国家，产品部管理员审核成功")  # 用例名称
    @allure.description("变更国家发起流程后，流程流转到产品部管理员审核，产品部管理员审核点击同意后，流程流转到产品部汇签")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20669(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更国家，产品部汇签审核成功")  # 用例名称
    @allure.description("变更国家发起流程后，流程流转到产品部汇签点击同意后，流程流转到产品经理修改")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20670(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更国家，产品经理修改审核成功")  # 用例名称
    @allure.description("变更国家发起流程后，流程流转到产品经理修改点击同意后，流程流转到产品部管理员复核")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20671(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更国家，产品部管理员复核审核成功")  # 用例名称
    @allure.description("变更国家发起流程后，流程流转到产品部管理员复核点击同意后，流程流转到项目经理审批")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20672(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更国家，单据状态已变为审批通过")  # 用例名称
    @allure.description("变更国家发起流程后，流程流转到产品部管理员复核点击同意后，流程流转直接进行抄送")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20673(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更产品，【xxxxx】产品存在在途单据【xxxxxx】")  # 用例名称
    @allure.description("选中一条数据点击变更产品，进行发起后，再次选中该条数据点击进行变更产品，不能进行发起，并提示【xxxxx】产品存在在途单据【xxxxxx】")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20674(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更国家，第1行产品国家【xxxxx】已经存在流程中单据【xxxxxxx】！")  # 用例名称
    @allure.description("选中一条数据点击变更国家，进行发起后，再次选中该条数据点击变更国家还是变更一样的国家，发起时会给出提示第1行产品国家【xxxxx】已经存在流程中单据【xxxxxxx】！")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20675(self, drivers):
        pass


    @allure.story("自动化测试")  # 用户故事名称
    @allure.title("出货国家出货国家查询=变更国家，项目经理修改页面，修改重复区域提示'第1行产品国家【XXX】已经存在流程中单据'")  # 用例名称
    @allure.description("流程未配置区域发起变更国家流程，柬埔寨更改为认证备份；再次发起变更国家流程，日本更改为认证备份，点击提交，流程走到项目经理修改，将柬埔寨更改为认证备份，点击提交提示重复")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20676(self, drivers):
        pass


if __name__ == '__main__':
      pass
