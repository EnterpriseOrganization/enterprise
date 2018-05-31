from django.shortcuts import render
from django.db.models import Q
from functools import reduce 
from django.http import HttpResponse
from enterprise.models import Material, MaterialClass
import json

# Create your views here.

def process_material(request):
    if request.method == "GET":
        return filter_material(request)
    if request.method == "DELETE":
        return delete_material(request)
        
def filter_material(request):
    name_str = request.GET.get("name")
    class_obj_str = request.GET.get("class_obj")
    id_str = request.GET.get("id")
    Q_list = []
    if name_str != "null":
        Q_list.append(Q(name=name_str))
    if class_obj_str != "null":
        Q_list.append(Q(class_obj__class_field=class_obj_str))
    if id_str != "null":
        Q_list.append(Q(id=int(id_str)))
    if Q_list:
        print(Q_list)
        final_Q = reduce(lambda x,y: x|y, Q_list)
        result = Material.objects.filter(final_Q)
        return HttpResponse(material_list_to_json(result), content_type="application/json")
    else:
        print("null request for all objects")
        result = Material.objects.all()
        return HttpResponse(material_list_to_json(result), content_type="application/json")

def material_list_to_json(result):
    ret = {"data": []}
    for item in result:
        ret["data"].append(single_material_to_dict(item))
    return json.dumps(ret)

def single_material_to_dict(item):
    return {"name": item.name, "class_obj": item.class_obj.class_field, "id": item.id}

def delete_material(request):
    return HttpResponse(status="404")    
    