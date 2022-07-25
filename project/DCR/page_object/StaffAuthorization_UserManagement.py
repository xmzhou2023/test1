from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserManagementPage(Base):
    """UserManagementPage 页面元素类"""

    @allure.step("user management页面，点击Add新增按钮")
    def click_add_user(self):
        self.is_click(user['Add'])
        sleep(3.5)

    @allure.step("进入Add user页面， 选择传音员工类型")
    def click_transsion_staff(self):
        self.is_click(user['Staff Type'])
        sleep(0.5)
        self.is_click(user['Transsion Staff'])

    @allure.step("Add user页面， 输入user ID字段")
    def input_user_id(self, content):
        self.input_text_dcr(user['User ID'], txt=content)

    @allure.step("Add user页面， 输入user Name字段")
    def input_user_name(self, content):
        Base.presence_sleep_dcr(self, user['User Name'])
        self.input_text(user['User Name'], txt=content)

    @allure.step("Add user页面， 输入销售区域，然后选中输入的销售区域")
    def input_sales_region(self, content):
        self.is_click(user['Sales Region'])
        self.input_text(user['Sales Region'], txt=content)
        sleep(2)
        self.is_click(user['Sales Region Value'])

    @allure.step("Add user页面， 输入国家城市，然后选中输入的国家城市")
    def input_country_city(self, content):
        self.is_click(user['Country City'])
        self.input_text(user['Country City'], txt=content)
        sleep(2)
        self.is_click(user['Country City Value'])

    @allure.step("Add user页面，选择点击品牌")
    def click_select_brand(self):
        self.is_click(user['Select Brand'])
        sleep(1)
        self.is_click(user['Brand TECNO'])
        self.is_click(user['Brand itel'])
        self.is_click(user['Brand Infinix'])

    @allure.step("关闭User Management菜单")
    def click_close_user_mgt(self):
        self.is_click(user['关闭用户管理菜单'])
        sleep(2)

    @allure.step("Add user页面，选择点击品牌")
    def click_edit_brand(self):
        self.is_click(user['Select Brand'])
        sleep(1)
        self.is_click(user['Brand oraimo'])

    @allure.step("Add user页面，选择点击品牌")
    def click_edit_dealer_brand(self):
        self.is_click(user['Select Brand'])
        sleep(1)
        self.is_click(user['Brand Infinix'])

    @allure.step("Add user页面，输入职位，选中输入的职位")
    def input_position_transsion(self, content):
        self.is_click(user['Position'])
        self.input_text(user['Position'], txt=content)
        sleep(1)
        self.is_click(user['Position Value Transsion'])

    @allure.step("Add user页面，输入上级领导，选中输入的上级领导")
    def input_superior(self, content):
        self.is_click(user['Superior'])
        self.input_text(user['Superior'], txt=content)
        sleep(2)
        self.is_click(user['Superior Value'], "lhmadmin lhmadmin")

    @allure.step("Add user页面，输入邮箱")
    def input_email(self, content):
        self.input_text(user['Email'], txt=content)

    @allure.step("Add user页面，输入联系电话")
    def input_contact_no(self, content):
        self.input_text(user['Contact No'], txt=content)

    # def click_marital_status(self):
    #     """Add user页面，选择婚姻状态"""
    #     self.is_click(user['Marital Status'])
    #     sleep(1)
    #     self.is_click(user['Marital Married'])

    @allure.step("Add user页面，选择性别")
    def click_gender_female(self):
        self.is_click(user['Gender'])
        sleep(1)
        self.is_click(user['Gender Female'])

    @allure.step("Add user页面，点击Submit提交按钮")
    def click_add_user_submit(self):
        self.is_click(user['Add User Submit'])
        sleep(2)

    @allure.step("获取列表User ID文本内容")
    def get_text_user_id(self):
        Base.presence_sleep_dcr(self, user['获取列表文本User ID'])
        userid = self.element_text(user['获取列表文本User ID'])
        return userid

    @allure.step("'获取列表User Name文本内容")
    def get_text_user_name(self):
        username = self.element_text(user['获取列表文本User Name'])
        return username

    @allure.step("输入user ID属性筛选")
    def input_query_userid(self, content1):
        self.is_click(user['Input User ID'])
        self.input_text(user['Input User ID'], txt=content1)
        self.is_click(user['User ID Value'])
        sleep(1)

    @allure.step("点击搜索功能")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(4)

    @allure.step("点击重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(3)


    """编辑用户时，筛选用户"""
    @allure.step("用户管理列表页面，筛选User，进行编辑或者删除")
    def input_query_User(self, content, content1):
        self.is_click_dcr(user['点击筛选用户输入框'])
        self.input_text_dcr(user['点击筛选用户输入框'], txt=content)
        sleep(3)
        self.is_click(user['Input User ID Value'], content1)

    @allure.step("点击编辑功能")
    def click_edit(self):
        Base.presence_sleep_dcr(self, user['修改第一个Edit'])
        self.is_click_dcr(user['修改第一个Edit'])
        sleep(2)

    @allure.step("点击第一个checkbox,对用户进行辞职操作")
    def click_first_checkbox(self):
        self.is_click(user['勾选第一个复选框'])
        sleep(1)

    @allure.step("编辑用户提交成功提示语")
    def get_set_up_successfully(self):
        set_up_success = self.element_text(user['Set Up Successfully'])
        return set_up_success

    @allure.step("点击更多操作")
    def click_more_option(self):
        self.is_click(user['More Option'])
        sleep(1)

    @allure.step("点击离职功能")
    def click_quit(self):
        Base.presence_sleep_dcr(self, user['Quit'])
        self.is_click(user['Quit'])
        sleep(3)

    @allure.step("点击确认删除按钮")
    def click_yes(self):
        self.is_click(user['确认删除Yes'])

    @allure.step("获取无数据文本")
    def get_text_nodata(self):
        nodata = self.element_text(user['No Data'])
        return nodata

    @allure.step("获取删除成功提示语文本内容")
    def get_text_delete_success(self):
        del_success = self.element_text(user['Disabled Successfully'])
        return del_success

    @allure.step("进入Add user页面， 选择代理员工类型")
    def click_dealer_staff(self):
        self.is_click(user['Staff Type'])
        sleep(0.5)
        self.is_click(user['Dealer Staff'])

    @allure.step("进入Add user页面， 输入客户ID")
    def input_belong_to_cust(self, content):
        self.is_click(user['Belong To Customer'])
        self.input_text(user['Belong To Customer'], txt=content)
        sleep(2)
        self.is_click(user['Belong To Customer Value'], "UG4019912")

    @allure.step("随机生成userid")
    def user_id_random(self):
        num = str(random.randint(100, 999))
        userid = '18648' + num
        return userid

    @allure.step("随机生成username")
    def user_name_random(self):
        num = str(random.randint(100, 999))
        username = "smarttest" + num
        return username

    @allure.step("随机生成电话号码尾号")
    def number_radom(self):
        num = str(random.randint(100, 999))
        return num

    @allure.step("Add user页面，输入职位，选中输入的职位")
    def input_position_dealer(self, content):
        self.is_click(user['Position'])
        self.input_text(user['Position'], txt=content)
        sleep(1)
        self.is_click(user['Position Value Dealer'])


if __name__ == '__main__':
    pass