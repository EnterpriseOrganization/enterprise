# from django.shortcuts import render
import sys
from django.http import JsonResponse
import time
from enterprise.models import *
from enterprise.DataScript import generateInventorInformation
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.
from collections import defaultdict
import json
def getInventory(req):
	queryset = getParams(req)
	has_query_condition = hasQueryCondition(queryset)
	answer = {}
	if(has_query_condition):
		answer = getInventoryByConditions(queryset)
	else:
		answer = getAllInventory(queryset)
	return JsonResponse(answer)
def hasQueryCondition(queryset):
	"""
	:queryset ǰ�����˷�����������
	:return bool������ȷ���Ƿ��в�ѯ����
	"""
	for i in queryset:
		if(queryset[i] != ''):
			return True
	return False
def getInventoryByConditions(params):
	"""
	:params ��ѯ�����б�
	:return ��ѯ����ֵ�
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
	:return ��ѯ����ֵ�
	"""
	answer_list = InventoryInformation.objects.all()
	answer = toDict(answer_list)
	return answer

def toDict(queryset):
	"""
	:queryset ��ѯ֮���queryset�Ľ��
	:return ��querysetת���ɴ�json��ʽ��dict�ֵ�
	"""
	answer = defaultdict(dict)
	count = 0
	for record in answer_list:
		material = record.material
		temp = {
		        'name':material.name,
		        'shelfnumber':record.shelfnumber,
		        'number':record.number,
		        'newestinwarehousedate':record.newestinwarehousedate
		}
		answer.setdefault(count,temp)
		count+=1	
	return answer
#TODO �������ӿ�����
@ensure_csrf_cookie
def addInventory(req):
	params = getParams(req)
	print(params)
	InventoryInformation.objects.create( material = params['material'], name =\
	                                     params['name'], shelfnumber = params['shelfnumber'], number =\
	                                     params['number'], newestinwarehousedate = time.localtime() )
	return JsonResponse({'res':'add success!'})

#TODO ����ɸ��Ŀ�����
def modifyInventory(req):
	params = getParams(req)
	InventoryInformation.objects.filter()
	return JsonResponse({'res':'modify success!'})

#TODO:������Ƴ�������
def removeRecord(req):
	return JsonResponse({'res':'remove success!'})

def getParams(req):
	"""
	:req ǰ��������
	:return �����������Ĳ����ֵ�
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
	