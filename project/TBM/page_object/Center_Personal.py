
# import allure
# from public.base.Basics import Base, sleep
# from libs.common.read_element import Element
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from ..test_case.conftest import *
#
# object_name = os.path.basename(__file__).split('.')[0]
# user = Element(pro_name,object_name)
#
# class UserPage(Base):
#     """用户类"""
#
#     @allure.step("查找工号")
#     def search_user(self, jobnum=None,name=None):
#         if jobnum is not None:
#             self.readonly_input_text(user['用户管理-工号输入框'], txt=jobnum)
#             sleep(2)
#             self.is_click_tbm(user['用户管理-工号下拉列表'], jobnum)
#         if name is not None:
#             self.readonly_input_text(user['用户管理-姓名输入框'], txt=name)
#             sleep(2)
#             self.is_click_tbm(user['用户管理-姓名下拉列表'], name)
#         self.is_click_tbm(user['用户管理-查询'])
#         sleep()
#
# if __name__ == '__main__':
#     pass


