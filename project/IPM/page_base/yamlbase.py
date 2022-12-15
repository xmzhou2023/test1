import yaml
from libs.config.conf import *



class YamlRead():

    def __init__(self,filename):
        self.filename=filename


    def yaml_read(self,Variable_name):
        yaml_path = os.path.join(os.path.join(PEROJECT_PATH,'IPM','data'), self.filename)
        print(os.path.join(PEROJECT_PATH,'IPM','data'))
        f = open(yaml_path, 'r', encoding='UTF-8')
        cfg = f.read()
        d = yaml.load(cfg, Loader=yaml.FullLoader)
        return d[Variable_name]


if __name__ == '__main__':
    print(os.path.join(PEROJECT_PATH,'IPM','data'))

file=YamlRead(r'material_A.yaml')
# A1=file.yaml_read('前')
# B1=file.yaml_read('后')


# A1=file.yaml_read('前端物料长描述')
# B1=file.yaml_read('后端物料长描述')

#
# A1=file.yaml_read('IPM颜色')
# B1=file.yaml_read('SAP颜色')
# # 同时遍历两个列表中的元素
# for (i1, i2) in zip(A1, B1):
#     # 由于price列表中的元素是数字，因此用str()转为字符串
#     try:
#         assert i1 is i2
#     except:
#         print(f'前端和后端结果不相等：{i1},{i2}')
