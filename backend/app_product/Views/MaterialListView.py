from app_product.Views import MaterialList
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
import json

@require_GET
def getMaterialList(request):
    """
    根据产品ID和数量返回所需要的原材料ID、名称、数量，提供给前端领料单信息
    :param request: GET task/material-list?product_id=*&product_num=*
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

    """
    product_id, product_num = request.GET.get("product_id"), request.GET.get("product_num")
    if(product_id and product_num):
        material_list = MaterialList.getMaterialList(product_id, product_num)
        return JsonResponse(material_list)
    else:
        return JsonResponse({}, status=401)
