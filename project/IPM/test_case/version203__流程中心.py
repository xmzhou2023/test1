import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from libs.common.action import KeyWord
import allure


@allure.feature("流程中心")  # 迭代名称
class Teststory_3294:
    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料申请点击物料申请，进入到物料申请页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23598(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/标题50个字符，必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23599(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/流程编码文本框只读，提交流程后，OneWorks自动生成流程的编码")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23600(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/申请人文本框只读，系统自动识别申请人名称并展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23601(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/申请部门文本框只读，系统自动识别申请人部门信息并展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23602(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/申请日期日期只读，系统自动生成，格式按照yyyyMMdd展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23603(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/申请类型下拉，值范围'手机物料/ODM物料/二级物料/手机物料二级BOM'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23604(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/申请类型必填，根据所选择申请类型后，加载页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23605(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("新增新增按钮，可以添加多个物料类型区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23606(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("全部展开全部展开所有的物料类型区域所有的物料数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23607(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("全部折叠全部折叠所有的物料类型区域所有的物料数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23608(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型下拉选择，必填，默认显示一个物料类型区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23609(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型下拉选择物料类型后，展示此物料类型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23610(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型按照分级的树型菜单联动展示所有物料类型，可支持搜索")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23611(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型物料类型的选值范围根据【申请类型】做过滤")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23612(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型若为'手机物料'及'ODM物料'，所有启用的物料对象类型都可选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23613(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型若为'二级物料'，9开头的所有物料组的启用的对象类型，支持配置实现")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23614(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型若为'二级BOM'，170、171、172、174、176、250、251的物料组的启用的对象类型，支持配置实现")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23615(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型选择物料类型后，默认带出物料数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23616(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型选择物料类型只能选择叶子节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23617(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型区域/删除支持删除，点击删除提示'请确定是否删除当前的物料类型区域'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23618(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型区域/全屏点击全屏，全屏展示此物料类型区域的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23619(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型区域/退出全屏全屏展示物料区域的数据后，点击退出全屏按钮后，物料区域的数据退出全屏")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23620(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型区域/全部展开全部展开所有的物料类型区域所有的物料数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23621(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型区域/全部折叠全部折叠所有的物料类型区域所有的物料数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23622(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型/重新选择点击重新选择，提示'已填写的物料数据将会清空，请确认'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23623(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("新增点击'按钮'新增一行物料数据（下面），展开新增的一行物料数据，光标定位到新的物料数据上，便于填写")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23624(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("删除点击'按钮'删除一行物料数据，删除时，提示'请确定是否删除当前选中的物料'，点确定删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23625(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("复制点击'复制按钮'复制一行物料数据，当前物料之后，光标定位到新的物料数据上，便于填写")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23626(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("复制前端复制所有填好的属性字段，合成属性也能够自动带出，全复制所有属性数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23627(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("签审人员信息签审人员信息，选择申请类型后，默认显示这块区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23628(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("角色解析其他的角色信息按照选择的'申请类型''物料类型'动态加载角色")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23629(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("抄送人员设置流程中设置固定人员，不在流程节点中体现，流程完成后，邮件及飞书通知给抄送人员")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23630(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("抄送邮件邮件内容，'标题'的流程审批通过，申请物料以表格展示，具体内容有'物料编码、物料名称、物料描述CN、物料描述EN、原厂代码、原厂描述'。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23631(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("附件附件区域，选择申请类型后，默认显示这块区域，当前区域为流程的附件补充数据，并非物料对象关联文档数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23632(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("提交'提交'按钮，提交当前流程，业务逻辑具体参考'US提交物料/文档/关系创建'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23633(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("提交提交需要验证，必填项是否填写，【标题】，【申请类型】，【物料类型】，必须一条物料数据，物料中定义的约束必填的属性；")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23634(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("提交提交需要验证，不同审批路径（节点）的物料暂时不能同时提交")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23635(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("保存'保存'按钮，保存为我的草稿，业务逻辑具体参考'US提交物料/文档/关系创建'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23636(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("保存保存需要验证，【标题】必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23637(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("保存保存需要验证，不同审批路径（节点）的物料暂时不能同时保存")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23638(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("取消点击取消按钮，提示'您确定要取消当前表单'，确定删除当前表单，取消关闭当前页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23639(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料申请点击物料申请，进入到物料申请页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24144(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/标题50个字符，必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24145(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/流程编码文本框只读，提交流程后，OneWorks自动生成流程的编码")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24146(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/申请人文本框只读，系统自动识别申请人名称并展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24147(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/申请部门文本框只读，系统自动识别申请人部门信息并展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24148(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/申请日期日期只读，系统自动生成，格式按照yyyyMMdd展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24149(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/申请类型下拉，值范围'手机物料/ODM物料/二级物料/手机物料二级BOM'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24150(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("基本信息/申请类型必填，根据所选择申请类型后，加载页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24151(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("新增新增按钮，可以添加多个物料类型区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24152(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("全部展开全部展开所有的物料类型区域所有的物料数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24153(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("全部折叠全部折叠所有的物料类型区域所有的物料数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24154(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型下拉选择，必填，默认显示一个物料类型区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24155(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型下拉选择物料类型后，展示此物料类型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24156(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型按照分级的树型菜单联动展示所有物料类型，可支持搜索")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24157(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型物料类型的选值范围根据【申请类型】做过滤")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24158(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型若为'手机物料'及'ODM物料'，所有启用的物料对象类型都可选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24159(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型若为'二级物料'，9开头的所有物料组的启用的对象类型，支持配置实现")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24160(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型若为'二级BOM'，170、171、172、174、176、250、251的物料组的启用的对象类型，支持配置实现")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24161(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型选择物料类型后，默认带出物料数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24162(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型选择物料类型只能选择叶子节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24163(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型区域/删除支持删除，点击删除提示'请确定是否删除当前的物料类型区域'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24164(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型区域/全屏点击全屏，全屏展示此物料类型区域的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24165(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型区域/退出全屏全屏展示物料区域的数据后，点击退出全屏按钮后，物料区域的数据退出全屏")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24166(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型区域/全部展开全部展开所有的物料类型区域所有的物料数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24167(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型区域/全部折叠全部折叠所有的物料类型区域所有的物料数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24168(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("物料类型/重新选择点击重新选择，提示'已填写的物料数据将会清空，请确认'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24169(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("新增点击'按钮'新增一行物料数据（下面），展开新增的一行物料数据，光标定位到新的物料数据上，便于填写")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24170(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("删除点击'按钮'删除一行物料数据，删除时，提示'请确定是否删除当前选中的物料'，点确定删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24171(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("复制点击'复制按钮'复制一行物料数据，当前物料之后，光标定位到新的物料数据上，便于填写")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24172(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("复制前端复制所有填好的属性字段，合成属性也能够自动带出，全复制所有属性数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24173(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("签审人员信息签审人员信息，选择申请类型后，默认显示这块区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24174(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("角色解析其他的角色信息按照选择的'申请类型''物料类型'动态加载角色")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24175(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("抄送人员设置流程中设置固定人员，不在流程节点中体现，流程完成后，邮件及飞书通知给抄送人员")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24176(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("抄送邮件邮件内容，'标题'的流程审批通过，申请物料以表格展示，具体内容有'物料编码、物料名称、物料描述CN、物料描述EN、原厂代码、原厂描述'。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24177(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("附件附件区域，选择申请类型后，默认显示这块区域，当前区域为流程的附件补充数据，并非物料对象关联文档数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24178(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("提交'提交'按钮，提交当前流程，业务逻辑具体参考'US提交物料/文档/关系创建'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24179(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("提交提交需要验证，必填项是否填写，【标题】，【申请类型】，【物料类型】，必须一条物料数据，物料中定义的约束必填的属性；")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24180(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("提交提交需要验证，不同审批路径（节点）的物料暂时不能同时提交")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24181(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("保存'保存'按钮，保存为我的草稿，业务逻辑具体参考'US提交物料/文档/关系创建'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24182(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("保存保存需要验证，【标题】必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24183(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("保存保存需要验证，不同审批路径（节点）的物料暂时不能同时保存")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24184(self, drivers):
        pass

    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title("取消点击取消按钮，提示'您确定要取消当前表单'，确定删除当前表单，取消关闭当前页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24185(self, drivers):
        pass


@allure.feature("流程中心")  # 迭代名称
class Teststory_3285:
    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("点击'结构开模申请'的卡片，全屏弹出'结构开模申请'的页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23993(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("权限拥有结构开模文档对象的创建权限才可创建流程表单")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23994(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("基本信息/标题文本框只读，50个字符组成，生成规则项目名称开模申请单申请人申请日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23995(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("基本信息/单据号文本框只读，20个字符组成，前四位JGKM")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23996(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("基本信息/申请人文本框只读，20个字符组成，系统自动识别申请人名称并展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23997(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("基本信息/申请部门文本框只读，20个字符组成，系统自动识别申请人部门信息并展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23998(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("基本信息/申请日期日期只读，系统自动生成，格式按照yyyyMMdd展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23999(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("开模信息/项目名称文本下拉选项,展示已有的研发项目实例查看权限且（生命周期状态为进行中的项目）及结构开模文档的创建权限，单选择框，支持输入，快速匹配选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24000(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("开模信息/所属品牌文本下拉框，单选框，下拉值Infinix/itel/TECNO，在数据字典中配置")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24001(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("开模信息/月需求量文本输入框，20个字符")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24002(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("开模信息/描述文本域，2000字符")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24003(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/NO序号按照新增顺序升序排序")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24004(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/物料描述文本输入框，200char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24005(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/物料工艺文本输入框，200char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24006(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/塑胶材质文本输入框，200char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24007(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/开模方式文本输入框，50char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24008(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/投模日期可选择日期为投模日期，YYYYmmdd")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24009(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/一模几穴文本输入框，50char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24010(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/供应商类别下拉框，在接口未实现前，先实现手写功能")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24011(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/一级供应商下拉框，在接口未实现前，先实现手写功能，从SAP获取供应商数据，单选择框，支持输入，快速匹配选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24012(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/关键器件名文本输入框，50char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24013(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格信息/二级供应商下拉框，在接口未实现前，先实现手写功能从SAP获取供应商数据，单选择框，支持输入，快速匹配选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24014(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格操作/新增点击新增按钮，可在表格中新增一条数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24015(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格操作/删除选中表格中的一条数据，点击删除按钮后删除选择的信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24016(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("表格操作/删除可批量选中删除多条数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24017(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("签审人员信息/复制上一单人员获取个人申请的上一个'结构开模'单据的填写的角色表单人员，进行复制，若人员不在当前选择的项目的角色中，跳过")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24018(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("签审人员信息根据所选择项目自动解析此项目团队中的人员")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24019(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("附件根据权限，可对已上传附件进行下载、上传、删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24020(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("附件上传多个附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24021(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('附件删除上传成功的附件')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24022(self, drivers):
        robot = KeyWord(drivers)
        robot.AI_get("http://10.250.112.57/")  # id77287147-4b13-4d95-bbeb-45bb76c4b771
        robot.AI_find_element(By.CSS_SELECTOR, ".hamburger").click()  # id28c141ed-a7ac-47eb-96e0-b85742419d86
        robot.AI_find_element(By.XPATH, "//div[4]/li/div/span").click()  # id617ad7d4-fdbc-4e0b-ad6c-85a29d86df39
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'JS Mgt')]").click()  # id7a54076f-56c8-4ba6-b9e5-5788dc64482d
        robot.AI_find_element(By.XPATH,
                              "//span[contains(.,'JS List')]").click()  # ide2a89d0d-db17-48d2-9bfb-036a2fd523a7
        robot.AI_find_element(By.CSS_SELECTOR,
                              "div:nth-child(2) > .el-button:nth-child(1) > span").click()  # id983e7462-7b79-4803-933c-ed1e8dabf262
        element = robot.AI_find_element(By.CSS_SELECTOR,
                                        "div:nth-child(2) > .el-button:nth-child(1) > span")  # id228184c7-7de4-414f-bbdd-cfe2c9b75723
        actions = ActionChains(robot)
        actions.move_to_element(element).perform()
        element = robot.AI_find_element(By.CSS_SELECTOR, "body")  # id5d32d7de-27e1-4dd4-9cb5-da510be407d7
        actions = ActionChains(robot)
        actions.move_to_element(element).perform()
        element = robot.AI_find_element(By.CSS_SELECTOR,
                                        ".el-button--warning")  # id8d540683-e189-47e6-90c0-f2eebe681ee4
        actions = ActionChains(robot)
        actions.move_to_element(element).perform()
        robot.AI_find_element(By.CSS_SELECTOR, ".hover > span").click()  # id7d94c671-4405-4e90-be48-05210aeb4ba3
        robot.AI_find_element(By.CSS_SELECTOR, ".hover > span").click()  # id9d7be00c-0bfc-469a-b0b4-a03d2dc0eda9

    def test_24130(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("附件删除上传成功的附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24022(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("附件替换上传成功的附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24023(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("附件校验校验上传附件超过1024M，提示'本系统不允许上传大于XXM附件'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24024(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title(
        "附件校验校验上传bat|exe|sh|htm|mht|html|shtml文件，否则提示错误信息'不可上传类型为bat,exe,sh,htm,mht,html,shtml的附件,请修改后提提示'。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24025(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("操作/保存、提交保存提交会在所选择的项目或者域中生成一个结构开模文档实例")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24026(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("操作/保存点击保存按钮，保存为草稿，提交人可在项目或者域中继续检出编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24027(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("保存验证保存为草稿时，不用验证项目经理、采购代表、产品经理为必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24028(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("保存验证验证选择项目时，在此项目中对结构文档需要有创建权限才可保存，如果没有权限则需提示'没有此项目结构开模文档的创建权限'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24029(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("操作/提交点击提交按钮，结构开模表单，提交到下个流程节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24030(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("提交验证点击提交按钮，验证项目经理、采购代表、产品经理必填，未填时需提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24031(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("操作/保存、提交文档的'保存'与'提升'操作，验证必填项处理与流程表单一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24032(self, drivers):
        pass

    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title("操作/提交提交的表单，不可进行编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24033(self, drivers):
        pass


@allure.feature("流程中心")  # 迭代名称
class Teststory_3288:
    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("基本信息/标题文本框只读，50个字符组成，生成规则项目名称开模申请单申请人申请日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24054(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("基本信息/单据号文本框只读，20个字符组成，前四位JGKM")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24055(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("基本信息/申请人文本框只读，20个字符组成，系统自动识别申请人名称并展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24056(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("基本信息/申请部门文本框只读，20个字符组成，系统自动识别申请人部门信息并展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24057(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("基本信息/申请日期日期只读，系统自动生成，格式按照yyyyMMdd展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24058(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("开模信息/项目名称文本下拉选项,展示已有的研发项目实例查看权限且（生命周期状态为进行中的项目）及结构开模文档的创建权限，单选择框，支持输入，快速匹配选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24059(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("开模信息/所属品牌文本下拉框，单选框，下拉值Infinix/itel/TECNO，在数据字典中配置")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24060(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("开模信息/月需求量文本输入框，20个字符")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24061(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("开模信息/描述文本域，2000字符")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24062(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/NO序号按照新增顺序升序排序")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24063(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/物料描述文本输入框，200char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24064(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/物料工艺文本输入框，200char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24065(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/塑胶材质文本输入框，200char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24066(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/开模方式文本输入框，50char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24067(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/投模日期可选择日期为投模日期，YYYYmmdd")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24068(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/一模几穴文本输入框，50char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24069(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/供应商类别下拉框，在接口未实现前，先实现手写功能")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24070(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/一级供应商下拉框，在接口未实现前，先实现手写功能，从SAP获取供应商数据，单选择框，支持输入，快速匹配选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24071(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/关键器件名文本输入框，50char")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24072(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格信息/二级供应商下拉框，在接口未实现前，先实现手写功能从SAP获取供应商数据，单选择框，支持输入，快速匹配选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24073(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格操作/新增点击新增按钮，可在表格中新增一条数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24074(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格操作/删除选中表格中的一条数据，点击删除按钮后删除选择的信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24075(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("表格操作/删除可批量选中删除多条数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24076(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("签审人员信息/复制上一单人员获取个人申请的上一个'结构开模'单据的填写的角色表单人员，进行复制，若人员不在当前选择的项目的角色中，跳过")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24077(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("签审人员信息根据所选择项目自动解析此项目团队中的人员")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24078(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("附件根据权限，可对已上传附件进行下载、上传、删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24079(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("附件上传多个附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24080(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("附件删除上传成功的附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24081(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("附件替换上传成功的附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24082(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("附件校验校验上传附件超过1024M，提示'本系统不允许上传大于XXM附件'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24083(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title(
        "附件校验校验上传bat|exe|sh|htm|mht|html|shtml文件，否则提示错误信息'不可上传类型为bat,exe,sh,htm,mht,html,shtml的附件,请修改后提提示'。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24084(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("操作/保存、提交保存提交会在所选择的项目或者域中生成一个结构开模文档实例")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24085(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("操作/保存点击保存按钮，保存为草稿，提交人可在项目或者域中继续检出编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24086(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("保存验证保存为草稿时，不用验证项目经理、采购代表、产品经理为必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24087(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("保存验证验证选择项目时，在此项目中对结构文档需要有创建权限才可保存，如果没有权限则需提示'没有此项目结构开模文档的创建权限'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24088(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("操作/提交点击提交按钮，结构开模表单，提交到下个流程节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24089(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("提交验证点击提交按钮，验证项目经理、采购代表、产品经理必填，未填时需提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24090(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("操作/保存、提交文档的'保存'与'提升'操作，验证必填项处理与流程表单一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24091(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("操作/提交提交的表单，不可进行编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24092(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("操作/作废点击作废按钮，提示'您确定要作废当前表单'，确定删除当前表单，取消关闭当前页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24093(self, drivers):
        pass

    @allure.story("开模流程/开模流程草稿箱")  # 用户故事名称
    @allure.title("操作/作废点击作废按钮，提示'您确定要作废当前表单'，确定删除当前表单，删除的表单会在项目或者域中同步删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24094(self, drivers):
        pass


@allure.feature("流程中心")  # 迭代名称
class Teststory_3286:
    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("流程页面点击标题，抽屉式打开审核页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24095(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("流程页面如页面所示，支持页面的全屏功能，点击全屏按钮，全屏展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24096(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("流程页面右边页面显示的是平台流程的功能，左下显示的是平台流程的按钮，根据登陆人员显示不同的按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24097(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("流程页面/意见在审批页面中可对当前流程有审批意见在此输入后点击操作按钮后，在查看页面中右侧流程详情会展示意见信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24098(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("流程页面流程中节点支持平台的'沟通'功能")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24099(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("流程页面/表单数据左上显示的是IPM的'结构开模'表单")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24100(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("流程页面/附件审批时可以下载附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24101(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("若为流程的当前节点的审核用户（除专家会签节点外），则显示'同意''拒绝''转交''加签'；若非当前节点的审核用户，则仅仅查看")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24102(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("驳回编辑驳回到发起节点后，申请人可修改表单重新提交，保存后可重新修改表单数据，修改后对象实例版本升版保存")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24103(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("驳回编辑驳回的表单在哪里进行维护")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24104(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("备注相当于对象实例同时做了'检出''修改''检入'动作，检入备注记载'流程表单修改'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24105(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("对象实例状态申请人提交，生命周期状态更改为'正在审阅'；若仍在申请人提交节点（或驳回申请人），生命周期状态更改为'编制中'；流程完成，对象实例生命周期状态更改为'已发布'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24106(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("驳回提交驳回到发起节点后，修改数据后重新提交，仍为同一个流程，重新提交后审批节点不做改变")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24107(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("支持催办（配置催办时间，如1小时一次），可以升级，参考US开模流程催办功能")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24108(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("提交申请结构工程师，在流程申请页面中提交申请后，文档生命周期状态更改为'正在审阅'，流程流转到项目经理节点审批")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24109(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("提交申请结构工程师，在文档实例中提升状态后，文档生命周期状态更改为'正在审阅'，流程流转到项目经理节点审批")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24110(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("我的申请结构工程师，提交申请后，在工作台中流程待办'我申请的'中可查看申请的流程，")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24111(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("提交人在申请节点（含打回重新提交）可以编辑表单，其他节点仅仅查看表单数据（只读）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24112(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("撤回重新撤回功能，尽在申请人提交后，流程还没有审核情况下，在'我申请的'中可对流程进行撤回操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24113(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("撤回申请人提交申请后，流程已进行审批后，此流程不展示撤回操作按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24114(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("同意流程流转到项目经理时，项目经理在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，无问题情况下，点击同意按钮，流程节点流转到采购节点进行审批")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24115(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("拒绝流程流转到项目经理时，项目经理在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，如有问题，点击拒绝按钮时，意见输入框必填，流程终止，驳回到发起节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24116(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("转交流程流转到项目经理时，项目经理在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，可点击转交按钮，填写转交人，此流程会流转到转交人节点进行审批")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24117(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("加签流程流转到项目经理时，项目经理在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，可点击加签按钮，输入加签人员工号后，此流程会同时流转到加签人节点进行审批，项目经理需与加签人员都审批通过后，流程才会流转到下个节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24118(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("同意流程流转到采购时，采购在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，无问题情况下，审批同意时，必须对成本'及'供应商'做确认，判断必须勾选，才能点击提交按钮，流程节点流转到产品节点进行审批")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24119(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("拒绝流程流转到采购时，采购在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，如有问题，点击拒绝按钮，流程终止，驳回到发起节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24120(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("转交流程流转到采购时，采购在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，可点击转交按钮，填写转交人，此流程会流转到转交人节点进行审批")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24121(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("加签流程流转到采购时，采购在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，可点击加签按钮，输入加签人员工号后，此流程会同时流转到加签人节点进行审批，采购需与加签人员都审批通过后，流程才会流转到下个节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24122(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("专家会签节点的审核用户，不能'拒绝'，显示'同意''转交''加签'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24123(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("同意流程流转到专家技术人员时，专家技术人员在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，无问题情况下，点击同意按钮，需所有的专家技术人员审批完成后才能流转到下个节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24124(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("转交专家技术人员时，专家技术人员在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，可点击转交按钮，填写转交人，此流程会流转到转交人节点进行审批")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24125(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("加签专家技术人员时，专家技术人员在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单据，可点击加签按钮，输入加签人员工号后，此流程会同时流转到加签人节点进行审批，专家技术人员需与加签人员都审批通过后，流程才会流转到下个节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24126(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("同意流程流转到总经理时，总经理在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，无问题情况下，点击同意按钮，流程完成，对象实例生命周期状态更改为'已发布'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24127(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("拒绝流程流转到总经理时，总经理在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，如有问题，点击拒绝按钮，流程终止，驳回到发起节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24128(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("转交流程流转到总经理时，总经理在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，可点击转交按钮，填写转交人，此流程会流转到转交人节点进行审批")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24129(self, drivers):
        pass

    @allure.story("开模流程/开模流程审批")  # 用户故事名称
    @allure.title("加签流程流转到总经理时，总经理在我的待办中可查看此流程，点击流程标题，进入审批页面，审批页面不能编辑表单数据，可点击加签按钮，输入加签人员工号后，此流程会同时流转到加签人节点进行审批，总经理需与加签人员都审批通过后，流程完成，对象实例生命周期状态更改为'已、发布quot")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24130(self, drivers):
        pass


if __name__ == '__main__':
    pass
