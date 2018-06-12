from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
from django.http import JsonResponse
from enterprise.models import UserTable
from django.db.models import Max
from enterprise.models import Purchase
from enterprise.models import PurchaseProduct
from enterprise.models import InventoryInformation
from enterprise.models import Material
from enterprise.models import Supplier
from enterprise.models import SupplierMaterial
from django.db.models import Q
from django.db.models import F
import json


@method_decorator(csrf_exempt)
def get_quotation_list(request):
	"""
	获取所有报价记录
	:param request:
	:return: list[{}{}..]
	"""
	if request.method == 'POST':
		sms = SupplierMaterial.objects.select_related('supplier', 'material').all()
		# attributes = SupplierMaterial._meta.get_fields()
		result = []
		for sm in sms:
			res = {
				'id': sm.id,
				'material_name': sm.material.name,
				'price': sm.price,
				'supplier_name':sm.supplier.name,
			}
			result.append(res)

		return JsonResponse({'msg': 200, 'result': result})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def add_quotation(request):
	"""
	增加供应商报价信息
	:param request:(material_id, supplier_id, price)
	:return: 200 or error message
	"""
	if request.method == 'POST':
		params = request.POST
		# 得到所有参数
		material_id = params.get('material_id')
		supplier_id = params.get('supplier_id')
		price = params.get('price')
		# 只有所有参数都收到且不为空
		if material_id and supplier_id and price:
			try:
				sp = Supplier.objects.get(id=supplier_id)
				mt = Material.objects.get(id=material_id)
			except Supplier.DoesNotExist:
				return JsonResponse({'msg': 'there is doesn`t have this supplier'})
			except Material.DoesNotExist:
				# 捕获找不到对象异常
				return JsonResponse({'msg': 'there is doesn`t have this material'})

			sm = SupplierMaterial(price=price, material=mt, supplier=sp)
			try:
				sm.save()
				return JsonResponse({'msg': 200, 'result': 'success'})
			except IntegrityError:
				# 捕获主键唯一冲突异常
				return JsonResponse({'msg': 'this supplier has already bid'})
		else:
			return JsonResponse({'msg': 'Incomplete parameters'})
	else:
		return JsonResponse({'msg': 'Please use POST'})


@method_decorator(csrf_exempt)
def delete_quotation(request):
	"""
	删除某一条供应商报价
	:param request: quotation_id
	:return: 200 or error message
	"""
	if request.method == 'POST':
		params = request.POST
		# 得到所有参数
		quotation_id = params.get('quotation_id')
		# 判断参数是否存在
		if quotation_id:
			try:
				sm = SupplierMaterial.objects.get(id=quotation_id)
			except SupplierMaterial.DoesNotExist:
				# 捕获get不到的异常
				return JsonResponse({'msg': 'this quotation does not exist'})
			# normal
			sm.delete()
			return JsonResponse({'msg': 200, 'result': 'success'})
		else:
			return JsonResponse({'msg': 'Incomplete parameters'})
	else:
		return JsonResponse({'msg': 'Please use POST'})


@method_decorator(csrf_exempt)
def quotation_query(request):
	"""
	条件查询物料报价
	:param request:
	:return:
	"""
	if request.method == 'POST':
		params = request.POST
		# 得到所有参数
		material_id = params.get('material_id')
		material_name = params.get('material_name')
		supplier_name = params.get('supplier_name')
		where_args = {}
		# 都有什么条件
		if material_id:
			where_args['material__id'] = material_id
		if supplier_name:
			where_args['supplier__name'] = supplier_name
		if material_name:
			where_args['material__name'] = material_name
		print(where_args)
		sms = SupplierMaterial.objects.select_related('supplier', 'material').filter(**where_args)
		result = []
		for sm in sms:
			res = {
				'id': sm.id,
				'material_name': sm.material.name,
				'price': sm.price,
				'supplier_name': sm.supplier.name,
			}
			result.append(res)

		return JsonResponse({'msg': 200, 'result': result})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def update_quotation_price(request):
	"""
	更新物料报价信息, 传入报价编号和准备修改的名字
	"""
	if request.method == 'POST':
		params = request.POST
		# 得到所有参数
		quotation_id = params.get('quotation_id')
		price = params.get('new_price')
		# 判断是否参数完整
		if quotation_id and price:
			try:
				sm = SupplierMaterial.objects.get(id=quotation_id)
			except SupplierMaterial.DoesNotExist:
				return JsonResponse({'msg': 'this quotation does not exist'})
			sm.price = price
			sm.save()
			return JsonResponse({'msg': 200, 'result': 'ok'})
		else:
			return JsonResponse({'msg': 'update failed, Incomplete parameters'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def add_supplier(request):
	"""
	新增提供商
	"""
	if request.method == 'POST':
		params = request.POST
		# 得到所有参数
		supplier_name = params.get('supplier_name')
		supplier_phone = params.get('supplier_phone')
		supplier_address = params.get('supplier_address')
		if supplier_address and supplier_name and supplier_phone:
			sp = Supplier(name=supplier_name, contact='no', phonenumber=supplier_phone, address=supplier_address)
			sp.save()
			return JsonResponse({'msg': 200})
		else:
			return JsonResponse({'msg': 'Incomplete parameters'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


def get_lack_list(request):
	"""
	获取所有缺料记录
	:param request:
	:return: list[{}{}{}]
	"""
	if request.method == 'POST':
		inifs = InventoryInformation.objects.select_related('material').filter(number__lt=F('threshold'))
		result = []
		for inif in inifs:
			res = {
				'id': inif.id,
				'material_id': inif.material.id,
				'material_name': inif.material.name,
				'number': inif.number,
				'threshold': inif.threshold
			}
			result.append(res)

		return JsonResponse({'msg': 200, 'result': result})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def lack_list_query(request):
	"""
	条件查询缺料列表
	:param request: （订单编号,物料编号,日期,采购人(字符串)）
	:return: list[{}{}{}]
	"""
	if request.method == 'POST':
		params = request.POST
		# 得到所有参数
		material_id = params.get('material_id')
		material_name = params.get('material_name')
		# 都有什么条件
		q1 = Q()
		q1.connector = 'AND'
		if material_id:
			q1.children.append(('material_id', material_id))
		if material_name:
			q1.children.append(('material__name', material_name))
		lacks = InventoryInformation.objects.select_related('material').filter(Q(number__lt=F('threshold')), q1)
		lacks.filter()
		result = []
		for lack in lacks:
			res = {
				'id': lack.id,
				'material_id': lack.material.id,
				'material_name': lack.material.name,
				'number': lack.number,
				'threshold': lack.threshold
			}
			result.append(res)

		return JsonResponse({'msg': 200, 'result': result})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


def get_min_price(material_id):
	"""
	从供应商报价中找到最小的
	:param material_id:
	:return:min price
	"""
	try:
		mt = Material.objects.get(id=material_id)
	except Material.DoesNotExist:
		return 'this Material does not exist'
	price = SupplierMaterial.objects.filter(material=mt).aggregate(Max('price'))
	return price


@method_decorator(csrf_exempt)
def add_purchase(request):
	"""
	新增购买记录(填写采购单)
	:param: 采购人,审核人,采购商品列表字典items(matreial_id,num,supplier_id)
	:return: 200 or error message
	"""

	if request.method == 'POST':
		params = request.POST
		purchaser = params.get('purchaser')
		checker = params.get('checker')
		supplier_id = params.get('supplier')
		items = params.get('items')
		if purchaser and checker and items and supplier_id:
			# 计算总价
			total_price = 0
			# 先转成列表，再判断字典
			items = list(items)
			for item in items:
				item_dict = dict(item)
				material_id = int(item_dict['material_id'])
				price = get_min_price(material_id)
				total_price += price
			# insert into db
			purchase = Purchase(purchaser=purchaser, checker=checker, supplier=supplier_id, totalprice=total_price)
			try:
				purchase.save()
			except IntegrityError:
				return JsonResponse({'msg': ' primary key error'})

			for item in items:
				item_dict = dict(item)
				matreial_id = item_dict['material_id']
				num = item_dict['num']
				price = get_min_price(material_id)

				if supplier_id and matreial_id and num and price:
					try:
						matreial = Material.objects.get(id=matreial_id)
						purchase_item = PurchaseProduct(purchase=purchase, matreial=matreial, num=num, price=price)
						purchase_item.save()
						return JsonResponse({'msg': 200, 'result': 'success'})
					except IntegrityError:		# 捕获主键唯一冲突异常
						return JsonResponse({'msg': ' primary key error'})
					except Material.DoesNotExist:		# 捕获get异常
						return JsonResponse({'msg': 'this Material does not exist'})
					except Supplier.DoesNotExist:
						return JsonResponse({'msg': 'this Supplier does not exist'})

				else:
					return JsonResponse({'msg': 'Incomplete parameters'})

		return JsonResponse({'msg': 200, 'result': 'ok'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def delete_purchases(request):
	"""
	批量删除采购记录
	:param request:(id1,id2,id3)以逗号分割的字符串
	:return: 200 or error message
	"""
	if request.method == 'POST':
		ids = request.POST.get('ids')
		if ids:
			ids = ids.split(',')

		q = Q()
		q.connector = 'OR'
		for id in ids:
			q.children.append(('id', id))
		Purchase.objects.filter(q).delete()
		return JsonResponse({'msg': 200, 'result': 'ok'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def get_purchase_list(request):
	"""
	获取采购单列表
	:param request:
	:return: list[{},{}]
	"""
	if request.method == 'POST':
		purchases = Purchase.objects.select_related('supplier').all()
		result = []
		for purchase in purchases:
			res = {
				'id': purchase.id,
				'date':purchase.date,
				'checker': purchase.checker,
				'supplier_name': purchase.supplier.name,
				'totalprice': purchase.totalprice,
				'purchaser': purchase.purchaser
			}
			result.append(res)

		return JsonResponse({'msg': 200, 'result': result})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def get_purchase_detail(request):
	"""
	获取采购单详细信息
	:param request: purchase_id
	:return:
	"""
	if request.method == 'POST':
		purchase_id = request.POST.get('purchase_id')
		if purchase_id:
			try:
				purchase = Purchase.objects.select_related('supplier').get(id=purchase_id)
				purchase_products = PurchaseProduct.objects.select_related('material').filter(purchase=purchase)
				res = {
					'id': purchase.id,
					'date': purchase.date,
					'checker': purchase.checker,
					'supplier_name': purchase.supplier.name,
					'totalprice': purchase.totalprice,
					'purchaser':purchase.purchaser
				}
				for purchase_product in purchase_products:
					res['material_id'] = purchase_product.material.id
					res['material_name'] = purchase_product.material.name
					res['number'] = purchase_product.number
					res['price'] = purchase_product.price

				return JsonResponse({'msg': 200, 'result': res})
			except IntegrityError:
				return JsonResponse({'msg': 'this purchase is not fount'})
		else:
			return JsonResponse({'msg': 'Incomplete parameters'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def purchase_query(request):
	"""
	条件查询采购单
	:param request:（订单编号,日期,采购人(字符串)）
	:return: list[{}{}]
	"""
	if request.method == 'POST':
		params = request.POST
		# 得到所有参数
		purchase_id = params.get('purchase_id')
		purchaser = params.get('purchaser')
		date = params.get('date')
		where_args = {}
		# 都有什么条件
		if purchase_id:
			where_args['id'] = purchase_id
		if purchaser:
			where_args['purchaser'] = purchaser
		if date:
			where_args['date'] = date
		print(where_args)
		purchases = Purchase.objects.select_related('supplier').filter(**where_args)
		result = []
		for purchase in purchases:
			for purchase in purchases:
				res = {
					'id': purchase.id,
					'date': purchase.date,
					'checker': purchase.checker,
					'supplier_name': purchase.supplier.name,
					'totalprice': purchase.totalprice,
					'purchaser':purchase.purchaser
				}
				result.append(res)

		return JsonResponse({'msg': 200, 'result': result})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def get_suppliers(request):
	"""
	获取提供商列表
	:param request:
	:return:list[{id: ,name: }{}]
	"""
	if request.method == 'POST':
		suppliers = Supplier.objects.values('id', 'name')
		suppliers_list = list(suppliers)
		return JsonResponse({'msg': 200, 'result': suppliers_list})
	else:
		return JsonResponse({'msg': 'Please use POST'})


@method_decorator(csrf_exempt)
def get_materials(request):
	"""
	获取物料列表
	:param request:
	:return:list[{id: ,name: }{}]
	"""
	if request.method == 'POST':
		materials = Material.objects.values('id', 'name')
		materials_list = list(materials)
		return JsonResponse({'msg': 200, 'result': materials_list})
	else:
		return JsonResponse({'msg': 'Please use POST'})
