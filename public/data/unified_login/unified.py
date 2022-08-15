from libs.common.read_csv import *

account = readCsvDict(os.path.join(PUBLIC_DATA_PATH, 'account.csv')) # 统一认证登录
account_srm= readCsvDict(os.path.join(PUBLIC_DATA_PATH, 'account_srm.csv')) # srm统一认证登录