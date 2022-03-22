import os
import sys
from common.read_env import environ
import yaml

folderPath = os.path.dirname(os.path.dirname(__file__)) + r'/data/DRP/'

def get_yaml_filepath(Environ="",filepath=""):
    Environ1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + environ)  # 拼接定位到data文件夹
    filepath1 =os.path.abspath(folderPath + '/' + filepath)  # 拼接定位到data文件夹

    if Environ:
        with open(Environ1, "r", encoding='utf-8')as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    if filepath:
        with open(filepath1, "r", encoding='utf-8')as f:
            return yaml.load(f, Loader=yaml.FullLoader)

if __name__ == '__main__':

    print(get_yaml_filepath(Environ=environ))
    print(get_yaml_filepath(filepath="system_management/sys_user_add.yaml"))

