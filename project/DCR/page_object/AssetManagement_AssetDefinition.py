from libs.common.read_element import Element
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from libs.config.conf import BASE_DIR
import random


object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AssetDefinitionPage(Base):

    @allure.step("Asset Definition页面，点击Add按钮")
    def click_add_asset(self):
        self.is_click(user['Add Asset Definition'])
        sleep(1)

    @allure.step("新增资产操作时，字段增加随机数")
    def asset_random(self):
        num = str(random.randint(100, 999))
        return num

    @allure.step("Asset Add页面, 新增资产")
    def add_asset(self, brand, design_by, category, asset_name_en, asset_name_cn, version, cost):
        #Asset Add页面，选择Brand
        self.is_click(user['Brand Select'])
        self.is_click(user['Brand Select Value'], brand)
        #Asset Add页面，选择Design By
        self.is_click(user['Design By'], design_by)
        #选择资产分类
        self.is_click(user['Asset Category'])
        self.is_click(user['Asset Category Value'], category)
        #输入资产英文名称
        self.input_text(user['Add Asset Name EN'], asset_name_en)
        # 输入资产中文名称
        self.input_text(user['Add Asset Name CN'], asset_name_cn)
        self.input_text(user['Add Version'], version)
        self.input_text(user['Add Cost'], cost)
        self.is_click(user['Has ASN'])
        self.is_click(user['Has ASN Yes'])
        #选all 国家启用状态
        self.is_click(user['Enable All'])


    @allure.step("Asset Add页面, 点击Picture上传图片按钮")
    def click_upload_picture(self, picture):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', picture)
        logging.info("打印上传的文件path：{}".format(path1))
        self.upload_picture_method(path1)

    @allure.step("Asset Add页面,上传图片")
    def upload_picture_method(self, file):
        self.is_click(user['Upload Picture'])
        sleep(2)
        ele = self.driver.find_element('xpath', "//div/..//input[@name='files']")
        ele.send_keys(file)
        sleep(2)

    @allure.step("Asset Add页面, 点击Submit按钮")
    def click_add_submit(self):
        self.is_click(user['Add Submit'])

    @allure.step("Asset Definition列表, 筛选当天的日期，查看资产信息")
    def query_create_date(self, start_date, end_date):
        self.is_click(user['Create Start Date Query'])
        self.input_text(user['Create Start Date Query'], start_date)
        self.is_click(user['Create End Date Query'])
        self.input_text(user['Create End Date Query'], end_date)

    @allure.step("Asset Definition列表, 点击Search")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(1.5)

    @allure.step("Asset Definition列表, 根据Create Date或者category条件筛选资产信息")
    def query_createdate_category(self, start_date, end_date, category):
        self.is_click(user['Unfold'])
        sleep(1)
        self.query_create_date(start_date, end_date)
        self.is_click(user['Cagegory Query'])
        self.is_click(user['Asset Category Value'], category)
        self.click_search()


    @allure.step("Asset Definition列表, 根据Create Date,Category,Asset Name字段筛选新增的资产")
    def query_asset_info(self, start_date, end_date, category, asset_name):
        #点击Unfold 展开筛选条件
        self.is_click(user['Unfold'])
        sleep(1)
        #调用筛选创建日期方法
        self.query_create_date(start_date, end_date)
        self.is_click(user['Cagegory Query'])
        self.is_click(user['Asset Category Value'], category)
        #筛选资产名称
        self.input_text(user['Asset Name Query'], asset_name)
        #点击收起筛选条件
        self.is_click(user['Fold'])

    @allure.step("Asset Definition列表, 根据Create Date,Category 字段筛选新增的资产")
    def query_asset_info_edit(self, start_date, end_date, category):
        # 点击Unfold 展开筛选条件
        self.is_click(user['Unfold'])
        sleep(1)
        # 调用筛选创建日期方法
        self.query_create_date(start_date, end_date)
        self.is_click(user['Cagegory Query'])
        self.is_click(user['Asset Category Value'], category)

    @allure.step("Asset Definition列表, 根据Asset Name条件筛选数据")
    def query_asset_name(self, asset_name_en):
        self.input_text(user['Asset Name Query'], asset_name_en)
        self.is_click(user['Fold'])

    @allure.step("Asset Definition列表, 获取列表字段内容")
    def get_list_field_content(self, field):
        field = self.element_text(user[field])
        return field

    @allure.step("Asset Definition页面, 点击Edit")
    def click_edit(self):
        self.is_click_dcr(user['Edit First'])
        sleep(3)


    @allure.step("Asset Edit页面, 修改资产属性")
    def edit_asset(self, asset_name_en, asset_name_cn, version, cost):
        # 输入资产英文名称
        self.presence_sleep_dcr(user['Edit Asset Name EN'])
        self.input_text(user['Edit Asset Name EN'], asset_name_en)
        # 输入资产中文名称
        self.input_text(user['Edit Asset Name CN'], asset_name_cn)
        self.input_text(user['Edit Version'], version)
        self.input_text(user['Edit Cost'], cost)

    @allure.step("Asset Edit页面, 点击提交按钮")
    def click_edit_submit(self):
        self.is_click(user['Edit Submit'])

    @allure.step("Asset Definition页面, 获取列表Total总条数")
    def get_list_total(self):
        total = self.element_text(user['Get list Total'])
        total1 = int(total[6:])
        return total1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) >= 1:
            logging.info("资产定义列表，分页总条数大于0，能查询到考勤记录数Total:{}".format(total))
        else:
            logging.info("资产定义列表，分页总条数为0，未查询到考勤记录数Total:{}:".format(total))


if __name__ == '__main__':
    pass
