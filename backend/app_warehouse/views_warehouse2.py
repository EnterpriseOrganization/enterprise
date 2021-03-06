﻿
# from django.shortcuts import render
from django.http import JsonResponse
import time
from enterprise.models import InventoryInformation,Material,MaterialClass
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
	"""
	:req 前端发起的请求
	:return 查询的结果，json格式
	"""
	params = getParams(req)
	user = req.user
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
			InventoryInformation.objects.create( material = material,\
			                                     shelfnumber = params['shelfnumber'], \
			                                     number = params['number'],\
			                                     threshold = params['threshold'],\
			                                     newestinwarehousedate = time.localtime() )
		return JsonResponse({'res':'add success!'})		
	else:
		response = JsonResponse({'res':'Sorry! You don\'t have the permission to do this operation!'})
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
		try:
			material = Material.objects.get(name = params['material'])
		except:
			return JsonResponse({'res':'Sorry! The material does not exist!'})
		try:
			inventory = InventoryInformation.objects.get(material=material)
			if(inventory.number < int(params['number'])):
				return JsonResponse({'res':'Sorry, the material is not enough to reduce.'})
			inventory.number -= int(params['number'])
			inventory.save()
		except:
			return JsonResponse({'res':'Sorry! The material does not exist!'})
		return JsonResponse({'res':'remove success!'})
	else:
		return JsonResponse({'res':'Sorry!Permission denied!'})

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
		for i in list(params.keys()):
			if params[i]=='':
				params.pop(i)
		print(params)
		return params
	elif(req.method == 'DELETE'):
		params = json.loads(req.body.decode('utf-8'))
		return params

def hasQueryCondition(queryset):
	"""
	:queryset 前端向后端发起的请求参数
	:return bool变量，确认是否有查询条件
	"""
	for i in queryset:
		if(i != ''):
			return True
	return False

def getInventoryByConditions(params):
	"""
	:params 查询条件列表
	:return 查询结果字典
	"""
	params_list = ['id','material','shelfnumber','number','threshold','newestinwarehousedate']
	old_query_answer = None
	if('material' in list(params.keys())):
		query_material = Material.objects.filter(name = params['material'])
		old_query_answer = InventoryInformation.objects.filter(material = query_material)
	else:
		old_query_answer = InventoryInformation.objects.all()
	for i in list(params.keys()):
		if(i == 'shelfnumber'):
			query_answer = old_query_answer.filter(shelfnumber = params[i])
		elif(i == 'id'):
			query_answer = old_query_answer.filter(id = params[i])
		elif(i == 'threhold'):
			query_answer = old_query_answer.filter(threshold = params[i])
		elif(i == 'newestinwarehousedate'):
			query_answer = old_query_answer.filter(newestinwarehousedate = params[i])
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
	print(answer)
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