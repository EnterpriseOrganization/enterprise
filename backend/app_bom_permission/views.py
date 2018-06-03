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
    def materialclassListToJson(result):
        ret = {"data": []}
        for item in result:
            ret["data"].append(MaterialClassProcessor.singleMaterialclassToDict(item))
        return json.dumps(ret)

    @staticmethod
    def singleMaterialclassToDict(item):
        return {"class_field": item.class_field, "class_id": item.id}

    @staticmethod
    def get(request):
        if request.method == "GET":
            result = MaterialClass.objects.all()
            return HttpResponse(MaterialClassProcessor.materialclassListToJson(result), content_type="application/json")
        else:
            print("Not valid operation for material class")
            return HttpResponse(status=400)


# Material Operations
class MaterialProcessor:
    # util
    @staticmethod
    def materialListToJson(result):
        ret = {"data": []}
        for item in result:
            ret["data"].append(MaterialProcessor.singleMaterialToDict(item))
        return json.dumps(ret)

    @staticmethod
    def singleMaterialToDict(item):
        return {"name": item.name, 
                "class_id": item.class_obj.id, 
                "id": item.id, 
                "class_field": item.class_obj.class_field
                }

    @staticmethod
    def getMaterialQ(request):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        id_str = request.GET.get("id")
        Q_list = []
        if name_str and name_str != "null":
            Q_list.append(Q(name=name_str))
        if class_id_str and class_id_str != "null":
            Q_list.append(Q(class_obj__id=int(class_id_str)))
        if name_str and id_str != "null":
            Q_list.append(Q(id=int(id_str)))
        return Q_list

    # process all
    @staticmethod
    def processMaterial(request):
        if request.method == "GET":
            return MaterialProcessor.filterMaterial(request)
        if request.method == "DELETE":
            return MaterialProcessor.deleteMaterial(request)
        if request.method == "POST":
            return MaterialProcessor.createMaterial(request)
            
    @staticmethod
    def filterMaterial(request):
        Q_list = MaterialProcessor.getMaterialQ(request)
        if Q_list:
            print(Q_list)
            final_Q = reduce(lambda x,y: x|y, Q_list)
            result = Material.objects.filter(final_Q)
            return HttpResponse(MaterialProcessor.materialListToJson(result), content_type="application/json")
        else:
            print("null request for all objects")
            result = Material.objects.all()
            return HttpResponse(MaterialProcessor.materialListToJson(result), content_type="application/json")

    @staticmethod
    def deleteMaterial(request):
        data = json.loads(request.body.decode())["data"]
        id_list = [item["id"] for item in data]
        for i in id_list:
            m = Material.objects.get(id=int(i))
            m.delete()
        return HttpResponse(status=204)

    @staticmethod
    def createMaterial(request):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        class_obj = MaterialClass.objects.get(id=int(class_id_str))
        m = Material(name=name_str, class_obj=class_obj)
        m.save()
        return HttpResponse(201)

    # process specific material
    @staticmethod
    def processSpecificMaterial(request, param_id):
        if request.method == "PUT":
            return MaterialProcessor.modifySpecificMaterial(request, param_id)
        if request.method == "DELETE":
            return MaterialProcessor.deleteSpecificMaterial(request, param_id)
        if request.method == "GET":
            return MaterialProcessor.getSpecificMaterial(request, param_id)

    # TODO: Object not found
    @staticmethod
    def modifySpecificMaterial(request, param_id):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        class_obj = MaterialClass.objects.get(id=int(class_id_str))
        item = Material.objects.get(id=int(param_id))
        item.name = name_str
        item.class_obj = class_obj
        item.save()
        return HttpResponse(status=201)

    # TODO: Object not found
    @staticmethod
    def deleteSpecificMaterial(request, param_id):
        item = Material.objects.get(id=int(param_id))
        item.delete()
        return HttpResponse(status=204)    

    @staticmethod
    def getSpecificMaterial(request, param_id):
        item = Material.objects.get(id=int(param_id))
        return HttpResponse(json.dumps(MaterialProcessor.singleMaterialToDict(item)), content_type="application/json")


class ProductClassProcessor:

    @staticmethod
    def productclassListToJson(result):
        ret = {"data": []}
        for item in result:
            ret["data"].append(ProductClassProcessor.singleProductclassToDict(item))
        return json.dumps(ret)

    @staticmethod
    def singleProductclassToDict(item):
        return {"class_field": item.class_field, "class_id": item.id}

    @staticmethod
    def get(request):
        if request.method == "GET":
            result = ProductClass.objects.all()
            return HttpResponse(ProductClassProcessor.productclassListToJson(result), content_type="application/json")
        else:
            print("Not valid operation for product class")
            return HttpResponse(status=400)

class ProductProcessor:
    # util
    @staticmethod
    def productListToJson(result):
        ret = {"data": []}
        for item in result:
            ret["data"].append(ProductProcessor.singleProductToDict(item))
        return json.dumps(ret)

    @staticmethod
    def singleProductToDict(item):
        return {"name": item.name, 
                "class_id": item.class_obj.id, 
                "id": item.id,
                "price": item.price,
                "class_field": item.class_obj.class_field
                }

    # TODO: filter for price
    @staticmethod
    def getProductQ(request):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        id_str = request.GET.get("id")
        Q_list = []
        if name_str and name_str != "null":
            Q_list.append(Q(name=name_str))
        if class_id_str and class_id_str != "null":
            Q_list.append(Q(class_obj__id=int(class_id_str)))
        if name_str and id_str != "null":
            Q_list.append(Q(id=int(id_str)))
        return Q_list

    # process all
    @staticmethod
    def processProduct(request):
        if request.method == "GET":
            return ProductProcessor.filterProduct(request)
        if request.method == "DELETE":
            return ProductProcessor.deleteProduct(request)
        if request.method == "POST":
            return ProductProcessor.createProduct(request)
            
    @staticmethod
    def filterProduct(request):
        Q_list = ProductProcessor.getProductQ(request)
        if Q_list:
            print(Q_list)
            final_Q = reduce(lambda x,y: x|y, Q_list)
            result = Product.objects.filter(final_Q)
            return HttpResponse(ProductProcessor.productListToJson(result), content_type="application/json")
        else:
            print("null request for all objects")
            result = Product.objects.all()
            return HttpResponse(ProductProcessor.productListToJson(result), content_type="application/json")

    @staticmethod
    def deleteProduct(request):
        data = json.loads(request.body.decode())["data"]
        id_list = [item["id"] for item in data]
        for i in id_list:
            m = Product.objects.get(id=i)
            m.delete()
        return HttpResponse(status=204)

    @staticmethod
    def createProduct(request):
        name_str = request.GET.get("name")
        class_id_str = request.GET.get("class_id")
        class_obj = ProductClass.objects.get(id=int(class_id_str))
        price_str = request.GET.get("price")
        m = Product(name=name_str, class_obj=class_obj, price=float(price_str))
        m.save()
        return HttpResponse(201)

    # process specific Product
    @staticmethod
    def processSpecificProduct(request, param_id):
        if request.method == "PUT":
            return ProductProcessor.modifySpecificProduct(request, param_id)
        if request.method == "DELETE":
            return ProductProcessor.deleteSpecificProduct(request, param_id)
        if request.method == "GET":
            return ProductProcessor.getSpecificProduct(request, param_id)

    # TODO: Object not found
    @staticmethod
    def modifySpecificProduct(request, param_id):
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

    # TODO: Object not found
    @staticmethod
    def deleteSpecificProduct(request, param_id):
        item = Product.objects.get(id=int(param_id))
        item.delete()
        return HttpResponse(status=204)    

    @staticmethod
    def getSpecificProduct(request, param_id):
        item = Product.objects.get(id=int(param_id))
        return HttpResponse(json.dumps(ProductProcessor.singleProductToDict(item)), content_type="application/json")


    
# class ProductmaterialProcessor:
#     # util
#     @staticmethod
#     def productmaterialListToJson(result):
#         ret = {"data": []}
#         for item in result:
#             ret["data"].append(ProductmaterialProcessor.singleProductmaterialToDict(item))
#         return json.dumps(ret)

#     @staticmethod
#     def singleProductmaterialToDict(item):
#         return {"id": item.id,
#                 "product_id": item.product.id,
#                 "product_class_field": item.product.class_field,
#                 "material_id": item.material.id,
#                 "material_class_field": item.material.class_field,
#                 "procedure": item.procedure,
#                 "number": item.number,
#                 "comments": item.comments
#                 }

#     # TODO: filter for 
#     @staticmethod
#     def getProductmaterialQ(request):
#         name_str = request.GET.get("name")
#         class_id_str = request.GET.get("class_id")
#         id_str = request.GET.get("id")
#         Q_list = []
#         if name_str and name_str != "null":
#             Q_list.append(Q(name=name_str))
#         if class_id_str and class_id_str != "null":
#             Q_list.append(Q(class_obj__id=int(class_id_str)))
#         if name_str and id_str != "null":
#             Q_list.append(Q(id=int(id_str)))
#         return Q_list

#     # # process all
#     # @staticmethod
#     # def processProductmaterial(request):
#     #     if request.method == "GET":
#     #         return ProductProcessor.filterProductmaterial(request)
#     #     if request.method == "DELETE":
#     #         return ProductProcessor.deleteProductmaterial(request)
#     #     if request.method == "POST":
#     #         return ProductProcessor.createProductmaterial(request)

#     @staticmethod
#     def processProductmaterialForCertainProduct(request, param):
#         if request.method == "GET":
#             return ProductProcessor.filterProductmaterial(request)
#         if request.method == "DELETE":
#             return ProductProcessor.deleteProductmaterial(request)
#         if request.method == "POST":
#             return ProductProcessor.createProductmaterial(request)

#     if 
            
#     @staticmethod
#     def filterProductmaterial(request):
#         Q_list = ProductProcessor.getProductQ(request)
#         if Q_list:
#             print(Q_list)
#             final_Q = reduce(lambda x,y: x|y, Q_list)
#             result = Product.objects.filter(final_Q)
#             return HttpResponse(ProductProcessor.productListToJson(result), content_type="application/json")
#         else:
#             print("null request for all objects")
#             result = Product.objects.all()
#             return HttpResponse(ProductProcessor.productListToJson(result), content_type="application/json")

#     @staticmethod
#     def deleteProduct(request):
#         data = json.loads(request.body.decode())["data"]
#         id_list = [item["id"] for item in data]
#         for i in id_list:
#             m = Product.objects.get(id=i)
#             m.delete()
#         return HttpResponse(status=204)

#     @staticmethod
#     def createProduct(request):
#         name_str = request.GET.get("name")
#         class_id_str = request.GET.get("class_id")
#         class_obj = ProductClass.objects.get(class_field=int(class_id_str))
#         price_str = request.GET.get("price")
#         m = Product(name=name_str, class_obj=class_obj, price=float(price_str))
#         m.save()
#         return HttpResponse(201)

#     # process specific Product
#     @staticmethod
#     def processSpecificProduct(request, param_id):
#         if request.method == "PUT":
#             return ProductProcessor.modifySpecificProduct(request, param_id)
#         if request.method == "DELETE":
#             return ProductProcessor.deleteSpecificProduct(request, param_id)
#         if request.method == "GET":
#             return ProductProcessor.getSpecificProduct(request, param_id)

#     # TODO: Object not found
#     @staticmethod
#     def modifySpecificProduct(request, param_id):
#         name_str = request.GET.get("name")
#         class_id_str = request.GET.get("class_id")
#         class_obj = ProductClass.objects.get(id=int(class_id_str))
#         price_str = request.GET.get("price")
#         item = Product.objects.get(id=int(param_id))
#         item.name = name_str
#         item.class_obj = class_obj
#         item.price = float(price_str)
#         item.save()
#         return HttpResponse(status=201)

#     # TODO: Object not found
#     @staticmethod
#     def deleteSpecificProduct(request, param_id):
#         item = Product.objects.get(id=int(param_id))
#         item.delete()
#         return HttpResponse(status=204)    

#     @staticmethod
#     def getSpecificProduct(request, param_id):
#         item = Product.objects.get(id=int(param_id))
#         return HttpResponse(json.dumps(ProductProcessor.singleProductToDict(item)), content_type="application/json")

