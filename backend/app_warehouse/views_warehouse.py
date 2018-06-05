# from django.shortcuts import render
import sys
from django.http import JsonResponse
import time
from enterprise.models import *
from enterprise.DataScript import generateInventorInformation
from django.core import serializers
# Create your views here.
from collections import defaultdict
def getInventor(req):
	anslist = InventorInformation.objects.all()
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