import allure
import pytest
from public.data.unified_login.unified import *

from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.SystemMgmt_UserMgmt import UserPage

@allure.feature("系统管理-aaaaaaa")
class TestSearchUser: # Test+(增，删，改，查，导入（上传），导出（下载）)

    @allure.story("查询aaaa")
    @allure.title("aaaaaaaabbbbbbb")
    @allure.description("aaaaaaaaaaa111aaaaaaaaa1")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.RT
    def test_001_001(self, drivers):
        pass

@allure.feature("系统管理-aaaaaaa")
class TestAppendUser:
    @allure.story("新建aaaa")
    @allure.title("bbbbbbbbcccccc")
    @allure.description("bbbbbbbbbbb11aaaaaaaaaa1")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_002_001(self, drivers):
        pass


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])

