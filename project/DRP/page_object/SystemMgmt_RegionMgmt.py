import allure
from public.base.Basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

user = Element('SystemMgmt_RegionMgmt')

class AreaPage(Base):
    """区域管理"""

    @allure.step("前往树")
    def goto_tree(self,  *content):
        for i in range(len(content)):
            if i == 0:
                self.is_click(user['tab区域总菜单'],choice=content[0])
                sleep(2)
                self.is_click(user['tab区域菜单一级菜单'],choice=content[0])
                sleep(2)
            elif i == 1:
                self.is_click(user['tab区域菜单二级菜单'],choice=content[1])
                sleep(2)
            elif i == 2:
                self.is_click(user['tab区域菜单三级菜单'],choice=content[2])
                sleep(2)
            elif i == 3:
                self.is_click(user['tab区域菜单四级菜单'],choice=content[3])
                sleep(2)

    @allure.step("区域导出")
    def download_area(self, content):
        self.check_download(user['区域导出'], content)

    @allure.step("编辑区域")
    def edit_area(self,num, content):
        pass

    @allure.step("删除区域")
    def del_area(self, content):
        self.check_download(user['区域导出'], content)

if __name__ == '__main__':
    pass
