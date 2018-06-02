from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
from django.http import JsonResponse
from enterprise.models import UserTable
from enterprise.models import Purchase
from enterprise.models import PurchaseProduct
from enterprise.models import InventorInformation
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
	return list
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
	条件查询
	"""
	if request.method == 'POST':
		params = request.POST
		# 得到所有参数
		quotation_id = params.get('quotation_id')
		material_name = params.get('material_name')
		supplier_name = params.get('supplier_name')
		where_args = {}
		# 都有什么条件
		if quotation_id:
			where_args['id'] = quotation_id
		if supplier_name:
			where_args['supplier__name'] = supplier_name
		if material_name:
			where_args['material__name'] = material_name

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
	更新物料报价信息, 传入报价编号和准备修改的名字
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
		else:
			return JsonResponse({'msg': 'Incomplete parameters'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def get_lack_list(request):
	"""
	获取所有缺料记录
	return list
	"""
	if request.method == 'POST':
		inifs = InventorInformation.objects.select_related('material').filter(number__lt=F('threshold'))
		result = []
		for inif in inifs:
			res = {
				'id': inif.id,
				'material_id':inif.material.id,
				'material_name': inif.material.name,
				'number': inif.number,
				'threshold':inif.threshold
			}
			result.append(res)

		return JsonResponse({'msg': 200, 'result': result})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def add_purchase(request):
	"""
	新增购买记录(填写采购单)
	传入参数：采购人,审核人,采购商品列表字典items(matreial_id,num,price,supplier_id)
	"""
	if request.method == 'POST':
		params = request.POST
		purchaser_id = params.get('purchaser')
		checker_id = params.get('checker')
		supplier_id = params.get('supplier')
		items = params.get('items')
		return JsonResponse({'msg': 'sorry'})
		if purchaser_id and checker_id and items:
			# 计算总价
			total_price = 0
			items_dict = json.loads(items)
			price = int(items_dict['price'])
			total_price += price
			try:
				purchaser = Purchase.objects.get(id=purchaser_id)
				checker = UserTable.objects.get(id=checker_id)
				supplier = Purchase.objects.get(id=supplier_id)
			except UserTable.DoesNotExist:
				return JsonResponse({'msg': 'this checker does not exist'})
			except Purchase.DoesNotExist:
				return JsonResponse({'msg': 'this purchaser does not exist'})
			except Supplier.DoesNotExist:
				return JsonResponse({'msg': 'this supplier does not exist'})
			purchase = Purchase(purchaser=purchaser, checker=checker, supplier=supplier, totalprice=total_price)
			try:
				purchase.save()
			except IntegrityError:
				return JsonResponse({'msg': ' primary key error'})

			# 这里有问题，应该先转成列表，再判断字典
			for item in items_dict:
				matreial_id = items_dict[item]
				num = items_dict[item]
				price = item.price

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
	"""
	if request.method == 'POST':
		purchases = Purchase.objects.select_related('supplier').all()
		result = []
		for purchase in purchases:
			res = {
				'id': purchase.id,
				'date':purchase.date,
				'checker': purchase.checker,
				'supplier_name': purchase.supplier.name
			}
			result.append(res)

		return JsonResponse({'msg': 200, 'result': result})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def get_purchase_detail(request):
	"""
	"""
	if request.method == 'POST':
		return JsonResponse({'msg': 200, 'result': 'ok'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def purchase_query(request):
	"""
	"""
	if request.method == 'POST':

		return JsonResponse({'msg': 200, 'result': 'ok'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})
