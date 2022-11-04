import allure
import pytest
@allure.feature("V2_10_7_1计划")  # 迭代名称
class Teststory_14:
    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理品牌新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理品牌进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理管理维度查询/翻页")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理管理维度进入页面。==输入关键字名称，点击查询。==页面存在多页数据时，调整页面显示数据量；前面翻页")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理管理维度新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理管理维度进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存==通过菜单路径DRP管理系统gt系统管理gt维度管理管理维度进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理管理维度编辑")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理管理维度进入页面。==选择一条数据，点击【编辑】，修改名称，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理管理维度启用/禁用")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理管理维度进入页面。==选择一条启用数据，点击【禁用】按钮。==选择一条禁用数据，点击【启用】按钮")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理市场分类查询/翻页")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理市场分类进入页面。==输入关键字名称，点击查询。==页面存在多页数据时，调整页面显示数据量；前面翻页")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理市场分类新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理市场分类进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存==通过菜单路径DRP管理系统gt系统管理gt维度管理市场分类进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理市场分类编辑")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理市场分类进入页面。==选择一条数据，点击【编辑】，修改名称，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理市场分类启用/禁用")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理市场分类进入页面。==选择一条启用数据，点击【禁用】按钮。==选择一条禁用数据，点击【启用】按钮")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理市场划分查询/翻页")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理市场划分进入页面。==输入关键字名称，点击查询。==页面存在多页数据时，调整页面显示数据量；前面翻页")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理市场划分新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理市场划分进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存==通过菜单路径DRP管理系统gt系统管理gt维度管理市场划分进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理市场划分编辑")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理市场划分进入页面。==选择一条数据，点击【编辑】，修改名称，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理市场划分启用/禁用")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理市场划分进入页面。==选择一条启用数据，点击【禁用】按钮==选择一条禁用数据，点击【启用】按钮")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理大区查询/翻页")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理大区进入页面。==输入关键字名称，点击查询。==页面存在多页数据时，调整页面显示数据量；前面翻页")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_15(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理大区新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理大区进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存==通过菜单路径DRP管理系统gt系统管理gt维度管理大区进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理大区编辑")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理大区进入页面。==选择一条数据，点击【编辑】，修改名称，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理大区启用/禁用")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理大区进入页面。==选择一条启用数据，点击【禁用】按钮。==选择一条禁用数据，点击【启用】按钮")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理组织查询/翻页")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理组织进入页面。==输入关键字名称，点击查询。==页面存在多页数据时，调整页面显示数据量；前面翻页")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理组织新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理组织进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存==通过菜单路径DRP管理系统gt系统管理gt维度管理组织进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理组织编辑")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理组织进入页面。==选择一条数据，点击【编辑】，修改名称，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理组织启用/禁用")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理组织进入页面。==选择一条启用数据，点击【禁用】按钮。==选择一条禁用数据，点击【启用】按钮")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理品牌查询/翻页")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理品牌进入页面。2.输入关键字名称，点击查询。3.页面存在多页数据时，调整页面显示数据量；前面翻页")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理品牌编辑")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理品牌进入页面。==选择一条数据，点击【编辑】，修改名称，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_25(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理品牌启用/禁用")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理品牌进入页面。==选择一条启用数据，点击【禁用】按钮。==选择一条禁用数据，点击【启用】按钮")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_26(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理国家查询/翻页")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理国家进入页面。==输入关键字名称，点击查询。3.页面存在多页数据时，调整页面显示数据量；前面翻页")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_27(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理国家新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理国家进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存==通过菜单路径DRP管理系统gt系统管理gt维度管理国家进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理国家编辑")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理国家进入页面。==选择一条数据，点击【编辑】，修改名称，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_29(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理国家启用/禁用")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理国家进入页面。==选择一条启用数据，点击【禁用】按钮。==选择一条禁用数据，点击【启用】按钮")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理数据版本查询/翻页")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理评审版本进入页面。==输入关键字名称，点击查询。3.页面存在多页数据时，调整页面显示数据量；前面翻页==通过菜单路径DRP管理系统gt系统管理gt维度管理数据版本进入页面。==输入关键字名称，点击查询。3.页面存在多页数据时，调整页面显示数据量；前面翻页")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理数据版本新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理评审版本进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存==通过菜单路径DRP管理系统gt系统管理gt维度管理评审版本进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存==通过菜单路径DRP管理系统gt系统管理gt维度管理数据版本进入页面。==点击【新增】按钮，输入ID、编码、名称Zh、名称En，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_32(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理数据版本编辑")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理评审版本进入页面。==选择一条数据，点击【编辑】，修改名称，点击保存==通过菜单路径DRP管理系统gt系统管理gt维度管理数据版本进入页面。==选择一条数据，点击【编辑】，修改名称，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_33(self, drivers):
        pass


    @allure.story("维度管理拓展到系统所有基本业务属性字段管理")  # 用户故事名称
    @allure.title("维度管理数据版本启用/禁用")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt维度管理评审版本进入页面。==选择一条启用数据，点击【禁用】按钮。==选择一条禁用数据，点击【启用】按钮==通过菜单路径DRP管理系统gt系统管理gt维度管理数据版本进入页面。==选择一条启用数据，点击【禁用】按钮。==选择一条禁用数据，点击【启用】按钮")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_34(self, drivers):
        pass


@allure.feature("V2_10_7_1计划")  # 迭代名称
class Teststory_15:
    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP0查询")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP0进入页面。==输入关键字名称，点击查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_35(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP0编辑评审节点")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP0进入页面，查看评审节点。==点击评审节点，修改评审节点名称，输入数字、汉字、字母==通过菜单路径DRP管理系统gt系统管理gt评审管理DRP0进入页面，查看评审节点。")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_36(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP0新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP0进入页面。==点击【新增】按钮，新增一行，负责人栏位，通过用户中心选择公司内的人员，单选；授权角色下拉显示权限中心的全部角色，仅单选，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_37(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP0删除")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP0进入页面。==选择一条数据，点击【删除】")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_38(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1查询")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1进入页面。==输入关键字名称，点击查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_39(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1编辑评审节点")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1进入页面，查看评审节点。==点击评审节点，修改评审节点名称，输入数字、汉字、字母==通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1进入页面，查看评审节点。")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_40(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1进入页面。==点击【新增】按钮，新增一行，负责人栏位，通过用户中心选择公司内的人员，单选；授权角色下拉显示权限中心的全部角色，仅单选，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_41(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1删除")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1进入页面。==选择一条数据，点击【删除】")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_42(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1评审查询")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1评审进入页面。==输入关键字名称，点击查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_43(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1评审编辑评审节点")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1评审进入页面，查看评审节点。==点击评审节点，修改评审节点名称，输入数字、汉字、字母==通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1评审进入页面，查看评审节点。")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_44(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1评审新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1评审进入页面。==点击【新增】按钮，新增一行，负责人栏位，通过用户中心选择公司内的人员，单选；授权角色下拉显示权限中心的全部角色，仅单选，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_45(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1评审删除")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1评审进入页面。==选择一条数据，点击【删除】")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_46(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1评审品牌查询")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1评审品牌进入页面。==输入关键字名称，点击查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_47(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1评审品牌编辑评审节点")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1评审品牌进入页面，查看评审节点。==点击评审节点，修改评审节点名称，输入数字、汉字、字母==通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1评审品牌进入页面，查看评审节点。")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_48(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1评审品牌新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1评审品牌进入页面。==点击【新增】按钮，新增一行，负责人栏位，通过用户中心选择公司内的人员，单选；授权角色下拉显示权限中心的全部角色，仅单选，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_49(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP1评审品牌删除")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP1评审品牌进入页面。==选择一条数据，点击【删除】")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_50(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP2查询")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP2进入页面。==输入关键字名称，点击查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_51(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP2编辑评审节点")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP2进入页面，查看评审节点。==点击评审节点，修改评审节点名称，输入数字、汉字、字母==通过菜单路径DRP管理系统gt系统管理gt评审管理DRP2进入页面，查看评审节点。")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_52(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP2新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP2进入页面。==点击【新增】按钮，新增一行，负责人栏位，通过用户中心选择公司内的人员，单选；授权角色下拉显示权限中心的全部角色，仅单选，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_53(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP2删除")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP2进入页面。==选择一条数据，点击【删除】")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_54(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP2差异确认查询")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP2差异确认进入页面。==输入关键字名称，点击查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_55(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP2差异确认编辑评审节点")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP2差异确认进入页面，查看评审节点。==点击评审节点，修改评审节点名称，输入数字、汉字、字母==通过菜单路径DRP管理系统gt系统管理gt评审管理DRP2差异确认进入页面，查看评审节点。")  # 用例描述
    @allure.severity("minor")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_56(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP2差异确认新增")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP2差异确认进入页面。==点击【新增】按钮，新增一行，负责人栏位，通过用户中心选择公司内的人员，单选；授权角色下拉显示权限中心的全部角色，仅单选，点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_57(self, drivers):
        pass


    @allure.story("新增评审管理功能配置评审节点负责人")  # 用户故事名称
    @allure.title("评审管理DRP2差异确认删除")  # 用例名称
    @allure.description("通过菜单路径DRP管理系统gt系统管理gt评审管理DRP2差异确认进入页面。==选择一条数据，点击【删除】")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_58(self, drivers):
        pass


@allure.feature("V2_10_7_1计划")  # 迭代名称
class Teststory_11:
    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("【DRP管理】一级菜单下新增【DRP2国家销售版/DRP2NationalSalesVer.】二级菜单，菜单权限控制准确")  # 用例名称
    @allure.description("登录DRP进入DRP管理菜单导航，查看下级菜单==统一用户中心去除用户对应菜单权限，返回DRP查看DRP管理下级菜单")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_102(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("销售版展示数据与用户数据权限保持一致")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版，查看销售版主页面展示数据")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_103(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版主页面页面信息完整，排版布局美观")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==主页面信息检查")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_104(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面查询条件下拉项与用户权限保持一致")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==查询条件提报周期、品牌、管理维度下拉框检查")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_105(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面各项查询，单项/联合查询成功，查询结果正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==切换提报周期查询==选择品牌进行查询==选择管理维度进行查询==联合查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_106(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面查询后进行重置，重置成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择查询条件查询后，点击重置")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_107(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面下载导入模板成功，文件格式内容正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==点击导入下载导入文件")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_108(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面导入管理维度和品牌不匹配，导入失败")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==点击导入，选择管理维度和品牌不匹配的文件进行导入")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_109(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面导入国家不在管理维度内，导入失败")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==点击导入，选择的国家不在管理维度内文件进行导入")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_110(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面导入机型、市场名、品牌不匹配，导入失败")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==点击导入，选择机型、市场名、品牌不匹配的文件进行导入")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_111(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面导入数据缺少关键字段数据，导入失败")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==点击导入，选择数据缺少关键字段数据的文件进行导入")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_112(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主页面导入文件内容合规的数据文件的，导入成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==点绕导入，选择文件内容合规的数据文件进行导入")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_113(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，不同数据状态的数据，按钮显隐不同")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==待发布状态数据，按钮检查==已发布状态数据，按钮检查")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_114(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面撤回按钮单独受权限控制显隐")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==设置用户撤回按钮权限，查看已发布状态数据==取消用户撤回按钮权限，查看已发布状态数据")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_115(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择单条待发布状态进行发布，发布成功，各状态流转正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择一条待发布状态数据，点击发布")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_116(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择多条待发布状态进行发布，发布成功，各状态流转正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择多条待发布状态数据，点击发布")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_117(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择多条含有已发布状态数据进行发布，发布失败")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择多条含有已发布状态数据进行发布")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_118(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择多条待发布数据确认删除，删除成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择多条待发布状态数据进行删除==确认删除")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_119(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择多条含有非待发布数据确认删除，删除失败")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择多条含有非待发布数据点击批量删除")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_120(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择多条待发布数据点击删除后取消，取消成功，数据无变更")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择多条待发布数据点击删除后取消")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_121(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面确认撤回数据成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择已发布数据点击撤回==确认撤回")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_122(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面取消撤回数据成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择已发布数据点击撤回==取消撤回")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_123(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面撤回数据后，重新发布成功，数据记录正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择已发布数据点击撤回==确认撤回==再次确认发布该数据")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_124(self, drivers):
        pass


    @allure.story("销售版DRP增加列表管理界面并支持状态控制")  # 用户故事名称
    @allure.title("DRP2国家销售版，主界面选择数据批量导出成功，数据内容正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择多条数据，点击批量导出")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_125(self, drivers):
        pass


@allure.feature("V2_10_7_1计划")  # 迭代名称
class Teststory_7:
    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情页面中头部信息完整")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==编辑详情title页面检查")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_126(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面精简模式和标准模式信息表单信息完整")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==明细页面标准和精简模式表单检查")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_127(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面，各项查询条件单项和联合查询成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==明细页面单项查询==联合查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_128(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面，导出数据成功，导出文件数据内容正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==明细页面点击导出")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_129(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面，确认删除机型成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==明细页面选择机型进行批量/单条删除==确认删除")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_130(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面，取消删除机型成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==明细页面选择机型进行批量/单条删除==取消删除")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_131(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情明细页面，在线编辑修改数据成功，保存成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==明细页面选择机型点击编辑==修改数据点击保存")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_132(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情总量页面，精简模式和标准模式信息表单完整")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==总量页面精简模式/总量模式检查")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_133(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情总量页面，各项查询条件单项和联合查询成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==总量页面单项查询==联合查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_134(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情总量页面，导出数据成功，导出文件数据内容正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==总量页面点击导出")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_135(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情页面，发布成功，数据变更正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==点击发布")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_136(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，编辑详情页面，返回成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击编辑==点击返回")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_137(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，查看详情页面，各页面元素与编辑页面保持一致")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择待发布数据点击查看==查看详情明细页面检查==查看详情总量页面检查")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_138(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，查看详情明细页面，各项查询条件单项和联合查询成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择已发布数据点击查看==明细页面单项查询==联合查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_139(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，查看详情总量页面，各项查询条件单项和联合查询成功")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择已发布数据点击查看==总量页面单项查询==联合查询")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_140(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，查看详情总量页面，导出数据成功，导出文件数据内容正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择已发布数据点击查看==总量页面点击导出")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_141(self, drivers):
        pass


    @allure.story("销售版DRP增加详情数据查看及编辑界面")  # 用户故事名称
    @allure.title("DRP2国家销售版，查看详情明细页面，导出数据成功，导出文件数据内容正确")  # 用例名称
    @allure.description("登录DRP，进入DRP管理DRP2国家销售版==选择已发布数据点击查看==明细页面点击导出")  # 用例描述
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_142(self, drivers):
        pass


if __name__ == '__main__':
      pass
