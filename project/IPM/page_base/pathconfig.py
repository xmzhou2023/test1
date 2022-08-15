import os

PATH=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA=os.path.join(PATH,'IPM\data')
print(DATA)
#手机物料
Mobile_Material=os.path.join(PATH,'IPM\data\手机物料')
#手机物料-二级BOM
Mobile_SecondaryMaterial=os.path.join(PATH,'IPM\data\手机物料-二级BOM')
#配件物料
AccessoryMaterials=os.path.join(PATH,'IPM\data\配件物料')
#ODM物料
ODM_Material=os.path.join(PATH,'IPM\data\ODM物料')

SecondaryMaterial=os.path.join(PATH,'IPM\data\二级物料')

print(SecondaryMaterial)