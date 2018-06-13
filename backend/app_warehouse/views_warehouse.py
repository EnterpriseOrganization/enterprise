
# from django.shortcuts import render
from django.http import JsonResponse
import time
from enterprise.models import InventoryInformation,Material,MaterialClass,InWarehouse,InwareHouseProduct,OutWarehouse,OutProduct
from django.core import serializers
from django.views.decorators.csrf	 import csrf_exempt
# Create your views here.
from collections import defaultdict
import json
def getInventory(req):
    """
    :req 前端发起的请求
    :return 查询结果
    """
    queryset = getParams(req)
    #print(req)
    has_query_condition = hasQueryCondition(queryset)
    answer = {}
    if(has_query_condition):
        answer = getInventoryByConditions(queryset)
    else:
        answer = getAllInventory()
    if(len(answer) == 0):
        answer = {'res':'Sorry, the record doesn\'t exist.'}
    return JsonResponse(answer)

@csrf_exempt
def addInventory(req):
    """
    :req 前端发起的请求
    :return 查询的结果，json格式
    """
    params = getParams(req)
    print("")
    user = req.user
    if(user.has_perm("add_InventoryInformation")):
        in_warehouse = InWarehouse.objects.create(indate=params['record_info']['indate'],checker=params['record_info']['checker'],operator=params['record_info']['operator'])
        for m_f in params['material_info']:
            try:
                material = Material.objects.get(name = m_f['material']) 
                inventory = InventoryInformation.objects.get(material = material)
                inventory.number += int(m_f['number'])
                inventory.save()
            except: # 如果这种原料不存在，则报错
                Material.objects.create(name=m_f['material'])
                material = Material.objects.get(name=m_f['material'])
                InventoryInformation.objects.create(material=material,number=int(m_f['number']),shelfnumber=m_f['shelfnumber'],threshold=100,newestinwarehousedate=params['record_info']['indate'])
            InwareHouseProduct.objects.create(number=int(m_f['number']),inwarehouse = in_warehouse,material=material)
        return JsonResponse({'result':1})		
    else:
        print("permission denied")
        response = JsonResponse({'result':2})
        return response
    
def modifyInventory(req):
    """
    :req 前端发起的请求
    :return 更新的结果
    """
    params = getParams(req)
    user = req.user
    if(user.has_perm('modify_InventoryInformation')):
        material = Material.objects.get(name = params['material'])
        inventory = InventoryInformation.objects.filter(material = material)
        for param in params:
            if(param == 'shelfnumber'):
                inventory.update(shelfnumber = params[param])
            elif(param == 'number'):
                inventory.update(number = params[param])
            elif(param == 'newestinwarehousedate'):
                inventory.update(newestinwarehousedate = params[param])
        return JsonResponse({'res':'modify success!'})
    else:
        return JsonResponse({'res':'Sorry! Permission denied!'})

def removeRecord(req):
    """
    :req 前端的请求
    :return 删除的结果
    """
    params = getParams(req)
    user = req.user
    if(user.has_perm('delete_InventoryInformation')):
        out_warehouse = OutWarehouse.objects.create(outdate=params['record_info']['outdate'],receiver=params['record_info']['receiver'],checker=params['record_info']['checker'])
        for m_f in params['material_info']:
            try:
                material = Material.objects.get(name = m_f['material'])
                print(material.id)
                inventory = InventoryInformation.objects.get(material = material)
                if(inventory.number < int(m_f['number'])):
                    return JsonResponse({'res':'Sorry, the material is not enough to reduce.'})
                inventory.number -= int(m_f['number'])
                inventory.save()
            except: # 如果这种原料不存在，则报错
                return JsonResponse({'res':"Sorry! The material does not exist!"})
            OutProduct.objects.create(number=int(m_f['number']),outwarehouse = out_warehouse,material=material)
        return JsonResponse({'res':'add out warehouse success!'})
    else:
        return JsonResponse({'res':'Sorry!Permission denied!'})

def getParams(req):
    """
    :req 前端请求体
    :return 请求体所带的参数字典
    """
    answer = {}
    params = None
    if(req.method == 'GET'):
        params = dict(req.GET)
    elif(req.method == 'POST'):
        params = json.loads(req.body.decode('utf-8'))
    elif(req.method == 'DELETE'):
        params = json.loads(req.body.decode('utf-8'))
    for param in params:
        if(params[param]!=''):
            answer.setdefault(param,params[param])
    return answer

def hasQueryCondition(queryset):
    """
    :queryset 前端向后端发起的请求参数
    :return bool变量，确认是否有查询条件
    """
    for i in queryset:
        if(queryset[i] != ''):
            return True
    return False

def getInventoryByConditions(params):
    """
    :params 查询条件列表
    :return 查询结果字典
    """
    query_answer = {}
    old_query_answer = {}
    print(params)
    params_list = ['material','shelfnumber','number','threshold','newestinwarehousedate']
    if('material' in list(params.keys())):
        query_material = Material.objects.filter(name = params['material'])
        old_query_answer = InventoryInformation.objects.filter(material = query_material)
    else:
        old_query_answer = InventoryInformation.objects.all()
    for i in list(params.keys()):
        if(i == 'shelfnumber'):
            query_answer = old_query_answer.filter(shelfnumber = params[i])
        elif(i == 'number'):
            query_answer = old_query_answer.filter(number = params[i])
        elif(i == 'threhold'):
            query_answer = old_query_answer.filter(threshold = params[i])
        elif(i == 'newestinwarehousedate'):
            query_answer = old_query_answer.filter(newestinwarehousedate = params[i])
        elif(i == 'material'):
            query_answer = old_query_answer
        old_query_answer = query_answer
    answer = toDict(old_query_answer)
    print(answer)
    return answer

def getAllInventory():
    """
    :return 查询结果字典
    """
    answer_list = InventoryInformation.objects.all()
    answer = toDict(answer_list)
    return answer

def toDict(queryset):
    """
    :queryset 查询之后的queryset的结果
    :return 将queryset转换成纯json格式的dict字典
    """
    answer = defaultdict(dict)
    count = 0
    for record in queryset:
        material = record.material
        temp = {
            'id':material.id,
            'name':material.name,
            'shelfnumber':record.shelfnumber,
            'number':record.number,
            'newestinwarehousedate':record.newestinwarehousedate
        }
        answer.setdefault(count,temp)
        count+=1
    return answer

def getInWarehouseRecord(req):
    params = getParams(req)
    query_material = None
    if('material' in list(params.keys())):
        try:
            query_material = Material.objects.get(name = params['material'])
        except:
            return JsonRepsonse({"res":"the material has no in warehouse record!"})
    in_warehouse = InWarehouse.objects.all()
    for param in list(params.keys()):
        if(param == 'operator' and params[param] != ""):
            in_warehouse = in_warehouse.filter(operator=params[param])
        elif(param=="checker" and params[param] != ""):
            in_warehouse = in_warehouse.filter(checker=params[param])

    answer = {}
    count = 0
    for i_w in in_warehouse:
        print(i_w.operator)
        in_warehouse_product = InwareHouseProduct.objects.filter(inwarehouse=i_w)
        if(query_material != None):
            in_warehouse_product = in_warehouse_product.filter(material=query_material)
        for i_w_m in in_warehouse_product:
            answer.setdefault(
                count,{
                    'in_or_out':'入库',
                    'id':i_w_m.material.id,
                    'name':i_w_m.material.name,
                    'number':i_w_m.number,
                    'checker':i_w.checker,
                    'time':i_w.indate
                }
            )
            count += 1
    print(answer)
    return JsonResponse(answer)

def getOutWarehouseRecord(req):
    params = getParams(req)
    query_material = None
    if('material' in list(params.keys())):
        try:
            query_material = Material.objects.get(name = params['material'])
        except:
            return JsonRepsonse({"res":"the material has no out warehouse record!"})
    out_warehouse = OutWarehouse.objects.all()
    for param in list(params.keys()):
        if(param == 'operator' and params[param] != ""):
            out_warehouse = out_warehouse.filter(receiver=params[param])
        elif(param=="checker" and params[param] != ""):
            out_warehouse = out_warehouse.filter(checker=params[param])
    answer = {}
    count = 0
    for o_w in out_warehouse:
        out_warehouse_product = OutProduct.objects.filter(outwarehouse=o_w)
        if(query_material != None):
            out_warehouse_product = out_warehouse_product.filter(material=query_material)
        for o_w_m in out_warehouse_product:
            answer.setdefault(
                count,{
                    'in_or_out':'出库',
                    'id':o_w_m.material.id,
                    'name':o_w_m.material.name,
                    'number':o_w_m.number,
                    'checker':o_w.checker,
                    'time':o_w.outdate
                }
            )
            count += 1
    return JsonResponse(answer)