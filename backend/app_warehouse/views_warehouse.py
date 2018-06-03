
# from django.shortcuts import render
from django.http import JsonResponse
import time
from enterprise.models import InventoryInformation
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
	params = getParams(req)
	user = req.user
	print("user is ",user)
	print(user.has_perm("add_InventoryInformation"))
	#print(params)
	if(user.has_perm("add_InventoryInformation")):
		
		try:
			material = Material.objects.get(name = params['material']) 
		except: # 如果这种原料不存在，则报错
			return JsonResponse({'res':'Sorry! material does not exist!'})
		try:
			inventory = InventoryInformation.objects.get(material = material)
			inventory.number += int(params['number'])
			inventory.save()
		except: # 如果这种库存不存在，那么就创建它
			InventoryInformation.objects.create( material = material, name =\
			                             params['name'], shelfnumber = params['shelfnumber'], number =\
			                             params['number'], newestinwarehousedate = time.localtime() )
		return JsonResponse({'res':'add success!'})		
	else:
		print("return from false")
		response = JsonResponse({'res':'Sorry! You don\'t have the permission to do this operation!'})
		print(response.content)
		return response
	
def modifyInventory(req):
	params = getParams(req)
	material = material.objects.get(id = params['material'])
	inventory = InventoryInformation.objects.filter(material = material)
	for param in params:
		if(param == 'shelfnumber'):
			inventory.shelfnumber = params[param]
		elif(param == 'number'):
			inventory.number = params[param]
		elif(param == 'newestinwarehousedate'):
			inventory.newestinwarehousedate = params[param]
	inventory.save()
	return JsonResponse({'res':'modify success!'})

#TODO:待完成移除库存操作
def removeRecord(req):
	
	return JsonResponse({'res':'remove success!'})

def getParams(req):
	"""
	:req 前端请求体
	:return 请求体所带的参数字典
	"""
	if(req.method == 'GET'):
		params = dict(req.GET)
		return params
	elif(req.method == 'POST'):
		params = json.loads(req.body.decode('utf-8'))
		return params
	elif(req.method == 'DELETE'):
		print("in delete")
		params = json.loads(req.body.decode('utf-8'))
		print(params)
		return params



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
	params_list = ['material','shelfnumber','number','threshold','newestinwarehousedate']

	old_query_answer = None
	if('material' in list(params.keys())):
		query_material = Material.objects.filter(id = params['material'][id])
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
		old_query_answer = query_answer
	answer = toDict(old_query_answer)
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
	for record in anslist:
		material = record.material
		#print("material is ", material.name)
		temp = {
			'id':material.id,
			'name':material.name,
		        'shelfnumber':record.shelfnumber,
		        'number':record.number,
		        'newestinwarehousedate':record.newestinwarehousedate
		}
		answer.setdefault(count,temp)
		count+=1
	return JsonResponse(answer)

def addInventor(req):
	return JsonResponse({'res':'add success!'})

def modifyInventor(req):

	return JsonResponse({'res':'modify success!'})

def removeRecord(req):
	return JsonResponse({'res':'remove success!'})