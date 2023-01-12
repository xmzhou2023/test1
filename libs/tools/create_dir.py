import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_path)
from libs.common.read_csv import *
from libs.config.conf import PEROJECT_PATH, BASE_DIR
import logging
import os
import shutil

# 自动新增文件夹
PERO_PATH = os.path.join(PEROJECT_PATH, 'MGDP')
# 创建文件依据
path = os.path.join('template/modle_name.csv')

# 引用模板位置
CASE_TEMPLATE_PATH = os.path.join('template/case_template.py')
OBJECT_TEMPLATE_PATH = os.path.join('template/object_template.py')
ELEMENT_TEMPLATE_PATH = os.path.join('template/element_template.yaml')
CONFTEST_TEMPLATE_PATH = os.path.join('template/conftest.py')
ENV_TEMPLATE_PATH = os.path.join(BASE_DIR,'libs','tools','template','env')

# 文件下载路径
CASE_PATH = os.path.join(PERO_PATH, 'test_case/')
OBJECT_PATH = os.path.join(PERO_PATH, 'page_object/')
ELEMENT_PATH = os.path.join(PERO_PATH, 'page_element/')
ENV_PATH = os.path.join(PERO_PATH, 'env')

def read_file(filepaxh):
    with open(filepaxh, 'r', encoding='utf-8') as file:
        txt = file.read()
        file.close()
    return txt

def mk_file(full_path, msg):
    if not os.path.exists(full_path) :
        file = open(full_path, 'w', encoding='utf-8')    # w 的含义为可进行读写
        file.write(msg)        #file.write()为写入指令
        file.close()
        logging.info("生成成功: 模块文件名为 | {} ".format(full_path))

def mk_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

def read_dir(dir_name):
    return os.path.isdir(dir_name)

def text_create(name, type="case"):
    if type == "element":
        desktop_path = ELEMENT_PATH
        mk_dir(desktop_path)
        full_path = desktop_path + name + '.yaml'   # 创建元素定位库yaml文件
        msg = read_file(ELEMENT_TEMPLATE_PATH)
        mk_file(full_path, msg)

    elif type == "object":
        desktop_path = OBJECT_PATH
        mk_dir(desktop_path)
        full_path = desktop_path + name + '.py'     # 创建页面对象
        msg = read_file(OBJECT_TEMPLATE_PATH)
        mk_file(full_path, msg)
    else:
        desktop_path = CASE_PATH     # 新创建的txt文件的存放路径
        mk_dir(desktop_path)
        full_path = desktop_path + name + '.py'
        msg = read_file(CASE_TEMPLATE_PATH)
        mk_file(full_path, msg)
        conftest_path = desktop_path + 'conftest.py'
        msg = read_file(CONFTEST_TEMPLATE_PATH)
        mk_file(conftest_path, msg)

def generate_module(file_type):
        list = readCsv(path)
        for i in range(len(list)):
            text_create(name=list[i][0],type=file_type)

def generate_env():
    try:
        shutil.copytree(ENV_TEMPLATE_PATH, ENV_PATH)
    except FileExistsError as e:
        print(e)

if __name__ == '__main__':
    generate_module("element")
    generate_module("object")
    generate_module("test_case")
    # generate_env()



