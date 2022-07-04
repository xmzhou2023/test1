import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from libs.common.logger_ui import log

user = Element('SystemMgmt_RegionMgmt')


class AreaPage(Base):
    """区域管理"""

    @allure.step("前往树")
    def goto_tree(self, *content):
        for i in range(len(content)):
            if i == 0:
                self.is_click(user['tab区域总菜单'], choice=content[0])
                sleep(2)
                self.is_click(user['tab区域菜单一级菜单'], choice=content[0])
                sleep(2)
            elif i == 1:
                self.is_click(user['tab区域菜单二级菜单'], choice=content[1])
                sleep(2)
            elif i == 2:
                self.is_click(user['tab区域菜单三级菜单'], choice=content[2])
                sleep(2)
            elif i == 3:
                self.is_click(user['tab区域菜单四级菜单'], choice=content[3])
                sleep(2)

    @allure.step("区域导出")
    def download_area(self, content):
        self.check_download(user['区域导出'], content)

    def check_tree(self, text, allist):
        """判断树"""
        try:
            count = 0
            for i in range(len(allist)):
                if text in allist[i]:
                    log.info("{} is in {}".format(text, allist[i]))
                    for j in range(1, len(allist[i])):
                        if text in allist[i][j]:
                            count = count + 1
                    return count
                else:
                    log.info("{}is not in {}".format(text, allist[i]))
        except Exception as e:
            print(str(e))

    @allure.step("查询区域")
    def search_area(self, content):
        """查询区域"""
        self.input_text(user["区域搜索框"], content)
        log.info("输入框键入{}".format(content))
        sleep(1)

    @allure.step("清空搜索框")
    def clear_tree(self):
        self.is_click(user['清除搜索框'])

    @allure.step("点击新增按钮")
    def add_button(self):
        self.is_click(user['新增'])
        sleep(1)

    @allure.step("点击保存按钮")
    def save_button(self):
        self.is_click(user['保存'])
        sleep(1)

    @allure.step("保存国家")
    def save_country_button(self):
        self.is_click(user['保存国家'])
        sleep(1)

    @allure.step("新增区域")
    def add_area(self, nameZh=None, nameEn=None, country=None):
        """新增区域"""
        txt = self.element_text(user['区域层级'])
        tier = ['组织', '地区部']
        if txt in tier:
            self.readonly_input_text(user['新增-中文名称输入'], nameZh)
            self.readonly_input_text(user['新增-英文名称输入'], nameEn)
        elif txt == '大区':
            self.readonly_input_text(user['查找国家'], country)
            sleep(1)

    @allure.step("市场分类配置 编辑")
    def update_market(self):
        self.is_click(user['市场编辑'])

    @allure.step("保存市场配置")
    def save_market(self):
        self.is_click(user['保存市场'])

    @allure.step("切换市场页签")
    def cut_market(self,cut=None):
        if cut == '国家市场划分配置':
            self.is_click(user['国家市场划分配置'])
        else:
            self.is_click(user['国家市场分类配置'])

    @allure.step("市场分类配置")
    def market_class(self,market=None,market1=None):
        a = self.element_text(user['市场'])
        if a == '市场分类':
            self.is_click(user['市场选项'])
            sleep(2)
            try:
                if market == "公开市场":
                    self.is_click(user['选择市场'], "1")
                elif market == "定制市场":
                    self.is_click(user['选择市场'], "2")
                elif market == "印度":
                    self.is_click(user['选择市场'], "3")
                elif market == "孟加拉":
                    self.is_click(user['选择市场'], "4")
                elif market == "运营商":
                    self.is_click(user['选择市场'], "5")
            except:
                self.is_click(user['市场选项'])

        elif a == '市场划分':
            self.is_click(user['市场选项'])
            try:
                if market1 == "SSA":
                    self.is_click(user['选择市场'], "1")
                elif market1 == "新市场":
                    self.is_click(user['选择市场'], "2")
                elif market1 == "北非":
                    self.is_click(user['选择市场'], "3")
                elif market1 == "巴基斯坦":
                    self.is_click(user['选择市场'], "4")
                elif market1 == "印度":
                    self.is_click(user['选择市场'], "5")
                elif market1 == "孟加拉":
                    self.is_click(user['选择市场'], "6")
            except:
                self.is_click(user['市场选项'])

    @allure.step("指定国家添加按钮")
    def add_list(self, area_name):
        """添加指定行数据"""
        a = self.find_elements(user['国家列表第二列'])
        b = []  # 取出列表第二列的所有文本
        for i in range(len(a)):
            b.append(a[i].text)
        if area_name in b:
            c = b.index(area_name) + 1  # 取到所传参数所在行号
            self.find_element(user['添加按钮'],str(c)).click()  # 将行号c替换到xpath中进行相关操作
        else:
            self.find_element(user['关闭国家窗口']).click()  # 出现异常 关闭窗口

    @allure.step("编辑区域")
    def update_area(self, nameZh=None, nameEn=None):
        """编辑区域"""
        sleep(2)
        txt = self.element_text(user['区域层级'])
        tier = ['组织', '地区部']
        if txt in tier:
            self.readonly_input_text(user['新增-中文名称输入'], nameZh)
            self.readonly_input_text(user['新增-英文名称输入'], nameEn)

    @allure.step("指定行编辑按钮")
    def update_list(self, area_name):
        """编辑列表指定行数据"""
        a = self.find_elements(user['列表第2列'])
        b = []  # 取出列表第二列的所有文本
        for i in range(len(a)):
            b.append(a[i].text)
        if area_name in b:
            c = b.index(area_name) + 1  # 取到所传参数所在行号
            self.find_element(user['编辑'],str(c)).click()  # 将行号c替换到xpath中进行相关操作

    @allure.step("删除区域")
    def delete_area(self):
        """删除区域"""
        txt = self.element_text(user['区域层级'])
        tier = ['组织', '地区部', '大区']
        if txt in tier:
            self.is_click(user['删除 确定'])
            sleep(1)

    @allure.step("指定行删除按钮")
    def del_list(self, area_name):
        """删除列表指定行数据"""
        a = self.find_elements(user['列表第2列'])
        b = []  # 取出列表第二列的所有文本
        for i in range(len(a)):
            b.append(a[i].text)
        if area_name in b:
            c = b.index(area_name) + 1  # 取到所传参数所在行号
            self.find_element(user['删除'],str(c)).click()  # 将行号c替换到xpath中进行相关操作

    @allure.step("关闭页签")
    def close_window(self,window_name):
        """关闭区域管理"""
        self.is_click(user['关闭菜单'],window_name)



if __name__ == '__main__':
    pass
