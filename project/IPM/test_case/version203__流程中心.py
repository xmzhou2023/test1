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
    @allure.title('物料申请点击物料申请，进入到物料申请页面')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23598(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/标题50个字符，必填')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23599(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/流程编码文本框只读，提交流程后，OneWorks自动生成流程的编码')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23600(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/申请人文本框只读，系统自动识别申请人名称并展示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23601(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/申请部门文本框只读，系统自动识别申请人部门信息并展示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23602(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/申请日期日期只读，系统自动生成，格式按照yyyyMMdd展示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23603(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/申请类型下拉，值范围'手机物料/ODM物料/二级物料/手机物料二级BOM'')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23604(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/申请类型必填，根据所选择申请类型后，加载页面')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23605(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('新增新增按钮，可以添加多个物料类型区域')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23606(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('全部展开全部展开所有的物料类型区域所有的物料数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23607(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('全部折叠全部折叠所有的物料类型区域所有的物料数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23608(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型下拉选择，必填，默认显示一个物料类型区域')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23609(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型下拉选择物料类型后，展示此物料类型')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23610(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型按照分级的树型菜单联动展示所有物料类型，可支持搜索')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23611(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型物料类型的选值范围根据【申请类型】做过滤')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23612(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型若为'手机物料'及'ODM物料'，所有启用的物料对象类型都可选择')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23613(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型若为'二级物料'，9开头的所有物料组的启用的对象类型，支持配置实现')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23614(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型若为'二级BOM'，170、171、172、174、176、250、251的物料组的启用的对象类型，支持配置实现')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23615(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型选择物料类型后，默认带出物料数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23616(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型选择物料类型只能选择叶子节点')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23617(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型区域/删除支持删除，点击删除提示'请确定是否删除当前的物料类型区域'')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23618(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型区域/全屏点击全屏，全屏展示此物料类型区域的数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23619(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型区域/退出全屏全屏展示物料区域的数据后，点击退出全屏按钮后，物料区域的数据退出全屏')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23620(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型区域/全部展开全部展开所有的物料类型区域所有的物料数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23621(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型区域/全部折叠全部折叠所有的物料类型区域所有的物料数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23622(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型/重新选择点击重新选择，提示'已填写的物料数据将会清空，请确认'')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23623(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('新增点击'按钮'新增一行物料数据（下面），展开新增的一行物料数据，光标定位到新的物料数据上，便于填写')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23624(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('删除点击'按钮'删除一行物料数据，删除时，提示'请确定是否删除当前选中的物料'，点确定删除')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23625(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('复制点击'复制按钮'复制一行物料数据，当前物料之后，光标定位到新的物料数据上，便于填写')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23626(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('复制前端复制所有填好的属性字段，合成属性也能够自动带出，全复制所有属性数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23627(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('签审人员信息签审人员信息，选择申请类型后，默认显示这块区域')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23628(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('角色解析其他的角色信息按照选择的'申请类型''物料类型'动态加载角色')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23629(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('抄送人员设置流程中设置固定人员，不在流程节点中体现，流程完成后，邮件及飞书通知给抄送人员')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23630(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('抄送邮件邮件内容，'标题'的流程审批通过，申请物料以表格展示，具体内容有'物料编码、物料名称、物料描述CN、物料描述EN、原厂代码、原厂描述'。')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23631(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('附件附件区域，选择申请类型后，默认显示这块区域，当前区域为流程的附件补充数据，并非物料对象关联文档数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23632(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('提交'提交'按钮，提交当前流程，业务逻辑具体参考'US提交物料/文档/关系创建'')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23633(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('提交提交需要验证，必填项是否填写，【标题】，【申请类型】，【物料类型】，必须一条物料数据，物料中定义的约束必填的属性；')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23634(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('提交提交需要验证，不同审批路径（节点）的物料暂时不能同时提交')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23635(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('保存'保存'按钮，保存为我的草稿，业务逻辑具体参考'US提交物料/文档/关系创建'')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23636(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('保存保存需要验证，【标题】必填')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23637(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('保存保存需要验证，不同审批路径（节点）的物料暂时不能同时保存')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23638(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('取消点击取消按钮，提示'您确定要取消当前表单'，确定删除当前表单，取消关闭当前页面')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23639(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料申请点击物料申请，进入到物料申请页面')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24144(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/标题50个字符，必填')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24145(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/流程编码文本框只读，提交流程后，OneWorks自动生成流程的编码')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24146(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/申请人文本框只读，系统自动识别申请人名称并展示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24147(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/申请部门文本框只读，系统自动识别申请人部门信息并展示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24148(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/申请日期日期只读，系统自动生成，格式按照yyyyMMdd展示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24149(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/申请类型下拉，值范围'手机物料/ODM物料/二级物料/手机物料二级BOM'')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24150(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('基本信息/申请类型必填，根据所选择申请类型后，加载页面')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24151(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('新增新增按钮，可以添加多个物料类型区域')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24152(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('全部展开全部展开所有的物料类型区域所有的物料数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24153(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('全部折叠全部折叠所有的物料类型区域所有的物料数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24154(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型下拉选择，必填，默认显示一个物料类型区域')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24155(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型下拉选择物料类型后，展示此物料类型')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24156(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型按照分级的树型菜单联动展示所有物料类型，可支持搜索')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24157(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型物料类型的选值范围根据【申请类型】做过滤')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24158(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型若为'手机物料'及'ODM物料'，所有启用的物料对象类型都可选择')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24159(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型若为'二级物料'，9开头的所有物料组的启用的对象类型，支持配置实现')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24160(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型若为'二级BOM'，170、171、172、174、176、250、251的物料组的启用的对象类型，支持配置实现')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24161(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型选择物料类型后，默认带出物料数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24162(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型选择物料类型只能选择叶子节点')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24163(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型区域/删除支持删除，点击删除提示'请确定是否删除当前的物料类型区域'')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24164(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型区域/全屏点击全屏，全屏展示此物料类型区域的数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24165(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型区域/退出全屏全屏展示物料区域的数据后，点击退出全屏按钮后，物料区域的数据退出全屏')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24166(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型区域/全部展开全部展开所有的物料类型区域所有的物料数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24167(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型区域/全部折叠全部折叠所有的物料类型区域所有的物料数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24168(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('物料类型/重新选择点击重新选择，提示'已填写的物料数据将会清空，请确认'')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24169(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('新增点击'按钮'新增一行物料数据（下面），展开新增的一行物料数据，光标定位到新的物料数据上，便于填写')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24170(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('删除点击'按钮'删除一行物料数据，删除时，提示'请确定是否删除当前选中的物料'，点确定删除')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24171(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('复制点击'复制按钮'复制一行物料数据，当前物料之后，光标定位到新的物料数据上，便于填写')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24172(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('复制前端复制所有填好的属性字段，合成属性也能够自动带出，全复制所有属性数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24173(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('签审人员信息签审人员信息，选择申请类型后，默认显示这块区域')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24174(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('角色解析其他的角色信息按照选择的'申请类型''物料类型'动态加载角色')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24175(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('抄送人员设置流程中设置固定人员，不在流程节点中体现，流程完成后，邮件及飞书通知给抄送人员')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24176(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('抄送邮件邮件内容，'标题'的流程审批通过，申请物料以表格展示，具体内容有'物料编码、物料名称、物料描述CN、物料描述EN、原厂代码、原厂描述'。')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24177(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('附件附件区域，选择申请类型后，默认显示这块区域，当前区域为流程的附件补充数据，并非物料对象关联文档数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24178(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('提交'提交'按钮，提交当前流程，业务逻辑具体参考'US提交物料/文档/关系创建'')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24179(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('提交提交需要验证，必填项是否填写，【标题】，【申请类型】，【物料类型】，必须一条物料数据，物料中定义的约束必填的属性；')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24180(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('提交提交需要验证，不同审批路径（节点）的物料暂时不能同时提交')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24181(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('保存'保存'按钮，保存为我的草稿，业务逻辑具体参考'US提交物料/文档/关系创建'')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24182(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('保存保存需要验证，【标题】必填')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24183(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('保存保存需要验证，不同审批路径（节点）的物料暂时不能同时保存')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24184(self, drivers):
        pass


    @allure.story("物料申请流程/物料申请流程发起")  # 用户故事名称
    @allure.title('取消点击取消按钮，提示'您确定要取消当前表单'，确定删除当前表单，取消关闭当前页面')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24185(self, drivers):
        pass


@allure.feature("流程中心")  # 迭代名称
class Teststory_3285:
    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('点击'结构开模申请'的卡片，全屏弹出'结构开模申请'的页面')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23993(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('权限拥有结构开模文档对象的创建权限才可创建流程表单')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23994(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('基本信息/标题文本框只读，50个字符组成，生成规则项目名称开模申请单申请人申请日期')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23995(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('基本信息/单据号文本框只读，20个字符组成，前四位JGKM')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23996(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('基本信息/申请人文本框只读，20个字符组成，系统自动识别申请人名称并展示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23997(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('基本信息/申请部门文本框只读，20个字符组成，系统自动识别申请人部门信息并展示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23998(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('基本信息/申请日期日期只读，系统自动生成，格式按照yyyyMMdd展示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23999(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('开模信息/项目名称文本下拉选项,展示已有的研发项目实例查看权限且（生命周期状态为进行中的项目）及结构开模文档的创建权限，单选择框，支持输入，快速匹配选择')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24000(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('开模信息/所属品牌文本下拉框，单选框，下拉值Infinix/itel/TECNO，在数据字典中配置')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24001(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('开模信息/月需求量文本输入框，20个字符')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24002(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('开模信息/描述文本域，2000字符')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24003(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/NO序号按照新增顺序升序排序')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24004(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/物料描述文本输入框，200char')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24005(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/物料工艺文本输入框，200char')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24006(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/塑胶材质文本输入框，200char')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24007(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/开模方式文本输入框，50char')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24008(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/投模日期可选择日期为投模日期，YYYYmmdd')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24009(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/一模几穴文本输入框，50char')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24010(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/供应商类别下拉框，在接口未实现前，先实现手写功能')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24011(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/一级供应商下拉框，在接口未实现前，先实现手写功能，从SAP获取供应商数据，单选择框，支持输入，快速匹配选择')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24012(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/关键器件名文本输入框，50char')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24013(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格信息/二级供应商下拉框，在接口未实现前，先实现手写功能从SAP获取供应商数据，单选择框，支持输入，快速匹配选择')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24014(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格操作/新增点击新增按钮，可在表格中新增一条数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24015(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格操作/删除选中表格中的一条数据，点击删除按钮后删除选择的信息')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24016(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('表格操作/删除可批量选中删除多条数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24017(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('签审人员信息/复制上一单人员获取个人申请的上一个'结构开模'单据的填写的角色表单人员，进行复制，若人员不在当前选择的项目的角色中，跳过')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24018(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('签审人员信息根据所选择项目自动解析此项目团队中的人员')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24019(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('附件根据权限，可对已上传附件进行下载、上传、删除')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_24020(self, drivers):
        pass


    @allure.story("开模流程/开模流程申请")  # 用户故事名称
    @allure.title('附件上传多个附件')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
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
        robot.AI_get("http://10.250.112.57/")#id77287147-4b13-4d95-bbeb-45bb76c4b771
        robot.AI_find_element(By.CSS, ".hamburger").click()#id28c141ed-a7ac-47eb-96e0-b85742419d86
        robot.AI_find_element(By.XPATH, "//div[4]/li/div/span").click()#id617ad7d4-fdbc-4e0b-ad6c-85a29d86df39
        robot.AI_find_element(By.XPATH, "//span[contains(.,'JS Mgt')]").click()#id7a54076f-56c8-4ba6-b9e5-5788dc64482d
        robot.AI_find_element(By.XPATH, "//span[contains(.,'JS List')]").click()#ide2a89d0d-db17-48d2-9bfb-036a2fd523a7
        robot.AI_find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button:nth-child(1) > span").click()#id983e7462-7b79-4803-933c-ed1e8dabf262
        element = robot.AI_find_element(By.CSS_SELECTOR, "div:nth-child(2) > .el-button:nth-child(1) > span")#id228184c7-7de4-414f-bbdd-cfe2c9b75723
        actions = ActionChains(robot)
        actions.move_to_element(element).perform()
        element = robot.AI_find_element(By.CSS_SELECTOR, "body")#id5d32d7de-27e1-4dd4-9cb5-da510be407d7
        actions = ActionChains(robot)
        actions.move_to_element(element, 0, 0).perform()
        element = robot.AI_find_element(By.CSS_SELECTOR, ".el-button--warning")#id8d540683-e189-47e6-90c0-f2eebe681ee4
        actions = ActionChains(robot)
        actions.move_to_element(element).perform()
        robot.AI_find_element(By.CSS_SELECTOR, ".hover > span").click()#id7d94c671-4405-4e90-be48-05210aeb4ba3
        robot.AI_find_element(By.CSS_SELECTOR, ".hover > span").click()#id9d7be00c-0bfc-469a-b0b4-a03d2dc0eda9
        
        
def test_24130(self, drivers):
        pass


if __name__ == '__main__':
    pass

