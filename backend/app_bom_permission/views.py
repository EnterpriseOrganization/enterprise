from django.shortcuts import render
from django.db.models import Q
from functools import reduce 
from django.http import HttpResponse
from enterprise.models import Material, MaterialClass
import json

# Create your views here.

# Material Operations
class MaterialProcessor:
    #util
    @staticmethod
    def material_list_to_json(result):
        ret = {"data": []}
        for item in result:
            ret["data"].append(single_material_to_dict(item))
        return json.dumps(ret)

    @staticmethod
    def single_material_to_dict(item):
        return {"name": item.name, "class_obj": item.class_obj.class_field, "id": item.id}

    @staticmethod
    def get_material_Q(request):
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
        return Q_list

    # process all
    @staticmethod
    def process_material(request):
        if request.method == "GET":
            return filter_material(request)
        if request.method == "DELETE":
            return delete_material(request)
        if request.method == "POST":
            return create_material(request)
            
    @staticmethod
    def filter_material(request):
        Q_list = get_material_Q(request)
        if Q_list:
            print(Q_list)
            final_Q = reduce(lambda x,y: x|y, Q_list)
            result = Material.objects.filter(final_Q)
            return HttpResponse(material_list_to_json(result), content_type="application/json")
        else:
            print("null request for all objects")
            result = Material.objects.all()
            return HttpResponse(material_list_to_json(result), content_type="application/json")

    @staticmethod
    def delete_material(request):
        data = json.loads(request.body)["data"]
        id_list = [item["id"] for item in data]
        for i in id_list:
            m = Material.objects.get(id=i)
            m.delete()
        return HttpResponse(status=204)

    @staticmethod
    def create_material(request):
        name_str = request.GET.get("name")
        class_obj_str = request.GET.get("class_obj")
        class_obj = MaterialClass.GET.get(class_field=class_obj_str)
        m = Material(name=name_str, class_obj=class_obj)
        return HttpResponse(201)

    #process specific material
    @staticmethod
    def process_specific_material(request, param_id):
        if request.method == "PUT":
            return modify_specific_material(request, param_id)
        if request.method == "DELETE":
            return delete_specific_material(request, param_id)

    #TODO: Object not found
    @staticmethod
    def modify_specific_material(request, param_id):
        name_str = request.GET.get("name")
        class_obj_str = request.GET.get("class_obj")
        class_obj = MaterialClass.GET.get(class_field=class_obj_str)
        item = Material.objects.get(id=int(param_id))
        item.name = name_str
        item.class_obj = class_obj
        item.save()
        return HttpResponse(status=201)

    #TODO: Object not found
    @staticmethod
    def delete_specific_material(request, param_id):
        item = Material.objects.get(id=int(param_id))
        item.delete()
        return HttpResponse(status=204)    
    