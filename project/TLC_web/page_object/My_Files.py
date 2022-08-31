import allure
from public.base.basics import Base
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
from ..test_case.conftest import *
pro_env = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, pro_env)

