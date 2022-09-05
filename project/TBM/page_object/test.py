import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class BOM(Base):
    """用户类"""

    @allure.step("查找工号")
    def search_user(self, jobnum=None,name=None):
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

    @allure.step("点击菜单")
    def click_menu(self):
        self.is_click_tbm(user['一级菜单'])
        self.is_click_tbm(user['二级菜单'])
        self.refresh()

    @allure.step("点击新增")
    def click_add(self):
        self.is_click_tbm(user['新增'])
        sleep(1)

    @allure.step("Bom信息-制作类型")
    def click_type(self):
        self.is_click_tbm(user['Bom信息-制作类型'])
        self.is_click_tbm(user['Bom信息-生产BOM'])

    @allure.step("Bom信息-品牌")
    def click_brand(self):
        self.is_click_tbm(user['Bom信息-品牌'])
        self.is_click_tbm(user['Bom信息-itel'])

    @allure.step("Bom信息-机型")
    def click_mach(self):
        self.readonly_input_text(user['Bom信息-机型'], 'C3250')
        sleep(2)
        self.is_click_tbm(user['Bom信息-C3250'])

    @allure.step("Bom信息-阶段")
    def click_stage(self):
        self.is_click_tbm(user['Bom信息-阶段'])
        self.is_click_tbm(user['Bom信息-量产阶段'])

    @allure.step("Bom信息-市场")
    def click_market(self):
        self.is_click_tbm(user['Bom信息-市场'])
        self.is_click_tbm(user['Bom信息-孟加拉'])

    @allure.step("新增Bom")
    def click_addBom(self):
        self.is_click_tbm(user['新增Bom'])

    @allure.step("新增Bom-Bom类型")
    def click_Bomtype(self):
        self.is_click_tbm(user['新增Bom-Bom类型'])
        self.is_click_tbm(user['新增Bom-国内生产BOM'])

    @allure.step("新增Bom-Bom状态")
    def click_Bomstatus(self):
        self.is_click_tbm(user['新增Bom-Bom状态'])
        self.is_click_tbm(user['新增Bom-转量产'])

    @allure.step("新增Bom-物料编码")
    def click_code(self):
        self.readonly_input_text(user['新增Bom-物料编码'], '12000001')
        self.is_click_tbm(user['新增Bom-12000001'])

    @allure.step("新增Bom-用量")
    def click_sum(self):
        self.readonly_input_text(user['新增Bom-用量'], '1000')

    @allure.step("新增Bom-确定")
    def click_comfirm(self):
        self.is_click_tbm(user['新增Bom-确定'])

    @allure.step("新增Bom-编辑")
    def click_edit(self):
        self.is_click_tbm(user['新增Bom-编辑'])

    @allure.step("审核人设置-MPM")
    def click_audit_mpm(self):
        self.is_click_tbm(user['审核人设置-MPM'])
        self.input_text(user['审核人设置-成员列表输入'], '李小素')
        self.is_click_tbm(user['审核人设置-18645960'])
        self.is_click_tbm(user['审核人设置-确定'])

    @allure.step("审核人设置-采购部")
    def click_audit_nps(self):
        self.is_click_tbm(user['审核人设置-采购部'])
        self.input_text(user['审核人设置-成员列表输入'], '李小素')
        self.is_click_tbm(user['审核人设置-18645960'])
        self.is_click_tbm(user['审核人设置-确定'])

    @allure.step("提交")
    def click_submit(self):
        self.is_click_tbm(user['提交'])

    @allure.step("查询")
    def click_search(self):
        self.is_click_tbm(user['查询'])

    @allure.step("流程编码")
    def get_code(self):
        code = self.element_text(user['流程编码'])
        return code

    @allure.step("待办列表-我申请的")
    def click_todo(self):
        self.is_click_tbm(user['待办列表'])
        self.is_click_tbm(user['我申请的'])
        self.refresh()
        self.frame_enter(user['iframe'])
        self.refresh()

    @allure.step("待办列表-查看详情")
    def click_app(self):
        self.is_click_tbm(user['查看详情'])
        self.switch_window(1)
        self.frame_enter(user['iframe'])

    @allure.step("撤回")
    def click_recall(self):
        self.is_click_tbm(user['撤回'])
        self.is_click_tbm(user['撤回确定'])
        self.close_switch(1)

    @allure.step("删除")
    def click_delete(self):
        self.is_click_tbm(user['查询'])
        self.is_click_tbm(user['删除'])
        self.is_click_tbm(user['撤回确定'])
if __name__ == '__main__':
    pass
