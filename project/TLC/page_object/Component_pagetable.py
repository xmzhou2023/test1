import allure, os, pyautogui, openpyxl, ddddocr, logging
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ComponentTable(Base):

    @allure.step('导航菜单')
    def click_menu(self, fType, sType):
        self.mouse_hover(user['一级菜单'], fType)
        self.is_click(user['二级菜单'], sType)
        sleep(1)
        self.refresh()

    @allure.step('处理输入')
    def input(self, yaml, txt, choice=None):
        self.input_text(user[yaml], txt, choice)


    @allure.step('pyautogui处理输入')
    def input_edit(self, x , y, txt):
        pyautogui.click(x, y, duration=1)
        pyautogui.hotkey('ctrl', 'a', 'backspace', interval=1)
        pyautogui.write(txt, interval=0.3)

    @allure.step('pyautogui处理换行输入')
    def input_line(self, x, y, txt):
        pyautogui.click(x, y, duration=1)
        pyautogui.hotkey('enter', interval=1)
        pyautogui.write(txt, interval=0.3)


    @allure.step('处理点击')
    def click(self, yaml, choice = None):
        sleep(1)
        self.is_click_dcr(user[yaml], choice)
        sleep(2)

    @allure.step('hover')
    def hover(self, ymal, choice=None):
        self.mouse_hover(user[ymal], choice)

    @allure.step('滚动')
    def scrollr(self, x, y):
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.scroll(-500)



    @allure.step('滚动移动')
    def drag_and_drop_scroll(self, x1, y1, x2, y2):
        # currentMouseX, currentMouseY = pyautogui.position()
        # pyautogui.click(currentMouseX, currentMouseY)
        # self.is_click(user[ymal], choice)
        pyautogui.moveTo(399, 650, duration=1)
        pyautogui.scroll(-500)
        pyautogui.moveTo(x1, y1, duration=1)
        pyautogui.dragTo(x2, y2, duration=1, button='left')
        # actions = ActionChains(self.driver)
        # actions.drag_and_drop(drag, drop).perform()
        sleep(2)

    @allure.step('移动')
    def drag_and_drop_tlc(self, x1, y1, x2, y2):
        # currentMouseX, currentMouseY = pyautogui.position()
        # pyautogui.click(currentMouseX, currentMouseY)
        # self.is_click(user[ymal], choice)
        # pyautogui.moveTo(399, 650, duration=1)
        # pyautogui.scroll(-500)
        pyautogui.moveTo(x1, y1, duration=1)
        pyautogui.dragTo(x2, y2, duration=1, button='left')
        # actions = ActionChains(self.driver)
        # actions.drag_and_drop(drag, drop).perform()
        sleep(2)


if __name__ == '__main__':

    pass