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
	anslist = InventoryInformation.objects.all()
	answer = defaultdict(dict)
	count = 0
	for record in anslist:
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
	return JsonResponse(answer)
@ensure_csrf_cookie
def addInventory(req):
	params = getParams(req)
	print(params)
	InventoryInformation.objects.create( material = params['material'], name =\
	                                     params['name'], shelfnumber = params['shelfnumber'], number =\
	                                     params['number'], newestinwarehousedate = time.localtime() )
	return JsonResponse({'res':'add success!'})

def modifyInventory(req):
	params = getParams(req)
	InventoryInformation.objects.filter()
	return JsonResponse({'res':'modify success!'})

def removeRecord(req):
	return JsonResponse({'res':'remove success!'})



def getParams(req):
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
	