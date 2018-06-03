from django.shortcuts import render
from django.db.models import Q
from functools import reduce 
from django.http import HttpResponse
from enterprise.models import Material, MaterialClass, Product, ProductClass
import json

# Create your views here.
# MaterialClass Operations

class MaterialClassProcessor:

    @staticmethod
    def materialclass_list_to_json(result):
        ret = {"data": []}
        for item in result:
            ret["data"].append(MaterialClassProcessor.single_materialclass_to_dict(item))
        return json.dumps(ret)

    @staticmethod
    def single_materialclass_to_dict(item):
        return {"class_field": item.class_field, "class_id": item.id}

    @staticmethod
    def get(request):
        if request.method == "GET":
            result = MaterialClass.objects.all()
            return HttpResponse(MaterialClassProcessor.materialclass_list_to_json(result), content_type="application/json")
        else:
            print("Not valid operation for material class")
            return HttpResponse(status=400)




# Material Operations
class MaterialProcessor:
    #util
    @staticmethod
    def material_list_to_json(result):
        ret = {"data": []}
        for item in result:
            ret["data"].append(MaterialProcessor.single_material_to_dict(item))
        return json.dumps(ret)

    @staticmethod
    def single_material_to_dict(item):
        return {"name": item.name, "class_id": item.class_obj.id, "id": item.id, "class_field": item.class_obj.class_field}

    @staticmethod
    def get_material_Q(request):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        id_str = request.GET.get("id")
        Q_list = []
        if name_str != "null":
            Q_list.append(Q(name=name_str))
        if class_id_str and class_id_str != "null":
            Q_list.append(Q(class_obj__id=int(class_id_str)))
        if id_str != "null":
            Q_list.append(Q(id=int(id_str)))
        return Q_list

    # process all
    @staticmethod
    def process_material(request):
        if request.method == "GET":
            return MaterialProcessor.filter_material(request)
        if request.method == "DELETE":
            return MaterialProcessor.delete_material(request)
        if request.method == "POST":
            return MaterialProcessor.create_material(request)
            
    @staticmethod
    def filter_material(request):
        Q_list = MaterialProcessor.get_material_Q(request)
        if Q_list:
            print(Q_list)
            final_Q = reduce(lambda x,y: x|y, Q_list)
            result = Material.objects.filter(final_Q)
            return HttpResponse(MaterialProcessor.material_list_to_json(result), content_type="application/json")
        else:
            print("null request for all objects")
            result = Material.objects.all()
            return HttpResponse(MaterialProcessor.material_list_to_json(result), content_type="application/json")

    @staticmethod
    def delete_material(request):
        print(request.body.decode())
        data = json.loads(request.body.decode())["data"]
        id_list = [item["id"] for item in data]
        for i in id_list:
            m = Material.objects.get(id=int(i))
            m.delete()
        return HttpResponse(status=204)

    @staticmethod
    def create_material(request):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        class_obj = MaterialClass.objects.get(id=int(class_id_str))
        m = Material(name=name_str, class_obj=class_obj)
        m.save()
        return HttpResponse(201)

    #process specific material
    @staticmethod
    def process_specific_material(request, param_id):
        if request.method == "PUT":
            return MaterialProcessor.modify_specific_material(request, param_id)
        if request.method == "DELETE":
            return MaterialProcessor.delete_specific_material(request, param_id)
        if request.method == "GET":
            return MaterialProcessor.get_specific_material(request, param_id)

    #TODO: Object not found
    @staticmethod
    def modify_specific_material(request, param_id):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        class_obj = MaterialClass.objects.get(id=int(class_id_str))
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

    @staticmethod
    def get_specific_material(request, param_id):
        item = Material.objects.get(id=int(param_id))
        return HttpResponse(json.dumps(MaterialProcessor.single_material_to_dict(item)), content_type="application/json")


class ProductClassProcessor:

    @staticmethod
    def productclass_list_to_json(result):
        ret = {"data": []}
        for item in result:
            ret["data"].append(ProductClassProcessor.single_productclass_to_dict(item))
        return json.dumps(ret)

    @staticmethod
    def single_productclass_to_dict(item):
        return {"class_field": item.class_field, "class_id": item.id}

    @staticmethod
    def get(request):
        if request.method == "GET":
            result = ProductClass.objects.all()
            return HttpResponse(ProductClassProcessor.productclass_list_to_json(result), content_type="application/json")
        else:
            print("Not valid operation for product class")
            return HttpResponse(status=400)

class ProductProcessor:
    #util
    @staticmethod
    def product_list_to_json(result):
        ret = {"data": []}
        for item in result:
            ret["data"].append(ProductProcessor.single_product_to_dict(item))
        return json.dumps(ret)

    @staticmethod
    def single_product_to_dict(item):
        return {"name": item.name, 
                "class_id": item.class_obj.id, 
                "id": item.id,
                "price": item.price
                }

    # TODO: filter for price
    @staticmethod
    def get_product_Q(request):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        id_str = request.GET.get("id")
        Q_list = []
        if name_str != "null":
            Q_list.append(Q(name=name_str))
        if class_id_str and class_id_str != "null":
            Q_list.append(Q(class_obj__id=int(class_id_str)))
        if id_str != "null":
            Q_list.append(Q(id=int(id_str)))
        return Q_list

    # process all
    @staticmethod
    def process_product(request):
        if request.method == "GET":
            return ProductProcessor.filter_product(request)
        if request.method == "DELETE":
            return ProductProcessor.delete_product(request)
        if request.method == "POST":
            return ProductProcessor.create_product(request)
            
    @staticmethod
    def filter_product(request):
        Q_list = ProductProcessor.get_product_Q(request)
        if Q_list:
            print(Q_list)
            final_Q = reduce(lambda x,y: x|y, Q_list)
            result = Product.objects.filter(final_Q)
            return HttpResponse(ProductProcessor.product_list_to_json(result), content_type="application/json")
        else:
            print("null request for all objects")
            result = Product.objects.all()
            return HttpResponse(ProductProcessor.product_list_to_json(result), content_type="application/json")

    @staticmethod
    def delete_product(request):
        data = json.loads(request.body)["data"]
        id_list = [item["id"] for item in data]
        for i in id_list:
            m = Product.objects.get(id=i)
            m.delete()
        return HttpResponse(status=204)

    @staticmethod
    def create_product(request):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        class_obj = ProductClass.objects.get(class_field=int(class_id_str))
        price_str = request.GET.get("price")
        m = Product(name=name_str, class_obj=class_obj, price=float(price_str))
        m.save()
        return HttpResponse(201)

    #process specific Product
    @staticmethod
    def process_specific_product(request, param_id):
        if request.method == "PUT":
            return ProductProcessor.modify_specific_product(request, param_id)
        if request.method == "DELETE":
            return ProductProcessor.delete_specific_product(request, param_id)

    #TODO: Object not found
    @staticmethod
    def modify_specific_product(request, param_id):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        class_obj = ProductClass.objects.get(id=int(class_id_str))
        price_str = request.GET.get("price")
        item = Product.objects.get(id=int(param_id))
        item.name = name_str
        item.class_obj = class_obj
        item.price = float(price_str)
        item.save()
        return HttpResponse(status=201)

    #TODO: Object not found
    @staticmethod
    def delete_specific_product(request, param_id):
        item = Product.objects.get(id=int(param_id))
        item.delete()
        return HttpResponse(status=204)    

