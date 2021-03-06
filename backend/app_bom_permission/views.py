#coding:utf8
from django.shortcuts import render
from django.db.models import Q
from functools import reduce 
from enterprise.models import Material, MaterialClass, Product, ProductClass, ProductMaterial
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
import datetime

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
            final_Q = reduce(lambda x,y: x&y, Q_list)
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
        return HttpResponse(json.dumps(MaterialProcessor.singleMaterialToDict(m)), content_type="application/json")

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
        return HttpResponse(json.dumps(MaterialProcessor.singleMaterialToDict(item)), content_type="application/json")

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
        result = {"class_field": item.class_field, "class_id": item.id}
        if item.parent_class:
            result['parent_class_field'] = item.parent_class.class_field
            result["parent_class_id"] = item.parent_class.id
        else:
            result['parent_class_field'] = "null"
            result["parent_class_id"] = "null"
        return result

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
        result = {"name": item.name, 
                "class_id": item.class_obj.id, 
                "id": item.id,
                "price": float(item.price),
                "class_field": item.class_obj.class_field
                }
        
        return result

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
            final_Q = reduce(lambda x,y: x&y, Q_list)
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
        return HttpResponse(json.dumps(ProductProcessor.singleProductToDict(m)), content_type="application/json")

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
        return HttpResponse(json.dumps(ProductProcessor.singleProductToDict(item)), content_type="application/json")

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


    
class ProductmaterialProcessor:
    # util
    @staticmethod
    def productmaterialListToJson(result):
        ret = {"data": []}
        for item in result:
            ret["data"].append(ProductmaterialProcessor.singleProductmaterialToDict(item))
        return json.dumps(ret)

    @staticmethod
    def singleProductmaterialToDict(item):
        return {"id": item.id,
                "product_id": item.product.id,
                "product_name": item.product.name,
                "product_class_field": item.product.class_obj.class_field,
                "material_id": item.material.id,
                "material_name": item.material.name,
                "material_class_field": item.material.class_obj.class_field,
                "procedure": item.procedure,
                "number": item.number,
                "comments": item.comments
                }

    # # TODO: filter for 
    # @staticmethod
    # def getProductmaterialQ(request):
    #     name_str = request.GET.get("name")
    #     class_id_str = request.GET.get("class_id")
    #     id_str = request.GET.get("id")
    #     Q_list = []
    #     if name_str and name_str != "null":
    #         Q_list.append(Q(name=name_str))
    #     if class_id_str and class_id_str != "null":
    #         Q_list.append(Q(class_obj__id=int(class_id_str)))
    #     if name_str and id_str != "null":
    #         Q_list.append(Q(id=int(id_str)))
    #     return Q_list

    # # process all
    @staticmethod
    def processProductmaterial(request):
        if request.method == "DELETE":
            return ProductmaterialProcessor.deleteProductmaterial(request)
        if request.method == "POST":
            return ProductmaterialProcessor.createProductmaterial(request)


    @staticmethod
    def createProductmaterial(request):
        product_id = request.GET.get("product_id")
        product = Product.objects.get(id=product_id)
        material_id = request.GET.get("material_id")
        material = Material.objects.get(id=material_id)
        procedure = int(request.GET.get("procedure"))
        number = int(request.GET.get("number"))
        comments = request.GET.get("comments")
        m = ProductMaterial(product=product, 
                            material=material, 
                            procedure=procedure, 
                            number=number,
                            comments=comments
                            )
        m.save()
        return HttpResponse(json.dumps(ProductmaterialProcessor.singleProductmaterialToDict(m)), content_type="application/json")

    @staticmethod
    def deleteProductmaterial(request):
        data = json.loads(request.body.decode())["data"]
        id_list = [item["id"] for item in data]
        for i in id_list:
            m = ProductMaterial.objects.get(id=int(i))
            m.delete()
        return HttpResponse(status=204)

    @staticmethod
    def processProductmaterialForCertainProduct(request, product_id):
        if request.method == "GET":
            return ProductmaterialProcessor.filterProductmaterialForCertainProduct(request, product_id)
        # if request.method == "POST":
        #     return ProductmaterialProcessor.createProductmaterialForCertainProduct(request, product_id)

    @staticmethod
    def filterProductmaterialForCertainProduct(request, product_id):
        product = Product.objects.get(id=product_id)
        result = ProductMaterial.objects.filter(product=product)
        return HttpResponse(ProductmaterialProcessor.productmaterialListToJson(result), content_type="application/json")



    # process specific Product
    @staticmethod
    def processSpecificProductmaterial(request, param_id):
        if request.method == "PUT":
            return ProductmaterialProcessor.modifySpecificProductmaterial(request, param_id)
        if request.method == "DELETE":
            return ProductmaterialProcessor.deleteSpecificProductmaterial(request, param_id)
        if request.method == "GET":
            return ProductmaterialProcessor.getSpecificProductmaterial(request, param_id)

    # TODO: Object not found
    @staticmethod
    def modifySpecificProductmaterial(request, param_id):
        productmaterial = ProductMaterial.objects.get(id=int(param_id))
        
        material_id = request.GET.get("material_id")
        material = Material.objects.get(id=material_id)
        procedure = int(request.GET.get("procedure"))
        number = int(request.GET.get("number"))
        comments = request.GET.get("comments")
        productmaterial.material = material
        productmaterial.procedure = procedure
        productmaterial.number = number
        productmaterial.comments = comments
        productmaterial.save()
        return HttpResponse(json.dumps(ProductmaterialProcessor.singleProductmaterialToDict(productmaterial)), content_type="application/json")

    # TODO: Object not found
    @staticmethod
    def deleteSpecificProductmaterial(request, param_id):
        item = ProductMaterial.objects.get(id=int(param_id))
        item.delete()
        return HttpResponse(status=204)

    @staticmethod
    def getSpecificProductmaterial(request, param_id):
        item = ProductMaterial.objects.get(id=int(param_id))
        return HttpResponse(json.dumps(ProductmaterialProcessor.singleProductmaterialToDict(item)), content_type="application/json")

def userLogin(request):
    print(request.body)
    username = request.POST['username']
    password = request.POST['password']
    print(request.user)
    user = authenticate(request, username=username, password=password)

    status = None
    if user is not None:
        login(request, user)
        print(request.COOKIES)
        print(request.user)
        # print(user.last_login)
        # print(list(Group.objects.filter(user=user))[0].name)
        status = 200
    else:
        status = 422
    response = JsonResponse({'status': status})
    return response


def getUser(request):
    print(request.user)
    user = request.user
    if not user.is_authenticated():
        return JsonResponse({"status ": 404})
    groups = Group.objects.filter(user=user)
    g_list = []
    # print('has perm',user.has_perm('enterprise.add_supplier'))
    # tmp = Supplier(id=3,name="testSupplier",contact="Nothing",phonenumber="11111111",address="NKU")
    # tmp.save()
    for g in groups:
        g_list.append(g.name)
    if request.user.is_authenticated():
        print("authenticated~")
        return JsonResponse({"status": 200,
                             "username": user.username,
                             "firstname": user.first_name,
                             "lastname":  user.last_name,
                             "email": user.email,
                             "lastlogin": user.last_login,
                             "groups": g_list,
                             "datejoined":user.date_joined
                             })
    else:
        return JsonResponse({"status ": 404})


def changePassword(request):
    print(request.user)
    userName = request.POST['username']
    oldPassword = request.POST['oldpassword']
    newPassword = request.POST['newpassword']
    user = authenticate(username=userName, password=oldPassword)
    if user is not None:
        user.set_password(newPassword)
        user.save()
        return JsonResponse({'status': 200})
    else:
        return JsonResponse({'status': 400, 'detail': "原密码错误"})


def changeInfo(request):
    user = User.objects.get(username=request.POST['username'])
    user.email = request.POST['newemail']
    user.last_name = request.POST['newlastname']
    user.first_name = request.POST['newfirstname']
    user.save()
    print(request.user)
    return JsonResponse({'status': 200})


def userLogout(request):
    user = request.user
    if user.is_authenticated():
        logout(request)
        return JsonResponse({"status":200,"detail":"登出成功"})    
    else:
        return JsonResponse({"status":404,"detail":"未登录"})

# def change_names(request):
#     user = User.objects.get(username=request.POST['username'])
#     user.last_name = request.POST['newlastname']
#     user.first_name = request.POST['newfirstname']
#     user.save()
#     print(request.user)
#     return JsonResponse({'status': 200})
