from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from enterprise.models import Purchase
from enterprise.models import Material
from enterprise.models import Supplier
from enterprise.models import SupplierMaterial
import datetime


def hello(request):
	res = {'title': 'hello', 'content': 'test'}
	return JsonResponse(res)


@method_decorator(csrf_exempt)
def get_quotation_list(request):
	"""
	get all quotations
	"""
	if request.method == 'POST':
		sms = SupplierMaterial.objects.select_related('supplier', 'material').all()
		# fileds = SupplierMaterial._meta.get_fields()
		print(sms)
		for sm in sms:
			print(sm.supplier)
			print(sm.material)
		result = list(sms)

		return JsonResponse({'msg': 200, 'result': 'ok'})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})


@method_decorator(csrf_exempt)
def history_list(request):
	if request.method == 'POST':
		params = request.POST
		dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		supplier = Supplier.objects.get(id=1)
		purchase = Purchase(purchaser='myh', date=dt, checker='leo', supplier=supplier)
		purchase.save()
		return JsonResponse({'msg':200})
	else:
		return JsonResponse({'msg': 'Please use POST', 'result': 'null'})
