import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class NavPage(Base):

    @allure.step("前往菜单")
    def click_gotonav(self, *content,):
        """前往菜单"""
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            self.is_click(user[level[i]])
        sleep(4)


    @allure.step("关闭标签页")
    def close_page(self):
        self.is_click(user['关闭标签页'])
        logging.info("关闭标签页")


if __name__ == '__main__':
    pass
