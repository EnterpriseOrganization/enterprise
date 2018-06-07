from enterprise.models import ProductMaterial, Material

def getMaterialList(product_id, product_num):
    '''
    根据产品ID和数量返回所需要的原材料ID、名称、数量，提供给前端领料单信息
    :param pro_id:领料单中的产品ID(一个领料单只会有一种产品)
    :param pro_num:领料单中产品的数量
    :return:
        {
            "material_requisition":[
                {
                    "material_id":id,
                    "material_name":name,
                    "material_num":num
                },
                {

                }
            ]
        }
    '''

    material_list = ProductMaterial.objects.select_related('material') \
        .values('material_id', 'material__name', 'number') \
        .filter(product_id = product_id)
    
    mlist = []

    for material in material_list:
        # material["number"] = material["number"] * pro_num
        mlist.append({
            "material_id":material["material_id"],
            "material_name":material["material__name"],
            "material_num":material["number"] * int(product_num)
        })

    return {"material_requisition":mlist}