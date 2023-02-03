from selenium.webdriver import Keys

from public.base.basics import Base
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from libs.common.read_config import *
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)
pro_env = "test"
ini = ReadConfig(pro_name, pro_env)


class LoginPage(Base):
    """DCR登录类"""
    @allure.step("输入工号")
    def input_account(self, content):
        self.input_text(user['工号输入框'], txt=content)

    @allure.step("输入密码")
    def input_passwd(self, content):
        self.input_text(user['密码输入框'], txt=content)

    @allure.step("语言切换")
    def switch_lanuage(self, content):
        self.is_click(user['语言切换'])
        self.is_click(user['选择英文'], content)

    @allure.step("判断是否被选中")
    def click_check_box(self):
        self.is_click(user['隐私保护勾选'])

    @allure.step("获取复选框对应的 Class属性是否包含is-checked")
    def get_check_box_class(self):
        ss = self.find_element(user['隐私保护勾选'])
        get_check_state = ss.get_attribute('class')
        return get_check_state

    @allure.step("判断是否被选中")
    def check_box(self):
        checkbox = self.select_state(user['隐私保护勾选'])
        return checkbox

    @allure.step("点击帐号密码登录")
    def click_loginsubmit(self):
        self.is_click(user['登录'])
        self.base_get_img()
        sleep(1)

    @allure.step("点击退出登录")
    def click_loginOut(self):
        self.is_click(user['退出登录'])
        sleep(1.5)

    @allure.step("获取页面已登录的账号")
    def get_login_account(self):
        get_login_account = self.element_text(user['获取登录账号'])
        return get_login_account

    @allure.step("关闭当天打开状态的菜单")
    def click_close_open_menu(self):
        self.is_click(user['关闭当前打开的菜单'])

    @allure.step("获取当前打开状态的菜单class值")
    def get_open_menu_class(self):
        open_menu = self.find_element(user['打开状态的菜单'])
        get_menu_class = open_menu.get_attribute('class')
        return get_menu_class

    @allure.step("获取页面是否有隐私政策内容")
    def dcr_get_yinsizhengce(self):
        yinsizhengce = self.element_text(user['DCR隐私政策'])
        return yinsizhengce

    @allure.step("同意按钮")
    def dcr_click_agree(self):
        self.is_click(user['agree button'])

    @allure.step("获取页面是否有隐私政策内容")
    def dcr_get_home_page_customer(self):
        home_page_cust = self.element_text(user['Home Page Customer'])
        return home_page_cust

    @allure.step("登录方法")
    def dcr_login(self, drivers, account, passwd):
        user = LoginPage(drivers)
        user.get_url(ini.url)
        sleep(3)
        user.input_account(account)
        user.input_passwd(passwd)
        sleep(1)
        get_check_class = user.get_check_box_class()
        if "is-checked" not in str(get_check_class):
            user.click_check_box()
        user.click_loginsubmit()
        DomAssert(self.driver).assert_att('testsupervisor')

    @allure.step("退出重新登录，去掉打开登录地址")
    def dcr_again_login(self, drivers, account, passwd):
        logging.info('退出重新登录')
        user = LoginPage(drivers)
        self.driver.delete_all_cookies()
        js = 'window.localStorage.clear();'
        self.driver.execute_script(js)
        self.refresh()
        user.input_account(account)
        user.input_passwd(passwd)
        sleep(3)
        get_check_class = user.get_check_box_class()
        if "is-checked" not in str(get_check_class):
            user.click_check_box()
        user.click_loginsubmit()

        """判断是否弹出DCR隐私政策页面"""
        user.privacy()
        DomAssert(drivers).assert_att(account)

    @allure.step("退出重新登录，去掉打开登录地址")
    def privacy(self):
        sleep(2.5)
        all_text = self.element_text(user['所有文本'])
        if '请下拉阅读完本隐私协议后可点击同意按钮' in all_text:
            for i in range(20):
                class_value = self.get_element_attribute(user['隐私同意按钮'], 'class')
                if 'pr-btn_gree_primary' not in class_value:
                    Base(self.driver).DivRolling(user['隐私滚动条'], direction='top', num=i*100000)
                    sleep(1)
                else:
                    self.is_click_tbm(user['隐私同意按钮'])
                    logging.info('点击隐私同意按钮')
                    break
        else:
            logging.info("打印获取的内容：{}".format(all_text))

    @allure.step("查找菜单")
    def click_gotomenu(self, *content):
        self.refresh()
        self.is_click(user['菜单栏'])
        self.refresh()
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            logging.info(user[level[i]])
            sleep(3.5)
            self.scroll_into_view(user[level[i]])
            sleep(3.5)
            self.is_click(user[level[i]])
        self.element_exist(user['Loading'])

    @allure.step("初始化登录方法")
    def initialize_login(self, drivers, account1, password):
        self.refresh()
        all_text = self.element_text(user['所有文本'])
        if 'Log in' in all_text:
            self.dcr_again_login(drivers, account1, password)
        else:
            get_account = self.get_login_account()
            if account1 != get_account:
                self.click_loginOut()
                self.dcr_again_login(drivers, account1, password)
            else:
                ref = Base(drivers)
                ref.refresh()


    """断言导出记录"""
    @allure.step("Customer Management页面，导出操作后，点击右上角下载图标,点击右上角more...")
    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        self.element_text(user['Loading'])

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(0.5)
        self.is_click_dcr(user['Task Name value'], content)

    @allure.step("输入Create Date开始日期筛选当天日期的导出记录")
    def export_record_create_start_date(self, start_date):
        self.is_click(user['导出记录筛选创建日期'])
        self.input_text(user['导出记录筛选创建日期'], start_date)
        self.is_click(user['点击筛选条件的标签'], 'Create Date')

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        download_status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
        return download_status

    @allure.step("导出记录页面，获取列表 Download Status文本")
    def get_download_status_text(self):
        status = self.find_element(user['获取下载状态文本'])
        while status != "COMPLETE":
            status = self.element_text(user['获取下载状态文本'])
            sleep(1)
        return status

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_file_size_text(self):
        file_size = self.element_text(user['获取文件大小文本'])
        file_size1 = file_size[0:1]
        return file_size1

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("断言文件或导出时间是否有数据")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("Attendance Records导出成功，File Size导出文件大于M:{}".format(file_size))
        else:
            logging.info("Attendance Records导出失败，File Size导出文件小于M:{}".format(file_size))
        if int(export_time) > 0:
            logging.info("Attendance Records导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Attendance Records导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))

    #批量导入页面定位
    @allure.step("Import Record导入记录页面，按Import Date条件筛选数据")
    def input_batch_import_date_query(self, start):
        self.is_click(user['筛选Import Date Start'])
        self.input_text(user['筛选Import Date Start'], start)
        self.is_click(user['筛选label标签'], 'Import Date')


if __name__ == '__main__':
    pass