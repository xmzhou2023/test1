# -*- coding: utf-8 -*-
# @Time    : 2022-08-01 17:28
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : login.py
# @Software: PyCharm
from libs.common.read_csv import *
from libs.config.conf import *

mes_account = readCsvDict(os.path.join(PEROJECT_PATH, 'MES_DAP', 'data', 'mes_account.csv')) # mes登录