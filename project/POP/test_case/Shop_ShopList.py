import allure,os
import pytest,logging,random,time
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Shop_ShopList import *
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

# 获取上传图片、视频文件在项目中的路径
path = os.path.dirname(os.path.abspath(__file__))
pthoto_path = os.path.join(os.path.dirname(path),"data/photo.png")
video_path = os.path.join(os.path.dirname(path),"data/video.mp4")


@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP商品-商品参数”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("门店","门店列表")


@allure.feature("门店") # 模块名称
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

@allure.feature("门店")
class TestAddShop:
    @allure.story("门店列表")
    @allure.title("门店新增")
    @allure.description("点击新增门店成功")
    @pytest.mark.smoke
    def test_002_001(self,drivers):
        users = AddShop(drivers)
        users.click_add()
        # 利于时间戳取数每次生成门店后缀数不一样，代码运行减少避免重复
        shopname = "zwq测试门店" + str(int(time.time()))
        users.input_shopname(shopname)
        users.switch_organization("TECNO事业部")
        users.switch_country("China")
        users.switch_province("重庆")
        users.switch_city("沙坪坝区")
        users.input_address("三峡广场")
        users.switch_city_level("T1")
        users.switch_region("China")
        users.input_linkman("张文强")
        users.input_phone("18323585901")
        users.switch_shop_level("超级旗舰店")
        users.switch_image_level("体验店")
        users.switch_sales_volume_level("A")
        users.switch_ownership("公司直营")
        users.input_shop_square_measure("66.66")
        users.input_shop_storey_height("5.25")

        # 根据获取的图片、视频路径上传图片
        users.upload_drawing_video(pthoto_path,video_path)
        users.add_userinformation("张文强")
        users.input_shop_monthlysales("8888")
        users.click_submit()
        sleep(0.5)

        # 断言--提交成功弹窗提示”success“字样
        DomAssert(drivers).assert_exact_att('门店ID')

        # 数据清理--数据库删除门店
        sql = f'DELETE from shop WHERE `name` = "{shopname}";'
        SQL("POP","test").delete_db(sql)



if __name__ == '__main__':
    pytest.main(['Shop_ShopList.py::TestAddShop'])