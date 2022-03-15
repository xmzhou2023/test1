import os
import sys
from common.read_env import environ
import yaml

folderPath = os.path.dirname(os.path.dirname(__file__)) + r'/data/DRP/'

def get_yaml_filepath(Environ="",filepath=""):
    Environ1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + environ)  # 拼接定位到data文件夹
    filepath1 =os.path.abspath(folderPath + '/' + filepath)  # 拼接定位到data文件夹
    # print(Environ1,filepath1)
    if Environ:
        with open(Environ1, "r", encoding='utf-8')as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    if filepath:
        with open(filepath1, "r", encoding='utf-8')as f:
            return yaml.load(f, Loader=yaml.FullLoader)

if __name__ == '__main__':

    print(get_yaml_filepath(Environ=environ))
    print(get_yaml_filepath(filepath="system_management/sys_user_add.yaml"))
#     print("ggg",get_yaml_filepath(filepath='member_controller\login.yaml'))
# class ReadYamlConfigs():
#     def __init__(self,filename):
#
#
#         self.filepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + Environ)+"/"+filename#拼接定位到data文件夹
#
#     def get_yaml_data(self):
#         with open(self.filepath, "r", encoding="utf-8")as f:
#             # 调用load方法加载文件流
#             return yaml.load(f,Loader=yaml.FullLoader)
#
# class ReadYamlData():
#     def __init__(self,filename):
#         self.filepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + r"/data")+"/"+filename#拼接定位到data文件夹
#
#     def get_yaml_data(self):
#         with open(self.filepath, "r", encoding="utf-8")as f:
#             # 调用load方法加载文件流
#             return yaml.load(f,Loader=yaml.FullLoader)
#
# Environ = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + Environ)+"/"+filename#拼接定位到data文件夹
# filepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + r"/data")+"/"+filename#拼接定位到data文件夹


# def get_yaml_Environ(Environ):
#     with open(Environ, "r", encoding="utf-8")as f:
#         # 调用load方法加载文件流
#         return yaml.load(f, Loader=yaml.FullLoader)
#
# def get_yaml_filepath(filepath):
#     with open(filepath, "r", encoding="utf-8")as f:
#         # 调用load方法加载文件流
#         return yaml.load(f, Loader=yaml.FullLoader)
#
# def get_yaml_filepath(filepath=None,Environ=None):
#     with open((filepath,Environ), "r", encoding="utf-8")as f:
#         # 调用load方法加载文件流
#         return yaml.load(f, Loader=yaml.FullLoader)
# if __name__ == '__main__':
#     data = ReadYaml("data.yaml").get_yaml_data()
#     data1 = ReadYaml_anjiekou("duo_data/admin_data/1,login_data.yml").get_yaml_data()  # 读取数据
#     print(data)
#     print(data1['login'])
