from project.IPM.api.APIRequest import *



# ApplyList=Api.Api_applyList(20220810085734677324)
# Api.Api_queryDeptAndEmployee(20220810085734677324)
def Get_required_fields(proname,fill):
    '''
    获取项目管理字段获取

    '''
    Api = APIRequest()
    field_att = Api.Api_project_field(proname)
    for i in field_att:
        if i.get("是否展示") ==True:
            if i.get("是否可读") ==False:
                if i.get("是否必填") ==True:
                    if fill == '填写':
                        if i.get("类型") =='text':
                            print(i.get("类型"))
                        if i.get("类型") == 'select':
                            print(i.get("类型"))
                        if i.get("类型") == 'date':
                            print(i.get("类型"))
                    else:
                        return i.get('字段名')

                else:
                    if i.get("类型") == 'text':
                        print(i.get("类型"))
                    if i.get("类型") == 'select':
                        print(i.get("类型"))
                    if i.get("类型") == 'date':
                        print(i.get("类型"))


def Get_notrequired_fields(proname):
    '''获取项目管理非必填字段'''
    field_att = Api.Api_project_field(proname)
    for i in field_att:
        if i.get("是否展示") ==True:
            if i.get("是否可读") ==False:
                if i.get("是否必填") ==False:
                    return i.get('字段名')


if __name__ == '__main__':
    Get_required_fields("IPM自动化2022-12-0813:39:12")