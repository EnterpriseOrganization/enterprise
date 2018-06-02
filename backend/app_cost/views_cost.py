#coding: utf-8
import sys
from django.http import JsonResponse
import time
from enterprise.models import *
from enterprise.DataScript import generateProduct
from django.http import JsonResponse, HttpResponse
from django.core import serializers
# Create your views here.
from collections import defaultdict
import json
import simplejson
import demjson
import requests
import re
def getAllCost(req):
	anslist = Product.objects.all()
	answer = defaultdict(dict)
	count = 0
	for record in anslist:
		categories = record.class_obj
		temp = {
			'category':categories.class_field,
			'name':record.name,
		    'price':record.price,
		}
		answer.setdefault(count,temp)
		count+=1
	print(count)
	return JsonResponse(answer)

def newProduct(req):
    data = req.body.decode("utf8")
    resp_cmt_json = json.loads(req.body.decode("utf8"))
    name = resp_cmt_json['name']
    price = resp_cmt_json['price']
    class_obj_id = 1
    Product.objects.create(name = name, price = price, class_obj_id = class_obj_id)
    return JsonResponse({'success': '1'})
    
def getCostByName(req):
    resp_cmt_json = json.loads(req.body.decode("utf8"))
    names = resp_cmt_json['name']
    anslist = Product.objects.filter(name = names)
    answer = defaultdict(dict)
    count = 0
    for record in anslist:
        categories = record.class_obj
        temp = {
            'category':categories.class_field,
            'name':record.name,
            'price':record.price,
        }
        answer.setdefault(count,temp)
        count+=1
    print(count)
    return JsonResponse(answer)

def getCostByMaterialID(req):
    resp_cmt_json = json.loads(req.body.decode("utf8"))
    ID = resp_cmt_json['MaterialID']
    anslist = Product.objects.filter(materialID = ID)
    answer = defaultdict(dict)
    count = 0
    for record in anslist:
        material = record.materialID
        temp = {
            'name':material.name,
            'price':record.price,
        }
        answer.setdefault(count,temp)
        count+=1
    print(count)
    return JsonResponse(answer)