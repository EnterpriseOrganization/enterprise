from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from enterprise.models import Purchase
from enterprise.models import Material
from enterprise.models import Supplier
from enterprise.models import SupplierMaterial
import datetime


@method_decorator(csrf_exempt)
def get_quotation_list(request):
	"""
	获取所有出价记录
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
			print(res)
			result.append(res)

		return JsonResponse({'msg': 200, 'result': result})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def add_quotation(request):
	"""
	增加
	"""
	if request.method == 'POST':
		params = request.POST
		# 得到所有参数
		material_id = params.get('material_id')
		material_name = params.get('material_id')
		supplier_id = params.get('supplier_id')
		price = params.get('price')
		# 只有所有参数都收到且不为空
		if material_id and material_name and supplier_id and price:
			sp = Supplier.objects.get(id=supplier_id)
			mt = Material.objects.get(id=material_id)
			sm = SupplierMaterial(price=price, material=mt, supplier=sp)
			sm.save()
			return JsonResponse({'msg': 200, 'result': 'success'})
		else:
			return JsonResponse({'msg': 'Incomplete parameters', 'result': 'null'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def delete_quotation(request):
	"""
	"""
	if request.method == 'POST':
		return JsonResponse({'msg': 200, 'result': 'ok'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def quotation_query(request):
	"""
	"""
	if request.method == 'POST':
		return JsonResponse({'msg': 200, 'result': 'ok'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def update_quotation_price(request):
	"""
	"""
	if request.method == 'POST':
		return JsonResponse({'msg': 200, 'result': 'ok'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def get_lack_list(request):
	"""
	"""
	if request.method == 'POST':
		return JsonResponse({'msg': 200, 'result': 'ok'})
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
