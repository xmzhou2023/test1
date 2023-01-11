import os

PATH=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA=os.path.join(PATH,'IPM\data')

MaterialRequisitionPATH=os.path.join(PATH,'IPM\data\ProcessCenter_MaterialRequisition_Add')
path_system_management = os.path.join(DATA)
# #手机物料
# Mobile_Material=os.path.join(MaterialRequisitionPATH,'手机物料\手机物料导入')
# #手机物料-二级BOM
# Mobile_SecondaryMaterial=os.path.join(MaterialRequisitionPATH,'手机物料-二级BOM\手机物料-二级BOM导入')
# #配件物料
# AccessoryMaterials=os.path.join(MaterialRequisitionPATH,'配件物料\配件物料导入')
# #ODM物料
# ODM_Material=os.path.join(MaterialRequisitionPATH,'ODM物料\ODM物料导入')
#
# SecondaryMaterial=os.path.join(MaterialRequisitionPATH,'data\二级物料\二级物料导入')
