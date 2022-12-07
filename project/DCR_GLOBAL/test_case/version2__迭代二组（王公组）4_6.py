import allure
import pytest
@allure.feature("迭代二组（王公组）4_6")  # 迭代名称
class Teststory_6:
    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("1、价格取数取国家价格表")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_144(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("2、user维度的价格取值取国家表中的RecommendedRetailPrice字段的价格")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_145(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("3、custmoter中Purchase二代、零售取Dealerprice字段的价格")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_146(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("4、customer中Sales国包取Dealerprice字段的价格")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_147(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("5、custmoter中Sales二代、零售取Retailerprice字段的价格")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_148(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("6、custmoter中Inventory取门店的RecommendedRetailPrice字段的价格")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_149(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("7、shop维度的价格取国家表中的RecommendedRetailPrice字段的价格")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_150(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("8、文本输入框支持输入最大的值为9位数字加小数点后四位")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_151(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("9、文本输入框输入最大的值为9位数字加小数点后五位不支持输入")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_152(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("10、筛选字段价格最高值不能低于最低值")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_153(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("11、输入最高值时在输入最低值时自动校验最高值不能低于最低值")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_154(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("12、输入100——300包含最低值100和最高值300")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_155(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("13、叠加筛选生效")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_156(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("14、中国tecno价格100到300元区间的筛选可以筛选出对应的机型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_157(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("15、中国tecno价格100以上的筛选可以筛选出对应的机型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_158(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("16、中国tecno价格0到300区间的筛选可以筛选出对应的机型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_159(self, drivers):
        pass


    @allure.story("机型选择新增价格筛选")  # 用户故事名称
    @allure.title("17、筛选出对应的机型可以给出对应的返利政策")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_160(self, drivers):
        pass


@allure.feature("迭代二组（王公组）4_6")  # 迭代名称
class Teststory_29:
    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("1、WEB端新增时允许上传多个附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_178(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("2、WEB端新增时当数量达到五个时再次添加附件时系统给出对应的提示信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_179(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("21、WEB端新增时附件可支持任意格式文件上传")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_180(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("22、WEB端新增时添加一个时再次返回允许添加附件数量至5个")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_181(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("23、WEB端新增时已添加的附件可删除后再次添加")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_182(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("24、WEB端新增时附件可删至最低为0个必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_183(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("25、WEB端新增时添加的附件多个时在对应的显示的位置转行显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_184(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("3、web端编辑数据内时编辑时允许修改已上传的附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_185(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("31、web端编辑数据内编辑时可以选择已删除附件上传")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_186(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("32、web端编辑数据内编辑时附件支持任意形式的文件上传")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_187(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("33、web端编辑数据内编辑时数量不允许超过5个")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_188(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("34、web端数据内编辑时允许添加减少附件数量")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_189(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("4、列表页面附件编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_190(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("41、列表页面附件编辑允许删除附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_191(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("42、列表页面附件编辑上传时需要附件全部清空时add按钮显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_192(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("43、列表页面删除的附件在对应的列表页面实时显示更新")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_193(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("5、导出时，多政策在同一列，逗号隔开")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_194(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("51、导出的数据与页面查询一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_195(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("6、APP端单条的附件页面显示与需求一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_196(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("61、APP端多条的页面附件轮播图显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_197(self, drivers):
        pass


    @allure.story("【PK】政策书附件可允许多个附件")  # 用户故事名称
    @allure.title("63、APP端显示的附件内容与上传一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_198(self, drivers):
        pass


@allure.feature("迭代二组（王公组）4_6")  # 迭代名称
class Teststory_27:
    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("礼品提示语正确")  # 用例名称
    @allure.description("1.创建一条门店激活返利礼品的返利政策")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_216(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("1、礼品返利的类型至涉及user维度和shop维度")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_338(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("2、shop维度和user维度涉及的校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_339(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("3、CaculateWise返利增加Gift")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_340(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("31、当CaculateWise未选择了'Gift'，Gift列表字段为空导出同列表数据一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_341(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("32、当CaculateWise选择了'Gift'，则政策设置区域对应新增Gift列与需求显示一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_342(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("321、Gift字段为两个文本输入框，必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_343(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("322、左侧文本输入框为销量文本输入框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_344(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("323、左侧文本输入框默认显示ALL")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_345(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("324、当显示ALL时默认所有的销量只给出你填写的对应的奖品")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_346(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("325、左侧文本输入框只允许输入数字字符的任意数字整数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_347(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("325、右侧文本输入框输入给出对应的礼品")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_348(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("326、右侧礼品输入框500字符不限制输入形式")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_349(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("327、右侧多礼品时逗号隔开不超过500字符")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_350(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("328、页面显示自适应")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_351(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("33、提示英文Multipliergiftscanbeset,e.g.forevery3unitssold,onegift。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_352(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("4、返利政策多场景校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_353(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("5、返利推送APP端校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_354(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("6、APP端数据显示正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_355(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("7、SchemeManagement、SchemeReport、chemeReport（Item）列表增加Gift字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_356(self, drivers):
        pass


    @allure.story("【印度】礼品返利类型，兼容倍数返利，每3台激活，给1台手机")  # 用户故事名称
    @allure.title("8、导出数据与列表数据一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_357(self, drivers):
        pass


@allure.feature("迭代二组（王公组）4_6")  # 迭代名称
class Teststory_22:
    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("1、门店销量上报正常，相关报表记录正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_218(self, drivers):
        pass


    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("2、门店库存上报正常，相关报表记录正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_219(self, drivers):
        pass


    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("21、门店上报库存符合激活转销量配置的imei可以正常转门店销量")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_220(self, drivers):
        pass


    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("3、涉及激活相关查询正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_221(self, drivers):
        pass


    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("31、ShopPurchaseQueryActivationCountry、ActivationStatusActivatedDate筛选项查询数据准确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_222(self, drivers):
        pass


    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("32、ShopSalesQueryActivationCountry、ActivationStatusActivatedDate筛选项查询数据准确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_223(self, drivers):
        pass


    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("33、ShopInventoryIMEIQueryActivationCountry、ActivationStatusActivatedDate筛选项查询数据准确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_224(self, drivers):
        pass


    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("4、激活转销量定时任务正常（先上报销量，再把激活转销量配置改成符合的）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_225(self, drivers):
        pass


    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("5、有效销量兼容position填ALL，item填ALL的场景")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_226(self, drivers):
        pass


    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("51、重点机型导入position为ALL，item为ALL，导入成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_227(self, drivers):
        pass


    @allure.story("销量上报性能优化")  # 用户故事名称
    @allure.title("52、设置达成规则后，任意印度国家的人员上报门店销量，均可跑出达成结果。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_228(self, drivers):
        pass


@allure.feature("迭代二组（王公组）4_6")  # 迭代名称
class Teststory_30:
    @allure.story("返利前端优化项")  # 用户故事名称
    @allure.title("1、返利报表列表Shop维度，现在的ShopOwnerName改为ShopContactName，ShopOwnerID改为ShopContactNo.，导出同步修改")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_689(self, drivers):
        pass


    @allure.story("返利前端优化项")  # 用户故事名称
    @allure.title("2、当政策满足无条件时对应的返利政策发钱提示语为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_690(self, drivers):
        pass


    @allure.story("返利前端优化项")  # 用户故事名称
    @allure.title("21、当政策不满足无条件时对应的单利政策不发钱提示语返回为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_691(self, drivers):
        pass


    @allure.story("返利前端优化项")  # 用户故事名称
    @allure.title("3、优化设置第二页的涉及到数量值（Quantity、TotalQuantity等）优化不能输入小数。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_692(self, drivers):
        pass


    @allure.story("返利前端优化项")  # 用户故事名称
    @allure.title("4、重选机型页面的数据当第一页发生改变时第二页重选的数据也对应改变")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_693(self, drivers):
        pass


@allure.feature("迭代二组（王公组）4_6")  # 迭代名称
class Teststory_23:
    @allure.story("隐私协议组件")  # 用户故事名称
    @allure.title("数据权限1、登录页面用用户中心的单点登录用户中心的用户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4907(self, drivers):
        pass


    @allure.story("隐私协议组件")  # 用户故事名称
    @allure.title("数据权限2、只有系统管理员能够新增/编辑/查看此菜单权限")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4908(self, drivers):
        pass


if __name__ == '__main__':
      pass
