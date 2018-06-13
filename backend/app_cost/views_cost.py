#coding: utf-8
import sys
from django.http import JsonResponse
import time
from enterprise.models import InventoryInformation,Order,OrderProduct,ProductMaterial,PurchaseProduct,Material
from django.core import serializers
# Create your views here.
from collections import defaultdict
import json
import simplejson
import demjson
import requests
import re
def getAllCost(req):
	print("inallCost")
	anslist = PurchaseProduct.objects.all()
	answer = defaultdict(dict)
	count = 0
	for record in anslist:
		material = record.material
		purchase = record.purchase
		parent = material.class_obj
		temp = {
			'parent_name':parent.class_field,
			'name':material.name,
			'price':record.price,
			'purchaser':purchase.purchaser,
			'supplier':purchase.supplier.name
		}
		answer.setdefault(count,temp)
		count+=1
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
	names = resp_cmt_json['materialName']
	if(names == ''):
		return getAllCost(2)
	else:
		print("~~~~"+names)
		anslist = Material.objects.filter(name = names)
		if(len(anslist) == 0):
			answer = {'res':'Sorry, the record doesn\'t exist.'}
			return JsonResponse(answer)
		materialId = anslist[0].id
		answer = defaultdict(dict)
		count = 0
		firstFilter = PurchaseProduct.objects.filter(material = materialId)
		for record in firstFilter:
			material = record.material
			purchase = record.purchase
			parent = material.class_obj
			temp = {
				'parent_name':parent.class_field,
				'name':material.name,
				'price':record.price,
				'purchaser':purchase.purchaser,
				'supplier':purchase.supplier.name
			}
			answer.setdefault(count,temp)
			count+=1
		if(len(answer) == 0):
			answer = {'res':'Sorry, the record doesn\'t exist.'}
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
	return JsonResponse(answer)

def getOrderCost(req):
	"""
	:req 前端的请求
	:return 订单的成本
	"""
	params = getParams(req)
	print("~~~~")
	print(params)
	conditions = hasQueryCondition(params)
	answer = {}
	if(conditions == False):
		answer = getAllOrderCost()
		return JsonResponse(answer)
	else:
		try:
			order_ids = []
			orders = Order.objects.all()
			for param in params:
				if(param == "indentor"):
					orders = orders.filter(indentor = params[param])
				elif(param == "orderID"):
					orders = orders.filter(id = int(params[param]))
			for order in orders:
				order_ids.append(order.id)
			count = 0
			for o in order_ids:
				print("o is ")
				print(o)
				order = orders.filter(id = o)[0]
				print(order)
				cost = getConditionOrderCost(o)
				print(cost)
				answer.setdefault(
					count,{
						'orderID':order.id,
						'cost':cost,
						'indentor':order.indentor,
						'order_price':order.totalprice
					}
				)
				count += 1
			if(len(answer) == 0):
				answer = {'res':'Sorry, the record doesn\'t exist.'}
			return JsonResponse(answer)
		except Exception as e:
			print(e)
			return JsonResponse({'res':'Sorry! order does not exist!'})


def getAllOrderCost():
	all_order = Order.objects.all()
	cost_list = defaultdict(dict)
	count = 0
	for order in all_order:
		
		single_cost = getConditionOrderCost(order.id)
		indentor = order.indentor
		order_price = order.totalprice
		single_dict = {
			'orderID':order.id,
			'cost':single_cost,
			'indentor':indentor,
			'order_price':order_price
		}
		cost_list[count] = single_dict
		count += 1
	return cost_list

def getConditionOrderCost(order_id):
	products_id = getProductsAndNumber([order_id])
	materials_id = getMaterialsAndNumber(products_id)
	print(products_id)
	print(materials_id)
	cost = 0
	for m_id in materials_id:
		p_p = PurchaseProduct.objects.filter(material_id = m_id)
		for p in p_p:
			cost += materials_id[m_id]*p.price
			print("cost %f"%p.price)
		print(cost)
	return cost
	

def getProductsAndNumber(order_ids):
	products_id = defaultdict(int)
	for o_id in order_ids:
		order_product = OrderProduct.objects.filter(order_id=o_id)
		for product in order_product:
			products_id[product.product] += product.number
	return products_id

def getMaterialsAndNumber(products_id):
	materials_id = defaultdict(int)
	for p_id in products_id:
		product_material = ProductMaterial.objects.filter(product_id = p_id)
		for p_m in product_material:
			materials_id[p_m.material_id] += p_m.number * products_id[p_id]
	return materials_id

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