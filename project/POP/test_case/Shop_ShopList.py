import allure,os
import pytest,logging,random,time
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Shop_ShopList import *
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
from public.base.basics import read_excel

object_name = os.path.basename(__file__).split('.')[0]   # 获取当前的文件是xxx.py文件，以.分割返回为[”xxx”,"py"]取第一个字符即文件名
user = Element(pro_name, object_name)

# 获取上传图片、视频文件在项目中的路径
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"data")
pthoto_path = os.path.join(path,"photo.png")
video_path = os.path.join(path,"video.mp4")

# 获取测试数据文件路径
data_path = os.path.join(path,"test_data.xls")

# 获取测试数据--以[('a','b'),('a','b')]二维列表格式返回
data = read_excel(data_path,"测试用例数据")


@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP商品-商品参数”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("门店","门店列表")


@allure.feature("门店-门店列表") # 模块名称
class TestQuery_shop:
    @allure.story("门店列表") # 场景名称
    @allure.title("门店列表查看")  # 用例名称
    @allure.description("点击查询按钮，正常查看门店列表信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = Query_shop(drivers)
        users.click_organization('TECNO事业部')
        users.click_shop('仙桃')
        users.click_query('仙桃体专店')
        # 断言
        test = users.element_text(user['门店名称'])
        ValueAssert.value_assert_equal(test,'仙桃体专店')

@allure.feature("门店-门店列表")
@pytest.mark.parametrize("shopname,organization,country,province,city,address,city_level,region,linkman,phone,"
                         "shop_level,image_level,sales_volume_level,ownership,shop_square_measure,shop_storey_height,userinformation,monthlysales,expect",data)  # 通过parametrize装饰器传入数据
class TestAddShop:
    @allure.story("门店列表")
    @allure.title("门店新增")
    @allure.description("点击新增门店成功")
    @pytest.mark.smoke
    def test_002_001(self,drivers,shopname,organization,country,province,city,address,city_level,region,linkman,phone,
                     shop_level,image_level,sales_volume_level,ownership,shop_square_measure,shop_storey_height,userinformation,monthlysales,expect):
        users = AddShop(drivers)
        # 点击新增
        users.click_add()
        # 输入门店名称
        users.input_shopname(shopname)
        # 输入组织
        users.switch_organization(organization)
        # 输入国家
        users.switch_country(country)
        # 选择省市
        users.switch_province(province)
        # 选择城市
        users.switch_city(city)
        # 输入详细地址
        users.input_address(address)
        # 选择城市等级
        users.switch_city_level(city_level)
        # 选择区域
        users.switch_region(region)
        # 输入建店联系人
        users.input_linkman(linkman)
        # 输入手机号
        users.input_phone(phone)
        # 选择门店等级
        users.switch_shop_level(shop_level)
        # 选择形象等级
        users.switch_image_level(image_level)
        # 选择销量等级
        users.switch_sales_volume_level(sales_volume_level)
        # 选择所有权
        users.switch_ownership(ownership)
        # 输入门店面积
        users.input_shop_square_measure(shop_square_measure)
        # 输入门店层高
        users.input_shop_storey_height(shop_storey_height)
        # 根据获取的图片、视频路径上传图片、视频
        users.upload_drawing_video(pthoto_path,video_path)
        # 增加门店人员信息
        users.add_userinformation(userinformation)
        # 输入门店预估月销售量
        users.input_shop_monthlysales(monthlysales)
        # 点击提交门店
        users.click_submit()
        sleep(2)   # 提交页面响应有时间--等待2s左右等新增成功提示--SUCCESS

        # 断言--新增提交成功提示SUCCESS
        test = users.element_text(user['新增成功提示'])
        ValueAssert.value_assert_equal(test,expect)   # expect为预期的结果值由测试数据表填入

        # 数据清理--数据库删除测试新增的对应门店
        sql = f'DELETE from shop WHERE `name` = "{shopname}";'
        SQL("POP","test").delete_db(sql)



if __name__ == '__main__':
    pytest.main(['Shop_ShopList.py::TestAddShop'])