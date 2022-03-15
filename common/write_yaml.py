import os
import sys
import yaml

folderPath = os.path.dirname(os.path.dirname(__file__)) + r'/data/DRP/Submit_for_review/manage_3_differance_confirm.yaml'
yaml_testlist = [{'interfacesID': 5987, 'interfacesName': '终审差异确认', 'interfaceURL': '/drp/manage/3/differance/confirm', 'parameterInfo': '[{year=Number}, {month=Number}, {mgmtDimensionCode=String}, {version=Number}, {brandCode=String}]', 'interfacesMethod': 'POST', 'interfacesModuleCN': '提报评审', 'interfacesModuleEN': 'Submit_for_review', 'reason': None}]

def write_yaml(yaml_list,filepath=""):
    with open(filepath, 'w',encoding='utf-8') as yaml_file:
        yaml.dump(yaml_list, yaml_file, default_flow_style=False,allow_unicode=True,width=1000)

if __name__ == '__main__':
    write_yaml(yaml_testlist,folderPath)
