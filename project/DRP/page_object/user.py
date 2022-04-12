from page_base.webpage import WebPage, sleep, CustomPage
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


user = Element('user')

class UserPage(WebPage, CustomPage):
    """用户类"""

    def search_user(self, jobnum=None,name=None):
        """工号，姓名查询"""
        if jobnum is not None:
            self.readonly_input_text(user['用户管理-工号输入框'], txt=jobnum)
            sleep(2)
            self.is_click(user['用户管理-工号下拉列表'], jobnum)
        if name is not None:
            self.readonly_input_text(user['用户管理-姓名输入框'], txt=name)
            sleep(2)
            self.is_click(user['用户管理-姓名下拉列表'], name)
        self.is_click(user['用户管理-查询'])
        sleep()

    def input_account(self, content):
        """输入工号"""
        self.readonly_input_text(user['用户管理-工号输入框'], txt=content)
        sleep(20)

    def input_name(self, content):
        """输入姓名"""
        self.readonly_input_text(user['用户管理-姓名输入框'], txt=content)
        sleep(20)

    def search_account(self):
        """查询工号"""
        self.is_click(user['用户管理-查询'])
        sleep()

    def reset_account(self):
        """重置工号"""
        self.is_click(user['用户管理-重置'])
        sleep()

    def append_account(self,content):
        """新增工号"""
        self.is_click(user['用户管理-新增'])
        sleep()
        self.input_text(user['人员列表-新增人员搜索框'], txt=content)
        self.is_click(user['人员列表-新增选择人员'], content)
        self.is_click(user['人员列表-新增'])

    """用户详情类"""

    def edit_Permission(self, jobnum=None, dimension=None):
        """给指定用户配置权限"""
        self.search_user(jobnum=jobnum)
        if dimension is not None:
            self.is_click(user['用户管理-列表人员'])
            i = 1
            for (key, value) in dimension.items():
                self.edituser_tab_click(user['编辑用户权限-维度'], key)
                if key != '区域':
                    # 对选中框做初始化操作
                    self.checkbox_init(user['编辑用户权限-列表初始化'], pane=i)
                    for item in value:
                        self.edituser_tab_click(user['编辑用户权限-权限'], item, pane=i)
                    i = i + 1
                else:
                    for (brand, area) in value.items():
                        self.is_click(user['编辑用户权限-区域-切换品牌'], brand)
                        # self.tree_init(user['编辑用户权限-区域初始化'], brand) #可单独把区域权限初始化这里无需初始化
                        self.tree_open(brand)
                        for bottom in range(len(area)):
                            self.scroll_into_view(user['编辑用户权限-区域-勾选树末结点勾选框'], area[bottom])
                            self.is_click(user['编辑用户权限-区域-勾选树末结点勾选框'], area[bottom])
                        # 为解决滑动条引起的样式异常问题
                        self.edituser_tab_click(user['编辑用户权限-维度'], "品牌")
                        self.edituser_tab_click(user['编辑用户权限-维度'], "区域")
        self.is_click(user['编辑用户权限-区域-确定'])

    def tree_open(self, brand):
        locator = user['编辑用户权限-区域-展开树']
        Npath = []
        Npath.append(locator[0])
        Npath.append(locator[1])
        Npath[1] = Npath[1].replace('variable', brand)

        """展开树"""
        while 1:
            num = len(self.custom_find_elements(Npath))
            if num != 0:
                self.find_element(Npath).click()
                # self.scroll_into_view(Npath)  # 可改为快速展开的方式
                # sleep(0.5)
                for i in range(3):
                    ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                    sleep(0.5)
            else:
                break


if __name__ == '__main__':
    pass