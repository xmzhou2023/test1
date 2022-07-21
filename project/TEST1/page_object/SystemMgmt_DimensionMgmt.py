from libs.common.read_element import Element
from project.TEST1.test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class DimenPage(Base):
    """用户类"""

    # @allure.step("查找工号")
    # def search_user(self, jobnum=None,name=None):
    #     if jobnum is not None:
    #         self.readonly_input_text(user['用户管理-工号输入框'], txt=jobnum)
    #         sleep(2)
    #         self.is_click(user['用户管理-工号下拉列表'], jobnum)
    #     if name is not None:
    #         self.readonly_input_text(user['用户管理-姓名输入框'], txt=name)
    #         sleep(2)
    #         self.is_click(user['用户管理-姓名下拉列表'], name)
    #     self.is_click(user['用户管理-查询'])
    #     sleep()


    # @allure.step("系统管理")
    # def sysmag_hover(self):
    #     self.hover(user["系统管理"])
    # # def click_systemanage(self):
    # #     self.is_click(user["系统管理"])
    # #     sleep(1)

    def click_dimension(self):
        self.is_click(user["系统管理-维度管理"])
        sleep(1)
        logging.info("点击维度管理")

    def click_role(self):
        self.is_click(user["系统管理-维度管理-角色管理"])
        sleep(1)

    def click_select(self,market=None):
        self.is_click(user["角色管理-维度管理下拉"])
        try:
            if market=="infinix事业部":
                self.is_click(user["下拉选择事业部"],"1")
            elif market =="itel事业部":
                self.is_click(user["下拉选择事业部"], "2")
            elif market == "TECNO事业部":
                self.is_click(user["下拉选择事业部"], "3")
            elif market == "印度地区部":
                self.is_click(user["下拉选择事业部"], "4")
            elif market == "孟加拉地区部":
                self.is_click(user["下拉选择事业部"], "5")
        except:
            self.is_click(user["战略客户事业部"])
    def click_search(self):
        self.is_click(user["角色管理-查询"])

    def click_reset(self):
        self.is_click(user["角色管理-重置"])


if __name__ == '__main__':
    pass
