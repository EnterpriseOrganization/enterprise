from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
from django.db.utils import Error
from django.http import JsonResponse
from enterprise.models import Purchase
from enterprise.models import InventorInformation
from enterprise.models import Material
from enterprise.models import Supplier
from enterprise.models import SupplierMaterial
import datetime


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

			sm = SupplierMaterial(price=price, material=mt[0], supplier=sp[0])
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
		# attributes = SupplierMaterial._meta.get_fields()
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
		inifs = InventorInformation.objects.select_related('material').all()
		result = []
		for inif in inifs:
			# 返回当前数量低于阈值的
			if inif.threshold <= inif.number:
				continue
			res = {
				'id': inif.id,
				'material_id':inif.material.id,
				'material_name': inif.material.name,
				'number': inif.number
			}
			result.append(res)

		return JsonResponse({'msg': 200, 'result': result})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def add_purchase(request):
	"""
	"""
	if request.method == 'POST':
		return JsonResponse({'msg': 200, 'result': 'ok'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def delete_purchases(request):
	"""
	"""
	if request.method == 'POST':
		return JsonResponse({'msg': 200, 'result': 'ok'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def get_purchase_list(request):
	"""
	"""
	if request.method == 'POST':
		return JsonResponse({'msg': 200, 'result': 'ok'})
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
