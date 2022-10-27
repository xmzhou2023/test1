from libs.common.read_element import Element
from project.POP.test_case.conftest import *
# from public.base.basics import Base, sleep
from selenium.webdriver.support.select import Select
from pykeyboard import PyKeyboard

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)
class Region(Base):
    """区域类"""
    @allure.step('点击菜单按钮')
    def click_button(self, variable):
        self.is_click(user['菜单按钮'], variable)
        sleep(2)


    @allure.step('新增搜索框输入区域')
    def input_region(self, region):
        self.is_click_tbm(user['新增搜索框'])
        self.input_text(user['新增搜索框'], region)
        sleep(2)

    @allure.step('点击新增子区域')
    def click_sub_region_Add(self):
        self.is_click(user['区域点击Add'])

    @allure.step('输入子区域')
    def input_sub_region_name(self, region_name):
        self.is_click(user['新增区域名称'])
        self.input_text(user['新增区域名称'],region_name)

    @allure.step('新增页面点击提交按钮')
    def click_submit(self):
        self.is_click(user['新增提交'])


    @allure.step('筛选框输入区域匹配第一个元素')
    def select_region(self, region):
        self.is_click(user['区域筛选框'])
        self.input_text(user['区域筛选框'], region)
        self.is_click(user['选择区域'], region)

    @allure.step('选择筛选条件')
    def click_dropdown(self, drop, value):
        self.is_click(user['下拉框'], drop)
        self.is_click(user['下拉框选项'], value)

    @allure.step('点击查询/重置按钮')
    def click_search(self, button):
        self.is_click(user['查询重置按钮'], button)

    @allure.step('勾选筛选的区域')
    def check_region(self, num):
        self.is_click(user['勾选区域'], num)

    @allure.step('修改父级字段')
    def edit_prent_region(self, parent):
        self.is_click_tbm(user['父级区域输入框'])
        sleep(1)
        self.input_text(user['父级区域输入框'], parent)
        self.is_click_tbm(user['选择父级区域'], parent)

    @allure.step('修改区域名称')
    def edit_region_name(self, new_region):
        self.is_click(user['编辑区域名称'])
        self.input_text(user['编辑区域名称'], new_region)


    @allure.step('编辑页面点击提交按钮')
    def edit_submit(self):
        self.is_click(user['编辑提交'])
        sleep(5)

    @allure.step('禁用-点击确定')
    def click_disable_yes(self):
        key = PyKeyboard()  # 实例化一个键盘
        key.press_key(key.enter_key)  # 按下enter键
        key.release_key(key.enter_key)
